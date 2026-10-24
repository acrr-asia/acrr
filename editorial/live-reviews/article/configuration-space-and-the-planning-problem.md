# Live review: Configuration Space and the Motion Planning Problem

- URL: https://acrr.asia/blog/configuration-space-and-the-planning-problem
- Source: `src/content/blog/configuration-space-and-the-planning-problem.mdx` (Motion Planning for Robots, entry 1)
- Commit deployed: `7e20c2c`
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40087219510 (2026-10-24 10:51 UTC): 33 desktop-light, 60 mobile-light, 60 mobile-dark tiles (dark tiles inspected where they hold the Mermaid diagram, the tables, the grids and the code)
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-24. The reviewer did not write or revise this article.
- Risk: routine (a technical explainer; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Accept with minor follow-up. The contract is delivered, every number checked is right and the page reads well on both screen sizes. One minor finding (L1): the definition of the wrapped angle difference in Section 2.2 is cut at the right edge at 1280 px.

**Library decision: retain.** This is the series' foundation: it defines the configuration space, the obstacle region, the planning problem, completeness and optimality, and edge checking, and the four later entries cite its sections by number. The 17 October QA finding (Summary row on shortest paths) is fixed and visible ("Shortest paths that bend around obstacles touch them"). Nothing should be merged or reclassified.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineer or student who knows frames and the two-link arm from Introduction to Robotics and wants to know what "planning a motion" means before learning any planner.
- Problem: turning "move this shape without hitting anything" into a precise problem, and knowing what a planner's answer (or failure) guarantees.
- Outcome: state a planning problem in configuration space; compute C-obstacles for a disk robot and, numerically, for the arm; explain topology (torus, components), completeness and optimality; check an edge safely with a clearance bound; place the main planner families.
- Distinctive contribution: one worked thread (room with boxes, two-link arm and disk) carried from definition to C-obstacle area, wall in joint space, components on the torus and a provable step bound D, with every number from runnable code.
- Evidence: derivations, programs with their real output, Lozano-Pérez (1983), Schwartz and Sharir (1983), Reif (1979), Canny (1988), Gilbert, Johnson and Keerthi (1988), Kavraki et al. (1996), Karaman and Frazzoli (2011), Ratliff et al. (2009), LaValle (2006), Choset et al. (2005), Lynch and Park (2017).
- Limitations: static obstacles, kinematic only; combinatorial planners named, not developed.

The benefit is delivered. Each section answers one part of the question and ends where the next entry picks up; the summary table and the map of methods let a reader return to it as a reference. Value category: conceptual understanding. Format: explainer.

Verified by computation: 36^6 = 2.18 x 10^9 and 36^7 = 7.84 x 10^10 cells; the grown-rectangle area 2.56 + 2.88 + 0.6362 = 6.0762 m^2; arcsin(0.2) = 11.54 degrees and the blocked window 8.958 to 11.042 degrees; the clearance bound D = 3.5605 and the Exercise 4 step of 0.0442.

Overlap: the visibility graph appears here (map of methods) and in entry 2 Section 2.3; the bound D is reused in entry 3 Section 5.3; the occupancy grid also appears in Sensing and State Estimation and entry 2. All are handled by cross-links, not repetition. The map of methods overlaps the series page's sequence paragraph, at a different depth.

## C. Substantive findings

None.

## D. Visual and structural findings

### L1. Section 2.2: definition of the angle difference cut at 1280 px

- Location: Section 2.2, the display equation defining rho and Delta_i; desktop-light-06.
- Problem: the equation is wider than the text column; the Delta_i definition ends at "cos(theta_i - theta_i'" with the closing part hidden behind the scroll edge.
- Why it matters: small; the wrap-around rule is explained in words around it, but a desktop reader expects a formula to fit.
- Required action: put the Delta_i definition on its own line (an `aligned` or `gathered` block).
- Priority: minor
- Acceptance condition: the equation is fully visible at 1280 px.

Site-level (not recorded): at 360 px the rho equation, the Section 2.3 and 3.1 displays, the Section 5.3 velocity bound, the Mermaid map of methods and the Section 6 table scroll sideways with no visible cue; table cells keep their 7rem minimum width. None hides a result the argument depends on that is not also stated in the text.

The page uses the right representations: grids printed by the programs for C-obstacles, a diagram for the map of methods and a comparison table.

## E. Technical and source findings

None. `facts.json`: HTTP 200 on all three viewports, no horizontal page scroll, 0 KaTeX errors, 0 console errors. Navigation: older "Distributed Memory and Message Passing", newer "Planning on Graphs"; the series block and related articles point to entries 2 to 5.

## F. Required changes

Mandatory: none.

Optional:

- [ ] L1: split the Section 2.2 rho equation.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
