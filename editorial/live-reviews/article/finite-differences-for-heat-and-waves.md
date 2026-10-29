# Live review: Finite Differences for Heat and Waves

- URL: https://acrr.asia/blog/finite-differences-for-heat-and-waves
- Source: `src/content/blog/finite-differences-for-heat-and-waves.mdx` (Numerical Simulation for Engineers, entry 2 of 5)
- Commit deployed: `7e20c2c`; the source is unchanged between that commit and the reviewed branch
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40129647345 (2026-10-24 20:29 UTC): 21 desktop-light, 37 mobile-light, 37 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-24. The reviewer did not write or revise this article.
- Risk: routine (a technical explainer; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Request revision. One major presentation finding (L1): four display equations are cut at 1280 px, two of which hide the result of their subsection (the FTCS truncation error in Section 2.1 and the tridiagonal form of BTCS in Section 3.1). The rest are minor.

**Library decision: retain and update.** The page is the only ACRR treatment of time stepping for PDEs: explicit, implicit and Crank–Nicolson schemes, von Neumann stability, the Lax equivalence theorem and the CFL condition. Later entries (3 and 5) and two pages outside the series (`numerical-integration-notes`, `distributed-memory-and-message-passing`) link into its sections. The content is accurate and every script reproduces. The update is presentational (L1 to L3); no section needs rewriting, merging or moving.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineer or student who has read entry 1 (or knows finite-difference truncation error) and has to choose a time step and a scheme for a heat or wave simulation.
- Problem: why an explicit scheme blows up when the step is a few percent too large, why implicit schemes do not, and how to choose among FTCS, BTCS, Crank–Nicolson and leapfrog.
- Outcome: derive the amplification factor of a scheme; state and apply the limits mu <= 1/2 and nu <= 1; explain stiffness, Crank–Nicolson's undamped oscillation and numerical dispersion; check a scheme's order by a refinement study.
- Distinctive contribution: each stability limit and order is shown by a short experiment that reproduces it (the 4% step increase that turns 2.9×10⁻³ into 10², the measured orders, the Crank–Nicolson sign flip, divergence under refinement at nu = 1.05), plus a worked example in physical units and a decision table.
- Evidence: derivations in the text; four scripts with their real output; Courant, Friedrichs and Lewy (1928), Crank and Nicolson (1947), Lax and Richtmyer (1956), LeVeque, Morton and Mayers, Strikwerda.
- Limitations: one-dimensional model problems with Dirichlet ends; two dimensions only as stated limits; nonlinear problems, other boundary conditions and higher-order schemes out of scope.

The contract is delivered. The opening states the question (stability, not accuracy, limits the step) and the prerequisites; Sections 1 to 4 develop the heat equation from stiffness to Crank–Nicolson; Section 5 names the theorem the experiments illustrate; Section 6 repeats the pattern for waves; Section 7 turns it into a choice; the summary answers the page's questions in one screen. Every major section serves the central question and nothing is repeated beyond short back-references. The verification aside in Section 6.3 (t = 2.5 versus t = 1) is a useful bridge to entry 5. Checked by computation for this review: all four scripts re-run with Python 3 and NumPy (output identical, line for line); the factor −1.0274 at xi = 19π/20 and its growth 4.1×10⁴ over 392 steps; the 2% agreement of the stable run (2.869×10⁻³ against 2.915×10⁻³); the Crank–Nicolson/BTCS error ratio on the finest grid (106); 0.9607¹⁰ = 0.67 ("by only a third"); Exercises 1 and 4. The page is worth its 23 minutes. Value category: conceptual understanding. Format: explainer.

What is missing: no figure. A plot of the stable and unstable FTCS runs of Section 2.2, or of |G(xi)| for the three heat schemes, would show at a glance what the text describes (optional, standards 6.8).

Overlap noticed (none is duplication; all are linked):

- `numerical-integration-notes`: stiffness and the stability regions of explicit Euler, backward Euler and the trapezoidal rule; this page applies them to the semi-discrete heat equation and both pages link each other.
- `from-differential-equations-to-discrete-problems` (entry 1): the method of lines and the consistency/stability/convergence vocabulary, referenced, not repeated.
- `distributed-memory-and-message-passing` (Parallel and High-Performance Computing): reuses the FTCS stability analysis in two dimensions for its Jacobi example and links Sections 2.1 and 2.2. For the overlap map: "measuring an observed order" appears here, in entry 1, in entry 5 and in the numerical-integration notes.

## C. Substantive findings

None. No technical or factual error was found on the page.

## D. Visual and structural findings

### L1. Display equations cut at desktop width, hiding two subsection results

- Location: Section 2.1, the truncation-error display after "as in Section 5.1 of the first entry, gives" (desktop-light-04); Section 3.1, the BTCS display (desktop-light-07); Section 1.1, the model problem (desktop-light-02); Section 4.1, the θ-scheme with the definition of δ² (desktop-light-08). At 360 px also Section 2.2, the amplification factor (mobile-light-08), Section 2.1, the FTCS update (mobile-light-07), and Section 6.1, the leapfrog update (mobile-light-21).
- Problem: at 1280 px these displays are wider than the text column and scroll sideways without a cue. In Section 2.1 the whole right-hand side, "= (Δt/2)u_tt − (αΔx²/12)u_xxxx + ...", is hidden; the reader sees only the definition of τ. In Section 3.1 the equivalent tridiagonal form "−μU_{j−1} + (1+2μ)U_j − μU_{j+1} = U_j^n" is cut after "(1 + 2μ". The model problem loses its initial condition and the θ-scheme its definition of δ². At 360 px the amplification factor ends at "= 1 −", hiding "4μ sin²(ξ/2)", the result Section 2.2 derives.
- Why it matters: the truncation-error terms are what the "first order in time, second order in space" statement and the Crank–Nicolson argument of Section 4.1 rest on, and the tridiagonal form is the linear system the section says each step must solve. A reader who does not discover the hidden scroll reads the formulas incomplete at the point the argument uses them.
- Required action: break each display over lines (an `aligned` or `gathered` block): the truncation error with its expansion on a second line; the BTCS difference form and its tridiagonal form one per line; the model problem with its boundary and initial conditions on a second line; the θ-scheme and the δ² definition as two lines. At 360 px, split the amplification factor after the first equals sign and the FTCS and leapfrog updates before the "+ μ" and "+ ν²" terms.
- Priority: major
- Acceptance condition: on new captures, the four displays are fully visible without sideways scrolling at 1280 px, and at 360 px the Section 2.1 truncation terms, the Section 2.2 result "1 − 4μ sin²(ξ/2)" and the Section 3.1 tridiagonal form are visible without scrolling.

### L2. Section 7 table: the "Use when" column is hidden at desktop width

- Location: Section 7, "Choosing a scheme" (desktop-light-16, desktop-light-17; at 360 px mobile-light-28 to 29).
- Problem: the six-column table is wider than the text column (site-wide 7rem minimum cell width), and the last column, "Use when", sits under the scroll shadow at 1280 px with its entries cut mid-word ("Fine tim... resoluti..."). At 360 px only three columns are visible.
- Why it matters: "Use when" is the recommendation the section exists to give; the other columns are its inputs.
- Required action: reduce the table to five columns (for example, merge "Equation" into "Scheme" as "FTCS (heat, explicit)"), or move "Use when" to second position, so that the recommendation is visible at 1280 px without scrolling.
- Priority: minor
- Acceptance condition: at 1280 px the "Use when" entries are fully visible.

The scroll cue for wide display equations at 360 px is a known site-level issue and is not raised again here.

## E. Technical and source findings

### L3. Output lines cut in Sections 4.2 and 4.3

- Location: Section 4.2 output block (desktop-light-09) and Section 4.3 output block (desktop-light-11).
- Problem: at 1280 px the observed orders of Section 4.2 show only their first value ("observed order in dx: 2.00", "0.88", "2.03"), and in Section 4.3 the step-10 values are hidden.
- Why it matters: small; the bullets after Section 4.2 restate the orders, and the step-10 behavior is described in the prose.
- Required action: optional; shorter labels in the `print` calls (for example "expl", "impl", "CN" and "order:") would let the lines fit. Changing the code means re-running it.
- Priority: minor
- Acceptance condition: both output blocks fully visible at 1280 px, or the finding is accepted as a limitation of wide code output.

No technical or source errors found. `facts.json`: HTTP 200 on all three viewports, no horizontal page scroll at 360 px, 0 KaTeX errors, no broken images, no console errors, no overflowing elements, capture not truncated. Dark mode: equations, code token colors and both tables are legible on mobile-dark tiles 9 to 12, 17 to 20 and 29 to 32. The six references are in the house format and alphabetical; imprint years were not re-verified in this review.

## F. Required changes

Mandatory:

- [ ] L1: split the four displays cut at 1280 px, and the Section 2.2 result at 360 px.

Optional:

- [ ] L2: make the "Use when" column of Section 7 visible at 1280 px.
- [ ] L3: shorter output labels in the Sections 4.2 and 4.3 scripts.
- [ ] Section 2.2, last paragraph: "the shortest grid mode (ξ = 19π/20)" breaks after the opening parenthesis on desktop (desktop-light-06); a comma construction ("the shortest grid mode, ξ = 19π/20,") avoids the orphaned bracket.
- [ ] A figure of the stable and unstable FTCS runs, or of |G(ξ)| for the three heat schemes.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
| L3 | | | |
