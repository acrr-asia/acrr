# ACRR — Advanced Computing & Robotics Research

A static, English-language research and technical publishing site. It has six sections: **Home**, **Blog**, **Series**, **Learning**, **Insights** and **About**, plus a **Tags** index (linked from the footer and from every tag). There is no backend and no database. The site is built with Astro, content lives in Markdown/MDX files with validated frontmatter, and the output is a folder of plain files (`dist/`) that any static host can serve.

> **About the content.** Everything currently published in this repository is **sample content** and is labelled as such (`example: true` in frontmatter, plus a visible "Example" badge or notice). It illustrates the formats; it is not original research. **No founder biography, credentials, affiliations, publications, contact details or statistics have been supplied, so none appear on the site.** The five research areas are *proposed areas of interest*, not claims of active projects or a staffed laboratory. No Notion pages exist yet, so Learning entries show "Coming soon" and carry no link. See [Content rules](#content-rules).

The full specification is in [idea-plan.md](idea-plan.md).

## Requirements

- **Node.js 22.12 or newer** (this is what Astro 7 requires; `package.json` declares it in `engines`). Older Node versions, including Node 20, will not run this project.
- npm 9.6.5 or newer (bundled with Node 22).

## Install and run

```sh
npm install
npm run dev
```

`npm run dev` starts the dev server on <http://localhost:4321>. In dev:

- **Draft content is visible** (labelled "Draft") so you can preview unfinished work. It is excluded from every production listing, route, RSS item, sitemap entry and search index.
- **Search does not work.** The search index is created by Pagefind *after* a production build, so the search dialog tells you to build first.

## Commands

| Command | What it does |
| --- | --- |
| `npm run dev` | Dev server with hot reload. Drafts are shown. |
| `npm run build` | `astro check` (type and template checks), then `astro build` (writes `dist/`), then `pagefind --site dist` (writes the search index to `dist/pagefind/`), then `scripts/check-site-url.mjs` (looks for `localhost` URLs in the sitemap and RSS feed, which appear when `SITE_URL` is not set). Fails on any type or content-schema error. Works with no setup for a local build; **set `SITE_URL` for every build you intend to deploy** (see [Site URL](#site-url-seo-sitemap-and-rss)). |
| `npm run build:local` | The same build, but `localhost` URLs in the sitemap and feed only print a warning, even in CI. For smoke tests that are not a deployment; do not deploy the resulting `dist/`. |
| `npm run preview` | Serves the already-built `dist/` locally, so you can test the real output, including search. Run `npm run build` first. |
| `npm run check` | Type and template checks only (`astro check`). |
| `npm run check:links` | Checks every internal `href`, `src` and `srcset` in `dist/` (including `#fragment` targets) against the built files. Exits non-zero on any broken link. Run a build first. |
| `npm run check:site-url` | Runs only the `localhost` guard on an existing `dist/` (`--allow-localhost` turns the failure into a warning). |

Typical release check: `SITE_URL=https://your-domain.example npm run build && npm run check:links`.

A plain `npm run build` with no `SITE_URL` succeeds locally and prints a warning that the sitemap and feed point at `localhost`; that `dist/` is fine for `npm run preview` but must not be deployed.

To stop a preview server that is still running in the background: `npx astro preview stop`.

## Project layout

```
src/
  content/
    blog/        Articles (.md / .mdx), one file per article
    series/      Series definitions (.md), one file per series
    insights/    Short-form pieces (.md)
  data/
    learning.json   Learning resource index (real URLs go here)
  content.config.ts Collection schemas (the source of truth for frontmatter)
  pages/            Routes (index, about, learning, blog/, series/, insights/, tags/, 404, rss.xml)
  layouts/          Base.astro (page shell) and Article.astro (article layout)
  components/       Header, Footer, SEO, Search, cards, badges, home sections
  components/home/research-areas.ts   The five proposed research areas (Home and About)
  lib/content.ts    Shared queries (drafts excluded in production), formatDate, slugify, tagSlug, getTagIndex
  lib/path.ts       publicPath(): the extensionless public route for Astro.url.pathname
  plugins/          remark-reading-time.mjs
  styles/           tokens.css (design tokens), global.css, prose.css
public/             favicon.svg, robots.txt (copied to dist/ unchanged)
scripts/check-links.mjs      Internal link checker for dist/
scripts/check-site-url.mjs   Warns (local) or fails (CI/deploy) when the sitemap/RSS contain localhost URLs
pagefind.yml        Search-indexing options
astro.config.mjs
```

## Writing content

Frontmatter is validated by `src/content.config.ts`. A missing required field, a wrong type, an unknown category or a series id that does not exist fails the build with a message naming the file. The file name (without extension) becomes the URL slug, so `src/content/blog/my-post.mdx` is served at `/blog/my-post`.

### Categories

`category` must be exactly one of: `Research Notes`, `Technical Tutorials`, `Engineering`, `AI and Machine Learning`, `Robotics and Control`, `Computing Systems`, `Mathematical Foundations`. To add a category, edit the `CATEGORIES` list in `src/content.config.ts`. Blog category pages (`/blog/category/<slug>`) are generated automatically for categories that have at least one published article. Tag pages work the same way, see below.

### Blog articles — `src/content/blog/<slug>.md` or `.mdx`

| Field | Required | Notes |
| --- | --- | --- |
| `title` | yes | String. |
| `description` | yes | One or two sentences. Used on cards, in `<meta name="description">` and in RSS. |
| `publishedAt` | yes | Date, e.g. `2026-10-11`. Archive and RSS are sorted newest first. |
| `updatedAt` | no | Date; shown as "Updated …" on the article. |
| `category` | yes | One of the categories above. |
| `tags` | no | List of strings. Default `[]`. Related articles are scored from shared tags and category. Each tag links to a generated page, `/tags/<slug>`, listing every published article and insight with that tag; `/tags` lists them all with counts. The slug drops accents and case (`Kálmán` → `kalman`), writes `+` as `plus` and `#` as `sharp`, so `C++` and `C#` stay distinct. Spelling variants that differ only in case or spacing (`Control Theory`, `control-theory`) share one page. Two tags that are genuinely different but would get the same slug fail the build with a message naming both. A tag used only by drafts has no page in production. |
| `draft` | no | `true` keeps the article out of production. Default `false`. |
| `example` | no | `true` labels the article as sample content (badge and notice). Default `false`. |
| `series` | no | The `id` (file name without `.md`) of a series in `src/content/series`. Must exist. |
| `seriesOrder` | no | Positive integer, the article's position in its series. |

```yaml
---
title: "Feedback and System Behavior"
description: "How closing the loop changes the speed of a first-order system and its sensitivity to disturbances."
publishedAt: 2026-09-20
category: "Robotics and Control"
tags: [control-theory, feedback]
series: foundations-of-control-systems
seriesOrder: 1
draft: false
example: true
---
```

Article bodies support GitHub-flavoured Markdown, MDX, syntax-highlighted code blocks (Shiki, light and dark themes), and LaTeX maths via KaTeX: `$a^2$` inline and `$$ ... $$` as a block. Reading time is calculated automatically from the article text. Every article page also gets a "Contents" aside built from its `##` and `###` headings (shown when there are at least two), older/newer article links based on publication date, and, for series articles, a series block with previous/next within the series.

### Series — `src/content/series/<id>.md`

| Field | Required | Notes |
| --- | --- | --- |
| `title`, `description` | yes | |
| `category` | yes | One of the categories above. |
| `objectives` | no | List of learning objectives. |
| `status` | no | `planned` (default), `in-progress` or `published`. Set this by hand; it is not inferred. |
| `plannedEntries` | no | List of `{ title, description? }` for entries not yet written. Shown as "Planned" with no link. |
| `example` | no | `true` labels the series as illustrative. |

The Markdown body below the frontmatter is shown as an introduction on the series page.

**Adding an entry to a series:**

1. Create the article in `src/content/blog/` with `series: <series-id>` and a `seriesOrder`.
2. If it was listed under `plannedEntries`, remove it from there so it is not shown twice.
3. Update the series `status` when it changes.

The series page lists published articles in `seriesOrder`, then the remaining planned entries. Progress ("2 of 4 entries published") is computed from the published articles and the planned entries; drafts never count.

### Insights — `src/content/insights/<id>.md`

| Field | Required | Notes |
| --- | --- | --- |
| `title`, `description` | yes | |
| `publishedAt` | yes | Date. |
| `kind` | yes | `Concept explanation`, `Engineering observation`, `Comparison`, `Research question`, `Methodological note` or `Emerging idea`. |
| `tags` | no | List of strings. Same tag pages as for articles (`/tags/<slug>` lists both). |
| `draft`, `example` | no | Same meaning as for articles. |

Each insight should keep three things apart, as three `##` sections: **Established** (facts that are well supported), **Interpretation** (how those facts are read), and **Open questions**.

### Draft versus example

These are different flags and are independent:

- `draft: true` means *unfinished*. The entry exists only under `npm run dev`. It is absent from production pages, the blog archive, tag pages (a tag that only drafts use has no page), series pages, home page, RSS, sitemap and the search index.
- `example: true` means *sample content that is published*. It appears in production with an "Example" badge and a notice that it is not original research. The label is also carried outside the page body so that a sample is not mistaken for real work: `[Example]` in the browser `<title>` and in RSS item titles, an "Example article/insight/series:" prefix on the meta and Open Graph description, and an "Example" badge on search results. Remove the flag (and the "example" wording in the text) only when the content is real.

Do not publish invented material as real. When replacing sample content with real writing, delete the sample file rather than editing it into something that looks like research.

### Learning resources — `src/data/learning.json`

A JSON array. Each object needs a unique `id`:

| Field | Required | Notes |
| --- | --- | --- |
| `id` | yes | Unique string. |
| `title`, `description` | yes | |
| `topic` | yes | Entries are grouped by this on the page. |
| `type` | yes | `Study notes`, `Course`, `Book`, `External reference` or `Learning path`. |
| `status` | no | `planned` (default), `in-progress` or `published`. |
| `url` | no | A real, valid URL. **Leave it out until the resource actually exists.** |

An entry without `url` is shown as **Coming soon** with no link. The Learning page itself contains no editing instructions for visitors; this section is where they live. To publish a real resource (for example a Notion page once it exists), add its genuine `url` to the entry and set `status`; the page picks it up with an "Open resource" link and no redesign. Never put a placeholder or guessed URL here. An invalid URL fails the build.

### Home and About text

The five proposed research areas are defined once in `src/components/home/research-areas.ts` and used on both pages. The wording of the About page is in `src/pages/about.astro`. Personal information (biography, credentials, affiliations, contact details) should be added there only when the site's author supplies it.

## Site URL, SEO, sitemap and RSS

Set `SITE_URL` at build time to the site's public origin, with no trailing slash:

```sh
SITE_URL=https://your-domain.example npm run build        # macOS / Linux / Git Bash
$env:SITE_URL = "https://your-domain.example"; npm run build   # PowerShell
```

`SITE_URL` controls:

- `<link rel="canonical">` and `og:url` on every page (omitted on the 404 page);
- the absolute URLs in `sitemap-index.xml` / `sitemap-0.xml`;
- the absolute links in `rss.xml`.

If `SITE_URL` is not set the build falls back to `http://localhost:4321`, so that no domain is ever invented. In that mode canonical tags are deliberately **omitted**, and the sitemap and RSS contain `localhost` URLs. To make sure such a build cannot be deployed by accident, `npm run build` ends with `scripts/check-site-url.mjs` (after Pagefind, so a failure never leaves a `dist/` without a search index), which looks for a `localhost`, `127.0.0.1` or `*.localhost` URL in `dist/sitemap-*.xml` and `dist/rss.xml`:

- **Local build** (none of the variables below set): prints a warning and the build **succeeds**, so `npm run build` works on a fresh checkout. Use that `dist/` for `npm run preview`, never for deployment.
- **Deploy environment** (`CI`, `GITHUB_ACTIONS`, `NETLIFY`, `CF_PAGES` or `VERCEL` is set to a non-empty value other than `0` or `false`): the build **fails (exit 1)**. Set `SITE_URL` to the public origin.
- **Explicitly allowed** (`npm run build:local`, `ALLOW_LOCALHOST_BUILD=1`, or `--allow-localhost`): warning only, in every environment. For a CI smoke test that is not a deployment.

So **set `SITE_URL` for every production build**.

After deploying, add a `Sitemap: <your-origin>/sitemap-index.xml` line to `public/robots.txt`. The site assumes it is served from the root of its domain (there is no `base` path configured).

Every page has its own `<title>` and meta description, a skip link, one `<h1>`, and respects the visitor's light/dark preference.

## Search

Press `Ctrl+K` / `Cmd+K`, or use the Search button in the header. Search is Pagefind, which indexes the built HTML in `dist/` and loads on first use. It indexes published content pages only: articles, insights, series pages, About and Learning. The listing pages (home, the blog archive and category pages, the tags index and tag pages, the series and insights indexes) and the 404 page are not indexed, so a search returns each piece once, under its own title, rather than also returning the lists that link to it. Sample content shows an "Example" badge in the results. To keep a new listing page out of the index, pass `searchable={false}` to `Base.astro`; to keep a block inside an indexed page out of the excerpts, add `data-pagefind-ignore` to it. `pagefind.yml` excludes KaTeX's duplicate renderings of formulas so excerpts read correctly. Pagefind silently falls back to shorter prefixes of a word that is not on the site (searching "kalman" would otherwise match any page with a word starting "k"), so the dialog keeps only results whose page text contains every query term as the start of a word, plus simple inflections such as plurals and "-ing" forms. A word that is not on the site shows "No results". Esc closes the dialog on the first press.

## Deploying

`npm run build` produces a fully static site in `dist/`. Deploy that folder to any static host. No server-side runtime is required.

General notes (the details depend on your provider; no account or hosting service is configured in this repository):

- **Build settings.** Build command `npm run build`, output directory `dist`, Node version 22.12 or newer, and the `SITE_URL` environment variable set to the public origin. On Netlify, Cloudflare Pages, Vercel and CI the build fails if `SITE_URL` is missing, which is intended: it stops a localhost sitemap and feed from being published.
- **Cloudflare Pages / Netlify.** Connect the repository (or upload `dist/`) with the settings above. Both serve a top-level `404.html` as the not-found page and resolve extensionless URLs such as `/blog` to `blog.html`.
- **GitHub Pages.** Publish the contents of `dist/` (for example from a workflow that runs the build and uploads `dist/`). `404.html` is used as the not-found page. Because routes assume the domain root, use a custom domain or a user/organisation site rather than a project sub-path, or configure `base` in `astro.config.mjs` (links in the source are written as root-relative paths and would then need adjusting).
- **Any other static host / your own server.** Serve `dist/` as-is. Routes are *extensionless* (`/blog`, `/blog/<slug>`) and the files are named `blog.html`, `blog/<slug>.html` (Astro `build.format: 'file'`). The host must try `<path>.html` for a request to `<path>`. In nginx that is `try_files $uri $uri.html $uri/ =404;`, and the not-found page is `404.html`.
- Run `npm run check:links` before deploying to catch broken internal links.

## Content rules

These are acceptance criteria for this project, not suggestions:

- English only.
- Never fabricate a founder biography, credentials, affiliations, publications, collaborators, contact details, statistics, readership or citation figures, research results, project counts, or external URLs. Missing data stays missing.
- Sample content is labelled (`example: true`); unfinished content is `draft: true`; planned content is labelled "Planned" or "Coming soon".
- Research areas are interests, not active projects. Do not overstate ACRR's size, activity or achievements.
- Any statistic shown on the site must be computed from real content (the home page counts, for example, are computed from the content collections).
- Technical writing must be original and technically correct.
