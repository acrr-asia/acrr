# Live review: Stability and Eigenvalues

- URL: https://acrr.asia/blog/stability-and-eigenvalues
- Source: `src/content/blog/stability-and-eigenvalues.mdx` (Foundations of Control Systems, entry 4 of 5)
- Commit deployed: `7e20c2c` (master after PR #57); the source is unchanged since `60c0823` (wave 2 resolution of 13 October)
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40085671258 (2026-10-24 10:26 UTC): 18 desktop-light, 33 mobile-light, 33 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-24. The reviewer did not write or revise this article.
- Risk: routine (a technical explainer; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Request revision. At 1280 px the page is complete and correct. At 360 px most of its two-part display equations are cut at the right edge, including the transfer-function formula of Section 6 and the Euler step-size condition of Section 7, which an exercise depends on (L1, major). One minor finding on code output.

**Library decision: retain.** The page is the series' (and the site's) only full treatment of why eigenvalues decide stability: the modal decomposition, the map from eigenvalues to $\omega_n$ and $\zeta$, marginal and repeated cases, non-normal transient growth, hidden modes and the controllability and observability that explain them, the discrete-time and Euler conditions, and Lyapunov's indirect method. Each section answers part of the question the title asks, and the transient-growth and hidden-mode sections are the "where it stops being enough" that the description promises. Other pages that touch eigenvalue stability (the primer, the numerical-integration notes, the z-transform entry) refer to this one rather than repeating it. Only presentation needs fixing.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: a student or engineer who has the state-space form $\dot{x} = Ax + Bu$ from the primer and basic linear algebra, and is about to design a controller.
- Problem: why the eigenvalues of $A$ decide whether a linear system decays, oscillates or grows, what else they say about the response, and when they are not enough.
- Outcome: write the free response as a sum of modes; read decay rate, frequency, $\omega_n$ and $\zeta$ from an eigenvalue; classify marginal and repeated cases; recognize transient growth and hidden unstable modes; apply the unit-circle test and the Euler step-size condition; judge local stability of a nonlinear equilibrium from its Jacobian.
- Distinctive contribution: one running example (the primer's mass-spring-damper) through modes, damping, transfer function and discrete time, with numerical checks, plus three short counterexamples (double integrator, non-normal matrix, hidden mode) that show the limits of the eigenvalue test.
- Evidence: derivations in the text; three NumPy scripts with their output; Åström and Murray (2021), Chen (2013), Franklin, Powell and Emami-Naeini (2019), Khalil (2002), Trefethen and Embree (2005).
- Limitations: the modal proof assumes a diagonalizable matrix (the Jordan case is stated, not proved); Lyapunov's direct method, pseudospectra and formal controllability and observability tests are not covered (the controllability test is in the next entry).

The benefit is delivered. The opening states what is proved here and what came before; the sections build in order; the summary table is a usable reference and the closing paragraph hands over to state feedback. Checked for this review: all three scripts re-run, output identical to the comments (eigenvalues $-0.25 \pm 1.98431348j$, $[-0.223098, -1.43759169]$ by both methods, 2.513 at 0.683 s, the pendulum eigenvalues); overshoot $67.3\%$ for $\zeta = 0.125$; $\mu = 0.956 \pm 0.192j$ with magnitude 0.975 at $T = 0.1$ s; Euler factor magnitudes 0.995 and 1.32; Euler bound 0.125 s; exercise answers ($c = 2.8$ N·s/m, $-1.4 \pm 1.428j$; $T < 0.59$ s; $x_1 \to x_1(0) + x_2(0)$). No section is padding and nothing is repeated beyond the summary. Value category: conceptual understanding. Format: explainer.

Overlap noticed: [A Primer on State-Space Models](/blog/state-space-models-primer) states the eigenvalue test and proves one direction (planned progression; linked). [Notes on numerical integration](/blog/numerical-integration-notes) treats the Euler stability region in more depth (linked). [The z-Transform, Poles and Stability](/blog/z-transform-poles-and-stability) gives the unit-circle test and the map $z = e^{sT_s}$ for difference equations (shown under Related articles, not linked in Section 7). [Signals and Systems in Discrete Time](/blog/signals-and-systems-in-discrete-time) defines BIBO stability for discrete-time systems. These are complementary; no duplication.

## C. Substantive findings

None. The argument is complete and correct.

## D. Visual and structural findings

### L1. Key equations cut off at 360 px

- Location (360 px): Section 2, the modal sum (loses "$z(0) = V^{-1}x(0)$") and the matrix exponential (loses "$e^{At} = V \operatorname{diag}(\dots)V^{-1}$" after "$V \operatorname{diag}($"), mobile-light-06; Section 3, "$\zeta = c/(2\sqrt{mk}) = 0.125$", mobile-light-10; Section 6, "$G(s) = C(sI - A)^{-1}B + D$" ends at "$C\,($", the mass-spring-damper transfer function loses its denominator, and the hidden-mode example loses $C$ and $D$, mobile-light-18 and 19; Section 7, "$A_d = e^{AT}$" and the Euler condition "$\Longleftrightarrow T < 2\sigma/|\lambda|^2$", mobile-light-22 and 23; Section 8, $J_{\text{up}}$, mobile-light-25.
- Problem: each of these displays puts two results side by side and is wider than a phone screen; the second result is hidden behind a sideways scroll that nothing on the page signals. At 1280 px all of them fit.
- Why it matters: the hidden halves include the central formula of Section 6, the output matrix of the hidden-mode example that Exercise 5 asks about, and the Euler bound that Exercise 4 asks the reader to use. A phone reader sees incomplete results at exactly the points where the argument depends on them.
- Required action: put each pair on separate lines (an `aligned` or `gathered` block, or two displays): the modal sum and $z(0)$; $x(t) = e^{At}x(0)$ and the modal $e^{At}$; $\omega_n$ and $\zeta$; $Y(s) = G(s)U(s)$ and $G(s) = C(sI - A)^{-1}B + D$; the two forms of the mass-spring-damper $G(s)$; $A, B$ and $C, D$ of the hidden-mode example; the discrete model and $A_d$; the two sides of the Euler condition; $J_{\text{down}}$ and $J_{\text{up}}$.
- Priority: major
- Acceptance condition: on new 360 px captures none of the listed equations is cut, in light and dark mode; the 1280 px layout is unchanged or better.

### L2. Code output given only as end-of-line comments

- Location: Sections 2, 5 and 8, the three scripts (desktop-light-14, mobile-light-08 and 25).
- Problem: the printed results are trailing comments on long lines. At 360 px all of them are hidden behind the code box's scroll, so "The two results agree to all printed digits" cannot be checked without scrolling; at 1280 px the first pendulum comment loses its closing bracket.
- Why it matters: small; the key values are repeated in the prose, but the agreement the text points to is not visible on a phone.
- Required action: optional; show the output in a separate output block after each script, as other ACRR articles do (for example the DFT and PID entries).
- Priority: minor
- Acceptance condition: the printed output of each script is readable at 360 px without scrolling sideways, or the finding is accepted as a limitation of commented output.

Site-level items affecting this page (not raised separately): at 360 px the 7rem minimum cell width pushes the "Behavior" column of the Section 3 table partly off-screen (mobile-light-11); at 1280 px an inline equation wraps away from its opening parenthesis in Section 4 ("Remove the damper from the example (" then "$c = 0$)"). Dark mode renders the equations, table and code correctly (mobile-dark-11, 18).

## E. Technical and source findings

No technical or source errors found (Section B lists what was recomputed). The references are complete in the house format. KaTeX rendered without errors, no broken images, no console errors, no page-level horizontal scroll at 360 px (`facts.json`).

## F. Required changes

Mandatory:

- [ ] L1: split the side-by-side display equations listed in L1 so that each fits at 360 px.

Optional:

- [ ] L2: output blocks for the three scripts.
- [ ] Section 7: link [The z-Transform, Poles and Stability](/blog/z-transform-poles-and-stability) where the unit-circle test is introduced, for readers coming from the signal-processing side.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
