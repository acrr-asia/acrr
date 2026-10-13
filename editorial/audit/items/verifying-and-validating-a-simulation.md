<!-- audit: {"slug":"verifying-and-validating-a-simulation","type":"article","series":"numerical-simulation","priority":"P2","before":{"purpose":4,"structure":4,"accuracy":4,"evidence":3,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":6,"optional":2}} -->
# Audit: Verifying and Validating a Simulation

- Path: `src/content/blog/verifying-and-validating-a-simulation.mdx` · Route: `/blog/verifying-and-validating-a-simulation` · Type: article (series entry) · Series `numerical-simulation`, entry 5 of 5 · Words: 3,432 (`eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 4.
- structure 4.
- accuracy 4: all three Python blocks re-run with `python3 -I` (Python 3.13.16, NumPy 2.5.3): output identical (the Monte Carlo block uses a seeded generator, so its output is reproducible). Recomputed Exercises 1, 2 and 4: $p = 1.9985$; two-grid GCI $5.77\times10^{-4}$; $u_{\text{input}} = 0.90$ K, $u_{\text{val}} = 1.03$ K, interval $[-3.78, 0.34]$ K; temperature rise 39.28 K, conductivity term 1.18 K, heat-generation term 0.79 K.
- evidence 3: the two JCGM entries have no year; Roache entries out of date order; comma outside closing quotes; list not alphabetical.
- language 3: a 68-word sentence in Section 1.1, a 49-word closing sentence, a broken list label "**time step error.**".
- consistency 3: "0.024 %", "95 %", "2 %", "3 %" with a space before %; "numpy"; "The ACRR note".
- publishing 2: description of 387 characters; seven title-case headings.

Total 23 of 28.

## Priority

P2.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| C1 | Should fix | `:207` | language | List label "**time step error.**" begins with a lowercase letter |
| P1 | Should fix | `:3` | publishing | Description 387 characters, a list |
| P2 | Should fix | `:19, :52, :125, :299, :362` and others | publishing | Title-case headings |
| C2 | Should fix | `:378-386` | evidence | References: JCGM entries without a year; order; comma placement |
| C3 | Should fix | `:199, :239, :253, :294, :331, :344` | consistency | Space before % |
| C4 | Should fix | `:23` | language | 68-word sentence naming the terminology sources |
| C5 | Optional | `:35` | consistency | "Grid and time step refinement" (compound modifier) |
| C6 | Optional | `:17, :209, :374` | language | "The ACRR note"; "actually"; 49-word closing sentence |

### C1. Broken list label
- **Where:** line 207, Section 3.4
- **Text:** "- **time step error.** For transient problems, refine the time step as well as the grid ..."
- **Problem:** The other labels ("**Iteration error.**", "**Round-off error.**") are capitalized; this one begins in lowercase, apparently from a mechanical replacement of "Time-step". As a modifier the house glossary would hyphenate it, but the glossary rule flags "time-step" before any noun except "size".
- **Correction:** "**Time discretization error.**"

### C2. References
- **Where:** lines 385-386 "JCGM 100:2008, *Evaluation of Measurement Data: Guide to the Expression of Uncertainty in Measurement* (GUM), Joint Committee for Guides in Metrology."
- **Problem:** Standards 7.3: every entry has a year. The year is part of the document designation (2008). Order: AIAA, ASME V&V 10, ASME V&V 20, JCGM 100, JCGM 101, Oberkampf, Richardson, Roache 1994, Roache 1998.
- **Correction:** Add ", 2008."; reorder; commas inside closing quotes.

### C4. Long sentence
- **Where:** line 23 "The terminology here follows the verification and validation (V&V) guides of the American Society of Mechanical Engineers (ASME), V&V 10 (...) and V&V 20 (...), which build on the earlier guide ... of the American Institute of Aeronautics and Astronautics (AIAA), and the books of Roache and of Oberkampf and Roy listed at the end."
- **Correction:** Split into two sentences.

### P1. Description
- **Correction:** "How to verify a simulation code with manufactured solutions, estimate the numerical error of a result, and validate a model against measurements."

## Revision log (wave 1)

- Structure: unchanged.
- Prose: the 68-word sentence of Section 1.1, the 53-word list of the three checks in the opening and the closing sentence split; "actually" removed; "The ACRR note" → "The insight"; the broken list label fixed ("**Time discretization error.**"); table cell "Grid and time step refinement" → "Refinement of the grid and the time step".
- Terminology/style: headings in sentence case; "NumPy"; no space before %.
- Metadata: description rewritten (one sentence, under 165 characters).
- References: house format, alphabetical; year 2008 added to both JCGM entries (taken from their designations JCGM 100:2008 and JCGM 101:2008).
- Technical corrections: none.
- Remaining warnings and why they stay: none. Suggestions kept: `sentence-length` at lines 17 and 38 (the linter counts across sentences that contain bold terms; the actual sentences are under 30 words), line 239 (47 words, one conditional statement) and line 353 (Exercise 5's question with its four lettered cases); `acronym-expansion` "JCGM" in the reference list (the document designation).
- Flags for independent review: none new.
- Vietnamese translation affected: no (no translation of this entry exists).
