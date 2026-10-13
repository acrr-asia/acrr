#!/usr/bin/env node
// Editorial pipeline for series: discovery, review freshness and the publication gate.
// Dependency-free, like the other scripts. See README "Series publication pipeline" and
// .claude/skills/complete-series/SKILL.md.
//
// Every answer is derived from the files in the repository, never from hidden state, so the
// pipeline can be stopped and resumed at any point and running a command twice changes nothing.
//
// A series review (reviews/<id>.md, written by .claude/skills/series-review/SKILL.md) is "current"
// when its "- Content hash:" line equals the hash of the series file and its English articles as
// they are now. `stamp` records that hash after the review's findings are resolved; any later edit
// to the series makes the review stale until the series is reviewed again and re-stamped.
//
// Usage:
//   node scripts/series-pipeline.mjs status [--json]   every series, its stage and what is missing
//   node scripts/series-pipeline.mjs hash <series-id>  content hash of the series file and its articles
//   node scripts/series-pipeline.mjs stamp <series-id> record the current hash in reviews/<id>.md
//   node scripts/series-pipeline.mjs gate [--json]     publication gate: exit 1 if a complete series
//                                                     has no current, resolved review
import { createHash } from 'node:crypto';
import { appendFileSync, existsSync, readFileSync, readdirSync, writeFileSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { listSeries } from './series-review.mjs';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const SERIES_DIR = 'src/content/series';
const REVIEWS_DIR = 'reviews';
const HASH_LINE = /^- Content hash: (sha256:[0-9a-f]{64})\s*$/m;

const read = (rel) => readFileSync(path.join(ROOT, rel), 'utf8').replace(/\r\n/g, '\n');

export function seriesIds() {
  return readdirSync(path.join(ROOT, SERIES_DIR))
    .filter((name) => /\.mdx?$/.test(name))
    .map((name) => name.replace(/\.mdx?$/, ''))
    .sort();
}

/** sha256 over the series file and its English articles (paths and contents, in a fixed order). */
export function contentHash(id) {
  const info = listSeries(id);
  const files = [info.file, ...info.articles.map((a) => a.path)].sort();
  const h = createHash('sha256');
  for (const f of files) h.update(`${f}\0${read(f)}\0`);
  return `sha256:${h.digest('hex')}`;
}

/** What the review report says, as far as the pipeline needs it. */
export function reviewState(id) {
  const rel = `${REVIEWS_DIR}/${id}.md`;
  if (!existsSync(path.join(ROOT, rel))) return { path: rel, exists: false };
  const text = read(rel);
  const counts = /Findings:\s*(\d+)\s*blocking,\s*(\d+)\s*should fix/i.exec(text);
  const blocking = counts ? Number(counts[1]) : null;
  const shouldFix = counts ? Number(counts[2]) : null;
  const resolved = /^## Resolution\b/m.test(text);
  return {
    path: rel,
    exists: true,
    hash: HASH_LINE.exec(text)?.[1] ?? null,
    blocking,
    shouldFix,
    resolved,
    hasVerificationLog: /^## Verification log\b/m.test(text),
    // A report with blocking or should-fix findings counts only once its Resolution says they were applied.
    clean: counts !== null && (blocking + shouldFix === 0 || resolved),
  };
}

/**
 * Stages, in pipeline order:
 *   needs-writing   planned entries remain, or the series is not marked published
 *   needs-review    complete, but no review report
 *   needs-fixes     report exists but its blocking/should-fix findings are not resolved
 *   review-stale    report resolved, but the series changed since it was stamped (or never stamped)
 *   ready           complete, reviewed, resolved and current: may be published
 */
export function seriesStatus(id) {
  const info = listSeries(id);
  const review = reviewState(id);
  const hash = contentHash(id);
  // An unfinished series may legitimately have no articles yet; everything else is structural.
  const structural = info.warnings.filter(
    (w) => !w.startsWith('The series is not complete') && !(w === 'The series has no articles.' && !info.complete),
  );
  let stage;
  if (!info.complete) stage = 'needs-writing';
  else if (!review.exists) stage = 'needs-review';
  else if (!review.clean || !review.hasVerificationLog) stage = 'needs-fixes';
  else if (review.hash !== hash) stage = 'review-stale';
  else stage = 'ready';
  return {
    id,
    title: info.title,
    status: info.status,
    planned: info.planned,
    articles: info.articles.length,
    stage,
    structuralWarnings: structural,
    hash,
    review,
  };
}

export function gate() {
  const rows = seriesIds().map(seriesStatus);
  const failures = [];
  for (const s of rows) {
    // Structural problems (gaps or duplicates in seriesOrder, drafts) block any series.
    for (const w of s.structuralWarnings) failures.push(`${s.id}: ${w}`);
    // A complete series is published as a whole, so it must carry a current, resolved review.
    if (s.stage !== 'ready' && s.stage !== 'needs-writing') {
      const why = {
        'needs-review': `no review report (${s.review.path}); run /series-review ${s.id}`,
        'needs-fixes': `review findings are not resolved in ${s.review.path} (or the report lacks its Verification log)`,
        'review-stale': s.review.hash
          ? `the series changed after its review was stamped (${s.review.path}); review it again, then run "node scripts/series-pipeline.mjs stamp ${s.id}"`
          : `the review in ${s.review.path} was never stamped; run "node scripts/series-pipeline.mjs stamp ${s.id}" after confirming it covers the current text`,
      }[s.stage];
      failures.push(`${s.id}: ${why}`);
    }
  }
  return { ok: failures.length === 0, failures, rows };
}

function stamp(id) {
  const s = seriesStatus(id);
  if (!s.review.exists) throw new Error(`${s.review.path} does not exist; run the series review first.`);
  if (s.stage === 'needs-writing') throw new Error(`${id} is not complete (stage needs-writing).`);
  if (!s.review.clean) throw new Error(`${s.review.path} has unresolved blocking or should-fix findings (no "## Resolution" section).`);
  if (!s.review.hasVerificationLog) throw new Error(`${s.review.path} has no "## Verification log" section.`);
  let text = read(s.review.path);
  const line = `- Content hash: ${s.hash}`;
  if (HASH_LINE.test(text)) text = text.replace(HASH_LINE, line);
  else {
    // Insert after the header bullet list (the first block of "- " lines after the title).
    const lines = text.split('\n');
    let i = lines.findIndex((l) => l.startsWith('- '));
    if (i < 0) throw new Error(`${s.review.path} has no header list to add the hash to.`);
    while (i < lines.length && lines[i].startsWith('- ')) i++;
    lines.splice(i, 0, line);
    text = lines.join('\n');
  }
  writeFileSync(path.join(ROOT, s.review.path), text);
  return s.hash;
}

function table(rows) {
  const out = ['| Series | Status | Articles | Planned | Stage |', '|---|---|---|---|---|'];
  for (const r of rows) out.push(`| \`${r.id}\` | ${r.status} | ${r.articles} | ${r.planned} | ${r.stage} |`);
  return out.join('\n');
}

const [cmd, arg] = process.argv.slice(2);
const json = process.argv.includes('--json');
try {
  if (cmd === 'status') {
    const rows = seriesIds().map(seriesStatus);
    console.log(json ? JSON.stringify(rows, null, 2) : table(rows));
  } else if (cmd === 'hash' && arg) {
    console.log(contentHash(arg));
  } else if (cmd === 'stamp' && arg) {
    console.log(`Stamped ${REVIEWS_DIR}/${arg}.md with ${stamp(arg)}`);
  } else if (cmd === 'gate') {
    const result = gate();
    const report = [
      `## Publication gate: ${result.ok ? 'passed' : 'FAILED'}`,
      '',
      table(result.rows),
      '',
      ...(result.failures.length ? ['Failures:', '', ...result.failures.map((f) => `- ${f}`)] : ['No failures.']),
    ].join('\n');
    console.log(json ? JSON.stringify(result, null, 2) : report);
    if (process.env.GITHUB_STEP_SUMMARY) appendFileSync(process.env.GITHUB_STEP_SUMMARY, `${report}\n`);
    process.exit(result.ok ? 0 : 1);
  } else {
    console.error('Usage: node scripts/series-pipeline.mjs status [--json] | hash <id> | stamp <id> | gate [--json]');
    process.exit(2);
  }
} catch (err) {
  console.error(err.message);
  process.exit(1);
}
