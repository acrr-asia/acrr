# Live review: From Differential Equations to Discrete Problems

- URL: https://acrr.asia/blog/from-differential-equations-to-discrete-problems
- Source: `src/content/blog/from-differential-equations-to-discrete-problems.mdx` (Numerical Simulation for Engineers, entry 1 of 5)
- Commit deployed: `1eb85d4` (master after PR #53); the source is unchanged between that commit and the reviewed branch
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/39980397404 (2026-10-23 15:43 UTC): 24 desktop-light, 43 mobile-light, 43 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-23. The reviewer did not write or revise this article.
- Risk: routine (a technical explainer; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Request revision. One major presentation finding (L1): the central-difference formula of Section 5.1, the result that Section 5.2 checks numerically, is cut off at 1280 px, and at 360 px all three Section 5.1 formulas are cut. The rest are minor.

**Library decision: retain and update.** The page is the foundation of its series: the four later entries cite its sections (4.3, 5.1, 6.1, 6.2) and its vocabulary, and no other ACRR page covers the model PDEs, boundary conditions, finite-difference truncation error and the consistency, stability and convergence vocabulary. The content is accurate and the worked numbers reproduce. The update is presentational only (L1 to L3): no section needs rewriting, merging or moving.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineer or student who knows calculus, basic linear algebra and ODEs, and is about to use or write a PDE solver without knowing what discretization does to the answer.
- Problem: understanding how a PDE becomes a finite algebraic problem, and what "error", "order", "consistent", "stable" and "convergent" mean for the result.
- Outcome: classify a model PDE and state the conditions it needs; derive a difference quotient and its truncation error from Taylor series; set up and solve the one-dimensional Poisson problem; measure an observed order of accuracy; recognize a boundary treatment that spoils the order.
- Distinctive contribution: one path from physical model to verified discrete solution, with every claim about order checked by a runnable script and every predicted error constant compared with the measured one (0.4207h, 0.09005h², 0.00822 against 0.00827, the ratio of about 300 at N = 80).
- Evidence: derivations in the text; three scripts with their real output (re-run for this review with Python 3 and NumPy: output identical, line for line); Higham, IEEE 754-2019, LeVeque, Morton and Mayers, Strauss, Strikwerda.
- Limitations: finite differences on uniform one-dimensional grids only; finite volumes not covered; the Lax equivalence theorem and time stepping deferred to entry 2.

The contract is delivered. The opening states the question and the prerequisites; Sections 1 to 4 build the model and the idea of discretization; Sections 5 and 6 carry it out and measure it; Section 7 names what was measured; Section 8 maps the series. Each major section serves the central question. Section 8 overlaps the series overview page, but it is short and ties each entry to the chain of Section 1.1, so it earns its place. The summary table answers the page's questions in one screen. Checked by computation for this review: the three code outputs, the error constants of Section 5.2, the h²π²/12 estimate (0.008225 at h = 0.1), the error ratio at N = 80 (292), the classification table of Section 2.4 (heat: a = α, c₀ = 0, discriminant 0; wave: a = −c², c₀ = 1, discriminant 4c² > 0), Exercises 1 (leading term −h²u'''/3), 3 (3.21×10⁻⁵ and 8.2×10⁻⁷), 4 (4000 s) and 5 (flux balance g − g₀ = −∫f). The page is worth its 25 minutes. Value category: conceptual understanding (with practical implementation close behind). Format: explainer.

Overlap noticed (none is duplication; all are linked):

- `numerical-integration-notes` (order of accuracy, time-step stability for ODEs): referenced in Sections 4.1, 4.2 and 7; this page applies the same notion to space discretization.
- `state-space-models-primer` (Foundations of Control Systems): the method of lines in Section 4.3 is pointed at its $\dot{x} = Ax$ form; complementary.
- `finite-differences-for-heat-and-waves` Section 1.2 repeats the method of lines and links back to Section 4.3; planned continuation.
- Insights `what-makes-a-simulation-trustworthy` and `floating-point-in-long-simulations`, and entry 5 (`verifying-and-validating-a-simulation`): the verification/validation distinction of Section 1.1 is stated briefly here and developed there. For the site-level overlap map: "order of accuracy and its measurement" is explained in this page, the numerical-integration notes and entry 5.

## C. Substantive findings

None. No technical or factual error was found on the page.

## D. Visual and structural findings

### L1. Section 5.1 central-difference formula cut off at desktop width

- Location: Section 5.1, the display equation after "subtracting the two expansions gives the central difference" (desktop-light-11); at 360 px also the Taylor expansion and the second-difference formula of the same section (mobile-light-20, mobile-light-21, mobile-dark-21).
- Problem: at 1280 px the display pairs the forward and the central difference on one line and is wider than the text column. Only "(u(x+h) − u(x−" with the denominator 2h is visible; the right-hand side "= u'(x) + (h²/6)u'''(x) + O(h⁴)" is hidden behind an unmarked sideways scroll. At 360 px the Taylor expansion ends at "(h²/2)u''", the forward difference at "(h/2)u''(x", and the second difference at "= u'", so none of the three truncation-error terms is visible.
- Why it matters: these truncation terms are the result of the section. Section 5.2 checks the constant h²/6 against the table, Section 6.1 uses h²/12, and the summary states the orders. A reader who does not discover the hidden scroll sees an incomplete formula where the argument depends on it.
- Required action: put the forward and the central difference in two separate displays (or an `aligned` block, one formula per line), and break the Taylor expansion and, if still needed at 360 px, the second-difference formula over two lines (for example the expansion with the odd terms on a second line).
- Priority: major
- Acceptance condition: on new captures, both difference formulas are fully visible without sideways scrolling at 1280 px, and at 360 px every Section 5.1 formula shows its truncation-error term without scrolling.

### L2. Other display equations cut at 360 px

- Location: Section 2.4, the general second-order equation (ends at "(lower-orde", mobile-light-12); Section 4.1, the grid definition ("Δx = L/N" hidden, mobile-light-17); Section 4.3, the method-of-lines system (index range hidden, only "j" visible, mobile-light-19); Section 6.1, the Poisson problem (boundary conditions u(0) = 0, u(1) = 0 hidden, mobile-light-24); Section 6.2, the mixed problem ("u'(1) = g" hidden, mobile-light-28).
- Problem: each display is wider than the 360 px column and scrolls sideways without a cue; in Sections 6.1 and 6.2 the hidden part is the boundary condition the subsection is about.
- Why it matters: a phone reader sees problems stated without their conditions; the text around them restates some, not all.
- Required action: split each display so that the equation and its conditions are on separate lines (for example `\begin{gathered}` or two displays).
- Priority: minor
- Acceptance condition: at 360 px each of the five displays is fully visible, or the part that remains hidden is not needed to read the equation.

### L3. Section 1.1 flowchart: last two stages off-screen at 360 px

- Location: Section 1.1, the Mermaid chain "Physical system → Mathematical model → Discrete problem → Computed numbers" (mobile-light-04, mobile-dark-04).
- Problem: at 360 px only the first two boxes and part of the third are visible; "Computed numbers", where the round-off and iteration errors of the following list arise, is hidden to the right with no scroll cue.
- Why it matters: the diagram introduces the three error sources the page and the series are organized around; on a phone the reader sees half the chain.
- Required action: a top-to-bottom layout (`flowchart TB`) for this four-step chain, or the site-level scroll cue for wide figures recommended in the DFT review (`dft-and-fft` L2).
- Priority: minor
- Acceptance condition: at 360 px all four stages are visible, or a visible cue shows that the figure scrolls.

The page already uses the right representations: a process diagram for the modeling chain, comparison tables for methods, equation types and error sources, derivations with intermediate steps, scripts with real output, and a summary table. Dark mode: equations, code (token colors), tables and the Mermaid diagram are legible on mobile-dark tiles 1 to 4, 9 to 12 and 21 to 28. No further visual is needed.

## E. Technical and source findings

No technical or source errors found. `facts.json`: HTTP 200 on all three viewports, no horizontal page scroll at 360 px, 0 KaTeX errors, no broken images, no console errors, no overflowing elements reported, capture not truncated. The six references are in the house format and alphabetical; their imprint years were not re-verified in this review (the 13 October audit lists the same items as not re-fetched, except Strauss).

## F. Required changes

Mandatory:

- [ ] L1: split the Section 5.1 formulas so that the truncation-error terms are visible at 1280 and 360 px.

Optional:

- [ ] L2: split the five other displays that are cut at 360 px.
- [ ] L3: top-to-bottom layout for the Section 1.1 flowchart (or the site-level scroll cue).
- [ ] Section 5.1, "Rearranging the "+" expansion": both quotation marks render as closing marks (”+”) on the live page (desktop-light-11, mobile-light-21); write the opening mark explicitly.
- [ ] Section 6.2, output block: at 360 px the "observed order" column is behind the code scroll (mobile-light-29); acceptable as wide code output, and the prose restates the result.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
| L3 | | | |
