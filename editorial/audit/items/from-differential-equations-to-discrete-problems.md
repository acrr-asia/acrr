<!-- audit: {"slug":"from-differential-equations-to-discrete-problems","type":"article","series":"numerical-simulation","priority":"P1","before":{"purpose":4,"structure":4,"accuracy":4,"evidence":3,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":5,"optional":3}} -->
# Audit: From Differential Equations to Discrete Problems

- Path: `src/content/blog/from-differential-equations-to-discrete-problems.mdx` · Route: `/blog/from-differential-equations-to-discrete-problems` · Type: article (series entry) · Series `numerical-simulation`, entry 1 of 5 · Words: 3,704 (`eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 4.
- structure 4.
- accuracy 4: all three Python blocks re-run with `python3 -I` (Python 3.13.16, NumPy 2.5.3; SciPy is not installed and not used): the printed output matches line for line. Recomputed: $\tfrac{h}{2}|\sin 1| = 0.4207h$, $\tfrac{h^2}{6}|\cos 1| = 0.09005h^2$, $h^2\pi^2/12 = 0.00822$ at $h = 0.1$, the one-sided/ghost-point error ratio at $N = 80$ ($1.69\times10^{-2}/5.78\times10^{-5} = 292$, "about 300"), Exercises 1-5.
- evidence 3: references not in the house format of standards 7.3 ("2nd edition" for "2nd ed.") and not alphabetical.
- language 3: intensifiers ("very", "simply"), three sentences of 47-50 words, the second opening paragraph reads as a table of contents.
- consistency 3: title-case headings; "numpy" in prose where the project's name is NumPy.
- publishing 2: description of 387 characters; seven title-case headings (`heading-case`).

Total 23 of 28.

## Priority

P1: the foundational entry of the series; the four later entries cite its sections (4.3, 5.2, 6.1, 6.2) and its vocabulary. Its defects are metadata and style, not substance.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 387 characters, a list of sections |
| P2 | Should fix | `:21, :52, :111, :131, :159, :219, :342, :363` | publishing | Title-case section headings |
| C1 | Should fix | `:437-442` | evidence | References not alphabetical, "2nd edition" instead of "2nd ed." |
| C2 | Should fix | `:81, :157, :163` | language | Intensifiers "very", "simply" |
| C3 | Should fix | `:19` | consistency | "numpy" for the library NumPy in prose |
| D1 | Optional | `:17` | structure | Second opening paragraph is a table of contents in prose |
| C4 | Optional | `:38, :217` | language | "The ACRR note" (unexpanded abbreviation; the link already says what it is) |
| D2 | Optional | `:433` | structure | Closing paragraph names "The next entry" without linking it |

### P1. Description too long
- **Where:** line 3
- **Text:** "The foundation of the series: the heat, wave and Poisson equations and where they come from, boundary and initial conditions, what discretization means, ..."
- **Problem:** 387 characters (limit 165, standards 8.1); it lists every section.
- **Correction:** "How the heat, wave and Poisson equations become finite algebraic problems, how finite differences approximate derivatives, and how discretization error is measured."

### P2. Title-case headings
- **Where:** "## 1. Why Simulations Discretize", "## 2. Three Model Equations", "## 3. Boundary and Initial Conditions", "## 4. The Idea of Discretization", "## 5. Finite-Difference Approximations", "## 6. A First Complete Discrete Problem", "## 7. The Vocabulary of Discretization Error", "## 8. Where the Series Goes"
- **Problem:** Standards 5.4 requires sentence case. Anchor slugs are lowercase, so the inbound fragment links (`#43-the-method-of-lines`, `#52-checking-the-orders-and-where-rounding-takes-over`) are unaffected.
- **Correction:** Sentence case, words unchanged.

### C1. Reference list format
- **Where:** lines 437-442
- **Text:** "K. W. Morton and D. F. Mayers, *Numerical Solution of Partial Differential Equations: An Introduction*, 2nd edition, ..."
- **Problem:** Standards 7.3: "3rd ed.", alphabetical by first author (Higham, IEEE 754-2019, LeVeque, Morton, Strauss, Strikwerda).
- **Correction:** Reorder and use "2nd ed."; details otherwise unchanged (verified in the 2026-10-13 series review).

### C2. Intensifiers
- **Where:** line 81 "Its solutions behave very differently from those of the heat equation"; line 157 "why some time-stepping schemes are stable only for very small steps"; line 163 "finite differences simply stop before the limit".
- **Problem:** Standards 5.2. "simply" about a technical step is banned.
- **Correction:** "behave differently in kind"; "stable only for steps far smaller than accuracy requires"; "finite differences stop before the limit".

### C3. Library name
- **Where:** line 19 "The code examples use Python 3 with numpy"
- **Problem:** The library's name is NumPy; the lowercase form is the import name and belongs in code.
- **Correction:** "NumPy" in prose (all five entries).

### D1. Opening reads as a table of contents
- **Where:** line 17 "This entry introduces the three model equations used throughout the series, the boundary and initial conditions that complete them, the idea of discretization, the simplest way to carry it out (finite differences), and the vocabulary ..."
- **Problem:** A 50-word list that Section 8 repeats for the series.
- **Correction:** Tighten to the purpose: what the entry establishes and why the later entries need it.

### C4. "The ACRR note"
- **Where:** lines 38, 217
- **Problem:** `acronym-expansion`; the link text identifies the insight already.
- **Correction:** "The insight [What Makes a Simulation Trustworthy?]"; "The insight on [floating-point rounding ...]".

### D2. Unlinked next entry
- **Where:** line 433 "The next entry puts these ideas to work on time-dependent problems."
- **Correction:** Link the title of the second entry.

## Revision log (wave 1)

- Structure: second opening paragraph tightened from a list of topics to a statement of what the entry establishes for the rest of the series; no section moved, renumbered or renamed (headings changed in case only, so every fragment link still resolves).
- Prose: intensifiers removed (lines 81, 157, 163); "The ACRR note" rephrased as "The insight"; the closing paragraph now links the second entry and its 46-word sentence is split; the first opening sentence (47 words) and the discretization sentence (50 words) split.
- Terminology/style: eight headings in sentence case; "numpy" → "NumPy" in prose.
- Metadata: description rewritten (one sentence, 164 characters).
- References: alphabetical order; "2nd ed." house form. No bibliographic detail changed.
- Technical corrections: none needed. All code re-run (output identical).
- Remaining warnings and why they stay: none. Two suggestions kept: `acronym-expansion` "SIAM" in the reference list (the publisher's name as printed on the title page); `intensifiers` "actually" at line 36 ("as actually obtained"), which carries the contrast between the exact solution of the discrete problem and the numbers the computer produces.
- Flags for independent review: none new. The fact-checker may wish to confirm the edition years of Strauss (2nd ed., Wiley, 2008) and Morton and Mayers (2nd ed., CUP, 2005), already checked in the 2026-10-13 series review.
- Vietnamese translation affected: no (no translation of this entry exists).
