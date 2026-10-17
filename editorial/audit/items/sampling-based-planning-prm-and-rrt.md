# Editorial review: Sampling-Based Planning: Probabilistic Roadmaps and RRT

- Path: `src/content/blog/sampling-based-planning-prm-and-rrt.mdx` · Route: `/blog/sampling-based-planning-prm-and-rrt` · Type: article · Series `motion-planning`, entry 3 of 5
- Stages in this report: developmental edit (EOS 6.1) and copy edit (EOS 6.2), 2026-10-17. Editor: developmental-editor and copy-editor roles (not the author of the draft).
- Length: 7,862 words by `wc -w` on the whole file (7,865 before the edit), including front matter, code, program output and references; within the 2,500 to 8,000 words the standards allow for a series entry. Length was not treated as a defect; nothing was cut for length alone.
- Lint at hand-off: 0 errors, 0 warnings, 2 suggestions (both kept, see C5). Before the edit: 0 errors, 0 warnings, 5 suggestions.
- Build check: `astro build --outDir /tmp/claude-0/mp/edit-build-3` exit 0 (356 pages); `check-links` on that build: "All internal links resolve", including the three links added in this pass. No letter glued to an inline element in the built page (the only matches are inside KaTeX markup). The build directory was deleted.
- Consistency with the first entry: Section 4.1 says that RRT and the fixed-$k$ PRM are not asymptotically optimal and that the fixed-radius PRM is asymptotically optimal but expensive, which matches the revised Section 4.3 of the first entry. Section 4.5 (optimal path grazes a corner and is approached from the free side) matches Section 4.1 of the first entry.
- Headings: all eight `##` headings and all `###` headings are unchanged, so no fragment changed. Inbound links checked: the first entry links `#5-narrow-passages-and-other-failure-modes`, which still resolves; the other entries link the page without a fragment.

## Developmental review

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| D1 | Should fix | `:17`, opening | structure | The second opening paragraph ended in a table of contents in prose, one clause per section (also the 46-word sentence the linter flagged). |
| D2 | Should fix | `:40`, Section 1.3; `:302`, Section 4.1 | structure | Probabilistic completeness and asymptotic optimality were defined again from scratch, although Sections 4.2 and 4.3 of the first entry define them; no back-reference. |
| D3 | Should fix | `:71`, Section 1.4 | consistency | The visibility graph was "mentioned in the second entry" without a link or section number. |
| D4 | Should fix | `:302`, Section 4.1 | evidence | "gave answers that surprised many practitioners" is an unsupported claim about other people's reactions. |
| D5 | Should fix | `:353`, Section 4.4 (old `:349`) | structure | One 176-word paragraph discussed the definitions of the table, the PRM results and the RRT results, introduced by "The table shows the theory at work." |
| D6 | Should fix | `:419`, Section 6.1 | structure | One paragraph moved from the homotopy result of `probe_shortcut.py` to clearance and to Geraerts and Overmars' remedies. |
| D7 | Optional | `:425`, Section 6.2; `:357`, Section 4.5; `:486`, Section 8 | structure | The hand-off to the fourth entry (paths have corners and no timing) was made three times; Section 6.2's version was the longest. |
| D8 | Optional, for the technical reviewer | `:216`, Section 3.2 | accuracy | "The probability of extending a vertex is proportional to the volume of its Voronoi region" holds for the uniform iterations, with the region intersected with $\mathcal{C}$; goal-biased iterations always extend the vertex nearest the goal. Left unchanged. |
| D9 | Optional, for the technical reviewer | `:405`, Section 6.1 | accuracy | "Each successful move shortens the path, by the triangle inequality": strictly, a move does not lengthen the path; it leaves it unchanged when the replaced piece is already straight. Left unchanged. |
| D10 | Optional, for the technical reviewer | `:461`, Exercise 4 answer | accuracy | "a coarse grid search in a low-dimensional projection" as evidence of infeasibility: a failed search in a projection proves nothing unless the projection and the marking are conservative. Left unchanged. |
| D11 | Optional, for the fact-checker | `:324`, Section 4.3; `:256`, Section 3.4; `:216`, Section 3.2 | evidence | Attributions to verify against the cited papers: the $(\log n / n)^{1/(d+1)}$ radius of Solovey et al. (2020); the seven-degree-of-freedom human arm model in Kuffner and LaValle (2000); LaValle and Kuffner naming the Voronoi bias as the reason for rapid exploration. Left unchanged. |

### D1. Table of contents in the opening
- **Where:** `:17`, opening paragraphs.
- **Text:** "After the concept of sampling (Section 1), it treats probabilistic roadmaps (Section 2) and random trees (Section 3), the variants that converge to optimal paths (Section 4), the situations in which sampling fails (Section 5) and the post-processing that makes a sampled path usable (Section 6)."
- **Problem:** The developmental-editor brief and Standards 6.1 ask the opening to say what the piece covers without a table of contents in prose; the sentence was also 46 words (`sentence-length`).
- **Correction (applied):** "It explains how the two families work and what their guarantees mean, which variants converge to optimal paths, where sampling fails and how a sampled path is shortened before a robot uses it."

### D2. Definitions repeated from the first entry
- **Where:** `:40`, section "1.3 Probabilistic completeness"; `:302`, section "4.1 Why the basic planners do not converge".
- **Text:** "A sampling-based planner is at best **probabilistically complete** : if a path exists, ..."; "A planner is **asymptotically optimal** if the cost of its solution converges to $C^*$, almost surely, ..."
- **Problem:** Standards 6.1 ("across a series, a later entry refers back instead of repeating") and 5.3 (a later entry may refer back). The definitions here are short and useful in place, so they were kept, but without a pointer the reader cannot tell that they are the series' definitions.
- **Correction (applied):** "... **probabilistically complete**, in the sense of [Section 4.2 of the first entry](/blog/configuration-space-and-the-planning-problem#42-completeness): if a path exists, ..." and "A planner is **asymptotically optimal**, as [Section 4.3 of the first entry](/blog/configuration-space-and-the-planning-problem#43-optimality-guarantees) defined it, if ...". Both fragments resolve in the build.

### D3. Unlinked reference to the visibility graph
- **Where:** `:71`, section "1.4 The test problems".
- **Text:** "(the graph whose edges join mutually visible corners, mentioned in the second entry)"
- **Problem:** Standards 8.1: cross-references cite numbered sections. The second entry treats the visibility graph in its Section 2.3.
- **Correction (applied):** "(the graph whose edges join mutually visible corners, [Section 2.3 of the second entry](/blog/graph-search-dijkstra-and-a-star#23-visibility-graphs))".

### D4. Unsupported claim about practitioners
- **Where:** `:302`, section "4.1 Why the basic planners do not converge".
- **Text:** "Karaman and Frazzoli examined this question in 2011 and gave answers that surprised many practitioners."
- **Problem:** No source supports what practitioners expected; Standards 7.2 and 2.3 (no claim without evidence, no rhetoric of importance). The result itself follows in the next sentences.
- **Correction (applied):** "Karaman and Frazzoli examined this question in 2011."

### D5. Section 4.4 discussion in one paragraph
- **Where:** `:349` before the edit, section "4.4 Measured convergence".
- **Text:** "... because blocked extensions add none. The table shows the theory at work. Between 1000 and 2000 samples, ..."
- **Problem:** 176 words with three topics (how to read the table, PRM against PRM*, RRT against RRT*); "The table shows the theory at work" announces rather than says. Standards 5.2.
- **Correction (applied):** Deleted "The table shows the theory at work." and split the paragraph into three: the reading notes, the PRM comparison (`:351`) and the RRT comparison (`:353`). No number changed.

### D6. Section 6.1 paragraph with two topics
- **Where:** `:419` and `:421`, section "6.1 Shortcutting".
- **Text:** "... a sixth longer than the next longest. Shortcuts also pull the path tight against obstacles, ... Geraerts and Overmars studied both issues: ..."
- **Problem:** The paragraph reported the homotopy result and then turned to clearance and to remedies for both limits; "both issues" had no clear antecedent.
- **Correction (applied):** New paragraph at "Shortcuts also pull the path tight"; "studied both issues" became "addressed both limits".

### D7. Hand-off to the fourth entry made three times
- **Where:** `:357` Section 4.5 ("a problem for the next entry"), `:425` Section 6.2, `:486` Section 8.
- **Text:** "Smoothing in geometry alone also says nothing about how fast the robot moves along the curve. That requires a time scaling, which is where the planner's output becomes something a controller can follow."
- **Problem:** Standards 6.1 (no redundancy; the closing paragraph is where the entry leads on).
- **Correction (applied):** Section 6.2 now ends "Geometric smoothing also says nothing about how fast the robot moves along the curve; that is the job of a time scaling." The closing paragraph keeps the full lead to the next entry; the half-clause in Section 4.5 was kept because it closes a list of limits.

### D8 to D11. For the technical reviewer and the fact-checker
- **D8, Where:** `:216`. **Text:** "The probability of extending a vertex is proportional to the volume of its Voronoi region, so the tree is pulled toward the largest unexplored parts of the space." **Proposed:** if confirmed, qualify as "For a uniform sample, the probability of extending a vertex is proportional to the volume of its Voronoi region within $\mathcal{C}$".
- **D9, Where:** `:405`. **Text:** "Each successful move shortens the path, by the triangle inequality". **Proposed:** "Each successful move never lengthens the path, by the triangle inequality," or keep if the program counts only moves that shorten.
- **D10, Where:** `:461`. **Text:** "If infeasibility is suspected, it needs other evidence, such as a check that the start and goal are free and in reach, or a coarse grid search in a low-dimensional projection." **Proposed:** the technical reviewer decides whether the projection search needs the qualification "with conservative marking".
- **D11, Where:** `:324`, `:256`, `:216`. **Text:** "showed asymptotic optimality for a radius that shrinks as $(\log n / n)^{1/(d+1)}$"; "The original paper reported it on planning problems for a seven-degree-of-freedom human arm model."; "LaValle and Kuffner described this **Voronoi bias** as the reason the tree spreads rapidly, hence the method's name." **Proposed:** verify each against the cited paper; qualify or remove any that the paper does not support.

### What changed (developmental)
- Opening: the prose table of contents replaced by one scope sentence (D1).
- Back-references with section links to the first entry's definitions (D2) and to the second entry's visibility graph (D3).
- Removed the unsupported "surprised many practitioners" (D4).
- Split the Section 4.4 and Section 6.1 discussions by topic (D5, D6).
- Shortened the Section 6.2 hand-off to the next entry (D7).

**Developmental verdict: pass.** Counts: 0 blocking, 6 should fix (all applied), 5 optional (D7 applied; D8 to D11 left open for the technical reviewer and the fact-checker). No blocking or should-fix finding of this stage remains open.

## Copy edit

`eos fix --rules spelling-variant,terminology`: 0 fixes applied (the draft was already in house spelling and terms). No contractions, em dashes, "simply", "obviously", "clearly", "of course" or non-derivation "we" were found.

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| C1 | Should fix | `:181`, Section 2.2; `:145` | language | "shortcut" used for skipping same-component neighbors, a second sense beside the shortcutting of Section 6; "the scratch programs" is authoring jargon for the reader. |
| C2 | Should fix | `:314`, Section 4.2 | language | "the cost of PRM* and of RRT*" meant computational cost in an entry where "cost" is path length. |
| C3 | Should fix | `:139`, figure caption | language | "Everything above the last box" describes a left-to-right flowchart. |
| C4 | Should fix | `:40`, `:122`, `:486`, `:302`, `:357`, `:425` | language | Punctuation and wording: a space before a colon, two serial commas, "too expensive" without a measure, an undefined "anytime planner", a 53-word sentence flagged in Section 6.2. |
| C5 | Optional | `:491`, `:499`, References | publishing | Lint suggestions `acronym-expansion` on "MIT" and "TR" kept. |
| C6 | Optional | `:124`, `:202`, `:216`, `:277`, `:486` | language | Generic or loose phrasing ("Three things stand out", "Why this simple rule explores well becomes clear from ...", "the picture is the same", "a path was found with a few thousand checks"). |

### C1. A term in two senses; authoring jargon
- **Where:** `:181` and `:145`, section "2.2 Choosing neighbors".
- **Text:** "Karaman and Frazzoli showed that this shortcut prevents the roadmap's paths from improving"; "all are in `mp.py` in the scratch programs."
- **Correction (applied):** "this economy prevents"; "all are in `mp.py`, the module that the programs of this entry share."

### C2. "Cost" in two senses
- **Where:** `:314`, section "4.2 The connection radius".
- **Text:** "They showed that the cost of PRM* and of RRT*, below, is within a constant factor of the cost of PRM and RRT."
- **Correction (applied):** "They showed that the computational cost of PRM* and of RRT* (Section 4.3) is within a constant factor of that of PRM and RRT." Meaning unchanged (the sentence is about the work per sample, as the preceding sentence on the number of edges shows); the forward reference now names its section.

### C3. Caption direction
- **Where:** `:139`.
- **Text:** "Everything above the last box is done once"
- **Correction (applied):** "Everything before the query box is done once" (the Mermaid diagram is `flowchart LR`).

### C4. Punctuation and precision
- `:40` "**probabilistically complete** :" (space before colon): fixed with D2.
- `:122` "keeps those that pass the point check, and tries" and `:486` "completeness only in probability, optimality only in the limit, and both slowed": serial commas removed (Standards 5.1); the second rephrased as "completeness only in probability and optimality only in the limit, both slowed by narrow passages".
- `:302` "which makes it too expensive" → "which makes it expensive for large $n$" (too expensive for what was unstated; agrees with "expensive" in Section 4.3 of the first entry).
- `:357` "best used as an anytime planner that improves its path while time remains" → "best used as an **anytime planner**, one that returns its first path early and keeps improving it while time remains" (term defined at first use, Standards 5.3).
- `:425` the `sentence-length` suggestion (53 words) came from a sentence starting with a bold term, which the linter joined to the previous sentence; rewritten as "The remedy, **smoothing**, replaces the polyline ...", which clears it.

### C5. Lint suggestions kept
- `acronym-expansion` "MIT" (`:491`): part of the publisher's name, MIT Press, in a reference entry; expanding it would misquote the imprint.
- `acronym-expansion` "TR" (`:499`): part of the report number "TR 98-11" of the cited technical report, which is written out as "Technical Report" in the same entry.

### C6. Generic or loose phrasing (applied)
- `:124` "The original paper targeted robots with many degrees of freedom, and its title names high-dimensional configuration spaces as its subject." → "The original paper was written for robots with many degrees of freedom, as its title says."
- `:202` "Three things stand out." → "The results show three effects."
- `:216` "Why this simple rule explores well becomes clear from the question of which vertex is extended." → "The rule explores well because of the way it selects the vertex to extend."
- `:277` "the picture is the same" → "the two planners compare in the same way".
- `:486` "in the examples here a path was found with a few thousand checks" → "in the examples here the trees found a path with a few thousand checks" (the roadmaps used tens of thousands; the sentence now says which planners it describes).

### What changed (copy)
- Terminology: one sense each for "shortcut" and "cost" (C1, C2).
- Precision: caption direction, measure for "expensive", definition of "anytime planner" (C3, C4).
- House style: two serial commas removed, a stray space before a colon (C4).
- Concision and generic phrasing: five sentences rewritten (C6).
- No technical claim, number, equation, code block, program output, unit, citation or link target was changed. Three links were added (D2, D3); all resolve.

**Copy verdict: pass.** Counts: 0 blocking, 4 should fix (all applied), 2 optional (C6 applied; C5 kept with reasons). Final `eos lint`: 0 errors, 0 warnings, 2 suggestions (C5).

<!-- Later stages (fact-check, technical review, resolution, QA) append their sections below. -->

## Fact-check

- Stage: fact-check (EOS 6.3), 2026-10-17. Reviewer: fact-checker role (not the author or an earlier editor of this item).
- Tools: WebSearch only. WebFetch and direct HTTPS to arXiv, doi.org, Crossref, DBLP, IEEE Xplore, SAGE and university repositories were refused by this session's egress proxy (`connect_rejected`, HTTP 403), so no full text was fetched. Bibliographic details were confirmed from the catalogue and publisher records that search returned (MIT DSpace, IEEE DOI records, Tel Aviv University CRIS, Utrecht University research portal, Illinois Experts, Kavrakilab, MIT Press Bookstore, CMU Robotics Institute, library catalogues), and theorem statements from search excerpts of the arXiv and Berkeley-hosted copies of the papers. Where only a secondary source was available, the table says so.
- References: `eos refs` lists 13 entries for this item. All 13 exist, and their authors, titles, venues, volumes, issues, pages and years match the sources found. No reference is unconfirmed, so there is no blocking reference finding.

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| F1 | Should fix | `:216`, Section 3.2 | evidence | The Voronoi-bias explanation is confirmed in Kuffner and LaValle (2000, RRT-Connect), not in LaValle and Kuffner (2001); "hence the method's name" is an inference about the naming that no source supports. Settles the third item of D11. |
| F2 | Optional | `:302`, Section 4.1 | evidence | Karaman and Frazzoli's negative result for RRT holds "under mild technical conditions" (their abstract); the sentence states it without a condition. |
| F3 | Optional | `:256`, Section 3.4 | evidence | Verified, with a nuance: the RRT-Connect paper says the method was designed for a 7-DOF human arm model (animation of grasping) and also reports 6-DOF PUMA examples. No change needed. Settles the second item of D11. |
| F4 | Optional | `:497`, References | evidence | Kleinbort et al. (2019) has a published correction (*IEEE Robotics and Automation Letters*, vol. 8, no. 2, pp. 1149–1150, 2023) that concerns the kinodynamic analysis only; the geometric result the entry cites is unaffected. No change needed. |

### F1. Voronoi bias attributed to the wrong paper; naming inference
- **Where:** `:216`, section "3.2 The Voronoi bias".
- **Text:** "LaValle and Kuffner described this **Voronoi bias** as the reason the tree spreads rapidly, hence the method's name."
- **Problem:** Search excerpts of J. J. Kuffner and S. M. LaValle, "RRT-connect: An efficient approach to single-query path planning" (ICRA 2000, vol. 2, pp. 995–1001) tie a vertex's chance of selection to the size of its Voronoi region and say that "an RRT is biased by large Voronoi regions to rapidly explore, before uniformly covering the space". I could not confirm the same argument in LaValle and Kuffner (2001), the paper that "LaValle and Kuffner" points to elsewhere in the entry (`:399`). "Hence the method's name" says the name was chosen because of the Voronoi bias; the name dates from the 1998 report, and no source found says why it was chosen.
- **Correction:** "Kuffner and LaValle described this **Voronoi bias** as what makes the tree explore rapidly, the property the method is named for." (The 2000 paper is already in the reference list.)

### F2. Negative result stated without its condition
- **Where:** `:302`, section "4.1 Why the basic planners do not converge".
- **Text:** "They proved that RRT is not: the probability that its solution converges to the optimal cost is zero."
- **Problem:** Karaman and Frazzoli (2011), abstract: the cost of the solution returned by the widely used algorithms "converges almost surely to a non-optimal value" "under mild technical conditions".
- **Correction (optional):** "They proved that, under mild technical conditions, RRT is not: ..."

### Items left by the developmental editor (D11)
- **First item** (`:324`, Solovey et al.): verified. The IEEE abstract of Solovey, Janson, Schmerling, Frazzoli and Pavone (ICRA 2020, pp. 2189–2195, DOI 10.1109/ICRA40945.2020.9196553) says the authors identify a logical gap in the RRT* optimality proof and change the radius from $\gamma(\log n/n)^{1/d}$ to $\gamma'(\log n/n)^{1/(d+1)}$ "to account for the additional dimension of time that dictates the samples' ordering". No change.
- **Second item** (`:256`, seven-DOF arm): verified (F3). No change.
- **Third item** (`:216`, Voronoi bias): partly verified; corrected by F1.

### Verification table

| Claim | Location | Status | Source |
|---|---|---|---|
| PRM* radius $r_n = \gamma_{\mathrm{PRM}}(\log n/n)^{1/d}$ with $\gamma_{\mathrm{PRM}} > 2(1+1/d)^{1/d}(\mu(\mathcal{C}_{\mathrm{free}})/\zeta_d)^{1/d}$ | `:306–312` | Verified | Karaman and Frazzoli (2011), theorem on the asymptotic optimality of PRM*, in search excerpts of the arXiv 1105.1186 copy and a survey that quotes it ("If $\gamma_{PRM} > 2(1+1/d)^{1/d}(\mu(\chi_{free})/\zeta_d)^{1/d}$, then the PRM* algorithm is asymptotically optimal") |
| $k$-nearest PRM* with $k(n) = k_{\mathrm{PRM}}\log n$, $k_{\mathrm{PRM}} > e(1+1/d)$ | `:316` | Verified | Karaman and Frazzoli (2011), Theorem 35 ("If $k_{PRM} > e(1 + 1/d)$, then the k-nearest implementation of the PRM* algorithm is asymptotically optimal") |
| $k_{\mathrm{PRM}} = 2e$ works for every $d \ge 2$ | `:316` | Verified by derivation | $e(1+1/d) \le 1.5e < 2e$ for $d \ge 2$, and equals $2e$ at $d = 1$, so the stated range is right (technical log) |
| RRT not asymptotically optimal; probability of converging to the optimum is zero | `:302` | Verified (condition: F2) | Karaman and Frazzoli (2011), abstract and RRT theorem as summarized in search excerpts |
| Fixed-$k$ PRM not asymptotically optimal | `:302` | Verified | Karaman and Frazzoli (2011): the $k$-nearest sPRM "is not asymptotically optimal for any fixed k" |
| Component-skipping PRM not asymptotically optimal | `:181`, `:302` | Verified | Karaman and Frazzoli (2011): "the standard PRM and RRT algorithms are not asymptotically optimal" (their standard PRM is the forest variant) |
| Fixed-radius PRM asymptotically optimal but expensive | `:302` | Verified | Karaman and Frazzoli (2011): "the 'simplified' PRM algorithm is asymptotically optimal, but computationally expensive" (sPRM joins all pairs within a fixed radius) |
| Computational cost of PRM* and RRT* within a constant factor of PRM and RRT | `:314` | Verified | Karaman and Frazzoli (2011), abstract |
| Gap in the RRT* proof; radius $\propto (\log n/n)^{1/(d+1)}$ | `:324` | Verified | Solovey et al. (2020), IEEE abstract |
| PRM by Kavraki, Švestka, Latombe and Overmars, 1996; "learning phase" and "query phase" | `:122` | Verified | Kavraki et al. (1996), abstract; *IEEE Trans. Robotics and Automation* 12(4):566–580, DOI 10.1109/70.508439 |
| RRT introduced by LaValle in Technical Report TR 98-11, Computer Science Department, Iowa State University, 1998 | `:210`, `:499` | Verified | Hosted copy of the report (title, Iowa State affiliation) and reference lists citing "Technical Report 98-11, Dept. of Computer Science, Iowa State University" (1998); month not given in the entry and not needed |
| RRT-Connect (2000); greedy connection; seven-DOF human arm | `:256` | Verified | Kuffner and LaValle (2000), abstract; Illinois Experts record ("human arm (modeled as a 7-DOF kinematic chain)") |
| Voronoi bias given by the RRT authors as the reason for rapid exploration | `:216` | Corrected (F1) | Kuffner and LaValle (2000) |
| Expansiveness; failure probability decreases exponentially in the number of samples | `:296` | Verified (secondary) | Hsu, Latombe and Motwani (1999): full text not reachable; the same group's later work (Hsu, Kindel, Latombe and Rock, *IJRR*, 2002) and course notes state that in an expansive space the failure probability decreases exponentially with the number of milestones; IJCGA 9(4&5):495–512 confirmed in reference lists |
| RRT probabilistically complete for geometric planning given a solution with positive clearance | `:296` | Verified | Kleinbort et al. (2019), *RA-L* 4(2):277–283, DOI 10.1109/LRA.2018.2888947: the geometric proof needs only that the solution path keep some clearance (F4) |
| Gaussian sampling: keep the free one when exactly one of the pair is free | `:388` | Verified | Boor, Overmars and van der Stappen, ICRA 1999, pp. 1018–1023 (Utrecht research portal); the description is the standard statement of the method |
| Bridge test (endpoints in collision, midpoint free); hybrid with uniform sampling | `:389` | Verified (hybrid partly) | Hsu, Jiang, Reif and Sun, ICRA 2003, vol. 3, pp. 4420–4426, DOI 10.1109/ROBOT.2003.1242285; excerpt: three checks at the endpoints and midpoint of a short segment, and the bridge test "severely reduces sampling efficiency elsewhere", which motivates the hybrid; the hybrid section itself was not seen |
| Partial shortcut (one DOF at a time); clearance methods | `:421` | Verified | Geraerts and Overmars, *IJRR* 26(8):845–863, 2007 (Utrecht portal and author PDF abstract) |
| RRT adapted to differential constraints by growing with controls (2001) | `:399` | Verified | LaValle and Kuffner, *IJRR* 20(5):378–400, 2001 (Illinois Experts record) |
| Textbooks of LaValle and of Choset et al. treat probabilistic completeness and these planners | `:40` | Verified (Choset); not verified (LaValle) | Choset et al. contents (CMU RI record) include "Sampling-Based Algorithms"; LaValle (2006) text not reachable |
| Choset et al., *Principles of Robot Motion: Theory, Algorithms, and Implementations*, MIT Press, 2005 | `:491` | Verified | MIT Press Bookstore and CMU RI records ("Implementations"; some library catalogues use the singular); seven authors as listed; same form as entries 1, 2 and 5 |
| LaValle, *Planning Algorithms*, Cambridge University Press, 2006 | `:500` | Verified | Publisher listings, ISBN 978-0521862059; author's page "Copyright 2006 Cambridge University Press" |
| Karaman and Frazzoli, *IJRR* 30(7):846–894, 2011 | `:495` | Verified | MIT DSpace record; DOI 10.1177/0278364911406761 |
| Cross-references to entries 1 and 2 | `:15–40`, `:71` | Verified | Source files: the second entry's Section 6.4 gives $10^{12}$ cells for six joints at 100 cells per joint and its Section 2.3 treats visibility graphs; the first entry's Sections 4.2 and 4.3 define probabilistic completeness and asymptotic optimality as used here, and its Section 4.3 agrees with Section 4.1 here |

### Not verified
- Hsu, Latombe and Motwani (1999), exponential decay of the failure probability: confirmed only from secondary sources by the same group and course notes, not from the paper (paywalled; fetch refused). The entry already attributes the claim to the paper, so no change is required; a stage with access should confirm it against the text.
- LaValle (2006): that the book treats probabilistic completeness and PRM/RRT was not checked against its text (fetch refused). Low risk: the sentence only points the reader to the book.
- Hsu et al. (2003): the hybrid strategy was seen only indirectly; the paper's hybrid section was not read.
- LaValle and Kuffner (2001): whether it also states the Voronoi-bias argument (F1 is written so that it does not depend on it).

**Fact-check verdict: fail** (no blocking finding; 1 should fix open: F1). Counts: 0 blocking, 1 should fix, 3 optional. It becomes pass when F1 is applied.

## Technical review

- Stage: technical review (EOS 6.4), 2026-10-17. Reviewer: technical-reviewer role (independent of the author and the earlier editors).
- Environment: Python 3.13.16, NumPy 2.5.3 (the entry states Python 3.13 and NumPy 2.5). Scratch programs: `/tmp/claude-0/mp/review/sampling-based-planning-prm-and-rrt/probe/`.
- Lint: `eos lint` 0 errors, 0 warnings, 2 suggestions (C5, kept). Not re-reported.

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| T1 | Should fix | `:212`, Section 3.1 | accuracy | "it is not added to the tree and is never checked for collision itself" is false when the sample lies within $\eta$ of the nearest vertex: `steer` then returns the sample itself, which is checked and added (1,228 of 3,953 iterations in the plane-map RRT runs). |
| T2 | Should fix | `:296`, Section 3.6 | accuracy | "PRM and RRT are both probabilistically complete under mild conditions" includes the fixed-$k$ nearest-neighbor PRM used throughout the entry, which Karaman and Frazzoli show is not necessarily probabilistically complete (not for $k = 1$). |
| T3 | Should fix | `:116`, Section 1.4 | accuracy | "the bands end at an elbow angle of about 1.7 rad": the printed grid's outermost obstacle cells are at ±1.83 rad, the bands reach 1.89 rad and a solution needs $|\theta_2| \ge 1.85$ rad; with 1.7 rad, "past 1.9 rad ... as the configuration-space picture requires" (`:292`) does not follow. |
| T4 | Should fix | `:363`, Section 5.1 | accuracy | The probability is defined as a share of the volume of $\mathcal{C}$, but the numbers (1.1%, 0.14%) are shares of the free area (shares of $\mathcal{C}$ would be 0.8% and 0.1%). |
| T5 | Should fix | `:405`, Section 6.1 | accuracy | "Each successful move shortens the path": a move whose two points lie on one straight run leaves the length unchanged (2 of 259 successful moves in the arm runs). Settles D9. |
| T6 | Should fix | `:461`, Exercise 4 answer | accuracy | A failed "coarse grid search in a low-dimensional projection" is evidence of infeasibility only if the grid's free set contains the true free space. Settles D10. |
| T7 | Optional | `:391`, Section 5.2 | evidence | "because it had only 150 uniform samples" explains a one-run difference (18 against 19 of 20); 40 further seeds confirm the direction (37 against 40 of 40) but the cause remains untested. |
| T8 | Optional | `:216`, Section 3.2 | accuracy | The Voronoi-region probability holds for the uniform iterations, with the region clipped to $\mathcal{C}$; goal-biased iterations always select the vertex nearest the goal. Settles D8. |
| T9 | Optional | `:116`, Section 1.4 | accuracy | "in which one of the links touches it": only the forearm can touch the disks. |
| T10 | Optional | `:306`, Section 4.2 | accuracy | "$n$ uniform samples are spaced roughly $n^{-1/d}$ apart" holds for unit volume; the spacing is $(\mu/n)^{1/d}$. |
| T11 | Optional | `:277`, Section 3.5 | accuracy | "the two planners compare in the same way": on the arm RRT-Connect needs fewer checks, but its median path is longer than RRT's (6.47 against 6.34 rad), the opposite of the plane map. |

### T1. The random sample can be added to the tree
- **Where:** `:212`, section "3.1 Growing a tree from the start".
- **Text:** "The random sample is only a direction to grow in; it is not added to the tree and is never checked for collision itself."
- **Problem:** In the listing (`:225–229`), `steer` returns `b.copy()` when `space.dist(a, b) <= eta`; that copy is the endpoint of the edge check and is appended to `V`. A wrapper around `steer` (`probe/sample_added.py`, plane-map RRT, $\eta = 0.5$ m, seeds 0 to 9) counted 1,228 such iterations out of 3,953.
- **Correction:** "When the random sample lies farther than $\eta$ from the tree, it is only a direction to grow in: it is not added and is never checked itself. When it lies within $\eta$, $q_{\mathrm{new}}$ is the sample."

### T2. Probabilistic completeness of the $k$-nearest PRM
- **Where:** `:296`, section "3.6 Completeness of roadmaps and trees".
- **Text:** "PRM and RRT are both probabilistically complete under mild conditions."
- **Problem:** Every PRM in the entry joins each vertex to its $k = 10$ nearest neighbors. Karaman and Frazzoli (2011) state that the $k$-nearest variant "is not necessarily probabilistically complete (e.g., it is not probabilistically complete for k = 1)". The analysis of Hsu, Latombe and Motwani that follows concerns roadmaps that join mutually visible milestones. Read with the entry's own PRM, the sentence claims more than the sources show.
- **Correction:** "A PRM that joins vertices within a connection radius, and RRT, are both probabilistically complete under mild conditions; a PRM with a fixed number $k$ of nearest neighbors, like the one in this entry, need not be (Karaman and Frazzoli show that it is not for $k = 1$)."

### T3. Where the bands end
- **Where:** `:116`, section "1.4 The test problems"; consequence at `:292`, Section 3.5.
- **Text:** "In the printed grid the bands end at an elbow angle of about 1.7 rad in magnitude." and "Every RRT-Connect path bends the elbow past 1.9 rad at some point, as the configuration-space picture requires."
- **Problem:** In the printed grid the topmost and bottommost rows that contain an obstacle cell (`#...` and `........#`) are centered at $\theta_2 = \pm 105° = \pm 1.83$ rad; the rows at $\pm 95°$ (1.66 rad) are the last ones crossed by whole bands. A 720 × 720 grid of the same checker (`probe/arm_bands.py`) gives a largest $|\theta_2|$ in $\mathcal{C}_{\mathrm{obs}}$ of 1.889 rad, and a flood fill shows that the start and goal are connected inside $|\theta_2| \le T$ only for $T \ge 1.854$ rad. That is what the shortcut paths show (extreme elbow angles 1.87 to 1.96 rad, `out_probe_shortcut.txt`). With "about 1.7 rad", the picture would not require "past 1.9 rad".
- **Correction:** "In the printed grid the bands reach an elbow angle of about 1.8 rad in magnitude; a finer grid shows that a path from the start to the goal must bend the elbow to at least about 1.85 rad." (The finer-grid computation should then be added to `show_maps.py` so that it is reproduced.) At `:292`: "Every RRT-Connect path bends the elbow past 1.9 rad at some point, beyond the 1.85 rad that the configuration space requires."

### T4. Share of $\mathcal{C}$ or of $\mathcal{C}_{\mathrm{free}}$
- **Where:** `:363`, section "5.1 Why narrow passages are hard".
- **Text:** "A uniform sample lands in a region with probability equal to the region's share of the volume of $\mathcal{C}$. ... With $w = 1.0$ m, a uniform sample lands in the door with probability about 1.1%; with $w = 0.125$ m, about 0.14%."
- **Problem:** $0.8/71.8 = 1.11\%$ and $0.1/71.1 = 0.141\%$ are shares of the free area, the right base for roadmap vertices, which are uniform samples that passed the point check (and the base of Exercise 3). Shares of $\mathcal{C}$ (100 m²) would be 0.8% and 0.1%.
- **Correction:** "A uniform sample that passes the point check, as every roadmap vertex does, lands in a region with probability equal to the region's share of the volume of $\mathcal{C}_{\mathrm{free}}$."

### T5. A shortcut need not shorten (D9)
- **Where:** `:405`, section "6.1 Shortcutting".
- **Text:** "Each successful move shortens the path, by the triangle inequality,"
- **Problem:** The triangle inequality gives "not longer"; equality holds when the replaced piece is straight, which happens on RRT-Connect paths because the greedy connection step produces collinear runs of $\eta$-steps. Replaying the shortcut loop one attempt at a time with the same generator stream (`probe/shortcut_moves.py`, seeds 0 to 9, 100 attempts each): 259 successful moves, 2 with no shortening, none lengthening. `shortcut` in `mp.py` accepts every free move, not only shortening ones, so the "keep if the program counts only moves that shorten" option of D9 does not apply.
- **Correction:** "No successful move lengthens the path, by the triangle inequality, and a move shortens it unless the replaced piece is already straight; the result stays collision-free up to the checker's resolution, because every new segment was checked."

### T6. Evidence of infeasibility (D10)
- **Where:** `:461`, Exercise 4 answer.
- **Text:** "If infeasibility is suspected, it needs other evidence, such as a check that the start and goal are free and in reach, or a coarse grid search in a low-dimensional projection."
- **Problem:** A failed search proves that no path exists only if every configuration it treats as blocked really is in collision, that is, if its free set contains the true free space. A coarse grid that marks a cell by checking one configuration, and a projection whose cells stand for many configurations, both fail this unless the marking is conservative. As written, the reader would take any failed coarse search as evidence, which contradicts the answer's own opening.
- **Correction:** "... such as a check that the start and goal are free and in reach, or a search on a coarse grid whose cells are marked blocked only when every configuration in them is in collision, so that a failure proves that no path exists."

### T7. One run in 20 explained causally
- **Where:** `:391`, section "5.2 Sampling where it matters".
- **Text:** "At the widest door the hybrid did slightly worse than uniform sampling (18 against 19 of 20), because it had only 150 uniform samples to cover the open rooms."
- **Problem:** A difference of one success in 20 cannot by itself support a comparison. Seeds 20 to 59 (`probe/more_seeds_narrow.py`) give uniform 40/40 and hybrid 37/40 at the 1.0 m door, so the direction holds, but no run tests the cause.
- **Correction (optional):** "At the widest door the hybrid did slightly worse than uniform sampling (18 against 19 of 20), probably because it had only 150 uniform samples to cover the open rooms."

### T8. Voronoi-region probability (D8)
- **Where:** `:216`. **Text:** "The probability of extending a vertex is proportional to the volume of its Voronoi region, so the tree is pulled toward the largest unexplored parts of the space."
- **Problem:** True for the uniform iterations (95% of them with goal bias 0.05), with each region intersected with $\mathcal{C}$ (on the torus for the arm); a goal-biased iteration always selects the vertex nearest $q_{\mathrm{goal}}$. "Extending" here means "selecting for extension"; the next paragraph explains that selected extensions can fail.
- **Correction (optional, recommended):** "For a uniform sample, the probability that a vertex is selected for extension is proportional to the volume of its Voronoi region within $\mathcal{C}$, so the tree is pulled toward the largest unexplored parts of the space."

### T9. Which link touches the disks
- **Where:** `:116`. **Text:** "Each disk becomes a curved band of configurations in which one of the links touches it."
- **Problem:** Distance from the shoulder to each disk minus its radius: $1.360 - 0.25 = 1.110$, $1.253 - 0.20 = 1.053$, $1.273 - 0.25 = 1.023$ m, all beyond $l_1 = 1.0$ m; a check of the obstacle cells confirms that only link 2 collides (`probe/arm_bands.py`).
- **Correction (optional):** "Each disk becomes a curved band of configurations in which the forearm touches it."

### T10. Sample spacing
- **Where:** `:306`. **Text:** "In a $d$-dimensional space, $n$ uniform samples are spaced roughly $n^{-1/d}$ apart."
- **Correction (optional):** "... spaced roughly $(\mu(\mathcal{C}_{\mathrm{free}})/n)^{1/d}$ apart, a length proportional to $n^{-1/d}$."

### T11. Arm comparison
- **Where:** `:277`. **Text:** "the two planners compare in the same way"
- **Correction (optional):** "RRT-Connect again needs fewer checks than RRT, and the two path lengths are similar".

### Recomputation and run log
- **Full reproduction.** The writer's programs were copied to `/tmp/claude-0/mp/review/sampling-based-planning-prm-and-rrt/run/` and `run.sh` run unchanged (12 min 48 s). All eight outputs are byte-identical to the writer's (`cmp`): `out_show_maps`, `out_optimal_plane`, `out_exp_plane`, `out_exp_optimal`, `out_exp_arm`, `out_exp_narrow`, `out_ref_arm`, `out_probe_shortcut`. Every seeded result reproduces exactly with the stated seeds.
- **Code and output in the article.** Both Python listings (`sample_free`/`prm_build`, `steer`/`rrt`) occur verbatim in `mp.py`. Every line of the eight `text` blocks, apart from the `...` elisions, occurs in the program outputs.
- **Optimal cost.** An independent visibility graph (`probe/cstar_indep.py`: dense sampling against the open rectangles, Floyd–Warshall) gives $C^* = 12.3023$, 12.4392, 12.5146 and 12.5651 m for the four doors, equal to `optimal_plane.py`. By hand: $2.6926 + 2.7313 + 3.7162 + 3.1623 = 12.3023$ m through $(3.5, 2.0)$, $(4.6, 4.5)$ and $(8.0, 6.0)$.
- **Maps.** Obstacle area $7.2 + 7.5 + 7.5 + 6.0 = 28.2$ m², free 71.80 m²; printed rows and columns match the rectangles; arm free cells 1136/1296 = 87.65%.
- **PRM* numbers.** $\gamma = 2 \times 1.224745 \times 4.780654 = 11.7102$ m; $r_n$ for $n$ = 500, 1000, 2000, 4000: 1.3055 (capped at 1.000), 0.9733, 0.7219, 0.5332 m; $\lceil 2e \ln n \rceil$ = 31, 34, 38, 42 for $n$ = 250, 500, 1000, 2000 (30.02, 33.79, 37.55, 41.32 before rounding); $e(1+1/d)$ = 5.437, 4.077, 3.624 for $d$ = 1, 2, 3, so $2e = 5.437$ satisfies the strict bound for $d \ge 2$ only. Exercise 1: $\ln 2000/2000 = 0.0038005$, square root 0.061648, $r_{2000} = 0.722$ m. All as printed.
- **Percentages and ratios.** PRM 13.88 and 13.15 m are 12.8% and 6.9% above $C^*$ ("7% to 13%"); RRT 16.91 m, 37.5%; RRT-Connect 16.29 m, 32.4% ("30% to 40%"); PRM 13.10 m, 6.5%; PRM* 12.49 m, 1.5%; RRT* 12.46 m, 1.3%; spreads 0.40, 0.13 and 0.13 m; $2456/22979.5 = 0.107$; $1158.5/2456 = 0.47$; $4655/1553 = 3.0$; $518.5/94 = 5.5$; $3277/227 = 14.4$; hybrid/uniform checks 14.6, 9.7, 8.4, 9.0 ("8 to 15"); shortcut $1 - 4.87/6.47 = 24.7\%$; $4.87/4.671 = 1.043$; $6.23/5.35 = 1.164$ ("a sixth"); $2\pi - 2.70 = 3.58$ rad; $2\pi - 6.2 = 0.083$ rad; Exercise 3: $21.0 + 7.9 = 28.9$ m² and $300 \times 0.1/71.1 = 0.42$; $100^6 = 10^{12}$. All as printed.
- **Arm checking resolution** (`:398`). The tip moves at most $\sigma_{\max}(J)\,\|\Delta q\|$; $\sigma_{\max}(J) \le \|J\|_F \le \sqrt{1.7^2 + 0.7^2} = 1.838$ m/rad, with equality at full extension (rank-one Jacobian), so $0.02 \times 1.838 = 0.037$ m is a tight bound. Correct.
- **Exercise 2.** `rrt(..., goal_bias=1.0, max_iter=2000)`, seed 0: no path, three vertices after 2000 iterations; the diagonal from $(1, 1)$ enters the box at its corner $(2, 2)$. Matches the answer.
- **Section 2.3 failures** (`probe/failed_seeds.py`, `probe/seed7.py`). PRM $n = 200$, seeds 2 and 7: exactly two components, all left-room vertices in one and all right-room vertices in the other, with no edge through the door (seed 7 has one vertex inside the door, joined only to the left room). The explanation at `:202` is confirmed.
- **Arm configuration space** (`probe/arm_bands.py`, 720 × 720 grid): free fraction 87.9%; largest $|\theta_2|$ in $\mathcal{C}_{\mathrm{obs}}$ 1.889 rad; start and goal connected within $|\theta_2| \le T$ only for $T \ge 1.854$ rad (T3); only link 2 collides (T9). That the bands separate start and goal at small elbow angles in both directions is confirmed.
- **Spread over seeds and generalization** (new seeds that the article does not use):
  - Plane map, seeds 10 to 39 (`probe/more_seeds_plane.py`): PRM $n = 200$ solved 29/30, construction checks median 22,808, cost median 13.74 m; PRM $n = 1000$ 30/30, 54,370 checks, 13.22 m; RRT 30/30, checks median 2,576 (1,072 to 5,223), cost 16.21 m; RRT-Connect 30/30, 1,024 checks, 15.84 m. The claims of Sections 2.3 and 3.5 hold (about 23,000 and 55,000 construction checks, RRT about a tenth of the small roadmap, RRT-Connect about half of RRT, paths 30% to 40% above $C^*$, wide spread). The two failures in ten at $n = 200$ are what seeds 0 to 9 gave; the text reports them as such, not as a rate.
  - Arm, seeds 10 to 29 (`probe/more_seeds_arm_opt.py`): RRT-Connect cost median 7.08 rad, 4.96 rad after 100 shortcuts, per-seed reduction median 23.5%; smallest extreme elbow angle on an RRT-Connect path 1.93 rad; checks median 1,331 for RRT-Connect against 2,152 for RRT. Sections 3.5 and 6.1 hold.
  - RRT* against the non-rewiring RRT, plane map, seeds 10 to 29: RRT* median 13.83, 13.03, 12.55, 12.46 m at 500, 1000, 2000, 4000 iterations (12.40 to 12.53 m at 4000); RRT 19.80 m falling to 19.72 m, worst seed 26.55 m throughout. Section 4.4 holds.
  - Narrow passages, seeds 20 to 59 (`probe/more_seeds_narrow.py`): uniform PRM 40, 27, 18, 7 of 40 and hybrid 37, 38, 37, 34 of 40 for doors of 1.0, 0.5, 0.25 and 0.125 m; RRT-Connect (seeds 10 to 29) median iterations 75.5, 109, 154, 453, worst 270, 775, 2348, 7203. The trends of Sections 5.1 and 5.2 hold; T7 covers the one-run comparison.
- Every seeded result is reported as the median, minimum and maximum over 10 or 20 seeds, as the Conventions paragraph says; the only claim resting on a one-run difference is T7. Seed-specific statements (seed 8 in Section 6.1 and Exercise 5) are presented as one seed's behavior.
- Nothing is presented as run that was not: every quoted output, the reference cost 4.671 rad and the probe results come from the programs named.
- Build: not rebuilt in this stage (no change to the source; the copy-edit stage built and link-checked the page).

**Technical verdict: fail** (no blocking finding; 6 should fix open: T1 to T6). Counts: 0 blocking, 6 should fix, 5 optional. It becomes pass when T1 to T6 are applied or answered in a Resolution section.

## Resolution

- Stage: resolution (EOS step 7), 2026-10-17, by the author. Developmental findings D1 to D7 were already applied by the editor; D8 to D11 are settled by T8, T5, T6 and F1/F3. No D finding remains open.
- Programs re-run: `show_maps.py` (extended for T3; its earlier lines are unchanged). No other program is affected by these changes. Every line of the nine `text` blocks in the article occurs in the `out_*.txt` files (checked by script).
- `eos lint`: 0 errors, 0 warnings, 2 suggestions (C5, kept). Build to a scratch folder exit 0; `check-links`: all internal links resolve (folder deleted).

| ID | Action | Exact change |
|---|---|---|
| F1 | Applied | Section 3.2: "LaValle and Kuffner described this **Voronoi bias** as the reason the tree spreads rapidly, hence the method's name." → "Kuffner and LaValle described this **Voronoi bias** as what makes the tree explore rapidly, the property the method is named for." |
| F2 | Applied | Section 4.1: "They proved that RRT is not:" → "They proved that, under mild technical conditions, RRT is not:" |
| F3, F4 | No change needed | As the fact-checker recorded. |
| T1 | Applied | Section 3.1: "The random sample is only a direction to grow in; it is not added to the tree and is never checked for collision itself." → "When the random sample lies farther than $\eta$ from the tree, it is only a direction to grow in: it is not added and is never checked itself. When it lies within $\eta$, $q_{\mathrm{new}}$ is the sample." |
| T2 | Applied | Section 3.6: "PRM and RRT are both probabilistically complete under mild conditions." → "A PRM that joins vertices within a connection radius, and RRT, are both probabilistically complete under mild conditions; a PRM with a fixed number $k$ of nearest neighbors, like the one in this entry, need not be (Karaman and Frazzoli show that it is not for $k = 1$)." The paragraph was also split before "For RRT the question" (lint paragraph length). Consistent with the first entry's Section 4.3. |
| T3 | Applied with changes | `show_maps.py` now also builds a 720 × 720 grid (0.5°, vectorized copy of the checker, marked at cell centers) and runs a bottleneck search for the smallest bound on $\|\theta_2\|$ joining start and goal; output "Fine grid 720 x 720: free fraction 0.879, largest \|theta2\| in C_obs 1.889 rad" and "smallest elbow bound joining start and goal: \|theta2\| <= 1.854 rad" (same values as the reviewer's probe). Section 1.4: "In the printed grid the bands end at an elbow angle of about 1.7 rad in magnitude." → "In the printed grid the bands reach an elbow angle of about 1.8 rad in magnitude." plus a sentence introducing the fine grid, a `text` block with the two output lines, and "A path from the start to the goal must therefore bend the elbow to at least about 1.85 rad, to the grid's resolution." Section 3.5: "as the configuration-space picture requires" → "beyond the 1.85 rad that the configuration space requires". `run.sh` already runs `show_maps.py`. |
| T4 | Applied | Section 5.1: "A uniform sample lands in a region with probability equal to the region's share of the volume of $\mathcal{C}$." → "A uniform sample that passes the point check, as every roadmap vertex does, lands in a region with probability equal to the region's share of the volume of $\mathcal{C}_{\mathrm{free}}$." |
| T5 | Applied | Section 6.1: "Each successful move shortens the path, by the triangle inequality, and the result stays" → "No successful move lengthens the path, by the triangle inequality, and a move shortens it unless the replaced piece is already straight; the result stays" |
| T6 | Applied with changes | Exercise 4 answer: "..., or a coarse grid search in a low-dimensional projection." → "... free and in reach. A search on a coarse grid also counts, provided its cells are marked blocked only when every configuration in them is in collision; a failure of that search proves that no path exists." (split in two sentences to stay under the sentence-length threshold; the projection was dropped). |
| T7 | Applied | Section 5.2: "because it had only 150 uniform samples" → "probably because it had only 150 uniform samples". |
| T8 | Applied | Section 3.2: "The probability of extending a vertex is proportional to the volume of its Voronoi region" → "For a uniform sample, the probability that a vertex is selected for extension is proportional to the volume of its Voronoi region within $\mathcal{C}$". |
| T9 | Applied with changes | Section 1.4: "in which one of the links touches it." → "in which the forearm touches it; all three disks lie beyond the reach of the upper arm." |
| T10 | Applied with changes | Section 4.2: "spaced roughly $n^{-1/d}$ apart." → "spaced roughly $(\mu(\mathcal{C}_{\mathrm{free}})/n)^{1/d}$ apart, where $\mu(\mathcal{C}_{\mathrm{free}})$ is the volume of the free space; this length is proportional to $n^{-1/d}$." The later "where $\mu(\mathcal{C}_{\mathrm{free}})$ is the volume of the free space and $\zeta_d$ ..." became "where $\zeta_d$ is the volume ..." to avoid defining it twice. |
| T11 | Applied | Section 3.5: "the two planners compare in the same way:" → "RRT-Connect again needs fewer checks than RRT, and the two path lengths are similar:" |

**Resolution verdict:** every blocking and should-fix finding (F1, T1 to T6) is applied; optional F2 and T7 to T11 are applied. No finding is open.

## Series review changes

From the series review `reviews/motion-planning.md` (2026-10-17), applied by the author side:

- F1: the PRM diagram of Section 2.1 is `flowchart TB` instead of `LR`; the built figure's min-width fell from 1005 px to 143 px (natural size 239 × 946 px).
- F6: the checking resolution in Sections 1.2 and 5.3 is $\varepsilon$, not $\delta$ (the first entry's safety margin).
- F7: the grid size in Section 1.1 and the Summary is $N$ ($N^d$ cells), as in Section 6.4 of the second entry.
- F8: the point check is related to the first entry's configuration check, with a link to its Section 5.1.
- F10: the answer to Exercise 4 now states both conditions for a grid proof of infeasibility (a whole-cell test and moves between cells that touch at a corner) and says that the second entry's grid planners give no such proof.
- F13: Section 5.3 identifies the 0.037 m tip bound with the bound $D$ of Section 5.3 of the first entry, linked.
- F15: Section 4.4 says that the printed radii are capped at $\eta = 1.0$ m and that the formula gives 1.306 m at $n = 500$ (recomputed: $11.71 \times (\ln 500/500)^{1/2} = 1.3055$ m).
- No program was changed and no quoted output changed.
