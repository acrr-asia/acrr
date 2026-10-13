#!/usr/bin/env node
/**
 * Post-build guard: the sitemap and the RSS feed must not point at a placeholder host.
 *
 *   node scripts/check-site-url.mjs [distDir] [--allow-localhost]
 *
 * astro.config.mjs falls back to http://localhost:4321 when SITE_URL is not set, so that dev builds
 * never invent a domain. That fallback is written into dist/sitemap-index.xml, dist/sitemap-*.xml and
 * dist/rss.xml (every <loc>, <link> and <guid>). A deployment built without SITE_URL would therefore
 * publish a sitemap and a feed that send crawlers and feed readers to localhost.
 *
 * `npm run build` runs this script as its LAST step (after `pagefind --site dist`, so a failure never
 * leaves a dist/ without a search index). What it does depends on where the build runs:
 *
 *   - Recognised deploy environment (CI, GITHUB_ACTIONS, NETLIFY, CF_PAGES or VERCEL is set):
 *     localhost URLs FAIL the build (exit 1). Set SITE_URL to the public origin.
 *   - Anywhere else (a plain local `npm run build`): the problem is printed as a WARNING and the
 *     build still succeeds (exit 0), because a local build is normally for previewing. Do not deploy
 *     that dist/.
 *   - Explicitly allowed (`--allow-localhost`, ALLOW_LOCALHOST_BUILD=1, or `npm run build:local`):
 *     warning only, in every environment. Use this for a CI smoke test that is not a deployment.
 *
 * A URL counts as a placeholder when its host is localhost, *.localhost, 127.0.0.1, 0.0.0.0 or ::1.
 *
 * Exit codes: 0 = clean, or placeholder hosts found but tolerated (local build / explicitly allowed),
 * 1 = placeholder hosts found in a deploy environment, 2 = dist missing or no sitemap/RSS to check.
 */
import { existsSync, readdirSync, readFileSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const projectRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const args = process.argv.slice(2);
const allowFlag = args.includes('--allow-localhost');
const distDir = path.resolve(args.find((a) => !a.startsWith('--')) ?? path.join(projectRoot, 'dist'));
const isSet = (name) => {
  const value = (process.env[name] ?? '').trim().toLowerCase();
  return value !== '' && value !== '0' && value !== 'false';
};
const allowEnv = isSet('ALLOW_LOCALHOST_BUILD');
const allowed = allowFlag || allowEnv;

/** Environment variables that mean "this build is probably being deployed". */
const DEPLOY_ENV_VARS = ['CI', 'GITHUB_ACTIONS', 'NETLIFY', 'CF_PAGES', 'VERCEL'];
const deployEnv = DEPLOY_ENV_VARS.filter(isSet);

if (!existsSync(distDir)) {
  console.error(`check-site-url: "${distDir}" does not exist. Run the Astro build first.`);
  process.exit(2);
}

/** Files whose URLs are published to crawlers and feed readers. */
// The Vietnamese feed is vi/rss.xml (see src/pages/vi/rss.xml.ts).
const targets = [
  ...readdirSync(distDir).filter((name) => name === 'rss.xml' || /^sitemap(-[^/\\]+)?\.xml$/.test(name)),
  ...(existsSync(path.join(distDir, 'vi', 'rss.xml')) ? ['vi/rss.xml'] : []),
].sort();

if (targets.length === 0) {
  console.error(`check-site-url: found no rss.xml or sitemap*.xml in "${distDir}". Nothing to check.`);
  process.exit(2);
}

const isPlaceholderHost = (hostname) => {
  const host = hostname.toLowerCase().replace(/^\[|\]$/g, '');
  return host === 'localhost' || host.endsWith('.localhost') || host === '127.0.0.1' || host === '0.0.0.0' || host === '::1';
};

const URL_RE = /https?:\/\/[^\s"'<>\]]+/gi;

const offenders = []; // { file, count, example }
for (const name of targets) {
  const text = readFileSync(path.join(distDir, name), 'utf8');
  let count = 0;
  let example = '';
  for (const [raw] of text.matchAll(URL_RE)) {
    let hostname;
    try {
      hostname = new URL(raw).hostname;
    } catch {
      continue;
    }
    if (isPlaceholderHost(hostname)) {
      count++;
      example ||= raw;
    }
  }
  if (count > 0) offenders.push({ file: name, count, example });
}

if (offenders.length === 0) {
  console.log(`check-site-url: ok (${targets.join(', ')}: no localhost URLs).`);
  process.exit(0);
}

const lines = offenders.map((o) => `  ${o.file}: ${o.count} URL${o.count === 1 ? '' : 's'} (for example ${o.example})`);

if (allowed) {
  console.warn(
    [
      '',
      'check-site-url: WARNING. The sitemap/RSS output contains localhost URLs:',
      ...lines,
      'Allowed for this build (ALLOW_LOCALHOST_BUILD / --allow-localhost / npm run build:local).',
      'Do NOT deploy this dist/. Set SITE_URL and run "npm run build" for a deployable build.',
      '',
    ].join('\n'),
  );
  process.exit(0);
}

if (deployEnv.length === 0) {
  console.warn(
    [
      '',
      'check-site-url: WARNING. SITE_URL is not set, so the sitemap/RSS output contains localhost URLs:',
      ...lines,
      'That is fine for a local preview (npm run preview). Do NOT deploy this dist/.',
      'For a deployable build set SITE_URL to the public origin and build again. In a deploy environment',
      `(${DEPLOY_ENV_VARS.join(', ')}) this check fails the build instead of warning.`,
      '',
    ].join('\n'),
  );
  process.exit(0);
}

console.error(
  [
    '',
    `check-site-url: FAILED. The sitemap/RSS output contains localhost URLs (deploy environment detected: ${deployEnv.join(', ')}):`,
    ...lines,
    '',
    'This build was made without SITE_URL, so deploying it would point crawlers and feed readers at',
    'localhost. Set SITE_URL to the public origin (no trailing slash) and build again:',
    '',
    '  SITE_URL=https://your-domain.example npm run build           (macOS / Linux / Git Bash)',
    '  $env:SITE_URL = "https://your-domain.example"; npm run build  (PowerShell)',
    '',
    'For a CI run that is not a deployment (a smoke test), use "npm run build:local" or set',
    'ALLOW_LOCALHOST_BUILD=1.',
    '',
  ].join('\n'),
);
process.exit(1);
