# Editorial review: Following a Plan: Path Tracking and Reactive Obstacle Avoidance

- Path: `src/content/blog/path-tracking-and-reactive-avoidance.mdx` · Route: `/blog/path-tracking-and-reactive-avoidance` · Type: article, series entry 5 of 5 (`motion-planning`)
- Reviewed against: `editorial/standards.md` 1.0, `editorial/glossary.json`, `plugins/editorial-os/references/review-protocol.md`, the series overview `src/content/series/motion-planning.md`, the four earlier entries (headings and the sections this entry cites), `what-is-a-robot.mdx` Sections 2.2, 4, 5 and 5.3, and the writer's programs in the scratch folder (read, not re-run: re-running belongs to the technical stage).
- Stages in this report: developmental (EOS step 6.1) and copy (6.2), both by an editor who did not write the entry. Line numbers refer to the revised file.

## Developmental review

The entry does its job for the stated reader. It opens from the fourth entry's output (a timed plan), says why a plan is not enough, and states what the entry adds. Each section opens with its concept before the equations: the layered architecture, then the robot model, then two tracking laws, then two reactive methods, then the system that combines them. Every method has a derivation or a worked example and a simulation whose output is quoted, and each section states its limits. Sections 3.3 and 4.4 compare the linear analysis with the simulation and say where it fails, which is the right depth for this reader. The Summary table and the closing paragraph return to the series objectives, as standards 6.2 requires of the last entry. The eight `##` headings and every `###` heading are unchanged, so the one fragment another entry links to (`#6-replanning-and-layered-navigation`, from `graph-search-dijkstra-and-a-star.mdx`) still resolves.

Length: about 5,650 words of prose (alphabetic words only, without code, display math, tables and references; about 6,000 if each inline formula counts as a word). That is within the series standard of 3,500 to 6,000 words. The cuts below removed a table of contents in prose, a repeated statement from the introduction and a recap of the second entry. They did not remove any argument.

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| D1 | Should fix | `:17`, opening | purpose | The second opening paragraph listed the sections as a table of contents in prose, and "all four earlier entries" named only three of them. |
| D2 | Should fix | `:29`, `:37`, Section 1 figure | consistency | The diagram had no tracking controller, and the caption said "three layers", which did not match the prose. |
| D3 | Should fix | `:95`, Section 2.4 | publishing | "Support code not shown in the listings is in the program files" pointed readers to files the site does not publish. |
| D4 | Should fix | `:452`, Section 6.2 | structure | The section restated the second entry's account of D* Lite instead of referring back to it. |
| D5 | Should fix (for technical reviewer) | `:93`, Section 2.4 | accuracy | "Without the lag and the limit, a tracking controller could be made arbitrarily aggressive and would never oscillate" ignores the 20 Hz sample-and-hold. |
| D6 | Should fix (for fact-checker) | `:458`, `:467`, Section 6.3 | evidence | The list of recovery behaviors is presented as "typically" used, and the section says they make a system "fail rarely", but neither claim has a source. |
| D7 | Optional | `:452`, Section 6.2 | consistency | The link to D* Lite targets Section 5 of the second entry; the method is in its Section 5.4. |
| D8 | Optional (for technical reviewer) | `:264`, Section 5.1 | accuracy | "every method of this kind can be led into a situation it cannot escape on its own" is a universal claim with no support. |
| D9 | Optional | `:141`, Section 3.3 | structure | The prose never discusses the RMS column of the look-ahead table. |

### D1. Opening reads as a list of contents and miscounts the earlier entries
- **Where:** `src/content/blog/path-tracking-and-reactive-avoidance.mdx:17`, second opening paragraph
- **Text:** "The entry builds on all four earlier entries: the configuration space of the first, the grid planners of the second for replanning and the timed references of the fourth. ... Section 1 places tracking and avoidance in that structure, Section 2 models a differential-drive robot, ... and Section 6 assembles a navigation system that replans and recovers."
- **Problem:** Standards 6.1 ask for an introduction "without a table of contents in prose" (the developmental agent definition, item 6). "All four" named three entries; the third entry's planners are used in Section 6.2 but were not mentioned. The paragraph also did not state what the examples assume (standards 6.2, item 1).
- **Correction (applied):** The sentence listing the sections is cut. The third entry is added and linked, and each entry's role is named: "...; the grid planners of the second and the sampling-based planners of the third, which Section 6 uses for replanning; and the timed references of the fourth, which trajectory tracking follows." A closing sentence states the assumption: "The examples simulate one small differential-drive robot and take its pose estimate as exact; Section 6.4 returns to that assumption." (This matches Section 6.4, which says the controllers take the estimate as truth.)

### D2. Figure and prose describe different layers
- **Where:** `:29` (Mermaid node `L`) and `:37` (caption), Section 1
- **Text:** node "Local planner<br/>nearby obstacles, many times per second"; caption "the three layers of a mobile robot's navigation software"
- **Problem:** The prose names a global planner, a local planner, a tracking controller and wheel controllers, and says that the local planner and the tracking controller together form the reactive layer. The figure left out the tracking controller, and its "three layers" were not the three layers of the deliberative, executive and reactive description in the next paragraph.
- **Correction (applied):** The node now reads "Local planner and tracking controller<br/>many times per second". The caption now reads "the layers of a mobile robot's navigation and control software". The build renders the diagram (checked in a scratch build).

### D3. Reference to unpublished program files
- **Where:** `:95`, Section 2.4, end of the second paragraph
- **Text:** "Support code not shown in the listings is in the program files."
- **Problem:** The programs are not published with the site, so readers have no "program files" to open. The sentence promises something the page cannot deliver.
- **Correction (applied):** "The listings of Sections 3 and 4 show the control laws only; the path construction, the error measurement and the simulation loop are omitted." (This matches `common.py`: `make_path`, `cross_track`, `step`.)

### D4. Recap of the second entry's D* Lite
- **Where:** `:452`, Section 6.2
- **Text:** "It searches from the goal toward the robot, so obstacles discovered near the robot require only a small repair: plan with what is known, move, sense, repair."
- **Problem:** Standards 6.1 (no redundancy across a series: a later entry refers back instead). The second entry, Section 5.4, already explains the backward search and why changes near the robot are cheap.
- **Correction (applied):** The sentence now keeps only the consequence the navigation system needs and leaves the mechanism to the linked entry: "Because it searches backward from the goal, a change near the robot needs only a small repair. Navigation then becomes a cycle: plan with what is known, move, sense, repair."

### D5. Claim that only the lag and the limit cause oscillation (for the technical reviewer)
- **Where:** `:93`, Section 2.4, end of the first paragraph
- **Text:** "Without the lag and the limit, a tracking controller could be made arbitrarily aggressive and would never oscillate."
- **Problem:** The same paragraph says the controller runs at 20 Hz and holds its command between updates. A sampled loop with a zero-order hold also limits the usable gain, and with a high enough gain it oscillates or goes unstable, even with no lag and no saturation. As written, the claim seems true only for continuous-time control. Text left unchanged (technical claim).
- **Correction (recommended):** Confirm, then for example: "Without the lag, the limit and the sampling, a tracking controller could be made arbitrarily aggressive without oscillating."

### D6. Recovery behaviors: practice described without a source (for the fact-checker)
- **Where:** `:458` ("runs **recovery behaviors** in order of increasing cost, typically:") and `:467` ("they make a system built from methods with known failure modes fail rarely and visibly")
- **Problem:** Standards 7.2: a claim about common practice that is not common knowledge needs a source. "Typically" claims that the list is common practice, and "fail rarely" is a claim about how often systems fail. No reference supports either. Text left unchanged.
- **Correction (recommended):** Either cite a source that describes such a sequence, or qualify the claim: "...runs **recovery behaviors** in order of increasing cost, for example:" and "...but they make the failures of a system built from methods with known failure modes visible and often recoverable."

### D7. Link to the whole of Section 5 for D* Lite
- **Where:** `:452`, Section 6.2
- **Text:** "described in [Section 5 of the second entry](/blog/graph-search-dijkstra-and-a-star#5-faster-any-angle-and-incremental-search)"
- **Problem:** D* Lite is in Section 5.4, "Incremental replanning: D* Lite". The link is not wrong, but it is less precise than it could be. The link target is not changed at this stage.
- **Correction (recommended):** "described in [Section 5.4 of the second entry](/blog/graph-search-dijkstra-and-a-star#54-incremental-replanning-d-lite)", after checking the fragment against the built page.

### D8. Universal claim about reactive methods
- **Where:** `:264`, Section 5.1
- **Text:** "The price is a local view: every method of this kind can be led into a situation it cannot escape on its own."
- **Problem:** The entry shows this for the two methods it treats (scenes B and C, the U trap), but states it for every reactive method. It reads as a theorem without one.
- **Correction (recommended):** Confirm the claim or narrow it: "The price is a local view: both methods of this section can be led into situations they cannot escape on their own (Sections 5.2 and 5.3)."

### D9. Unused table column
- **Where:** `:141`, Section 3.3 output
- **Problem:** The RMS column is defined in the text but never interpreted; it repeats the corner-error trend. The column is program output, so it stays. Optional: add half a sentence, or leave it as is.
- **Correction:** None applied.

**Verdict (developmental): pass.** D1 to D4 are applied. D5 and D6 concern technical and factual claims, which this stage may not change; they are handed to the technical reviewer and the fact-checker, and the item cannot publish until they are resolved.

## Copy edit

`npm run eos -- fix <path> --rules spelling-variant,terminology` applied 0 fixes. The first lint run on the writer's draft showed 3 errors (links to the third entry, which did not exist yet; it now exists and they resolve), 0 warnings and 13 suggestions. After the edits: **0 errors, 0 warnings, 5 suggestions**, all kept (see C7). No em dashes, contractions, banned intensifiers or "we" outside a derivation step were found; the one "we" ("Differentiating $\dot{e}_y$ once more, we obtain", `:202`) is a derivation step. Headings are in sentence case, abbreviations (RMS, DWA) are expanded at first use, and the title (64 characters) and description (one sentence, within 70 to 165 characters) meet standards 8.1.

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| C1 | Should fix | `:17`, `:39`, `:93`, `:268`, `:354`, `:446`, `:452` | language | There were sentences over 45 words, and commas before the last item of a list against house style. |
| C2 | Should fix | `:306`, Section 5.2 | language | The three potential-field scenes were packed into one 63-word sentence. |
| C3 | Should fix | `:392`, Section 5.3 | consistency | "The row below the winner" pointed at the wrong row of the output. |
| C4 | Should fix | `:340`, Section 5.2 | language | "0.63 m before the gap" did not say where the gap is measured from. |
| C5 | Optional | `:148`, `:162`, `:430` | language | There were vague or loaded words: "reacts violently", "one intuitive parameter", "They differ in what they respect". |
| C6 | Optional | `:23`, `:65`, `:471` | language | There was a repeated statement, a stock phrase and an inexact count. |
| C7 | Optional | `:542`-`:545`, References | language | The acronym-expansion suggestions in the reference list are kept (reason below). |

### C1. Long sentences and serial commas
- **Where:** `:17` (two sentences, 47 and 37 words; "simulated, and take", which lint flags as a serial comma), `:39` (46 words), `:93` ("runs every fifth step, at 20 Hz, and holds"), `:268` ("the goal attracts it, obstacles repel it, and the robot moves"), `:354` (46 words; "..., a clearance term ..., and a velocity term"), `:446` (50 words), `:452` (50 words)
- **Problem:** Standards 5.1 (no serial comma) and 5.2 (a sentence over about 45 words is flagged for a second look). In every case the rest of the sentence made the parts hard to follow.
- **Correction (applied):** The long sentences are split into two each. "every fifth step (20 Hz) and holds"; "obstacles repel it and the robot moves"; "DWA picks the one with the highest weighted sum of three terms. A heading term rewards facing the goal, a clearance term rewards distance to the nearest obstacle on the arc and a velocity term rewards speed."; "... often with a term that rewards staying near the path. The point plays the role of the goal point of pure pursuit."

### C2. Scene descriptions in one sentence
- **Where:** `:306`, Section 5.2
- **Text:** "There are three scenes: (A) one disk ...; (B) a U-shaped wall ...; (C) two disks ... between their surfaces:"
- **Problem:** The sentence is 63 words long and introduces a code block. Readers look these scenes up again when they read the output and the ASCII map.
- **Correction (applied):** "The robot starts at $(0, 0)$ and the goal is at $(10, 0)$, in three scenes:" followed by a three-item list with the same wording, then "The program prints:". No numbers changed.

### C3. Wrong row locator in the DWA output
- **Where:** `:392`, Section 5.3
- **Text:** "The row below the winner shows that speed and turning interact: at the same $\omega = 0.20$ rad/s but $v = 0.525$ m/s, ..."
- **Problem:** In the quoted output the row below the winner (`0.475 +0.20`) is `0.450 +0.20`. The row described, `0.525 +0.20 ... 0.453`, is the fourth row.
- **Correction (applied):** "The fourth row shows that speed and turning interact. At the same ... the curvature falls from 0.42 to 0.38 m$^{-1}$, so the wider arc clips the wall's upper end after 1.36 m and the clearance drops to 0.453." The numbers are unchanged.

### C4. Unclear reference point for "before the gap"
- **Where:** `:340`, Section 5.2, scene C
- **Text:** "the robot stops at $(4.37, 0)$, 0.63 m before the gap"
- **Problem:** The disks begin at $x = 4.6$ m, so "the gap" could mean several places. The number is $5 - 4.37 = 0.63$, so it is measured to the line through the disk centers at $x = 5$ m.
- **Correction (applied):** "0.63 m before the line through the two centers". The number is unchanged.

### C5. Vague or loaded words
- **Where and correction (applied):** `:148` "reacts violently to the initial offset" became "overcorrects the initial offset". `:162` "it has one intuitive parameter, needs no special treatment of curvature jumps and degrades gracefully, since ..." became "its one parameter has a geometric meaning, curvature jumps need no special treatment and a robot far from the path heads back toward it" (the same three properties; "degrades gracefully" was the claim the "since" clause already stated). `:430` "They differ in what they respect." became "They differ in what they search and in what they guarantee." (this matches the rows of the comparison table).

### C6. Repetition, stock phrase, inexact count
- **Where and correction (applied):** `:23` cut "and both the map and the robot model are always somewhat wrong", which repeated the opening paragraph ("for a robot model that is never exact"). `:65` "harder than it looks" became "hard", and the Brockett sentence became "no smooth feedback law that depends on the state alone can asymptotically stabilize it to a fixed pose" (the same claim, in the active voice). `:471` "Several problems remain open" became "Four problems remain open", matching the list.

### C7. Lint suggestions kept
- `acronym-expansion` for "MIT" (`:542`), "CMU", "RI", "TR" (`:543`, in the report number `CMU-RI-TR-92-01`) and "AAAI" (`:545`): these are publisher names and a report identifier in bibliographic entries. Expanding them would change how the sources identify themselves, and the reference format in standards 7.3 uses publisher names as published.
- The serial comma in the Koren and Borenstein list (`:342`, "..., no passage between closely spaced obstacles, and oscillations near obstacles and in narrow passages") is kept by the exception in standards 5.1. Both of the last two items contain "and", and without the comma they would run together. Lint does not flag it.

**Verdict (copy): pass.** No blocking or should-fix copy finding remains open. Final `npm run eos -- lint src/content/blog/path-tracking-and-reactive-avoidance.mdx`: 0 errors, 0 warnings, 5 suggestions (C7).

A scratch build (`astro build --outDir`, since deleted) rendered the page and the revised Mermaid diagram. At the time of the build, the link checker reported only the links to the third entry, which did not yet exist. The page shows no text glued to an inline element; the `m<span` matches are KaTeX exponents in units such as "m$^{-1}$".

<!-- Later stages (fact-check, technical review, resolution, QA) append their sections below. -->

## Fact-check

Stage: EOS step 6.3, by a reviewer who did not write or revise the entry. Method: every reference was looked up with web search (library catalogues, DBLP and publisher listings, author repositories, reference lists in later papers). Direct fetches of DBLP, IEEE Xplore, arXiv and the NPS archive were refused by this session's network proxy. Every claim that rests only on search-result snippets or reference lists is marked as such. Earlier entries of the series cite Choset et al., Lynch and Park, Siciliano et al., Gat and Koenig and Likhachev in the same form (checked with grep), so the reference list is consistent across the series.

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| F1 | Should fix | `:101`, Section 3.1 | evidence | "The method was developed at Carnegie Mellon University for outdoor vehicles" could not be confirmed from Coulter's report or any other source. |
| F2 | Should fix | `:458`, `:467`, Section 6.3 (D6) | evidence | "typically" and "fail rarely" have no source; common navigation software confirms the kinds of behaviors listed but not their order or a failure rate. |
| F3 | Optional | `:545`, References (Gat) | evidence | The chapter's pages (195–210) are given by one secondary source only, so they are not added. |
| F4 | Optional | `:344`, Section 5.2 | evidence | The 1992 paper gives an explicit formula for sphere worlds. The extension to "worlds that can be mapped onto them" is confirmed only from later papers, which attribute it to a diffeomorphism construction. |

### F1. Origin of pure pursuit
- **Where:** `src/content/blog/path-tracking-and-reactive-avoidance.mdx:101`, Section 3.1 "The geometry"
- **Text:** "The method was developed at Carnegie Mellon University for outdoor vehicles; Coulter's 1992 report documents its implementation, derives the curvature formula and discusses the effect of the look-ahead distance."
- **Problem:** The report exists: R. C. Coulter, CMU-RI-TR-92-01, Robotics Institute, January 1992 (CMU RI publication record; DTIC ADA255524). Its abstract confirms that it describes the implementation, gives a geometric derivation and discusses performance "as a function of its parameters". The search did not confirm who developed the method or where. The abstract only says the algorithm had "general success over the past few years". Standards 7.2: an unverified historical attribution is qualified or removed.
- **Correction:** "Coulter's 1992 technical report from Carnegie Mellon University documents an implementation of the method, derives the curvature formula and examines how its performance depends on the look-ahead distance." (This drops the origin claim and keeps everything the source supports.)

### F2. Recovery behaviors (settles D6)
- **Where:** `:458` ("runs **recovery behaviors** in order of increasing cost, typically:") and `:467` ("they make a system built from methods with known failure modes fail rarely and visibly")
- **Problem:** Widely used open-source navigation software confirms the kinds of behavior listed. The ROS 1 `move_base` defaults are a conservative costmap reset, a rotation in place and an aggressive costmap reset, followed by abort. The Nav2 default behavior tree uses clear costmaps, spin, wait and back up, plus replanning. Neither uses the article's order (both clear the costmap before waiting). "Typically" therefore claims more than these sources show. "Fail rarely" is a claim about failure frequency, and no source supports it. These sources were seen only through search results, not fetched, so they cannot be cited as they stand (standards 7.3: no URL that has not been fetched).
- **Correction (D6 settled, apply both):** "...and runs **recovery behaviors**, roughly in order of increasing cost, for example:" and "...but they make a system built from methods with known failure modes fail visibly, and often recover from the failure." (The editor's wording for D6 is equally acceptable.)

### F3. Gat chapter pages
- **Where:** `:545`, References
- **Problem:** Standards 7.3 asks for pages when they exist. The range 195–210 appears only in a Wikipedia reference. The chapter's existence, title, editors and AAAI Press/MIT Press imprint are confirmed by a hosted copy and reference lists. One later paper gives the year as 1997, but the catalogue year of the volume is 1998.
- **Correction:** Leave the entry as it is unless the page range is confirmed from the book's contents page. Then add "pp. 195–210" before the year, in this entry and in `what-is-a-robot.mdx`.

### F4. Scope of the navigation-function result
- **Where:** `:344`
- **Text:** "for worlds of spherical obstacles and worlds that can be mapped onto them"
- **Problem:** The abstract in the Penn repository describes the explicit construction for (generalized) sphere worlds. Later papers attribute the extension to star worlds to a suitable diffeomorphism, which Rimon and Koditschek developed in related work. Whether the 1992 paper itself covers that extension was not confirmed.
- **Correction (optional):** "...for worlds of spherical obstacles, and, through a change of coordinates, for worlds that can be mapped onto them."

### Verification table

| Claim or reference | Location | Status | Source |
|---|---|---|---|
| Brockett, "Asymptotic stability and feedback stabilization," in *Differential Geometric Control Theory*, eds. Brockett, Millman, Sussmann, Birkhäuser, pp. 181–191, 1983 | `:541` | Verified | Library catalogue (Kaiyodai OPAC: Birkhäuser, Boston, 1983, proceedings of the 1982 Michigan Tech conference); MaRDI/zbMATH Prog. Math. 27, 181–191 (Zbl 0528.93051). Optional addition: "Progress in Mathematics, vol. 27". |
| Brockett's necessary condition fails for the unicycle; no smooth state feedback stabilizes a fixed pose | `:65`, `:530` | Verified | Theorem 1(iii) of the paper (image of $(x,u)\mapsto f(x,u)$ must contain a neighborhood of 0, for C¹ feedback), as cited by Kvalheim (arXiv 2205.07840). Checked directly: $(0, \varepsilon, 0)$ is not attained near the origin, since $v\cos\theta = 0$ and $v\sin\theta = \varepsilon$ with $\theta$ small has no solution |
| Choset et al., *Principles of Robot Motion*, MIT Press, 2005 (seven authors, order as given) | `:542` | Verified | Google Books / Internet Archive record (ISBN 9780262033275); CMU RI publication record |
| Attractive potential quadratic within $d^*$, conic beyond, "in the form given by Choset et al." | `:268`–`:276` | Verified in form | Choset's 16-735 course slides and a course page based on Chapter 4 describe this switch. The constant $-\tfrac12 k_a {d^*}^2$ follows from continuity at $d^*$ (checked: both branches equal $\tfrac12 k_a {d^*}^2$ there, and the gradient magnitude beyond is $k_a d^*$). The book's equation text was not seen |
| Coulter, CMU-RI-TR-92-01, 1992; derives the curvature and discusses look-ahead | `:101`, `:543` | Verified | CMU RI publication record; DTIC ADA255524 |
| Pure pursuit "developed at CMU for outdoor vehicles" | `:101` | Not verified | See F1 |
| Fox, Burgard, Thrun, *IEEE RAM* 4(1):23–33, 1997; developed for synchro-drive robots; searches velocities that can be reached and from which the robot can stop | `:348`, `:544` | Verified | CMU RI record (March 1997); UW RSE abstract; DOI 10.1109/100.580977 |
| Gat, "On Three-Layer Architectures," AAAI Press/MIT Press, 1998; three layers | `:39`, `:545` | Verified (pages: see F3) | Hosted copy (BIU course site); Wikipedia reference list |
| Kanayama, Kimura, Miyazaki, Noguchi, ICRA 1990, pp. 384–389 | `:193`, `:546` | Verified | DBLP listing (ICRA 1990: 384–389) via search; DOI 10.1109/ROBOT.1990.126006 in reference lists. Not to be confused with the IROS 1991 paper "...for a non-holonomic mobile robot" |
| The law $v = v_r\cos e_\theta + K_x e_x$, $\omega = \omega_r + v_r(K_y e_y + K_\theta \sin e_\theta)$ and the robot-frame error | `:175`–`:200` | Verified by derivation, with the paper's Lyapunov function | The paper's Lyapunov function, from the full-text OCR summarized in search results, is $V = \tfrac12(e_x^2+e_y^2) + (1-\cos e_\theta)/K_y$. With the law as written and the error dynamics of `:184`, $\dot V = -K_x e_x^2 - v_r K_\theta \sin^2 e_\theta / K_y \le 0$ (derived, Technical review log item 4). Only this law makes that $V$ work |
| "stable for any positive gains when $v_r > 0$"; critical damping $K_\theta^2 = 4K_y$ | `:200`, `:208` | Verified | Paper abstract ("any set of positive parameters makes the system stable"; critical damping from linearization) and Corollary, via search results |
| Khatib, *IJRR* 5(1):90–98, 1986; potential field for manipulators and mobile robots; FIRAS repulsion form | `:268`, `:278`, `:547` | Verified | SAGE DOI 10.1177/027836498600500106 (vol. 5, issue 1), March 1986 |
| Koenig and Likhachev, "D* Lite," AAAI-02, pp. 476–483, 2002 | `:452`, `:548` | Verified | ML Anthology / BibTeX record, pp. 476–483. AAAI-02 is the Eighteenth National Conference |
| Koren and Borenstein, ICRA 1991, pp. 1398–1404 | `:342`, `:549` | Verified | The paper's first page (author-hosted copy, Sacramento, April 7–12, 1991); DBLP; DOI 10.1109/ROBOT.1991.131810 |
| Koren and Borenstein's list of inherent problems (traps, no passage between close obstacles, oscillations near obstacles and in narrow passages) | `:342` | Verified against the paper's known structure | Abstract confirmed ("systematic criticism of the inherent problems"). The four problems are the paper's own section topics, as recalled; the full text was not fetched (see Not verified) |
| Lynch and Park, *Modern Robotics*, CUP, 2017; Siciliano et al., Springer, 2009; both derive the unicycle and wheel relations | `:53`, `:550`, `:552` | Verified | Standard textbooks, cited identically in four or five other entries of the site |
| Rimon and Koditschek, *IEEE TRA* 8(5):501–518, 1992 | `:344`, `:551` | Verified | Reference lists giving 8(5):501–518 (Springer chapter; arXiv 2306.16160 via Semantic Scholar); ModelDB (vol. 8, 1992); Penn repository record |
| Navigation functions: only minimum at the goal, convergence from almost every initial configuration, sphere worlds | `:344` | Verified (extension: F4) | Penn repository abstract |
| Unicycle and nonholonomic definitions consistent with What Is a Robot? Section 2.2; layered architecture with its Section 5.3; occupancy grid with the second entry's Section 2.1; D* Lite with its Section 5.4; $q(t) = \sigma(s(t))$ with the fourth entry's Section 1.1 | `:17`–`:63`, `:448`, `:452`, `:168` | Verified | The cited sections, read in full |
| Every internal link fragment (`#53-layered-hybrid-architectures`, `#4-loops-within-loops`, `#5-organizing-the-software`, `#22-degrees-of-freedom-and-mobility`, `#1-paths-and-trajectories`, `#3-obstacles-in-configuration-space`, `#2-from-a-map-to-a-graph`, `#5-faster-any-angle-and-incremental-search`, `#72-localization-and-mapping`) and the insight `closing-the-sim-to-real-gap` | throughout | Verified | Headings of the target files (slugs derived from the headings); the insight file exists. No site build was run at this stage |

### Not verified

- Pure pursuit's origin at CMU (`:101`): the sources were not reachable; recommended correction F1.
- The exact wording of Choset et al.'s attractive potential (`:268`): the book's text was not seen. The form is confirmed by the author's course slides and by the continuity derivation, so no change is needed.
- Gat chapter pages 195–210: only one secondary source (F3).
- Whether Rimon and Koditschek (1992) itself covers worlds mapped onto sphere worlds (F4).
- Koren and Borenstein's list of four problems (`:342`): taken from knowledge of the paper's section structure; the full text was not fetched. The risk is low and no change is recommended.
- The Kanayama law and error definitions were not read in the original typeset paper; IEEE and NPS were unreachable. They are confirmed indirectly: the paper's Lyapunov function and its critical-damping corollary, seen through OCR excerpts in search results, hold exactly for the law and errors as written (derivation in the Technical review). The writer's open question is settled to that extent.

**Verdict (fact-check): fail** until F1 and F2 are applied. Counts: 0 blocking, 2 should fix, 2 optional. Every reference exists, and its bibliographic details are confirmed, including the four items the writer could not confirm: Rimon and Koditschek issue 5 and pages 501–518; the Kanayama law, through its Lyapunov function and corollary; the attractive potential, in form; and Brockett 1983 (Birkhäuser, pp. 181–191, Progress in Mathematics 27).

## Technical review

Stage: EOS step 6.4, by a reviewer who did not write or revise the entry. Environment: Python 3.13.16, NumPy 2.5.3 (matches the stated Python 3.13 / NumPy 2.5). Scratch files are in `/tmp/claude-0/mp/review/path-tracking-and-reactive-avoidance/` (`out.txt`, `recompute.py`, `experiments.py`, `d5_zoh.py`, `exp2.py`).

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| T1 | Should fix | `:93`, Section 2.4 (D5) | accuracy | The 20 Hz sample-and-hold alone makes an aggressive gain unstable, with no lag and no limit. |
| T2 | Should fix | `:156`, Section 3.3 | accuracy | The 0.258 m overshoot at $L_d = 0.15$ m comes mainly from the turn-rate limit, not the phase lag the text puts first. |
| T3 | Should fix | `:264`, Section 5.1 (D8) | accuracy | "every method of this kind can be led into a situation it cannot escape" is false under the entry's own definition; Bug algorithms are a counterexample. |
| T4 | Should fix | `:411`, `:426`, Section 5.3 | accuracy | "The closest approach, 0.054 m" is the clearance at the 0.25 s control instants only; along the path the closest approach is 0.050 m. |
| T5 | Optional | `:392`, `:394`, `:516`–`:521` | consistency | One $s_{\mathrm{hit}}$ value is quoted from the program's 0.02 m sampling (1.26 m) and the other is computed analytically (0.35 m; the program uses 0.36 m). |
| T6 | Optional | `:258`, Section 4.5 | accuracy | "as Brockett's result in Section 2.2 implies" attributes to Brockett a consequence of $v_r > 0$. |

### T1. Sampling also limits the gain (settles D5)
- **Where:** `:93`
- **Text:** "Without the lag and the limit, a tracking controller could be made arbitrarily aggressive and would never oscillate."
- **Problem:** Confirmed as D5 suspected. Linearized pure pursuit on a straight line, with no lag and no limit, is a double integrator $\dot e = v\theta$, $\dot\theta = v\kappa$. With $\kappa = -2e/L_d^2 - 2\theta/L_d$ applied through a zero-order hold at $T = 0.05$ s (exact discretization, `d5_zoh.py`), the largest closed-loop pole magnitude is 0.833 at $L_d = 0.15$ m, 0.375 at 0.04 m and 0.250 at 0.03 m. At $L_d = 0.02$ m it is **2.03**, so the loop is unstable. In the continuous-time model the damping stays at 0.707 for every $L_d$, so the instability comes from the sampling alone.
- **Correction:** "Without the lag, the limit and the 20 Hz sampling, a tracking controller's gains could be raised without bound and the loop would stay stable; with them, aggressive gains overshoot, oscillate or go unstable."

### T2. Cause of the overshoot at $L_d = 0.15$ m
- **Where:** `:156`
- **Text:** "At $L_d = 0.15$ m, $\omega_n = 4.7$ rad/s is no longer small compared with the drive's bandwidth ... so the extra phase lag reduces the damping; the 0.5 m initial error ... also saturates $\omega$. Both effects lie outside the linear model and produce the 0.258 m overshoot."
- **Problem:** I re-ran the same simulation (`experiments.py`, same path, start and controller) with each effect switched off:

  | Lag | Turn-rate limit | Overshoot (m) |
  |---|---|---|
  | none | none | 0.018 |
  | 0.1 s | none | 0.029 |
  | none | 1.5 rad/s | 0.166 |
  | 0.1 s | 1.5 rad/s | 0.258 (the article's value, reproduced) |

  The limit is active in 83 of the controller updates of the original run. The lag alone adds 0.011 m; the limit, together with its interaction with the lag, causes the rest. The text presents the lag first and the saturation as an addition, which misleads about the cause. Both effects are properties of the drive, so the closing sentence stays true.
- **Correction:** "At $L_d = 0.15$ m the 0.5 m initial error, more than three times $L_d$, drives $\omega$ to its 1.5 rad/s limit, and the drive lag ($\omega_n = 4.7$ rad/s against a bandwidth of $1/0.1 = 10$ rad/s and the 20 Hz update) adds phase lag on top. Run separately, the lag alone gives an overshoot of 0.029 m and the limit alone 0.166 m; together they produce the 0.258 m. The look-ahead distance therefore has a lower limit set by the robot's drive, here mostly by its turn-rate limit."

### T3. Universal claim about reactive methods (settles D8, raised to should fix)
- **Where:** `:264`
- **Text:** "The price is a local view: every method of this kind can be led into a situation it cannot escape on its own."
- **Problem:** The entry defines a reactive method as one that "computes a command from the current readings and the robot's state, without searching the map". The Bug algorithms of Lumelsky and Stepanov (1987) fit that definition. They use only local sensing plus a few remembered values (the hit point and the distance to the goal), and they are guaranteed to reach the goal whenever it is reachable. They are slow, but they cannot be trapped. The claim is true for the two methods the section treats, which is all the entry demonstrates.
- **Correction:** "The price is a local view: both methods of this section can be led into situations they cannot escape on their own (Sections 5.2 and 5.3)."

### T4. DWA closest approach is sampled at the control instants
- **Where:** `:411` (output) and `:426` ("The closest approach, 0.054 m, is set by the 0.05 m safety margin")
- **Problem:** In `dwa.run`, the minimum clearance is measured only at the end of each 0.25 s period. When each executed arc is sampled every 0.005 s (`exp2.py`), the closest approach is **0.0499 m** in the wall run and 0.0508 m in the U trap. The argument gets stronger, since the margin sets the clearance exactly, but the quoted number is not the closest approach. The output line is real program output and can stay.
- **Correction:** "The closest approach, about 0.050 m along the path (0.054 m at the control instants, where the program measures it), is set by the 0.05 m safety margin: ..."

### T5. Two conventions for $s_{\mathrm{hit}}$ (optional)
- **Where:** `:392` ("$s_{\mathrm{hit}} = 1.26$ m"), `:394` ("$s_{\mathrm{hit}} = 1.5 - 0.9 - 0.25 = 0.35$ m"), Exercise 5
- **Problem:** `first_contact` samples the curve every 0.02 m. It returns 1.26 m (the analytic value is 1.25 m) and **0.36 m** (analytic 0.35 m). The first value is the program's; the second is analytic. With 0.36 m the speed bound is 0.488 m/s instead of 0.480 m/s. Both lie between 0.475 and 0.500, so no conclusion changes.
- **Correction:** After "0.35 m" add "(0.36 m on the program's 0.02 m sampling, which moves the bound below to 0.488 m/s and changes nothing on the 0.025 m/s grid)". Alternatively, write "1.25 m analytically, 1.26 m as sampled" at `:392`.

### T6. What Brockett's result implies (optional)
- **Where:** `:258`
- **Text:** "The law needs $v_r > 0$, so stopping at a pose needs a different controller in the last few centimeters, as Brockett's result in Section 2.2 implies."
- **Problem:** The need for another controller follows from $v_r > 0$. Brockett's theorem adds that the other controller cannot be a smooth function of the state alone.
- **Correction:** "The law needs $v_r > 0$, so stopping at a pose needs a different controller in the last few centimeters, and by Brockett's result (Section 2.2) that controller cannot be a smooth function of the state alone."

### Log of checks and recomputations

1. **Programs re-run.** `sh run.sh` (the writer's), output saved to `out.txt`. A diff against the writer's `outputs.txt` shows no difference. Every line of all nine `text` output blocks in the article occurs verbatim in the output (script check), including the Kanayama $K_y = 16$ block that the article omits. All programs are deterministic: no random numbers are drawn.
2. **Listings against programs.** The four `python` blocks (`pure_pursuit`, `kanayama`, `descend`, `evaluate`) are verbatim substrings of `pure_pursuit.py`, `kanayama.py`, `potential_field.py` and `dwa.py`. The simulation setup described in Section 2.4 matches `common.py`: Euler step 0.01 s, control every fifth step, lag 0.1 s on $v$ and $\omega$, $|\omega| \le 1.5$ rad/s, $r = 0.05$ m, $b = 0.30$ m, and the path geometry.
3. **Wheel relations and the pure pursuit example.** $v = 0.5$, $\omega = 0.5$ gives 11.50 and 8.50 rad/s, and $v/\omega = 1$ m. Goal point (0.5, 0.3): $L_d = 0.5831$ m, $\alpha = 0.5404$ rad, $\kappa = 1.7647$ m$^{-1}$, $R = 0.567$ m, $\omega = 0.8824$ rad/s. The arc derivation (circle tangent at the origin, center $(0,R)$) is correct. The diamond of reachable $(v,\omega)$ under wheel-speed limits is correct.
4. **Derivations.** The pure pursuit linearization $y_g \approx -e - L_d\theta$ gives $\ddot e + (2v/L_d)\dot e + (2v^2/L_d^2)e = 0$, so $\zeta = 1/\sqrt2$ and $\omega_n = \sqrt2 v/L_d$ (correct). The overshoot of the initial-condition response equals the step overshoot $e^{-\pi} = 4.32\%$, which gives 0.0216 m. $L_d = kv$ gives $\omega_n = \sqrt2/k$ (correct). The robot-frame error, the error dynamics and the Kanayama law are dimensionally consistent ($K_x$ in 1/s, $v_r K_y e_y$ and $v_r K_\theta$ in 1/s). Lyapunov check: with $V = \tfrac12(e_x^2+e_y^2) + (1-\cos e_\theta)/K_y$, substituting the law gives $\dot V = -K_x e_x^2 - v_r K_\theta\sin^2 e_\theta/K_y$. Linearization: $\ddot e_y + v_rK_\theta\dot e_y + v_r^2K_y e_y = 0$, $\zeta = K_\theta/(2\sqrt{K_y})$, giving 1, 0.5 and 0.25 for $K_y$ = 4, 16 and 64, and a double pole at $-1$ s$^{-1}$ (all correct). The repulsive gradient $-k_r(1/\rho-1/\rho_0)\nabla\rho/\rho^2$ is correct. The attractive potential is continuous at $d^*$. The nonholonomic constraint and Brockett's condition for the unicycle were checked.
5. **Numbers recomputed** (`recompute.py`). Bend times 12.0 s and 15.14 s. Exercise 1: 4.2 and 7.8 rad/s, radius 0.5 m. Exercise 2: 1.0198 m, −0.3846 m$^{-1}$, 2.6 m, −0.3077 rad/s. Exercise 3: 4 and 4. Exercise 4: real root of $2\rho^3+\rho-1$ is 0.5898, stop at 5.410 m. The minimum claim was also checked: on the axis the end wall's repulsion has no $y$ component and the attraction restores $y$. Exercise 5: 0.4797 and 0.5916 m/s. DWA: window [0.275, 0.525] × [−0.5, 0.5] and 121 candidates; stopping distance 0.4069 m; $G$ = 0.8135; curvatures 0.421 and 0.381 m$^{-1}$; $0.453 \times 3 = 1.36$ m. Scene C equilibrium at (4.37, 0): $\rho = 0.618$ m, total repulsion along $x$ 1.998 against an attraction of 2 (balanced). All match the text.
6. **Statements drawn from the simulations** (`exp2.py`). Kanayama: the speed command reaches the 1.0 m/s limit during the first 0.2 s. For $K_y = 64$ the turn-rate limit is active from 0 to 0.85 s, which confirms "the turn rate limit dominates the first second". For $K_y = 4$, $e_y e^{t}$ at 2, 3 and 4 s is 1.00, 1.39 and 1.80, nearly linear in $t$ as a double pole at −1 predicts. Potential field: with $\rho_0 \le 0.6$ m scene C reaches the goal while scene B stays trapped for every $\rho_0$ tried (0.3 to 0.8 m), which confirms ":342". DWA U trap: the robot stands still ($v = 0$) for 137 of the 160 periods, and no period lacks an admissible command, which confirms "brakes in front of the closed end".
7. **Sensitivity tests** (`experiments.py`, `d5_zoh.py`): see T1 and T2. The text's claims about trends are not based on a single lucky run: every program is deterministic, and the claims are about trends in parameter sweeps that the programs print.
8. **Consistency with the series.** $\mathcal{C} = \mathbb{R}^2 \times S^1$ and angle wrapping to $(-\pi, \pi]$ agree with the first entry (Section 2.2). $q(t) = \sigma(s(t))$ agrees with the fourth entry (Section 1.1). D* Lite's backward search agrees with the second entry (Section 5.4). "Nonholonomic" is consistent with What Is a Robot? (Section 2.2). The units are SI and angles are in radians, as the series overview states.
9. **Lint.** `npm run eos -- lint` reports 0 errors, 0 warnings and 5 suggestions, the same as the copy stage. No site build was run at this stage; the link fragments were checked against the target headings (Fact-check table).

**Verdict (technical): fail** until T1 to T4 are applied. Counts: 0 blocking, 4 should fix, 2 optional. Every quoted output reproduces exactly, every listing matches its program, and every equation and worked number checks out. The findings concern three causal or universal statements and one mislabeled measurement.

## Resolution

Stage: EOS step 7, by the author. Every quoted number below comes from a program in `/tmp/claude-0/mp/path-tracking-and-reactive-avoidance/`, re-run with Python 3.13.16 and NumPy 2.5.3. `run.sh` now also runs `zoh.py`, and its output matches `outputs.txt`. Every line of every `text` block in the article occurs verbatim in that output (script check). The existing outputs are unchanged by the program edits: the defaults of `common.step` are unchanged, and the new lines are only appended or inserted. Final `npm run eos -- lint`: 0 errors, 0 warnings, 6 suggestions (one 46-word sentence at `:93`; the five reference-list acronyms kept under C7). A scratch build passed, and the link checker reports that all internal links resolve, including `#54-incremental-replanning-d-lite`.

| ID | Action | Exact change |
|---|---|---|
| F1 | Applied | Section 3.1: "The method was developed at Carnegie Mellon University for outdoor vehicles; Coulter's 1992 report documents its implementation, derives the curvature formula and discusses the effect of the look-ahead distance." → "Coulter's 1992 technical report from Carnegie Mellon University documents an implementation of the method, derives the curvature formula and examines how its performance depends on the look-ahead distance." |
| F2 (settles D6) | Applied | Section 6.3: "runs **recovery behaviors** in order of increasing cost, typically:" → "runs **recovery behaviors**, roughly in order of increasing cost, for example:"; "...fail rarely and visibly." → "...fail visibly, and often recover from the failure." |
| F3 | Not applied | The page range 195–210 is still confirmed by one secondary source only, so the Gat reference is unchanged. |
| F4 | Applied | Section 5.2: "for worlds of spherical obstacles and worlds that can be mapped onto them." → "for worlds of spherical obstacles, and, through a change of coordinates, for worlds that can be mapped onto them." |
| T1 (settles D5) | Applied with changes | Section 2.4: the sentence "Without the lag and the limit, ... would never oscillate." becomes "Without the lag, the limit and the 20 Hz sampling, a tracking controller's gains could be raised without bound and the loop would stay stable; with them, aggressive gains overshoot, oscillate or go unstable. The sampling alone is enough. Take the linearized pure pursuit loop of Section 3.3 on a straight line, with each command held for 0.05 s and no lag or limit: the largest closed-loop pole has magnitude 0.833 at $L_d = 0.15$ m but 2.032 at $L_d = 0.02$ m, an unstable loop (program `zoh.py`)." The numbers come from the new program `zoh.py` (exact zero-order-hold discretization), which reproduces the reviewer's values. |
| T2 | Applied with changes | Section 3.3: the cause is restated with the limit first. "At $L_d = 0.15$ m the 0.5 m initial error, more than three times $L_d$, drives $\omega$ to its 1.5 rad/s limit. The drive lag adds phase lag on top, since $\omega_n = 4.7$ rad/s is no longer small against the drive's bandwidth of $1/0.1 = 10$ rad/s and the 20 Hz update. The program `pure_pursuit.py` also reruns this case with each effect switched off. The overshoot is 0.018 m with neither, 0.029 m with the lag alone, 0.166 m with the limit alone and 0.258 m with both. The look-ahead distance therefore has a lower limit set by the robot's drive, here mostly by its turn-rate limit." `pure_pursuit.py` gained `tau` and `w_max` arguments and prints this sweep after its table (real output: 0.018, 0.029, 0.166, 0.258 m). In the Summary table, "Short $L_d$ overshoots against drive lag" → "Short $L_d$ overshoots against the turn-rate limit and drive lag". |
| T3 (settles D8) | Applied | Section 5.1: "every method of this kind can be led into a situation it cannot escape on its own." → "both methods of this section can be led into situations they cannot escape on their own (Sections 5.2 and 5.3)." |
| T4 | Applied with changes | `dwa_demo.py` now also samples each executed arc every 0.005 s and prints "wall: closest approach along the path 0.0499 m" and "U trap: closest approach along the path 0.0508 m". These lines are quoted in a new block after the closed-loop output, with the lead-in "The program measures this clearance at the control instants only. Sampling each executed arc every 0.005 s, it then prints the closest approach along the whole path:". "The closest approach, 0.054 m, is set by the 0.05 m safety margin:" → "The closest approach, 0.050 m along the path (0.054 m at the control instants), is set by the 0.05 m safety margin." (the sentence that follows starts afresh). "0.051 m from it" → "about 0.05 m from it". |
| T5 | Applied | `dwa_demo.py` prints the sampled values: "s_hit of the straight arc as sampled: 0.36 m (at the origin: 1.26 m)". This line is added to the quoted block of the second decision. Text: "$s_{\mathrm{hit}} = 1.26$ m" → "$s_{\mathrm{hit}} = 1.26$ m as sampled (1.25 m analytically)". After the analytic 0.35 m and 0.480 m/s, added: "The program's 0.02 m sampling gives 0.36 m, which moves the bound to 0.488 m/s and changes nothing on the 0.025 m/s grid." Exercise 5 keeps the analytic 0.35 m. |
| T6 | Applied | Section 4.5: "..., as Brockett's result in Section 2.2 implies." → "..., and by Brockett's result (Section 2.2) that controller cannot be a smooth function of the state alone." |
| D7 | Applied | Section 6.2: the link now reads "[Section 5.4 of the second entry](/blog/graph-search-dijkstra-and-a-star#54-incremental-replanning-d-lite)"; the fragment was checked in the built page. |
| D9 | Applied | Section 3.3, after "an error under 1 cm in the bend.": "The RMS column, which covers the bend and the final straight, follows the corner errors: it grows from 0.0035 m at $L_d = 0.3$ m to 0.0719 m at 1.2 m." (values from the quoted table). |
| D1–D4, C1–C7 | Already applied by the editors | No author action needed; the re-read confirmed that their wording is consistent with the changes above. |

No open blocking or should-fix finding remains.

## Series review changes

From the series review `reviews/motion-planning.md` (2026-10-17), applied by the author side:

- F4: the Khatib (1986) reference now names the journal *International Journal of Robotics Research*, as in the first entry and every other reference to that journal in the series.
- F14: the answer to Exercise 3 writes the characteristic polynomial in $\lambda$ instead of $s$ (the series' path parameter, and the unit symbol beside it).
- F3 needed no change here: the second entry now cites the same 2002 paper.
- No number, code or output changed.

## QA

Stage: EOS step 10, by an independent QA editor who did not write or revise the entry. Recorded with `eos record`: **decision revise, total 24/28** (`editorial/records/article/path-tracking-and-reactive-avoidance.json`).

| Dimension | Score | Reason when below 4 |
|---|---|---|
| purpose | 4 | |
| structure | 4 | |
| accuracy | 4 | |
| evidence | 3 | Gat (1998) has no page range (F3), and several bibliographic details were confirmed from search results, not fetched sources. |
| language | 4 | |
| consistency | 3 | Units with exponents differ from entry 4 and the rest of the site (Q1); the link text names the insight by an outdated title (Q2). |
| publishing | 2 | `eos validate-site dist` exits 1 with 22 `glued-inline` issues on this page, so the publication gate and deploy fail (Q1). |

Critical conditions: C8 (Q1 is open and blocking). C9: the series review is resolved but not yet stamped (`series-pipeline status`: review-stale). That is expected until every record is written.

Confirmed resolved in the text: D1–D9, C1–C7, F1, F2, F4, T1–T6, series F3, F4 and F14. F3 (Gat pages) is deliberately unchanged.

Independent checks:
- `sh run.sh` output is identical to `outputs.txt`, and every line of the ten `text` blocks occurs verbatim in it.
- Recomputed independently: the ZOH pole magnitudes (0.833, 0.375, 0.250, 2.032), the pure pursuit example (0.5831 m, 0.5404 rad, 1.7647 m⁻¹, 0.567 m, 0.8824 rad/s), $e^{-\pi} = 4.32\%$ (0.0216 m), Exercise 4 ($\rho = 0.5898$ m), Exercise 5 (0.4797, 0.5916 m/s, and 0.4879 m/s with 0.36 m) and the DWA stopping distance (0.4069 m) and curvatures (0.421, 0.381 m⁻¹).
- Checked against the fact-check table: Kanayama et al., Fox et al., Rimon and Koditschek, Khatib, and Koenig and Likhachev. The list is in alphabetical order.
- Every fragment resolves (`check:links`: all internal links resolve). Each target says what the text claims (What Is a Robot? §2.2, §4, §5, §5.3; entry 2 §2.1 and §5.4; entry 4 §1; Sensing and State Estimation §7.2), except the insight title (Q2).
- `eos lint`: 0 errors, 0 warnings, 6 suggestions. These are kept with reasons: C7, and one 46-word sentence at `:93`.

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| Q1 | Blocking | `:95`, `:115`, `:200`, `:208`, `:226`, `:254`, `:354`, `:392`, `:502`, `:506`, `:511`, `:524` | publishing | 22 units written as text plus a KaTeX exponent fail `eos validate-site`, and so CI. |
| Q2 | Should fix | `:484`, Section 6.4 | consistency | The link text "Closing the Sim-to-Real Gap" is not the insight's title. |

### Q1. Unit exponents in KaTeX fail validate-site
- **Where:** 22 occurrences. Lines 95, 115, 392 and 502: `m$^{-1}$`. Line 200: `1/m$^2$`. Line 208: `m$^{-1}$`, `m$^{-2}$` (×2) and `s$^{-1}$`. Line 226: `s$^{-1}$`, `m$^{-1}$` and `m$^{-2}$`. Line 254: `m$^{-2}$` (×2) and `s$^{-1}$`. Line 354: `m/s$^2$` and `rad/s$^2$`. Line 506: `s$^{-1}$`. Line 511: `s$^{-1}$`, `m$^{-1}$` and `m$^{-2}$`. Line 524: `m/s$^2$`.
- **Problem:** Each one renders as a letter glued to `<span class="katex">`. These are exactly the 22 `glued-inline` issues that make `eos validate-site dist` exit 1. That command is a blocking step in `publication-gate.yml` and `deploy.yml`, and the acceptance checklist requires validate-site to be clean for the page. This is the only page on the site that writes units this way. Entry 4 and the other articles use Unicode superscripts (rad/s², m/s², s⁻¹).
- **Correction:** Replace in prose only (not inside `$...$` formulas) as follows:
  - `m$^{-1}$` → `m⁻¹`
  - `m$^{-2}$` → `m⁻²`
  - `s$^{-1}$` → `s⁻¹`
  - `m/s$^2$` → `m/s²`
  - `rad/s$^2$` → `rad/s²`
  - `1/m$^2$` → `1/m²`

  Then rebuild and confirm that `eos validate-site dist` reports no issue for this page.

### Q2. Outdated title of the linked insight
- **Where:** `:484`, Section 6.4, "Tuning and verification".
- **Text:** "the insight [Closing the Sim-to-Real Gap](/insights/closing-the-sim-to-real-gap) discusses the gap between simulated and real behavior."
- **Problem:** The insight's title is "Is the Sim-to-Real Gap Something to Close or to Measure?" (`src/content/insights/closing-the-sim-to-real-gap.md:2`). Its argument is that the gap may be better measured than closed, so the old name misstates it.
- **Correction:** "the insight [Is the Sim-to-Real Gap Something to Close or to Measure?](/insights/closing-the-sim-to-real-gap) discusses the gap between simulated and real behavior."

Not verified: the items under the fact-check's "Not verified", unchanged. Outside this item: `validate-site` also reports 4 `meta-description` issues on Vietnamese pages (`vi/blog/data-parallelism-vector-units-and-gpus.html`, `memory-hierarchy-and-locality.html`, `performance-models-and-scaling-laws.html`, `threads-and-shared-memory-parallelism.html`). These also make the command exit 1.

After Q1 and Q2 are applied, QA must be re-run and recorded again, because the edit changes the content hash.

**QA follow-up (re-record):**
- The author applied Q1 and Q2 exactly. The diff touches only the 12 lines with units and line 484.
- After a rebuild with `npm run build:local`, `eos validate-site dist` reports "No issues" and exits 0 (the four Vietnamese descriptions were also shortened), and `check:links` reports that every internal link resolves.
- Re-recorded: **decision publish, total 27/28**. Scores: purpose 4, structure 4, accuracy 4, evidence 3 (Gat pages; search-result confirmations), language 4, consistency 4, publishing 4.
- No critical condition holds. Open findings: 0.
