# Live review: Notes on Numerical Integration of ODEs

- URL: https://acrr.asia/blog/numerical-integration-notes
- Source: `src/content/blog/numerical-integration-notes.mdx` (standalone article; no series)
- Commit deployed: `1eb85d4`
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/39980397404 (2026-10-23 15:43 UTC): 11 desktop-light, 20 mobile-light, 20 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-23. The reviewer did not write or revise this article.
- Risk: routine (a technical explainer; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Accept with minor follow-up. The contract is delivered and the technical content is correct; the three findings are presentation polish at 360 px.

**Library decision: retain.** The 13 October audit decided to keep the note standalone because six articles in four series (two in Numerical Simulation, one in Foundations of Control Systems, two in Digital Signal Processing, one in Industrial Automation) and one insight link to it as the site's treatment of ODE time stepping and the explicit-Euler stability limit, rather than repeating it. That decision holds: the live page now has an opening with prerequisites, definitions and a derivation of order, a measured-order experiment, the stability regions, a limits section, a summary and references, and none of this is duplicated elsewhere on the site. A merge into the Numerical Simulation series would break that hub role for the control and DSP readers who arrive from outside the series.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineer or student who knows calculus and Taylor series and has an ODE to simulate, often arriving from a series entry that needs a time-stepping background.
- Problem: choosing a method and a step size, and understanding why a step that looks accurate enough can still make a simulation blow up.
- Outcome: state and measure the order of explicit Euler and classical RK4; compare them at equal cost; use the amplification factor and stability region to find the largest stable step for a mode $\lambda$; tell accuracy and stability apart; know when to turn to implicit methods.
- Distinctive contribution: one short page that keeps accuracy and stability apart on the test equation, with the order derived from the amplification factor, measured by a runnable script, compared at equal work, and the stability limits shown in a figure, including the imaginary axis for undamped oscillations; it is the common reference point for the site's simulation, control and DSP entries.
- Evidence: derivation on the test equation; a standard-library Python script with its output table; Butcher (2016), Hairer, Nørsett and Wanner (1993), LeVeque (2007).
- Limitations: fixed step only; linear analysis; stiffness and implicit methods left to the Numerical Simulation series; general nonlinear order proof left to the references.

The benefit is delivered. Each section answers one part of the question, and the Section 6 table and closing paragraph state the decision rule (smooth, non-stiff problems are limited by accuracy and favor RK4; fast-decaying modes are limited by stability and call for implicit methods). Recomputed in this review: $R(-2.5) = 0.6484$ and $0.6484^{20} = 1.73\times10^{-4}$; the RK4 real-axis boundary $-2.7853$ (bisection on $|R(z)| = 1$); $1.5^{20} \approx 3.3\times10^{3}$; $e^{-50} = 1.9\times10^{-22}$; the RK4 amplitude factors on the imaginary axis from $|R(jy)|^2 = 1 - y^6/72 + y^8/576$ (0.99391 at $y = 1$, 0.74536 at $y = 2$); the observed orders and the equal-work ratio from the table. The figure was checked against these numbers: the RK4 boundary meets the real axis at about $-2.79$ and the marked point sits at $-2.5$, outside the Euler disc. All correct.

Value density: high for its length (about 10 minutes); no section repeats another, and the blockquote in Section 4 is the one sentence a reader should keep. Value category: conceptual understanding. Format: explainer.

Overlap noticed: [Finite Differences for Heat and Waves](/blog/finite-differences-for-heat-and-waves) applies the same stability regions to the method-of-lines system, and [Stability and Eigenvalues](/blog/stability-and-eigenvalues) compares $e^{\lambda T}$ with Euler's $1 + \lambda T$. Both link here and this page links back to both, so the division of labor is explicit; this is the intended hub, not duplication.

## C. Substantive findings

None.

## D. Visual and structural findings

### L1. Stability-region figure: right edge hidden at 360 px

- Location: Section 4, the stability-region figure (mobile-light-11 and 12; mobile-dark-11 and 12).
- Problem: at 360 px the figure keeps a minimum width and is cut at the imaginary axis: the part of the RK4 region to the right of the axis (where the boundary crosses it at $\pm 2.83j$ and bulges slightly into the right half-plane) and the "Re $h\lambda$" axis label are off-screen, with no scroll cue.
- Why it matters: the paragraph after the figure is about the imaginary axis (undamped oscillations), which is the part a phone reader does not see.
- Required action: let this figure scale to the column at 360 px (it is a generated SVG, `scripts/generate-diagrams.py`; its labels remain readable at about 85 percent), or crop its plotted range so the imaginary axis and the right-hand bulge fit; alternatively the site-level scroll cue for wide figures.
- Priority: minor
- Acceptance condition: at 360 px the imaginary axis crossing of the RK4 boundary and the "Re $h\lambda$" label are visible, or a visible cue shows the figure scrolls.

### L2. RK4 update equation cut at 360 px

- Location: Section 1, the display equation $y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$ (mobile-light-04).
- Problem: at 360 px the equation ends at "$+ k_4$" with the closing parenthesis and period hidden behind a sideways scroll.
- Why it matters: small (only the last term is affected), but it is the definition of the method.
- Required action: set the weighted sum on its own line (for example $y_{n+1} = y_n + \tfrac{h}{6}\,k$ with $k = k_1 + 2k_2 + 2k_3 + k_4$ below, or an `aligned` split), or reduce it with `\tfrac` so it fits.
- Priority: minor
- Acceptance condition: at 360 px the whole equation is visible.

### L3. Punctuation after inline math

- Location: Section 2, the Taylor series sentence ("$z^5/120 + \dots$." reads as four dots, desktop-light-04, mobile-light-06); Section 2, first paragraph (the period after "does not depend on $h$" alone on a line, mobile-light-05) and second paragraph (the semicolon after "at fixed $T$" at the start of a line, mobile-light-06).
- Problem: an ellipsis followed by a sentence period, and punctuation after inline math that wraps on its own.
- Why it matters: polish.
- Required action: end the series with "$+ \cdots$" and start a new sentence without the extra period (or drop the ellipsis and write "and so on"); keep punctuation attached to the math (inside it, or joined by a word joiner). The site-level fix proposed in the live review of Inside a Microcontroller (L4 there) would also cover the wrapping.
- Priority: minor
- Acceptance condition: no four-dot ellipsis, and no line starting with a lone period or semicolon, on new captures at 1280 and 360 px.

The page uses the right representations: displayed method definitions, an error table, the stability-region figure with a caption that says what to notice, and a summary table. No further visual is needed.

## E. Technical and source findings

None. All numbers checked (Section B) are correct; the wave 2 technical points (bounded amplification in the order argument, the RK4 damping figures, the decay condition, the stiffness example) are correctly reflected on the live page. The three references are in house format. `facts.json`: HTTP 200 on all three viewports, one h1, no horizontal page scroll at 360 px, no overflowing page elements, 0 KaTeX errors, 0 broken images, 0 console errors, every SVG figure titled.

## F. Required changes

Mandatory:

- None.

Optional:

- [ ] L1: make the stability-region figure fit (or scroll visibly) at 360 px.
- [ ] L2: split the RK4 update equation for 360 px.
- [ ] L3: fix the ellipsis and keep punctuation attached to inline math.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
| L3 | | | |
