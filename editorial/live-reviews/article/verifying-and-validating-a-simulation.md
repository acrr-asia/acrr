# Live review: Verifying and Validating a Simulation

- URL: https://acrr.asia/blog/verifying-and-validating-a-simulation
- Source: `src/content/blog/verifying-and-validating-a-simulation.mdx` (Numerical Simulation for Engineers, entry 5 of 5)
- Commit deployed: `7e20c2c`; the source is unchanged between that commit and the reviewed branch
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40129647345 (2026-10-24 20:29 UTC): 21 desktop-light, 39 mobile-light, 39 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-25. The reviewer did not write or revise this article.
- Risk: routine (a technical explainer; the validation example uses invented values and says so twice; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Request revision. At 1280 px the page reads cleanly: every display, table, code block and output fits the column, and the Mermaid figure of Section 1.2 is complete. The one major finding (L1) is limited to 360 px: the Richardson extrapolation formula of Section 3.1, the result that names the section, is off the right edge, and the conservative scheme of Section 2.3 is cut mid-numerator. The rest is minor.

**Library decision: retain and update.** The page is ACRR's only treatment of verification and validation as procedures: the V&V vocabulary of ASME and AIAA, code verification by observed order and manufactured solutions (with a planted bug the observed order exposes), solution verification by Richardson extrapolation and the GCI on a problem with a known answer, and a validation comparison in the V&V 20 form with GUM uncertainty propagation. It closes the series, and the insight `what-makes-a-simulation-trustworthy` states in brief what this page turns into method. The content is accurate; the update is a small presentational fix at 360 px (L1, L2), and no section needs rewriting, merging or moving.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineer or student who can build and solve a discretization (entries 1 to 4) and must now say how far a simulation result can be trusted.
- Problem: how to show that a code solves its equations correctly, how large the numerical error of one result is when no exact solution exists, and what a comparison with a measurement does and does not prove about the model.
- Outcome: run an observed-order test with a manufactured solution; compute the observed order, the Richardson extrapolate and the GCI from three grids, with the asymptotic-range check; form E = S − D and u_val and read the interval E ± 2u_val; list what a simulation report must state.
- Distinctive contribution: each procedure demonstrated by a script on the series' own problems, including a plausible indexing bug that still converges (order 1.08 to 1.02 instead of 2.00), a GCI tested against a Fourier-series reference, and a validation example in which input uncertainty, not the solver, limits what can be concluded.
- Evidence: three scripts with their real output; AIAA G-077-1998; ASME V&V 10-2006 and V&V 20-2009; JCGM 100:2008 and 101:2008; Oberkampf and Roy; Richardson (1911); Roache (1994, 1998).
- Limitations: steady, scalar quantities of interest on smooth problems; the validation case is hypothetical; model-form uncertainty and validation hierarchies are described, not computed.

The contract is delivered. Section 1 fixes the vocabulary and the order (verification before validation); Section 2 gives code verification; Section 3 solution verification; Section 4 validation; Section 5 turns the three into a reporting checklist and states the extrapolation limit plainly; the summary table answers the page's questions. Every major section serves the central question, and the warnings (a converging code is not verified; calibration data cannot also validate) are the page's strongest teaching. Checked by computation for this review: all three scripts re-run with Python 3 and NumPy (output identical: orders 2.00 and 1.08, 1.04, 1.02; p = 1.993, extrapolate 0.0736714, GCI 0.0242%, ratio 1.0006, actual error 0.0192%; S = 59.28 °C, u_num = 0.010 K, u_input = 1.43 K, E = −1.72 K, u_val = 1.52 K, interval [−4.75, 1.31] K); the manufactured source f; the series truncation claim (4001 against 2001 terms differ by 1.4×10⁻¹¹); 3% and 2% of the 39.3 K rise (1.18 K, 0.79 K); Exercises 1, 2 and 4. The page is worth its 24 minutes. Value category: practical implementation (procedures a reader can apply to their own code). Format: explainer.

Overlap noticed (none is duplication; all are linked):

- Insight `what-makes-a-simulation-trustworthy`: the verification/validation distinction in brief, with open questions; this page is its method counterpart and cites its open questions in Section 5.
- Insight `floating-point-in-long-simulations`: round-off, cited in Section 3.4.
- `measurement-systems-and-sensor-characteristics` (Sensor Systems), Section 5.2: GUM standard uncertainty and coverage factor; Section 4.2 here reuses the convention and links it. For the overlap map: "GUM uncertainty propagation" is explained in both, from the measurement side there and the simulation side here.
- `from-differential-equations-to-discrete-problems` (entry 1): the error taxonomy and the one-sided boundary example reused by name.
- Insight `closing-the-sim-to-real-gap` links here; different subject (robot learning transfer), no shared explanation.

## C. Substantive findings

None. No technical or factual error was found on the page.

## D. Visual and structural findings

### L1. Richardson extrapolation and the Section 2.3 scheme hidden at 360 px

- Location: Section 3.1, the display after "after L. F. Richardson's 1911 paper" (mobile-light-14); Section 2.3, the conservative finite-difference scheme (mobile-light-10).
- Problem: at 360 px the Section 3.1 display shows the observed-order formula p = ln((f₃ − f₂)/(f₂ − f₁))/ln r and then a lone "f" at the right edge; the Richardson extrapolate f_exact ≈ f₁ + (f₁ − f₂)/(rᵖ − 1) is off-screen with no cue. In Section 2.3 the scheme is cut after "k_{j−1/2}(U_j −", so the term in which the planted bug sits is incomplete. At 1280 px both displays are complete on the desktop tiles.
- Why it matters: the extrapolate is the result Section 3.1 is named after and that the GCI and the Section 3.3 study ("the extrapolated value agrees with the series to all seven digits") depend on; a phone reader is never shown the formula. The scheme is the object of the code-verification demonstration.
- Required action: set the Section 3.1 pair as two displays (or an `aligned` block with one formula per line); break the Section 2.3 fraction, for example by writing the numerator as two terms over h² on two lines or as the flux-difference form −(F_{j+1/2} − F_{j−1/2})/h with F defined on the next line.
- Priority: major
- Acceptance condition: on new 360 px captures, the Richardson extrapolation formula and the full Section 2.3 scheme are visible without sideways scrolling, and the 1280 px layout is unchanged.

The site-level issues are present and not raised again: no scroll cue for wide displays and for the Section 1.2 Mermaid figure at 360 px (the "Computational model" box is cut, mobile-light-07), and the Section 1.1 activity table scrolls at 360 px (7rem minimum cell width). `facts.json` reports one SVG figure without a title, as every page with a diagram in this capture run does (site-level property of the Mermaid output).

## E. Technical and source findings

### L2. Outputs and a secondary display cut at 360 px

- Location: Section 2.3 output (mobile-light-12), Section 3.3 output (mobile-light-17), Section 4.4 output (mobile-light-26); Section 4.4 display of S (mobile-light-25).
- Problem: at 360 px the observed-order column of the Section 2.3 output, the extrapolate and GCI lines of Section 3.3 and the u_input and interval values of Section 4.4 sit beyond the code box edge; the S display hides "φ_h = 0.0736572 (the N = 64 value)".
- Why it matters: small; code blocks scroll, and the prose restates each value (1 instead of 2, 1.993 and 0.024%, 1.52 K and [−4.75, 1.31] K; φ is also in the code).
- Required action: optional; put φ_h on its own line in the Section 4.4 display; shorter output labels would reduce the code-box scrolling. Changing the code means re-running it.
- Priority: minor
- Acceptance condition: φ_h visible at 360 px, or the finding is accepted as a limitation of code output at phone width.

No technical or source errors found. `facts.json`: HTTP 200 on all three viewports, no horizontal page scroll at 360 px, 0 KaTeX errors, no broken images, no console errors, no overflowing elements, capture not truncated. Dark mode: equations, code, the tables and the Mermaid figure are legible on mobile-dark tiles 5 to 12 and 25 to 28. The nine references are in the house format; imprint years were not re-verified in this review.

## F. Required changes

Mandatory:

- [ ] L1: the Richardson extrapolate and the Section 2.3 scheme visible at 360 px.

Optional:

- [ ] L2: φ_h on its own line in Section 4.4; shorter output labels.
- [ ] Section 3.3: at 360 px the Fourier series sits on its own line after a stranded "u =" and is followed by a line starting with a comma (mobile-light-16); a display equation would read better. Likewise "E = 0" followed by a line-initial period (mobile-light-28) and "E" followed by ", with standard uncertainty" (mobile-light-23).

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
