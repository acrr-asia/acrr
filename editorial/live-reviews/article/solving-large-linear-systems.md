# Live review: Solving Large Linear Systems

- URL: https://acrr.asia/blog/solving-large-linear-systems
- Source: `src/content/blog/solving-large-linear-systems.mdx` (Numerical Simulation for Engineers, entry 3 of 5)
- Commit deployed: `7e20c2c`; the source is unchanged between that commit and the reviewed branch
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40129647345 (2026-10-24 20:29 UTC): 23 desktop-light, 41 mobile-light, 41 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-24. The reviewer did not write or revise this article.
- Risk: routine (a technical explainer; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Request revision. One major presentation finding (L1): the conjugate gradient iteration of Section 5.1, the one algorithm the page writes out in full, is cut at 1280 px after "r^(m+1) = r^(m) − α_m"; the search-direction update that makes the method conjugate is not visible. At 360 px the matrix T of Section 1.1 is hidden as well. The rest is minor.

**Library decision: retain and update.** The page is ACRR's only treatment of sparse linear solvers: structure of discretization matrices, banded and sparse direct methods, fill-in, conditioning and the rounding floor, stationary iterations, multigrid in outline, conjugate gradients and preconditioning, closed by a measured comparison and a decision guide. Entries 2, 4 and 5 and `distributed-memory-and-message-passing` link into its sections. The content is accurate; the update is presentational (L1, L2), and no section needs rewriting, merging or moving.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineer or student who can set up a discretization (entries 1 and 2) and now faces a two- or three-dimensional system too large for a dense library call.
- Problem: whether to use a direct or an iterative solver, and why the answer depends on dimension, size and conditioning.
- Outcome: estimate the memory and flops of dense, banded and sparse direct solvers; explain fill-in and the condition number's growth like h⁻²; predict iteration counts for Jacobi, Gauss–Seidel, SOR and CG; choose a solver family for a given problem.
- Distinctive contribution: every cost and rate is tied to the series' own model problem and checked by computation (fill-in of 98% of the band, κ against cot²(πh/2), the rounding floor at N = 10⁵ to 10⁶, measured iteration counts against the spectral-radius and CG-bound predictions), ending in a cost table and a decision diagram.
- Evidence: derivations and operation counts in the text; five scripts with their real output; Briggs, Henson and McCormick; Davis; George (1973); Golub and Van Loan; Hestenes and Stiefel (1952); Higham; Saad; Trefethen and Bau.
- Limitations: SPD model problem only; multigrid and preconditioners described, not implemented; nonsymmetric Krylov methods (GMRES, BiCGSTAB) out of scope.

The contract is delivered. Section 1 sets up the matrix and why size matters; Section 2 covers direct methods and fill-in; Section 3 shows why refinement eventually stops paying, with the rounding floor demonstrated rather than asserted; Sections 4 and 5 present the iterative families with their convergence rates; Section 6 measures them; Section 7 answers the page's question with a table and a flowchart. Every major section serves the central question. Checked by computation for this review: all five scripts re-run with Python 3 and NumPy, with the Section 3.2 block after the `thomas` definition as the text says (output identical, line for line); 30,256 band positions and 98% fill at N = 32; 7.5 TB and 54 MB in Section 1.2; 10⁸ flops and 8 MB, 9×10¹³ flops and 76 GB in Section 2.4; the crossover h ≈ u_r^(1/4) ≈ 10⁻⁴ and κu_r ≈ 4.5×10⁻⁵ at N = 10⁶; the SOR predictions 47, 94, 188 and the CG bound 97 at N = 16; the factor 128 between Jacobi and CG; Exercise 2 (61,152) and Exercise 4, re-run in float32 (smallest error 1.7×10⁻⁵ at N = 256, 3.6×10⁻⁴ at N = 1024). The page is worth its 24 minutes. Value category: technical decision (direct against iterative, with explicit cost criteria), with conceptual understanding close behind. Format: explainer.

Overlap noticed (none is duplication):

- `distributed-memory-and-message-passing` (Parallel and High-Performance Computing): uses the Jacobi iteration of Section 4.2 as its parallel example and links it; complementary.
- `gradient-descent-and-its-variants` (Machine Learning Foundations): explains the condition number and the zig-zag of steepest descent on an elongated quadratic, the point Section 5.1 makes in one sentence. Not linked from here; an optional cross-link (Phase 7 overlap map: "condition number and steepest descent" explained in both).
- `gaussian-processes-and-kernels` and `scaling-bayesian-deep-learning`: use Cholesky factorization and conjugate gradients for kernel matrices; different context, no shared explanation.
- `finite-element-method` (entry 4): derives the SPD property and the energy functional φ; both pages link each other.

## C. Substantive findings

None. No technical or factual error was found on the page.

## D. Visual and structural findings

### L1. Conjugate gradient iteration cut off; matrix T hidden at 360 px

- Location: Section 5.1, the display after "two inner products and three vector updates" (desktop-light-13; at 360 px mobile-light-24). At 360 px also Section 1.1, the definition of A and T (mobile-light-04), the model problem and the five-point formula (mobile-light-03).
- Problem: at 1280 px the four CG formulas are set on one line wider than the column. The reader sees α_m, the update of U and "r^(m+1) = r^(m) − α_m"; the rest of the residual update and the whole search-direction update p^(m+1) = r^(m+1) + (r^(m+1)ᵀr^(m+1) / r^(m)ᵀr^(m)) p^(m) are off the right edge with no cue. At 360 px only α_m and the start of the U update are visible. In Section 1.1 at 360 px the display shows "A = (1/h²)(I⊗T + T⊗I), T =" and the matrix T itself is not visible.
- Why it matters: the text announces "three vector updates" and the reader can see one and a half; the direction update is what distinguishes CG from steepest descent, which the paragraph above has just contrasted with it. T is the building block of every matrix on the page and of the cross-references from entries 1 and 2.
- Required action: set the CG iteration as an aligned block with one formula per line (α_m, U, r, p), and at 360 px put the definition of T on its own line below A (or as a second display).
- Priority: major
- Acceptance condition: on new captures, all four CG formulas are fully visible without sideways scrolling at 1280 px and at 360 px, and the matrix T of Section 1.1 is visible at 360 px.

The site-level issues are present and not raised again: no scroll cue for wide displays at 360 px, and the Section 7 cost table scrolls at 360 px (7rem minimum cell width). At 360 px the Section 7 decision flowchart fits by scaling, with labels at roughly 8 px (mobile-light-32); legible, but small. `facts.json` reports one SVG figure without a title, as every page with a diagram in this capture run does (site-level property of the Mermaid output).

## E. Technical and source findings

### L2. Output columns cut in Sections 2.4 and 3.1

- Location: Section 2.4 output block (desktop-light-06); at 360 px also Section 3.1 (mobile-light-14).
- Problem: at 1280 px the "min eigenvalue" column of the fill-in script is cut after "min eigen", although the next paragraph starts from those values (19.487, 19.676, 19.723 approaching 2π²). At 360 px the Section 3.1 output hides the cot² and 4/(πh)² columns it compares.
- Why it matters: small; the prose restates the conclusion, but not the three eigenvalues.
- Required action: optional; shorter labels (for example "nnz(A)", "nnz(L)", "SPD", "λmin") would let the Section 2.4 lines fit at 1280 px. Changing the code means re-running it.
- Priority: minor
- Acceptance condition: the Section 2.4 output fully visible at 1280 px, or the finding is accepted as a limitation of wide code output.

No technical or source errors found. `facts.json`: HTTP 200 on all three viewports, no horizontal page scroll at 360 px, 0 KaTeX errors, no broken images, no console errors, no overflowing elements, capture not truncated. Dark mode: equations, code, the tables and the flowchart are legible on mobile-dark tiles 13 to 16 and 29 to 32. The eight references are in the house format and alphabetical; imprint years were not re-verified in this review.

## F. Required changes

Mandatory:

- [ ] L1: one formula per line for the CG iteration, and T on its own line at 360 px.

Optional:

- [ ] L2: shorter output labels in the Section 2.4 script.
- [ ] Section 4.1: "storage only for A's nonzeros" renders with an opening quotation mark after the math (A‘s, desktop-light-10, mobile-light-17); write the apostrophe explicitly or rephrase ("the nonzeros of A").
- [ ] Sections 3.1 and 3.2: on desktop, inline math at a line end pushes the following comma or period to the start of the next line (", and the same value holds", ". The two cross near"; desktop-light-08); a non-breaking join or a reworded sentence avoids it.
- [ ] Section 7 flowchart: "10^5" in the first box could read "10⁵" (Unicode superscript) to match the text.
- [ ] Section 5.1: a link to `gradient-descent-and-its-variants` where steepest descent and elongated level sets are mentioned.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
