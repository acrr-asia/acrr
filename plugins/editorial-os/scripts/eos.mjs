#!/usr/bin/env node
// Editorial OS (EOS): the deterministic half of the editorial workflow.
//
// It reads a publication's configuration (eos.config.json), discovers its content, and answers the
// questions that do not need judgment: what exists, which mechanical style and structure rules a
// file breaks, whether cross-references point where they say, whether a file has a current,
// passing editorial review record, and whether the built site has rendering and accessibility
// defects. The judgment-intensive stages (developmental, copy, fact-checking, technical, series and
// QA review) are skills and agents in this plugin; they record their outcome with `eos record`,
// and `eos gate` refuses publication until every published item carries a current, passing record.
//
// Dependency-free (Node >= 18). Every answer is derived from the files, never from hidden state, so
// any command can be re-run at any time and running it twice changes nothing.
//
// Usage: node eos.mjs <command> [options]   (run `node eos.mjs help` for the list)

import { createHash } from 'node:crypto';
import { execSync } from 'node:child_process';
import { appendFileSync, existsSync, mkdirSync, readFileSync, readdirSync, statSync, writeFileSync, copyFileSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const PLUGIN_ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const VERSION = JSON.parse(readFileSync(path.join(PLUGIN_ROOT, '.claude-plugin', 'plugin.json'), 'utf8')).version;
const SEVERITIES = ['error', 'warning', 'suggestion'];
const DIMENSIONS = ['purpose', 'structure', 'accuracy', 'evidence', 'language', 'consistency', 'publishing'];
const ORDINALS = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth'];

// ---------------------------------------------------------------------------------------------
// Arguments and configuration
// ---------------------------------------------------------------------------------------------

function parseArgs(argv) {
  const args = { _: [] };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a.startsWith('--')) {
      const [k, v] = a.slice(2).split(/=(.*)/s);
      if (v !== undefined) args[k] = v;
      else if (i + 1 < argv.length && !argv[i + 1].startsWith('--')) args[k] = argv[++i];
      else args[k] = true;
    } else args._.push(a);
  }
  return args;
}

function findUp(start, names) {
  let dir = path.resolve(start);
  for (;;) {
    for (const n of names) if (existsSync(path.join(dir, n))) return path.join(dir, n);
    const parent = path.dirname(dir);
    if (parent === dir) return null;
    dir = parent;
  }
}

/** Locate and load the publication config. Paths in it are relative to the project root. */
export function loadConfig(explicit) {
  const start = process.env.CLAUDE_PROJECT_DIR || process.cwd();
  const file = explicit
    ? path.resolve(explicit)
    : process.env.EOS_CONFIG
      ? path.resolve(process.env.EOS_CONFIG)
      : findUp(start, ['editorial/eos.config.json', 'eos.config.json', '.editorial/eos.config.json']);
  if (!file || !existsSync(file)) {
    throw new EosError(
      'No eos.config.json found. Run "node <plugin>/scripts/eos.mjs init" in the project root, or pass --config <file>.',
      2,
    );
  }
  const cfg = JSON.parse(readFileSync(file, 'utf8'));
  const marker = findUp(path.dirname(file), ['package.json', '.git']);
  const root = path.resolve(marker ? path.dirname(marker) : path.dirname(file), cfg.content?.root ?? '.');
  cfg.rules = { ...defaultRules(), ...(cfg.rules ?? {}) };
  cfg.thresholds = {
    titleMaxChars: 70, descriptionMinChars: 70, descriptionMaxChars: 165, sentenceMaxWords: 45,
    paragraphMaxWords: 170, headingMaxWords: 12, ...(cfg.thresholds ?? {}),
  };
  cfg.content.fields = {
    title: 'title', description: 'description', published: 'publishedAt', updated: 'updatedAt', series: 'series',
    seriesOrder: 'seriesOrder', draft: 'draft', example: 'example', status: 'status', plannedEntries: 'plannedEntries',
    ...(cfg.content.fields ?? {}),
  };
  cfg.review = {
    recordsDir: 'editorial/records', auditDir: 'editorial/audit', minimumPerDimension: 3, minimumTotal: {},
    requiredStages: {}, ...(cfg.review ?? {}),
  };
  const glossaryFile = cfg.glossary ? path.resolve(root, cfg.glossary) : null;
  cfg._glossary = glossaryFile && existsSync(glossaryFile)
    ? JSON.parse(readFileSync(glossaryFile, 'utf8'))
    : { terms: [], phrases: [], intensifiers: [] };
  cfg._file = file;
  cfg._root = root;
  return cfg;
}

function defaultRules() {
  return {
    'spelling-variant': 'warning', terminology: 'warning', phrases: 'warning', intensifiers: 'suggestion',
    contractions: 'off', 'doubled-word': 'error', 'serial-comma': 'suggestion', placeholder: 'error', 'sentence-length': 'suggestion',
    'paragraph-length': 'suggestion', exclamation: 'warning', 'heading-levels': 'error', 'heading-case': 'off',
    'heading-numbering': 'warning', 'heading-punctuation': 'warning', 'heading-duplicate': 'warning',
    'heading-length': 'suggestion', 'title-length': 'warning', 'description-length': 'warning',
    'description-form': 'warning', 'required-fields': 'error', 'required-sections': 'error', 'series-sections': 'off',
    'opening-paragraph': 'warning', 'internal-link': 'error', 'series-crossref': 'error', 'section-reference': 'warning',
    'link-text': 'warning', 'math-balance': 'error', 'acronym-expansion': 'off', 'reference-format': 'off',
  };
}

class EosError extends Error {
  constructor(message, code = 1) {
    super(message);
    this.code = code;
  }
}

// ---------------------------------------------------------------------------------------------
// Files
// ---------------------------------------------------------------------------------------------

function globToRegex(glob) {
  let re = '';
  for (let i = 0; i < glob.length; i++) {
    const c = glob[i];
    if (c === '*' && glob[i + 1] === '*') {
      re += glob[i + 2] === '/' ? '(?:.*/)?' : '.*';
      i += glob[i + 2] === '/' ? 2 : 1;
    } else if (c === '*') re += '[^/]*';
    else if (c === '?') re += '[^/]';
    else if (c === '{') {
      const end = glob.indexOf('}', i);
      re += `(?:${glob.slice(i + 1, end).split(',').map(escapeRe).join('|')})`;
      i = end;
    } else re += escapeRe(c);
  }
  return new RegExp(`^${re}$`);
}

const escapeRe = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
const SKIP_DIRS = new Set(['node_modules', '.git', '.astro', '.next', '.cache']);

function walk(root, dir = '', out = []) {
  for (const name of readdirSync(path.join(root, dir))) {
    if (SKIP_DIRS.has(name)) continue;
    const rel = dir ? `${dir}/${name}` : name;
    const st = statSync(path.join(root, rel));
    if (st.isDirectory()) walk(root, rel, out);
    else out.push(rel);
  }
  return out;
}

let fileCache = null;
function projectFiles(cfg) {
  if (!fileCache) fileCache = walk(cfg._root);
  return fileCache;
}

const readText = (abs) => readFileSync(abs, 'utf8').replace(/\r\n/g, '\n');
const hashText = (text) => `sha256:${createHash('sha256').update(text.replace(/\r\n/g, '\n')).digest('hex')}`;

function gitHead(root) {
  try {
    return execSync('git rev-parse --short HEAD', { cwd: root, stdio: ['ignore', 'pipe', 'ignore'] }).toString().trim();
  } catch {
    return null;
  }
}

// ---------------------------------------------------------------------------------------------
// Front matter (a YAML subset: scalars, quoted strings, lists of scalars, lists of flat objects)
// ---------------------------------------------------------------------------------------------

function parseScalar(raw) {
  const v = raw.trim();
  if (v === '') return '';
  if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) {
    return v.startsWith('"') ? v.slice(1, -1).replace(/\\"/g, '"').replace(/\\\\/g, '\\') : v.slice(1, -1).replace(/''/g, "'");
  }
  if (v === 'true') return true;
  if (v === 'false') return false;
  if (/^-?\d+(\.\d+)?$/.test(v)) return Number(v);
  if (v === '[]') return [];
  return v;
}

export function parseFrontmatter(text) {
  if (!text.startsWith('---\n')) return { data: {}, end: 0, endLine: 0, spans: {} };
  const close = text.indexOf('\n---', 3);
  if (close < 0) return { data: {}, end: 0, endLine: 0, spans: {} };
  const block = text.slice(4, close);
  const end = text.indexOf('\n', close + 1) + 1 || text.length;
  const data = {};
  const spans = {}; // field -> [{start, end, line}] character spans of prose values (title, description, list items)
  let key = null;
  let offset = 4;
  let lineNo = 2;
  for (const line of block.split('\n')) {
    const top = /^([A-Za-z_][\w-]*):\s*(.*)$/.exec(line);
    const item = /^\s+-\s+(.*)$/.exec(line);
    const nested = /^\s+([A-Za-z_][\w-]*):\s*(.*)$/.exec(line);
    if (top) {
      key = top[1];
      if (top[2] === '') data[key] = [];
      else {
        data[key] = parseScalar(top[2]);
        const valStart = offset + line.indexOf(top[2]);
        (spans[key] ??= []).push({ start: valStart, end: valStart + top[2].length, line: lineNo });
      }
    } else if (item && key) {
      if (!Array.isArray(data[key])) data[key] = [];
      const objStart = /^([A-Za-z_][\w-]*):\s*(.*)$/.exec(item[1]);
      if (objStart) data[key].push({ [objStart[1]]: parseScalar(objStart[2]) });
      else {
        data[key].push(parseScalar(item[1]));
        const valStart = offset + line.indexOf(item[1]);
        (spans[key] ??= []).push({ start: valStart, end: valStart + item[1].length, line: lineNo });
      }
    } else if (nested && key && Array.isArray(data[key]) && data[key].length) {
      const last = data[key][data[key].length - 1];
      if (last && typeof last === 'object') last[nested[1]] = parseScalar(nested[2]);
    }
    offset += line.length + 1;
    lineNo++;
  }
  return { data, end, endLine: lineNo, spans };
}

// ---------------------------------------------------------------------------------------------
// Prose masking: replace everything that is not reader-facing prose with spaces, keeping offsets
// and line numbers, so that rules never fire inside code, math, markup, URLs or front matter keys.
// ---------------------------------------------------------------------------------------------

export function maskProse(text, fm, proseFields = ['title', 'description', 'objectives']) {
  const chars = text.split('');
  const blank = (s, e) => {
    for (let i = s; i < e && i < chars.length; i++) if (chars[i] !== '\n') chars[i] = ' ';
  };
  const blankRe = (re, group) => {
    const src = chars.join('');
    for (const m of src.matchAll(re)) {
      if (group) {
        const g = m[group];
        if (g === undefined) continue;
        const s = m.index + m[0].indexOf(g);
        blank(s, s + g.length);
      } else blank(m.index, m.index + m[0].length);
    }
  };
  // Front matter: keep only the values of prose fields.
  if (fm.end) {
    const keep = [];
    for (const f of proseFields) for (const s of fm.spans[f] ?? []) keep.push(s);
    for (let i = 0; i < fm.end; i++) {
      if (chars[i] === '\n') continue;
      if (!keep.some((s) => i >= s.start && i < s.end)) chars[i] = ' ';
    }
    for (const s of keep) {
      // Drop the quotes around a quoted value.
      if (/["']/.test(chars[s.start])) chars[s.start] = ' ';
      if (/["']/.test(chars[s.end - 1])) chars[s.end - 1] = ' ';
    }
  }
  // Fenced code blocks (``` or ~~~), possibly indented inside JSX.
  {
    const lines = chars.join('').split('\n');
    let pos = 0;
    let fence = null;
    for (const line of lines) {
      const m = /^\s*(`{3,}|~{3,})/.exec(line);
      if (fence) {
        blank(pos, pos + line.length);
        if (m && m[1][0] === fence[0] && m[1].length >= fence.length && line.trim() === m[1]) fence = null;
      } else if (m) {
        fence = m[1];
        blank(pos, pos + line.length);
      }
      pos += line.length + 1;
    }
  }
  blankRe(/^(import|export)\s[^\n]*$/gm);
  blankRe(/<!--[\s\S]*?-->/g);
  blankRe(/\{\/\*[\s\S]*?\*\/\}/g);
  blankRe(/\$\$[\s\S]*?\$\$/g);
  blankRe(/\\\[[\s\S]*?\\\]/g);
  blankRe(/(?<![\\$])\$(?!\s)(?:[^$\n\\]|\\.)+?(?<!\s)\$(?!\d)/g);
  blankRe(/(`+)[^`\n]+?\1/g);
  blankRe(/<\/?[A-Za-z][^<>]*>/g);
  blankRe(/\{[^{}\n]*\}/g);
  blankRe(/\]\(([^)\s]+(?:\s+"[^"]*")?)\)/g, 1);
  blankRe(/^\s*\[[^\]]+\]:\s*\S+.*$/gm);
  blankRe(/https?:\/\/[^\s)>\]]+/g);
  return chars.join('');
}

function lineStarts(text) {
  const starts = [0];
  for (let i = 0; i < text.length; i++) if (text[i] === '\n') starts.push(i + 1);
  return starts;
}

function locate(starts, index) {
  let lo = 0;
  let hi = starts.length - 1;
  while (lo < hi) {
    const mid = (lo + hi + 1) >> 1;
    if (starts[mid] <= index) lo = mid;
    else hi = mid - 1;
  }
  return { line: lo + 1, col: index - starts[lo] + 1 };
}

// ---------------------------------------------------------------------------------------------
// Spelling variants
// ---------------------------------------------------------------------------------------------

let variantCache = null;
function spellingMap(variant) {
  if (variantCache?.variant === variant) return variantCache.map;
  const data = JSON.parse(readFileSync(path.join(PLUGIN_ROOT, 'data', 'spelling-variants.json'), 'utf8'));
  const pairs = [];
  for (const stem of data.ize) {
    for (const [gb, us] of [['ise', 'ize'], ['ises', 'izes'], ['ised', 'ized'], ['ising', 'izing'], ['isation', 'ization'],
      ['isations', 'izations'], ['iser', 'izer'], ['isers', 'izers'], ['isable', 'izable'], ['isational', 'izational']]) {
      pairs.push([stem + gb, stem + us, false]);
    }
  }
  for (const stem of data.yse) {
    for (const [gb, us] of [['yse', 'yze'], ['ysed', 'yzed'], ['ysing', 'yzing'], ['yser', 'yzer'], ['ysers', 'yzers']]) {
      pairs.push([stem + gb, stem + us, false]);
    }
  }
  for (const stem of data.our) {
    for (const suf of ['', 's', 'ed', 'ing', 'al', 'ally', 'able', 'ably', 'ite', 'ites', 'ful', 'less', 'ism', 'er', 'ers']) {
      pairs.push([`${stem}our${suf}`, `${stem}or${suf}`, false]);
    }
  }
  for (const stem of data.re) {
    for (const suf of ['', 's']) pairs.push([`${stem}re${suf}`, `${stem}er${suf}`, false]);
  }
  for (const [gb, us, oneWay] of data.words) pairs.push([gb, us, oneWay === 'oneWay']);
  const map = new Map();
  for (const [gb, us, oneWay] of pairs) {
    if (variant === 'en-US') map.set(gb.toLowerCase(), us);
    else if (variant === 'en-GB' && !oneWay) map.set(us.toLowerCase(), gb);
  }
  // A word spelled the same way in both variants must never be "corrected".
  for (const [gb, us] of pairs) if (gb.toLowerCase() === us.toLowerCase()) map.delete(gb.toLowerCase());
  variantCache = { variant, map };
  return map;
}

function matchCase(original, replacement) {
  if (original === original.toUpperCase() && original.length > 1) return replacement.toUpperCase();
  if (original[0] === original[0].toUpperCase()) return replacement[0].toUpperCase() + replacement.slice(1);
  return replacement;
}

// ---------------------------------------------------------------------------------------------
// Documents
// ---------------------------------------------------------------------------------------------

/** Every content item the config describes: path, type, slug, route, front matter, text. */
export function discover(cfg) {
  const files = projectFiles(cfg);
  const exclude = (cfg.content.exclude ?? []).map(globToRegex);
  const items = [];
  for (const [type, def] of Object.entries(cfg.content.types)) {
    const res = def.globs.map(globToRegex);
    for (const rel of files) {
      if (!res.some((r) => r.test(rel)) || exclude.some((r) => r.test(rel))) continue;
      const text = readText(path.join(cfg._root, rel));
      const fm = parseFrontmatter(text);
      const slug = path.basename(rel).replace(/\.[^.]+$/, '');
      const f = cfg.content.fields;
      items.push({
        id: `${type}/${slug}`,
        type,
        def,
        path: rel,
        slug,
        route: def.route ? def.route.replace('{slug}', slug) : null,
        text,
        fm,
        data: fm.data,
        title: fm.data[f.title] ?? slug,
        draft: fm.data[f.draft] === true,
        example: fm.data[f.example] === true,
        series: def.isSeriesIndex ? null : (fm.data[f.series] ?? null),
        seriesOrder: fm.data[f.seriesOrder] ?? null,
        hash: hashText(text),
      });
    }
  }
  items.sort((a, b) => a.path.localeCompare(b.path));
  // Series membership, so rules can check cross-references between entries.
  const series = new Map();
  for (const it of items) {
    if (it.def.isSeriesIndex) series.set(it.slug, { index: it, entries: [] });
  }
  for (const it of items) {
    if (it.series && !it.draft) {
      if (!series.has(it.series)) series.set(it.series, { index: null, entries: [] });
      series.get(it.series).entries.push(it);
    }
  }
  for (const s of series.values()) s.entries.sort((a, b) => (a.seriesOrder ?? 0) - (b.seriesOrder ?? 0));
  return {
    items,
    series,
    root: cfg._root,
    byRoute: new Map(items.filter((i) => i.route).map((i) => [i.route, i])),
    prefixRoutes: cfg.content.pages?.prefixes ?? [],
  };
}

function headingsOf(text, masked) {
  const out = [];
  const lines = text.split('\n');
  const mlines = masked.split('\n');
  for (let i = 0; i < lines.length; i++) {
    // A heading line survives masking (its # marks are not code); inline code inside it may not.
    const m = /^(#{1,6})\s+(.+?)\s*#*\s*$/.exec(lines[i]);
    if (m && /^#{1,6}\s/.test(mlines[i])) {
      const num = /^(\d+(?:\.\d+)*)\.?\s+(.*)$/.exec(m[2]);
      out.push({ level: m[1].length, text: m[2], number: num ? num[1] : null, bare: num ? num[2] : m[2], line: i + 1 });
    }
  }
  return out;
}

function proseWords(masked) {
  return masked.replace(/^#{1,6}\s.*$/gm, ' ').match(/[A-Za-z][A-Za-z'’-]*/g)?.length ?? 0;
}

// ---------------------------------------------------------------------------------------------
// Lint
// ---------------------------------------------------------------------------------------------

export function lintItem(cfg, item, site) {
  const issues = [];
  const { text } = item;
  const fm = item.fm;
  const masked = maskProse(text, fm, cfg.content.proseFields ?? ['title', 'description', 'objectives']);
  const starts = lineStarts(text);
  const sev = (rule) => cfg.rules[rule] ?? 'off';
  const add = (rule, index, message, extra = {}) => {
    const s = extra.severity ?? sev(rule);
    if (s === 'off') return;
    const at = typeof index === 'number' ? locate(starts, index) : { line: index.line, col: 1 };
    issues.push({ rule, severity: s, line: at.line, col: at.col, message, ...extra, severity: s });
  };
  const f = cfg.content.fields;
  const bodyStart = fm.end;
  const isBody = (idx) => idx >= bodyStart;

  // --- front matter ---
  const required = item.def.requiredFields ?? (item.def.isSeriesIndex ? [f.title, f.description] : [f.title, f.description, f.published]);
  for (const k of required) {
    if (item.data[k] === undefined || item.data[k] === '') add('required-fields', { line: 1 }, `Missing front-matter field "${k}".`);
  }
  const title = String(item.data[f.title] ?? '');
  const desc = String(item.data[f.description] ?? '');
  const titleLine = fm.spans[f.title]?.[0]?.line ?? 1;
  const descLine = fm.spans[f.description]?.[0]?.line ?? 1;
  if (title.length > cfg.thresholds.titleMaxChars) {
    add('title-length', { line: titleLine }, `Title is ${title.length} characters (limit ${cfg.thresholds.titleMaxChars}); search results and cards truncate it.`);
  }
  if (desc) {
    if (desc.length > cfg.thresholds.descriptionMaxChars) {
      add('description-length', { line: descLine }, `Description is ${desc.length} characters (aim for ${cfg.thresholds.descriptionMinChars}-${cfg.thresholds.descriptionMaxChars}); it is the meta description and card summary, and search engines truncate it.`);
    } else if (desc.length < cfg.thresholds.descriptionMinChars) {
      add('description-length', { line: descLine }, `Description is ${desc.length} characters (aim for ${cfg.thresholds.descriptionMinChars}-${cfg.thresholds.descriptionMaxChars}); too short to tell a reader what the page covers.`);
    }
    if (/^(this|in this) (article|entry|post|page|series|insight|note)\b/i.test(desc)) {
      add('description-form', { line: descLine }, 'Description opens with "This article/entry..."; start with the subject itself.');
    }
    if (!/[.?!]$/.test(desc.trim())) add('description-form', { line: descLine }, 'Description should be a complete sentence ending with a full stop.');
  }

  // --- headings ---
  const heads = headingsOf(text, masked).filter((h) => h.line > fm.endLine);
  let prev = 1;
  for (const h of heads) {
    if (h.level === 1) add('heading-levels', { line: h.line }, 'Level-1 heading in the body; the page title is the only h1.');
    else if (h.level > prev + 1 && prev >= 1) add('heading-levels', { line: h.line }, `Heading jumps from level ${prev} to level ${h.level}.`);
    prev = h.level;
    const words = h.bare.split(/\s+/);
    if (words.length > cfg.thresholds.headingMaxWords) add('heading-length', { line: h.line }, `Heading has ${words.length} words; headings should be short labels.`);
    if (/[.:;,]$/.test(h.bare)) add('heading-punctuation', { line: h.line }, 'Heading ends with punctuation.');
    if (cfg.language?.headingCase === 'sentence') {
      const phrases = (cfg.properNouns ?? []).filter((n) => n.includes(' '));
      const caseWords = phrases.reduce((t, n) => t.split(n).join(' '), h.bare).split(/\s+/).filter(Boolean);
      const rest = (h.bare.startsWith(caseWords[0] ?? '') ? caseWords.slice(1) : caseWords).map((w) => w.replace(/[^\p{L}\p{N}-]/gu, '')).filter(Boolean);
      const titled = rest.filter((w) => w.length >= 4 && /^\p{Lu}\p{Ll}+$/u.test(w) && !(cfg.properNouns ?? []).includes(w));
      const lower = rest.filter((w) => w.length >= 4 && /^\p{Ll}/u.test(w));
      if ((titled.length >= 2 && titled.length > lower.length) || (titled.length >= 1 && lower.length === 0)) {
        add('heading-case', { line: h.line }, `Heading looks like title case ("${h.bare}"); the house style is sentence case (capitalize only the first word and proper nouns).`);
      }
    }
  }
  const seen = new Map();
  for (const h of heads) {
    const k = `${h.level}:${h.bare.toLowerCase()}`;
    if (seen.has(k) && !['exercises', 'solutions', 'answers', 'example', 'examples'].includes(h.bare.toLowerCase())) {
      add('heading-duplicate', { line: h.line }, `Duplicate heading "${h.bare}" (also line ${seen.get(k)}); links to it are ambiguous.`);
    } else seen.set(k, h.line);
  }
  const exempt = new Set(['references', 'further reading', 'acknowledgments', 'acknowledgements', 'appendix', 'notes']);
  const h2 = heads.filter((h) => h.level === 2 && !exempt.has(h.bare.toLowerCase()));
  const numbered = h2.filter((h) => h.number);
  if (numbered.length && numbered.length !== h2.length) {
    for (const h of h2.filter((x) => !x.number)) add('heading-numbering', { line: h.line }, `Unnumbered section "${h.bare}" in an article whose other sections are numbered.`);
  }
  if (numbered.length) {
    let expect = 1;
    let parent = null;
    let sub = 0;
    for (const h of heads) {
      if (h.level === 2 && h.number) {
        if (h.number !== String(expect)) add('heading-numbering', { line: h.line }, `Section number ${h.number}, expected ${expect}.`);
        expect = Number(h.number.split('.')[0]) + 1;
        parent = h.number;
        sub = 0;
      } else if (h.level === 3 && h.number && parent) {
        sub++;
        if (h.number !== `${parent}.${sub}`) add('heading-numbering', { line: h.line }, `Subsection number ${h.number}, expected ${parent}.${sub}.`);
        sub = Number(h.number.split('.')[1] ?? sub);
      }
    }
  }

  // --- required sections ---
  const bareSet = heads.map((h) => h.bare.toLowerCase());
  for (const name of item.def.requiredSections ?? []) {
    if (!heads.some((h) => h.level === 2 && h.bare.toLowerCase() === name.toLowerCase())) {
      add('required-sections', { line: fm.endLine }, `Missing required section "## ${name}".`);
    }
  }
  if (item.series && cfg.content.seriesArticle?.requiredSections) {
    for (const name of cfg.content.seriesArticle.requiredSections) {
      if (!bareSet.includes(name.toLowerCase())) add('series-sections', { line: fm.endLine }, `Series article has no "${name}" section.`);
    }
  }
  if (!item.def.isSeriesIndex && heads.length) {
    const before = masked.slice(bodyStart, starts[heads[0].line - 1]);
    if (!/[A-Za-z]{3,}/.test(before)) add('opening-paragraph', { line: heads[0].line }, 'No introduction before the first heading; open with what the piece covers and for whom.');
  }

  // --- prose rules ---
  // Cited titles keep the spelling of the work they name, so reference lists are exempt.
  const refLines = new Set(referencesOf(cfg, item).map((r) => r.line));
  const inRefs = (idx) => refLines.has(locate(starts, idx).line);
  const map = cfg.language?.variant ? spellingMap(cfg.language.variant) : new Map();
  for (const m of masked.matchAll(/[A-Za-z]+(?:[-'][A-Za-z]+)*/g)) {
    if (inRefs(m.index)) continue;
    const w = m[0];
    const lw = w.toLowerCase();
    if (map.has(lw)) {
      add('spelling-variant', m.index, `"${w}" is not ${cfg.language.variant} spelling; use "${matchCase(w, map.get(lw))}".`, { match: w, fix: matchCase(w, map.get(lw)) });
    }
  }
  for (const m of masked.matchAll(/\bper cent\b/gi)) {
    if (cfg.language?.variant === 'en-US') add('spelling-variant', m.index, '"per cent" is British; use "percent".', { match: m[0], fix: 'percent' });
  }
  for (const term of cfg._glossary.terms ?? []) {
    for (const pat of term.avoid ?? []) {
      const re = new RegExp(pat, term.caseSensitive ? 'g' : 'gi');
      for (const m of masked.matchAll(re)) {
        if ((term.scope === 'body' && !isBody(m.index)) || inRefs(m.index)) continue;
        add('terminology', m.index, `Use "${term.prefer}" instead of "${m[0]}".${term.note ? ` ${term.note}` : ''}`, { match: m[0], ...(term.replace !== undefined ? { fix: m[0].replace(new RegExp(pat, term.caseSensitive ? '' : 'i'), term.replace) } : {}) });
      }
    }
  }
  for (const p of cfg._glossary.phrases ?? []) {
    for (const m of masked.matchAll(new RegExp(p.avoid, 'gi'))) add('phrases', m.index, `"${m[0]}": ${p.message}`, { match: m[0], ...(p.severity && sev('phrases') !== 'off' ? { severity: p.severity } : {}) });
  }
  const intens = cfg._glossary.intensifiers ?? [];
  if (intens.length) {
    const re = new RegExp(`\\b(${intens.map(escapeRe).join('|')})\\b`, 'gi');
    for (const m of masked.matchAll(re)) if (isBody(m.index)) add('intensifiers', m.index, `"${m[0]}" rarely adds meaning; keep it only if the sentence is false without it.`, { match: m[0] });
  }
  if (cfg.language?.contractions === 'avoid') {
    const re = /\b(?:[A-Za-z]+n['’]t|it['’]s|that['’]s|there['’]s|here['’]s|what['’]s|let['’]s|who['’]s|where['’]s|[A-Za-z]+['’]re|[A-Za-z]+['’]ve|[A-Za-z]+['’]ll|I['’]m|(?:I|you|we|they|he|she|it)['’]d)\b/g;
    // A contraction joined by a hyphen is part of a compound term ("don't-care" in digital logic), not a contraction in prose.
    for (const m of masked.matchAll(re)) if (masked[m.index + m[0].length] !== '-') add('contractions', m.index, `Contraction "${m[0]}"; the house style writes it out in article prose.`, { match: m[0] });
  }
  if (cfg.language?.serialComma === false) {
    // "A, B, and C": a comma before the conjunction that closes a list of three or more short items.
    const re = /\b[\w-]+(?: [\w-]+){0,2}, [\w-]+(?: [\w-]+){0,2}, (?:and|or) [\w-]+/g;
    for (const m of masked.matchAll(re)) if (isBody(m.index) && !inRefs(m.index)) add('serial-comma', m.index + m[0].lastIndexOf(','), 'Serial comma before the last item of a list; the house style omits it.', { match: m[0] });
  }
  for (const m of masked.matchAll(/\b([A-Za-z]+)[ \t]+([A-Za-z]+)\b/g)) {
    const [, a, b] = m;
    if (a.toLowerCase() !== b.toLowerCase() || ['that', 'had'].includes(a.toLowerCase())) continue;
    if ((a === a.toUpperCase()) !== (b === b.toUpperCase()) && a.length > 1) continue; // "AND and": an operator name, then a word
    if (!/^[A-Za-z]+\s+[A-Za-z]+$/.test(text.slice(m.index, m.index + m[0].length))) continue; // something was masked between them
    add('doubled-word', m.index, `Repeated word "${a} ${b}".`, { match: m[0] });
  }
  for (const m of masked.matchAll(/\b(TODO|TBD|FIXME|XXX)\b|lorem ipsum/gi)) add('placeholder', m.index, `Placeholder text "${m[0]}".`, { match: m[0] });
  for (const m of masked.matchAll(/[A-Za-z)]!(?=\s|$)/g)) if (isBody(m.index)) add('exclamation', m.index, 'Exclamation mark in prose.');

  // Sentences and paragraphs (body prose only; tables, lists of fragments and headings excluded).
  const paras = [];
  {
    let cur = null;
    const lines = masked.split('\n');
    let pos = 0;
    for (const line of lines) {
      const isProse = pos >= bodyStart && /\S/.test(line) && !/^\s*(#|\||[-*+]\s|\d+\.\s|>)/.test(line);
      if (isProse) {
        if (!cur) cur = { start: pos, text: '' };
        cur.text += `${line} `;
      } else if (cur) {
        paras.push(cur);
        cur = null;
      }
      pos += line.length + 1;
    }
    if (cur) paras.push(cur);
  }
  for (const p of paras) {
    const words = p.text.match(/[A-Za-z0-9][\w'’-]*/g) ?? [];
    if (words.length > cfg.thresholds.paragraphMaxWords) add('paragraph-length', p.start, `Paragraph of ${words.length} words; split it where the topic shifts.`);
    const sentences = p.text.replace(/\b(e\.g|i\.e|cf|vs|et al|Fig|Eq|Sec|No|approx|resp)\./g, '$1').split(/(?<=[.?!])\s+(?=[A-Z(“"])/);
    let offset = 0;
    for (const s of sentences) {
      const n = (s.match(/[A-Za-z0-9][\w'’-]*/g) ?? []).length;
      if (n > cfg.thresholds.sentenceMaxWords) {
        const idx = p.text.indexOf(s.slice(0, 20), offset);
        add('sentence-length', p.start + Math.max(0, idx), `Sentence of ${n} words; consider splitting it.`);
      }
      offset += s.length;
    }
  }

  // --- math ---
  const noCode = maskCodeOnly(text);
  const dollars = (noCode.slice(bodyStart).match(/\$\$/g) ?? []).length;
  if (dollars % 2) add('math-balance', { line: fm.endLine }, 'Unbalanced $$ display-math delimiters.');

  // --- links ---
  for (const m of text.matchAll(/(?<!!)\[([^\]]*)\]\(([^)\s]+)(?:\s+"[^"]*")?\)/g)) {
    if (!isBody(m.index) || isInCode(noCode, m.index)) continue;
    const [, label, href] = m;
    if (/^(here|this|this link|click here|link|read more|more)$/i.test(label.trim())) add('link-text', m.index, `Link text "${label}" does not say where it goes.`);
    if (href.startsWith('/') && site) {
      const route = href.split('#')[0].replace(/\/$/, '') || '/';
      if (/\.(png|jpe?g|svg|gif|webp|pdf|xml|txt|json)$/.test(route)) continue;
      const known = site.byRoute.has(route) || (cfg.content.pages?.routes ?? []).includes(route) || site.extraRoutes?.has(route);
      if (!known && !site.prefixRoutes?.some((p) => route.startsWith(p))) add('internal-link', m.index, `Link target ${href} does not match any content item or listed page.`);
    }
  }

  // --- series cross-references ---
  if (item.series && site?.series.has(item.series)) {
    const s = site.series.get(item.series);
    const entries = s.entries;
    const self = item.seriesOrder;
    const noun = cfg.content.seriesArticle?.entryNoun ?? 'entry';
    const ordRe = new RegExp(`\\[(?:[^\\]]*?\\b)?(${ORDINALS.join('|')}|next|previous|preceding|following|last|final)\\s+${noun}\\b[^\\]]*\\]\\((/[^)#\\s]+)`, 'gi');
    for (const m of text.matchAll(ordRe)) {
      if (!isBody(m.index) || isInCode(noCode, m.index)) continue;
      const word = m[1].toLowerCase();
      const target = site.byRoute.get(m[2].replace(/\/$/, ''));
      if (!target || !target.series) {
        add('series-crossref', m.index, `"${m[0].slice(0, 60)}..." names a ${word} ${noun} but does not link to a series entry.`);
        continue;
      }
      if (target.series !== item.series) {
        // A reference into another series ("the first entry of the control series"): only an ordinal can be checked.
        const n = ORDINALS.indexOf(word) + 1;
        if (n && target.seriesOrder !== n) add('series-crossref', m.index, `Link says "${word} ${noun}" but points to entry ${target.seriesOrder} of the ${target.series} series.`);
        continue;
      }
      let expected = ORDINALS.indexOf(word) + 1;
      if (word === 'next' || word === 'following') expected = self + 1;
      if (word === 'previous' || word === 'preceding') expected = self - 1;
      if (word === 'last' || word === 'final') expected = entries.length;
      if (expected && target.seriesOrder !== expected) {
        add('series-crossref', m.index, `Link says "${word} ${noun}" but points to entry ${target.seriesOrder} ("${target.title}").`);
      }
    }
    const ordinalRe = new RegExp(`\\b(${ORDINALS.join('|')})\\s+${noun}\\b`, 'gi');
    for (const m of masked.matchAll(ordinalRe)) {
      if (!isBody(m.index)) continue;
      const n = ORDINALS.indexOf(m[1].toLowerCase()) + 1;
      if (n > entries.length) add('series-crossref', m.index, `"${m[0]}" but the series has ${entries.length} entries.`);
    }
    // "Section 3.2 of the first entry" / "first entry, Section 3.2" / "(Section 4)".
    const secRe = new RegExp(`(?:\\b(${ORDINALS.join('|')})\\s+${noun}(?:'s)?,?\\s+(?:in\\s+)?Sections?\\s+(\\d+(?:\\.\\d+)*))|(?:Sections?\\s+(\\d+(?:\\.\\d+)*)(?:\\s+(?:of|in)\\s+the\\s+(${ORDINALS.join('|')})\\s+${noun})?)`, 'gi');
    for (const m of masked.matchAll(secRe)) {
      if (!isBody(m.index)) continue;
      const ord = (m[1] ?? m[4])?.toLowerCase();
      const num = m[2] ?? m[3];
      const target = ord ? entries[ORDINALS.indexOf(ord)] : item;
      if (!target) continue;
      const targetHeads = headingsOf(target.text, maskProse(target.text, target.fm)).filter((h) => h.number);
      if (!targetHeads.some((h) => h.number === num) && targetHeads.length) {
        add('section-reference', m.index, `"${m[0]}": ${target === item ? 'this article' : `the ${ord} ${noun}`} has no section numbered ${num}. (Ignore if it cites an external standard.)`);
      }
    }
  }

  // --- acronyms ---
  if (sev('acronym-expansion') !== 'off') {
    const known = new Set(cfg.acronyms?.known ?? []);
    const first = new Map();
    const bodyMasked = masked.slice(bodyStart);
    for (const m of bodyMasked.matchAll(/\b[A-Z][A-Z0-9]{1,5}s?\b/g)) {
      const a = m[0].replace(/s$/, '');
      if (known.has(a) || /^[IVXLC]+$/.test(a) || a.length < 2 || !/[A-Z]{2}/.test(a)) continue;
      if (!first.has(a)) first.set(a, m.index);
    }
    for (const [a, idx] of first) {
      const ctx = bodyMasked.slice(Math.max(0, idx - 2), idx + a.length + 3);
      const after = bodyMasked.slice(idx + a.length, idx + a.length + 3);
      const expandedHere = ctx.startsWith('(') || /^\s*\(/.test(after) || bodyMasked.slice(Math.max(0, idx - 1), idx) === '(';
      if (!expandedHere) add('acronym-expansion', bodyStart + idx, `Abbreviation "${a}" is not expanded at its first use in this article.`, { match: a });
    }
  }

  // --- references ---
  if (sev('reference-format') !== 'off') {
    for (const r of referencesOf(cfg, item)) {
      if (!/\b(1[5-9]|20)\d{2}\b/.test(r.text)) add('reference-format', { line: r.line }, 'Reference has no year.');
      if (!/\*[^*]+\*|“[^”]+”|"[^"]+"|_[^_]+_/.test(r.text) && !/^(RFC|IEC|ISO|IEEE Std|NIST)\b/.test(r.text.replace(/^[-*]\s*/, ''))) {
        add('reference-format', { line: r.line }, 'Reference title is not italicized (book, standard) or quoted (article, chapter).');
      }
    }
  }

  const counts = Object.fromEntries(SEVERITIES.map((s) => [s, issues.filter((i) => i.severity === s).length]));
  return { item: item.path, id: item.id, issues: issues.sort((a, b) => a.line - b.line || a.col - b.col), counts, words: proseWords(masked.slice(bodyStart)) };
}

function maskCodeOnly(text) {
  const lines = text.split('\n');
  let fence = null;
  return lines
    .map((line) => {
      const m = /^\s*(`{3,}|~{3,})/.exec(line);
      if (fence) {
        if (m && m[1][0] === fence[0] && line.trim() === m[1]) fence = null;
        return ' '.repeat(line.length);
      }
      if (m) {
        fence = m[1];
        return ' '.repeat(line.length);
      }
      return line.replace(/(`+)[^`\n]+?\1/g, (s) => ' '.repeat(s.length));
    })
    .join('\n');
}

const isInCode = (noCode, idx) => noCode[idx] === ' ' && noCode.slice(idx, idx + 2).trim() === '';

export function referencesOf(cfg, item) {
  const names = (cfg.references?.sectionHeadings ?? ['References']).map((s) => s.toLowerCase());
  const lines = item.text.split('\n');
  const out = [];
  let inRefs = false;
  let level = 0;
  for (let i = 0; i < lines.length; i++) {
    const h = /^(#{1,6})\s+(?:\d+(?:\.\d+)*\.?\s+)?(.+?)\s*$/.exec(lines[i]);
    if (h) {
      if (names.includes(h[2].toLowerCase())) {
        inRefs = true;
        level = h[1].length;
        continue;
      }
      if (inRefs && h[1].length <= level) inRefs = false;
    }
    if (inRefs && /^\s*([-*]|\d+\.)\s+\S/.test(lines[i])) out.push({ line: i + 1, text: lines[i].trim() });
  }
  return out;
}

// ---------------------------------------------------------------------------------------------
// Fix (mechanical, reversible through version control): spelling variant and glossary terms that
// declare a "replace" value. Only unmasked prose is touched.
// ---------------------------------------------------------------------------------------------

function fixItem(cfg, item, rules) {
  const site = discover(cfg);
  const result = lintItem(cfg, item, site);
  const starts = lineStarts(item.text);
  const edits = result.issues
    .filter((i) => rules.includes(i.rule) && i.fix !== undefined && i.match)
    .map((i) => ({ start: starts[i.line - 1] + i.col - 1, len: i.match.length, fix: i.fix, rule: i.rule }))
    .sort((a, b) => b.start - a.start);
  let text = item.text;
  let last = Infinity;
  let applied = 0;
  for (const e of edits) {
    if (e.start + e.len > last) continue; // overlapping edits: keep the later one
    if (text.slice(e.start, e.start + e.len).toLowerCase() !== item.text.slice(e.start, e.start + e.len).toLowerCase()) continue;
    text = text.slice(0, e.start) + e.fix + text.slice(e.start + e.len);
    last = e.start;
    applied++;
  }
  if (applied) writeFileSync(path.join(cfg._root, item.path), text);
  return applied;
}

// ---------------------------------------------------------------------------------------------
// Review records and the publication gate
// ---------------------------------------------------------------------------------------------

const recordPath = (cfg, item) => path.join(cfg._root, cfg.review.recordsDir, item.type, `${item.slug}.json`);

function readRecord(cfg, item) {
  const p = recordPath(cfg, item);
  return existsSync(p) ? JSON.parse(readFileSync(p, 'utf8')) : null;
}

function evaluateRecord(cfg, item, rec) {
  const problems = [];
  const stages = cfg.review.requiredStages[item.type] ?? [];
  for (const s of stages) {
    const v = rec.stages?.[s];
    if (v !== 'pass' && v !== 'n/a') problems.push(`stage "${s}" is ${v ?? 'missing'}`);
    if (v === 'n/a' && !rec.notes) problems.push(`stage "${s}" is n/a without a note explaining why`);
  }
  for (const d of DIMENSIONS) {
    const v = rec.scores?.[d];
    if (typeof v !== 'number' || v < 0 || v > 4) problems.push(`score "${d}" missing or outside 0-4`);
    else if (v < cfg.review.minimumPerDimension) problems.push(`score "${d}" is ${v} (minimum ${cfg.review.minimumPerDimension})`);
  }
  const total = DIMENSIONS.reduce((s, d) => s + (Number(rec.scores?.[d]) || 0), 0);
  const min = cfg.review.minimumTotal[item.type] ?? 0;
  if (total < min) problems.push(`total score ${total}/28 is below ${min}`);
  if ((rec.critical ?? []).length) problems.push(`unresolved critical failures: ${rec.critical.join('; ')}`);
  if ((rec.findings?.open ?? 0) > 0) problems.push(`${rec.findings.open} blocking or should-fix findings still open`);
  return { total, problems, decision: problems.length ? 'revise' : 'publish' };
}

function record(cfg, item, input) {
  const site = discover(cfg);
  const lint = lintItem(cfg, item, site);
  const prior = readRecord(cfg, item);
  const rec = {
    schema: 'eos-review-record/1',
    id: item.id,
    path: item.path,
    type: item.type,
    title: item.title,
    hash: item.hash,
    reviewedAt: input.reviewedAt ?? new Date().toISOString().slice(0, 10),
    commit: gitHead(cfg._root),
    stages: input.stages ?? {},
    scores: input.scores ?? {},
    critical: input.critical ?? [],
    findings: input.findings ?? { blocking: 0, shouldFix: 0, optional: 0, open: 0 },
    lint: lint.counts,
    notVerified: input.notVerified ?? [],
    changes: input.changes ?? [],
    reviewers: input.reviewers ?? [],
    reportRef: input.reportRef ?? null,
    notes: input.notes ?? '',
    history: [
      ...(prior?.history ?? []),
      ...(prior ? [{ reviewedAt: prior.reviewedAt, hash: prior.hash, decision: prior.decision, total: prior.total, commit: prior.commit }] : []),
    ],
  };
  if (lint.counts.error) rec.critical = [...rec.critical, `${lint.counts.error} lint error(s); run "eos lint ${item.path}"`];
  const ev = evaluateRecord(cfg, item, rec);
  rec.total = ev.total;
  rec.decision = ev.decision;
  rec.problems = ev.problems;
  const p = recordPath(cfg, item);
  mkdirSync(path.dirname(p), { recursive: true });
  writeFileSync(p, `${JSON.stringify(rec, null, 2)}\n`);
  return rec;
}

/** One row per item: lint counts and the state of its review record. */
export function status(cfg) {
  const site = discover(cfg);
  return site.items.map((item) => {
    const lint = lintItem(cfg, item, site);
    const rec = readRecord(cfg, item);
    let stage;
    if (item.draft) stage = 'draft';
    else if (!rec) stage = 'needs-review';
    else if (rec.decision !== 'publish') stage = 'needs-fixes';
    else if (rec.hash !== item.hash) stage = 'review-stale';
    else if (lint.counts.error) stage = 'lint-errors';
    else stage = 'ready';
    if (rec && rec.decision === 'publish') {
      const ev = evaluateRecord(cfg, item, rec);
      if (ev.decision !== 'publish') stage = 'needs-fixes';
    }
    return { id: item.id, path: item.path, title: item.title, type: item.type, series: item.series, order: item.seriesOrder, draft: item.draft, example: item.example, words: lint.words, lint: lint.counts, record: rec ? { decision: rec.decision, total: rec.total, reviewedAt: rec.reviewedAt, current: rec.hash === item.hash } : null, stage };
  });
}

function gate(cfg, opts = {}) {
  const rows = status(cfg).filter((r) => !opts.types || opts.types.includes(r.type));
  const failures = [];
  for (const r of rows) {
    if (r.stage === 'draft' || r.stage === 'ready') continue;
    const why = {
      'needs-review': 'no editorial review record',
      'needs-fixes': 'the review record does not pass (decision "revise", or it fails the current acceptance rules)',
      'review-stale': 'the file changed after its review was recorded; review the change and record it again',
      'lint-errors': `${r.lint.error} lint error(s)`,
    }[r.stage];
    failures.push(`${r.path}: ${why}`);
  }
  return { ok: failures.length === 0, failures, rows };
}

// ---------------------------------------------------------------------------------------------
// Built-site validation (static HTML): rendering and accessibility defects a build does not catch.
// ---------------------------------------------------------------------------------------------

function validateSite(cfg, distArg) {
  const vcfg = cfg.validation?.site ?? {};
  const dist = path.resolve(cfg._root, distArg ?? vcfg.dist ?? 'dist');
  if (!existsSync(dist)) throw new EosError(`${dist} does not exist; build the site first.`, 2);
  const ignore = (vcfg.ignore ?? []).map(globToRegex);
  const pages = walk(dist).filter((f) => f.endsWith('.html') && !ignore.some((r) => r.test(f)));
  const issues = [];
  const add = (page, check, message) => issues.push({ page, check, message });
  // Pages not generated from a content item (home, about, listings) are not linted as content,
  // so their visible English text gets the spelling and phrase rules here.
  const site = discover(cfg);
  const variantMap = cfg.language?.variant ? spellingMap(cfg.language.variant) : new Map();
  const phraseRes = (cfg._glossary.phrases ?? []).filter((p) => !p.severity).map((p) => ({ re: new RegExp(p.avoid, 'gi'), msg: p.message }));
  for (const page of pages) {
    const html = readFileSync(path.join(dist, page), 'utf8');
    const route = `/${page.replace(/(index)?\.html$/, '')}`.replace(/\/$/, '') || '/';
    if (!site.byRoute.has(route) && /<html[^>]*\blang="en/i.test(html)) {
      const visible = decodeEntities(
        html
          .replace(/<(script|style|pre|code|svg|math)\b[\s\S]*?<\/\1>/gi, ' ')
          .replace(/<span class="katex[\s\S]*?<\/span><\/span><\/span>/g, ' ')
          .replace(/<[^>]+>/g, ' '),
      );
      const seenWords = new Set();
      for (const m of visible.matchAll(/[A-Za-z]+(?:[-'][A-Za-z]+)*/g)) {
        const lw = m[0].toLowerCase();
        if (variantMap.has(lw) && !seenWords.has(lw)) {
          seenWords.add(lw);
          add(page, 'spelling-variant', `"${m[0]}" is not ${cfg.language.variant} spelling; use "${matchCase(m[0], variantMap.get(lw))}".`);
        }
      }
      for (const { re, msg } of phraseRes) for (const m of visible.matchAll(re)) add(page, 'phrases', `"${m[0]}": ${msg}`);
    }
    const main = /<main\b[\s\S]*?<\/main>/i.exec(html)?.[0] ?? html;
    const h1 = (main.match(/<h1\b/gi) ?? []).length + (html.replace(main, '').match(/<h1\b/gi) ?? []).length;
    if (h1 !== 1) add(page, 'one-h1', `${h1} <h1> elements (expected exactly one).`);
    if (!/<html[^>]*\blang="[a-z]{2}/i.test(html)) add(page, 'html-lang', 'No lang attribute on <html>.');
    const title = /<title>([^<]*)<\/title>/i.exec(html)?.[1]?.trim();
    if (!title) add(page, 'title', 'Empty or missing <title>.');
    const desc = /<meta\s+name="description"\s+content="([^"]*)"/i.exec(html)?.[1];
    if (!desc) add(page, 'meta-description', 'No meta description.');
    else if (vcfg.descriptionMaxChars && decodeEntities(desc).length > vcfg.descriptionMaxChars) add(page, 'meta-description', `Meta description is ${decodeEntities(desc).length} characters (limit ${vcfg.descriptionMaxChars}).`);
    for (const m of html.matchAll(/<img\b[^>]*>/gi)) if (!/\balt=/.test(m[0])) add(page, 'img-alt', `Image without alt: ${m[0].slice(0, 80)}`);
    if (/class="katex-error"/.test(html)) add(page, 'katex-error', 'KaTeX failed to render an expression.');
    let last = 1;
    for (const m of main.matchAll(/<h([1-6])\b/gi)) {
      const lv = Number(m[1]);
      if (lv > last + 1) add(page, 'heading-order', `Heading level jumps from h${last} to h${lv}.`);
      last = lv;
    }
    const ids = new Map();
    for (const m of html.matchAll(/\sid="([^"]+)"/g)) ids.set(m[1], (ids.get(m[1]) ?? 0) + 1);
    const ignoreIds = (vcfg.ignoreDuplicateIds ?? []).map((r) => new RegExp(r));
    for (const [id, n] of ids) if (n > 1 && !ignoreIds.some((r) => r.test(id))) add(page, 'duplicate-id', `id="${id}" appears ${n} times.`);
    for (const m of html.matchAll(/<a\b[^>]*>(\s*)<\/a>/gi)) if (!/aria-label=/.test(m[0])) add(page, 'empty-link', 'Link with no text and no aria-label.');
    const text = main.replace(/<(pre|code|svg|script|style)\b[\s\S]*?<\/\1>/gi, '');
    for (const m of text.matchAll(/[A-Za-z0-9.,;:!?]<(span|strong|em|a|code)\b/g)) {
      // KaTeX splits operator names ("log", "arg") across spans by design; that is not glued prose.
      if (/class="(?:m[a-z]+|katex[a-z-]*|base|vlist[a-z-]*)[^"]*"[^>]*>[^<]*$/.test(text.slice(Math.max(0, m.index - 80), m.index + 1))) continue;
      // An opening quote written as an entity, or a decorative aria-hidden arrow, is not glued text.
      if (/&[a-z]+;$|&#\d+;$/.test(text.slice(Math.max(0, m.index - 10), m.index + 1)) || /^<[a-z]+[^>]*aria-hidden="true"/.test(text.slice(m.index + 1, m.index + 200))) continue;
      add(page, 'glued-inline', `Text glued to <${m[1]}>: ...${text.slice(Math.max(0, m.index - 25), m.index + 12).replace(/\s+/g, ' ')}...`);
    }
    if (vcfg.maxDiagramMinWidthPx) {
      for (const m of html.matchAll(/min-width:\s*(\d+(?:\.\d+)?)px/g)) {
        if (Number(m[1]) > vcfg.maxDiagramMinWidthPx) add(page, 'wide-figure', `Figure min-width ${m[1]}px exceeds ${vcfg.maxDiagramMinWidthPx}px and will overflow the text column.`);
      }
    }
  }
  return { dist, pages: pages.length, issues };
}

function decodeEntities(s) {
  return s.replace(/&amp;/g, '&').replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&#x27;/g, "'");
}

// ---------------------------------------------------------------------------------------------
// External links: checked only where the network allows; unreachable is "not verified", not "broken".
// ---------------------------------------------------------------------------------------------

async function checkExternal(cfg) {
  const site = discover(cfg);
  const urls = new Map();
  for (const it of site.items) {
    const noCode = maskCodeOnly(it.text);
    for (const m of noCode.matchAll(/https?:\/\/[^\s)>\]"'`]+/g)) {
      const u = m[0].replace(/[.,;:]+$/, '');
      if (/\b(example\.(com|org|net)|localhost|127\.0\.0\.1)\b|\.example\b/.test(u)) continue;
      if (!urls.has(u)) urls.set(u, []);
      urls.get(u).push(it.path);
    }
  }
  const results = [];
  for (const [url, where] of urls) {
    let state;
    let detail = '';
    try {
      const ctl = AbortSignal.timeout(15000);
      let res = await fetch(url, { method: 'HEAD', redirect: 'follow', signal: ctl });
      if (res.status === 405 || res.status === 403) res = await fetch(url, { method: 'GET', redirect: 'follow', signal: AbortSignal.timeout(15000) });
      state = res.ok ? 'ok' : res.status >= 400 && res.status < 500 && res.status !== 429 && res.status !== 403 ? 'broken' : 'not-verified';
      detail = `HTTP ${res.status}`;
    } catch (e) {
      state = 'not-verified';
      detail = e.cause?.code ?? e.name ?? 'network error';
    }
    results.push({ url, state, detail, where });
  }
  return results;
}

// ---------------------------------------------------------------------------------------------
// Inventory
// ---------------------------------------------------------------------------------------------

function inventory(cfg, opts = {}) {
  const site = discover(cfg);
  const rows = status(cfg);
  const translations = cfg.content.translations ?? {};
  const items = rows.map((r) => {
    const it = site.items.find((i) => i.id === r.id);
    const trans = {};
    for (const [lang, pattern] of Object.entries(translations)) {
      const dir = path.dirname(it.path);
      const rel = pattern.replace('{dir}', dir).replace('{file}', path.basename(it.path));
      trans[lang] = existsSync(path.join(cfg._root, rel)) ? rel : null;
    }
    return {
      ...r,
      route: it.route,
      published: it.data[cfg.content.fields.published] ?? null,
      updated: it.data[cfg.content.fields.updated] ?? null,
      status: it.data[cfg.content.fields.status] ?? (it.draft ? 'draft' : 'published'),
      planned: (it.data[cfg.content.fields.plannedEntries] ?? []).length || 0,
      headings: headingsOf(it.text, maskProse(it.text, it.fm)).length,
      references: referencesOf(cfg, it).length,
      translations: trans,
    };
  });
  const pages = [];
  const distDir = path.resolve(cfg._root, opts.dist ?? cfg.content.pages?.dist ?? 'dist');
  if (existsSync(distDir)) {
    for (const f of walk(distDir).filter((x) => x.endsWith('.html') && !x.startsWith('pagefind/'))) {
      const route = `/${f.replace(/(index)?\.html$/, '')}`.replace(/\/$/, '') || '/';
      if (site.byRoute.has(route)) continue;
      const html = readFileSync(path.join(distDir, f), 'utf8');
      const title = decodeEntities(/<title>([^<]*)<\/title>/i.exec(html)?.[1] ?? '');
      const lang = /<html[^>]*\blang="([^"]+)"/.exec(html)?.[1] ?? '';
      const kind = (cfg.content.pages?.routes ?? []).includes(route) ? 'page' : /\/vi(\/|$)/.test(route) ? 'translation' : 'listing';
      pages.push({ route, file: f, title, lang, kind, source: cfg.content.pages?.sources?.[route] ?? null });
    }
  }
  return { generatedAt: new Date().toISOString(), commit: gitHead(cfg._root), items, pages };
}

// ---------------------------------------------------------------------------------------------
// Vale export: the same rules as a Vale style, for editors that run Vale in their IDE or in CI.
// ---------------------------------------------------------------------------------------------

function valeStyle(cfg, outDir) {
  const name = (cfg.publication?.id ?? 'House').replace(/[^A-Za-z0-9]/g, '').replace(/^./, (c) => c.toUpperCase());
  const dir = path.resolve(cfg._root, outDir ?? 'editorial/vale');
  const styles = path.join(dir, 'styles', name);
  mkdirSync(styles, { recursive: true });
  const yamlStr = (s) => `'${String(s).replace(/'/g, "''")}'`;
  const level = (rule) => ({ error: 'error', warning: 'warning', suggestion: 'suggestion' })[cfg.rules[rule]] ?? 'warning';
  const map = spellingMap(cfg.language?.variant ?? 'en-US');
  const swap = [...map.entries()].map(([from, to]) => `  ${yamlStr(from)}: ${yamlStr(to)}`).join('\n');
  writeFileSync(path.join(styles, 'Spelling.yml'), `extends: substitution\nmessage: "Use '%s' (${cfg.language?.variant}) instead of '%s'."\nlevel: ${level('spelling-variant')}\nignorecase: true\nswap:\n${swap}\n`);
  const terms = (cfg._glossary.terms ?? []).flatMap((t) => (t.avoid ?? []).map((a) => [a, t.prefer]));
  writeFileSync(path.join(styles, 'Terms.yml'), `extends: existence\nmessage: "Check the house term: %s"\nlevel: ${level('terminology')}\nignorecase: false\nraw:\n  - '(?:${terms.map(([a]) => a.replace(/\(\?<[!=][^)]*\)/g, '').replace(/'/g, "''")).join('|')})'\n`);
  const phrases = (cfg._glossary.phrases ?? []).map((p) => p.avoid.replace(/\(\?<[!=][^)]*\)/g, ''));
  writeFileSync(path.join(styles, 'Phrases.yml'), `extends: existence\nmessage: "Avoid '%s' (see the house standards)."\nlevel: ${level('phrases')}\nignorecase: true\nraw:\n  - '(?:${phrases.map((p) => p.replace(/'/g, "''")).join('|')})'\n`);
  if (cfg.language?.contractions === 'avoid') {
    writeFileSync(path.join(styles, 'Contractions.yml'), `extends: existence\nmessage: "Write out the contraction '%s'."\nlevel: ${level('contractions')}\nignorecase: true\nraw:\n  - '\\b(?:\\w+n''t|it''s|that''s|there''s|let''s|\\w+''re|\\w+''ve|\\w+''ll)\\b'\n`);
  }
  const globs = Object.values(cfg.content.types).flatMap((t) => t.globs);
  const exts = [...new Set(globs.map((g) => g.split('.').pop()))].join(',');
  writeFileSync(path.join(dir, '.vale.ini'), `# Generated by editorial-os (eos vale-style) from ${path.relative(cfg._root, cfg._file)}; do not edit by hand.\n# Vale 3 needs mdx2vast on PATH for .mdx (npm i -g mdx2vast).\nStylesPath = styles\nMinAlertLevel = suggestion\n\n[*.{${exts}}]\nBasedOnStyles = ${name}\nTokenIgnores = (\\$+[^\\n$]+\\$+)\nBlockIgnores = (?s)(\\$\\$.*?\\$\\$)\n`);
  return { dir, style: name, rules: ['Spelling', 'Terms', 'Phrases', cfg.language?.contractions === 'avoid' ? 'Contractions' : null].filter(Boolean) };
}

// ---------------------------------------------------------------------------------------------
// Output helpers
// ---------------------------------------------------------------------------------------------

function printLint(results, { quiet }) {
  const lines = [];
  for (const r of results) {
    const shown = r.issues.filter((i) => !quiet || i.severity !== 'suggestion');
    if (!shown.length) continue;
    lines.push(`\n${r.item}`);
    for (const i of shown) lines.push(`  ${String(i.line).padStart(4)}:${String(i.col).padEnd(3)} ${i.severity.padEnd(10)} ${i.rule.padEnd(20)} ${i.message}`);
  }
  const tot = Object.fromEntries(SEVERITIES.map((s) => [s, results.reduce((n, r) => n + r.counts[s], 0)]));
  lines.push(`\n${results.length} file(s): ${tot.error} error(s), ${tot.warning} warning(s), ${tot.suggestion} suggestion(s).`);
  return { text: lines.join('\n'), tot };
}

function mdTable(header, rows) {
  return [`| ${header.join(' | ')} |`, `|${header.map(() => '---').join('|')}|`, ...rows.map((r) => `| ${r.join(' | ')} |`)].join('\n');
}

function selectItems(site, args) {
  const want = args._.slice(1);
  if (!want.length) return site.items;
  const out = [];
  for (const w of want) {
    const rel = path.relative(site.root, path.resolve(w)).replace(/\\/g, '/');
    const hit = site.items.filter((i) => i.path === rel || i.path === w || i.id === w || i.slug === w || (i.series === w && !i.def.isSeriesIndex) || i.path.startsWith(`${rel}/`));
    if (!hit.length) throw new EosError(`No content item matches "${w}".`, 2);
    out.push(...hit);
  }
  return [...new Set(out)];
}

const HELP = `editorial-os ${VERSION}: deterministic editorial checks and the publication gate

  eos init                         create editorial/ config, glossary and standards from templates (never overwrites)
  eos inventory [--json|--md] [--dist dir]  every content item and built page, with state
  eos lint [paths|ids|series...] [--json] [--quiet] [--rules a,b]   style, structure, link and cross-reference rules
  eos fix [paths...] [--rules spelling-variant,terminology]         apply mechanical fixes in prose only
  eos status [--json]              review stage of every item (needs-review, review-stale, ready, ...)
  eos record <path> --from review.json   write the review record (stages, scores, findings) for a file
  eos gate [--json] [--types article,insight]   exit 1 unless every published item has a current passing record
  eos validate-site [dist] [--json]       rendering and accessibility checks on the built HTML
  eos refs [--json]                bibliography of every References section
  eos check-external [--json] [--strict]   fetch external URLs (unreachable = not verified, not broken)
  eos vale-style [--out dir]       export spelling, terms and phrases as a Vale style
  eos syntax [paths...]            compile Markdown/MDX with the project's MDX compiler (fast, no site build)
  eos hook                         Claude Code PostToolUse hook: lint the edited content file
  eos hash <path>                  content hash used by records

Options: --config <file> (default: editorial/eos.config.json found upwards from the project directory)`;

// ---------------------------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------------------------

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const cmd = args._[0] ?? 'help';
  if (cmd === 'help' || args.help) return console.log(HELP);
  if (cmd === 'version') return console.log(VERSION);

  if (cmd === 'init') {
    const root = process.env.CLAUDE_PROJECT_DIR || process.cwd();
    const dest = path.join(root, 'editorial');
    mkdirSync(dest, { recursive: true });
    const made = [];
    for (const [src, name] of [['eos.config.example.json', 'eos.config.json'], ['glossary.example.json', 'glossary.json'], ['standards.template.md', 'standards.md']]) {
      const to = path.join(dest, name);
      if (existsSync(to)) continue;
      copyFileSync(path.join(PLUGIN_ROOT, 'templates', src), to);
      made.push(path.relative(root, to));
    }
    console.log(made.length ? `Created ${made.join(', ')}. Edit editorial/eos.config.json next (content globs, routes, language variant).` : 'editorial/ already has a config, glossary and standards; nothing changed.');
    return;
  }

  if (cmd === 'hook') {
    // PostToolUse hook: never blocks; adds lint findings for the edited file to Claude's context.
    let input = '';
    for await (const chunk of process.stdin) input += chunk;
    let file;
    try {
      file = JSON.parse(input || '{}').tool_input?.file_path;
    } catch {
      return;
    }
    if (!file) return;
    let cfg;
    try {
      cfg = loadConfig(args.config);
    } catch {
      return; // no config: the project does not use EOS
    }
    const site = discover(cfg);
    site.root = cfg._root;
    const rel = path.relative(cfg._root, path.resolve(file)).replace(/\\/g, '/');
    const item = site.items.find((i) => i.path === rel);
    if (!item) return;
    const r = lintItem(cfg, item, site);
    const important = r.issues.filter((i) => i.severity !== 'suggestion');
    const rec = readRecord(cfg, item);
    const notes = [];
    if (important.length) {
      notes.push(`Editorial lint for ${rel}: ${r.counts.error} error(s), ${r.counts.warning} warning(s).`);
      for (const i of important.slice(0, 25)) notes.push(`- ${i.line}:${i.col} ${i.severity} ${i.rule}: ${i.message}`);
      if (important.length > 25) notes.push(`- ... ${important.length - 25} more; run eos lint ${rel}`);
    }
    if (rec && rec.hash !== item.hash) notes.push(`${rel} has an editorial review record that this edit made stale; the publication gate will block it until the change is reviewed and recorded again (editorial skill, stage "qa", then eos record).`);
    if (notes.length) process.stdout.write(JSON.stringify({ hookSpecificOutput: { hookEventName: 'PostToolUse', additionalContext: notes.join('\n') } }));
    return;
  }

  const cfg = loadConfig(args.config);

  if (cmd === 'hash') {
    const site = discover(cfg);
    site.root = cfg._root;
    for (const it of selectItems(site, args)) console.log(`${it.hash}  ${it.path}`);
    return;
  }

  if (cmd === 'lint') {
    const site = discover(cfg);
    site.root = cfg._root;
    const only = args.rules ? String(args.rules).split(',') : null;
    const results = selectItems(site, args).map((it) => {
      const r = lintItem(cfg, it, site);
      if (only) {
        r.issues = r.issues.filter((i) => only.includes(i.rule));
        r.counts = Object.fromEntries(SEVERITIES.map((s) => [s, r.issues.filter((i) => i.severity === s).length]));
      }
      return r;
    });
    if (args.json) console.log(JSON.stringify(results, null, 2));
    else {
      const { text, tot } = printLint(results, { quiet: args.quiet });
      console.log(text);
      process.exitCode = tot.error ? 1 : 0;
      return;
    }
    process.exitCode = results.some((r) => r.counts.error) ? 1 : 0;
    return;
  }

  if (cmd === 'fix') {
    const rules = args.rules ? String(args.rules).split(',') : ['spelling-variant'];
    const site = discover(cfg);
    site.root = cfg._root;
    let total = 0;
    for (const it of selectItems(site, args)) {
      const n = fixItem(cfg, { ...it, text: readText(path.join(cfg._root, it.path)) }, rules);
      if (n) console.log(`${it.path}: ${n} fix(es)`);
      total += n;
    }
    console.log(`${total} fix(es) applied (${rules.join(', ')}). Review the diff before committing.`);
    return;
  }

  if (cmd === 'status') {
    const rows = status(cfg);
    if (args.json) return console.log(JSON.stringify(rows, null, 2));
    console.log(mdTable(['Item', 'Type', 'Words', 'Lint (E/W/S)', 'Review', 'Stage'], rows.map((r) => [
      `\`${r.path}\``, r.type, r.words, `${r.lint.error}/${r.lint.warning}/${r.lint.suggestion}`,
      r.record ? `${r.record.decision} ${r.record.total}/28 ${r.record.reviewedAt}${r.record.current ? '' : ' (stale)'}` : '-', r.stage,
    ])));
    const by = {};
    for (const r of rows) by[r.stage] = (by[r.stage] ?? 0) + 1;
    console.log(`\n${rows.length} item(s): ${Object.entries(by).map(([k, v]) => `${v} ${k}`).join(', ')}.`);
    return;
  }

  if (cmd === 'record') {
    const site = discover(cfg);
    site.root = cfg._root;
    const [item] = selectItems(site, { _: ['record', args._[1]] });
    if (!args.from) throw new EosError('Usage: eos record <path> --from <review.json>', 2);
    const input = JSON.parse(readFileSync(path.resolve(args.from), 'utf8'));
    const rec = record(cfg, item, input);
    console.log(`${path.relative(cfg._root, recordPath(cfg, item))}: decision ${rec.decision}, total ${rec.total}/28${rec.problems.length ? `\n  - ${rec.problems.join('\n  - ')}` : ''}`);
    process.exitCode = rec.decision === 'publish' ? 0 : 1;
    return;
  }

  if (cmd === 'gate') {
    const result = gate(cfg, { types: args.types ? String(args.types).split(',') : null });
    const counts = {};
    for (const r of result.rows) counts[r.stage] = (counts[r.stage] ?? 0) + 1;
    const report = [
      `## Editorial gate: ${result.ok ? 'passed' : 'FAILED'}`,
      '',
      `${result.rows.length} item(s): ${Object.entries(counts).map(([k, v]) => `${v} ${k}`).join(', ')}.`,
      '',
      ...(result.failures.length ? ['Failures:', '', ...result.failures.map((f) => `- ${f}`)] : ['No failures: every published item has a current, passing editorial review record and no lint errors.']),
    ].join('\n');
    console.log(args.json ? JSON.stringify(result, null, 2) : report);
    if (process.env.GITHUB_STEP_SUMMARY) appendFileSync(process.env.GITHUB_STEP_SUMMARY, `${report}\n`);
    process.exitCode = result.ok ? 0 : 1;
    return;
  }

  if (cmd === 'validate-site') {
    const r = validateSite(cfg, args._[1]);
    if (args.json) console.log(JSON.stringify(r, null, 2));
    else {
      const by = {};
      for (const i of r.issues) (by[i.check] ??= []).push(i);
      console.log(`Checked ${r.pages} page(s) in ${path.relative(cfg._root, r.dist) || r.dist}.`);
      for (const [check, list] of Object.entries(by)) {
        console.log(`\n${check} (${list.length})`);
        for (const i of list.slice(0, 20)) console.log(`  ${i.page}: ${i.message}`);
        if (list.length > 20) console.log(`  ... ${list.length - 20} more`);
      }
      console.log(r.issues.length ? `\n${r.issues.length} issue(s).` : '\nNo issues.');
    }
    process.exitCode = r.issues.length ? 1 : 0;
    return;
  }

  if (cmd === 'refs') {
    const site = discover(cfg);
    const refs = site.items.flatMap((it) => referencesOf(cfg, it).map((r) => ({ item: it.path, line: r.line, text: r.text.replace(/^([-*]|\d+\.)\s+/, '') })));
    if (args.json) return console.log(JSON.stringify(refs, null, 2));
    const unique = new Map();
    for (const r of refs) {
      if (!unique.has(r.text)) unique.set(r.text, []);
      unique.get(r.text).push(`${r.item}:${r.line}`);
    }
    for (const [text, where] of [...unique.entries()].sort()) console.log(`- ${text}\n  cited in: ${where.join(', ')}`);
    console.log(`\n${refs.length} reference entries, ${unique.size} distinct.`);
    return;
  }

  if (cmd === 'check-external') {
    const results = await checkExternal(cfg);
    if (args.json) console.log(JSON.stringify(results, null, 2));
    else {
      for (const r of results) console.log(`${r.state.padEnd(13)} ${r.detail.padEnd(14)} ${r.url}  (${r.where.join(', ')})`);
      const broken = results.filter((r) => r.state === 'broken').length;
      const nv = results.filter((r) => r.state === 'not-verified').length;
      console.log(`\n${results.length} external URL(s): ${results.length - broken - nv} ok, ${broken} broken, ${nv} not verified (network or server refused; check by hand).`);
    }
    process.exitCode = args.strict && results.some((r) => r.state === 'broken') ? 1 : 0;
    return;
  }

  if (cmd === 'inventory') {
    const inv = inventory(cfg, { dist: args.dist });
    if (args.json) return console.log(JSON.stringify(inv, null, 2));
    console.log(`# Content inventory\n\nGenerated ${inv.generatedAt} at commit ${inv.commit ?? '(no git)'}.\n`);
    console.log(mdTable(['Item', 'Type', 'Series (order)', 'Words', 'Refs', 'Translations', 'Lint (E/W/S)', 'Stage'], inv.items.map((r) => [
      `\`${r.path}\``, r.type, r.series ? `${r.series} (${r.order})` : '-', r.words, r.references,
      Object.entries(r.translations).map(([l, v]) => `${l}:${v ? 'yes' : 'no'}`).join(' ') || '-', `${r.lint.error}/${r.lint.warning}/${r.lint.suggestion}`, r.stage,
    ])));
    if (inv.pages.length) {
      console.log(`\n## Built pages not backed by a content item (${inv.pages.length})\n`);
      console.log(mdTable(['Route', 'Kind', 'Lang', 'Title', 'Source'], inv.pages.map((p) => [p.route, p.kind, p.lang, p.title.replace(/\|/g, '\\|'), p.source ?? '-'])));
    }
    return;
  }

  if (cmd === 'syntax') {
    // Compile Markdown/MDX with the project's own @mdx-js/mdx (and remark-math if present), without a site build.
    const { createRequire } = await import('node:module');
    const req = createRequire(path.join(cfg._root, 'package.json'));
    let compile;
    let remarkMath = null;
    try {
      ({ compile } = await import(req.resolve('@mdx-js/mdx')));
    } catch {
      console.log('syntax: @mdx-js/mdx is not installed in this project; skipped (run the site build instead).');
      return;
    }
    try {
      remarkMath = (await import(req.resolve('remark-math'))).default;
    } catch {}
    const site = discover(cfg);
    site.root = cfg._root;
    let bad = 0;
    for (const it of selectItems(site, args)) {
      const src = it.text.slice(0, it.fm.end).replace(/[^\n]/g, '') + it.text.slice(it.fm.end);
      try {
        await compile(src, { remarkPlugins: remarkMath ? [remarkMath] : [], format: it.path.endsWith('.mdx') ? 'mdx' : 'md' });
      } catch (e) {
        bad++;
        console.log(`${it.path}:${e.line ?? e.place?.line ?? '?'}: ${e.reason ?? e.message}`);
      }
    }
    console.log(bad ? `${bad} file(s) failed to compile.` : 'All files compile.');
    process.exitCode = bad ? 1 : 0;
    return;
  }

  if (cmd === 'vale-style') {
    const r = valeStyle(cfg, args.out);
    console.log(`Wrote ${path.relative(cfg._root, r.dir)}/.vale.ini and style ${r.style} (${r.rules.join(', ')}). Run: vale --config ${path.relative(cfg._root, r.dir)}/.vale.ini <files>`);
    return;
  }

  throw new EosError(`Unknown command "${cmd}".\n\n${HELP}`, 2);
}

main().catch((err) => {
  console.error(err instanceof EosError ? err.message : err.stack);
  process.exit(err.code ?? 1);
});
