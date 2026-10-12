// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import { unified } from '@astrojs/markdown-remark';
import { remarkReadingTime } from './src/plugins/remark-reading-time.mjs';

// Set SITE_URL at build time to enable canonical URLs, sitemap and RSS links.
// Falls back to a local placeholder so dev builds never invent a domain. The placeholder must
// never reach a deployment: `npm run build` finishes with scripts/check-site-url.mjs, which fails
// the build in a deploy environment (CI, Netlify, Cloudflare Pages, Vercel) when the sitemap or RSS
// feed contains a localhost URL, and only warns on a local build (see the script's header).
const site = process.env.SITE_URL || 'http://localhost:4321';

export default defineConfig({
  site,
  trailingSlash: 'never',
  build: { format: 'file' },
  integrations: [mdx(), sitemap()],
  markdown: {
    processor: unified({
      remarkPlugins: [remarkMath, remarkReadingTime],
      rehypePlugins: [rehypeKatex],
    }),
    // 'github-dark' comments (#6A737D) are only 3.5:1 on --code-bg (dark); WCAG 1.4.3 needs 4.5:1.
    // 'github-dark-default' (comments #8b949e) clears it. See the Shiki gotcha in CLAUDE.md.
    shikiConfig: { themes: { light: 'github-light', dark: 'github-dark-default' } },
  },
});
