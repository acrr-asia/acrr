# Series review: Motion Planning for Robots

- Series: `motion-planning` (5 articles, status published, 0 planned entries)
- Reviewed commit: 9b1c7ed
- Date: 2026-10-17
- Reviewer: independent Series Editor (EOS step 8); I did not write or revise any of the entries or the series file.

## Summary

The series is technically sound and reads as one publication. The five entries keep the notation the first entry declares for the whole series ($q$, $\mathcal{C}$, $\mathcal{C}_{\mathrm{free}}$, $\mathcal{C}_{\mathrm{obs}}$, $\sigma$, $q(t) = \sigma(s(t))$, $C^*$), they use the same two-link arm ($l_1 = 1.0$ m, $l_2 = 0.7$ m, $\theta_2$ relative, torus without limits, reachable ring 0.3 to 1.7 m) throughout, and the statements about completeness and asymptotic optimality in entries 1 and 3 agree. Every cross-entry link resolves to a section that says what the link claims, and every forward promise is kept. The problems are of the kind only a series reading finds. The third entry's PRM diagram renders more than 1,000 px wide and overflows the column (the one blocking finding). The two entries that discuss D* Lite cite two different papers for it, and the Khatib (1986) paper is cited in two forms. Several symbols ($\rho$, $\delta$, the grid size) mean different things in different entries. The first entry presents RRT*'s asymptotic optimality as shown in 2011 without the later correction that the third entry reports. The second entry's link to the state estimation entry overstates what that entry describes, and one answer in the third entry states a proof condition that the second entry's grids do not meet. The series should be published after the blocking finding and the should-fix findings are resolved.

Findings: 1 blocking, 10 should fix, 5 optional.

## Resolution

The blocking finding, all 10 should-fix findings and four of the five optional ones (F13 to F16) were applied by the author side, not by the reviewer, mostly with the reviewer's recommended text. F12 is deferred. No number, equation, code or quoted output changed, so no program was re-run; the one new figure in the text (1.306 m, F15) was recomputed. The series has no Vietnamese translations, so no translation needed the same changes.

| Finding | Resolution |
|---|---|
| F1 | Entry 3, Section 2.1: the PRM diagram is `flowchart TB`. After the rebuild the figure in `dist/blog/sampling-based-planning-prm-and-rrt.html` has `min-width:143px` (natural size 239 × 946 px), down from 1005 px. The caption is unchanged and still true. |
| F2 | Entry 1, Section 4.3: applied as recommended; the sentence now links Section 4 of the third entry and mentions "a later correction to the proof for RRT*". |
| F3 | Entry 2, Section 5.4: "**D* Lite**, introduced by Koenig and Likhachev in 2002, produces the same paths with a simpler algorithm, and their journal account shows that it is at least as efficient as D*." The AAAI-02 paper (pp. 476–483, verified by a web search of its bibliographic record) is added before the 2005 journal paper, which is kept. Entry 5 needed no change. |
| F4 | Entry 5, References: Khatib (1986) now names *International Journal of Robotics Research*, identical to entry 1. |
| F5 | Entry 2, Section 2.1: the three occurrences of $\rho$ are $r$. $r$ is not used for anything else in entry 2. |
| F6 | Entry 3, Sections 1.2 and 5.3: the checking resolution is $\varepsilon$; no other $\varepsilon$ or $\delta$ remains in entry 3. |
| F7 | Entry 3, Section 1.1 and Summary: $N$ cells per axis, $N^d$ cells. $N$ occurs nowhere else in entry 3. |
| F8 | Entry 3, Section 1.2: applied as recommended, with the link to `#51-the-collision-checker-as-an-oracle`. |
| F9 | Entry 2, Section 2.1: applied as recommended ("names such a grid as one form of map in simultaneous localization and mapping, where the robot builds the map while it localizes itself"). |
| F10 | Entry 3, Exercise 4 answer: applied as recommended. The two conditions were checked: a free path meets only cells that contain a free configuration, so none is blocked under a whole-cell test, and consecutive cells on a continuous path share a side or a corner, so a search with corner moves (and the torus wrap) finds a cell path. |
| F11 | Overview: a new paragraph after the sequence rationale states the scope: static obstacles, geometry first and timing second, and no kinodynamic planning, trajectory optimization beyond a mention in the first entry, moving obstacles or tracking control of arms. The reviewer's serial comma was removed (standards 5.1), and the sentence is its own paragraph because the linter flagged the merged paragraph at 189 words. |
| F12 (optional) | Not applied. Choosing one in-text citation form for the series touches every entry and is polish; it is left for the next revision, as the reviewer suggested. |
| F13 (optional) | Applied with the recommended wording in entry 1, Section 4.3, and entry 3, Section 5.3. The identification with $D$ was checked: maximizing $1.7|a| + 0.7|b|$ over $a^2 + b^2 = 0.02^2$ gives $0.02\sqrt{1.7^2 + 0.7^2} = 0.0368$ m. |
| F14 (optional) | Applied where a reuse could confuse. Entry 2: $d(\cdot)$ in Section 3.2 and the Exercise 3 answer is $g^*(\cdot)$, the symbol Section 4.2 already uses for the true cost from the start, because Section 2.1 of the same entry uses $d = 2$ for the dimension. Entry 5, Exercise 3: the polynomial variable is $\lambda$, since $s$ is the series' path parameter and also the unit symbol in "$-0.8$ s$^{-1}$" beside it. Entry 4 not changed: its $D$ is the distance of a move, and its Section 6.2 states the first entry's bound as an expression without naming it $D$, so the two never meet; renaming would also touch the program and its output. |
| F15 (optional) | Applied as recommended; 1.306 m recomputed ($11.71 \times (\ln 500/500)^{1/2} = 1.3055$ m). |
| F16 (optional) | Applied as recommended in the overview's conventions paragraph. |

Second pass. After the corrections, the overview and all five entries were re-read in full for defects the changes introduced:
- Every changed sentence was read in its paragraph. The new cross-references (entry 1 to entry 2 `#22-connectivity-and-edge-costs` and entry 3 `#4-asymptotic-optimality-prm-and-rrt`; entry 3 to entry 1 `#51-the-collision-checker-as-an-oracle` and `#53-a-check-that-cannot-miss`, and to entry 2 `#63-a-grid-over-the-arms-configuration-space`) resolve, and each target says what the linking text claims (entry 3 Section 4.3 reports the corrected proof; entry 2 Section 6.3 tests cell centers; entry 1 Section 5.3 defines $D$).
- The renamed symbols ($r$ and $g^*$ in entry 2, $\varepsilon$ and $N$ in entry 3, $\lambda$ in entry 5) collide with no other use in their entries, and no occurrence of the old symbol was left behind in the changed passages.
- Entry 2's D* Lite text and references now agree with entry 5 (2002, AAAI-02 paper), and the two Koenig and Likhachev references are in date order.
- One defect introduced by the first pass was found and fixed: the F11 sentence made the overview's sequence paragraph 189 words long, so it became its own paragraph; it also carried a serial comma, removed.
- The F1 diagram is now narrow (143 px minimum) but tall (946 px at natural size); it no longer scrolls horizontally at any width, which was the defect, and no other entry's diagram width changed (369, 407, 188 and 320 px).
- A further full pass found nothing blocking or should-fix.
- `npm run build:local` exits 0, `npm run check:links` reports that all internal links resolve, `eos lint` shows 0 errors and 0 warnings on all six files, and the five built pages have no `katex-error` and no letter glued to `<a `, `<strong>` or `<code`.
- The edits make the review records of the overview and of entries 1, 2, 3 and 5 stale; they need the QA stage and `eos record` again before `eos gate` passes, and the series needs `series-pipeline stamp` after that.

## Objectives coverage

| Objective (from the series file) | Covered by | Assessment |
|---|---|---|
| State a motion planning problem in configuration space, and explain how obstacles in the workspace become obstacles in configuration space. | Entry 1, Sections 1–3 (problem statement, Minkowski sum, arm C-obstacles, split free space), Exercises 1–3 and 6 | Met. |
| Plan on a grid or graph with Dijkstra's algorithm and A*, and explain when a heuristic keeps A* optimal. | Entry 2, Sections 2–4 (admissibility proof, consistency through reduced costs, grid heuristics, inadmissible case), Exercises 1–3 and 6 | Met. |
| Explain how probabilistic roadmaps and rapidly-exploring random trees find paths in high-dimensional spaces, and what their completeness and optimality guarantees mean. | Entry 3, Sections 1–5, with the definitions of entry 1, Sections 4.2–4.3; Exercises 1, 4 | Met. The examples are two-dimensional so that they can be printed, which entry 3 states (Section 1.4); the high-dimensional argument rests on entry 2, Section 6.4. |
| Turn a geometric path into a trajectory that respects velocity and acceleration limits. | Entry 4, Sections 1–6, Exercises 1–6 | Met; jerk limits are covered as well. |
| Follow a planned path on a mobile robot with a tracking controller, and avoid obstacles that the plan did not know about. | Entry 5, Sections 2–6, Exercises 1–5 | Met. |

## Findings

| ID | Severity | Article | Location | Dimension | Finding |
|---|---|---|---|---|---|
| F1 | Blocking | `src/content/blog/sampling-based-planning-prm-and-rrt.mdx` | Section 2.1 (lines 133–144) | Writing quality (mechanical check) | The PRM `flowchart LR` renders with `min-width: 1005px`, far wider than the ~612 px column. |
| F2 | Should fix | `src/content/blog/configuration-space-and-the-planning-problem.mdx` | Section 4.3 (line 318) | Factual consistency | RRT*'s asymptotic optimality is attributed to Karaman and Frazzoli (2011) without the proof correction that entry 3, Section 4.3, reports. |
| F3 | Should fix | `graph-search-dijkstra-and-a-star.mdx`, `path-tracking-and-reactive-avoidance.mdx` | Section 5.4 and References (lines 400, 549); Section 6.2 and References (lines 460, 556) | Factual consistency | D* Lite is cited from the 2005 journal paper in entry 2 and from the 2002 conference paper, "introduced ... in 2002", in entry 5. |
| F4 | Should fix | `src/content/blog/path-tracking-and-reactive-avoidance.mdx` | References (line 555) | Factual consistency | Khatib (1986) is cited in *The International Journal of Robotics Research*; entry 1 (line 549) writes *International Journal of Robotics Research*. |
| F5 | Should fix | `src/content/blog/graph-search-dijkstra-and-a-star.mdx` | Section 2.1 (line 50) | Notation | The disk radius is $\rho$, which entry 1 uses for the distance on $\mathcal{C}$; entry 1, Section 3.1, which this sentence summarizes, calls the radius $r$. |
| F6 | Should fix | `src/content/blog/sampling-based-planning-prm-and-rrt.mdx` | Sections 1.2 and 5.3 (lines 36, 407) | Notation | $\delta$ is the checking resolution, but entry 1, Section 5.5, defines $\delta$ as the safety margin. |
| F7 | Should fix | `src/content/blog/sampling-based-planning-prm-and-rrt.mdx` | Section 1.1 (line 25), Summary (line 487) | Notation | "$m$ cells per axis ... $m^d$" restates entry 2, Section 6.4, which uses $N$ and $N^d$. |
| F8 | Should fix | `src/content/blog/sampling-based-planning-prm-and-rrt.mdx` | Section 1.2 (line 33) | Terminology | Entry 1, Section 5.1, names the query a "configuration check"; entry 3 renames it "point check" without relating the two. |
| F9 | Should fix | `src/content/blog/graph-search-dijkstra-and-a-star.mdx` | Section 2.1 (line 48) | Cross-article references | The state estimation entry is said to describe "how such a grid is built"; its Section 7.2 only names the occupancy grid as one form of SLAM map. |
| F10 | Should fix | `src/content/blog/sampling-based-planning-prm-and-rrt.mdx` | Exercise 4 answer (line 470) | Technical accuracy | The grid search that "proves that no path exists" needs moves between cells that touch at a corner, which the grids of entry 2 forbid; the condition is not stated. |
| F11 | Should fix | `src/content/series/motion-planning.md` | Body (lines 14–16) | Purpose, audience and scope | The overview does not say what the series leaves out, although the entries exclude kinodynamic planning, trajectory optimization and moving obstacles. |
| F12 | Optional | all entries | In-text citations | Writing quality | Entry 1 cites as "(Author, year)"; entries 2–5 name authors in the prose, with or without a year. |
| F13 | Optional | `configuration-space-and-the-planning-problem.mdx`, `sampling-based-planning-prm-and-rrt.mdx` | Entry 1 Section 4.3 (line 318); entry 3 Section 5.3 (line 407) | Cross-article references | Two back-references are given without links: "(second entry)" for the 8-connected excess, and entry 3's tip-motion bound, which is entry 1's bound $D$. |
| F14 | Optional | entries 2, 4, 5 | Entry 2 line 130; entry 4 lines 126–152; entry 5 line 511 | Notation | Local reuse of series symbols: $d(u)$ beside the dimension $d$, $D$ (distance) beside entry 1's bound $D$, $s$ as the Laplace variable beside the path parameter $s$. |
| F15 | Optional | `src/content/blog/sampling-based-planning-prm-and-rrt.mdx` | Section 4.4 (lines 347, 358) | Writing quality | "r_n at n = 500: 1.000 m" is the cap at $\eta$, not the formula's 1.306 m, and the text does not say so. |
| F16 | Optional | `src/content/series/motion-planning.md` | Body (line 18) | Overview completeness | The shared conventions list $q$, $\mathcal{C}$, $\mathcal{C}_{\mathrm{free}}$, $\mathcal{C}_{\mathrm{obs}}$ but not $d$, $\sigma$ and $q(t) = \sigma(s(t))$, which entry 1 declares for the whole series. |

### F1. The PRM diagram overflows the text column

- **Where:** `src/content/blog/sampling-based-planning-prm-and-rrt.mdx:133–144`, Section 2.1 "A graph of random free configurations".
- **Text:** "```mermaid / flowchart LR / A[Sample q uniformly] --> B{Point check} ... G --> H[Query: join start and goal, search]"
- **Problem:** In `dist/blog/sampling-based-planning-prm-and-rrt.html` the figure carries `min-width:1005px` (60% of a natural width of about 1,675 px). The text column is about 612 px, so the diagram forces horizontal scrolling on every screen, and at 360 px the reader sees under a third of it. The skill's mechanical check treats a Mermaid width above about 600 px as a failure. The other four entries' diagrams are 188 to 407 px.
- **Recommended correction:** Change line 134 from `flowchart LR` to `flowchart TB` (the eight nodes then stack in one column), rebuild and confirm that the figure's `min-width` is at most 600 px. If the vertical form is too tall, split the chain into two rows with a subgraph, or drop node `G` and join `F` and the blocked branch directly to `H`. The italic caption at line 146 ("Everything before the query box is done once") stays true in either layout.

### F2. RRT*'s asymptotic optimality in the first entry

- **Where:** `src/content/blog/configuration-space-and-the-planning-problem.mdx:318`, Section 4.3 "Optimality guarantees".
- **Text:** "A PRM that joins every pair within a fixed radius is asymptotically optimal but expensive, and they introduced variants that are asymptotically optimal at lower cost (Karaman and Frazzoli, 2011); Section 4 of the third entry describes them."
- **Problem:** Entry 3, Section 4.3 (`sampling-based-planning-prm-and-rrt.mdx:333`), reports that Solovey, Janson, Schmerling, Frazzoli and Pavone (2020) found a gap in the 2011 proof for RRT* and proved asymptotic optimality for a radius shrinking as $(\log n / n)^{1/(d+1)}$, and its Summary repeats "RRT* proof needed a revised radius". Entry 1 attributes the guarantee to the 2011 paper without qualification, so the two entries tell the reader different things about who showed what.
- **Recommended correction:** "... and they introduced variants that are asymptotically optimal at lower cost (Karaman and Frazzoli, 2011); [Section 4 of the third entry](/blog/sampling-based-planning-prm-and-rrt#4-asymptotic-optimality-prm-and-rrt) describes them, including a later correction to the proof for RRT*."

### F3. D* Lite cited from two different papers

- **Where:** `src/content/blog/graph-search-dijkstra-and-a-star.mdx:400` and `:549`; `src/content/blog/path-tracking-and-reactive-avoidance.mdx:460` and `:556`.
- **Text:** entry 2: "**D* Lite**, by Koenig and Likhachev, produces the same paths with a simpler algorithm"; reference "S. Koenig and M. Likhachev, "Fast replanning for navigation in unknown terrain," *IEEE Transactions on Robotics*, vol. 21, no. 3, pp. 354–363, 2005." Entry 5: "D* Lite, introduced by Koenig and Likhachev in 2002 and described in Section 5.4 of the second entry"; reference "S. Koenig and M. Likhachev, "D* Lite," in *Proceedings of the Eighteenth National Conference on Artificial Intelligence (AAAI-02)*, pp. 476–483, 2002."
- **Problem:** The entry that treats D* Lite cites only the 2005 journal paper, while the entry that refers back to it dates the method to 2002 and cites the conference paper, which entry 2 does not list. A reader following entry 5's back-reference finds a different source and year. (Entry 5's fact-check states that the earlier entries cite Koenig and Likhachev "in the same form"; they cite a different work.) Both references are correct in themselves.
- **Recommended correction:** In entry 2, line 400, write "**D* Lite**, introduced by Koenig and Likhachev in 2002, produces the same paths with a simpler algorithm, and their journal account shows that it is at least as efficient as D*." Add to entry 2's references, in alphabetical position before the 2005 entry: "S. Koenig and M. Likhachev, "D* Lite," in *Proceedings of the Eighteenth National Conference on Artificial Intelligence (AAAI-02)*, pp. 476–483, 2002." Keep the 2005 reference, which supports the efficiency statement.

### F4. Khatib (1986) cited in two forms

- **Where:** `src/content/blog/path-tracking-and-reactive-avoidance.mdx:555`; compare `src/content/blog/configuration-space-and-the-planning-problem.mdx:549`.
- **Text:** entry 5: "... *The International Journal of Robotics Research*, vol. 5, no. 1, pp. 90–98, 1986."; entry 1: "... *International Journal of Robotics Research*, vol. 5, no. 1, pp. 90–98, 1986."
- **Problem:** The same work is cited differently. Every other reference in the series to this journal (Karaman and Frazzoli, LaValle and Kuffner, Geraerts and Overmars, Bobrow et al.) uses "International Journal of Robotics Research". All other references shared between entries (Choset et al., Dijkstra, Fox et al., Hart et al., Karaman and Frazzoli, Kavraki et al., LaValle, LaValle and Kuffner, Lozano-Pérez and Wesley, Lynch and Park) are identical.
- **Recommended correction:** Entry 5, line 555: "- O. Khatib, "Real-time obstacle avoidance for manipulators and mobile robots," *International Journal of Robotics Research*, vol. 5, no. 1, pp. 90–98, 1986."

### F5. $\rho$ as the disk radius in the second entry

- **Where:** `src/content/blog/graph-search-dijkstra-and-a-star.mdx:50`, Section 2.1 "Occupancy grids".
- **Text:** "For a disk robot of radius $\rho$ that can move in any direction, the first entry showed that the configuration-space obstacles are the workspace obstacles grown by $\rho$ ... marks every cell within $\rho$ of an occupied cell as blocked"
- **Problem:** The sentence summarizes entry 1, Section 3.1, where the disk radius is $r$ (lines 111–117, 140–166, Exercise 2), and entry 1, Section 2.2 (line 76), defines $\rho(q, q')$ as the distance on $\mathcal{C}$ that the series uses for path length. Entry 5 uses $\rho(p)$ for the distance to an obstacle (Khatib's notation, local to Section 5.2). Standards 5.5 and the skill's notation dimension ask for one symbol per quantity.
- **Recommended correction:** Replace the three occurrences of $\rho$ on line 50 by $r$: "For a disk robot of radius $r$ ... grown by $r$ ... marks every cell within $r$ of an occupied cell as blocked".

### F6. $\delta$ as the checking resolution in the third entry

- **Where:** `src/content/blog/sampling-based-planning-prm-and-rrt.mdx:36` (Section 1.2) and `:407` (Section 5.3).
- **Text:** "An edge check at resolution $\delta$ can miss an obstacle thinner than $\delta$"; "an edge checked at resolution $\delta$ can pass through an obstacle thinner than $\delta$ in configuration space."
- **Problem:** Entry 1, Section 5.5 (`configuration-space-and-the-planning-problem.mdx:420`), defines the **safety margin** $\delta$, the quantity by which obstacles are inflated, in the section the third entry relies on for collision checking. The two quantities are of the same kind (a small length in $\mathcal{C}$) and appear together in practice, so the clash can mislead.
- **Recommended correction:** Use $\varepsilon$ for the resolution in both places: line 36 "An edge check at resolution $\varepsilon$ can miss an obstacle thinner than $\varepsilon$"; line 407 "an edge checked at resolution $\varepsilon$ can pass through an obstacle thinner than $\varepsilon$ in configuration space."

### F7. The grid size is $m$ in the third entry and $N$ in the second

- **Where:** `src/content/blog/sampling-based-planning-prm-and-rrt.mdx:25` (Section 1.1) and `:487` (Summary).
- **Text:** "A grid with $m$ cells per axis has $m^d$ cells, and [Section 6.4 of the second entry](/blog/graph-search-dijkstra-and-a-star#64-the-curse-of-dimensionality) showed what that means"; Summary "not with $m^d$ cells".
- **Problem:** The linked section writes "A grid with $N$ cells along each of $d$ axes has $N^d$ cells" (`graph-search-dijkstra-and-a-star.mdx:452`), and its Summary and Section 6.3 use $N$ as well. The third entry restates the same formula with a new letter in the sentence that refers back to it.
- **Recommended correction:** Line 25: "A grid with $N$ cells per axis has $N^d$ cells, and ..."; line 487: "not with $N^d$ cells". ($N$ does not occur elsewhere in the third entry, whose sample count is $n$.)

### F8. "Configuration check" and "point check"

- **Where:** `src/content/blog/sampling-based-planning-prm-and-rrt.mdx:33`, Section 1.2; compare `src/content/blog/configuration-space-and-the-planning-problem.mdx:336`, Section 5.1.
- **Text:** entry 1: "a **configuration check**: does the robot at $q$ intersect an obstacle?"; entry 3: "a **point check**, which asks whether a single configuration $q$ is free, by placing the robot's geometry at $q$ and testing it against the obstacles in the workspace".
- **Problem:** The same query is defined in bold under two names, and the third entry, which then counts "point checks" throughout its results, never relates its term to the first entry's. Standards 5.3: one term, defined once, used consistently. Keeping entry 3's term is reasonable, since its tables are labeled with it; the link to the earlier term is what is missing.
- **Recommended correction:** Line 33: "- a **point check** (the configuration check of [Section 5.1 of the first entry](/blog/configuration-space-and-the-planning-problem#51-the-collision-checker-as-an-oracle)), which asks whether a single configuration $q$ is free, by placing ..."

### F9. The link to the state estimation entry overstates its content

- **Where:** `src/content/blog/graph-search-dijkstra-and-a-star.mdx:48`, Section 2.1.
- **Text:** "The [state estimation entry of the Introduction to Robotics series](/blog/sensing-and-state-estimation#72-localization-and-mapping) describes how such a grid is built while the robot localizes itself."
- **Problem:** The target section (`sensing-and-state-estimation.mdx:212`) defines localization, mapping and SLAM, and mentions the occupancy grid once, in a parenthesis, as one form the map can take ("an occupancy grid: a grid of cells over the floor plan, each holding the probability that it is occupied"). It does not describe how a grid is built. Entry 5, Section 6.4 (line 482), links the same section correctly, for pose estimation.
- **Recommended correction:** "The [state estimation entry of the Introduction to Robotics series](/blog/sensing-and-state-estimation#72-localization-and-mapping) names such a grid as one form of map in simultaneous localization and mapping, where the robot builds the map while it localizes itself."

### F10. The grid proof of infeasibility in the third entry

- **Where:** `src/content/blog/sampling-based-planning-prm-and-rrt.mdx:470`, answer to Exercise 4.
- **Text:** "A search on a coarse grid also counts, provided its cells are marked blocked only when every configuration in them is in collision; a failure of that search proves that no path exists."
- **Problem:** The conclusion holds only if the search may also move between cells that touch at a single corner: a free path can pass from one cell to a diagonal neighbor through their common corner while both side cells are entirely blocked. The grids of the second entry forbid exactly that move (Section 2.2, line 54, "allows it only when both of those cells are free"), and they mark cells at their centers (Section 6.3, line 431), not over the whole cell, so a reader who applies the answer to the grid planner of the series would draw a false conclusion. It also reads against entry 1, Exercise 5 (line 503), and entry 2, Section 6.1, which say that a grid failure does not prove that no path exists, without saying how this grid differs.
- **Recommended correction:** "A search on a coarse grid also counts, provided its cells are marked blocked only when every configuration in them is in collision (a test over the whole cell, unlike the center test of [Section 6.3 of the second entry](/blog/graph-search-dijkstra-and-a-star#63-a-grid-over-the-arms-configuration-space)) and it may move between any two cells that touch, even at a single corner; a failure of that search proves that no path exists. The grid planners of the second entry, which test cell centers and forbid corner moves, give no such proof."

### F11. The overview does not state what the series leaves out

- **Where:** `src/content/series/motion-planning.md:14–16`.
- **Text:** "This series is for engineers and students who want to understand how a robot decides where to move ..." through "... with reactive methods that avoid obstacles the plan did not know about."
- **Problem:** The overview gives the reader, the prerequisites and the sequence rationale, but not the scope boundary that the entries draw: entry 4, Section 1.1 (line 26), "kinodynamic planning ... this entry does not treat it"; entry 3, Section 5.3 (line 408), differential constraints "beyond this entry"; entry 1, Section 6 (line 456), trajectory optimization "The series does not treat it in depth"; entry 5, Section 6.4 (line 481), moving obstacles remain open; and tracking is treated for the mobile robot only, not for the arm. The skill's purpose-and-scope dimension asks the overview to say what the series covers and leaves out, so that a reader looking for one of these topics knows before starting.
- **Recommended correction:** Add at the end of line 16: "The series treats static obstacles and plans geometry first and timing second; it does not treat planning with dynamics or differential constraints (kinodynamic planning), trajectory optimization beyond a mention in the first entry, moving obstacles, or tracking control of arms."

### F12. In-text citation style (optional)

- **Where:** e.g. `configuration-space-and-the-planning-problem.mdx:31` "(Schwartz and Sharir, 1983)" against `graph-search-dijkstra-and-a-star.mdx:400` "by Koenig and Likhachev" and `path-tracking-and-reactive-avoidance.mdx:193` "In 1990 Kanayama, Kimura, Miyazaki and Noguchi proposed".
- **Problem:** The standards fix the reference list, not the in-text form. Entry 1 cites with parenthetical author and year; entries 2–5 name authors in the prose, sometimes with a year. This is polish.
- **Recommended correction:** Choose one form for the series when the entries are next revised.

### F13. Two back-references without links (optional)

- **Where:** `configuration-space-and-the-planning-problem.mdx:318`; `sampling-based-planning-prm-and-rrt.mdx:407`.
- **Text:** "which an 8-connected grid cannot do for most straight lines (second entry)"; "a joint-space step of 0.02 rad moves the tip of the arm by at most $0.02 \times \sqrt{1.7^2 + 0.7^2} = 0.037$ m between checks (1.7 m is the lever arm of the shoulder, 0.7 m that of the elbow)".
- **Problem:** Both rely on an earlier or later section without linking it. The second is entry 1's bound $D = (l_1 + l_2)|\Delta\theta_1| + l_2|\Delta\theta_2|$ (Section 5.3) maximized over a joint-space step of Euclidean length 0.02 rad; recomputed, 0.03677 m. Entry 4, Section 6.2, links the same bound.
- **Recommended correction:** Entry 1: "(Section 2.2 of the [second entry](/blog/graph-search-dijkstra-and-a-star#22-connectivity-and-edge-costs))". Entry 3, after "that of the elbow)": "; this is the bound $D$ of [Section 5.3 of the first entry](/blog/configuration-space-and-the-planning-problem#53-a-check-that-cannot-miss) for the worst direction of the step".

### F14. Local reuse of series symbols (optional)

- **Where:** `graph-search-dijkstra-and-a-star.mdx:130` ($d(u)$, the cheapest cost to $u$, in the entry that also uses the dimension $d$ in Section 6.4); `trajectories-and-time-scaling.mdx:126–152` ($D$, the distance of a move, while Section 6.2 uses entry 1's bound, which entry 1 calls $D$); `path-tracking-and-reactive-avoidance.mdx:511` ($s$ as the variable of the characteristic polynomial, while $s$ is the path parameter of entry 4 and $s_{\mathrm{hit}}$ an arc length in entry 5).
- **Problem:** Each use is defined locally and causes no error, but each puts a second meaning on a symbol the series uses.
- **Recommended correction:** If the entries are revised: $\operatorname{dist}(u)$ or $g^*(u)$ in entry 2, Section 3.2 (entry 2 already uses $g^*$ in Section 4.2); $\Delta$ or $L$ for the distance in entry 4, Section 3 (or leave $D$ and do not name the bound in Section 6.2, as now); $\lambda$ for the polynomial variable in entry 5, Exercise 3.

### F15. The capped radius in the third entry's output (optional)

- **Where:** `sampling-based-planning-prm-and-rrt.mdx:347` and `:358`, Section 4.4.
- **Text:** "r_n at n = 500: 1.000 m"; "The radii are those for a tree of $n$ vertices; the tree of RRT* has slightly fewer vertices than iterations, because blocked extensions add none."
- **Problem:** The formula of Section 4.2 gives $11.71 \times (\log 500/500)^{1/2} = 1.306$ m; the printed 1.000 m is the cap at $\eta = 1.0$ m from Section 4.3. A reader checking the line against Exercise 1's method gets a different number.
- **Recommended correction:** "The radii are those for a tree of $n$ vertices, capped at $\eta = 1.0$ m (the formula gives 1.306 m at $n = 500$); the tree of RRT* has ..."

### F16. Shared notation in the overview (optional)

- **Where:** `src/content/series/motion-planning.md:18`.
- **Text:** "A configuration is written $q$, the configuration space $\mathcal{C}$, its free part $\mathcal{C}_{\mathrm{free}}$ and its obstacle region $\mathcal{C}_{\mathrm{obs}}$."
- **Problem:** Entry 1's Conventions (line 19) declare for the whole series also the dimension $d$, the path $\sigma$ and the trajectory $q(t) = \sigma(s(t))$, which entries 3, 4 and 5 use. Standards 6.5 ask the overview for the shared conventions "when they matter".
- **Recommended correction:** Append: "The dimension of $\mathcal{C}$ is $d$; a path is $\sigma : [0, 1] \to \mathcal{C}_{\mathrm{free}}$, and a trajectory is $q(t) = \sigma(s(t))$ with a time scaling $s(t)$."

## Concept introduction map

| Concept | First used (path:line) | Introduced where (path:line, or "not introduced") | Assessment |
|---|---|---|---|
| Motion planning, motion planner | `configuration-space-and-the-planning-problem.mdx:15` | same, `:15`, `:25` | Good |
| Configuration, configuration space, degrees of freedom | `configuration-space-and-the-planning-problem.mdx:15` | same, `:51` | Good |
| Topology, $S^1$, torus | `configuration-space-and-the-planning-problem.mdx:65` | same, `:65–71` | Good |
| Distance on $\mathcal{C}$ | `configuration-space-and-the-planning-problem.mdx:73` | same, `:73–79` | Good; symbol reused in entry 2 (F5) |
| Workspace, forward kinematics | `configuration-space-and-the-planning-problem.mdx:83` | same, `:83–91`, with the kinematics entry linked | Good |
| C-obstacle, Minkowski sum | `configuration-space-and-the-planning-problem.mdx:95` | same, `:95–117` | Good |
| Clearance | `configuration-space-and-the-planning-problem.mdx:187` | same; restated in `graph-search-dijkstra-and-a-star.mdx:94`, `sampling-based-planning-prm-and-rrt.mdx:430` | Acceptable (short reminders) |
| Completeness (three strengths), optimality (three strengths) | `configuration-space-and-the-planning-problem.mdx:308`, `:318` | same | Good; used consistently in entries 2 and 3 |
| PSPACE | `configuration-space-and-the-planning-problem.mdx:324` | same | Good |
| Collision checker, configuration and edge checks | `configuration-space-and-the-planning-problem.mdx:334` | same; renamed in entry 3 (F8) | F8 |
| Graph, frontier, closed set, expansion | `graph-search-dijkstra-and-a-star.mdx:19`, `:27` | same | Good (graph and queue stated as prerequisites, `:17`) |
| Occupancy grid, inflation, resolution | `graph-search-dijkstra-and-a-star.mdx:48` | same, `:48–50` | Good; link wording F9 |
| Admissible and consistent heuristics | `graph-search-dijkstra-and-a-star.mdx:223` | same, `:227`, `:237` | Good |
| Visibility graph | `configuration-space-and-the-planning-problem.mdx:450` | same; developed `graph-search-dijkstra-and-a-star.mdx:86` | Good |
| Curse of dimensionality | `graph-search-dijkstra-and-a-star.mdx:452` | same | Good; symbol restated in entry 3 (F7) |
| PRM, RRT, Voronoi bias | `configuration-space-and-the-planning-problem.mdx:318` (named) | `sampling-based-planning-prm-and-rrt.mdx:129`, `:217`, `:223` | Good |
| Expansiveness | `sampling-based-planning-prm-and-rrt.mdx:303` | same | Good |
| Homotopy class | `sampling-based-planning-prm-and-rrt.mdx:426` | same | Good |
| Time scaling, path speed, jerk | `configuration-space-and-the-planning-problem.mdx:19` (announced) | `trajectories-and-time-scaling.mdx:18`, `:37`, `:39` | Good |
| Phase plane, velocity limit curve | `trajectories-and-time-scaling.mdx:202`, `:208` | same | Good |
| Cubic spline, knots, tridiagonal system | `trajectories-and-time-scaling.mdx:297` | same, `:297–315` | Good |
| Jacobian | `trajectories-and-time-scaling.mdx:16`, `:252` | kinematics entry, linked at `:16` | Good |
| Unicycle model, nonholonomic constraint | `configuration-space-and-the-planning-problem.mdx:59` (announced) | `path-tracking-and-reactive-avoidance.mdx:53`, `:63`, with What Is a Robot? linked | Good |
| Feedback, damping ratio, natural frequency | `path-tracking-and-reactive-avoidance.mdx:156` | Foundations of Control Systems, stated as prerequisite (overview `:14`, entry 5 `:17`) | Good |
| Potential field, local minimum, navigation function | `path-tracking-and-reactive-avoidance.mdx:268`, `:340`, `:344` | same | Good |
| Dynamic window, admissible velocity | `path-tracking-and-reactive-avoidance.mdx:348` | same | Good |
| Cost map, D* Lite | `graph-search-dijkstra-and-a-star.mdx:400`; `path-tracking-and-reactive-avoidance.mdx:456` | entry 2 `:400–404`; entry 5 refers back | Good; references F3 |

## Versions, defaults and conventions

| Assumption | Where it appears | Stated in the text? | Assessment |
|---|---|---|---|
| Python 3.13, NumPy 2.5 | Overview `:18`; every entry's Conventions (entry 2: standard library plus NumPy where needed; entry 4: no SciPy) | Yes | Consistent |
| SI units; radians in computation, degrees only in text and tables | Overview; entry 1 `:19`; entries 3, 4, 5 | Yes | Consistent; entry 2 grid costs in cell sizes, stated (`:21`) |
| Right-handed frames; $x$ right, $y$ up | Overview; entry 1; entry 3 map (`:47`); entry 5 `:19` | Yes | Consistent; entry 2's printed maps put row 0 at the top and $(x, y) =$ (column, row), stated (`:21`, `:94`) |
| Two-link arm $l_1 = 1.0$ m, $l_2 = 0.7$ m, $\theta_2$ relative | All entries that use the arm (1, 2, 3, 4) and the overview | Yes | Consistent; reachable ring 0.3–1.7 m in entries 1 (`:91`) and 4 (`:254`) |
| Arm without joint limits: torus, angle differences wrapped to $(-\pi, \pi]$ | Entry 1 `:67–69`; entry 2 `:431`; entry 3 `:73`; entry 5 heading wrap `:181` | Yes | Consistent; entry 4 adds joint ranges for its check (`:397`), stated |
| Touching counts as collision ($\mathcal{C}_{\mathrm{free}}$ open; clearance $\le 0$ collides) | Entry 1 `:101`, `:187`; entry 2 `:431`; entry 3 `:73` | Yes | Consistent |
| Path length as cost, in radians for the arm (unit weights) | Entry 1 `:302`; entry 2 `:433`; entry 3 `:19` | Yes | Consistent |
| Determinism and seeds | Overview `:18`; entries 1, 4, 5 deterministic; entry 2 one seeded map; entry 3 seeds stated per experiment | Yes | Consistent |
| Natural logarithms | Entry 3 `:19` | Yes | Good |
| Limits $v_{\max} = 1.0$ rad/s, $a_{\max} = 2.0$ rad/s², $j_{\max} = 10$ rad/s³, illustrative | Entry 4 `:18` | Yes | Good |
| Differential-drive robot $r = 0.05$ m, $b = 0.30$ m; 20 Hz control, 0.1 s lag | Entry 5 `:81`, `:93` | Yes | Good |
| Pose estimate taken as exact | Entry 5 `:17`, `:482` | Yes | Good |

## Series design

**Purpose, audience and scope.** The overview names the reader (engineers and students), the prerequisites (the two-link arm and frames of Introduction to Robotics, linear algebra and calculus, Python, feedback from Foundations of Control Systems) and what the reader can do at the end (five checkable objectives, each met by a named entry). The claim that the Introduction to Robotics series "ends by naming motion planning" holds (`sensing-and-state-estimation.mdx:269`). The overview does not say what the series leaves out (F11).

**Sequence rationale.** The order, from the abstract statement in configuration space to the robot's wheels, is stated and is the right one for the reader: entry 2's curse of dimensionality motivates entry 3, entry 3's paths with corners motivate entry 4, and entry 4's check with tracking error leads to entry 5. Each closing paragraph names the next entry, and entry 5's returns to the objectives, as standards 6.2 require.

**Prerequisites and dependencies.** Nothing depends on a later entry. Forward mentions in entry 1 (grids, sampling, time scaling, nonholonomic motion, reactive methods) are announcements with the material delivered later, and each is kept: entry 2 Section 6 (resolution), entry 3 Sections 4 and 5 (optimal variants, narrow passages), entry 4 Section 6 (checking a timed path), entry 5 Sections 2.2 and 5 (nonholonomic constraint, potential fields and DWA with their local minima).

**Notation and depth.** The series notation declared in entry 1 is kept by every entry. The exceptions are local reuses of $\rho$, $\delta$ and the grid size (F5–F7) and minor ones (F14). Depth is comparable: every entry has derivations, programs run with real output, a limits discussion, exercises with answers, a summary table and references.

**Overview completeness.** The description and body match what the entries deliver, including the conventions paragraph, which agrees with every entry's Conventions; it omits part of the shared notation (F16) and the scope boundary (F11).

## Series-level notes

Cross-reference map (all links resolve, checked by `check:links`, and each target section was read):

| From | To | Claim | Holds |
|---|---|---|---|
| E1 §3.1 | E2 §6 | the limit of grids for narrow strips | Yes (§6.1) |
| E1 §4.2 | E3 §5 | narrow passages slow probabilistically complete planners | Yes |
| E1 §4.3 | E2; E3 §4 | 8-connected grids; PRM* and RRT* | Yes; attribution F2 |
| E1 §5.5 | E4 §6 | a timed path is checked again | Yes (§6.1–6.3) |
| E1 §6 table and text | E2, E3, E4, E5 | visibility graphs, smoothing, time scaling, potential fields and DWA | Yes |
| E2 opening, §2.1, §6.1, §6.3 | E1 §3, §4, §5, §3.3 | Minkowski inflation, guarantees, check risks, walls | Yes |
| E2 §2.1 | Sensing and State Estimation §7.2 | how an occupancy grid is built | No (F9) |
| E2 §5.4, §6.2 | E5 §6; E4; E5 | replanning; profiles; tracking under the constraint | Yes |
| E3 opening, §1.1, §1.4 | E2 §6, §6.4, §2.3 | limits of grids; visibility graph | Yes |
| E3 §1.2, §1.3, §4.1 | E1 §5, §4.2, §4.3 | edge checks; completeness; asymptotic optimality | Yes; term F8 |
| E3 §4.5, §6.2, end | E4 | corners need timing | Yes (§5.1) |
| E4 opening | E3 §6; E1 §4; kinematics §5 | shortened paths as input; path; Jacobian | Yes |
| E4 §6.1, §6.2 | What Is a Robot? §4; E1 §5, §3.2, §5.3 | planner assumes the trajectory is followed; clearance; motion bound | Yes |
| E4 §6.3, end | E5 | controllers that keep the tracking error small | Yes |
| E5 opening, §1, §2.2, §4.1, §6.1, §6.2 | E1–E4; What Is a Robot? §2.2, §4, §5, §5.3 | layers, nonholonomic, $q(t) = \sigma(s(t))$, cost map, D* Lite | Yes; reference F3 |

Repeated material that is deliberate and short: the series notation in each Conventions paragraph (standards 6.2), clearance restated as a reminder in entries 2 and 3, and the visibility graph met in entries 1, 2 and 3 (each building on the previous). No explanation is repeated at length; entry 5 refers back to entry 2 for D* Lite, as its own developmental review required.

Facts stated in more than one entry agree: the 8-connected excess of 8.24% (entry 2, Sections 2.2 and 6.2, and Exercise 1); $10^{12}$ cells for six joints at 100 cells per joint (entries 2 and 3); the definitions of asymptotic optimality and of the non-optimality of RRT and fixed-$k$ PRM (entries 1 and 3); positive clearance as the condition of probabilistic completeness (entries 1 and 3); D* Lite's backward search and the cheapness of repairs near the robot (entries 2 and 5); the arm's motion bound (entries 1, 3 and 4).

Structure and tone are uniform: numbered sections, a Conventions paragraph, programs with real output, Exercises with answers, a Summary table and References in every entry.

## Verification log

- `npm run build:local`: exit 0 (astro check 0 errors, 0 warnings; Pagefind "Indexed 2 languages", "Indexed 121 pages"; check-site-url warns about localhost URLs, as expected for a local build).
- `npm run check:links`: "Checked 356 pages and 11152 internal references in dist. All internal links resolve."
- Mermaid widths in `dist/blog/<slug>.html`: entry 1 369px; entry 2 407px and 188px; entry 3 1005px (F1); entry 4 none; entry 5 320px.
- Glued inline elements: none in the five pages (letters or punctuation glued to or after `<a `, `<code>`, `<strong>`, `<em>`, outside KaTeX, code blocks and SVG).
- Cross-entry recomputations (reviewer's runs, Python 3):
  - Entry 1: grown 1.6 m square at $r = 0.45$ m, 6.0762 m²; Exercise 2, 2.4827 m²; $\arcsin(0.2) = 11.54^\circ$; $36^6 = 2.18 \times 10^9$, $36^7 = 7.84 \times 10^{10}$; Exercise 4 ($D = 1.13$, step 0.0442).
  - Entry 2: band of the first link 0.3673 to 0.7136 rad for the obstacle at (1.0, 0.6) m, center 1.1662 m from the base; ratios 1.0590 (grid against visibility graph), 20.7% (8- against 4-connected), 1.074, 1.105 and 1.244 for weighted A*; Exercise 5 (729 kB, 4.25 TB, 66 GB).
  - Entry 3: $\gamma = 11.710$ m; $r_n = 0.973$, 0.722, 0.533 m at $n = 1000$, 2000, 4000 and 1.306 m at 500 (printed 1.000 m, the cap; F15); $k(n) = 31, 34, 38, 42$; RRT and RRT-Connect medians 37% and 32% above $C^*$, PRM 6.9%; door probabilities 1.1% and 0.14%; tip bound 0.0368 m (consistent with entry 1's $D$); the three disks lie 1.110, 1.053 and 1.023 m from the base at their nearest points, beyond the 1.0 m first link, as stated.
  - Entry 4: forward kinematics of the four waypoints, (1.065, 0.195), (0.774, 0.662), (0.666, 1.246), (0.520, 1.541) m.
  - Entry 5: Exercise 1 wheel speeds 4.2 and 7.8 rad/s; Exercise 4 root $\rho = 0.5898$ m, stopping point 5.41 m.
- Cross-entry text checks: What Is a Robot? Sections 2.2, 4, 5 and 5.3 and Sensing and State Estimation Section 7.2 were read against every sentence that cites them (all hold except F9); the per-item audits in `editorial/audit/items/` were read for D* Lite, Khatib and the diagrams.
- Not verified: the full-length program outputs of each entry (rerun by the per-item technical reviews, recorded in `editorial/audit/items/<slug>.md`, and not repeated here); the primary texts of Koenig and Likhachev (2002, 2005), whose attributions the per-item fact-checks verified from abstracts. Vietnamese translations: none exists for this series.
