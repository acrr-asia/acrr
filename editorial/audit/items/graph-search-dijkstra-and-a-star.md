# Editorial review: Planning on Graphs: Dijkstra's Algorithm and A*

- Path: `src/content/blog/graph-search-dijkstra-and-a-star.mdx` · Route: `/blog/graph-search-dijkstra-and-a-star` · Type: article, series entry 2 of 5 (`motion-planning`)
- Reviewed against: `editorial/standards.md` 1.0, `editorial/glossary.json`, `plugins/editorial-os/references/review-protocol.md`, the series overview `src/content/series/motion-planning.md`, the first entry (in full where cited: Sections 3, 3.3, 4, 5 and 6), the headings of the fourth and fifth entries and the outline of the third entry (still being written)
- Stages in this report: developmental (EOS step 6.1) and copy (6.2), both by an editor who did not write the entry. Line numbers refer to the revised file.
- Programs: `/tmp/claude-0/mp/graph-search-dijkstra-and-a-star/` (`run.sh` reproduces every quoted output). This stage did not re-run them; one derived number was recomputed (D8).

## Developmental review

The entry does its job for the stated reader. The opening links the first entry and says what this one builds on (path cost, completeness and optimality in Section 4 of the first entry; the C-obstacles of its Section 3), and the **Conventions** paragraphs state indexing, units, versions and the seed policy. Each section opens with its concept before the mechanism: the generic search loop before any specific algorithm, the occupancy grid before connectivity, the idea of settling nodes before the proof, admissibility and consistency before the grid heuristics. Every claim about the example map is backed by quoted program output, and the proofs (Dijkstra by first failure, A* optimality, consistency as reduced costs, the weighted A* bound) are sketched at the depth the outline asks for. Limits are stated section by section and gathered in Section 6, and the closing paragraph leads to the third entry. The order of Section 6.2 of the standards is followed. The eight `##` headings and every `###` heading are unchanged, so no fragment changed; the incoming links (`configuration-space-and-the-planning-problem.mdx:181` to `#6-the-limits-of-grids`, `path-tracking-and-reactive-avoidance.mdx:442` and `:446` to `#2-from-a-map-to-a-graph` and `#5-faster-any-angle-and-incremental-search`) still resolve.

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| D1 | Should fix | `:15`, opening | structure | The opening ended with a list of the sections, a table of contents in prose. |
| D2 | Should fix | `:15`, opening | consistency | "takes the first family on that entry's map" is false: grid search is the second family on that map. |
| D3 | Should fix | `:88`, Section 2.3 | publishing | Visitor copy referred to "the scratch folder", an authoring location the reader cannot see. |
| D4 | Should fix | `:146`, Section 3.4 | consistency | "A single function implements every search of Sections 3 to 5" is not true of Theta* or D* Lite. |
| D5 | Should fix | `:500`, Exercise 6 | consistency | The question asked why "the first run" expands more; the first run is $h = 0$, and the answer is about the run with $h = h^*$. |
| D6 | Should fix | whole entry | structure | Prose length about 6,090 words with headings, above the 6,000-word ceiling of the series brief. |
| D7 | Optional | `:21`, Conventions | consistency | "The two-link arm of Section 6" pointed at a whole section; the arm is in Section 6.3. |
| D8 | Should fix (for technical reviewer) | `:313`, Section 4.5 | evidence | "The savings are smaller than in open space" is a comparison with a run the entry does not show. |
| D9 | Should fix (for fact-checker) | `:370`, Section 5.2 | evidence | Jump point search: "no extra memory" and "its authors report speedups of A* by an order of magnitude or more" need checking against Harabor and Grastien (2011). |
| D10 | Should fix (for fact-checker) | `:385`, `:389`, Sections 5.3 and 5.4 | evidence | Two attributed claims: Nash et al. "state that Theta* is not guaranteed to find shortest paths"; Koenig and Likhachev "show that it is at least as efficient as D*". |
| D11 | Optional (for fact-checker) | `:364`, Section 5.1 | evidence | The weighted A* bound without reopening is attributed to the ARA* paper; confirm the paper's theorem covers this case (consistent $h$, no re-expansion). |
| D12 | Optional | `:91` and `:381` | structure | The visibility-graph output line is quoted twice (Sections 2.3 and 5.3). |

### D1. Opening reads as a list of contents
- **Where:** `src/content/blog/graph-search-dijkstra-and-a-star.mdx:15`, opening paragraph
- **Text:** "It shows how a map becomes a graph, derives Dijkstra's algorithm and A* with the arguments that make them optimal, compares heuristics by the nodes each search expands on a concrete grid, and describes weighted A*, any-angle search and incremental replanning. It ends with the limits of grids, which motivate the sampling-based planners of the next entry."
- **Problem:** Standards 6.1 and the developmental brief: the introduction sets up what follows "without a table of contents in prose". The list also carried a serial comma.
- **Correction (applied):** "Dijkstra's algorithm and A* return optimal paths on such a graph, and the arguments that prove it also say when a heuristic is safe and how much work a bounded loss of optimality saves. These guarantees hold only on the graph, and a grid grows exponentially with the dimension of the configuration space, which is why the next entry turns to sampling." The opening now states the argument of the entry, not its sections.

### D2. Wrong position on the first entry's map of methods
- **Where:** `:15`
- **Text:** "This entry takes the first family on that entry's map of methods"
- **Problem:** Section 6 of the first entry (`configuration-space-and-the-planning-problem.mdx:424-460`) lists combinatorial planners first and "Grid and graph search (second entry)" second. A false cross-reference (standards 9.1, C6).
- **Correction (applied):** "This entry treats the grid and graph search family from that entry's map of methods: discretize the free space into a graph, then search the graph."

### D3. Authoring location in visitor copy
- **Where:** `:88`, Section 2.3
- **Text:** "as the program `anyangle.py` in the scratch folder finds, 18 edges"
- **Problem:** The reader has no scratch folder; CLAUDE.md keeps authoring details out of public page copy. The entry names its programs elsewhere without a location.
- **Correction (applied):** "as the program `anyangle.py` finds, 18 edges".

### D4. Overstated scope of the listed function
- **Where:** `:146`, Section 3.4
- **Text:** "A single function implements every search of Sections 3 to 5."
- **Problem:** Theta* (Section 5.3) is a separate function `theta_star` in `anyangle.py`, the visibility-graph search is another, and D* Lite (5.4) is described, not implemented. Checked in the programs folder.
- **Correction (applied):** "A single function implements the grid searches of Sections 3, 4 and 5.1."

### D5. Exercise 6 question names the wrong run
- **Where:** `:500`
- **Text:** "Explain how many expansions the perfect heuristic should need, and why the first run below expands more."
- **Problem:** The first line of the output is $h = 0$ (359 expansions); the answer explains why $h = h^*$ expands 33 instead of 23. The answer also said "The first run expands 33".
- **Correction (applied):** "... and why the run with $h = h^*$ below expands more." In the answer: "The run with $h = h^*$ expands 33 because values of $f$ that are equal in exact arithmetic ... representation. The tie-breaking rule then never sees a tie, ..." (also splits a 51-word sentence; lint `sentence-length`).

### D6. Length above the series ceiling
- **Where:** whole entry
- **Problem:** The series brief sets 3,500 to 6,000 words of prose. Counted without front matter, code, display math, tables and reference lines, the draft had about 6,090 words including headings.
- **Correction (applied):** Tightened without removing any technical content: the new opening (D1); a shorter closing paragraph (the sentence restating the trade-offs of Section 5 is cut, since the Summary table states them); "The loop is the same for every method; what distinguishes them is the meaning of "best"" → "The methods differ only in the meaning of "best""; the node-expansion paragraph of Section 1 merged into one sentence; the clause "and the incremental planner of Section 5.4 searches backward for the same reason" (Section 3.3) cut, since 5.4 gives its own reason; the sentence "The estimate at $n$ may not exceed the cost of one step plus the estimate after it" (Section 4.3), a verbal restatement of the displayed inequality, cut; smaller cuts in Sections 1, 2.1, 3.1, 4.1, 4.5, 6.1 and 6.4. Result: about 6,000 words including headings and 5,840 without them.

### D7. Section reference to a whole section
- **Where:** `:21`
- **Text:** "The two-link arm of Section 6 has ..."
- **Correction (applied):** "The two-link arm of Section 6.3 has ...".

### D8. Comparison with open space not shown (for the technical reviewer)
- **Where:** `:313`, Section 4.5
- **Text:** "The savings are smaller than in open space because the walls mislead every heuristic."
- **Problem:** The entry shows no obstacle-free run, so the comparison is asserted, not demonstrated (standards 6.1, evidence for every non-trivial claim).
- **Correction:** The technical reviewer either runs `gridsearch.py` on the same grid without walls and quotes the counts, or the sentence is reworded to "The walls mislead every heuristic:" with the rest of the paragraph unchanged. Text left as written.
- **Recomputed in passing (no finding):** the blocked band of Section 6.3, "between about 0.367 and 0.714 rad", is $\operatorname{atan2}(0.6, 1.0) \pm \arccos\bigl((1 + 1.36 - 0.0625)/(2 \cdot 1.1662)\bigr) = 0.5404 \pm 0.1732$, that is 0.3673 to 0.7136 rad, and the center distance 1.1662 m; both agree with the text. The percentages of Sections 3.4, 4.5, 4.6, 5.1 and 5.3 and the answers to Exercises 1 and 5 were recomputed from the quoted outputs and agree.

### D9. Jump point search claims (for the fact-checker)
- **Where:** `:370`, Section 5.2
- **Text:** "It returns optimal paths with no preprocessing and no extra memory, and its authors report speedups of A* by an order of magnitude or more on their benchmark maps."
- **Problem:** Attributed performance claim (standards 7.2). Check against D. Harabor and A. Grastien, AAAI 2011, pp. 1114–1119; if the paper gives the speedup differently, quote its own wording or qualify.
- **Correction:** Verify; text left as written.

### D10. Attributed claims about Theta* and D* Lite (for the fact-checker)
- **Where:** `:385`, Section 5.3; `:389`, Section 5.4
- **Text:** "Nash et al. state that Theta* is not guaranteed to find shortest paths" and "its authors show that it is at least as efficient as D*"
- **Problem:** Both attribute a specific statement to a cited paper. Check against Nash et al. (AAAI 2007) and Koenig and Likhachev (IEEE Transactions on Robotics, 2005). The 2005 paper's comparison with D* is empirical; if it does not say "at least as efficient", reword to what it reports.
- **Correction:** Verify; text left as written.

### D11. Weighted A* bound without reopening (for the fact-checker)
- **Where:** `:364`, Section 5.1
- **Text:** "Likhachev, Gordon and Thrun proved, for their anytime algorithm Anytime Repairing A* (ARA*), that with a consistent $h$ the bound holds without reopening as well"
- **Problem:** The usual account; confirm that the theorem in the NIPS 16 paper is stated for consistent heuristics and for a search that does not re-expand states within one iteration.
- **Correction:** Verify; text left as written.

### D12. Duplicated output line
- **Where:** `:91` (Section 2.3) and `:381` (Section 5.3)
- **Problem:** The visibility-graph line appears in both blocks. Each block is needed where it stands (2.3 for the path through the corners, 5.3 for the comparison), so the repetition is defensible.
- **Correction:** None applied.

**Developmental verdict: pass.** The six should-fix findings of this stage (D1 to D6) and the optional D7 are applied. D8 goes to the technical reviewer and D9 to D11 to the fact-checker; they are not this stage's to resolve and remain open there.

## Copy edit

`npm run eos -- fix --rules spelling-variant,terminology` applied 0 fixes: spelling is American and the house terms are already used. Before the edit, lint showed 3 errors, 0 warnings and 5 suggestions; after it, 3 errors, 0 warnings and 3 suggestions. The 3 errors are expected while the third entry is being written and are not this item's to fix: `series-crossref` "fifth entry" at `:393` and `:416` (the linter counts the four entries that exist) and `internal-link` to `/blog/sampling-based-planning-prm-and-rrt` at `:528`. There are no em dashes, contractions, banned phrases, "simply/obviously/clearly/of course", first person singular or "we". Headings are in sentence case and numbered sequentially. The title (47 characters) is in headline style; the description is one sentence of 149 characters that says what the reader will learn.

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| C1 | Should fix | `:54`, Section 2.2 | language | The corner-cutting rule was hard to parse ("both cells that share a side with the two endpoints"). |
| C2 | Should fix | `:25`, Section 1 | evidence | A motive was attributed to LaValle's book ("because every grid or roadmap planner ends by solving it"). |
| C3 | Should fix | `:416`, Section 6.2 | language | "The optimal variant returned depends on tie-breaking" used "variant" for "path", and the paragraph's last item began with "And". |
| C4 | Should fix | `:313`, Section 4.5 | language | A 47-word sentence (lint `sentence-length`) with an appositive "the Euclidean heuristic, less informed, needs 208". |
| C5 | Should fix | `:528`, Summary | language | The closing paragraph had a 52-word sentence (lint `sentence-length`), and after D6 it used "RRT" in the link text before its expansion (lint `acronym-expansion`). |
| C6 | Should fix | `:251`, Section 4.3 | language | Serial comma: "its $g$ is final, no node is reopened, and the path is optimal". |
| C7 | Optional | `:223`, `:245`, `:217`, `:102` | language | Generic or wordy phrasing: "The importance of consistency is clearest through ...", "it is where knowledge ... enters", "and it has no information about", "A five-node graph shows the mechanism." |
| C8 | Optional | `:532`, `:535`, `:536`, References | language | Lint suggestions `acronym-expansion` for MIT, ACM and AAAI, kept (see below). |

### C1. Corner-cutting rule
- **Where:** `:54`
- **Text:** "A diagonal move squeezes between two cells that touch only at a corner, so the implementation used here allows it only when both cells that share a side with the two endpoints are free"
- **Problem:** "both cells that share a side with the two endpoints" can be read as four cells; the rule in the code (`FREE[r][nc] and FREE[nr][c]`) tests the two cells adjacent to both endpoints.
- **Correction (applied):** "A diagonal move passes between the two cells that share a side with both of its endpoints, so the implementation used here allows it only when both of those cells are free; otherwise the path would cut the corner of an obstacle."

### C2. Motive attributed to a cited book
- **Where:** `:25`
- **Text:** "LaValle's *Planning Algorithms* treats this discrete planning problem before any continuous method, because every grid or roadmap planner ends by solving it."
- **Problem:** The "because" states the author's reason as fact (standards 5.7, fact and interpretation). The next sentence already says why the discrete problem matters.
- **Correction (applied):** "LaValle's *Planning Algorithms* treats this discrete planning problem before any continuous method." The fact-checker still confirms the order of chapters (Chapter 2, discrete planning).

### C3. "Optimal variant"
- **Where:** `:416`
- **Correction (applied):** "Which of several optimal paths is returned depends on tie-breaking, and the one returned may hug an obstacle ..."; "And a grid over $(x, y)$ ignores" → "Finally, a grid over $(x, y)$ ignores".

### C4. Long sentence about the route over the walls
- **Where:** `:313`
- **Correction (applied):** "the less informed Euclidean heuristic needs 208"; "The path passes above both walls. The gap below the first wall is nearer the start row, but the second wall reaches down to row 13, so the route above both is cheaper; it runs straight along row 2 past the top of the second wall."

### C5. Closing paragraph
- **Where:** `:528`
- **Correction (applied):** The paragraph is now five sentences: optimality on the graph; "The guarantees hold only on the graph, and a grid over configuration space grows exponentially with its dimension: the two-link arm fits in 129,600 cells, but a six-joint arm does not fit in any grid fine enough to be useful."; "Probabilistic roadmaps and rapidly-exploring random trees (RRT) abandon the grid."; then the link to the next entry, which "shows how they build the graph from random samples ..., use the collision checker as their only access to the geometry and replace resolution completeness by a probabilistic guarantee." "fits comfortably" lost the intensifier.

### C6. Serial comma
- **Correction (applied):** "its $g$ is final, no node is reopened and the path is optimal."

### C7. Generic or wordy phrasing
- **Correction (applied):** "Consistency is easiest to understand through a change of edge costs."; "the **heuristic**, through which knowledge about the problem enters the search"; "grows a wavefront of equal cost around the start with no information about where the goal lies"; "In the five-node graph below, the edge labels are costs:"; "after which the robot is planned as a point moving between free cells".

### C8. Suggestions kept
- `acronym-expansion` MIT (`:532`), ACM (`:535`), AAAI (`:536`): publisher and venue names inside the reference list, given as the works give them; the house reference format does not expand them.

No technical claim, number, equation, code block, quoted output, unit, citation or link target was changed by either stage.

**Copy verdict: pass.** C1 to C6 are applied; no should-fix finding of this stage remains open. The three remaining lint errors belong to the unfinished third entry and clear when it exists.

Translation: no Vietnamese translation of this entry exists yet (`src/content/blog/vi/`), so none is marked for update.

<!-- Later stages (fact-check, technical review, resolution, QA) add their sections below. -->

## Fact-check

Stage EOS 6.3, by a reviewer who did not write or revise the entry. Line numbers refer to the file as it stands after the copy edit. `WebFetch` could not resolve any host in this session (`getaddrinfo ENOTFOUND` for dblp.org, ojs.aaai.org, idm-lab.org, arxiv.org), so every source below was checked through `WebSearch` result listings and their quoted abstracts, publisher records and catalogue entries; nothing was confirmed from a full text unless stated. No URL was added to the entry.

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| F1 | Should fix | `:48`, Section 2.1 | evidence | "Elfes introduced the representation for sonar-based mapping": occupancy grids were introduced by Moravec and Elfes in 1985; the cited 1989 article is Elfes's later, fuller account. |
| F2 | Should fix | `:223`, Section 4.1 | evidence | "proved the two properties this section derives" is broader than the 1968 paper supports: it proves optimality with an admissible heuristic and introduces the consistency assumption, but the reduced-cost argument and the no-reopening result in the form of Section 4.3 are not shown to be theirs. |

### F1. Origin of occupancy grids
- **Where:** `src/content/blog/graph-search-dijkstra-and-a-star.mdx:48`, Section 2.1 "Occupancy grids"
- **Text:** "Elfes introduced the representation for sonar-based mapping"
- **Problem:** H. Moravec and A. Elfes, "High resolution maps from wide angle sonar," Proceedings of the IEEE International Conference on Robotics and Automation, pp. 116–121, March 1985 (Carnegie Mellon Robotics Institute publication record; the paper builds "a rasterized map of probable occupied and empty areas" from wide-angle sonar). The cited A. Elfes, *Computer* 22(6):46–57, 1989 (confirmed, special issue on autonomous intelligent machines) is the later, fuller presentation. Crediting Elfes alone with introducing the representation is a misattribution (standards 7.2).
- **Correction:** "Moravec and Elfes introduced the representation for sonar-based mapping, and Elfes developed it into a probabilistic framework, and the [state estimation entry ...]" (or split into two sentences), and add to the references, in alphabetical position after Lozano-Pérez and Wesley: "- H. Moravec and A. Elfes, "High resolution maps from wide angle sonar," in *Proceedings of the IEEE International Conference on Robotics and Automation*, pp. 116–121, 1985." Smallest alternative without a new reference: "Elfes developed the representation for sonar-based mapping".

### F2. What Hart, Nilsson and Raphael proved
- **Where:** `:223`, Section 4.1
- **Text:** "Hart, Nilsson and Raphael introduced the algorithm in 1968 and proved the two properties this section derives."
- **Problem:** The section derives (4.2) optimality with an admissible heuristic and (4.3) that a consistent heuristic gives final $g$ at expansion, no reopening, and equivalence to Dijkstra's algorithm on reduced costs. The 1968 paper (IEEE Trans. SSC 4(2):100–107, confirmed) proves admissibility of A* when $h$ is a lower bound and, under its "consistency assumption", that A* expands no more nodes than any admissible algorithm no better informed. The authors' 1972 correction (SIGART Newsletter) states that their optimality proof had used $g(n) = g^*(n)$ for closed nodes, which depends on consistency, so the closed-node result is in the paper in some form; the reduced-cost formulation is not. The sentence is defensible only in a narrower form.
- **Correction:** "Hart, Nilsson and Raphael introduced the algorithm in 1968, proved that it returns an optimal path whenever $h$ never overestimates, and introduced the consistency condition of Section 4.3."

### Developmental and copy findings left to this stage
- **D9 (Section 5.2, `:370`): settled, verified, no change.** The 2011 paper's own summary: the method is "fast, optimal and requires no memory overhead", and "searching with jump points can speed up A* by an order of magnitude and more". The authors' later papers (SoCS 2012, ICAPS 2014) state that JPS needs no preprocessing; the 2011 method is online pruning with no offline step. The text's "no preprocessing and no extra memory" and "speedups of A* by an order of magnitude or more on their benchmark maps" match.
- **D10 (Sections 5.3 and 5.4, `:385`, `:389`): settled, verified, no change.** Nash et al. (AAAI 2007) conclude that neither Field D* nor Theta* is guaranteed to find shortest paths (the 2010 JAIR version says Basic Theta* "is not guaranteed to find true shortest paths"). The abstract of Koenig and Likhachev (2005) says D* Lite "determines the same paths" as D* and "is at least as efficient as D*". Both attributions are accurate. (The technical reviewer asks for a change to the explanation that follows, T2; that is not an attribution problem.)
- **D11 (Section 5.1, `:364`): settled, verified with a caveat, no change.** ARA* runs weighted A* without re-expanding a state within one call of ImprovePath (it keeps the INCONS list for that purpose), and the paper's bound is $g \le \epsilon\,g^*$ under consistent heuristics. Confirmed from the abstract and secondary descriptions (for example the ARA*+ comparison, "ARA*, which forbids the expanded states to be expanded again"); the theorem wording itself was not seen (Not verified). The sentence attributes nothing beyond this.
- **C2 (Section 1, `:25`): settled, verified, no change.** LaValle's book site lists Chapter 2, "Discrete Planning" (feasible and optimal planning, Dijkstra's algorithm, A*), in Part I, before Part II "Motion Planning", which starts at Chapter 3 (geometric representations). The sentence as revised by the copy stage is accurate.

### Verification table

| Claim | Location | Status | Source |
|---|---|---|---|
| LaValle treats discrete planning before any continuous method | `:25` | Verified | LaValle, *Planning Algorithms*, CUP 2006, chapter list on the author's site (Ch. 2 Discrete Planning; Part II from Ch. 3) |
| Elfes introduced occupancy grids for sonar mapping | `:48` | Corrected (F1) | Moravec and Elfes, ICRA 1985, pp. 116–121 (CMU RI record); Elfes, *Computer* 22(6):46–57, 1989 |
| Shortest path among polygons bends only at vertices; Lozano-Pérez and Wesley used it in the visibility graph | `:86` | Verified | Lozano-Pérez and Wesley, CACM 22(10):560–570, 1979 (ACM October 1979 issue listing; the author's MIT publication list) |
| Naive visibility-graph construction $O(n^3)$; Choset et al. describe a rotational plane sweep in $O(n^2 \log n)$ | `:94`, `:520` | Verified (secondary) | CMU 15-381 lecture slides (naive $O(N^3)$, sweep $O(N^2 \log N)$); the pathviz project states its rotational-plane-sweep pseudocode is from *Principles of Robot Motion*; book text not seen |
| Visibility graphs do not carry over to 3-D (shortest paths can run along edges) | `:94` | Verified | Standard result (textbook knowledge; consistent with the 3-D shortest-path literature) |
| Dijkstra 1959, three-page note that also gave a minimum spanning tree algorithm | `:100` | Verified | *Numerische Mathematik* 1:269–271, doi 10.1007/BF01386390 (Springer); the paper's first problem is the tree of minimum total length |
| Fibonacci heap: $O(E + V\log V)$ | `:140` | Verified | Fredman and Tarjan, JACM 34(3):596–615, 1987: "O(n log n + m)" for single-source shortest paths |
| Hart, Nilsson and Raphael introduced A* (1968) and proved the section's two properties | `:223` | Corrected (F2) | IEEE Trans. SSC 4(2):100–107, 1968 (IEEE Xplore record, abstract); the authors' 1972 correction |
| Pohl studied weighting of path cost against the heuristic, 1970 | `:352` | Verified | Pohl, *Artificial Intelligence* 1(3–4):193–204, 1970, doi 10.1016/0004-3702(70)90007-X (abstract: efficiency as a function of "the weight placed on the heuristics") |
| Weighted A* bound without reopening, consistent $h$, ARA* | `:364` | Verified (secondary) | Likhachev, Gordon and Thrun, NIPS 16, pp. 767–774 (NeurIPS proceedings page); see D11 |
| ARA* lowers $w$ and reuses earlier search effort | `:366` | Verified | ARA* abstract: "reuses previous search efforts" while tightening the bound |
| JPS: optimal, no preprocessing, no extra memory, order-of-magnitude speedups of A* | `:370` | Verified | Harabor and Grastien, AAAI 2011, pp. 1114–1119 (AAAI OJS 25(1)); see D9 |
| Theta* by Nash, Daniel, Koenig and Felner; not guaranteed shortest paths | `:374`, `:385` | Verified | AAAI 2007, pp. 1177–1183 (mlanthology, idm-lab bibliography); JAIR 39:533–579, 2010 |
| D* by Stentz is an early incremental algorithm for navigation | `:389` | Verified | Stentz, ICRA 1994, vol. 4, pp. 3310–3317 (IEEE Xplore 351061, CMU RI record) |
| D* Lite produces the same paths as D*, at least as efficient | `:389` | Verified | Koenig and Likhachev, IEEE T-RO 21(3):354–363, 2005, abstract |
| D* Lite: backward search, rhs lookahead, key modifier for robot motion | `:391–393` | Verified | Same paper (standard description of D* Lite); consistent with the 2002 AAAI "D* Lite" abstract |
| Arm lengths $l_1 = 1.0$ m, $l_2 = 0.7$ m as in the kinematics entry | `:21` | Verified | `planar-arm-kinematics.mdx:65` |
| Every reference entry (13): authors, title, venue, volume, issue, pages, year | `:532–544` | Verified | As listed above; Choset et al. author order and MIT Press 2005 confirmed (CMU RI and Northwestern records, ISBN 0-262-03327-5). ARA*: NeurIPS lists the conference year 2003; the MIT Press volume appeared in 2004, so "2004" is acceptable |

### Not verified
- The exact wording of the ARA* theorem (consistent heuristics, no re-expansion within an iteration) at `:364`: full text not reachable in this session; confirmed from the abstract and secondary descriptions only. No change recommended; the sentence claims no more than the standard account.
- Choset et al.'s own statement of the $O(n^2 \log n)$ rotational plane sweep at `:94`: book text not reachable; two independent secondary sources (a course slide deck and a project stating its pseudocode is from the book) agree. No change recommended.
- Nothing else in the entry was left unverified. The four items the writer could not confirm are settled: the rotational plane sweep (secondary, above), the consistency result (corrected, F2), the Lozano-Pérez and Wesley end page (570, confirmed by the ACM issue listing and the author's publication list) and the LaValle details (C2, verified).

**Fact-check verdict: fail** until F1 and F2 are applied (two should-fix, no blocking). No reference is fabricated or unconfirmed.

## Technical review

Stage EOS 6.4, by a reviewer who did not write or revise the entry. Scratch files: `/tmp/claude-0/mp/review/graph-search-dijkstra-and-a-star/`.

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| T1 | Should fix | `:313`, Section 4.5 | evidence | (Settles D8.) "The savings are smaller than in open space" is true but unshown; the open-space run gives 23 against 345 expansions. |
| T2 | Should fix | `:374`, `:385`, Section 5.3 | accuracy | The implementation's choice of cell centers as nodes is presented as the definition of Theta*, and the reason given for its non-optimality is specific to that choice. |
| T3 | Optional | `:149`, Section 3.4 listing | consistency | The listing's comment says "The search used in Sections 3 to 5"; the prose (after D4) says Sections 3, 4 and 5.1. |
| T4 | Optional | `:435`, Section 6.3 | accuracy | "every path found is close to 4.94 rad": the $N = 36$ path is 5.0016 rad. |

### T1. Open space comparison (D8)
- **Where:** `:313`
- **Text:** "The savings are smaller than in open space because the walls mislead every heuristic."
- **Problem:** The claim is correct but the entry gives no evidence for it. Running the article's own `astar` on the same 15 by 26 grid with every cell free, same start and goal (`recompute.py`):
  ```text
  Dijkstra      4 exp  319 cost 22.0000
  A* Manhattan  4 exp   23 cost 22.0000
  Dijkstra      8 exp  345 cost 22.0000
  A* Euclid     8 exp   23 cost 22.0000
  A* octile     8 exp   23 cost 22.0000
  ```
  In open space the octile heuristic cuts the expansions by 93% (23 of 345, the 23 path cells only); with the walls by 52%.
- **Correction:** Add a no-walls run to `gridsearch.py` (so that `run.sh` produces the number) and replace the sentence with: "Without the walls, on the same grid, A* with the octile heuristic expands only the 23 cells of its path against Dijkstra's 345; the walls cut the savings because they mislead every heuristic." If no run is added, use the editors' fallback: "The walls mislead every heuristic:" and keep the rest of the paragraph.

### T2. Theta* nodes and the reason it misses the shortest path
- **Where:** `:374` and `:385`, Section 5.3
- **Text:** "it tests whether the parent of $n$ sees $n'$, that is, whether the segment between their centers stays out of blocked cells" and "It is not the shortest path, because it turns at cell centers while the shortest path turns at obstacle corners"
- **Problem:** Cell centers as nodes are a choice of `anyangle.py` (`xy(cell)` maps a cell to its center; the line-of-sight test is between centers). Theta* is not defined by that choice, and the "because" makes the cell-center placement the reason Theta* is not optimal. The general reason, the one Nash et al. give, is that a node can take as its parent only the expanded node or that node's parent, so Theta* does not search every visible vertex (that is why the 2010 paper adds Angle-Propagation Theta* and still calls Basic Theta* not guaranteed optimal). As written, a reader would conclude that Theta* with obstacle corners as nodes would be exact, which the source does not support.
- **Correction:** At `:374`: "... it tests whether the parent of $n$ sees $n'$, that is, whether the segment between them stays out of blocked cells (in the implementation here, nodes are cell centers)." At `:385`: "It is not the shortest path. This implementation turns only at cell centers, while the shortest path turns at obstacle corners, and in any case Theta* considers as the parent of a node only the expanded node or that node's parent; Nash et al. state that Theta* is not guaranteed to find shortest paths."

### T3. Listing comment
- **Where:** `:149`
- **Correction:** "# Python 3.13. The grid search of Sections 3, 4 and 5.1 (from gridsearch.py)."

### T4. Arm path lengths
- **Where:** `:435`
- **Text:** "but every path found is close to 4.94 rad"
- **Correction:** "but every path found is between 4.93 and 5.00 rad long".

### Log of checks

Programs run (Python 3.13.16, NumPy 2.5.3, matching the stated versions): the writer's eight programs were copied to `run/` and `run.sh` was executed; its output is **byte-identical** to `all_output.txt`, and every quoted block in the entry (Sections 2.3, 3.1, 3.4, 4.4, 4.5, 4.6, 5.3, 6.3, 6.4 and Exercise 6) matches that output exactly. The listing at `:148–207` was diffed against `gridsearch.py`: identical apart from the omitted map and print code, as the Conventions say. The one random map uses `default_rng(7)`, stated in the text; the text presents it as one case, not a general rate. A 200-seed sweep (`seeds.py`) on the same 10 by 14 map type gives 147 solvable maps, of which the Manhattan heuristic returns a costlier path on 48 and fewer expansions on 135, so the seed is representative, not a lucky one.

Independent recomputations (`recompute.py`, `vis_indep.py`):
- Section 2.2: 4-connected excess $\max(\cos\phi + \sin\phi) = \sqrt{2} = 1.4142$ at 45°; 8-connected $\sqrt{4 - 2\sqrt{2}} = 1.08239$ at 22.5°, confirmed analytically and by a numeric maximum over $\phi$ (1.082392 at 22.4999°). 370 free cells out of 390.
- Section 2.3: visibility graph rebuilt by a different method (dense sampling of each segment against the open rectangles, not Liang–Barsky): 10 vertices, 18 edges, cost 25.469131, same path. Path length from the printed vertices 25.4691; Theta* vertex path 26.1265.
- Section 3.1 trace checked by hand against the five-node graph. Section 3.2 proof and Exercise 3 checked step by step ($d(B) = 3 > d(A) = 1$).
- Section 3.3: $E \le 4V$ for 8-connectivity; the binary-heap and Fibonacci-heap bounds are standard.
- Sections 3.4 and 4.5: 20.7% (0.2067), 5.9% (1.0590), 52% (0.5153); $10 + 12\sqrt{2} = 26.9706$, $12 + 12\sqrt{2} = 28.9706$, $10 + 14\sqrt{2} = 29.7990$, $18 + 11\sqrt{2} = 33.5563$. The route description (gap below the first wall nearer the start row; second wall rows 3 to 13; path along row 2) matches the map and the printed path.
- Sections 4.2, 4.3 and 5.1: the optimality proof, the telescoping sum of reduced costs and the weighted A* chain $C = f_w(\text{goal}) \le f_w(n') \le w\,C^*$ checked; each step follows (using $h(\text{goal}) = 0$, $h \le h^*$ and $w \ge 1$).
- Section 4.4: the Manhattan overestimate factor $2/\sqrt{2} = \sqrt{2}$; consistency of octile and Euclidean (Exercise 2) checked.
- Section 4.6: $6 + 8\sqrt{2} = 17.3137$, $14 + 4\sqrt{2} = 19.6569$, ratio 1.1353 (13.5%); nine straight moves along the bottom row counted from the printed map.
- Section 5.1: $C/C^*$ = 1.0742, 1.1049, 1.2442.
- Section 5.3: 1.0258 (2.6%) and 1.0590 (5.9%); three segments from four vertices.
- Section 6.3: center distance 1.16619 m; band $0.5404 \pm 0.1732$ = 0.3673 to 0.7136 rad (21.04° to 40.89°); the closest point of link 1 to the center is its end in that band, since the foot of the perpendicular lies beyond 1.0 m. Grid cell centers are at integer degrees for $N = 360$, so 22° to 40° (0.3840 to 0.6981 rad) is the expected discretization. A*/Dijkstra expansion ratios 0.232, 0.217, 0.229, 0.211 ("about a fifth"). Straight line 1.7088 rad; the way around ($\sqrt{(2\pi - 1.6)^2 + 0.6^2} = 4.72$ rad) is consistent with grid paths near 4.94 rad. Without wraparound in $\theta_1$ the band blocks every $\theta_2$, so failure is forced.
- Section 6.4: $360^6 = 2.177 \times 10^{15}$ cells, 272 TB; $100^6/8$ B = 125 GB; $360^7/8$ B = $9.8 \times 10^{16}$ B; 3.6° at 1 m = 6.28 cm.
- Exercise 1: 10, $4 + 3\sqrt{2} = 8.2426$, $\sqrt{58} = 7.6158$, 31.3%, 8.23%, $\arctan(3/7) = 23.2°$. Exercise 4: $C^* \in [16, 48]$. Exercise 5: $180^3 = 5{,}832{,}000$ cells, 729 kB; $180^6 = 3.40 \times 10^{13}$, 4.25 TB; $90^6/8$ B = 66.4 GB. Exercise 6: the 23-expansion argument with exact ties checked against the rounded-key run (23).
- Cross-references: every internal fragment in the entry resolves to an existing heading (`sensing-and-state-estimation#72-...`, `configuration-space-and-the-planning-problem#3-...`, `#33-...`, `#4-...`, `#5-...`, `path-tracking-and-reactive-avoidance#6-...`); the third entry now exists with the title used at `:528`, and its references to this entry (`#6-the-limits-of-grids`, `#64-the-curse-of-dimensionality`, $10^{12}$ cells) agree. The definition of resolution completeness at `:410` agrees with `configuration-space-and-the-planning-problem.mdx:311`. `eos lint` on the item: 0 errors, 0 warnings, 3 suggestions (C8, kept). The site was not built in this stage.

Nothing in the entry is presented as run that was not run.

**Technical verdict: fail** until T1 and T2 are applied (two should-fix, no blocking; T3 and T4 optional). Every equation, number and quoted output is correct.

## Resolution

By the author. Each change was made in `src/content/blog/graph-search-dijkstra-and-a-star.mdx`. Afterward `eos lint` reported 0 errors, 0 warnings and 3 suggestions (C8, kept). `run.sh` was re-run: its output is identical to `all_output.txt`, and every line of every quoted `text` block appears in that output. The map in Section 2.2 is the program's `MAP` constant, unchanged.

| ID | Action | Exact change |
|---|---|---|
| F1 | Applied | Section 2.1: "Elfes introduced the representation for sonar-based mapping, and the [state estimation entry ...]" became "Moravec and Elfes introduced the representation for sonar-based mapping, and Elfes developed it into a probabilistic framework. The [state estimation entry ...]". Added to References, after Lozano-Pérez and Wesley: H. Moravec and A. Elfes, "High resolution maps from wide angle sonar," in *Proceedings of the IEEE International Conference on Robotics and Automation*, pp. 116–121, 1985. The authors, title, venue, pages and year were verified by search (CMU Robotics Institute record, March 1985, pp. 116–121, with the same pages in a library catalogue). |
| F2 | Applied | Section 4.1: "introduced the algorithm in 1968 and proved the two properties this section derives." became "introduced the algorithm in 1968, proved that it returns an optimal path whenever $h$ never overestimates, and introduced the consistency condition of Section 4.3." |
| T1 | Applied with changes (preferred fix) | `gridsearch.py` now ends with a run on the same grid, start and goal with every cell free (8-connected Dijkstra, Euclidean and octile). `run.sh` already runs this file, so it produces the new output. Section 4.5: "The savings are smaller than in open space because the walls mislead every heuristic." became "Without the walls the savings are far larger (see below); the walls cut them because they mislead every heuristic." After that paragraph a new paragraph quotes the real output (Dijkstra 345 expansions; Euclidean and octile 23 each; cost 22.0000 for all three) and states: "Without the walls, A* with the octile heuristic expands only the 23 cells of its path against Dijkstra's 345, a reduction of 93%, and the Euclidean heuristic does as well; the walls bring the reduction down to 52%." The change from the suggested wording is that only the 8-connected rows are printed, since the paragraph compares 8-connected counts; the review's 4-connected figures (319 and 23) are not quoted. |
| T2 | Applied with changes | Section 5.3, mechanism: "whether the segment between their centers stays out of blocked cells." became "whether the segment between them stays out of blocked cells (in the implementation here, nodes are cell centers)." Result paragraph: "It is not the shortest path, because it turns at cell centers while the shortest path turns at obstacle corners; Nash et al. state ..." became "It is not the shortest path. This implementation turns only at cell centers, while the shortest path turns at obstacle corners. More generally, Theta* considers as the parent of a node only the expanded node or that node's parent, and Nash et al. state that Theta* is not guaranteed to find shortest paths." This is the suggested text, split into two sentences to stay under the sentence-length limit. |
| T3 | Applied | Listing comment: "# Python 3.13. The search used in Sections 3 to 5 (from gridsearch.py)." became "# Python 3.13. The grid search of Sections 3, 4 and 5.1 (from gridsearch.py)." `gridsearch.py` itself has no such comment, so the listing still matches the code. |
| T4 | Applied | Section 6.3: "but every path found is close to 4.94 rad." became "but every path found is between 4.93 and 5.00 rad long." (The table gives 4.9293 to 5.0016 rad.) |

## Series review changes

From the series review `reviews/motion-planning.md` (2026-10-17), applied by the author side:

- F3: Section 5.4 now reads "**D* Lite**, introduced by Koenig and Likhachev in 2002, ... and their journal account shows that it is at least as efficient as D*"; the AAAI-02 paper "D* Lite" (pp. 476–483) is added to the references before the 2005 journal paper, which is kept.
- F5: the disk radius in Section 2.1 is $r$ (as in the first entry), not $\rho$.
- F9: the link to the state estimation entry now says that it names such a grid as one form of map in simultaneous localization and mapping, not that it describes how the grid is built.
- F14: the cheapest cost in the proof of Section 3.2 and in the answer to Exercise 3 is $g^*(\cdot)$ (as in Section 4.2) instead of $d(\cdot)$, which clashed with the dimension $d$.
- No number, code or output changed.

## QA

Final gate (EOS step 10), by an independent QA editor who wrote and revised none of the entry. Record: `editorial/records/article/graph-search-dijkstra-and-a-star.json`. **Decision: publish, total 26/28.**

| Dimension | Score | Justification (below 4) |
|---|---|---|
| purpose | 4 | |
| structure | 4 | |
| accuracy | 4 | |
| evidence | 3 | The ARA* theorem wording, Choset et al.'s plane sweep and the Theta*/D* Lite attributions rest on abstracts and secondary sources, not full texts; the text claims no more than they support. |
| language | 4 | |
| consistency | 3 | Series review F12 (optional, deferred) leaves in-text citation forms differing across the series; within the entry everything agrees. |
| publishing | 4 | |

Critical conditions C1-C9: none holds for the item. C9 note: `reviews/motion-planning.md` is current and resolved but not yet stamped (`series-pipeline status`: review-stale); `series-pipeline stamp motion-planning` is due once all the series records are written, and the series gate fails until then.

Checks performed:
- Every should-fix finding of the item report (D1-D6, D8-D10, C1-C6, F1, F2, T1, T2) and of the series review (F3, F5, F9; optional F14) is resolved in the text as the Resolution says; none re-opened. No blocking finding was raised.
- `eos lint`: 0 errors, 0 warnings, 3 suggestions (C8, kept). `eos validate-site dist`: no issue on this page (the 26 site issues are on other pages); `dist/blog/graph-search-dijkstra-and-a-star.html` is newer than the source, has no `katex-error`, diagrams 407 px and 188 px. `npm run check:links`: all internal links resolve.
- `run.sh` re-run in `/tmp/claude-0/mp/qa/gs/` (Python 3.13.16): output byte-identical to `all_output.txt`; every line of every quoted `text` block is in it; the Section 2.2 map equals `MAP` in `gridsearch.py`; the listing matches `gridsearch.py` apart from its header comment.
- Recomputed independently: $10 + 12\sqrt{2} = 26.9706$; weighted A* ratios 1.0742, 1.1049, 1.2442; reductions 51.5% and 93.3%; 20.7%, 5.9%, 2.6%; 8-connected maximum 1.0824; Section 6.3 band 0.3673 to 0.7136 rad, center 1.1662 m; Section 4.6 13.5%; Section 6.4 and Exercise 5 memory figures (272 TB, 125 GB, 4.25 TB, 729 kB, 66.4 GB, 6.28 cm); Exercise 1 (8.2426, 7.6158, 31.3%, 8.23%, 23.2°). All agree. The proofs of Sections 3.2, 4.2, 4.3 and 5.1 and the Exercise 3 answer were read step by step.
- References against the fact-check table: Dijkstra (1959), Fredman and Tarjan (1987), Hart et al. (1968), Moravec and Elfes (1985) and Koenig and Likhachev (2002) agree in every detail; the list is alphabetical, the two Koenig and Likhachev entries in date order.
- Cross-references: each target exists and says what is claimed (first entry Sections 3, 3.3, 4 including the resolution-completeness definition, 5, and the map of methods in Section 6 listing grid and graph search second; Sensing and State Estimation Section 7.2; fifth entry Section 6; the fourth and third entries by title; arm lengths in the kinematics entry).
- Opening states purpose, prerequisites, conventions and versions; the ending summarizes and leads to the third entry. Title 47 characters, description 149 characters, one sentence. No example content; `example` not set, correctly.

Not verified: as listed in the fact-check (ARA* theorem wording, Choset et al. text); no full texts were re-read at this stage. No Vietnamese translation of the entry exists.
