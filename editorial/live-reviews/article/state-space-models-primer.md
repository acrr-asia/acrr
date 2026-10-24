# Live review: A Primer on State-Space Models

- URL: https://acrr.asia/blog/state-space-models-primer
- Source: `src/content/blog/state-space-models-primer.mdx` (Foundations of Control Systems, entry 3 of 5)
- Commit deployed: `1eb85d4` (master after PR #53); the source and its two diagram components are unchanged between that commit and the reviewed branch
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/39980397404 (2026-10-23 15:43 UTC): 11 desktop-light, 20 mobile-light, 20 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-23. The reviewer did not write or revise this article.
- Risk: routine (a technical explainer; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Accept with follow-up. The contract is delivered and the page renders correctly at 1280 px in light mode and at 360 px in dark mode; the two findings (L1, L2) are minor rendering defects at 360 px.

**Library decision: retain.** The page introduces the $(A, B, C, D)$ notation, the state concept and the eigenvalue test that entries 4 and 5 of its series and the numerical-simulation and numerical-integration pages build on. The wave 1 revision of 13 October added what the audit found missing (definition of state, the input-output link, coordinate invariance, assumptions, summary and references), and the page is now a short, complete bridge between the first entry's transfer functions and the fourth entry's modal analysis. Nothing else on ACRR does that job, and its length (9 minutes) is right for it.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: a student or engineer who has met transfer functions and poles (this series' first two entries) and needs the state-space form before modal analysis and state feedback.
- Problem: what a state is, how to write a physical system as $\dot{x} = Ax + Bu$, $y = Cx + Du$, and how this form relates to the transfer function and to stability.
- Outcome: write a mass-spring-damper in state-space form; read the sizes and roles of $A, B, C, D$; explain why eigenvalues do not depend on the choice of state; state and half-prove the eigenvalue test; derive $G(s)$ for the example and see that its poles are the eigenvalues.
- Distinctive contribution: one worked example carried through every representation (ODE, state equations, characteristic polynomial, eigenvalues by code and in a figure, transfer function), with the limits of the linear time-invariant model stated.
- Evidence: derivations in the text; one NumPy check; Åström and Murray (2021), Chen (2013), Franklin, Powell and Emami-Naeini (2019).
- Limitations: second-order mechanical example only; the general $C(sI - A)^{-1}B + D$, the other half of the eigenvalue proof and hidden modes are deferred to the fourth entry (which was checked to contain them: `stability-and-eigenvalues`, Sections 2 and 6, and its pendulum linearization in Section 8).

The contract is delivered. The opening states what the entry builds on, what it covers and its conventions; Section 1 motivates the state before using it; Sections 2 to 5 follow one example; Section 6 states the assumptions; the summary table is a usable reference. Checked by computation for this review: eigenvalues $-0.25 \pm 1.98431j$ for $m = 1$, $c = 0.5$, $k = 4$ ($\sqrt{15.75}/2$); $G(0) = 1/k = 0.25$ m/N; $G(s) = (1/k)\,\omega_n^2/(s^2 + 2\zeta\omega_n s + \omega_n^2)$ with $\omega_n^2 = k/m$, so "up to the factor $1/k$" is right; the determinant identity for $T A T^{-1}$. No section is padding and nothing is repeated beyond the summary. Value category: conceptual understanding. Format: explainer.

Overlap noticed: the eigenvalue test is stated here and proved in `stability-and-eigenvalues`, and the second-order benchmark of `introduction-to-control-systems` Section 4.2 is the same system; this is planned progression and each page links the others. `from-differential-equations-to-discrete-problems` (Section 4.3) and `numerical-integration-notes` (Section 4) send readers here for $\dot{x} = Ax$. For the site-level overlap map: "eigenvalues of A decide stability" appears in this page, `stability-and-eigenvalues`, `numerical-integration-notes` and `z-transform-poles-and-stability` (discrete time); only the second explains it in depth.

## C. Substantive findings

None. No technical or factual error was found on the page.

## D. Visual and structural findings

### L1. Three display equations cut at 360 px

- Location: Section 2, the state equation (the output equation $y = [1\;\,0]\,x$ is hidden, mobile-light-05); Section 3, the coordinate change (ends at "$y = CT^-$", mobile-light-07); Section 5, the transfer function (ends at "$s^2 + 0.5\,s$", with "+ 4" and "for the example" hidden, mobile-light-12). Same in dark mode (mobile-dark-05, -07, -12).
- Problem: each display places two equations, or an equation and a remark, on one line that is wider than the 360 px column; the right part scrolls sideways without a cue.
- Why it matters: on a phone the output equation of the worked model, and the numerical transfer function of the example, are not visible where they are defined; the prose restates them only in part.
- Required action: split each display: state equation and output equation on separate lines; the two coordinate-change equations on separate lines; $G(s) = 1/(ms^2 + cs + k)$ and the numerical form on separate lines, with "for the example" moved into the sentence.
- Priority: minor
- Acceptance condition: at 360 px the three displays are fully visible without sideways scrolling.

### L2. Mass-spring-damper diagram: labels cut at 360 px

- Location: Section 2, the figure "The mass-spring-damper" (mobile-light-04, mobile-dark-04).
- Problem: the diagram keeps a minimum width wider than the phone column, so the labels "displacement q" and "force u" on its right edge are cut to "dis" and "fo".
- Why it matters: the two labels name the input and the output of the model the section builds; the caption names them too, so the loss is small.
- Required action: in `scripts/generate-diagrams.py`, shorten the labels to the symbols with their arrows ($q$, $u$) or move them inside the drawing so that they fit at 360 px; alternatively the site-level scroll cue for wide figures (see `dft-and-fft` L2).
- Priority: minor
- Acceptance condition: at 360 px both labels are fully visible, or a visible cue shows that the figure scrolls.

The eigenvalue plot is legible at 360 px and in dark mode (mobile-light-11, mobile-dark-11); its caption says what to notice. Tables and code are legible in both modes.

## E. Technical and source findings

No technical or source errors found. `facts.json`: HTTP 200 on all three viewports, no horizontal page scroll at 360 px, 0 KaTeX errors, no broken images, no console errors, no overflowing elements, capture not truncated. Reference details were not re-verified in this review.

## F. Required changes

Mandatory: none.

Optional:

- [ ] L1: split the three displays cut at 360 px.
- [ ] L2: diagram labels that fit at 360 px.
- [ ] Section 4.1 calls the same page "the next entry" in its first paragraph and "the fourth entry" in its second (and the summary returns to "next entry"); one name throughout would read more cleanly.
- [ ] Section 4.3, code: the trailing comment that gives the expected output is hidden behind the code scroll at 360 px (mobile-light-11); a separate printed-output block, as in other entries, would show it.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
