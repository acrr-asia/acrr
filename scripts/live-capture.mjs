#!/usr/bin/env node
// Captures of published pages for the chief editor's live-site review (editorial/standards.md 4.4).
// Opens each page at its public URL in Chromium, takes screenshots on a wide and a 360-pixel screen
// (light, and dark on the narrow screen), cut into screen-height tiles so each one stays legible, and
// records rendering facts that a reviewer would otherwise have to find by eye. Used by
// .github/workflows/live-review.yml; works against any origin, so it can be tried on `npm run preview`.
//
//   node scripts/live-capture.mjs routes <base> <head>       routes to capture for the files changed
//                                                            between two commits, one per line
//   node scripts/live-capture.mjs capture <origin> <out> <route...> [--routes-file f]
//
// `routes` maps a changed content file to its route through its editorial queue entry (or, for a
// Vietnamese translation, to /vi/<route>), and adds the main section pages when site code changed.
// `capture` writes <out>/<page>/ with desktop-light-NN.jpg, mobile-light-NN.jpg, mobile-dark-NN.jpg
// and facts.json, plus <out>/index.md (also appended to $GITHUB_STEP_SUMMARY when set). It exits 1
// only when a page cannot be loaded; rendering findings are for the reviewer, not a gate.
import { execFileSync } from 'node:child_process';
import { appendFileSync, existsSync, mkdirSync, readFileSync, readdirSync, writeFileSync } from 'node:fs';
import path from 'node:path';

const VIEWPORTS = [
  { name: 'desktop-light', width: 1280, height: 900, scheme: 'light' },
  { name: 'mobile-light', width: 360, height: 780, scheme: 'light' },
  { name: 'mobile-dark', width: 360, height: 780, scheme: 'dark' },
];
const MAX_TILES = 80; // per viewport; a longer page is cut off and the facts say so
const SECTION_PAGES = ['/', '/blog', '/series', '/insights', '/learning', '/about', '/vi'];
const SITE_CODE = /^(src\/(views|components|layouts|styles|pages|lib|i18n|plugins)\/|astro\.config\.mjs$|public\/)/;

const pageDir = (route) => (route === '/' ? 'home' : route.replace(/^\//, '').replace(/\//g, '__'));

function changedRoutes(base, head) {
  const files = execFileSync('git', ['diff', '--name-only', `${base}..${head}`], { encoding: 'utf8' }).split('\n').filter(Boolean);
  const queueDir = 'editorial/queue';
  const bySource = new Map();
  if (existsSync(queueDir)) {
    for (const type of readdirSync(queueDir)) {
      for (const f of readdirSync(path.join(queueDir, type)).filter((n) => n.endsWith('.json'))) {
        const e = JSON.parse(readFileSync(path.join(queueDir, type, f), 'utf8'));
        if (e.source && e.url) bySource.set(e.source, new URL(e.url).pathname);
      }
    }
  }
  const routes = new Set();
  for (const file of files) {
    if (!existsSync(file)) continue; // deleted
    const m = /^src\/content\/(blog|series|insights)\/(vi\/)?([^/]+)\.mdx?$/.exec(file);
    if (m) {
      const section = m[1] === 'blog' ? 'blog' : m[1];
      const en = bySource.get(file.replace('/vi/', '/')) ?? `/${section}/${m[3]}`;
      routes.add(m[2] ? `/vi${en}` : en);
    } else if (SITE_CODE.test(file)) for (const r of SECTION_PAGES) routes.add(r);
  }
  return [...routes].sort();
}

/** Rendering facts measured in the page itself. Runs in the browser. */
function measure() {
  const vw = document.documentElement.clientWidth;
  const main = document.querySelector('main') ?? document.body;
  const scrollsX = (el) => {
    for (let n = el.parentElement; n && n !== document.body; n = n.parentElement) {
      const o = getComputedStyle(n).overflowX;
      if (o === 'auto' || o === 'scroll' || o === 'hidden') return true;
    }
    return false;
  };
  const label = (el) => `${el.tagName.toLowerCase()}${el.id ? `#${el.id}` : ''}${el.className && typeof el.className === 'string' ? `.${el.className.trim().split(/\s+/).slice(0, 2).join('.')}` : ''}`;
  const overflowing = [...main.querySelectorAll('img, svg, table, pre, figure, .katex-display, iframe, video')]
    .filter((el) => el.getBoundingClientRect().right > vw + 1 && !scrollsX(el))
    .slice(0, 20)
    .map((el) => `${label(el)} (right edge ${Math.round(el.getBoundingClientRect().right)} px)`);
  const nearestHeading = (el) => {
    let n = el;
    while (n && n !== main) {
      let s = n.previousElementSibling;
      while (s) {
        if (/^H[1-4]$/.test(s.tagName)) return s.textContent.trim().slice(0, 80);
        s = s.previousElementSibling;
      }
      n = n.parentElement;
    }
    return null;
  };
  return {
    title: document.title,
    h1: [...document.querySelectorAll('h1')].map((h) => h.textContent.trim().replace(/\s+/g, ' ')),
    lang: document.documentElement.lang,
    description: document.querySelector('meta[name="description"]')?.content ?? null,
    pageWidth: document.documentElement.scrollWidth,
    viewportWidth: vw,
    horizontalScroll: document.documentElement.scrollWidth > vw + 1,
    height: document.documentElement.scrollHeight,
    katexErrors: [...document.querySelectorAll('.katex-error')].map((e) => ({ near: nearestHeading(e), text: e.textContent.slice(0, 80) })),
    brokenImages: [...document.querySelectorAll('img')].filter((i) => i.complete && i.naturalWidth === 0).map((i) => i.currentSrc || i.src),
    imagesWithoutAlt: [...document.querySelectorAll('img:not([alt])')].length,
    svgFiguresWithoutTitle: [...main.querySelectorAll('figure svg')].filter((s) => !s.querySelector('title') && !s.getAttribute('aria-label') && !s.getAttribute('aria-labelledby')).length,
    overflowing,
    headings: [...main.querySelectorAll('h2, h3')].map((h) => `${h.tagName.toLowerCase()} ${h.textContent.trim().replace(/\s+/g, ' ').slice(0, 90)}`),
    figures: main.querySelectorAll('figure').length,
    tables: main.querySelectorAll('table').length,
    codeBlocks: main.querySelectorAll('pre').length,
    equations: main.querySelectorAll('.katex-display').length,
  };
}

async function capture(origin, out, routes) {
  const { chromium } = await import('playwright');
  const browser = await chromium.launch(process.env.PLAYWRIGHT_CHROMIUM_PATH ? { executablePath: process.env.PLAYWRIGHT_CHROMIUM_PATH } : {});
  const rows = [];
  let failed = 0;
  mkdirSync(out, { recursive: true });
  for (const route of routes) {
    const url = new URL(route, origin).href;
    const dir = path.join(out, pageDir(route));
    mkdirSync(dir, { recursive: true });
    const facts = { url, route, capturedAt: new Date().toISOString(), viewports: {} };
    for (const vp of VIEWPORTS) {
      const ctx = await browser.newContext({ viewport: { width: vp.width, height: vp.height }, colorScheme: vp.scheme, deviceScaleFactor: 1 });
      const page = await ctx.newPage();
      const consoleErrors = [];
      page.on('console', (m) => m.type() === 'error' && consoleErrors.push(m.text().slice(0, 200)));
      page.on('pageerror', (e) => consoleErrors.push(String(e).slice(0, 200)));
      let status = null;
      try {
        const res = await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 });
        status = res?.status() ?? null;
        await page.evaluate(() => document.fonts.ready);
      } catch (e) {
        facts.viewports[vp.name] = { error: String(e).slice(0, 300) };
        await ctx.close();
        continue;
      }
      const m = await page.evaluate(measure);
      const tiles = Math.min(MAX_TILES, Math.ceil(m.height / vp.height));
      for (let i = 0; i < tiles; i++) {
        await page.screenshot({
          path: path.join(dir, `${vp.name}-${String(i + 1).padStart(2, '0')}.jpg`),
          type: 'jpeg', quality: 70, fullPage: true,
          clip: { x: 0, y: i * vp.height, width: vp.width, height: Math.min(vp.height, m.height - i * vp.height) },
        });
      }
      facts.viewports[vp.name] = { status, ...m, tiles, truncated: Math.ceil(m.height / vp.height) > MAX_TILES, consoleErrors };
      await ctx.close();
    }
    writeFileSync(path.join(dir, 'facts.json'), `${JSON.stringify(facts, null, 2)}\n`);
    const d = facts.viewports['desktop-light'] ?? {};
    const mo = facts.viewports['mobile-light'] ?? {};
    const ok = d.status === 200 && mo.status === 200;
    if (!ok) failed++;
    const issues = [
      !ok && `HTTP ${d.status ?? d.error ?? '?'} / ${mo.status ?? mo.error ?? '?'}`,
      mo.horizontalScroll && `horizontal scroll at 360 px (page ${mo.pageWidth} px)`,
      mo.overflowing?.length && `${mo.overflowing.length} element(s) wider than 360 px`,
      d.katexErrors?.length && `${d.katexErrors.length} KaTeX error(s)`,
      d.brokenImages?.length && `${d.brokenImages.length} broken image(s)`,
      (d.h1?.length ?? 1) !== 1 && `${d.h1?.length} h1`,
      [...new Set(Object.values(facts.viewports).flatMap((v) => v.consoleErrors ?? []))].length && 'console errors',
      Object.values(facts.viewports).some((v) => v.truncated) && `captures cut at ${MAX_TILES} screens`,
    ].filter(Boolean);
    rows.push(`| ${route} | ${d.status ?? '-'} | ${d.tiles ?? 0}/${mo.tiles ?? 0}/${facts.viewports['mobile-dark']?.tiles ?? 0} | ${issues.join('; ') || 'none found'} |`);
  }
  await browser.close();
  const report = [
    `## Live captures: ${origin}`,
    '',
    `${routes.length} page(s); screenshots are tiles of one screen each (desktop light, mobile light, mobile dark). Rendering checks are leads for the live review, not a verdict.`,
    '',
    '| Page | HTTP | Tiles (D/M/Mdark) | Automatic findings |',
    '|---|---|---|---|',
    ...rows,
  ].join('\n');
  writeFileSync(path.join(out, 'index.md'), `${report}\n`);
  console.log(report);
  if (process.env.GITHUB_STEP_SUMMARY) appendFileSync(process.env.GITHUB_STEP_SUMMARY, `${report}\n`);
  return failed;
}

const [cmd, ...rest] = process.argv.slice(2);
if (cmd === 'routes') {
  const [base, head] = rest;
  if (!base || !head) throw new Error('Usage: live-capture.mjs routes <base> <head>');
  console.log(changedRoutes(base, head).join('\n'));
} else if (cmd === 'capture') {
  const fileIdx = rest.indexOf('--routes-file');
  let args = rest;
  let routes = [];
  if (fileIdx >= 0) {
    routes = readFileSync(rest[fileIdx + 1], 'utf8').split('\n').map((s) => s.trim()).filter(Boolean);
    args = rest.filter((_, i) => i !== fileIdx && i !== fileIdx + 1);
  }
  const [origin, out, ...more] = args;
  routes = [...new Set([...routes, ...more])];
  if (!origin || !out || !routes.length) throw new Error('Usage: live-capture.mjs capture <origin> <out> <route...> [--routes-file f]');
  process.exitCode = (await capture(origin, out, routes)) ? 1 : 0;
} else {
  console.log(readFileSync(new URL(import.meta.url), 'utf8').split('\n').filter((l) => l.startsWith('//')).map((l) => l.slice(3)).join('\n'));
}
