---
name: write-article
description: Write, publish or revise an ACRR blog article (src/content/blog/*.md|mdx), including series entries, Mermaid diagrams, SVG figures and KaTeX maths. Use when the user asks for a new post, article, tutorial or research note, or to edit/update an existing one.
---

# Write an ACRR blog article

The frontmatter contract is `src/content.config.ts`; the authoring guide is README.md, "Writing content > Blog articles". Read both before writing. The content-integrity rules in CLAUDE.md are acceptance criteria.

## 1. Settle the brief before writing

Confirm (ask only for what you cannot infer): topic and angle, target reader, `category` (must be one of `CATEGORIES`), whether it belongs to a series (`series` id + `seriesOrder`), and whether it is real writing or a sample. A sample gets `example: true` and must say so; unfinished work gets `draft: true`.

Check for overlap first: `grep -ril "<topic words>" src/content` and skim related articles so the new one links to them instead of repeating them.

## 2. File and frontmatter

- Path: `src/content/blog/<kebab-case-slug>.mdx` (`.md` if it needs no components). The file name is the public URL `/blog/<slug>`; never rename a published article (it breaks links and RSS ids).
- `publishedAt`: today's date unless the user gives one. On revisions of published work, keep `publishedAt` and set `updatedAt`.
- `description`: one or two plain sentences; it is the card text, meta description and RSS summary.
- `tags`: reuse existing spellings (`grep -h -A12 '^tags:' src/content/*/*.md* | sort | uniq -c`). A new tag that slug-collides with a different one fails the build.

## 3. Body

- Start with prose, not a heading; the page already renders the `<h1>` from `title`. Use `##`/`###` only (they feed the Contents aside).
- Original, technically correct writing. Derive formulas, state assumptions and units, keep claims proportional to the evidence. No invented results, benchmarks, citations, quotes, statistics or URLs. If a source is needed and you cannot verify it, say so to the user rather than citing it.
- Maths: `$...$` inline, `$$...$$` display.
- Code: fenced blocks with a language; keep them runnable or clearly marked as excerpts.
- Diagrams: a ```` ```mermaid ```` block for flowcharts/sequence diagrams (no caption: explain it in the text). For plots and drawings, add a generator to `scripts/generate-diagrams.py`, run it, and wrap the component in `Figure` (see README). Plot data must come from the article's own formulas. A new Mermaid diagram type (class, state, ER...) needs a light and dark screenshot check.
- Series entry: remove the matching item from the series' `plannedEntries` and update its `status` (see the `plan-series` skill).

## 4. Verify

Run the `verify-site` skill (at least `npm run build && npm run check:links`), then grep the built page: `dist/blog/<slug>.html` should contain the title, and no text glued to an inline element. Finish with the `editorial-review` skill on the new file before committing.
