# Live review: Sampling-Based Planning: Probabilistic Roadmaps and RRT

- URL: https://acrr.asia/blog/sampling-based-planning-prm-and-rrt
- Source: `src/content/blog/sampling-based-planning-prm-and-rrt.mdx` (Motion Planning for Robots, entry 3)
- Commit deployed: `7e20c2c`
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40087219510 (2026-10-24 10:51 UTC): 32 desktop-light, 61 mobile-light, 61 mobile-dark tiles (dark tiles inspected where they hold the Mermaid diagram, the table, the maps and code)
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-24. The reviewer did not write or revise this article.
- Risk: routine (a technical explainer; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Request revision. One major finding (L1): the article never shows a roadmap or a tree. Its central geometric claims (the Voronoi bias, roadmap paths that zigzag, RRT branches that wander 37% past the optimum, RRT* straightening its branches) are made in words and tables only, although the programs that produce the numbers could draw them. Two minor findings: the PRM* radius threshold is cut at 360 px (L2) and "RRT*'s" renders with an opening quotation mark (L3). The content itself is correct.

**Library decision: retain and update.** The article is the library's only treatment of sampling-based planning, and its measured comparisons (PRM against RRT and RRT-Connect, PRM* and RRT* convergence, narrow passages with uniform and bridge-test sampling, shortcutting) are original and checkable. The update is additive: one figure of the plane map with a PRM and an RRT drawn from the article's own runs. Nothing should be merged or reclassified.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineer or student who has read entries 1 and 2 and needs to plan for robots with more than two or three degrees of freedom.
- Problem: grids do not scale with dimension; which sampling planner to use, what its guarantees mean and when it fails.
- Outcome: build a PRM and an RRT on top of a collision checker; read probabilistic completeness and asymptotic optimality correctly; set the PRM* radius or k; recognize narrow passages and choose a sampling strategy; shorten a path.
- Distinctive contribution: the same planner code run on a point in a room and on the two-link arm on the torus, reported over 10 or 20 seeds as median, minimum and maximum against a known optimum (12.30 m).
- Evidence: programs with real output and seeds; Kavraki et al. (1996), LaValle (1998), Kuffner and LaValle (2000), LaValle and Kuffner (2001), Hsu, Latombe and Motwani (1999), Boor, Overmars and van der Stappen (1999), Hsu et al. (2003), Geraerts and Overmars (2007), Karaman and Frazzoli (2011), Kleinbort et al. (2019), Solovey et al. (2020), LaValle (2006), Choset et al. (2005).
- Limitations: two-dimensional examples (stated: so they can be printed); differential constraints out of scope; RRT* run with the PRM* constant and a capped radius, labeled a demonstration.

The benefit is delivered in substance: every claim is backed by a number, and the summary table states each method's limit. What holds the reader back is L1. Value category: conceptual understanding. Format: explainer.

Verified by computation: PRM* threshold 2 x 1.5^(1/2) x (71.80/pi)^(1/2) = 11.71 m; r_n = 0.973 m at n = 1000 and 0.722 m at 2000; k = ceil(2e ln n) = 31, 34, 38, 42 for n = 250 to 2000; RRT 16.91 / 12.30 = 1.375; RRT* 12.46 / 12.30 = 1.013; door sample probabilities 1.1% (w = 1.0 m) and 0.14% (w = 0.125 m); 0.02 x sqrt(1.7^2 + 0.7^2) = 0.037 m; shortcut reduction 6.47 to 4.87 rad (25%) and 4.87 / 4.671 = 1.043.

Overlap: probabilistic completeness, asymptotic optimality and the step bound D are defined in entry 1 and linked, not restated; the grid-scaling argument links to entry 2 Section 6.4; entry 5 Section 6.2 points back here for replanning in high dimension.

## C. Substantive findings

### L1. No picture of a roadmap or a tree

- Location: Sections 2.3, 3.2, 3.5 and 4.4; the only figure is the PRM flowchart in Section 2.1 (desktop-light-07 to 09, 14 to 18; mobile-light-15 to 31).
- Problem: the article explains a spatial process without showing it. The Voronoi bias (3.2) is argued in prose; "a roadmap path follows its edges, which point in random directions, so it zigzags" (2.3) and "each branch wanders wherever the random samples pulled it" (3.5) describe shapes the reader never sees; RRT* "straightens" its branches (4.3) with no before and after. The plane map is already printed by the programs, so the data for a drawing exist.
- Why it matters: standards 6.8 asks for a diagram where it reduces the effort of understanding the main concept. Here the main concept is how samples cover the free space; a reader who has never watched an RRT grow has to imagine it, and the 37% excess and the zigzag remain abstract.
- Required action: add one figure (generated by `scripts/generate-diagrams.py` from the article's own runs, as the house diagrams are) showing the plane map with (a) a PRM of 200 or 1000 vertices and its query path and (b) an RRT and its first path for one stated seed, both with the optimal path for comparison. Optionally a third panel with the RRT* tree after 4000 iterations. Caption says which seed and that it is one run.
- Priority: major
- Acceptance condition: on new captures the figure is present near Section 2.3 or 3.5, readable at 1280 px and at 360 px in light and dark mode, its seed and parameters match the text, and its caption states what to notice.

## D. Visual and structural findings

### L2. PRM* radius threshold cut at 360 px

- Location: Section 4.2, the display with r_n and gamma_PRM; mobile-light-32.
- Problem: on a phone the line ends at "gamma_PRM >", so the threshold, the formula Exercise 1 and the worked example use, is hidden with no scroll cue.
- Why it matters: it is the section's result; the worked example below restates it only for d = 2.
- Required action: put r_n and the gamma_PRM threshold on separate lines.
- Priority: minor
- Acceptance condition: both formulas fully visible at 360 px.

### L3. "RRT*'s" renders with an opening quotation mark

- Location: Section 4.3, "The original proof of RRT*'s asymptotic optimality"; desktop-light-19, mobile-light-34.
- Problem: the apostrophe after the asterisk is typeset as a left single quotation mark ("RRT*‘s").
- Why it matters: visible typographic error.
- Required action: write U+2019 in the source or rephrase ("the original proof that RRT* is asymptotically optimal").
- Priority: minor
- Acceptance condition: correct apostrophe or no possessive on new captures.

Site-level (not recorded): at 360 px the Mermaid flowchart, the summary table, the program listings and output blocks scroll sideways without a cue; table cells keep their 7rem minimum width.

## E. Technical and source findings

None. `facts.json`: HTTP 200 on all three viewports, no horizontal page scroll, 0 KaTeX errors, 0 console errors. Navigation: series previous entry 2, next entry 4; older and newer articles the same.

## F. Required changes

Mandatory:

- [ ] L1: add a figure of a PRM and an RRT on the plane map from the article's own runs.

Optional:

- [ ] L2: split the PRM* radius display.
- [ ] L3: fix the apostrophe in "RRT*'s".

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
| L3 | | | |
