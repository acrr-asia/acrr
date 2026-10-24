# Live review: Designing a State-Feedback Controller

- URL: https://acrr.asia/blog/state-feedback-controller-design
- Source: `src/content/blog/state-feedback-controller-design.mdx` (Foundations of Control Systems, entry 5 of 5)
- Commit deployed: `7e20c2c` (master after PR #57); the source is unchanged since the wave 2 resolution of 13 October (`60c0823`)
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40085671258 (2026-10-24 10:26 UTC): 15 desktop-light, 27 mobile-light, 27 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-24. The reviewer did not write or revise this article.
- Risk: routine (a technical tutorial; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Request revision. The closed-loop characteristic polynomial, the result Section 1 derives and Section 3 designs against, is cut off at 1280 px, and at 360 px most of the design results are cut (L1, major). Two minor findings.

**Library decision: retain.** The page completes its series: it turns the eigenvalue analysis of entry 4 into a design method, works it through one plant with numbers a reader can check (gains, reference gain, integral action, observer gain), and gives as much space to what the design assumes (model, actuator, measurement, sampling) as to the method, which is what distinguishes it from a textbook recipe. No other ACRR page teaches pole placement or observers. Only presentation and one cross-link need work.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: a student or engineer who has followed the series to the eigenvalue test and wants to design a first state-space controller.
- Problem: how to choose feedback gains so that a plant's eigenvalues land where the specifications need them, how to make the output track a reference, and what such a design silently assumes.
- Outcome: write the closed loop $A - BK$; test controllability; translate overshoot and settling requirements into target eigenvalues; compute $K$ by matching coefficients or Ackermann's formula; compute a reference gain and know why integral action is more robust; know the roles of actuator limits, observers, noise, sampling and LQR.
- Distinctive contribution: one plant (the series' mass-spring-damper) carried from specification to gains, reference gain, integral action and observer, with simulated results and a table that shows the force cost of faster eigenvalues, and a closing account of what the whole series has covered against its objectives.
- Evidence: derivations in the text; one NumPy script with its output; simulations reported in two tables and the text; Ackermann (1972), Åström and Murray (2021), Chen (2013), Franklin, Powell and Emami-Naeini (2019), Ogata (2010).
- Limitations: single-input systems only; LQR and Kalman filtering are named, not developed; discrete-time design is pointed to, not done.

The benefit is delivered. The opening states the problem and the target (settle within about 1.5 s with little overshoot); each section adds one step; Section 6 is a substantial list of assumptions, each with a number from the example. Checked for this review: the Ackermann script re-run, output identical (`[[12. 5.1]]`, $-2.8 \pm 2.85657137j$); an independent explicit Euler simulation (0.1 ms step) reproduces every simulated figure on the page: open loop 67.3% and 14.7 s, state feedback 4.6% and 1.49 s, integral design peaks 1.015 m and 1.006 m, settling 1.2 s, 0.9 m reached at 1.0 s against 0.66 s, and the $\omega_n = 8$ design settling in 0.75 s, 0.90 s with a 10 N limit. Also checked: the table gains for $\omega_n = 2$ and 8, the observer gain $L = [19.5 \;\; 86.25]^\top$, the 5.9% offset, and the four exercise answers. Value category: practical implementation. Format: tutorial.

The closing three paragraphs of the summary restate the series twice (once as a line of thought, once against the objectives); they serve a reader who arrives at the end of the series, but could be one paragraph (optional, F).

Overlap noticed: integral action and integrator windup also appear in [PID Control of Process Variables](/blog/pid-control-of-process-variables) (Industrial Automation) and [From Signal Processing to Digital Control](/blog/from-signal-processing-to-digital-control) (Digital Signal Processing); the second also quantifies the sample-and-hold delay that Section 6.4 mentions and links to Section 6.4, but this page does not link back (L2). The Kalman filter is linked to [Sensing and State Estimation](/blog/sensing-and-state-estimation). Complementary treatments; no duplication.

## C. Substantive findings

None. The method, numbers and assumptions are correct.

## D. Visual and structural findings

### L1. Design equations cut off

- Location: Section 1, the display "$A - BK = \dots$, $\det(sI - (A - BK)) = s^2 + (0.5 + k_2)s + (4 + k_1)$" (desktop-light-03: ends at "$= s^2$ -"; mobile-light-04: the determinant is not visible at all). At 360 px also: the opening display loses $C$ and $D$ of the plant (mobile-light-02); Section 2 loses "$\det\mathcal{C} = -1 \neq 0$" (mobile-light-06); Section 3 loses "$+ 16$" of the desired polynomial and "$k_2 = 5.1$ N·s/m" (mobile-light-08); Section 4 loses the definition of $\varphi(A)$ (mobile-light-09); Section 5.3 loses $k_I = 64$ (mobile-light-13).
- Problem: the side-by-side displays are wider than the text column; the second half is hidden behind a sideways scroll that nothing on the page signals.
- Why it matters: the closed-loop polynomial is the bridge from the feedback law to the design; at the point it is derived, a desktop reader sees "$s^2$ -" and nothing more. On a phone the reader also misses the output matrix that the reference gain and the observer use, the conclusion of the controllability test, one of the two computed gains and the definition Ackermann's formula needs.
- Required action: put each pair on separate lines (an `aligned` or `gathered` block, or two displays): $A - BK$ and its determinant; $A, B$ and $C, D$; $AB$, $\mathcal{C}$ and $\det\mathcal{C}$; the desired polynomial (two lines if needed); $k_1$ and $k_2$; $K$ and $\varphi(A)$; the three integral gains.
- Priority: major
- Acceptance condition: on new captures the Section 1 determinant is fully visible at 1280 px, and at 360 px none of the listed equations is cut, in light and dark mode.

### L3. Block diagram: no caption or accessible name, raw label

- Location: Section 1, the Mermaid block diagram (desktop-light-02); `facts.json` reports one SVG figure without a title on every viewport.
- Problem: the diagram has no caption and no accessible title, and its gain block reads "k_r" with a literal underscore where the text writes $k_r$.
- Why it matters: screen-reader users get nothing; the raw label looks like a typo next to the typeset symbol.
- Required action: add `accTitle:`/`accDescr:` and a one-sentence caption (what to notice: the state, not the output, is fed back); label the block "reference gain" or use a Unicode subscript.
- Priority: minor
- Acceptance condition: `facts.json` reports 0 SVG figures without a title, the diagram has a caption, and no label shows an underscore.

Site-level items affecting this page (not raised separately): at 360 px the block diagram's right part (gain $K$, output) is off-screen with no scroll cue (mobile-light-04), and the 7rem minimum cell width hides the "Largest force" column of the Section 5.1 table and the last two columns of the Section 6.2 table (mobile-light-11, 16); punctuation after an inline equation wraps to the next line in Section 5.2 at 1280 px ("$+16r$" then ", so") and in the summary table at 360 px. Dark mode renders the diagram, equations and tables correctly (mobile-dark-04, 16).

## E. Technical and source findings

### L2. Section 6.4 does not link the page that quantifies sampling effects

- Location: Section 6.4, "The controller runs in continuous time".
- Problem: the section says the sample-and-hold "adds delay that erodes damping" without a pointer; [From Signal Processing to Digital Control](/blog/from-signal-processing-to-digital-control) derives that delay (half a sample), its phase cost and a rule for the sampling rate, and itself links to this section.
- Why it matters: the reader who needs to implement the controller digitally, the next practical step, has no path to the page that answers how fast to sample.
- Required action: one clause in Section 6.4 linking to that article (its Sections 4 and 5).
- Priority: minor
- Acceptance condition: Section 6.4 links to `/blog/from-signal-processing-to-digital-control`.

No technical or source errors found. KaTeX rendered without errors, no broken images, no console errors, no page-level horizontal scroll at 360 px (`facts.json`).

## F. Required changes

Mandatory:

- [ ] L1: split the side-by-side design equations listed in L1 so that they fit at 1280 and 360 px.

Optional:

- [ ] L2: link Section 6.4 to From Signal Processing to Digital Control.
- [ ] L3: caption, accessible title and clean label for the block diagram.
- [ ] Summary: merge the two closing paragraphs that retell the series into one.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
| L3 | | | |
