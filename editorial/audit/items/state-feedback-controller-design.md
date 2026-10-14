<!-- audit: {"slug":"state-feedback-controller-design","type":"article","series":"foundations-of-control-systems","priority":"P2","before":{"purpose":4,"structure":3,"accuracy":4,"evidence":3,"language":3,"consistency":2,"publishing":2},"findings":{"blocking":0,"shouldFix":5,"optional":2}} -->
# Audit: Designing a State-Feedback Controller

- Path: `src/content/blog/state-feedback-controller-design.mdx` · Route: `/blog/state-feedback-controller-design` · Type: article (series entry) · Series `foundations-of-control-systems`, entry 5 of 5 · Words: 2,276 (`eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 4.
- structure 3: sections unnumbered; "## Where the series ends" follows the Summary, so the References sit under a section that is not the Summary and the Summary itself has no closing paragraph (standards 6.2 item 6).
- accuracy 4: gains, eigenvalues, augmented gains, observer gain recomputed (`acker` gives [12, 5.1], [34.4, 9.1, 64]; observer [19.5, 86.25]); script output matches.
- evidence 3: five verified references, but not alphabetical (Ogata before Chen, Ackermann last) and not in house format ("2nd edition"; comma outside the quotes in the Ackermann title).
- language 3: two sentences over 50 words (`:103`, `:186`); "they are worth listing explicitly" is filler.
- consistency 2: structure differs from the house standard; "the previous entry's sections on marginal stability and transient growth" could cite section numbers.
- publishing 2: description 287 characters.

## Priority

P2: final entry; metadata and structural inconsistencies, no critical condition.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| D1 | Should fix | `:266-280` | structure | "Where the series ends" sits after the Summary; Summary lacks a closing paragraph against the series objectives |
| D2 | Should fix | headings | structure | Sections unnumbered |
| C1 | Should fix | `:3` | publishing | Description 287 characters |
| C2 | Should fix | `:282-288` | evidence | References not alphabetical, not house format |
| C3 | Should fix | `:103`, `:186` | language | Sentences of 55 and 53 words |
| P1 | Optional | `:194` | consistency | "the previous entry's sections on marginal stability and transient growth" could cite Sections 4 and 5 |
| C4 | Optional | `:190` | language | "they are worth listing explicitly" filler |

### D1. Closing
- **Text:** "## Summary" table, then "## Where the series ends" paragraph, then "### References".
- **Correction:** merge the closing paragraph into the Summary and relate it to the four series objectives.

### D2. Number sections (1-6, Exercises 7, Summary 8).

### C1. Description
- **Text:** "Pole placement for the mass-spring-damper: the state-feedback law, the controllability test, ..." (287)
- **Correction:** one sentence ≤ 165 characters.

### C2. References
- **Correction:** order Ackermann, Åström and Murray, Chen, Franklin et al., Ogata; "2nd ed."; `"... im Zustandsraum," *Regelungstechnik ...*`. Volume 20 and pages 297–300 were verified by the previous series review; the issue number could not be re-verified (doi.org rate-limited), so none is added.

### C3. Split the two long sentences.
### P1, C4. As stated.

## Revision log (wave 1)

- **Structure:** sections numbered 1-8 (Exercises 7, Summary 8); new heading "5.1 The reference gain" so the tracking section has an introduction and three subsections; "## Where the series ends" removed and its paragraph merged into the Summary as the closing, now split into three paragraphs and extended with one paragraph mapping the four series objectives to the entries that meet them.
- **Prose:** the 55- and 53-word sentences split; "they are worth listing explicitly" replaced; "previous entry's sections on marginal stability and transient growth" → "(fourth entry, Sections 4 and 5)"; settling-time sentence now cites the first entry's Section 4.3 and this entry's Section 5.1 for the simulation.
- **Metadata:** description shortened to one sentence (155 characters). No `updatedAt` (published 2026-10-13).
- **References:** reordered alphabetically (Ackermann, Åström and Murray, Chen, Franklin et al., Ogata); "ed." form; comma moved inside the quotation marks of the Ackermann title. No issue number or DOI added: doi.org could not be fetched (rate-limited), so the previous review's DOI was not re-verified.
- **Code:** unchanged; re-run (`acker` → `[[12. 5.1]]`, eigenvalues as printed); augmented and observer gains recomputed ([34.4, 9.1, 64], [19.5, 86.25]).
- Remaining warnings: none.
- **Flags:** fragment id `#the-controller-runs-in-continuous-time` is now `#64-the-controller-runs-in-continuous-time`; `src/content/blog/from-signal-processing-to-digital-control.mdx:267` links the old id (outside scope). (fact-check) Ackermann 1972 issue number/DOI.
- **Vietnamese translation affected:** no translation exists.
- **Style (follow-up):** "numpy" in prose changed to "NumPy" (glossary term added by the coordinator); code and code spans unchanged.

## Independent review (wave 2)

- Reviewer: independent reviewer (fact-check, technical, series), commit `9232ed9`, 2026-10-13. Report: `reviews/foundations-of-control-systems.md`.
- Fact-check verdict: pass (F1 optional).
- Technical verdict: pass.
- Findings concerning this item: F1 (optional).
- Not verified: Ackermann (1972) issue designation and DOI (not cited in the text; doi.org not reachable).

## Revision log (wave 2 resolution)

- F1: Ackermann journal title corrected to "*Regelungstechnik und Prozess-Datenverarbeitung*", the spelling in library catalogues (reviewer's evidence) (`:288`).
- Lint 0/0/0; syntax passes.
- Vietnamese translation affected: no translation exists.
