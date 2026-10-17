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
