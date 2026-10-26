# Live review: Planning on Graphs: Dijkstra's Algorithm and A*

- URL: https://acrr.asia/blog/graph-search-dijkstra-and-a-star
- Source: `src/content/blog/graph-search-dijkstra-and-a-star.mdx` (Motion Planning for Robots, entry 2)
- Commit deployed: `7e20c2c`
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40087219510 (2026-10-24 10:51 UTC): 33 desktop-light, 60 mobile-light, 60 mobile-dark tiles (dark tiles inspected where they hold the two Mermaid diagrams, the tables and code)
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-24. The reviewer did not write or revise this article.
- Risk: routine (a technical tutorial; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Accept with minor follow-up. The contract is delivered and every figure checked is right. Three minor findings: a wrong-way quotation mark in "A*'s" (L1), the weighted A* bound cut at its last term at 1280 px (L2), and three proof equations of Section 4 cut at 360 px (L3).

**Library decision: retain.** The page is the series' treatment of discrete search, from the generic loop to Dijkstra's algorithm, A*, heuristics, weighted A*, jump point search, Theta*, D* Lite and the limits of grids, each with a proof sketch or a measured result on one map. Nothing else in the library covers it. Nothing should be merged or reclassified.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineer or student who has read entry 1, knows what a graph and a queue are and reads Python.
- Problem: planning on a discretized configuration space and knowing which search to use, what it guarantees and what it costs.
- Outcome: build a grid or visibility graph; run and prove Dijkstra's algorithm; choose an admissible and consistent heuristic; predict the effect of weights, any-angle search and incremental replanning; see why grids do not scale with dimension.
- Distinctive contribution: one 15 by 26 map on which every search is run and counted (expansions, cost as a + b sqrt 2), short proofs of optimality and of the weighted bound, and a measured arm grid on the torus.
- Evidence: proofs in the text; programs with real output; Dijkstra (1959), Hart, Nilsson and Raphael (1968), Pohl (1970), Lozano-Pérez and Wesley (1979), Fredman and Tarjan (1987), Elfes (1989), Stentz (1994), Koenig and Likhachev (2002, 2005), Likhachev, Gordon and Thrun (2004), Nash et al. (2007), Harabor and Grastien (2011), LaValle (2006), Choset et al. (2005).
- Limitations: uniform-cost grids in the measurements; D* Lite described without its bookkeeping; counts depend on tie-breaking (stated).

The benefit is delivered. Value category: conceptual understanding, with practical implementation close behind (the full grid search is listed). Format: explainer.

Verified by computation: 10 + 12 sqrt 2 = 26.9706; 8-connected path 20.7% cheaper than 34 and 5.9% above 25.4691; the octile excess maximum sqrt(4 - 2 sqrt 2) = 1.0824 at 22.5 degrees; expansions 174 against 359 (52%) and 23 against 345 (93%); the inadmissible run 19.6569 / 17.3137 = 1.135; weighted ratios 1.074, 1.105, 1.244; Theta* 26.1265 / 25.4691 = 1.026; the arm band 0.367 to 0.714 rad; 360^6 = 2.18 x 10^15 cells and 272 TB at one bit per cell; the five-node Dijkstra trace (path S-A-B-C-G, cost 7).

Overlap: the visibility graph and the Minkowski inflation repeat entry 1 briefly with links; D* Lite (Section 5.4) is picked up in entry 5 Section 6.2 by link; the occupancy grid also appears in Sensing and State Estimation, linked.

## C. Substantive findings

None.

## D. Visual and structural findings

### L1. "A*'s" renders with an opening quotation mark

- Location: Section 4.3, last sentence of the second paragraph ("that is the source of A*'s savings"); desktop-light-14, mobile-light-25.
- Problem: the apostrophe after the asterisk is typeset as a left single quotation mark, so the page reads "A*‘s".
- Why it matters: a visible typographic error in running text.
- Required action: write the apostrophe as a right single quotation mark (U+2019) in the source, or rephrase ("the savings of A*").
- Priority: minor
- Acceptance condition: the sentence shows a correct apostrophe or no possessive on new captures.

### L2. Weighted A* bound: last term cut at 1280 px

- Location: Section 5.1, the chain from C = f_w(goal) to w C*; desktop-light-19.
- Problem: the equation ends at "<= w(g*(n') + h*(n')) =" with "w C*" behind the scroll edge.
- Why it matters: small; the result C <= w C* is displayed on its own just above.
- Required action: split the chain over two lines.
- Priority: minor
- Acceptance condition: the chain is fully visible at 1280 px.

### L3. Section 4 proof equations cut at 360 px

- Location: Section 4.2 (f(n') <= g*(n') + h*(n') = C*), Section 4.3 (the telescoping sum of reduced costs) and Section 4.4 (h_oct); mobile-light-23, 24 and 26.
- Problem: each ends mid-expression on a phone ("<= g*(n') + i", "= g(n", "+ (sqrt 2 -"), with no scroll cue.
- Why it matters: the first two are the steps the optimality and consistency arguments rest on; a phone reader who does not find the hidden scroll sees an incomplete proof. The site-level scroll cue would also solve this.
- Required action: break each over two lines (aligned blocks), or rely on the site-level scroll cue when it ships.
- Priority: minor
- Acceptance condition: at 360 px each of the three equations is fully visible or carries a visible scroll cue.

Site-level (not recorded separately): at 360 px the two Mermaid diagrams (the "Expand n" box of the search loop), the method and summary tables and wide program output scroll sideways without a cue; table cells keep their 7rem minimum width. On desktop the Theta* comparison output loses its right end; the values are repeated in the prose.

The page uses the right representations: a flowchart for the generic loop, a small weighted graph for the trace, ASCII maps printed by the programs for each search and comparison tables.

## E. Technical and source findings

None. `facts.json`: HTTP 200 on all three viewports, no horizontal page scroll, 0 KaTeX errors, 0 console errors. Navigation: older entry 1, newer entry 3; series previous and next correct.

## F. Required changes

Mandatory: none.

Optional:

- [ ] L1: fix the apostrophe in "A*'s".
- [ ] L2: split the weighted A* chain.
- [ ] L3: split the three Section 4 equations (or site-level scroll cue).

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
| L3 | | | |
