# Live review: The Finite Element Method

- URL: https://acrr.asia/blog/finite-element-method
- Source: `src/content/blog/finite-element-method.mdx` (Numerical Simulation for Engineers, entry 4 of 5)
- Commit deployed: `7e20c2c`; the source is unchanged between that commit and the reviewed branch
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40129647345 (2026-10-24 20:29 UTC): 21 desktop-light, 37 mobile-light, 37 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-24. The reviewer did not write or revise this article.
- Risk: routine (a technical explainer; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Request revision. One major presentation finding (L1): the weak form of Section 1.2, the definition the whole page builds on, shows a(u, v) but hides ℓ(v), and with it the flux term that the next paragraph calls the natural boundary condition; at 360 px further key displays are cut, including the L² estimate of Section 4.2. The rest is minor.

**Library decision: retain and update.** The page is the only ACRR introduction to the finite element method: weak form, essential and natural conditions, Galerkin orthogonality, element assembly, a priori estimates and linear triangles, each rate confirmed by a script. It ties the series together (the FD matrix of entry 1, the SPD systems and conjugate gradients of entry 3, the time stepping of entry 2) without repeating them. The content is accurate; the update is presentational (L1, L2), and no section needs rewriting, merging or moving.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineer or student who knows finite differences (entries 1 to 3) and meets FEM in a commercial or open-source code without knowing what it computes or why it converges.
- Problem: what the weak form is and why it allows meshes of any shape; what essential and natural boundary conditions mean in practice; why Galerkin's method is accurate; what convergence rate to expect from linear and quadratic elements.
- Outcome: derive a weak form with Dirichlet, Neumann or Robin conditions; assemble element matrices into K; state and check the rates h^d and h^(d+1); recognize when FEM and finite differences give the same equations and when FEM is worth its cost.
- Distinctive contribution: the method built in the order its theory needs, with every element matrix written out, the predicted orders measured (1 and 2 for linear, 2 and 3 for quadratic elements), and the exact identity between linear triangles and the five-point matrix on a uniform mesh shown by computation.
- Evidence: derivations in the text; three scripts with their real output; Brenner and Scott, Courant (1943), Hughes, Johnson, Strang and Fix, Zienkiewicz, Taylor and Zhu.
- Limitations: linear elliptic model problems; one and two dimensions; adaptivity, non-smooth solutions, isoparametric and three-dimensional elements described but not computed.

The contract is delivered. The opening explains why a different starting point is needed and states the order of the argument; Sections 1 and 2 give the theory, Section 3 makes it concrete in one dimension, Section 4 adds degree and the estimates, Section 5 moves to two dimensions, Section 6 places FEM among the three families. Every major section serves the central question. The honest statement in Section 5.3 that FEM has no advantage on a uniform square grid, with the reasons it is used anyway, is a strength. Checked by computation for this review: all three scripts re-run with Python 3 and NumPy (output identical, line for line); the element matrix of Exercise 2; Exercise 3 (3.15×10⁻²·64/N = 7.98×10⁻⁴ gives N = 2526, "about 2,500"); the comparison of 8 quadratic with 32 linear elements (2.46×10⁻⁴ against 6.22×10⁻⁴); h times the entry-1 matrix in Section 3.2; F_i = h²f from six triangles of total area 3h². The page is worth its 24 minutes. Value category: conceptual understanding. Format: explainer.

What is missing: no picture of a hat function, a pyramid basis function or a triangle mesh. A figure of the hat functions on a 1D mesh (Section 3.1) and of the two-triangle split of a grid square (Section 5.3) would make the "locality gives sparsity" and "no diagonal neighbors" arguments visible (optional, standards 6.8).

Overlap noticed (none is duplication; all are linked):

- `solving-large-linear-systems` (entry 3): the SPD property, the energy functional φ(V) minimized by conjugate gradients and the five-point matrix; this page derives where they come from.
- `from-differential-equations-to-discrete-problems` (entry 1): the test problem, the FD matrix and the Robin condition; reused by name.
- `finite-differences-for-heat-and-waves` (entry 2): time stepping via the method of lines, one sentence and a link. For the overlap map: "the comparison of finite differences, finite elements and finite volumes" exists only here.

## C. Substantive findings

None. No technical or factual error was found on the page.

## D. Visual and structural findings

### L1. The weak form and other key displays cut off

- Location: Section 1.2, the weak-form display after "find u with u(0) = 0 such that" (desktop-light-03; at 360 px mobile-light-05); Section 1.1, the model problem (desktop-light-02, mobile-light-03). At 360 px also Section 1.2, the integration-by-parts display (mobile-light-05); Section 2.1, the Galerkin equations (mobile-light-09); Section 4.2, the a priori estimates (mobile-light-18); Section 5.1, the two-dimensional weak form (mobile-light-22).
- Problem: at 1280 px the weak form shows "a(u, v) = ℓ(v) for all admissible v, a(u, v) = ∫ k u′v′ dx," and stops: the definition "ℓ(v) = ∫ f v dx + q_L v(L)" is off the right edge with nothing to show it is there. The model problem loses "= q_L". At 360 px the weak form stops at "for all admissible", the Galerkin system loses "⟺ KU = F", the estimates show only the H¹ bound (the L² bound C′h^(d+1) is hidden), and the 2D weak form loses its boundary integrand and quantifier.
- Why it matters: ℓ(v) is where the flux condition enters; the very next bullet ("the flux condition appears inside ℓ(v) ... a natural boundary condition") and Exercise 1 depend on seeing it. The L² estimate is the result Sections 3.3 and 4.2 measure. A reader who does not discover the hidden scroll reads the definitions incomplete.
- Required action: put the weak-form statement, a(u, v) and ℓ(v) on three lines (an `aligned` block, or the statement in one display and the two definitions in a second); break the model problem before the boundary conditions. For 360 px, split the Galerkin system before "⟺", put the two estimates on separate lines, and break the 2D weak form before "+ ∫_ΓN".
- Priority: major
- Acceptance condition: on new captures, the definition of ℓ(v) and the condition k(L)u′(L) = q_L are visible without sideways scrolling at 1280 px, and at 360 px the weak form, the L² estimate and the Galerkin system "KU = F" are visible without scrolling.

The site-level issues are present and not raised again: no scroll cue for the Section 5.2 Mermaid workflow at 360 px (only "Geometry", "Mesh", "Element matrices" visible, mobile-light-24), and the comparison table of Section 6 scrolls at 360 px (7rem minimum cell width). `facts.json` reports one SVG figure without a title; every page in this capture run reports the same for its diagrams, so it is a site-level property of the Mermaid output, not of this page.

## E. Technical and source findings

### L2. Output columns cut in Sections 3.3 and 5.3

- Location: Section 3.3 output block (desktop-light-09) and Section 5.3 output block (desktop-light-15).
- Problem: at 1280 px the H¹ orders of Section 3.3 are cut ("H1 1."), and in Section 5.3 the "True" of the stiffness-matrix comparison is visible only on the first line. The prose calls that last column "the more instructive result".
- Why it matters: small; the prose states both results.
- Required action: optional; shorter labels (for example "same as 5-point x h^2:") would let the lines fit. Changing the code means re-running it.
- Priority: minor
- Acceptance condition: both output blocks fully visible at 1280 px, or the finding is accepted as a limitation of wide code output.

No technical or source errors found. `facts.json`: HTTP 200 on all three viewports, no horizontal page scroll at 360 px, 0 KaTeX errors, no broken images, no console errors, no overflowing elements, capture not truncated. Dark mode: equations, element matrices, code and the Mermaid diagram are legible on mobile-dark tiles 17 to 24. The six references are in the house format and alphabetical; imprint years were not re-verified in this review.

## F. Required changes

Mandatory:

- [ ] L1: split the weak form and the model problem so that ℓ(v) and the flux condition are visible at 1280 px, and the key displays at 360 px.

Optional:

- [ ] L2: shorter output labels in the Sections 3.3 and 5.3 scripts.
- [ ] Exercise 3: "From the table in Section 3.3" also needs the quadratic H¹ error, which is in the table of Section 4.2; "From the tables in Sections 3.3 and 4.2" is exact.
- [ ] A figure of the 1D hat functions and of the two-triangle split of a grid square.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
