# Live review: PID Control of Process Variables

- URL: https://acrr.asia/blog/pid-control-of-process-variables
- Source: `src/content/blog/pid-control-of-process-variables.mdx` (Industrial Automation, entry 4 of 5)
- Commit deployed: `7e20c2c` (master after PR #57); the source is unchanged since `6c5490f` (wave 2 resolution of 13 October)
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40085671258 (2026-10-24 10:26 UTC): 22 desktop-light, 40 mobile-light, 40 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-24. The reviewer did not write or revise this article.
- Risk: routine (a technical tutorial on process control; no reporting, named-party claims, safety guidance or commercial relationship; the vendor remarks in Section 3.2 name no vendor)

## A. Decision

Request revision. One major presentation finding (L1): the PID law and its two discrete forms, the equations the whole page is built on, are cut off at 360 px, and the velocity form is also cut at 1280 px. The rest is minor.

**Library decision: retain.** The page is the site's only treatment of PID control as practiced in process plants: FOPDT and integrating models, step-test identification, the three PID forms and their units, the practical features of a real controller (derivative on measurement, setpoint weighting, anti-windup, bumpless transfer), a reproducible comparison of two tuning rules, and the character of the four classic loops. It is long (24 minutes) but every section serves the central question, how to model, implement and tune a process loop, and the simulation turns the tuning advice into evidence. The fixes needed are presentational and one cross-reference; no content needs rewriting.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineer or student who knows the feedback loop and the proportional offset (Foundations of Control Systems, entries 1 and 2) and has to commission or tune temperature, level, flow or pressure loops in a PLC or DCS.
- Problem: how to get a usable model of a process, what a real PID block does beyond the textbook law, how to choose its settings and why loops of different kinds behave differently.
- Outcome: identify an FOPDT model from a step test; convert between PID forms and units; know why derivative kick, noise, windup and mode switching need the features real controllers have; compute Ziegler–Nichols and SIMC settings and explain why the robust one is usually preferred; diagnose a slow level oscillation and suspect stiction.
- Distinctive contribution: one worked process (a heated vessel) carried from step test to tuning, with a short standard-library simulation that compares two tuning rules on the nominal and a perturbed process and shows windup in numbers; plus the integrating-loop result that reducing gain worsens a slow level oscillation.
- Evidence: derivations in the text; two Python programs with their output; Åström and Hägglund (2006), Seborg et al. (2016), Shinskey (1996), Skogestad (2003), Ziegler and Nichols (1942).
- Limitations: PI and PID only; no frequency-domain tuning, no model-predictive control, no gain scheduling; the step-test data are generated from the model, as the page says.

The benefit is delivered. The opening places the entry in both series and states the conventions; Sections 1 and 2 give the vocabulary and the models; Sections 3 and 4 the law and its implementation; Section 5 the tuning, with evidence; Section 6 the variable-specific advice; exercises with answers and a summary table close it. Checked for this review: both programs re-run together, all eight output lines identical to the page; $\tau = 1.5 \times 200.1 = 300.1$ s and $\theta = 29.8$ s; Ziegler–Nichols 6.00 and 100 s, SIMC 3.33 and 240 s; level SIMC settings (2.0 and 40 s; 0.19 and 420 s; $k'K_cT_i = 4.0$ and 3.99); Exercise 5 ($\zeta = 0.5$, $\omega_n = 0.025$ rad/s, period 290 s; halved gain $\zeta = 0.354$). No section is padding; the summary table repeats the page by design. Value category: practical implementation. Format: tutorial.

Overlap noticed: [From Signal Processing to Digital Control](/blog/from-signal-processing-to-digital-control) (Digital Signal Processing, entry 5) also teaches a discretized PI controller, integrator windup with clamping and a simulation of it, the derivative filter and the half-sample delay of the hold, from the signal-processing side (a motor-like plant, z-domain). The two pages are complementary, but neither links the other (L4). [Feedback and System Behavior](/blog/feedback-and-system-behavior) supplies the proportional offset this page builds on and is linked.

## C. Substantive findings

### L2. Section 4.4 points to the wrong section for the windup demonstration

- Location: Section 4.4, last sentence: "The simulation in Section 5.3 shows the effect."
- Problem: the effect of windup (with and without anti-windup) is shown in Section 5.4, "Windup in numbers". Section 5.3 uses clamping throughout and never shows a wound-up loop.
- Why it matters: a reader who follows the pointer finds a tuning comparison, not the windup effect.
- Required action: change the reference to Section 5.4.
- Priority: minor
- Acceptance condition: the sentence names Section 5.4 on the live page.

### L4. No link to the digital-control treatment of the same controller features

- Location: Section 4 (A digital PID controller), or the closing paragraph.
- Problem: [From Signal Processing to Digital Control](/blog/from-signal-processing-to-digital-control) covers discretizing a PI controller, windup and clamping, derivative filtering and the hold's half-sample delay; this page mentions the half-sample delay (Section 4.1) without pointing to the page that derives it.
- Why it matters: a reader who wants the sampled-data reasons behind Section 4 has no path to them; the site overlap map (Phase 7) needs the two pages connected.
- Required action: one sentence in Section 4.1 linking to that article for the derivation of the hold delay and the effect of sampling on stability.
- Priority: minor
- Acceptance condition: Section 4 links to `/blog/from-signal-processing-to-digital-control`.

## D. Visual and structural findings

### L1. The PID law and its discrete forms are cut off

- Location: Section 4.1, velocity-form equation (desktop-light-07); at 360 px also Section 3.1, the standard PID law (mobile-light-10), Section 4.1, position form (mobile-light-13) and velocity form (mobile-light-14), and Section 5.2, the SIMC FOPDT rule (mobile-light-20).
- Problem: at 1280 px the velocity form ends at "$u_k =$", hiding $u_k = u_{k-1} + \Delta u_k$. At 360 px the standard law loses its derivative term after "$e(\xi)$", the position form ends at "$\frac{T_d}{T_s}$", the velocity form shows only its first two terms, and the SIMC $T_i$ rule ends at "$\min(\tau, 4$". Each scrolls sideways, but nothing on the page says so.
- Why it matters: these are the equations the page is built on (the law every later section implements and tunes). A reader who does not discover the hidden scroll reads an incomplete law, and on desktop a dangling "$u_k =$".
- Required action: put $u_k = u_{k-1} + \Delta u_k$ on its own line under the velocity form; break the standard law, the position form and the velocity form over lines (an `aligned` block) so that each line fits 360 px; put the two SIMC FOPDT expressions on separate lines.
- Priority: major
- Acceptance condition: on new captures the velocity form is fully visible at 1280 px, and at 360 px no line of the Section 3.1 and 4.1 equations or the SIMC rule is cut.

### L3. Simulation results readable only in a wide code output

- Location: Section 5.3, output block (desktop-light-13, mobile-light-23).
- Problem: at 1280 px the last column loses its unit ("load IAE 97" without "%·s"); at 360 px only the overshoot column is visible, and settling time, load dip and IAE are hidden behind the code box's scroll. The prose quotes some values but not the load dips or the 45 s settling times.
- Why it matters: the comparison table is the evidence for the section's three conclusions.
- Required action: add a small results table after the output (four runs; overshoot, settling, load dip, load IAE), or shorten the printed labels so that the output fits at 1280 px (changing the code means re-running it).
- Priority: minor
- Acceptance condition: all four measures of the four runs are readable at 1280 px and at 360 px without scrolling inside the code box.

### L5. Loop diagram has no caption or accessible name

- Location: Section 1.1, the Mermaid loop diagram (desktop-light-02); `facts.json` reports one SVG figure without a title on every viewport.
- Problem: the diagram has no caption and no accessible title; at 1280 px its labels are noticeably smaller than the body text.
- Why it matters: screen-reader users get no description of the loop the bullet list then names; the caption is where the reader would be told that the transmitter closes the loop.
- Required action: add `accTitle:`/`accDescr:` lines and a one-sentence caption (for example via the `Figure` component).
- Priority: minor
- Acceptance condition: `facts.json` of new captures reports 0 SVG figures without a title, and the diagram has a caption.

Site-level items affecting this page (not raised separately): at 360 px the loop diagram's right half (Process, Transmitter) is off-screen with no scroll cue, and the 7rem minimum cell width hides the "Conversion to the standard form" column of the Section 3.2 table and part of the Section 5.2 settings table; punctuation after an inline equation wraps to the next line ("$\tau_c = \theta$" then "; a larger" at 1280 px, "$\theta/\tau = 0.1$" then "." at 360 px). Dark mode renders the diagram, tables, code and equations correctly (mobile-dark-04, 12, 22, 28).

## E. Technical and source findings

No technical or source errors found. Both programs reproduce the printed output exactly; every worked number and exercise answer checked (Section B) is right. The references are complete in the simplified IEEE form. KaTeX rendered without errors, no broken images, no console errors, no page-level horizontal scroll at 360 px (`facts.json`).

## F. Required changes

Mandatory:

- [ ] L1: break the PID law, the position and velocity forms and the SIMC FOPDT rule over lines so that they fit at 1280 and 360 px.

Optional:

- [ ] L2: Section 4.4 reference to Section 5.4.
- [ ] L3: results table for the Section 5.3 simulation.
- [ ] L4: link to From Signal Processing to Digital Control.
- [ ] L5: caption and accessible title for the loop diagram.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
| L3 | | | |
| L4 | | | |
| L5 | | | |
