---
name: verify-site
description: Run the ACRR release check and the post-build regression greps after any change to content, components, layouts, styles, config or scripts. Use before committing, before saying a change works, and when a build or link check fails.
---

# Verify the site

There is no test framework; the build plus these checks are the test suite. Report failures with their output, do not summarise them away.

## 1. Release check (always)

```sh
SITE_URL=https://acrr.asia npm run build && npm run check:links
```

Both must exit 0. `npm run build` = `astro check` (types/templates) + `astro build` + Pagefind + the localhost guard. For a fast loop while editing `.astro`/`.ts` files, `npm run check` first. To experiment without touching `dist/`: `npx astro build --outDir <scratch>` then `node scripts/check-links.mjs <scratch>`.

Read the Pagefind log line "Indexed N pages": N must equal articles + insights + series detail pages + About + Learning. A different N means `searchable`/`noindex` handling changed.

## 2. Targeted greps (run the ones your change touches)

- Navigation/header/`Astro.url` changes: each of `dist/blog.html dist/series.html dist/learning.html dist/insights.html dist/about.html` contains `aria-current="page"`.
- Copy mixing text and inline elements: `grep -RnoE '[A-Za-z0-9.,;:!?)](<span|<strong>|<a |<code)[^>]{0,30}' dist --include=*.html | grep -vE 'aria-hidden|sr-only'` should print nothing (arrow and screen-reader spans carry their own space); inspect any hit that is visible text glued to an element (see CLAUDE.md "Whitespace before inline elements").
- Example content: `[Example]` appears in its `<title>` and in `dist/rss.xml`; meta description starts "Example article/insight/series:".
- Drafts: add a temporary `draft: true` entry, build, confirm its slug and title are absent from `dist/` (`grep -rl <slug> dist`), then delete it.
- Links: never a trailing slash or `.html` in an internal href: `grep -RnoE 'href="/[^"]*(/|\.html)"' dist --include=*.html`.
- Shiki theme or `--code-bg` changes: re-check token contrast (CLAUDE.md "Code-block colours").

## 3. Visual check (UI changes)

`npm run preview` (after a build; search only works here), then screenshot with Playwright (Chromium is preinstalled; launch with `executablePath` if versions differ) at 360px and 1280px, light and dark (`colorScheme`). Stop the server with `npx astro preview stop`.

## 4. Report

State which commands ran and their result. If something was skipped, say so.
