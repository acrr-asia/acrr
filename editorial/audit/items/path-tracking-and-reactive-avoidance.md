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
