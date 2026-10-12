---
name: plan-series
description: Create or update an ACRR series (src/content/series/*.md) and Learning resources (src/data/learning.json) — outlines, planned entries, status changes, attaching a published article to a series, or adding a real resource URL. Use when the user plans a series, reorganises an outline, or publishes a Learning entry.
---

# Series and Learning resources

## Create a series

File `src/content/series/<id>.md`; the id is the file name and the URL `/series/<id>`. Frontmatter: `title`, `description`, `category` (one of `CATEGORIES`), `objectives` (learning objectives, verb first), `status` (`planned` until the first article is published), `plannedEntries` (`{ title, description }`, in reading order). The body is a short introduction; while nothing is published it must say the series is planned and the outline may change.

## Attach an article to a series

1. In the article: `series: <id>` and the next `seriesOrder`.
2. Remove that entry from `plannedEntries` (otherwise it shows twice).
3. Set `status`: `in-progress` once at least one entry is published and some remain planned; `published` when no planned entries remain. It is not inferred.
4. If the introduction still says nothing is published, update it.

A `series:` id that does not exist fails the build via the guard in `src/lib/content.ts`; Astro alone would only log it.

## Learning resources (`src/data/learning.json`)

Each item: unique `id`, `title`, `description`, `topic` (groups the page), `type`, `status`. Add `url` only when the user gives a real, existing URL (for example a Notion page); never a placeholder. Without `url` the entry shows "Coming soon". The notices on the Learning page are conditional on the data; after adding the first URLs, read `src/pages/learning.astro` and confirm its wording is still true.

## Verify

`npm run build && npm run check:links`; check `dist/series/<id>.html` lists entries in order and the progress text ("N of M entries published") matches.
