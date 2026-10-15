<!-- audit: {"slug":"finite-differences-for-heat-and-waves","type":"article","series":"numerical-simulation","priority":"P2","before":{"purpose":4,"structure":4,"accuracy":3,"evidence":3,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":6,"optional":2}} -->
# Audit: Finite Differences for Heat and Waves

- Path: `src/content/blog/finite-differences-for-heat-and-waves.mdx` · Route: `/blog/finite-differences-for-heat-and-waves` · Type: article (series entry) · Series `numerical-simulation`, entry 2 of 5 · Words: 3,069 (`eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 4.
- structure 4.
- accuracy 3: all four Python blocks re-run with `python3 -I` (Python 3.13.16, NumPy 2.5.3): output identical. Recomputed $\cot^2(\pi/200) = 4{,}052$, $L^2/(\alpha\pi^2) = 101.3$ s, $\tfrac{4}{\pi^2}e^{-\pi^2/2} = 2.915\times10^{-3}$, the Crank–Nicolson factor $-0.9607$ at $\mu = 25$, Exercises 1-4 (0.018 s; $1.67\times10^{-5}$ s; 113 and 115 steps; 0.0099). Exercise 5 is loose (A1).
- evidence 3: reference titles end with the comma outside the closing quote, "2nd edition", not alphabetical.
- language 3: one 60-word sentence; "simply"; CFL abbreviation used in a heading before it is expanded.
- consistency 3: title-case headings; "numpy" in prose; "2 %" with a space (standards 5.5: no space before %).
- publishing 2: description of 350 characters; seven title-case headings.

Total 22 of 28.

## Priority

P2: should-fix metadata and style problems plus one loose numerical statement in an exercise answer.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| A1 | Should fix | `:406`, Exercise 5 | accuracy | Growth factor and error estimates stated loosely; "within a factor of about 100" overstates the gap |
| P1 | Should fix | `:3` | publishing | Description 350 characters, a list |
| P2 | Should fix | `:19, :70, :135, :161, :260, :270, :352` | publishing | Title-case headings |
| C1 | Should fix | `:283, :297` | language | "CFL" in the heading of 6.2 before its expansion |
| C2 | Should fix | `:427-432` | evidence | Reference format and order |
| C3 | Should fix | `:133, :336`; `:17` | consistency | "2 %", "4 %", "5 %"; "numpy" |
| C4 | Optional | `:258` | language | 60-word sentence on A- and L-stability; "or simply BTCS" |
| D1 | Optional | `:17` | purpose | The opening names the CFL condition without its abbreviation, which the heading of 6.2 then uses |

### A1. Exercise 5: growth factor and estimates
- **Where:** line 406, Exercise 5 answer
- **Text:** "The shortest grid mode is multiplied by a root of the quadratic of Section 6.2 with modulus about 1.84 at every step ... the same estimate gives about $10^{10}$ and $10^{36}$, within a factor of about 100 of the observed $4.5\times10^{8}$ and $7.6\times10^{34}$"
- **Problem:** The modulus depends on the grid, because the shortest mode has $\xi = (N-1)\pi/N$. Recomputed (roots of $G^2 - 2(1 - 2\nu^2\sin^2(\xi/2))G + 1 = 0$, $\nu = 1.05$): 1.839 ($N = 20$), 1.868 ($N = 40$), 1.875 ($N = 80$). With 48, 95 and 190 steps from $10^{-16}$: $5.0\times10^{-4}$, $6.0\times10^{9}$, $7.4\times10^{35}$, which are 13 and 10 times the observed values, not "about 100". With 1.84 on every grid the estimates would be $1.4\times10^{9}$ and $2\times10^{34}$, not $10^{10}$ and $10^{36}$. The 2026-10-13 series review lists the same three estimates ($5.0\times10^{-4}$, $6\times10^{9}$, $7\times10^{35}$).
- **Correction:** "with modulus 1.84 on the coarsest grid and 1.87 on the two finer ones ... the same estimate gives about $6\times10^{9}$ and $7\times10^{35}$, within a factor of about 15 of the observed ..."

### P1. Description
- **Where:** line 3: "Time stepping for the heat and wave equations: the method of lines and stiffness, the explicit, implicit and Crank–Nicolson schemes, ..."
- **Correction:** "How explicit and implicit finite-difference schemes advance the heat and wave equations in time, and why stability, not accuracy, limits the time step."

### P2. Headings
- **Where:** "## 1. The Heat Equation on a Grid", "## 2. The Explicit Scheme", "## 3. The Implicit Scheme", "## 4. Crank–Nicolson and the θ-Scheme", "## 5. Consistency, Stability, Convergence", "## 6. The Wave Equation", "## 7. Choosing a Scheme"
- **Correction:** Sentence case; Section 5 becomes "Consistency, stability and convergence" (no fragment link points to it).

### C1. CFL
- **Where:** line 283 "### 6.2 Stability and the CFL condition"; expansion at line 297.
- **Correction:** Expand in the opening ("the Courant–Friedrichs–Lewy (CFL) condition"), so that the heading follows the definition.

### C2. References
- **Where:** lines 427-432, e.g. "J. Crank and P. Nicolson, "A practical method ... heat-conduction type", *Proceedings ...*"
- **Problem:** Standards 7.3: comma inside the closing quote, "2nd ed.", alphabetical (Courant, Crank, Lax, LeVeque, Morton, Strikwerda).

### C3. Percent spacing and library name
- **Where:** line 133 "to within 2 %. A 4 % increase"; line 336 "5 % above the limit"; line 17 "Python 3 with numpy".
- **Correction:** "2%", "4%", "5%"; "NumPy".

### C4. Long sentence
- **Where:** line 258, "In terms of the stability regions of the numerical integration notes, the trapezoidal rule is **A-stable** (...) but not **L-stable** (...), while backward Euler is both." and "or simply BTCS where second-order time accuracy is not needed".
- **Correction:** Split into two sentences; "or BTCS throughout where ...".

## Revision log (wave 1)

- Structure: unchanged (sections, numbering and fragment targets kept).
- Prose: the A-/L-stability sentence split in two; "simply" removed; the opening now expands CFL.
- Terminology/style: seven headings in sentence case (Section 5 "Consistency, stability and convergence"); "NumPy" in prose; "2%", "4%", "5%".
- Metadata: description rewritten (one sentence, 151 characters).
- References: house format (comma inside the closing quotation mark, "2nd ed."), alphabetical. No bibliographic detail changed.
- Technical corrections: Exercise 5 answer corrected (A1). Evidence: the roots of the Section 6.2 quadratic for $\nu = 1.05$ and $\xi = (N-1)\pi/N$, computed with NumPy, have moduli 1.8391, 1.8678, 1.8750; $1.8391^{48}\times10^{-16} = 5.0\times10^{-4}$, $1.8678^{95}\times10^{-16} = 6.0\times10^{9}$, $1.8750^{190}\times10^{-16} = 7.4\times10^{35}$; ratios to the observed $4.52\times10^{8}$ and $7.64\times10^{34}$ are 13 and 10.
- Remaining warnings and why they stay: none. Suggestion kept: `acronym-expansion` "SIAM" in the reference list (publisher's name).
- Flags for independent review: technical reviewer to confirm the corrected Exercise 5 wording (A1).
- Vietnamese translation affected: no (no translation of this entry exists).

## Independent review (wave 2)

- Reviewer: independent reviewer (fact-check, technical, series), 2026-10-14; report `reviews/numerical-simulation.md`.
- Fact-check: pass (Courant-Friedrichs-Lewy 1928, Crank-Nicolson 1947, Lax-Richtmyer 1956 confirmed). Technical: pass (4 code blocks re-run, output identical; corrected Exercise 5 confirmed: moduli 1.8391/1.8678/1.8750, estimates 5.0e-4, 6.0e9, 7.4e35, ratios 13 and 10).
- Findings concerning this item: S1 (its matrix `T` = tridiag(1,-2,1) conflicts with entry 3's `T`; correction proposed in entry 3, no change needed here).
- Not verified: imprint years of LeVeque 2007, Morton and Mayers 2005, Strikwerda 2004 not re-fetched in this pass.
