<!-- audit: {"slug":"floating-point-in-long-simulations","type":"insight","series":null,"priority":"P2","before":{"purpose":2,"structure":3,"accuracy":4,"evidence":3,"language":3,"consistency":3,"publishing":3},"findings":{"blocking":1,"shouldFix":3,"optional":1}} -->
# Audit: Floating-Point Rounding in Long Simulations

- Path: `src/content/insights/floating-point-in-long-simulations.md` · Route: `/insights/floating-point-in-long-simulations` · Type: insight (Methodological note) · Words: 351
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 2: no framing paragraph (standards 6.4).
- structure 3: sound.
- accuracy 4: recomputed in Python 3.13: `(1e16+1)+1 == 1e16` and `1e16+(1+1) == 1e16+2` (printed 1.0000000000000002e+16); `float32(2**24)+1 == float32(2**24)` is true; $10^6 \cdot 2^{-24} = 0.0596$, $10^6 \cdot 2^{-53} = 1.1\times10^{-10}$. All match.
- evidence 3: the recursive-summation bound is attributed to nothing; Higham's *Accuracy and Stability of Numerical Algorithms* (chapter 4, "Summation"), already cited in the series, is the standard source.
- language 3: "very long" (lint `intensifiers`); "Two checks follow, and their cost depends on the code. Repeat the run ... Alternatively, reorder ..." reads as three checks.
- consistency 3: the series cites this insight twice (`from-differential-equations-to-discrete-problems` line 217, `verifying-and-validating-a-simulation` line 206) but the insight does not link back to the series' concrete case where rounding overtakes discretization (`solving-large-linear-systems`, Section 3.2).
- publishing 3: description 132 characters but a noun phrase.

## Priority

P2.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| D1 | Blocking | line 12 | structure | No framing paragraph (standards 6.4, C7). |
| D2 | Should fix | whole file | consistency | No links to the series sections on rounding. |
| D3 | Should fix | line 18 | evidence | Summation bound not attributed. |
| C1 | Should fix | line 24 | language | "Two checks follow ... Repeat ... or ... Alternatively": the count does not match the list. |
| P1 | Optional | `:3` | publishing | Description a noun phrase. |

## Revision log (wave 1)

- Structure: added the framing paragraph.
- Evidence: the recursive-summation bound attributed inline to Higham, *Accuracy and Stability of Numerical Algorithms*, 2nd ed., SIAM, 2002, chapter 4 (the book is cited in the series; chapter 4 "Summation" confirmed from a search listing of the book's chapter structure). **unit roundoff** in bold at definition.
- Cross-references: new paragraph in Established linking `/blog/from-differential-equations-to-discrete-problems#52-checking-the-orders-and-where-rounding-takes-over` and `/blog/solving-large-linear-systems#32-where-rounding-overtakes-discretization`; Interpretation links `/blog/verifying-and-validating-a-simulation#34-the-other-numerical-errors` (the two series entries already link back here).
- Prose: "very long" → "long"; the two checks now read as two ("The first repeats the run with less rounding ...; the second reorders the summation").
- Metadata: description rewritten as one sentence (142 characters).
- Remaining suggestion: "SIAM" in the inline citation (publisher name).
- Flags for independent review: (fact-check) confirm chapter 4 of Higham (2nd ed.) is the summation chapter.
- Vietnamese translation affected: yes: framing paragraph, attribution, new Established paragraph with two links, reworded checks paragraph with a link, new description.

## Independent review (wave 2)

- Report: `editorial/audit/review/standalone.md`
- Fact-check: pass
- Technical: pass
- Findings: none
- Not verified: none (Higham chapter 4 "Summation" confirmed from the book's contents).
