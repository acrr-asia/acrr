---
name: write-insight
description: Write or revise an ACRR Insights entry (src/content/insights/*.md) — short research observations, comparisons and open questions that keep established facts, interpretation and open questions apart. Use when the user asks for an insight, observation, research question or short perspective piece.
---

# Write an ACRR insight

Schema: `insights` in `src/content.config.ts`. Guide: README.md, "Insights".

## Shape

An insight is short (roughly 400 to 900 words) and argues one point. It has exactly these three `##` sections, in this order, and nothing before the first:

1. `## Established` — what is well supported: definitions, theorems, textbook results, measured behaviour that is widely reproduced. State conditions precisely (the Kalman insight is a good model: assumptions first, then the result).
2. `## Interpretation` — how those facts are read. Signal that it is a reading ("One reading is...", "This suggests..."). Rough guides and heuristics belong here, never in Established.
3. `## Open questions` — a short list of what stays unresolved or hard. Real questions, not rhetorical ones.

If a claim could go in either of the first two sections, it goes in Interpretation.

## Frontmatter

`title`, `description` (one or two sentences), `publishedAt` (today unless told), `kind` (one of the enum values: Concept explanation, Engineering observation, Comparison, Research question, Methodological note, Emerging idea), `tags` (reuse existing spellings). `example: true` for samples, `draft: true` for unfinished work.

File: `src/content/insights/<kebab-case-id>.md`, served at `/insights/<id>`.

## Integrity

No invented experiments, numbers, citations or URLs; ACRR has no lab results to report unless the user supplies them. Do not present an interpretation as a finding.

## Verify

`npm run build && npm run check:links`, then `grep -c '<title' dist/insights/<id>.html` and read the page in `npm run preview` if the layout matters. Run `editorial-review` on the file.
