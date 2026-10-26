# Live review: Motion Planning for Robots (series overview)

- URL: https://acrr.asia/series/motion-planning
- Source: `src/content/series/motion-planning.md` (five entries, status published, no planned entries)
- Commit deployed: `7e20c2c`
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40087219510 (2026-10-24 10:51 UTC): 4 desktop-light, 7 mobile-light, 7 mobile-dark tiles (the page has no figure, table, code or display equation, so the dark tiles were not inspected individually)
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-24. The reviewer did not write or revise this page.
- Risk: routine (a series front door for technical explainers; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Accept. The overview states its reader and prerequisites, the order of the five entries with the reason for it, the scope and what is left out, and the shared conventions; five objectives say what the reader will be able to do. Every statement was checked against the entries. No findings.

**Library decision: retain.** The page is the series' entry point and adds what the entry cards cannot: the dependency from configuration space to graphs, sampling, timing and tracking, and the notation all five entries share. Nothing should be merged or reclassified.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineer or student who knows the two-link arm and frames from Introduction to Robotics, basic linear algebra and calculus, and reads Python, deciding whether and where to start motion planning on ACRR.
- Problem: knowing what the five entries cover, why in this order, what is out of scope and which conventions they share.
- Outcome: the reader knows the path from the abstract problem to the robot's wheels, where feedback comes from, what is excluded (kinodynamic planning, trajectory optimization beyond a mention, moving obstacles, arm tracking) and the notation q, C, C_free, C_obs, sigma, s(t).
- Distinctive contribution: an order stated as "the question a planner answers, from the most abstract statement to the robot's wheels", with each entry's role in one sentence.
- Evidence: the five entries. Checked in this review: entry 1 states the problem, C-obstacles and the torus and mentions trajectory optimization (CHOMP) in its map of methods; entry 2 covers Dijkstra's algorithm and A* and Section 6 their limits in dimension; entry 3 covers PRM, RRT and their guarantees, with kinodynamic planning only named; entry 4 adds time scaling with velocity and acceleration limits (reviewed separately the same day); entry 5 covers tracking and reactive avoidance on a differential-drive robot. All use SI units, radians in computation, l1 = 1.0 m, l2 = 0.7 m, Python 3.13 with NumPy 2.5 and stated seeds.
- Limitations: an overview; total reading time (about 198 minutes from the card estimates) is not stated.

The benefit is delivered. The opening screen gives the title, a complete description, the category, the Published status and "Start with entry 1"; progress shows 5 of 5. The objectives begin with assessable verbs and promise nothing the entries do not deliver. It links back to Introduction to Robotics and to Foundations of Control Systems; the reverse link from Introduction to Robotics is that series' open finding L2. Value category: reference value. Format: reference.

Overlap: mapped in the entry reviews of the same date (visibility graph in entries 1 and 2; D* Lite in entries 2 and 5; the clearance bound D in entries 1 and 3; occupancy grids with Sensing and State Estimation); all handled by links.

## C. Substantive findings

None.

## D. Visual and structural findings

None. The page reads correctly at 1280 and 360 px; the timeline of entry cards and the objectives column stack cleanly on a phone.

## E. Technical and source findings

None. `facts.json`: HTTP 200 on all three viewports, no horizontal page scroll, 0 KaTeX errors, 0 console errors.

## F. Required changes

Mandatory: none.

Optional: none.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| (none) | | | |
