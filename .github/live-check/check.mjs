// Temporary live-site check for https://acrr.asia, run by .github/workflows/live-check.yml on a
// GitHub runner (the authoring environment has no internet access). Prints one RESULT line per
// check and SHOT lines carrying small base64 JPEG screenshots, so everything is readable from the
// job log. Exits 1 if any check fails.
import { chromium } from 'playwright';
import { execSync } from 'node:child_process';

const ORIGIN = process.env.ORIGIN || 'https://acrr.asia';
let failures = 0;
const result = (ok, name, detail = '') => {
  if (!ok) failures++;
  console.log(`RESULT ${ok ? 'PASS' : 'FAIL'} | ${name}${detail ? ' | ' + detail : ''}`);
};
const sh = (cmd) => {
  try { return execSync(cmd, { encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] }).trim(); }
  catch (e) { return `ERR ${String(e.stdout || '')}${String(e.stderr || '')}`.trim(); }
};

// 1. DNS, HTTPS, redirects
console.log('DNS A ' + sh('dig +short A acrr.asia | tr "\\n" " "'));
console.log('DNS AAAA ' + sh('dig +short AAAA acrr.asia | tr "\\n" " "'));
console.log('DNS www ' + sh('dig +short www.acrr.asia | tr "\\n" " "'));
const cert = sh(`curl -sSv -o /dev/null ${ORIGIN}/ 2>&1 | grep -iE "subject:|issuer:|expire date|SSL certificate verify"`);
console.log('CERT ' + cert.replace(/\n/g, ' / '));
result(/verify ok/i.test(cert), 'HTTPS certificate valid', cert.split('\n').find((l) => /expire/i.test(l)) || '');
const httpRedirect = sh(`curl -sS -o /dev/null -w "%{http_code} %{redirect_url}" http://acrr.asia/`);
result(/^30[1278] https:\/\/acrr\.asia\/?$/.test(httpRedirect), 'http:// redirects to https://', httpRedirect);
const www = sh(`curl -sS -o /dev/null -w "%{http_code} %{redirect_url}" https://www.acrr.asia/`);
result(/^30[1278] https:\/\/acrr\.asia\/?$/.test(www), 'www redirects to apex', www);

// 2. Status codes and text checks on every page
const fetchText = async (path) => {
  const r = await fetch(ORIGIN + path, { redirect: 'manual' });
  return { status: r.status, text: r.status === 200 ? await r.text() : '' };
};
const pages = ['/', '/blog', '/series', '/insights', '/about', '/learning', '/tags', '/rss.xml',
  '/sitemap-index.xml', '/robots.txt', '/CNAME'];
const sitemapIndex = (await fetchText('/sitemap-index.xml')).text;
for (const sm of [...sitemapIndex.matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1])) {
  const xml = await (await fetch(sm)).text();
  for (const m of xml.matchAll(/<loc>([^<]+)<\/loc>/g)) pages.push(new URL(m[1]).pathname);
}
const unique = [...new Set(pages)];
const bad = [];
const labelled = [];
const html = {};
for (const p of unique) {
  const { status, text } = await fetchText(p);
  if (status !== 200) bad.push(`${p}=${status}`);
  html[p] = text;
  if (/\[Example\]|class="badge notice">Example|illustrative example|sample content|Example article:|Example insight:|Example series:/i.test(text)) labelled.push(p);
}
result(bad.length === 0, `All ${unique.length} pages from the sitemap and nav return 200`, bad.join(', '));
result(labelled.length === 0, 'No "Example"/sample labels on any page', labelled.join(', '));
const nf = await fetchText('/does-not-exist');
const nfBody = await (await fetch(ORIGIN + '/does-not-exist')).text();
result(nf.status === 404 && /ACRR/.test(nfBody), '404 page is the site\'s own', `status ${nf.status}`);
result((html['/CNAME'] || '').trim() === 'acrr.asia', 'CNAME is acrr.asia');
result(/Sitemap: https:\/\/acrr\.asia\/sitemap-index\.xml/.test(html['/robots.txt'] || ''), 'robots.txt Sitemap line');
const rss = html['/rss.xml'] || '';
result(/<link>https:\/\/acrr\.asia\//.test(rss) && !/localhost|\[Example\]/.test(rss), 'RSS uses https://acrr.asia, no [Example]',
  `${(rss.match(/<item>/g) || []).length} items`);
result(unique.includes('/blog/token-based-authentication'), 'Token article is in the sitemap');

// 3. Browser checks
const browser = await chromium.launch();
const articles = {
  'introduction-to-control-systems': { svg: 2, mermaid: 0 },
  'feedback-and-system-behavior': { svg: 2, mermaid: 0 },
  'state-space-models-primer': { svg: 2, mermaid: 0 },
  'numerical-integration-notes': { svg: 1, mermaid: 0 },
  'token-based-authentication': { svg: 0, mermaid: 5 },
};
const shot = async (locator, name) => {
  const buf = await locator.screenshot({ type: 'jpeg', quality: 55, scale: 'css' });
  console.log(`SHOT ${name} ${buf.toString('base64')}`);
};
for (const scheme of ['light', 'dark']) {
  const page = await browser.newPage({ viewport: { width: 1200, height: 900 }, colorScheme: scheme });
  const errors = [];
  page.on('pageerror', (e) => errors.push(e.message));
  page.on('console', (m) => { if (m.type() === 'error') errors.push(m.text()); });
  for (const [slug, want] of Object.entries(articles)) {
    await page.goto(`${ORIGIN}/blog/${slug}`, { waitUntil: 'networkidle' });
    const counts = await page.evaluate(() => ({
      svg: document.querySelectorAll('svg.diagram-svg').length,
      mermaid: document.querySelectorAll('figure.mermaid-diagram svg').length,
      mermaidCode: document.querySelectorAll('pre[data-language="mermaid"], code.language-mermaid').length,
      canonical: document.querySelector('link[rel=canonical]')?.href,
      ogUrl: document.querySelector('meta[property="og:url"]')?.content,
      title: document.title,
      katex: document.querySelectorAll('.katex').length,
      // every diagram actually drew something with a non-zero box
      drawn: [...document.querySelectorAll('figure.diagram svg')].every((s) => {
        const r = s.getBoundingClientRect();
        return r.width > 100 && r.height > 50 && s.querySelectorAll('path,rect,line,circle,polygon').length > 3;
      }),
    }));
    if (scheme === 'light') {
      result(counts.svg === want.svg && counts.mermaid === want.mermaid && counts.mermaidCode === 0 && counts.drawn,
        `Diagrams render on /blog/${slug}`, `svg=${counts.svg} mermaid=${counts.mermaid} mermaid-as-code=${counts.mermaidCode} drawn=${counts.drawn}`);
      result(counts.canonical === `${ORIGIN}/blog/${slug}` && counts.ogUrl === `${ORIGIN}/blog/${slug}`,
        `Canonical/og:url on /blog/${slug}`, String(counts.canonical));
      console.log(`INFO ${slug} title="${counts.title}" katex=${counts.katex}`);
    }
    const figs = page.locator('figure.diagram');
    const n = await figs.count();
    const pick = slug === 'token-based-authentication' ? [1, 4] : slug === 'numerical-integration-notes' ? [0] : scheme === 'dark' ? [] : [0];
    for (const i of pick) if (i < n) { await figs.nth(i).scrollIntoViewIfNeeded(); await shot(figs.nth(i), `${scheme}-${slug}-${i}`); }
  }
  result(errors.length === 0, `No console/page errors (${scheme})`, errors.slice(0, 3).join(' ; '));
  await page.close();
}

// Narrow screen
const mobile = await browser.newPage({ viewport: { width: 360, height: 780 } });
const wide = [];
for (const p of ['/', '/blog', ...Object.keys(articles).map((s) => `/blog/${s}`)]) {
  await mobile.goto(ORIGIN + p, { waitUntil: 'networkidle' });
  const sw = await mobile.evaluate(() => document.documentElement.scrollWidth);
  if (sw > 360) wide.push(`${p}=${sw}`);
}
result(wide.length === 0, 'No page-level horizontal scroll at 360px', wide.join(', '));
await mobile.goto(`${ORIGIN}/blog/token-based-authentication`, { waitUntil: 'networkidle' });
await shot(mobile.locator('figure.mermaid-diagram').first(), 'mobile-token-0');
await mobile.goto(ORIGIN + '/', { waitUntil: 'networkidle' });
await shot(mobile.locator('body'), 'mobile-home');

// Search
const sp = await browser.newPage({ viewport: { width: 1200, height: 900 } });
await sp.goto(ORIGIN + '/blog', { waitUntil: 'networkidle' });
const search = async (q) => {
  await sp.keyboard.press('Control+k');
  await sp.locator('#site-search-input').waitFor({ state: 'visible' });
  await sp.fill('#site-search-input', q);
  await sp.waitForFunction(() => /result|No results/i.test(document.querySelector('#site-search-status')?.textContent || ''), null, { timeout: 15000 }).catch(() => {});
  await sp.waitForTimeout(800);
  const status = await sp.textContent('#site-search-status');
  const titles = await sp.locator('#site-search-results a').allTextContents();
  await sp.keyboard.press('Escape');
  return { status: (status || '').trim(), titles: titles.map((t) => t.trim()) };
};
const k = await search('kalman');
result(k.titles.some((t) => /Kalman Filter Enough/i.test(t)), 'Search "kalman" finds the Kalman insight', `${k.status} :: ${k.titles.join(' | ')}`);
const e = await search('eigenvalues');
result(e.titles.length > 0, 'Search "eigenvalues" returns results', `${e.status} :: ${e.titles.join(' | ')}`);
const j = await search('jwt');
result(j.titles.some((t) => /Token-Based Authentication/i.test(t)), 'Search "jwt" finds the token article', `${j.status} :: ${j.titles.join(' | ')}`);
const z = await search('zzzqqq');
result(/No results/i.test(z.status), 'Search "zzzqqq" shows No results', z.status);

await browser.close();
console.log(`SUMMARY ${failures === 0 ? 'ALL PASS' : failures + ' FAILED'}`);
process.exit(failures === 0 ? 0 : 1);
