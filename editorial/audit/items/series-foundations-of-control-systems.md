<!-- audit: {"slug":"foundations-of-control-systems","type":"series","series":"foundations-of-control-systems","priority":"P2","before":{"purpose":3,"structure":2,"accuracy":4,"evidence":4,"language":3,"consistency":3,"publishing":3},"findings":{"blocking":0,"shouldFix":3,"optional":1}} -->
# Audit: Foundations of Control Systems (series overview)

- Path: `src/content/series/foundations-of-control-systems.md` · Route: `/series/foundations-of-control-systems` · Type: series overview · 5 entries, status published · Words: 68 (`eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 3: audience stated ("comfortable with calculus and basic linear algebra"), but not the extra prerequisites the entries use (complex numbers, linear ODEs with constant coefficients) nor tools (Python 3, numpy).
- structure 2: one paragraph; no sequence rationale (why input-output first, then state space); does not say how entries connect beyond a list; no shared conventions.
- accuracy 4.
- evidence 4 (n/a for an overview; nothing claimed that needs a source).
- language 3: "Each entry introduces one idea" is not accurate for entries 4 and 5, which cover many.
- consistency 3: objectives are checkable and begin with assessable verbs (explain, describe, relate, recognize); "Describe" and "Recognize" are acceptable.
- publishing 3: description 153 characters, fine; not phrased as what the reader learns ("A series on ...").

## Priority

P2: overview page structurally thin against standards 6.5.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| D1 | Should fix | `:13` | structure | No sequence rationale and no account of how entries connect (standards 6.5) |
| D2 | Should fix | `:13` | purpose | Prerequisites incomplete; shared conventions (SI units, rad/s, 2% settling, $j$, Python 3 and numpy) not stated |
| C1 | Should fix | `:13` | language | "Each entry introduces one idea" is untrue of entries 4-5 |
| C2 | Optional | `:3` | publishing | Description "A series on ..." could say what the reader learns |

### D1-D2, C1
- **Text:** "This series is intended for readers who are comfortable with calculus and basic linear algebra. Each entry introduces one idea, ..."
- **Correction:** three short paragraphs: reader and prerequisites; sequence and how entries connect; shared conventions. No promise beyond what the entries deliver.

### C2
- Keep within 70-165 characters; do not change `status`, `category`, `objectives` meaning, `plannedEntries` (none).

## Revision log (wave 1)

- **Structure/prose:** body rewritten as three paragraphs: reader and prerequisites (calculus, basic linear algebra, Python; complex numbers and linear ODEs; Laplace transform and matrix exponential introduced in the entries), the sequence and how entries connect with the rationale for input-output before state space, and shared conventions (SI units, rad/s, 2% settling, $j$, Python 3, numpy from entry 3). "Each entry introduces one idea" removed.
- **Not changed:** title, description (C2 optional, left to keep the translation in step), status, category, objectives.
- Remaining warnings: none.
- **Flags:** (series) confirm the overview promises nothing the entries do not deliver (the prerequisites list matches entry openings).
- **Vietnamese translation affected: yes**, `src/content/series/vi/foundations-of-control-systems.md` body should be retranslated; front matter unaffected.
- **Style (follow-up):** "numpy" in prose changed to "NumPy" (glossary term added by the coordinator); code and code spans unchanged.

## Independent review (wave 2)

- Reviewer: independent reviewer (fact-check, technical, series), commit `9232ed9`, 2026-10-13. Report: `reviews/foundations-of-control-systems.md`.
- Fact-check verdict: pass (no factual claims beyond the entries; references n/a).
- Technical verdict: fail until S1 is resolved.
- Findings concerning this item: S1.
- Not verified: none.

## Revision log (wave 2 resolution)

- S1: body paragraph 2 now says "A single first-order equation cannot describe ..." and that state-space models collect several first-order equations into one matrix equation (`:15`); the paragraph is split before the sequence rationale (new `:17`), which clears the paragraph-length suggestion.
- Lint 0/0/0.
- Vietnamese translation affected: yes, `src/content/series/vi/foundations-of-control-systems.md` paragraph 2 needs the same change when it is retranslated.
