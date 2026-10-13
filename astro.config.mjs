// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import { unified } from '@astrojs/markdown-remark';
import rehypeMermaid from 'rehype-mermaid';
import { remarkReadingTime } from './src/plugins/remark-reading-time.mjs';
import { rehypeMermaidFigure } from './src/plugins/rehype-mermaid-figure.mjs';

// Set SITE_URL at build time to enable canonical URLs, sitemap and RSS links.
// Falls back to a local placeholder so dev builds never invent a domain. The placeholder must
// never reach a deployment: `npm run build` finishes with scripts/check-site-url.mjs, which fails
// the build in a deploy environment (CI, Netlify, Cloudflare Pages, Vercel) when the sitemap or RSS
// feed contains a localhost URL, and only warns on a local build (see the script's header).
const site = process.env.SITE_URL || 'http://localhost:4321';

/** @type {import('rehype-mermaid').RehypeMermaidOptions} */
const mermaidOptions = {
  strategy: 'inline-svg',
  mermaidConfig: {
    theme: 'neutral',
    fontFamily: "ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif",
    // Compact layout: the article column is about 40rem wide, so wide diagrams would
    // otherwise be scaled down until their labels are unreadable.
    flowchart: { nodeSpacing: 30, rankSpacing: 40, padding: 10, wrappingWidth: 180 },
    sequence: { wrap: true, width: 130, actorMargin: 30, boxMargin: 8, messageMargin: 30, noteMargin: 8 },
  },
  errorFallback: (_element, _diagram, error, file) => {
    throw new Error(`Mermaid diagram failed to render in ${file.path}: ${error}`);
  },
};

export default defineConfig({
  site,
  trailingSlash: 'never',
  build: { format: 'file' },
  // The sitemap pairs /x with /vi/x (hreflang alternates) wherever both pages exist.
  integrations: [mdx(), sitemap({ i18n: { defaultLocale: 'en', locales: { en: 'en', vi: 'vi' } } })],
  markdown: {
    processor: unified({
      remarkPlugins: [remarkMath, remarkReadingTime],
      rehypePlugins: [
        rehypeKatex,
        // ```mermaid blocks become inline SVG at build time (headless Chromium via Playwright; see
        // README "Diagrams"). The 'neutral' theme is recoloured with the site's tokens in prose.css,
        // so diagrams follow dark mode. A diagram with a syntax error fails the build.
        [rehypeMermaid, mermaidOptions],
        rehypeMermaidFigure,
      ],
    }),
    // Mermaid blocks are left to rehype-mermaid instead of Shiki.
    syntaxHighlight: { type: 'shiki', excludeLangs: ['mermaid', 'math'] },
    // 'github-dark' comments (#6A737D) are only 3.5:1 on --code-bg (dark); WCAG 1.4.3 needs 4.5:1.
    // 'github-dark-default' (comments #8b949e) clears it. See the Shiki gotcha in CLAUDE.md.
    shikiConfig: { themes: { light: 'github-light', dark: 'github-dark-default' } },
  },
});
