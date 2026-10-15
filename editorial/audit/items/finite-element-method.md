<!-- audit: {"slug":"finite-element-method","type":"article","series":"numerical-simulation","priority":"P2","before":{"purpose":4,"structure":4,"accuracy":4,"evidence":3,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":5,"optional":3}} -->
# Audit: The Finite Element Method

- Path: `src/content/blog/finite-element-method.mdx` · Route: `/blog/finite-element-method` · Type: article (series entry) · Series `numerical-simulation`, entry 4 of 5 · Words: 3,035 (`eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 4.
- structure 4.
- accuracy 4: all three Python blocks re-run with `python3 -I` (Python 3.13.16, NumPy 2.5.3): output identical, including the P2 element matrix and the identity of the linear-triangle and five-point matrices. Exercise 3 recomputed ($3.15\times10^{-2}\times64/N = 7.98\times10^{-4}$ gives $N \approx 2{,}526$, "about 2,500"); the finite-difference comparison value $1.3\times10^{-4}$ at $N = 80$ matches entry 1 ($1.285\times10^{-4}$).
- evidence 3: references in the wrong format and order.
- language 3: "very useful", "is simply", "very small angles", "remarkably"; sentences of 50-55 words in Sections 5.3 and 5.4.
- consistency 3: title-case headings; "numpy"; `$180°$` (a Unicode degree sign inside KaTeX, where the rest of the series writes symbols in LaTeX).
- publishing 2: description of 423 characters; six title-case headings.

Total 23 of 28.

## Priority

P2.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 423 characters, a list |
| P2 | Should fix | `:19, :75, :111, :197, :274, :372` | publishing | Title-case headings |
| C1 | Should fix | `:448-453` | evidence | Reference format (comma outside quote, "3rd edition") and order |
| C2 | Should fix | `:109, :195, :289, :370` | language | "very useful", "remarkably", "is simply", "very small angles" |
| C3 | Should fix | `:17` | consistency | "numpy" in prose |
| C4 | Optional | `:366` | language | Two sentences of 50 and 55 words in the Section 5.3 discussion |
| C5 | Optional | `:370` | consistency | `$180°$` in math |
| D1 | Optional | `:17` | structure | Second opening paragraph lists the sections |

### P1. Description
- **Text:** "The finite element method from its variational form: weak formulations and essential and natural boundary conditions, the energy principle, ..."
- **Correction:** "How the finite element method follows from the weak form of a boundary value problem, and how its error depends on mesh size and element degree."

### P2. Headings
- "## 1. From Strong Form to Weak Form", "## 2. Galerkin's Method", "## 3. Linear Elements in One Dimension", "## 4. Higher-Order Elements and Error Estimates", "## 5. Two Dimensions", "## 6. Comparing the Three Families" → sentence case (Galerkin stays capitalized).

### C1. References
- "R. Courant, "Variational methods ... vibrations", *Bulletin ...*" → comma inside the quote; "3rd ed.", "7th ed."; alphabetical (Brenner, Courant, Hughes, Johnson, Strang, Zienkiewicz).

### C2. Intensifiers and editorializing
- line 109 "the weaker but still very useful statement"; line 195 "The nodal values, remarkably, are exact"; line 289 "the element stiffness matrix is simply"; line 370 "very small angles worsen the condition number".
- **Correction:** "the weaker statement"; "The nodal values are exact"; "is"; "angles close to zero worsen".

### C4. Long sentences
- line 366 "On this particular mesh, the linear-triangle stiffness matrix is exactly $h^2$ times the five-point matrix (each right-angled triangle ...), and vertex quadrature gives ..." and "On a uniform grid of a square, the finite element method has no advantage; its value lies in what finite differences cannot do easily: ..." → split.

## Revision log (wave 1)

- Structure: no section moved; the second opening paragraph now states the order of the argument instead of listing sections (D1).
- Prose: intensifiers and "remarkably" removed; Section 5.3 discussion rewritten in shorter sentences ("The second column holds a lesson" replaced by a specific statement); in Section 5.4 the mass matrix sentence split and **mass matrix** set as a defined term.
- Terminology/style: six headings in sentence case; "NumPy"; `$180^\circ$`.
- Metadata: description rewritten (one sentence, under 165 characters).
- References: house format, alphabetical. No bibliographic detail changed.
- Technical corrections: none.
- Remaining warnings and why they stay: none. Three `sentence-length` suggestions (46-51 words, Sections 2.2, 4.1, 5.4) kept: each is one definition or list that reads more clearly unbroken.
- Flags for independent review: none new.
- Vietnamese translation affected: no (no translation of this entry exists).

## Independent review (wave 2)

- Reviewer: independent reviewer (fact-check, technical, series), 2026-10-14; report `reviews/numerical-simulation.md`.
- Fact-check: pass (Courant 1943 confirmed; Zienkiewicz-Taylor-Zhu 7th ed. 2013 confirmed). Technical: pass (3 code blocks re-run, output identical; P2 element matrix, Exercise 2 matrix, Exercise 3 recomputed).
- Findings concerning this item: T3 (optional, line 292).
- Not verified: imprint years of Brenner-Scott 2008, Hughes 1987/2000, Johnson 1987, Strang-Fix 1973 not re-fetched in this pass.

## Revision log (wave 2 resolution)

- T3: the triangle's area in §5.2 is now written $|e|$ (the area of triangle $e$) instead of $|T|$, which avoids another meaning of $T$ in the series. Lint: 0 errors, 0 warnings. Syntax compiles. Vietnamese: no translation exists; notation only.
