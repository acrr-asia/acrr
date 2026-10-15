# Series audit: Numerical Simulation for Engineers (`numerical-simulation`)

- Scope: `src/content/series/numerical-simulation.md` and the five entries, in order: `from-differential-equations-to-discrete-problems`, `finite-differences-for-heat-and-waves`, `solving-large-linear-systems`, `finite-element-method`, `verifying-and-validating-a-simulation`. Related item outside scope: `src/content/blog/numerical-integration-notes.mdx`.
- Audited at commit `e21dcc8`, 2026-10-13, by the Content Auditor role; revised in wave 1 by the developmental and copy-editing roles (see each item's revision log).
- Previous review: `reviews/numerical-simulation.md` (resolved 2026-10-13). None of its corrections was undone; F1-F17 were re-read in place.

## Item summary

| Item | Priority | Score before (of 28) | Main problems |
|---|---|---|---|
| Series overview | P2 | 20 | No sequence rationale or conventions; one 77-word sentence; description 225 characters; bundled objective |
| Entry 1 | P1 | 23 | Description 387 characters; title-case headings; reference format |
| Entry 2 | P2 | 22 | Description 350; headings; loose Exercise 5 estimate (corrected) |
| Entry 3 | P2 | 23 | Description 385; headings; "D. Bau" (now "D. Bau III"); 199-word paragraph |
| Entry 4 | P2 | 23 | Description 423; headings; intensifiers |
| Entry 5 | P2 | 23 | Description 387; headings; broken label "**time step error.**"; JCGM references without year |

## Systemic problems (all five entries)

1. **Descriptions** of 350-423 characters, each a list of the entry's sections, used as card summary and meta description. All rewritten to one sentence of 144-165 characters saying what the reader learns.
2. **Title-case section headings** (35 headings). All set in sentence case; words unchanged except entry 2 Section 5 ("Consistency, Stability, Convergence" → "Consistency, stability and convergence") and entry 3 Section 4.2 ("... and SOR" → "... and successive over-relaxation"). Fragment slugs are lowercase, so the six in-series fragment links still resolve; grep over `src/` found no link from outside the series to any fragment of these entries and no "Section x.y" reference to them from outside.
3. **Reference lists** not in the house format of standards 7.3: "2nd edition" for "2nd ed.", comma outside the closing quotation mark, not alphabetical; JCGM entries without a year. All fixed; no bibliographic detail changed except "D. Bau" → "D. Bau III" (entry 3, confirmed by a library catalogue record).
4. **"numpy"** in prose for the library NumPy (lowercase kept in code). **Space before %** ("2 %", "98 %", "95 %") against standards 5.5. **"The ACRR note"** (unexpanded abbreviation) for links to insights. All fixed.
5. **"time-step" vs "time step"**: no "time-step" remained in scope. The only trace was a broken list label in entry 5 Section 3.4, "**time step error.**" (lowercase, apparently from a mechanical replacement); now "**Time discretization error.**". Entry 5's table cell "Grid and time step refinement" (a compound modifier the glossary does not allow to hyphenate) is now "Refinement of the grid and the time step".

## Structural consistency across entries

- Every entry has opening paragraphs without a heading, numbered sections, numbered Exercises with answers in `<details>`, a numbered Summary with a question-and-answer table and a closing paragraph, and `### References` under the Summary. The convention is uniform, so nothing was renumbered.
- Opening paragraphs: each states what it builds on (linked), what it covers, and the tools (Python 3, NumPy, double precision). Entries 1 and 4 had a second opening paragraph that listed the sections; both now state the purpose or order of the argument instead.
- Closing transitions: entries 1-4 lead to the next entry (entry 1's is now linked); entry 5 closes the series against the chain of Section 1.1 of entry 1.
- Code: 17 Python blocks re-run with `python3 -I` (Python 3.13.16, NumPy 2.5.3), each file's blocks in order in one namespace; every printed output matches the text. SciPy is not installed in this environment and none of the code uses it.

## Notation and terminology

Consistent across the series: $-\nabla^2 u = f$; capital $U$ discrete, lowercase $u$ exact; $h$ mesh size and $\Delta t$ time step (with the explicit mapping to the notes' $h$); $u_r$ for unit roundoff; $U_{\!f}$ for the LU factor; $r$ residual (entry 3) and refinement ratio (entry 5), each defined locally; "entry" vocabulary; en dash in Crank–Nicolson, Gauss–Seidel, Courant–Friedrichs–Lewy. No conflict found.

## Overlap with the numerical integration notes (outside scope)

- No duplicated explanation: entries 1 and 2 cite the notes for the meaning of order, the explicit Euler stability bound $|1 + h\lambda| \le 1$ and the stability-region picture, and do not re-derive them. Entry 2 §4.3 introduces A- and L-stability itself and attributes only the stability regions to the notes (the series review's F1 correction holds).
- No conflicting explanation. Two small differences for the owner of the notes: (a) the notes write "Runge-Kutta" with a hyphen, while the series and the insight *What Makes a Simulation Trustworthy?* use the en dash of a two-person name ("Runge–Kutta" in the insight; the series does not name the method); (b) the notes end "Stiff problems ... usually call for implicit methods, which are outside the scope of these notes" without pointing to entry 2 §1.2-3, which now treats stiffness and implicit schemes; a forward link from the notes would help readers.
- Notation: the notes use $h$ for the time step, the series uses $h$ for the mesh size; entry 1 §4.1 and entry 2 §4.3 state the mapping explicitly, so no change is needed.

## Overview page against standards 6.5

Before: audience and prerequisites present; sequence rationale, shared conventions and the connection between entries missing; objective 4 combined two outcomes. After revision the overview has three paragraphs (reader and prerequisites with links; why the entries come in this order and what each hands to the next; shared conventions) and five objectives, each beginning with an assessable verb and each covered by one entry (1: entry 1; 2: entry 2; 3: entry 3; 4: entry 4; 5: entry 5). It promises nothing the entries do not deliver: the claim about experiments is the "main convergence rates and stability limits" wording of the series review's F6.

## Cross-references

All "first/second/.../fifth entry" mentions, the six fragment links (`#43-the-method-of-lines`, `#22-banded-and-tridiagonal-systems`, `#52-checking-the-orders-and-where-rounding-takes-over`, `#11-the-five-point-matrix`, `#51-solving-by-minimizing`, `#41-why-iterate`) and the "Section x.y" citations were checked after revision; `eos lint` reports no `series-crossref` or `section-reference` problem. The link to the measurement entry of the sensor series (`#52-evaluating-uncertainty`) is unchanged.

## Translation

No entry of this series has a Vietnamese translation. The Vietnamese series file `src/content/series/vi/numerical-simulation.md` needs updating: new description, five objectives instead of four, and a rewritten body (copied fields unchanged, so the build is unaffected).

## Gate note

The series review stamp in `reviews/numerical-simulation.md` hashes the series file and the English articles; every file changed in this wave, so `node scripts/series-pipeline.mjs gate` will report the review stale until a new series review and `stamp`.
