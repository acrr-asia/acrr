---
name: editorial-review
description: Editorial and integrity review of ACRR content (articles, insights, series, Learning entries, Home/About copy) before publishing — technical correctness, fabrication, example/draft labelling, structure and house style. Use when asked to review, proofread or fact-check content, and after writing new content.
---

# Editorial review

Review the named files, or `git diff --name-only master... -- src/content src/data src/pages src/components/home` if none are named. Report findings as a list ordered by severity: **Blocking** (integrity or correctness), **Should fix**, **Nit**. Quote the line, say why, propose the fix. Do not edit unless asked.

## Blocking

- **Fabrication**: biography, credentials, affiliations, publications, collaborators, contact details, statistics, readership/citation figures, research results, benchmarks, project counts, quotes, citations or URLs that the user did not supply and you cannot verify. Missing data stays missing.
- **Overclaiming**: research areas presented as active projects, ACRR described as a staffed lab, "we found/our experiments" without real experiments, any figure not computed from real content.
- **Technical errors**: check every equation, derivation step, unit, sign and code sample. Recompute numeric examples. Flag hidden assumptions (linearity, Gaussian noise, steady state...).
- **Labelling**: sample content without `example: true` and visible wording; unfinished content without `draft: true`; unwritten series entries or resources not marked planned / "Coming soon"; a Learning `url` that is not real.
- **Copying**: text, names or taglines from another site (including the design reference tieukhoimai.me).
- **Insights**: missing or out-of-order `## Established` / `## Interpretation` / `## Open questions`, or an interpretation stated as established.
- Visitor-facing copy that contains authoring instructions (file names, field names, commands).

## Should fix

- `description` longer than two sentences or not matching the body.
- Category or tags wrong or inconsistent with existing spellings.
- Heading structure: no `#` in the body, no skipped levels, at least two `##`/`###` if the article is long enough to need Contents.
- Mermaid diagram not explained in the surrounding text (it has no caption and is not indexed).
- Series bookkeeping: entry still in `plannedEntries`, stale `status` or introduction.

## House style (nits)

English only, plain and precise; define terms on first use; prefer short paragraphs and concrete examples; no marketing language, no emoji; consistent spelling within a piece; code and maths formatted as such.
