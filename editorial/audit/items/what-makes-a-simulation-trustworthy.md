<!-- audit: {"slug":"what-makes-a-simulation-trustworthy","type":"insight","series":null,"priority":"P2","before":{"purpose":2,"structure":3,"accuracy":4,"evidence":3,"language":3,"consistency":2,"publishing":2},"findings":{"blocking":1,"shouldFix":5,"optional":1}} -->
# Audit: What Makes a Simulation Trustworthy?

- Path: `src/content/insights/what-makes-a-simulation-trustworthy.md` · Route: `/insights/what-makes-a-simulation-trustworthy` · Type: insight (Methodological note) · Words: 306
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 2: no framing paragraph (standards 6.4).
- structure 3: sound.
- accuracy 4: the Euler and RK4 halving factors (2 and 16) agree with the recomputed ratios in `numerical-integration-notes` (2.04/2.02 and 16.7/16.3). Explicit Euler on $\dot{x} = v$, $\dot{v} = -\omega^2 x$ multiplies the energy by exactly $1 + h^2\omega^2$ per step (derived: $|1 + jh\omega|^2$), so "makes the energy grow with every step" is correct.
- evidence 3: verification and validation are stated without a source; the site's fifth Numerical Simulation entry gives the ASME and Oberkampf–Roy definitions and is not linked.
- language 3: math in code spans (`p`, `h^p`, `h`) instead of KaTeX (standards 5.5); "actually" (lint `intensifiers`).
- consistency 2: this insight is a short version of `verifying-and-validating-a-simulation` (Sections 1, 2, 4, 5) and of `numerical-integration-notes` (order measurement), yet links neither.
- publishing 2: description 103 characters, a noun phrase.

## Priority

P2.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| D1 | Blocking | line 12 | structure | No framing paragraph (standards 6.4, C7). |
| D2 | Should fix | whole file | consistency | No links to the V&V entry or the integration notes. |
| C1 | Should fix | line 16 | language | Math in code spans: "`p`", "`h^p`", "`h`". |
| C2 | Should fix | line 24 | language | "actually" adds nothing. |
| P1 | Should fix | `:3` | publishing | Description a noun phrase. |
| C3 | Should fix | line 22 | language | "Trust seems to be a property ..." hedge before an interpretation already labeled as one. |
| D3 | Optional | line 24 | structure | The last Interpretation paragraph matches Section 5 of the V&V entry; a link avoids the duplication. |

## Revision log (wave 1)

- Structure: added the framing paragraph, which names the fifth Numerical Simulation entry as the in-depth treatment.
- Cross-references: `/blog/verifying-and-validating-a-simulation`, `/blog/numerical-integration-notes` (which measures both halving factors).
- Language: math moved from code spans to KaTeX ($p$, $h^p$, $h$); "actually" removed; **verification** and **validation** in bold at definition; "Trust seems to be" → "One reading is that trust is" (one label instead of a hedge).
- Content: last Interpretation sentence ends with "since outside that regime a prediction is an extrapolation", the point of Section 5 of the V&V entry.
- Metadata: description rewritten as one sentence (140 characters).
- Remaining suggestion: `sentence-length` at line 16 (59 words) is a splitter artifact; the paragraph's sentences are 6, 27 and 24 words.
- Flags for independent review: none new.
- Vietnamese translation affected: yes: framing paragraph, link sentence on the integration notes, extrapolation clause, new description.
