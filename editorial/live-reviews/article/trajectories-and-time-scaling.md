# Live review: From Paths to Trajectories: Time Scaling and Velocity Profiles

- URL: https://acrr.asia/blog/trajectories-and-time-scaling
- Source: `src/content/blog/trajectories-and-time-scaling.mdx` (Motion Planning for Robots, entry 4)
- Commit deployed: `7e20c2c`
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40087219510 (2026-10-24 10:51 UTC): 30 desktop-light, 55 mobile-light, 55 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-24. The reviewer did not write or revise this article.
- Risk: routine (a technical tutorial with illustrative limit values; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Request revision. Two major findings: the equations that define the spline system and the stretch factor are cut even at 1280 px, and several more are cut at 360 px (L1); and a page about velocity profiles and the phase plane has no figure at all, so the reader must picture trapezoids, S-curves and the time-optimal curve from prose and program output (L2). Two minor findings (L3, L4). The text and the numbers are correct.

**Library decision: retain and update.** No other ACRR page covers time scaling, velocity profiles, time-optimal path parameterization or trajectory splines; the motion-planning series needs this entry between path planning and path tracking. Its overlap with the robotics series is handled by deep links rather than repetition (the Jacobian of Forward and Inverse Kinematics of a Planar Arm; the motion bound and clearance of Configuration Space and the Motion Planning Problem, Sections 3.2 and 5.3, which the editorial review had already removed from this page). The update is presentation: line-broken equations and two or three plots computed from the page's own programs. There was no 13 October audit for this article (published 17 October); the items of its own editorial review (repetition, undefined bang-bang terms, authoring reference in visitor copy, incomplete Pham reference) are resolved on the live page.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: a student or engineer who has a collision-free path from a planner (the series' first three entries) and must send a timed motion to real motors with speed, acceleration and jerk limits; comfortable with calculus and reading Python.
- Problem: a path says where but not when; the reader needs to choose a schedule that is as fast as the limits allow, smooth enough for the structure, passes through waypoints without stopping, and is verified before it reaches the hardware.
- Outcome: derive cubic and quintic time scalings and their shortest durations; compute trapezoidal, triangular and S-curve durations in every case; explain the phase plane, the velocity limit curve and the structure of time-optimal scaling; fit natural and clamped cubic splines with the Thomas algorithm; check a trajectory by sampling with a provable collision bound and fix a too-fast timing by uniform stretching.
- Distinctive contribution: one running example (the two-link arm with round limits) carried from polynomial scaling to S-curves, a discretized forward–backward time-optimal pass whose small limit violations are measured and explained, splines through waypoints, and a sampling check that distinguishes a proof of clearance from a sample that proves nothing.
- Evidence: derivations; Python listings with their real output (NumPy, deterministic); six exercises with answers; Bobrow et al. (1985), de Boor (2001), Flash and Hogan (1985), Kunz and Stilman (2012), Lynch and Park (2017), Pham (2014), Shin and McKay (1985).
- Limitations: kinematic limits only (no torque dynamics, although the 1985 papers treat them); kinodynamic planning and moving obstacles named but not treated; the forward–backward pass approximates, and does not replace, the switching-point algorithms; limit values are illustrative.

The benefit is delivered, at a cost in reading effort (the header says 40 minutes; the length is within the series standard and no section is padding). Spot checks recomputed in this review (python3, numpy, with the page's own `scurve_time` and an independent spline solver): cubic and quintic peaks ($6$, $10/\sqrt3 = 5.7735$) and durations (2.25 s, 2.8125 s); trapezoid 2.0 s; S-curve 2.2 s, 1.0 s (peak 0.6) and 0.5429 s (peak 0.1842), 72% longer than the 0.3162 s triangle; all natural and clamped knot accelerations, peak speeds and accelerations of Section 5.3 and the overshoot $\theta_2 = 1.9219$ rad; the gripper waypoints; $k = 1.1199$; Exercises 2, 5 and 6. The time-optimal run of Section 4.2 (1.818 s, the active-constraint intervals) was not recomputed, because the listing omits `x_limit`, the inverse kinematics and `path`; the editorial review reran the author's full program. Value density: Sections 4.3 and 6.2, which show what a numerical result does and does not prove, are the most valuable passages. Value category: practical implementation. Format: tutorial.

## C. Substantive findings

### L2. No figure for profiles whose shape is the subject

- Location: whole page (`facts.json`: 0 figures); most acutely Sections 3.1 to 3.3 (trapezoidal, triangular and S-curve profiles), Section 4.1 (the phase plane, the velocity limit curve, "a faster scaling is one whose curve lies higher") and Section 4.3 (which constraint is active where).
- Problem: the page describes shapes over time and a curve in the $(s, \dot s)$ plane entirely in words, equations and printed numbers. The reader is told the velocity "is a trapezoid, hence the name" and that the S-curve "has the S shape that names it" but never sees either, and must reconstruct the time-optimal curve from four lines of program output.
- Why it matters: standards 6.8 prefer a line chart for change over time; here the shapes are the concepts. Without them the phase-plane argument of Section 4, the hardest part of the page, demands far more effort than a single plot would, and a reader who cannot picture it is held back at the point the page's distinctive content begins.
- Required action: add, generated from the page's own programs: (1) velocity (and acceleration) against time for the cubic, quintic, trapezoidal and S-curve profiles of the running example on common axes; (2) the phase-plane plot of Section 4.2: the velocity limit curve, the backward and forward passes and the final scaling, with the active-constraint intervals of Section 4.3 marked. Captions say what to notice. Optionally, the clamped and natural spline of Section 5.3 for joint 2 with the overshoot marked.
- Priority: major
- Acceptance condition: the live page shows at least the profile plot and the phase-plane plot with captions, legible at 1280 and 360 px and correct in dark mode.

## D. Visual and structural findings

### L1. Equations cut, some at desktop width

- Location: at 1280 px: Section 5.2, the tridiagonal recurrence loses its last term and closing parenthesis, and the clamped end condition for $M_n$ is cut after "$= 6$" (desktop-light-18); Section 6.3, the stretch-factor display ends at "$\max(1.0725, \sqrt{1.254}$", hiding the result $1.1199$ (desktop-light-24). At 360 px, additionally: Section 5.2, the recurrence shows only its left-hand side (mobile-light-33); Section 2.3, the acceleration inequality loses "$a_{\max,i}$" (mobile-light-11); Section 4.1, the joint acceleration constraint loses its index (mobile-light-21).
- Problem: displays wider than the column; the hidden part scrolls sideways with no cue.
- Why it matters: the recurrence and end conditions are the system that Section 5's code and Exercise 5 solve; a reader cannot check the code against an equation whose right-hand side is invisible. The stretch factor is the result of Section 6.3.
- Required action: break the recurrence over two lines (left-hand side, then "$= 6(\dots)$"), put the two clamped end conditions on separate lines, and put the numerical evaluation of $k$ on its own line.
- Priority: major
- Acceptance condition: on new captures, the Section 5.2 and 6.3 displays are fully visible at 1280 px, and every display named above is fully visible at 360 px, light and dark.

### L3. Program output cut at desktop width where the prose relies on it

- Location: Section 3.2 output (the "simulated x, v_end" check is hidden; desktop-light-10); Section 4.2 output (the "at interval end" accelerations are hidden; desktop-light-15); Section 6.2 output ("motion bound per sample" values hidden; desktop-light-23).
- Problem: the printed lines are wider than the code box at 1280 px.
- Why it matters: small, because the prose repeats the numbers (2.0079 rad/s², 0.0023 m, 0.2265 m), but these are the values the argument of Sections 4.3 and 6.2 rests on, and the reader is told to read them from the output.
- Required action: shorten the labels or split the printed lines in the programs (re-run them and paste the new output).
- Priority: minor
- Acceptance condition: the three output blocks fit at 1280 px, or the finding is accepted as a limitation of wide program output.

At 360 px every code and output block scrolls sideways inside its box, which is expected for code; the comparison and summary tables scroll with the site's scroll shadow (site-level 7rem minimum cell width, already recorded). Code highlighting is legible in dark mode (mobile-dark-35).

## E. Technical and source findings

### L4. Reproducibility promise the reader cannot use

- Location: opening, Conventions paragraph: "all computations are deterministic, so rerunning the programs reproduces every quoted number exactly"; Sections 2.3, 4.2, 5.2 and 6.2, which say the listings omit helpers.
- Problem: the page publishes partial listings (omitting `x_limit`, the inverse kinematics, `path`, `spline_eval`, `clearance` and the printing code), so a reader cannot rerun the programs of Sections 4.2 and 6.2 at all.
- Why it matters: the sentence reads as an invitation to reproduce; a reader who tries finds it impossible for the two most interesting results.
- Required action: either publish the complete programs (for example as a downloadable file or a collapsed full listing) or reword the sentence to what is true for the reader ("the quoted output comes from running the complete programs, of which the listings show the core").
- Priority: minor
- Acceptance condition: the live page either links the complete programs or no longer implies the reader can rerun them.

No technical error found; all numbers checked in B agree. `facts.json`: HTTP 200 on all three viewports, no horizontal page scroll, no overflowing elements, 0 KaTeX errors, 0 broken images, 0 console errors.

Not verified in this review: the time-optimal output of Section 4.2 (see B); the attributions to Lynch and Park, Siciliano et al. and de Boor (checked by the article's fact-check stage, not re-checked here); reference details (not re-fetched).

## F. Required changes

Mandatory:

- [ ] L1: line-break the Section 5.2 and 6.3 displays (and the 360 px cases).
- [ ] L2: add the profile plot and the phase-plane plot, generated from the page's own programs.

Optional:

- [ ] L3: shorter output lines in the Section 3.2, 4.2 and 6.2 programs.
- [ ] L4: publish the full programs or reword the reproducibility sentence.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
| L3 | | | |
| L4 | | | |
