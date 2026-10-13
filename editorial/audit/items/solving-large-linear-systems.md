<!-- audit: {"slug":"solving-large-linear-systems","type":"article","series":"numerical-simulation","priority":"P2","before":{"purpose":4,"structure":4,"accuracy":4,"evidence":3,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":6,"optional":2}} -->
# Audit: Solving Large Linear Systems

- Path: `src/content/blog/solving-large-linear-systems.mdx` · Route: `/blog/solving-large-linear-systems` · Type: article (series entry) · Series `numerical-simulation`, entry 3 of 5 · Words: 3,274 (`eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 4.
- structure 4.
- accuracy 4: all five Python blocks re-run with `python3 -I` in order (the rounding block after the `thomas` definition, as the text says), Python 3.13.16, NumPy 2.5.3: output identical. Recomputed: the iteration predictions $\ln(10^8)/(-\ln\rho)$ (Jacobi 949, 3,816, 15,283; SOR 47, 94, 188), the constants $3.7N^2$, $1.9N^2$, $2.9N$, the CG bound (97, 194, 389), 8 TB and 7.5 TB, 76 GB and $9\times10^{13}$ flops, Exercise 1 (768, 7.8, 0.4 megabytes).
- evidence 3: "D. Bau" for David Bau III; reference format and order.
- language 3: a 199-word paragraph (Section 4.3), sentences of 55-67 words, "essentially".
- consistency 3: "SOR" in a heading before its expansion; "numpy"; "98 %".
- publishing 2: description of 385 characters; eight title-case headings.

Total 23 of 28.

## Priority

P2.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 385 characters, a list |
| P2 | Should fix | `:19, :57, :132, :186, :194, :216, :255, :329` | publishing | Title-case headings |
| C1 | Should fix | `:194, :200` | language | "SOR" in the heading of 4.2 before its expansion |
| C2 | Should fix | `:214` | language | 199-word paragraph with a 67-word sentence |
| C3 | Should fix | `:417-424` | evidence | Reference format and order; "D. Bau" should be "D. Bau III" |
| C4 | Should fix | `:17, :100, :128, :387` | consistency | "numpy" in prose; "98 %" |
| C5 | Optional | `:128, :130, :251` | language | "essentially full"; 55- and 57-word sentences |
| C6 | Optional | `:184`; `:360` | language | "The ACRR note"; "MB" unexpanded |

### C1. SOR before expansion
- **Where:** line 194 "### 4.2 Jacobi, Gauss–Seidel and SOR"; expansion at line 200 "**Successive over-relaxation** (SOR)".
- **Correction:** Heading "Jacobi, Gauss–Seidel and successive over-relaxation" (no fragment link targets 4.2; checked with grep over `src/`).

### C2. Section 4.3 paragraph
- **Where:** line 214, "The slow convergence has a clear cause. ... is a standard introduction." (199 words)
- **Problem:** Three topics in one paragraph: why Jacobi is slow, weighted Jacobi as a smoother, multigrid.
- **Correction:** Split into two paragraphs at "**Weighted Jacobi**" and at "After a few such iterations"; split the 67-word sentence.

### C3. References
- **Where:** line 418 "L. N. Trefethen and D. Bau, *Numerical Linear Algebra*, SIAM, 1997."
- **Problem:** The second author is David Bau III, as on the book's title page (SIAM, 1997). Format: "2nd ed.", comma inside closing quotes, alphabetical order (Briggs, Davis, George, Golub, Hestenes, Higham, Saad, Trefethen).

### C4. Name and percent
- **Where:** "Python 3 with numpy" (17), "Cholesky factor with numpy" (100), "98 %" (128), "in numpy `float32`" (387).
- **Correction:** "NumPy"; "98%".

### C5, C6. Minor wording
- "the band is essentially full" (98% of the band): "almost full". The nested-dissection sentence (55 words) and the preconditioner sentence (57 words) split. "The ACRR note on [floating-point rounding ...]" → "The insight on ..."; "768 MB" → "768 megabytes".

### P1. Description
- **Where:** line 3 "The sparse, structured systems that discretization produces and how to solve them: Gaussian elimination, LU and Cholesky factorization, ..."
- **Correction:** "How the sparse systems produced by discretization are solved, by direct factorization or by iteration, and how grid size decides which approach is cheaper."

## Revision log (wave 1)

- Structure: Section 4.3 split into three paragraphs (cause of slow convergence; weighted Jacobi as a smoother; multigrid). No section moved or renumbered.
- Prose: "essentially" removed; long sentences in the opening, Sections 2.4, 4.3 and 5.3 split; "The ACRR note" → "The insight"; "MB" written out.
- Terminology/style: eight headings in sentence case; heading 4.2 now "Jacobi, Gauss–Seidel and successive over-relaxation"; "NumPy" in prose; "98%".
- Metadata: description rewritten (one sentence, under 165 characters).
- References: "D. Bau III"; house format; alphabetical.
- Technical corrections: none.
- Remaining warnings and why they stay: none. Suggestions kept: `sentence-length` on one 46-word sentence (see lint output; a single argument), and `acronym-expansion` "SIAM" in the reference list (publisher's name).
- Flags for independent review: none. "D. Bau III" confirmed by web search on 2026-10-13 (library catalogue record "Numerical linear algebra / Lloyd N. Trefethen, David Bau III", catalogue.i2m.univ-amu.fr/bib/9110, and the author's page people.maths.ox.ac.uk/trefethen/text.html).
- Vietnamese translation affected: no (no translation of this entry exists).
