#!/usr/bin/env node
// Helper for the series review workflow (see README "Automated series review" and
// .claude/skills/series-review/SKILL.md). Dependency-free, like the other scripts.
//
// A series is "complete" when its frontmatter has `status: "published"` and no
// `plannedEntries`. The review is triggered when a series *becomes* complete.
//
// Usage:
//   node scripts/series-review.mjs list <series-id>    the series and its articles in reading order (JSON)
//   node scripts/series-review.mjs detect <base> <head> ids of series that became complete between two commits (JSON array)
//   node scripts/series-review.mjs hook                Claude Code PostToolUse hook: reads the hook JSON on stdin
import { readFileSync, readdirSync, existsSync, statSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const SERIES_DIR = 'src/content/series';
const BLOG_DIR = 'src/content/blog';
const SERIES_FILE = /^src\/content\/series\/([^/]+)\.mdx?$/;

function frontmatter(text) {
  const m = /^---\r?\n([\s\S]*?)\r?\n---/.exec(text ?? '');
  return m ? m[1] : '';
}

function field(fm, name) {
  const m = new RegExp(`^${name}:\\s*(.*)$`, 'm').exec(fm);
  if (!m) return undefined;
  return m[1].trim().replace(/^(["'])(.*)\1$/, '$2');
}

/** Number of `- title:` items under the top-level `plannedEntries:` key. */
function plannedCount(fm) {
  const lines = fm.split(/\r?\n/);
  const start = lines.findIndex((l) => /^plannedEntries:/.test(l));
  if (start < 0 || /^plannedEntries:\s*\[\s*\]\s*$/.test(lines[start])) return 0;
  let count = 0;
  for (const line of lines.slice(start + 1)) {
    if (/^\S/.test(line) && !line.startsWith('#')) break; // next top-level key
    if (/^\s*-\s+title:/.test(line)) count++;
  }
  return count;
}

export function seriesState(text) {
  const fm = frontmatter(text);
  const status = field(fm, 'status') ?? 'planned';
  const planned = plannedCount(fm);
  return { title: field(fm, 'title'), status, planned, complete: status === 'published' && planned === 0 };
}

function git(args) {
  return execFileSync('git', args, { cwd: ROOT, encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] });
}

function gitShow(rev, file) {
  try {
    return git(['show', `${rev}:${file}`]);
  } catch {
    return null; // file absent at that revision
  }
}

function isCommit(rev) {
  if (!rev || /^0+$/.test(rev)) return false;
  try {
    git(['cat-file', '-e', `${rev}^{commit}`]);
    return true;
  } catch {
    return false;
  }
}

function walk(dir) {
  const abs = path.join(ROOT, dir);
  if (!existsSync(abs)) return [];
  return readdirSync(abs).flatMap((name) => {
    const rel = `${dir}/${name}`;
    return statSync(path.join(ROOT, rel)).isDirectory() ? walk(rel) : /\.mdx?$/.test(name) ? [rel] : [];
  });
}

export function listSeries(id) {
  const file = ['md', 'mdx'].map((ext) => `${SERIES_DIR}/${id}.${ext}`).find((f) => existsSync(path.join(ROOT, f)));
  if (!file) throw new Error(`No series file for id "${id}" in ${SERIES_DIR}`);
  const state = seriesState(readFileSync(path.join(ROOT, file), 'utf8'));
  const articles = walk(BLOG_DIR)
    .map((rel) => {
      const fm = frontmatter(readFileSync(path.join(ROOT, rel), 'utf8'));
      if (field(fm, 'series') !== id) return null;
      const order = Number(field(fm, 'seriesOrder'));
      return {
        order: Number.isFinite(order) ? order : null,
        title: field(fm, 'title'),
        path: rel,
        route: `/blog/${rel.slice(BLOG_DIR.length + 1).replace(/\.mdx?$/, '')}`,
        draft: field(fm, 'draft') === 'true',
      };
    })
    .filter(Boolean)
    .sort((a, b) => (a.order ?? Infinity) - (b.order ?? Infinity) || a.path.localeCompare(b.path));

  const warnings = [];
  if (articles.length === 0) warnings.push('The series has no articles.');
  articles.forEach((a, i) => {
    if (a.order === null) warnings.push(`${a.path} has no seriesOrder.`);
    else if (a.order !== i + 1) warnings.push(`${a.path} has seriesOrder ${a.order}; expected ${i + 1} (gap or duplicate).`);
    if (a.draft) warnings.push(`${a.path} is a draft and is not published.`);
  });
  if (!state.complete) warnings.push(`The series is not complete (status "${state.status}", ${state.planned} planned entries).`);
  return { id, file, ...state, articles, warnings };
}

export function detect(base, head = 'HEAD') {
  if (!isCommit(head)) throw new Error(`Not a commit: ${head}`);
  // A new branch or a force push has no usable "before"; compare with the parent instead.
  const from = isCommit(base) ? base : isCommit(`${head}^`) ? `${head}^` : null;
  const files = from
    ? git(['diff', '--name-only', from, head, '--', SERIES_DIR]).split('\n').filter(Boolean)
    : git(['ls-tree', '--name-only', head, `${SERIES_DIR}/`]).split('\n').filter(Boolean);
  const ids = [];
  for (const file of files) {
    const m = SERIES_FILE.exec(file);
    if (!m) continue;
    const now = gitShow(head, file);
    if (!now || !seriesState(now).complete) continue;
    const before = from ? gitShow(from, file) : null;
    if (!before || !seriesState(before).complete) ids.push(m[1]);
  }
  return ids;
}

function hook() {
  let input;
  try {
    input = JSON.parse(readFileSync(0, 'utf8'));
  } catch {
    return; // not hook input; stay silent
  }
  const abs = input?.tool_input?.file_path;
  if (typeof abs !== 'string') return;
  const projectDir = process.env.CLAUDE_PROJECT_DIR || input.cwd || ROOT;
  const rel = path.relative(projectDir, abs).split(path.sep).join('/');
  const m = SERIES_FILE.exec(rel);
  if (!m || !existsSync(abs)) return;

  if (!seriesState(readFileSync(abs, 'utf8')).complete) return;
  const committed = gitShow('HEAD', rel);
  if (committed && seriesState(committed).complete) return; // already complete before this edit

  const info = listSeries(m[1]);
  const lines = [
    `The series "${info.title}" (${rel}) has just become complete: status "published" with no planned entries, ${info.articles.length} article(s).`,
    `This project runs a comprehensive series review when a series is completed. The procedure is in .claude/skills/series-review/SKILL.md (invoked as /series-review ${m[1]}); it writes its report to reviews/${m[1]}.md.`,
    'The review is expected before the change is committed or published, unless the user has said otherwise.',
  ];
  if (info.warnings.length) lines.push(`Series checks: ${info.warnings.join(' ')}`);
  process.stdout.write(
    JSON.stringify({ hookSpecificOutput: { hookEventName: 'PostToolUse', additionalContext: lines.join('\n') } }),
  );
}

const [cmd, ...args] = process.argv.slice(2);
try {
  if (cmd === 'list' && args[0]) {
    console.log(JSON.stringify(listSeries(args[0]), null, 2));
  } else if (cmd === 'detect') {
    console.log(JSON.stringify(detect(args[0], args[1] ?? 'HEAD')));
  } else if (cmd === 'hook') {
    hook();
  } else {
    console.error('Usage: node scripts/series-review.mjs list <series-id> | detect <base> [head] | hook');
    process.exit(2);
  }
} catch (err) {
  if (cmd === 'hook') process.exit(0); // a hook must never break the edit that triggered it
  console.error(err.message);
  process.exit(1);
}
