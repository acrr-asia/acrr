# Live review: Introduction to Control Systems

- URL: https://acrr.asia/blog/introduction-to-control-systems
- Source: `src/content/blog/introduction-to-control-systems.mdx` (Foundations of Control Systems, entry 1)
- Commit deployed: `1eb85d4`
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/39980397404 (2026-10-23 15:43 UTC): 14 desktop-light, 25 mobile-light, 25 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-23. The reviewer did not write or revise this article.
- Risk: routine (a technical explainer; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Accept with minor follow-up. The page delivers its contract, every number on it was reproduced in this review and no finding is critical or major. Three minor presentation findings at 360 px remain open (L1 to L3); L3 comes from site-wide figure styling.

**Library decision: retain.** This is the foundation entry of the control series and the most linked-to control page on the site: entries 2 to 5, What Is a Robot?, the Sensor Systems first entry (Section 4), PID Control of Process Variables and From Signal Processing to Digital Control rely on its vocabulary (loop roles, transfer function, poles, step-response measures). The 13 October audit found it thin (no derivations, no Summary or References, undefined LTI); the wave 1 revision added all of that, and the live page now shows the derivations of both benchmark formulas and a table that tests the settling-time estimate. Its content does not need to change.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineering student or engineer who knows calculus, complex numbers and constant-coefficient linear ODEs and is starting control theory.
- Problem: acquiring the vocabulary and the performance measures that every later entry uses, and knowing where the textbook step-response formulas come from and when they hold.
- Outcome: name the parts of a feedback loop and the four requirements and why they trade off; define linear time-invariant systems, the Laplace transform, the transfer function, poles, zeros and steady-state gain; read a step response (final value, overshoot, 2% settling time); derive the second-order overshoot formula and see why $4/(\zeta\omega_n)$ is only an estimate.
- Distinctive contribution: both benchmark formulas derived on the page, the settling-time estimate tested against the exact response for four damping ratios, and a standard-library script that reproduces the numbers.
- Evidence: derivations in the text; one Python script with its quoted output; Åström and Murray (2021); Franklin, Powell and Emami-Naeini (2019); Ogata (2010).
- Limitations: second-order benchmark only; no frequency response, no controller design; limits of the measures stated qualitatively (extra poles and zeros, saturation, what a step does not show).

The benefit is delivered. Spot checks recomputed in this review: the ζ table (overshoot 37.2%, 16.3%, 4.6%, 0%; estimates 6.67, 4.00, 2.86, 2.00 s; exact 2% settling 5.62, 4.04, 2.99, 2.92 s, by scanning the analytic response at 1e-4 s); the minimum settling time 1.80 s at $\zeta = 0.78$, where the overshoot is 1.99%; $\ln 50 = 3.91$; poles $-1 \pm 1.732j$ and peak time 1.81 s; the script's printed output. Value density: Section 4.3 is the most valuable part of the page, since it turns two remembered formulas into reasoning a reader can check; Section 2 gives mechanisms for the gain trade-off instead of an assertion. No section is padding.

Overlap with other ACRR articles: the first-order time constant (63% and 98%) reappears in Measurement Systems and Sensor Characteristics (Section 4.1), with consistent numbers and a link to this series; step-response measures reappear in PID Control of Process Variables (Section 5, tuning) and pole-response reasoning in Stability and Eigenvalues. The overlap is short and linked; it is not duplication. Value category: conceptual understanding. Format: explainer.

## C. Substantive findings

None. The argument, the numbers and the references hold.

## D. Visual and structural findings

### L1. Display equations cut at 360 px

- Location: Section 3.3, the plant equation (mobile-light-09); Section 4.2, the pole pair and $\omega_d$ (mobile-light-14); the same tiles in dark mode.
- Problem: at 360 px both displays are wider than the column and their right end is hidden behind an unmarked sideways scroll: "$b > 0$" in 3.3, and in 4.2 the definition $\omega_d = \omega_n\sqrt{1 - \zeta^2}$ stops at "$\omega_n\sqrt{1-$".
- Why it matters: the 4.2 display is the only place $\omega_d$ is defined, and 4.3 and 4.4 use it; a phone reader who does not find the hidden scroll sees an incomplete definition.
- Required action: put the two parts of each display on separate lines (for example an `aligned` block or two displays), or a site-level scroll cue for wide equations.
- Priority: minor
- Acceptance condition: on new 360 px captures both displays are fully visible, or a visible cue shows that they scroll.

### L2. Settling-time table: comparison column hidden at 360 px

- Location: Section 4.3, the table of ζ, overshoot, estimate and exact settling time (mobile-light-16).
- Problem: at 360 px only the first three columns are visible; the fourth, "2% settling time from the response", sits beyond the scroll shadow.
- Why it matters: the table exists to compare the estimate with the exact value; without the fourth column the phone reader sees only the estimate, which the section says is poor at the extremes.
- Required action: shorten the headers (for example "ζ", "Overshoot", "Estimate (s)", "Exact (s)", with $\omega_n = 2$ rad/s stated in the sentence before the table) so that all four columns fit at 360 px.
- Priority: minor
- Acceptance condition: on new 360 px captures all four columns of the table, headers included, are visible without scrolling.

### L3. Both figures clipped at 360 px

- Location: Section 1.2 closed-loop diagram (mobile-light-05) and Section 4.2 step-response plot (mobile-light-14, 15); the same tiles in dark mode.
- Problem: the generated figures keep a 26rem minimum width (`.diagram-svg` in `prose.css`), so at 360 px their right part is hidden: in the loop diagram the "Plant" block is cut and the disturbance label, the output $y$ and the feedback take-off point are off-screen; in the plot the time axis stops at 4 s and the "±2% band" label and the settled tail are hidden.
- Why it matters: the output and the disturbance are two of the loop roles the section defines; the hidden tail of the plot is where the settling time is read.
- Required action: a site-level scroll cue for wide figures, or a lower minimum width for these two figures (both are legible at about 330 px).
- Priority: minor (site-wide behavior of generated diagrams, also recorded on Feedback and System Behavior)
- Acceptance condition: at 360 px both figures are shown whole, or a visible cue shows that they scroll.

Dark mode: both figures, the tables and the code blocks render correctly (mobile-dark-05, 14, 16, 18).

## E. Technical and source findings

None. `facts.json`: HTTP 200 on all three viewports, no horizontal page scroll, no overflowing elements, 0 KaTeX errors, 0 broken images, 0 console errors. The three textbook references are standard and support the material; chapter and page were not checked in this review.

## F. Required changes

Mandatory: none.

Optional:

- [ ] L1: split the two displays for narrow screens.
- [ ] L2: shorten the Section 4.3 table headers.
- [ ] L3: scroll cue or smaller minimum width for generated figures (site-level).
- [ ] Section 3.4, desktop-light-06: "one for each pole $p$, and each" breaks before the comma at 1280 px, so a line starts with ", and"; keeping the comma inside the math or rewording ("one term for each pole $p$; each such term") avoids it.
- [ ] Figure 2 caption: "ωn" is plain text without the subscript; "ω<sub>n</sub>" or "natural frequency 2 rad/s" reads better.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
| L3 | | | |
