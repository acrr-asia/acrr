# Editorial review: Configuration Space and the Motion Planning Problem

- Path: `src/content/blog/configuration-space-and-the-planning-problem.mdx` · Route: `/blog/configuration-space-and-the-planning-problem` · Type: article · Series `motion-planning`, entry 1 of 5
- Stages in this report: developmental edit (EOS 6.1) and copy edit (EOS 6.2), 2026-10-17. Editor: developmental-editor and copy-editor roles (not the author of the draft).
- Prose length: about 6,150 words by a count that drops front matter, code, display math, tables and references (about 6,200 before the edit); the series standard is 3,500 to 6,000 words of prose, and the exercises' answers account for the excess.
- Lint at hand-off: 6 errors, 0 warnings, 2 suggestions. All six errors are expected while entry 3 is being written and are not defects of this file: `internal-link` and `series-crossref` on the link to `/blog/sampling-based-planning-prm-and-rrt#5-narrow-passages-and-other-failure-modes` (line 314; the fragment matches the fixed `## 5. Narrow passages and other failure modes` heading in BRIEF.md), and four `series-crossref` errors on "fifth entry" (lines 27, 59, 448, 458), which the linter counts against the four entries that exist now. Re-run lint once entry 3 exists; these must then clear.
- Build check: `astro build --outDir /tmp/claude-0/mp/edit-build-1` exit 0; `check-links` on that build reports only the entry 3 link above for this page; no letter glued to an inline element in the built HTML. The build directory was deleted.

## Developmental review

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| D1 | Should fix | `:35`, `:460` (old), `:538` (old) | structure | The hand-off to the fourth and fifth entries was explained three times (Section 1.2, end of Section 6, closing paragraph). |
| D2 | Should fix | `:282`, Section 3.3 | structure | The last paragraph of Section 3.3 gave away the answer to Exercise 6. |
| D3 | Should fix | `:326`, Section 4.4 | evidence | Two Canny works of 1988 are cited; the inline citation of the STOC paper was an awkward, partly expanded venue name. |
| D4 | Should fix | `:536`, Section 8 | consistency | The closing paragraph called the collision checker "the planner's only window" on the space, which contradicts Section 6 (combinatorial planners compute $\mathcal{C}_{\mathrm{free}}$ exactly). |
| D5 | Optional | `:51`, Section 2.1 | purpose | "DOF" was defined and never used; the reference to the prerequisite entry's count of degrees of freedom was unlinked. |
| D6 | Should fix, for the technical reviewer and fact-checker | `:318`, Section 4.3 | accuracy | "Karaman and Frazzoli showed that the basic sampling-based planners are not asymptotically optimal" may overgeneralize. Left unchanged. |
| D7 | Should fix, for the technical reviewer | `:304`, Section 4.1 | accuracy | "A shortest path among obstacles touches them" holds only when the obstacles block the straight segment. Left unchanged. |
| D8 | Optional, for the fact-checker | `:53`, Section 2.1 | evidence | Check that the attribution of the configuration-space formulation to Lozano-Pérez (1983) does not read as a claim of priority. Left unchanged. |

### D1. The later layers explained three times
- **Where:** `:35` Section 1.2; Section 6 (last paragraph, now deleted); `:536` Section 8.
- **Text:** "Two further stages turn a path into motion: the fourth entry adds velocity and acceleration profiles, and the fifth tracks the timed path with feedback inside a layered navigation system."
- **Problem:** Section 1.2 already states what the fourth and fifth entries add, and the Mermaid diagram of Section 6 shows the same pipeline. Standards 6.1 ("No redundancy").
- **Correction (applied):** Deleted the final paragraph of Section 6. Tightened the Section 1.2 paragraph to "The statement is deliberately narrow: it assumes exact, static models ... Later layers add what it leaves out. The fourth entry times a path so that it respects velocity and acceleration limits, and the fifth follows a path on a wheeled robot whose motion is constrained and avoids obstacles that the map did not contain. Each layer starts from a collision-free geometric path."

### D2. Section 3.3 answered Exercise 6
- **Where:** `:282`, section "3.3 Free space can come apart".
- **Text:** "The wrap-around matters too. On a square whose edges are not glued, the free space of a single disk at $(0.5, 0)$ m splits into two pieces, left and right of the wall at $\theta_1 = 0$; on the torus they are one region, joined through $\theta_1 = \pm 180^\circ$ (Exercise 6)."
- **Problem:** The paragraph states the full answer to Exercise 6, which the exercise's answer then repeats with the program output. Standards 6.1 (earned elements, no redundancy).
- **Correction (applied):** "The labeling also depends on the wrap-around; Exercise 6 asks what a single disk at $(0.5, 0)$ m does to the free space when the edges of the grid are not glued." The argument is now made once, in the answer, with its output.

### D3. Two Canny 1988 citations
- **Where:** `:326`, section "4.4 How hard the problem is".
- **Text:** "(Canny, 1988, at the Symposium on Theory of Computing of the Association for Computing Machinery)"
- **Problem:** The reference list has two Canny items of 1988; the inline form disambiguated them by venue, in a long parenthesis, while the roadmap citation two sentences later disambiguates by title. Inconsistent and hard to read.
- **Correction (applied):** "Canny later showed, in his 1988 paper on algebraic and geometric computations in PSPACE, that it can be decided in polynomial space, so it is PSPACE-complete." The cited work and the claim are unchanged; both Canny citations now identify the work by its title.

### D4. "Only window" in the closing paragraph
- **Where:** `:536`, section "8. Summary".
- **Text:** "The collision checker is the planner's only window on that space, and what a planner guarantees depends on how it looks through that window."
- **Problem:** Section 6 (`:450`) says combinatorial planners "compute an exact representation of $\mathcal{C}_{\mathrm{free}}$"; Section 5.1 limits the "only access" claim to sampling-based planners. The metaphor also restated Section 5.1 in vaguer form.
- **Correction (applied):** "Apart from the combinatorial methods, planners see that space only through collision queries, and what a planner guarantees depends on where and how finely it makes them." The lead to the next entry was kept and joined into one sentence.

### D5. Degrees of freedom
- **Where:** `:51`.
- **Text:** "the robot's number of **degrees of freedom** (DOF), as the first entry of the Introduction to Robotics series counted them."
- **Correction (applied):** Removed the unused "(DOF)" and linked the prerequisite section: "as [Section 2.2 of What Is a Robot?](/blog/what-is-a-robot#22-degrees-of-freedom-and-mobility) counted them." Fragment checked against the built page (`id="22-degrees-of-freedom-and-mobility"`).

### D6. Which sampling-based planners are not asymptotically optimal (for the technical reviewer and fact-checker)
- **Where:** `:318`, section "4.3 Optimality guarantees".
- **Text:** "Karaman and Frazzoli showed that the basic sampling-based planners are not asymptotically optimal and introduced variants that are (Karaman and Frazzoli, 2011)"
- **Problem:** As the editor reads Karaman and Frazzoli (2011), the negative results concern RRT and the k-nearest PRM with a fixed $k$, while a PRM with a fixed connection radius is asymptotically optimal but costly. "The basic sampling-based planners" may therefore claim more than the paper shows. Not verified against the paper in this stage.
- **Correction (proposed, not applied):** If confirmed: "Karaman and Frazzoli showed that RRT and the PRM that connects each sample to a fixed number of neighbors are not asymptotically optimal, and introduced variants that are (Karaman and Frazzoli, 2011)". Keep consistent with Section 4 of the third entry.

### D7. Shortest paths touch obstacles (for the technical reviewer)
- **Where:** `:304`, section "4.1 Feasibility, cost and optimality".
- **Text:** "A shortest path among obstacles touches them: around a polygon in the plane, it runs straight to a vertex and straight on."
- **Problem:** True when the straight segment from start to goal is blocked; when it is free, the shortest path touches nothing, and the next sentence ("no shortest path exists in the open set") also holds only in the blocked case.
- **Correction (proposed, not applied):** "When obstacles block the straight line, a shortest path touches them: ..." and "... no shortest path then exists in the open set ...".

### D8. Attribution of the configuration-space formulation (for the fact-checker)
- **Where:** `:53`.
- **Text:** "Lozano-Pérez formulated spatial planning as a search in the space of configurations and gave algorithms for computing its obstacle regions for polygons and polyhedra (Lozano-Pérez, 1983)."
- **Problem:** The sentence does not claim priority, and the 1983 paper is the standard citation. Earlier uses of the idea exist (Lozano-Pérez and Wesley, 1979, is in the reference list). Confirm that the wording is accurate for the 1983 paper's content (polygons and polyhedra).
- **Correction:** None proposed unless the fact-checker finds a mismatch.

### Assessment

- **Purpose and reader:** the opening links the series and the three prerequisite entries, states what the entry covers and gives a full **Conventions** paragraph (shared notation, units, radians, Python 3.13 and NumPy 2.5, determinism). Depth suits the series reader.
- **Concepts before mechanics:** each concept (configuration, topology, distance, C-obstacle, Minkowski sum, clearance, completeness, PSPACE, bounding volumes) is defined before its formula or code.
- **Progression:** problem, configuration space, obstacles, guarantees, collision checking, map of methods, exercises, summary. Matches the fixed outline and Standards 6.2. Section 3.4 sets up the move to implicit representations that Section 5 delivers.
- **Evidence:** the grids and edge-check figures are program output (scratch programs and `run.sh` in `/tmp/claude-0/mp/configuration-space-and-the-planning-problem/`); the clearance bound is derived. The editor spot-checked by hand: the area formula ($2.56 + 2.88 + 0.6362 = 6.0762$), the corridor strip (0.3 m), the cell counts 180 and 240, $\arcsin(0.2) = 11.54^\circ$, the contact window ($\arcsin(0.03/1.65) = 1.042^\circ$), the 0.05 rad sample angles $8.57^\circ$ and $11.43^\circ$, the 62nd check at 0.02 rad, $D = 3.5605$, Exercise 2 and Exercise 4. All agree. Recomputation of the program outputs is left to the technical review.
- **Earned elements:** the ASCII grids show the shapes of C-obstacles and the split free space, which prose cannot. The Mermaid diagram shows the pipeline order and the table compares guarantees, so they are not duplicates. The six exercises test separate skills.
- **Ending:** the summary table plus a closing paragraph that leads to the second entry (linked).

### What changed (developmental)

- Deleted the last paragraph of Section 6 and tightened Section 1.2 (D1).
- Replaced the wrap-around paragraph of Section 3.3 with a pointer to Exercise 6 (D2).
- Rewrote the Canny PSPACE sentence (D3).
- Rewrote the closing paragraph's middle sentence and joined its lead to the next entry (D4).
- Linked `/blog/what-is-a-robot#22-degrees-of-freedom-and-mobility` and removed "(DOF)" (D5).
- No `##` or `###` heading was renamed or renumbered, so no fragment changed. Other entries link to `#3-obstacles-in-configuration-space`, `#33-free-space-can-come-apart`, `#4-paths-cost-and-what-a-planner-guarantees` and `#5-collision-checking`, and all of them still resolve.

**Developmental verdict: pass.** D1 to D5 are applied. D6 to D8 are routed to the technical review and the fact-check, and those stages must close them.

## Copy edit

Tools: `npm run eos -- lint` (before: 6 errors, all expected, see above; 0 warnings; 2 suggestions) and `npm run eos -- fix --rules spelling-variant,terminology` (0 fixes applied). Manual checks: no em dash, contraction, "simply", "obviously", "clearly" or "of course" anywhere; "we" appears only in the derivation step of Section 5.3 ("We differentiate with respect to time"); no serial comma found (every ", and" or ", or" joins clauses); headings are in sentence case and numbered in sequence; abbreviations (IK, BVH, GJK, PSPACE, PRM, RRT, CHOMP) are expanded at first use.

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| C1 | Should fix | `:31`, Section 1.2 | language | Generic opener "has a memorable name" and a three-part sentence with a clause that adds nothing. |
| C2 | Should fix | `:53`, Section 2.1 | language | "In motion planning, Lozano-Pérez formulated planning ...": redundant frame. |
| C3 | Should fix | `:101`, Section 3 | language | "can differ greatly ... Three examples show how": vague intensifier and stock transition. |
| C4 | Optional | `:17`, `:19` | language | Wordy prose outline in the opening and the determinism sentence. |
| C5 | Optional | `:71`, `:117`, `:408`, `:412`, `:426` | language | Small wording fixes: "Textbook treatments include", "This is why", "dearer than", "impossibly slow", "flows ... toward motion". |
| C6 | Optional | References `:540`, `:541` | language | Lint suggestions on "MIT" and "ACM". Kept. |

### C1. Opener of Section 1.2
- **Text:** "The purely geometric core of the task has a memorable name. A grand piano carried through the doors of a house can turn as well as slide, its shape matters and a sequence of small rotations is often the only way through."
- **Correction (applied):** "The geometric core of the task is named after moving furniture. A grand piano carried through the doors of a house can turn as well as slide, and a sequence of small rotations is often the only way through."

### C2. Redundant frame
- **Text:** "In motion planning, Lozano-Pérez formulated planning as a search in the space of configurations"
- **Correction (applied):** "Lozano-Pérez formulated spatial planning as a search in the space of configurations" ("spatial planning" is the term of the cited paper's title).

### C3. Section 3 introduction
- **Text:** "The definition is simple, but the shape of $\mathcal{C}_{\mathrm{obs}}$ can differ greatly from the shape of $\mathcal{O}$. Three examples show how."
- **Correction (applied):** "The definition is short, but $\mathcal{C}_{\mathrm{obs}}$ can look nothing like $\mathcal{O}$, as the three examples below show."

### C4. Opening and Conventions
- **Text:** "It covers the configuration space and its shape, how obstacles become obstacles in that space, what feasibility, optimality and completeness mean, how collisions are checked and how the planning methods of the later entries fit together." / "Every program in this entry is deterministic, so no random seed is involved, and every quoted output comes from running it."
- **Correction (applied):** "It builds the configuration space and its obstacles, defines what a planner can guarantee, shows how collisions are checked and places the methods of the later entries on one map." / "The programs are deterministic, so no random seed is needed, and every quoted output comes from running them."

### C5. Small wording fixes (applied)
- `:71` "Textbook treatments include Chapter 2 of ..." → "Chapter 2 of Lynch and Park (2017), Chapter 4 of LaValle (2006) and Choset et al. (2005) treat these spaces in detail."
- `:117` "This is why mobile-robot software inflates ..." → "Mobile-robot software relies on this result when it inflates ..."
- `:408` "it needs a distance query, dearer than a yes-or-no test, and a velocity bound" → "it needs two things a fixed-step check does not: a distance query, which costs more than a yes-or-no test, and a velocity bound"; "said the same about" → "gave the same answer for".
- `:412` "would make planning impossibly slow" → "would be far too slow for planning".
- `:426` "shows how a problem flows through them toward motion; the table compares them" → "shows how a problem passes through them on its way to motion, and the table compares them".

### C6. Lint suggestions kept
- `acronym-expansion` "MIT" (`:540`): it is part of the publisher's name "MIT Press" in a reference entry, which the house reference format (Standards 7.3) gives as the publisher writes it.
- `acronym-expansion` "ACM" (`:541`): it is part of the proceedings title "ACM Symposium on Theory of Computing (STOC)" in a reference entry. After D3 the body no longer names the venue.

### What changed (copy)

- Wording only, by category: generic openers and transitions (C1, C3), redundancy (C2), concision (C4, C5). No technical claim, number, equation, code block, quoted output, unit, citation target or link target was changed.
- Front matter unchanged: the title is 51 characters; the description is one sentence of 150 characters and says what the reader learns.

**Copy verdict: pass.** C1 to C5 are applied and C6 is kept for the reasons given. Lint now shows 0 warnings, and the only errors left are the six expected entry 3 and entry-count errors described at the top.

<!-- Later stages (fact-check, technical review, resolution, QA) add their sections below. -->

## Fact-check

Stage: EOS 6.3, 2026-10-17. Role: fact-checker (not the author or the editor of this item). Network: WebSearch worked; WebFetch could not resolve any host (arxiv.org, dblp.org, dspace.mit.edu, crossref and others: `ENOTFOUND` or proxy 403), so every bibliographic check below rests on search-engine records of publisher, library and author pages, and no full text was read. Lint at this stage: 0 errors, 0 warnings, 2 suggestions (entry 3 now exists, so the six expected errors noted at the top have cleared).

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| F1 | Should fix | `:318`, Section 4.3 | evidence | "the basic sampling-based planners are not asymptotically optimal" overstates Karaman and Frazzoli (2011) and contradicts entry 3, Section 4.1 (settles D6). |

### F1. What Karaman and Frazzoli showed (settles D6)
- **Where:** `src/content/blog/configuration-space-and-the-planning-problem.mdx:318`, section "4.3 Optimality guarantees".
- **Text:** "Karaman and Frazzoli showed that the basic sampling-based planners are not asymptotically optimal and introduced variants that are (Karaman and Frazzoli, 2011); the third entry describes them."
- **Problem:** The paper's negative results are specific. The MIT abstract of the work states that neither RRT nor the k-nearest PRM, for any fixed k, is asymptotically optimal, and that the PRM with a fixed connection radius *is* asymptotically optimal but costs more than RRT or the efficient PRM variants (S. Karaman and E. Frazzoli, IJRR 30(7), 2011, DOI 10.1177/0278364911406761; arXiv 1105.1186; MIT DSpace 1721.1/81442, search records). "The basic sampling-based planners" includes the fixed-radius PRM, which the paper shows is asymptotically optimal. Entry 3 (`sampling-based-planning-prm-and-rrt.mdx:302`) states the specific version, so the two entries disagree.
- **Correction:** "Karaman and Frazzoli showed that RRT and the PRM that connects each sample to a fixed number of neighbors are not asymptotically optimal, and introduced variants that are (Karaman and Frazzoli, 2011); the third entry describes them." (This is D6's proposed text, now confirmed.)

### D7 and D8 (routed to this stage)
- **D7** is a technical claim and is settled in the technical review (T1).
- **D8: no change.** The IEEE Xplore record of Lozano-Pérez (1983) (document 1676196) and its abstract say the paper characterizes the position and orientation of an object as a point in a configuration space, calls the forbidden regions configuration space obstacles and "presents algorithms for computing these configuration space obstacles when the objects are polygons or polyhedra"; the MIT AI Lab version (AIM-605, DSpace 1721.1/5684) also describes the slice-projection approximation used for rotation, which supports the citation at `:183`. The sentence at `:53` says "formulated" and claims no priority; it is accurate.

### Verification table

| Claim or reference | Location | Status | Source |
|---|---|---|---|
| Schwartz and Sharir called the general problem the piano movers' problem in a series of papers in the early 1980s and gave a general algorithm | `:31` | Verified | Series "On the piano movers' problem" I–V, 1983–1984 (Part I, *Comm. Pure Appl. Math.* 36; Part II, *Adv. Appl. Math.* 4); NYU reports of 1981–1982; Part II gives the general algebraic technique |
| Lozano-Pérez (1983): configuration-space formulation; C-obstacle algorithms for polygons and polyhedra; slices for rotation | `:53`, `:183` | Verified (D8) | IEEE Xplore 1676196 abstract; MIT AIM-605 |
| Chapter 2 of Lynch and Park (2017), Chapter 4 of LaValle (2006), Choset et al. (2005) treat C-space topology | `:71` | Verified | Modern Robotics contents (Ch. 2 "Configuration Space", 2.3.1 "Configuration Space Topology"); LaValle, lavalle.pl/planning node123 "4. The Configuration Space" (Cambridge Core pp. 105–152); Choset et al. contents (configuration space chapter) |
| Orientations of a rigid body: no three-angle set covers the rotation group without singularities | `:71` | Verified (standard) | LaValle (2006) Section 4.2; Lynch and Park (2017) Ch. 2–3 |
| Gripper reaches the ring $0.3 \le r \le 1.7$ m | `:91` | Verified | `planar-arm-kinematics.mdx:87` |
| Prerequisite claims: planner between task level and joint controllers; wrapping with atan2 into $(-\pi, \pi]$ | `:25`, `:67` | Verified | `what-is-a-robot.mdx:142–183`; `coordinate-frames-and-transformations.mdx:247` |
| Minkowski sum of two convex polygons has at most $m + n$ edges | `:286` | Verified (standard) | de Berg et al., computational geometry texts; LaValle (2006) Section 4.3 |
| Probabilistic completeness assumes a solution with positive clearance (LaValle, 2006) | `:314` | Not verified at page level | Standard statement; book text not fetched (see Not verified) |
| Karaman and Frazzoli: which planners are not asymptotically optimal | `:318`, `:454` | Corrected (F1) | MIT abstract; arXiv 1105.1186 abstract |
| PSPACE definition; PSPACE-hard means poly-time reduction from every PSPACE problem; believed, not proved, intractable | `:324` | Verified (standard) | Garey and Johnson; Sipser |
| Reif (1979): generalized mover's problem (linked polyhedra, unbounded DOF) is PSPACE-hard | `:326` | Verified (secondary) | Duke record of the FOCS 1979 paper (DOI 10.1109/SFCS.1979.10); Reif's later survey; Canny STOC 1988 introduction |
| Canny (1988, STOC): the generalized mover's problem is in PSPACE, hence PSPACE-complete | `:326` | Verified | STOC 1988 abstract (UCB/CSD-88-439): existential theory of the reals in PSPACE; "Generalized Movers' Problem ... PSPACE-complete" |
| Schwartz–Sharir cell decomposition doubly exponential in $d$ | `:328` | Verified (secondary) | Cylindrical algebraic decomposition; bound of order $(2n)^{3^{d+1}}$ cited in arXiv 1705.04721; arXiv 1403.5384; LaValle Section 6.4.3 |
| Canny's roadmap singly exponential in $d$, polynomial for fixed robot | `:328` | Verified | Publisher abstract of *The Complexity of Robot Motion Planning*; LaValle Section 6.4.3 |
| For fixed $d$, complete algorithms are polynomial in the number of obstacle features | `:328` | Verified | Same two sources |
| GJK computes the distance between convex sets | `:414` | Verified | Gilbert et al. (1988) abstract: "Euclidean distance between a pair of convex sets in R^m" |
| Visibility graph contains the shortest path for a point among polygons; Lozano-Pérez and Wesley applied it to grown polyhedral obstacles | `:450` | Verified | CACM 1979 paper (scanned copy, Columbia CS course notes): obstacles transformed into forbidden regions for a reference point, then a vertex network searched |
| PRM (Kavraki et al., 1996) multi-query; RRT (LaValle and Kuffner, 2001) | `:454` | Verified | Paper abstracts (learning and query phases; RRT-based kinodynamic planning) |
| CHOMP uses (covariant) gradient optimization; finds local optima | `:456` | Verified | Ratliff et al. (2009) abstract; the expansion "Covariant Hamiltonian optimization for motion planning" is the name used in Zucker et al., IJRR 32(9), 2013, for the same method |
| Potential fields (Khatib, 1986); dynamic window (Fox et al., 1997) | `:458` | Verified | Paper abstracts |
| **References** | | | |
| Canny, *The Complexity of Robot Motion Planning*, MIT Press, 1988 | `:540` | Verified | ACM Distinguished Dissertation series, MIT Press, 1988 (library catalogues) |
| Canny, STOC 1988, pp. 460–467 | `:541` | Verified | JACM bibliography and Numdam reference: Twentieth Annual ACM STOC, Chicago, 2–4 May 1988, pp. 460–467 |
| Choset et al., *Principles of Robot Motion*, MIT Press, 2005 | `:542` | Verified | CMU RI record, ISBN 0-262-03327-5; author list matches |
| Dijkstra, *Numerische Mathematik* 1, pp. 269–271, 1959 | `:543` | Verified | Springer, DOI 10.1007/BF01386390 |
| Fox, Burgard and Thrun, IEEE RAM 4(1), pp. 23–33, 1997 | `:544` | Verified | CMU RI record; DOI 10.1109/100.580977 |
| Gilbert, Johnson and Keerthi, IEEE J. Robotics Autom. 4(2), pp. 193–203, 1988 | `:545` | Verified | Paper first page (U. Michigan copy); ACM DL reference |
| Hart, Nilsson and Raphael, IEEE TSSC 4(2), pp. 100–107, 1968 | `:546` | Verified | DOI 10.1109/TSSC.1968.300136 |
| Karaman and Frazzoli, IJRR 30(7), pp. 846–894, 2011 | `:547` | Verified | Citation records: "30, no. 7 (June 2011): 846–894"; DOI 10.1177/0278364911406761 |
| Kavraki et al., IEEE TRA 12(4), pp. 566–580, 1996 | `:548` | Verified | DOI 10.1109/70.508439 |
| Khatib, IJRR 5(1), pp. 90–98, 1986 | `:549` | Verified | DOI 10.1177/027836498600500106 (SAGE DOIs encode volume 005, issue 001); catalogue records give vol. 5, pp. 90–98, spring 1986 |
| LaValle, *Planning Algorithms*, Cambridge University Press, 2006 | `:550` | Verified | Cambridge Core |
| LaValle and Kuffner, IJRR 20(5), pp. 378–400, 2001 | `:551` | Verified | DOI 10.1177/02783640122067453 |
| Lozano-Pérez, IEEE Trans. Computers C-32(2), pp. 108–120, 1983 | `:552` | Verified | IEEE Xplore 1676196 |
| Lozano-Pérez and Wesley, CACM 22(10), pp. 560–570, 1979 | `:553` | Verified | Paper's own copyright line (scanned copy); one patent citation gives "objects" for "obstacles" in the title, but the paper's title page reads "obstacles" |
| Lynch and Park, *Modern Robotics*, Cambridge University Press, 2017 | `:554` | Verified | Cambridge Core |
| Ratliff et al., ICRA 2009, pp. 489–494 | `:555` | Verified | DOI 10.1109/ROBOT.2009.5152817; CMU RI record |
| Reif, FOCS 1979, pp. 421–427 | `:556` | Verified | Duke record; DOI 10.1109/SFCS.1979.10 |
| Schwartz and Sharir, *Adv. Appl. Math.* 4(3), pp. 298–351, 1983 | `:557` | Verified | Several bibliographies give 4(3), 298–351; NYU report of February 1982 has the same title |

The writer's open items are settled: Karaman and Frazzoli vol. 30, no. 7, pp. 846–894 (confirmed); Khatib no. 1 (confirmed through the DOI and catalogues); Canny STOC pp. 460–467 (confirmed); Lynch and Park Chapter 2 and LaValle Chapter 4 (confirmed); Schwartz and Sharir doubly exponential (confirmed by secondary sources and by the method, cylindrical algebraic decomposition).

### Not verified

- `:314` "its guarantee assumes a path with positive clearance ... (LaValle, 2006)": the standard statement, but the book's text could not be fetched to confirm the section. Recommend no change; the QA stage may add a section number if one is checked.
- Karaman and Frazzoli (2011) full text: the arXiv and IJRR pages could not be fetched; F1 rests on the MIT abstract and the arXiv abstract as returned by search. The F1 correction claims only what those abstracts state (RRT and fixed-$k$ PRM). Entry 3's further claim about the component-skipping PRM is outside this item.
- Reif (1979): the original theorem statement was not read; "linked polyhedra whose number of degrees of freedom grows with the input" rests on Reif's later survey and on Canny's summary.

**Fact-check verdict: fail** (F1 should fix open; no blocking finding). Counts: 0 blocking, 1 should fix, 0 optional.

## Technical review

Stage: EOS 6.4, 2026-10-17. Role: technical reviewer (not the author or editor). Environment: Python 3.13.16, NumPy 2.5.3 (matches the stated Python 3.13 and NumPy 2.5). Scratch files: `/tmp/claude-0/mp/review/configuration-space-and-the-planning-problem/`.

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| T1 | Should fix | `:304`, Section 4.1 | accuracy | "A shortest path among obstacles touches them" and "no shortest path exists in the open set" hold only when obstacles block the straight segment (settles D7). |
| T2 | Should fix | `:278`, Section 3.3 | accuracy | The small C-obstacle regions near $\theta_2 = \pm 150^\circ$ come from the folded second link meeting the disk *beside* the first link, not "the opposite disk". |
| T3 | Should fix | `:302`, Section 4.1 | accuracy | With unit weights the length in $\rho$ is the Euclidean length in joint space, not "the total joint rotation". |
| T4 | Should fix | `:518`, Exercise 6 | accuracy | "For a shoulder limited short of $\pm 180^\circ$, the square is right": with only the shoulder limited, $\theta_2$ still wraps, so the space is a cylinder. |
| T5 | Optional | `:362`, Section 5.3 | accuracy | "no point ... travels more than $c$ cannot cause a collision": travel of exactly $c$ can reach contact, which this entry counts as collision. |
| T6 | Optional | `:257` vs `:480`, `:485` | consistency | Section 3.3 and Exercise 3 say $|\theta_1| < 11.54^\circ$; with touching counted as collision the set is $|\theta_1| \le 11.54^\circ$, as the answer to Exercise 3 writes. |
| T7 | Optional | `:318`, Section 4.3 | accuracy | "as Dijkstra's algorithm and A* do on a graph": A* is resolution optimal only with an admissible heuristic. |

### T1. Shortest paths touch obstacles only when obstacles are in the way (settles D7)
- **Where:** `:304`, section "4.1 Feasibility, cost and optimality".
- **Text:** "A shortest path among obstacles touches them: around a polygon in the plane, it runs straight to a vertex and straight on. Because touching counts as collision here, no shortest path exists in the open set $\mathcal{C}_{\mathrm{free}}$, only paths whose cost comes arbitrarily close to $C^*$."
- **Problem:** If the segment from $q_{\mathrm{start}}$ to $q_{\mathrm{goal}}$ lies in $\mathcal{C}_{\mathrm{free}}$, it is the shortest path, touches nothing and is attained. Both sentences hold only when every shortest path in the closure of $\mathcal{C}_{\mathrm{free}}$ meets the boundary, the case of a blocked segment. The example also needs "for a point" (a robot that only translates, reduced to a point).
- **Correction:** "When obstacles block the straight segment from start to goal, a shortest path touches them: for a point among polygons in the plane, it runs straight to a vertex and straight on. Because touching counts as collision here, no shortest path then exists in the open set $\mathcal{C}_{\mathrm{free}}$, only paths whose cost comes arbitrarily close to $C^*$."

### T2. "The opposite disk"
- **Where:** `:278`, section "3.3 Free space can come apart".
- **Text:** "the small regions near $\theta_2 = \pm 150^\circ$ are the folded second link reaching the opposite disk."
- **Problem:** For every `#` cell outside the two walls, a script tested which disk each link meets (`blob_sources` run, scratch directory). All 28 such cells are second-link contacts with the disk next to the first link: at $(\theta_1, \theta_2) = (-45^\circ, 145^\circ)$ to $(-15^\circ, 175^\circ)$ and $(15^\circ, -175^\circ)$ to $(45^\circ, -145^\circ)$ the disk at $(0.5, 0)$ m; at $(135^\circ, 145^\circ)$ to $(165^\circ, 175^\circ)$ and $(-165^\circ, -175^\circ)$ to $(-135^\circ, -145^\circ)$ the disk at $(-0.5, 0)$ m. Example: at $(-35^\circ, 155^\circ)$ the clearance to the disk at $(0.5, 0)$ is $-0.090$ m and to the disk at $(-0.5, 0)$ is $+0.400$ m. Each region sits beside the wall made by the same disk.
- **Correction:** "the small regions near $\theta_2 = \pm 150^\circ$ are the folded second link swinging back over the disk beside the first link, the same disk that makes the nearer wall."

### T3. Unit-weight length is not total joint rotation
- **Where:** `:302`, section "4.1 Feasibility, cost and optimality".
- **Text:** "For the arm with unit weights, this is the total joint rotation in radians, not the distance traveled by the gripper."
- **Problem:** With $w_1 = w_2 = 1$, $\lVert \dot\sigma \rVert_w = \sqrt{\dot\theta_1^2 + \dot\theta_2^2}$, so $J$ is the Euclidean arc length in the $(\theta_1, \theta_2)$ plane. "Total joint rotation" reads as $\int (|\dot\theta_1| + |\dot\theta_2|)\,ds$, the 1-norm. They differ: for the straight edge of Exercise 4 ($\Delta\theta = (0.5, -0.4)$ rad) the length is $\sqrt{0.41} = 0.640$ rad, the total rotation $0.9$ rad.
- **Correction:** "For the arm with unit weights, this is the Euclidean length of the path in joint space, in radians, not the distance traveled by the gripper."

### T4. Exercise 6: a limited shoulder gives a cylinder
- **Where:** `:518`, answer to Exercise 6.
- **Text:** "For a shoulder limited short of $\pm 180^\circ$, the square is right and the parts are disconnected."
- **Problem:** Limiting $\theta_1$ removes only the left-right gluing; if the elbow is unlimited, $\theta_2$ still wraps and the space is $[\theta_{1,\min}, \theta_{1,\max}] \times S^1$, a cylinder. The square is right only if the elbow is limited too. The conclusion (two components) holds either way, because the wall spans every $\theta_2$. In an entry whose point is that topology matters, the wrong space should not be named.
- **Correction:** "For a shoulder limited short of $\pm 180^\circ$, $\theta_1$ no longer wraps (the space is a cylinder, or the square if the elbow is limited too), and the parts are disconnected."

### T5. Travel of exactly $c$ (optional)
- **Text (`:362`):** "a motion during which no point of the robot travels more than $c$ cannot cause a collision."
- **Correction:** "a motion during which every point of the robot travels less than $c$ cannot cause a collision; at exactly $c$ it can at most reach contact, which the next check detects." The algorithm is unaffected: it re-checks at the end of each step.

### T6. Strict and non-strict bound (optional)
- **Correction:** At `:257` and in the Exercise 3 prompt (`:480`), write $|\theta_1| \le 11.54^\circ$, matching the answer (`:485`) and the convention that touching collides.

### T7. A* needs an admissible heuristic (optional)
- **Correction (`:318`):** "as Dijkstra's algorithm and A* with an admissible heuristic do on a graph". Entry 2, Section 4.2, gives the condition.

### Checks performed

Definitions and derivations:
- Configuration, C-space, $\mathcal{C}_{\mathrm{obs}}$, free space as an open set (closed obstacles, compact robot), Minkowski-sum derivation $q = o - a \Rightarrow \mathcal{O} \oplus (-\mathcal{A})$, and $-\mathcal{A} = \mathcal{A}$ for a centered disk: correct.
- Topologies: $S^1$, torus $S^1 \times S^1$ with the square glued edge to edge, box for limited joints, Exercise 1 (a)–(d): correct. Wrapping with $\operatorname{atan2}(\sin\Delta, \cos\Delta)$ into $(-\pi, \pi]$: correct and matches the Introduction to Robotics series.
- Distance $\rho$ and units: correct; T3 on its unit-weight reading.
- Forward kinematics and ring $0.3 \le r \le 1.7$ m: match `planar-arm-kinematics.mdx`.
- Completeness definitions (complete, resolution complete, probabilistically complete) and optimality definitions: standard (LaValle 2006, Chapters 5 and 6; Lynch and Park 2017, Section 10.1.2).
- Velocity bound of Section 5.3: $\dot p = l_1 \dot\theta_1 e^\perp(\theta_1) + u(\dot\theta_1 + \dot\theta_2) e^\perp(\theta_1 + \theta_2)$; the triangle inequality and $u \le l_2$ give $(l_1 + l_2)|\dot\theta_1| + l_2|\dot\theta_2|$; points of link 1 move at most $l_1|\dot\theta_1|$. Correct. Clearance is 1-Lipschitz in the displacement of the robot's points, so a step of $c/D$ cannot pass through an obstacle; with the tolerance each step is at least $\mathrm{tol}/D$, so the walk ends. Correct (T5 on wording).
- Section 3.1 area formula $wh + 2r(w+h) + \pi r^2$: correct by decomposition.
- PSPACE statements, Reif and Canny, singly and doubly exponential bounds: see the fact-check.

Programs run (`sh run.sh`, copies in `progs/`): exit 0; output identical (`diff`) to the writer's `run_output.txt`. Every `text` block of the article was matched line by line, in order, against the rerun output (ellipsis lines skipped): 7 blocks, 0 unmatched lines. Elided rows checked: the r = 0.45 m grid has 20 identical rows; the elided rows of the Section 3.2 grid are all free; those of the Section 3.3 grid equal the row at 135°.

Article code blocks run (`run_article_code.py`): the three `python` listings, executed as written, reproduce the disk cell counts 128, 180, 240; the two arm grids are identical to the program's (60 and 172 cells); `certified(qa, qb, obstacles)` gives 4 checks, collision, $\theta_1 = 8.933^\circ$ (1.65 m) and 12 checks, free (1.75 m). The listing's `certified` takes `qa, qb, obstacles` where the program's uses globals; behavior is the same. The fixed-step loop is described in prose ("The listing omits ..." for Section 3.1; the fixed-step and labeling code are not listed), which the text does not claim otherwise.

Recomputed numbers (`numbers.txt`): grown-square area $6.07617$ m² (quoted 6.0762; $2.56 + 2.88 + 0.6362$); Exercise 2 $2.48274$ m²; $\arcsin(0.2) = 11.537^\circ$; contact window $8.958^\circ$ to $11.042^\circ$, width $2.0836^\circ = 0.03637$ rad; 0.05 rad step: 42 steps, samples at $8.571^\circ$ and $11.429^\circ$; 0.02 rad step: first hit at check 62, $\theta_1 = 9.714^\circ$; $D = 3.56047$ m; Exercise 4: $D = 1.13$, step 0.044248, joints 0.022124 rad ($1.268^\circ$) and $-0.017699$ rad ($-1.014^\circ$); $36^6 = 2.177 \times 10^9$, $36^7 = 7.836 \times 10^{10}$; IK of $(1.3, 0.2)$ m: $(-22.88^\circ, 80.13^\circ)$ and $(40.37^\circ, -80.13^\circ)$. Fixed-step check counts $\lceil 2.0944/h \rceil + 1$: 12, 22, 43, 106, 211. All agree with the text.

Further checks: band extent of Section 3.2 on a $0.1^\circ$ grid, excluding pure touching: penetration only for $|\theta_2| \le 110.4^\circ$ ("about $110^\circ$" correct); at exactly $\theta_1 = 0$ the first link touches the disk for every $\theta_2$, a measure-zero line the text covers ("can at most touch it"). Corridor arithmetic: strip $1.85$ to $2.15$ m, cell centers 1.9 and 2.1 m inside it; grown obstacles one cell wider at $r = 0.25$ m. Exercise 6 output (1 component on the torus, 2 on the square) reproduced. Cross-entry fragments: `#22-degrees-of-freedom-and-mobility`, `#4-loops-within-loops`, `#5-organizing-the-software`, `#2-forward-kinematics-of-a-two-link-arm`, `#4-closed-form-inverse-kinematics`, `#6-the-limits-of-grids`, `#6-checking-a-trajectory`, `#5-narrow-passages-and-other-failure-modes` all match headings in the target files; the descriptions of those sections agree with their content (entry 4 writes $q(t) = \sigma(s(t))$; entry 3, Section 6 smooths paths). Determinism: no random numbers are used, as stated. No site build was made in this stage (no file changed).

**Technical verdict: fail** (T1 to T4 should fix open; no blocking finding). Counts: 0 blocking, 4 should fix, 3 optional.


## Resolution

Stage: author resolution, 2026-10-17. Role: author of the draft (not a reviewer of it). The file was re-read as left by the editors, and all corrections were made in `src/content/blog/configuration-space-and-the-planning-problem.mdx` only; entry 3 was read, not edited. Asymptotic optimality is now stated as in `sampling-based-planning-prm-and-rrt.mdx`, Section 4: RRT and the fixed-$k$ PRM are not asymptotically optimal, and the fixed-radius PRM is but is expensive. No quoted output, number or code listing changed, so `run.sh` was not re-run for this stage; its last output is unchanged. Lint after resolution: 0 errors, 0 warnings, 2 suggestions (C6, kept). Build under the lock (`flock`): exit 0, `check-links` reports that all internal links resolve (including `#5-narrow-passages-and-other-failure-modes` in entry 3), no KaTeX errors; the build directory was deleted.

| ID | Action | Exact change |
|---|---|---|
| D1–D5 | Already applied by the editor; kept | None |
| D6 | Settled by F1 | See F1 |
| D7 | Settled by T1 | See T1 |
| D8 | Not applied: the fact-check found the sentence accurate | None |
| F1 | Applied with changes | Section 4.3: "Karaman and Frazzoli showed that the basic sampling-based planners are not asymptotically optimal and introduced variants that are (Karaman and Frazzoli, 2011); the third entry describes them." → "Karaman and Frazzoli showed that the rapidly-exploring random tree (RRT) and the probabilistic roadmap (PRM) that connects each sample to a fixed number of neighbors are not asymptotically optimal. A PRM that joins every pair within a fixed radius is asymptotically optimal but expensive, and they introduced variants that are asymptotically optimal at lower cost (Karaman and Frazzoli, 2011); Section 4 of the third entry describes them." The fixed-radius sentence was added so that this entry matches entry 3, Section 4. Because RRT and PRM now first appear here, their expansions moved here, and Section 6 now reads "The PRM builds ..." and "the RRT grows ..." |
| T1 | Applied | Section 4.1: "A shortest path among obstacles touches them: around a polygon in the plane, it runs straight to a vertex and straight on. Because touching counts as collision here, no shortest path exists in the open set" → "When obstacles block the straight segment from start to goal, a shortest path touches them: for a point among polygons in the plane, it runs straight to a vertex and straight on. Because touching counts as collision here, no shortest path then exists in the open set" |
| T2 | Applied | Section 3.3: "are the folded second link reaching the opposite disk." → "are the folded second link swinging back over the disk beside the first link, the same disk that makes the nearer wall." Checked by hand at $(-35^\circ, 155^\circ)$: the second link ends near $(0.47, 0.03)$ m, beside the disk at $(0.5, 0)$ m. |
| T3 | Applied | Section 4.1: "this is the total joint rotation in radians" → "this is the Euclidean length of the path in joint space, in radians" |
| T4 | Applied | Exercise 6 answer: "For a shoulder limited short of $\pm 180^\circ$, the square is right and the parts are disconnected." → "For a shoulder limited short of $\pm 180^\circ$, $\theta_1$ no longer wraps (the space is a cylinder, or the square if the elbow is limited too), and the parts are disconnected." |
| T5 | Applied | Section 5.3: "a motion during which no point of the robot travels more than $c$ cannot cause a collision." → "a motion during which every point of the robot travels less than $c$ cannot cause a collision; at exactly $c$ it can at most reach contact, which the next check detects." |
| T6 | Applied | Section 3.3: "$|\theta_1| < \arcsin(0.1/0.5) = 11.54^\circ$" → "$|\theta_1| \le \arcsin(0.1/0.5) = 11.54^\circ$"; Exercise 3 prompt: "$|\theta_1| < 11.54^\circ$" → "$|\theta_1| \le 11.54^\circ$" |
| T7 | Applied | Section 4.3: "as Dijkstra's algorithm and A* do on a graph." → "as Dijkstra's algorithm and A* with an admissible heuristic do on a graph." |
| C6 | Kept, as the editor recommended | None |

**Resolution status:** no blocking or should-fix finding remains open.
