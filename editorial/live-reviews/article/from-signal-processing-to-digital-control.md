# Live review: From Signal Processing to Digital Control

- URL: https://acrr.asia/blog/from-signal-processing-to-digital-control
- Source: `src/content/blog/from-signal-processing-to-digital-control.mdx` (Digital Signal Processing for Engineers, entry 5 of 5)
- Commit deployed: `7e20c2c` (master after PR #57); the source is unchanged since `2e79a4b` (wave 2 resolution of 15 October)
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40085671258 (2026-10-24 10:26 UTC): 20 desktop-light, 36 mobile-light, 36 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-24. The reviewer did not write or revise this article.
- Risk: routine (a technical explainer; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Accept with follow-up. The page is complete and correct at 1280 px, and its contract is delivered. Three minor findings: display equations cut at 360 px whose results the text restates nearby (L1), two diagrams without captions or accessible names (L2), and a missing cross-link to the PID entry (L3).

**Library decision: retain.** The page is the bridge between the site's two halves of control: it closes the DSP series by putting a filter inside a loop, and it supplies what the continuous-time control series leaves out (the zero-order-hold model, the stability limit that sampling imposes, emulation rules, windup in a digital PI, the hold's half-sample delay and a sampling-rate rule). Its examples reuse the plant of Feedback and System Behavior so every discrete result is compared with a continuous one, which no other page does. It overlaps in topic with the PID entry (windup, derivative filtering) but from the sampled-data side, with different evidence; both should stay and link each other.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineer or student who has the discrete-time tools of the DSP series (difference equations, z-transform, spectra, filter design) and basic feedback vocabulary, and has to implement or analyze a controller on a computer.
- Problem: what changes when a feedback loop is closed through an ADC, a computer and a DAC, and how to choose the discretization method and the sampling rate.
- Outcome: derive the zero-order-hold equivalent of a first-order plant; compute the stability limit sampling imposes on a proportional loop; choose between forward Euler, backward Euler and Tustin; implement a digital PI with clamping; estimate the phase cost of the hold and of computation delay; choose a sampling rate from a phase budget.
- Distinctive contribution: one first-order plant, shared with the continuous-time control series, analyzed exactly in discrete time, with two scripts that show the sampling-induced oscillation and the windup effect, and a sampling-rate rule derived from one formula.
- Evidence: derivations in the text; two NumPy scripts with their real output; Åström and Murray (2008), Åström and Wittenmark (1997), Franklin, Powell and Workman (1998), Oppenheim and Schafer (2010).
- Limitations: first-order plant only in detail; no direct discrete-time design method beyond the pointer to pole placement; nonlinear effects other than saturation not treated.

The benefit is delivered. The opening places the entry at the end of its series and names what it reuses from the control series; Sections 1 to 5 move from the loop's parts to the plant model, the controller, the delays and the sampling rate, and Section 6 ties the whole series to the loop. Checked for this review: both scripts re-run, output identical to the page; the $k_{\max}$ table ($\coth(T/2)$: 200.0, 20.02, 10.03, 4.08, 2.16); $\zeta = 5/(2\sqrt{10}) = 0.79$; the PI zero ($0.882$ for $T = 0.05$ s); the emulation images of $sT = -2.5$; Exercises 1 to 4 (20.07; $k = 9.51$ and 0.905; 1.8 and 5.4 kHz; 0.286 and $-0.111$). No section is padding. Value category: conceptual understanding. Format: explainer.

Overlap noticed: [PID Control of Process Variables](/blog/pid-control-of-process-variables) (Industrial Automation) also treats windup and clamping (with its own simulation), derivative filtering and the half-sample delay of sampling, from the process-control side; neither page links the other (L3, and L4 of that page's review). [Stability and Eigenvalues](/blog/stability-and-eigenvalues) Section 7 gives the discrete-time model and unit-circle test for state-space systems and is linked. [Designing a State-Feedback Controller](/blog/state-feedback-controller-design) Section 6.4 is linked from Section 5 (that page does not link back; L2 of its review). [Numerical integration notes](/blog/numerical-integration-notes) are linked for the Euler stability limit.

## C. Substantive findings

None. The analysis, numbers and recommendations are correct.

## D. Visual and structural findings

### L1. Three display equations cut at 360 px

- Location (360 px): Section 2.1, the zero-order-hold equivalent ends at "$(1 - e^{-aT}$" (mobile-light-08); Section 2.2, the stability bound ends at "$= \frac{a}{b}\coth$" (mobile-light-10); Section 3.2, the integral update loses its last term (mobile-light-16); Section 4.2, the phase-lag formula ends at "$= 180°$" without "$f_c/f_s$" (mobile-light-21).
- Problem: each display is wider than a phone screen and scrolls sideways without a visible cue. Unlike the cut equations recorded on other pages, each hidden result is restated nearby ($\varphi$ and $\gamma$ in the next sentence; $\coth(T/2)$ in Section 5 and the summary; $180° f_c/f_s$ in Section 5 and the summary), so the argument survives.
- Why it matters: the reader meets an incomplete formula at the point where it is derived and finds the result only later.
- Required action: break the zero-order-hold equivalent and the stability bound after the first "=", and the phase-lag chain into two lines (an `aligned` block); shorten the integral update or break it after "$+ K_i\frac{T}{2}$".
- Priority: minor
- Acceptance condition: on new 360 px captures none of the four displays is cut.

### L2. The two diagrams have no caption or accessible name

- Location: Section 1.1, the loop flowchart; Section 1.2, the timing sequence diagram; `facts.json` reports two SVG figures without a title on every viewport.
- Problem: neither diagram has a caption or an accessible title and description.
- Why it matters: screen-reader users get nothing; a caption would tell the reader what to notice (in the sequence diagram: the computation delay between the sample and the write).
- Required action: add `accTitle:`/`accDescr:` lines and a one-sentence caption to each.
- Priority: minor
- Acceptance condition: `facts.json` of new captures reports 0 SVG figures without a title, and each diagram has a caption.

Site-level items affecting this page (not raised separately): at 360 px both diagrams are cut on the right (the sensor block and the DAC lifeline) with no scroll cue; the 7rem minimum cell width hides the last three columns of the $k_{\max}$ table (including the critical $T = 0.5$ s value), the "Image of a stable continuous pole" column of the emulation table and the last two columns of the phase-lag table at 360 px, and puts the $T = 1.0$ column of the $k_{\max}$ table under the scroll shadow at 1280 px. Dark mode renders the flowchart, the sequence diagram, tables and code correctly (mobile-dark-05, 18).

## E. Technical and source findings

### L3. No link to the PID entry

- Location: Section 3.3 (windup) or Section 3.4 (derivative filter).
- Problem: [PID Control of Process Variables](/blog/pid-control-of-process-variables) covers the same controller features in the setting where most PID loops run (setpoint weighting, derivative on measurement, back-calculation, bumpless transfer, tuning rules), and this page does not point to it.
- Why it matters: a reader who has just met windup and derivative filtering here has no path to the practical treatment; the Phase 7 overlap map needs the pages connected.
- Required action: one sentence in Section 3.3 or 3.4 linking to that article.
- Priority: minor
- Acceptance condition: Section 3 links to `/blog/pid-control-of-process-variables`.

No technical or source errors found. KaTeX rendered without errors, no broken images, no console errors, no page-level horizontal scroll at 360 px (`facts.json`).

## F. Required changes

Mandatory:

- None (no critical or major finding).

Optional:

- [ ] L1: split the four displays so that they fit at 360 px.
- [ ] L2: captions and accessible titles for the two diagrams.
- [ ] L3: link Section 3 to the PID entry.
- [ ] Section 4.2: the first sentence says "falls through 1" twice ("For the usual loop whose gain falls through 1 once ... where the loop gain falls through 1"); one mention is enough.
- [ ] References: Åström and Murray is cited in its 2008 first edition here and in its 2021 second edition across the control series; citing the same edition would be more consistent (not an error).

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
| L3 | | | |
