#!/usr/bin/env node
// Post-publication verification: does the live site serve what the build produced?
// Dependency-free, like the other scripts. Used by the "verify" job of .github/workflows/deploy.yml.
//
//   node scripts/verify-live.mjs manifest [distDir]            JSON manifest of every sitemap page:
//                                                              route and the text of its <h1>
//   node scripts/verify-live.mjs check <origin> <manifest.json> [--attempts N] [--delay S] [--only <prefix>]
//
// `check` fetches every route of the manifest from <origin> (for example https://acrr.asia) and
// requires HTTP 200 and the same <h1> text as the build. Pages that fail are retried, because a
// GitHub Pages deployment can take a little while to reach every edge server. It writes a Markdown
// report to stdout (and to $GITHUB_STEP_SUMMARY when set) and exits 1 if any page still fails.
import { appendFileSync, existsSync, readFileSync, readdirSync } from 'node:fs';
import path from 'node:path';

const decode = (s) =>
  s
    .replace(/&#x([0-9a-f]+);/gi, (_, h) => String.fromCodePoint(parseInt(h, 16)))
    .replace(/&#(\d+);/g, (_, d) => String.fromCodePoint(Number(d)))
    .replace(/&quot;/g, '"')
    .replace(/&apos;|&#39;/g, "'")
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&amp;/g, '&');

/** Text of the first <h1>, tags stripped and whitespace collapsed. */
export function h1Text(html) {
  const m = /<h1\b[^>]*>([\s\S]*?)<\/h1>/i.exec(html);
  return m ? decode(m[1].replace(/<[^>]+>/g, ' ')).replace(/\s+/g, ' ').trim() : null;
}

function manifest(dist) {
  if (!existsSync(dist)) throw new Error(`${dist} does not exist; build first.`);
  const sitemaps = readdirSync(dist).filter((f) => /^sitemap-\d+\.xml$/.test(f));
  if (!sitemaps.length) throw new Error(`No sitemap-N.xml in ${dist}.`);
  const pages = [];
  for (const sm of sitemaps) {
    for (const [, loc] of readFileSync(path.join(dist, sm), 'utf8').matchAll(/<loc>([^<]+)<\/loc>/g)) {
      const route = new URL(loc).pathname;
      const file = route === '/' ? 'index.html' : `${route.replace(/^\//, '').replace(/\/$/, '/index')}.html`;
      const abs = path.join(dist, file);
      if (!existsSync(abs)) throw new Error(`Sitemap lists ${route} but ${file} is not in ${dist}.`);
      pages.push({ route, h1: h1Text(readFileSync(abs, 'utf8')) });
    }
  }
  return pages.sort((a, b) => a.route.localeCompare(b.route));
}

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function checkPage(origin, page) {
  try {
    // Cache-busting query: a stale edge copy must not hide a failed deployment.
    const res = await fetch(`${origin}${page.route}?verify=${Date.now()}`, { redirect: 'follow' });
    if (res.status !== 200) return `HTTP ${res.status}`;
    const live = h1Text(await res.text());
    if (live !== page.h1) return `h1 is "${live}", expected "${page.h1}"`;
    return null;
  } catch (err) {
    return `fetch failed: ${err.message}`;
  }
}

async function check(origin, manifestPath, { attempts, delay, only }) {
  origin = origin.replace(/\/$/, '');
  let pending = JSON.parse(readFileSync(manifestPath, 'utf8')).filter((p) => !only || p.route.startsWith(only));
  const total = pending.length;
  const errors = new Map();
  for (let attempt = 1; attempt <= attempts && pending.length; attempt++) {
    if (attempt > 1) await sleep(delay * 1000);
    const results = [];
    for (let i = 0; i < pending.length; i += 8) {
      const batch = pending.slice(i, i + 8);
      results.push(...(await Promise.all(batch.map(async (p) => [p, await checkPage(origin, p)]))));
    }
    pending = [];
    for (const [p, err] of results) {
      if (err) {
        errors.set(p.route, err);
        pending.push(p);
      } else errors.delete(p.route);
    }
    console.error(`attempt ${attempt}: ${total - pending.length}/${total} pages verified`);
  }
  const lines = [
    `## Live verification of ${origin}: ${errors.size ? 'FAILED' : 'passed'}`,
    '',
    `${total - errors.size} of ${total} pages return HTTP 200 with the expected title.`,
  ];
  if (errors.size) lines.push('', ...[...errors].map(([route, err]) => `- \`${route}\`: ${err}`));
  const report = lines.join('\n');
  console.log(report);
  if (process.env.GITHUB_STEP_SUMMARY) appendFileSync(process.env.GITHUB_STEP_SUMMARY, `${report}\n`);
  return errors.size === 0;
}

const argv = process.argv.slice(2);
const opt = (name, fallback) => {
  const i = argv.indexOf(name);
  return i >= 0 ? argv[i + 1] : fallback;
};
try {
  if (argv[0] === 'manifest') {
    console.log(JSON.stringify(manifest(argv[1] && !argv[1].startsWith('--') ? argv[1] : 'dist'), null, 2));
  } else if (argv[0] === 'check' && argv[1] && argv[2]) {
    const ok = await check(argv[1], argv[2], {
      attempts: Number(opt('--attempts', 10)),
      delay: Number(opt('--delay', 30)),
      only: opt('--only', null),
    });
    process.exit(ok ? 0 : 1);
  } else {
    console.error('Usage: node scripts/verify-live.mjs manifest [distDir] | check <origin> <manifest.json> [--attempts N] [--delay S] [--only <prefix>]');
    process.exit(2);
  }
} catch (err) {
  console.error(err.message);
  process.exit(1);
}
