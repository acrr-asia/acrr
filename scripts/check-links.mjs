#!/usr/bin/env node
/**
 * Dependency-free internal link checker for the built site.
 *
 *   npm run build:local && npm run check:links      (or SITE_URL=<origin> npm run build && ...)
 *   node scripts/check-links.mjs [distDir]      (default: ./dist next to this script's parent)
 *
 * Walks every dist/**\/*.html page, collects internal href / src / srcset references and checks that
 * each one resolves to a file under dist, using the same fallbacks a static host applies:
 *
 *   /blog/post   ->  dist/blog/post  |  dist/blog/post.html  |  dist/blog/post/index.html
 *   /blog/       ->  dist/blog/index.html   (a trailing slash means "directory")
 *
 * When the target is an HTML page and the link has a #fragment, the fragment must match an id
 * (or <a name>) in that page. Ignored: external URLs, protocol-relative URLs, mailto:/tel:/data:/
 * javascript:, fragment-only links (#main), and /pagefind/ assets (generated after the Astro build).
 * If SITE_URL is set, absolute URLs under that origin are checked as internal links.
 *
 * Exit codes: 0 = all links resolve, 1 = broken links found, 2 = dist missing or empty.
 */
import { readdirSync, readFileSync, existsSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const projectRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const distDir = path.resolve(process.argv[2] ?? path.join(projectRoot, 'dist'));
const siteOrigin = (process.env.SITE_URL ?? '').replace(/\/+$/, '');

if (!existsSync(distDir)) {
  console.error(`check-links: "${distDir}" does not exist. Run "npm run build" first.`);
  process.exit(2);
}

// ---------------------------------------------------------------------------------------------
// File inventory (exact-case set of URL paths, so a case mismatch fails here as it would on Linux)
// ---------------------------------------------------------------------------------------------
function walk(dir, out = []) {
  for (const entry of readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(full, out);
    else if (entry.isFile()) out.push(full);
  }
  return out;
}

const toUrlPath = (file) => '/' + path.relative(distDir, file).split(path.sep).join('/');
const toDiskPath = (urlPath) => path.join(distDir, ...urlPath.split('/').filter(Boolean));

const allFiles = walk(distDir).map(toUrlPath);
const files = new Set(allFiles);
const pages = allFiles.filter((f) => f.endsWith('.html') && !f.startsWith('/pagefind/')).sort();

if (pages.length === 0) {
  console.error(`check-links: no .html files found in "${distDir}". Run "npm run build" first.`);
  process.exit(2);
}

// ---------------------------------------------------------------------------------------------
// Minimal HTML helpers (no dependencies)
// ---------------------------------------------------------------------------------------------
const TAG_RE = /<([a-zA-Z][^\s/>]*)((?:"[^"]*"|'[^']*'|[^'">])*)>/g;
const ATTR_RE = /([^\s"'<>/=]+)(?:\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s"'=<>`]+)))?/g;
const NON_MARKUP_RE = /<(script|style|textarea)((?:"[^"]*"|'[^']*'|[^'">])*)>[\s\S]*?<\/\1\s*>/gi;

const NAMED_ENTITIES = { amp: '&', lt: '<', gt: '>', quot: '"', apos: "'", nbsp: ' ' };

function decodeEntities(s) {
  return s.replace(/&(#x[0-9a-f]+|#\d+|[a-z]+);/gi, (whole, body) => {
    if (body[0] === '#') {
      const code = body[1].toLowerCase() === 'x' ? parseInt(body.slice(2), 16) : parseInt(body.slice(1), 10);
      try {
        return String.fromCodePoint(code);
      } catch {
        return whole;
      }
    }
    return NAMED_ENTITIES[body.toLowerCase()] ?? whole;
  });
}

/** Drop comments and the bodies of <script>/<style>/<textarea> so their text is never read as markup. */
function stripNonMarkup(html) {
  return html.replace(/<!--[\s\S]*?-->/g, '').replace(NON_MARKUP_RE, '<$1$2></$1>');
}

function* parseTags(html) {
  for (const m of html.matchAll(TAG_RE)) {
    const attrs = new Map();
    for (const a of m[2].matchAll(ATTR_RE)) {
      const name = a[1].toLowerCase();
      if (!attrs.has(name)) attrs.set(name, a[2] ?? a[3] ?? a[4] ?? '');
    }
    yield { tag: m[1].toLowerCase(), attrs };
  }
}

function safeDecode(s) {
  try {
    return decodeURIComponent(s);
  } catch {
    return s;
  }
}

// ---------------------------------------------------------------------------------------------
// Resolution
// ---------------------------------------------------------------------------------------------

/** URL a visitor would see for a built file; used as the base for relative references. */
function pageUrl(filePath) {
  if (filePath.endsWith('/index.html')) return filePath.slice(0, -'index.html'.length);
  return filePath.replace(/\.html$/, '');
}

/** Returns the dist file (as a URL path) that serves `pathname`, or null. */
function resolveTarget(pathname) {
  const trailing = pathname.length > 1 && pathname.endsWith('/');
  const bare = pathname.replace(/\/+$/, '');
  const candidates = [];
  if (bare === '') {
    candidates.push('/index.html');
  } else if (trailing) {
    candidates.push(`${bare}/index.html`);
  } else {
    candidates.push(bare, `${bare}.html`, `${bare}/index.html`);
  }
  return candidates.find((c) => files.has(c)) ?? null;
}

const idCache = new Map();
function idsOf(targetFile) {
  let ids = idCache.get(targetFile);
  if (!ids) {
    ids = new Set();
    const html = stripNonMarkup(readFileSync(toDiskPath(targetFile), 'utf8'));
    for (const { tag, attrs } of parseTags(html)) {
      if (attrs.has('id')) ids.add(decodeEntities(attrs.get('id')));
      if (tag === 'a' && attrs.has('name')) ids.add(decodeEntities(attrs.get('name')));
    }
    idCache.set(targetFile, ids);
  }
  return ids;
}

/**
 * Turns a raw attribute value into { pathname, fragment } for an internal reference,
 * or null when it should be ignored (external, mailto:, fragment-only, /pagefind/, ...).
 */
function toInternalRef(raw, fromPageUrl) {
  let value = decodeEntities(raw).trim();
  if (!value || value.startsWith('#') || value.startsWith('//')) return null;

  if (/^[a-zA-Z][a-zA-Z0-9+.-]*:/.test(value)) {
    const underSite =
      siteOrigin !== '' &&
      value.startsWith(siteOrigin) &&
      (value.length === siteOrigin.length || /^[/?#]/.test(value.slice(siteOrigin.length)));
    if (!underSite) return null; // external, mailto:, tel:, data:, ...
    const rest = value.slice(siteOrigin.length);
    value = rest.startsWith('/') ? rest : `/${rest}`;
  }

  let url;
  try {
    url = new URL(value, `http://internal.invalid${fromPageUrl}`);
  } catch {
    return { pathname: value, fragment: '', malformed: true };
  }
  const pathname = safeDecode(url.pathname);
  if (pathname.startsWith('/pagefind/')) return null;
  return { pathname, fragment: safeDecode(url.hash.slice(1)) };
}

function* referencesIn(html) {
  for (const { attrs } of parseTags(html)) {
    for (const name of ['href', 'src']) {
      if (attrs.has(name)) yield [name, attrs.get(name)];
    }
    const srcset = attrs.get('srcset');
    if (srcset && !srcset.includes('data:')) {
      for (const part of srcset.split(',')) {
        const candidate = part.trim().split(/\s+/)[0];
        if (candidate) yield ['srcset', candidate];
      }
    }
  }
}

// ---------------------------------------------------------------------------------------------
// Check
// ---------------------------------------------------------------------------------------------
const broken = []; // { page, attr, value, reason }
let referenceCount = 0;

for (const page of pages) {
  const html = stripNonMarkup(readFileSync(toDiskPath(page), 'utf8'));
  const base = pageUrl(page);
  const seen = new Set();

  for (const [attr, raw] of referencesIn(html)) {
    const ref = toInternalRef(raw, base);
    if (!ref) continue;

    const key = `${attr}\u0000${raw}`;
    if (seen.has(key)) continue;
    seen.add(key);
    referenceCount++;

    const report = (reason) => broken.push({ page, attr, value: decodeEntities(raw).trim(), reason });

    if (ref.malformed) {
      report('malformed URL');
      continue;
    }

    const target = resolveTarget(ref.pathname);
    if (!target) {
      const trailingSlash = ref.pathname.length > 1 && ref.pathname.endsWith('/');
      report(
        trailingSlash
          ? `target not found (no ${ref.pathname.replace(/\/+$/, '')}/index.html; this site uses no trailing slashes)`
          : 'target not found',
      );
      continue;
    }

    if (ref.fragment && ref.fragment.toLowerCase() !== 'top' && target.endsWith('.html')) {
      if (!idsOf(target).has(ref.fragment)) {
        report(`fragment "#${ref.fragment}" not found in ${target}`);
      }
    }
  }
}

// ---------------------------------------------------------------------------------------------
// Report
// ---------------------------------------------------------------------------------------------
console.log(`Checked ${pages.length} pages and ${referenceCount} internal references in ${path.relative(process.cwd(), distDir) || '.'}.`);

if (broken.length === 0) {
  console.log('All internal links resolve.');
} else {
  const byPage = new Map();
  for (const b of broken) {
    if (!byPage.has(b.page)) byPage.set(b.page, []);
    byPage.get(b.page).push(b);
  }
  console.error(`\n${broken.length} broken internal link${broken.length === 1 ? '' : 's'} on ${byPage.size} page${byPage.size === 1 ? '' : 's'}:\n`);
  for (const [page, items] of byPage) {
    console.error(`  ${page}  (served as ${pageUrl(page)})`);
    for (const b of items) console.error(`    ${b.attr}="${b.value}"  ->  ${b.reason}`);
    console.error('');
  }
  process.exitCode = 1;
}
