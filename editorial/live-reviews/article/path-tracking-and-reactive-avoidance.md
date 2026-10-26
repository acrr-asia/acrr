# Live review: Following a Plan: Path Tracking and Reactive Obstacle Avoidance

- URL: https://acrr.asia/blog/path-tracking-and-reactive-avoidance
- Source: `src/content/blog/path-tracking-and-reactive-avoidance.mdx` (Motion Planning for Robots, entry 5)
- Commit deployed: `7e20c2c`
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40087219510 (2026-10-24 10:51 UTC): 33 desktop-light, 62 mobile-light, 62 mobile-dark tiles (dark tiles inspected where they hold the Mermaid diagram, the tables, the maps and code)
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-24. The reviewer did not write or revise this article.
- Risk: routine (a technical tutorial on simulated controllers; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Accept with minor follow-up. The contract is delivered, the worked numbers are right and the page closes the series as its opening promised. One minor finding (L1): two edge labels of the layers diagram overlap on every screen size.

**Library decision: retain.** The article is the library's only treatment of mobile-robot path tracking (pure pursuit, the Kanayama law) and reactive avoidance (potential fields, the dynamic window), with each method's failure demonstrated in simulation rather than asserted. The 17 October QA findings (unit superscripts; the insight link title) are fixed and visible. Nothing should be merged or reclassified.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineer or student who has followed entries 1 to 4 and knows basic feedback (Foundations of Control Systems), about to make a mobile robot follow a plan.
- Problem: a plan computed once from a map meets a robot that slips, lags and meets obstacles the map did not show.
- Outcome: write the unicycle and wheel equations; tune pure pursuit from its linearization; implement the Kanayama tracking law and choose its gains; explain and reproduce the traps of potential fields and DWA; place both in a layered navigation system with replanning and recovery.
- Distinctive contribution: one simulated differential-drive robot (first-order lag, turn-rate limit, 20 Hz control) on which each controller is run and its numbers explained by a linear model, including which effect (lag or limit) causes the overshoot.
- Evidence: derivations, programs with real output, Brockett (1983), Khatib (1986), Kanayama et al. (1990), Koren and Borenstein (1991), Coulter (1992), Rimon and Koditschek (1992), Fox, Burgard and Thrun (1997), Gat (1998), Koenig and Likhachev (2002), Choset et al. (2005), Siciliano et al. (2009), Lynch and Park (2017).
- Limitations: pose estimate taken as exact (stated, returned to in 6.4); kinematic model with one lag; static obstacles; DWA simplified (stated).

The benefit is delivered. Value category: practical implementation, with conceptual understanding close behind. Format: tutorial.

Verified by computation: the pure pursuit example L_d = 0.5831 m, kappa = 1.7647 1/m, omega = 0.8824 rad/s; the closed-loop pole magnitudes 0.833 (L_d = 0.15 m) and 2.032 (L_d = 0.02 m) of the sampled linear loop; zeta = 1/sqrt 2 and e^(-pi) = 4.3%; Kanayama critical damping K_y = K_theta^2/4 = 4 and zeta = 0.5, 0.25 for K_y = 16, 64; DWA stopping distance 0.525 x 0.25 + 0.525^2/1.0 = 0.41 m and G = 0.814; the braking bound v = 0.480 m/s (0.488 with s_hit = 0.36 m); the scene B stopping point (1 - rho = 2 rho^3 gives rho = 0.59 m, so x = 5.41 m).

Overlap: D* Lite is described in entry 2 Section 5.4 and only referenced here (6.2); the potential-field and DWA preview of entry 1 Section 6 is developed here; the occupancy grid and cost map link to entry 2; the layered architecture links to What Is a Robot? Sections 4 and 5. All handled by links.

## C. Substantive findings

None.

## D. Visual and structural findings

### L1. Layers diagram: "motor current" label overlapped by "wheel encoders"

- Location: Section 1, the Mermaid diagram of the navigation layers; the arrows between "Wheel speed control" and "Robot and environment"; mobile-light-06, mobile-dark-06 and the desktop rendering of the same figure.
- Problem: the two edge labels are placed on top of each other; "motor current" reads "motor curr" with the rest under "wheel encoders".
- Why it matters: the figure frames the whole entry (each arrow down a command, each arrow up the information that closes a loop), and the lowest loop is the one whose labels collide.
- Required action: change the layout so the two edges separate (for example place the encoder feedback edge on the other side, or move the labels into nodes), then check the rendering at 1280 and 360 px in both themes.
- Priority: minor
- Acceptance condition: both labels fully readable on new captures at both widths, light and dark.

Site-level (not recorded): at 360 px the Section 2.3 wheel-speed equations, the Section 3.1 circle equation, the Section 4 error dynamics and Kanayama law, the Section 5.2 piecewise potentials (their conditions are also stated in the text), the comparison and summary tables, and program output scroll sideways without a cue; table cells keep their 7rem minimum width.

The page uses the right representations: a layered diagram, program output tables for each tuning sweep, ASCII maps of the traps, and comparison and summary tables. A response plot of the cross-track error for the four look-ahead distances would add something, but the table and the linear model already carry the argument; not required.

## E. Technical and source findings

None. `facts.json`: HTTP 200 on all three viewports, no horizontal page scroll, 0 KaTeX errors, 0 console errors. Navigation: series previous entry 4 and "View the full series"; older entry 4, newer "What Is Critical Thinking?".

## F. Required changes

Mandatory: none.

Optional:

- [ ] L1: separate the two overlapping edge labels in the layers diagram.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
