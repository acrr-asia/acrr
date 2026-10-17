# Editorial review: From Paths to Trajectories: Time Scaling and Velocity Profiles

- Path: `src/content/blog/trajectories-and-time-scaling.mdx` · Route: `/blog/trajectories-and-time-scaling` · Type: article, series entry 4 of 5 (`motion-planning`)
- Reviewed against: `editorial/standards.md` 1.0, `editorial/glossary.json`, `plugins/editorial-os/references/review-protocol.md`, the series overview `src/content/series/motion-planning.md`, the first entry (Sections 3.2, 4 and 5, which this entry cites or overlaps), the second and fifth entries (the passages that link to this entry), `what-is-a-robot` Section 4 and `planar-arm-kinematics` Section 5. The third entry was still being drafted; its headings were taken from the writer brief.
- Stages in this report: developmental (EOS step 6.1) and copy (6.2), both by an editor who did not write the entry. Line numbers refer to the revised file.
- Programs: the writer's `run.sh` was rerun (Python 3.13, NumPy 2.5); its output is identical to the saved `output.txt`, so every quoted program output matches a real run.

## Developmental review

The entry does its job for the stated reader. The opening links the entries and the arm article it builds on, says what it covers and states its conventions, versions and limit values (marked as illustrative, not data of a real arm). Each section opens with its concept before the equations: the chain rule before the scalings, the cubic and quintic derived from their boundary conditions, the trapezoid and S-curve from the phases of the motion, the phase plane before the forward-backward pass, splines before the tridiagonal system, and what to check before how. The argument runs from the straight joint-space line (where the limits on $\dot s$ and $\ddot s$ are constant) to a curved path (where they are coupled), then to waypoints and finally to checking, and the running example connects Sections 2, 3 and 5. Limits are stated in every section (4.3 and 6.3 in particular), the six exercises each test a derived result, and the Summary leads to the fifth entry. The eight `##` headings and all 18 `###` headings are unchanged, so the fragments linked from other entries (`#1-paths-and-trajectories` from the fifth entry, `#6-checking-a-trajectory` from the first) still resolve.

Length: the series standard is 3,500 to 6,000 words of prose. Measured with the `eos` prose counter (code, math and front matter masked), the draft had 5,152 words and the revision has 5,104; counting without tables and references, 4,949 (4,389 before the exercises, 473 in the exercises). The writer's figure of about 6,500 included inline math and table text. The entry is therefore within the limit; the cuts below remove repetition rather than content.

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| D1 | Should fix | `:393`, Section 6.2 | structure | The motion bound and the clearance were rederived, although the first entry derives both. |
| D2 | Should fix | `:250`, Section 4.2 | publishing | Visitor copy pointed to "the scratch programs", which readers cannot see. |
| D3 | Should fix | `:190`, `:514`, Section 3.3 and closing | structure | The point that polynomials are slow because they touch their limits only at instants, and a list of every method, were repeated from Section 2.3 and the Summary table. |
| D4 | Should fix | `:138`, Section 3.1; `:281` | consistency | "bang-coast-bang" and "bang-bang" were used without being defined. |
| D5 | Optional | `:14`, opening | purpose | "The planners of the first three entries" misdescribes the first entry, which states the problem and presents no planner. |
| D6 | Optional | `:16`, opening | purpose | The coverage sentence was a list of section topics (a table of contents in prose). |
| D7 | Optional | `:283`, Section 4.3 | consistency | "as Section 6 does for splines" pointed at a whole section; the stretch is in 6.3. |
| D8 | Should fix (for fact-checker) | `:522`, References | evidence | The Pham (2014) reference has no volume, issue or pages. |
| D9 | Should fix (for fact-checker) | `:26`, `:190`, `:311` | evidence | Three statements about what the textbooks contain need checking against them. |
| D10 | Should fix (for technical reviewer) | `:210`, Section 4.1 | accuracy | The description of where the time-optimal scaling switches between maximum acceleration and deceleration is imprecise. |
| D11 | Optional (for fact-checker) | `:210`, Section 4.1 | evidence | The algorithm attributed to both 1985 papers ("integrate forward ... and backward") should be checked against each paper. |

### D1. Section 6.2 repeats the first entry
- **Where:** `src/content/blog/trajectories-and-time-scaling.mdx:393`, Section 6.2 "Sampling, and what it proves"
- **Text (before):** "It also computes the **clearance**, the distance between the arm and a disk obstacle ... A point on the second link at distance $\rho \le l_2$ from the elbow moves at most $l_1|\Delta\theta_1| + \rho\,|\Delta\theta_1 + \Delta\theta_2|$, which is at most $(l_1 + l_2)|\Delta\theta_1| + l_2|\Delta\theta_2|$, and within an interval $\Delta t$ each joint changes by at most its peak speed times $\Delta t$:"
- **Problem:** The first entry defines **clearance** in bold (`configuration-space-and-the-planning-problem.mdx:187`, Section 3.2) and derives the same bound, with the point on the second link written $u$ rather than $\rho$ (Section 5.3, `:365-372`). Standards 6.1: "across a series, a later entry refers back instead of repeating"; 5.3: a later entry may refer back for a term. The repetition also introduced a second symbol for the same quantity.
- **Correction (applied):** "The obstacle is a disk of radius 0.15 m centered at $(0.95, 1.0)$ m. The checker computes the arm's clearance to it as in [Section 3.2 of the first entry](...#32-the-two-link-arm-and-one-obstacle), with both links treated as line segments. To make the clearance at the samples say something about the whole motion, it bounds how far any point of the arm can move within one sample interval. [Section 5.3 of the first entry](...#53-a-check-that-cannot-miss) showed that no point of the arm moves faster than $(l_1 + l_2)|\dot\theta_1| + l_2|\dot\theta_2|$. Within an interval $\Delta t$, each joint changes by at most its peak speed times $\Delta t$:" The bound is the same one the code computes (`step = ((L1 + L2)*vmax[0] + L2*vmax[1])*dt`). Both fragments were confirmed in the built page. Section 6.1 (`:389`) now also says that the first entry's edge checks "rest on the same idea and share its weakness".

### D2. Authoring reference in visitor copy
- **Where:** `:250`, Section 4.2
- **Text (before):** "The listing omits three helpers, which are in the scratch programs: `x_limit`, ..."
- **Problem:** The scratch folder is an authoring artifact; readers cannot reach it. `CLAUDE.md` (Content-integrity rules) keeps authoring details out of visitor-facing copy.
- **Correction (applied):** "The listing omits three helpers: `x_limit`, ..." The sentence still says what each omitted helper does, so the listing remains honest about what it leaves out.

### D3. Repetition of the polynomial argument and of the method list
- **Where:** `:190` (Section 3.3) and `:514` (closing paragraph)
- **Text (before):** "The polynomials are the slowest because they touch their limits only at isolated instants." and "Polynomial scalings give smooth motion at the cost of time; trapezoidal and S-curve profiles spend as much of the move as possible at a limit; time-optimal scaling extends that idea to curved paths; and splines carry a robot through waypoints without stopping. Each of them yields a trajectory that is only as trustworthy as the check that follows it."
- **Problem:** Section 2.3 (`:120`) already makes the first point ("the joint reaches its speed limit only at one instant ... for the rest of the motion it moves below both"), and the closing list restates the Summary table row by row (standards 2.3 and 6.1 on restating the same point in the body, a summary and the conclusion).
- **Correction (applied):** The sentence in 3.3 is cut. The closing paragraph now reads: "A trajectory is a path with a schedule, and the schedule is bounded by what the motors and the structure can deliver. The faster a profile, the more of the motion it spends at a limit, and every profile is only as trustworthy as the check that follows it. The [next entry] ..."

### D4. Undefined terms bang-coast-bang and bang-bang
- **Where:** `:138`, Section 3.1; used again at `:281` and in the Summary table
- **Text (before):** "this bang-coast-bang profile is the minimum-time rest-to-rest motion."
- **Problem:** Standards 5.3: define a technical term at first use, in bold. The terms were used before the sentence that describes the behavior they name.
- **Correction (applied):** The sentence now reads "this profile is the minimum-time rest-to-rest motion", and after the description of its phases: "A profile of this kind (full acceleration, constant speed, full deceleration) is called **bang-coast-bang**; without the constant-speed phase it is **bang-bang**."

### D5. The first entry has no planner
- **Where:** `:14`, opening
- **Text (before):** "The planners of the first three entries answer a geometric question"
- **Problem:** The first entry states the problem and maps the methods (`configuration-space-and-the-planning-problem.mdx`, Sections 1-6); the planners are in the second and third entries.
- **Correction (applied):** "The first three entries answer a geometric question".

### D6. Opening lists sections
- **Where:** `:16`
- **Text (before):** "It covers the chain rule that links a path to a trajectory, polynomial time scalings, trapezoidal and jerk-limited profiles, time-optimal scaling along a fixed path, splines through waypoints and the checks a trajectory must pass before it is sent to a robot."
- **Correction (applied):** "It shows how the schedule along a path sets the joint velocities and accelerations, and derives the standard velocity profiles and the fastest schedule along a fixed path. It then carries a trajectory through waypoints with splines and ends with the checks a trajectory must pass before it is sent to a robot."

### D7. Section reference too broad
- **Where:** `:283`
- **Correction (applied):** "as Section 6 does for splines" became "as Section 6.3 does for splines".

### D8. Incomplete Pham reference (for the fact-checker)
- **Where:** `:522`
- **Text:** "Q.-C. Pham, "A general, fast, and robust implementation of the time-optimal path parameterization algorithm," *IEEE Transactions on Robotics*, 2014."
- **Problem:** Standards 7.3: volume, issue and pages are given when they exist. They are omitted here. Not added by this stage (no verified source in hand).
- **Correction:** Fact-checker to verify and add volume, issue and pages from IEEE Xplore or DBLP, or confirm the omission.

### D9. Claims about the textbooks (for the fact-checker)
- **Where and text:** `:26` "The textbooks of Lynch and Park and of Siciliano et al. develop the decoupled approach first"; `:190` "Lynch and Park derive the polynomial and trapezoidal scalings and describe the S-curve in the same terms"; `:311` "De Boor's book treats these spline systems and their end conditions in detail, and Siciliano et al. apply cubic splines through joint-space points in the same way."
- **Problem:** Each claim attributes content to a book; standards 7.2 require that a source supports the claim it is cited for. Wording was changed at `:26` (word order only, same claim).
- **Correction:** Fact-checker to confirm against the books' chapters on trajectory generation (Lynch and Park, Chapter 9; Siciliano et al., Chapter 4) and de Boor; qualify or remove what is not supported.

### D10. Switching structure of the time-optimal scaling (for the technical reviewer)
- **Where:** `:210`, Section 4.1
- **Text:** "At every point it uses either the largest acceleration $U$ or the smallest $L$, and it switches between them at points that touch the velocity limit curve. Their algorithms integrate forward from the start with maximum acceleration and backward from the goal with maximum deceleration, and find the switching points between these curves."
- **Problem:** In the phase-plane method, a switch from deceleration to acceleration occurs at a point where the profile touches the velocity limit curve, but a switch from acceleration to deceleration occurs where a forward maximum-acceleration curve meets a backward maximum-deceleration curve, which need not touch the velocity limit curve. The first sentence reads as if all switches are at the curve; the second sentence partly corrects it. The program's own output (`:271-274`) shows a switch from acceleration to the lower bound at $s = 0.235$, before the profile reaches the speed limit curve at $s = 0.566$, which is consistent with the second reading.
- **Correction:** Technical reviewer to confirm, then for example: "... it uses either the largest acceleration $U$ or the smallest $L$. It switches from deceleration to acceleration only at points where it touches the velocity limit curve, and from acceleration to deceleration where a forward curve of maximum acceleration meets a backward curve of maximum deceleration."

### D11. Attribution of the algorithm (for the fact-checker)
- **Where:** `:210`
- **Text:** "Their algorithms integrate forward from the start with maximum acceleration and backward from the goal with maximum deceleration"
- **Problem:** The sentence attributes the forward-backward integration to both Bobrow et al. and Shin and McKay. Shin and McKay's 1985 paper is often described in terms of a phase-plane construction with its own switching-point search; whether both papers integrate in this way should be checked.
- **Correction:** Fact-checker to confirm, or narrow the attribution ("Bobrow et al. integrate forward ...").

Verdict (developmental): **pass**. Every blocking or should-fix finding of this stage within the editor's remit (D1-D4) was applied; D8-D11 are handed to the fact-check and technical stages, which own them.

## Copy edit

`eos fix --rules spelling-variant,terminology` applied 0 fixes (the draft was already in American spelling and house terms). `eos lint` on the draft reported 2 errors and no warnings or suggestions; the two errors are the link to the third entry, which does not exist yet (expected, not this stage's). The developmental revisions introduced three sentence-length suggestions, all removed by splitting. Final `eos lint`, run after the third entry's file appeared: 0 errors, 0 warnings, 0 suggestions. Grep for em dashes, contractions, "simply", "obviously", "clearly", "of course" and "we": none in prose. MDX compiles (`eos syntax`); a site build (`/tmp/claude-0/mp/edit-build-4`, deleted afterwards) plus `check-links` reported only the missing third-entry page for this article, and no letter glued to an inline element.

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| C1 | Should fix | `:24` | consistency | "**time-scaling**" was bolded a second time after the definition in Conventions. |
| C2 | Optional | `:79` | language | "The derivatives factor neatly." was filler. |
| C3 | Optional | `:37` | language | "This term is why a robot must slow down ... it is the source of most of the difficulty" was wordy. |
| C4 | Optional | `:382` | language | "As Section 4 ... put it" implied a quotation of a paraphrase. |
| C5 | Optional | `:433` | language | "the speed of joint 2 7.25% above its limit" put two numerals side by side. |
| C6 | Optional | `:18`, `:283`, `:347` | language | Small rewordings for concision and precision. |
| C7 | Should fix (for technical reviewer) | `:181`, Section 3.3 | accuracy | "the five profiles" introduces a table of four rows. |
| C8 | Should fix (for technical reviewer) | `:283`, Section 4.3 | evidence | "the small violation does not vanish on its own" is not shown by the output and appears to be contradicted by a rerun. |
| C9 | Optional (for technical reviewer) | `:39`, Section 1.2 | accuracy | "Jerk limits come from the structure rather than the motor" is stated as absolute. |
| C10 | Optional (for technical reviewer) | `:250`, Section 4.2 | accuracy | "setting the gripper's acceleration along the path to zero" is ambiguous. |

### C1. Term bolded twice
- **Where:** `:24`, Section 1.1
- **Text (before):** "and a **time-scaling** step chooses how fast to move along it."
- **Problem:** **time scaling** is defined in bold in the Conventions paragraph (`:18`); standards 5.6 reserve bold for the point of definition.
- **Correction (applied):** "and a time-scaling step chooses how fast to move along it."

### C2. Filler
- **Where:** `:79`
- **Correction (applied):** Deleted "The derivatives factor neatly."; the paragraph now opens "The path speed is ...".

### C3. Wordy causal sentence
- **Where:** `:37`
- **Correction (applied):** "This term forces a robot to slow down on tight curves, and it causes most of the difficulty in Section 4."

### C4. Paraphrase presented as a quotation
- **Where:** `:382`
- **Text (before):** "As [Section 4 of the first Introduction to Robotics entry](...) put it, the planner assumes ..., and that assumption holds only for ..."
- **Problem:** The cited section says "the planner assumes that the trajectory it sends is the trajectory the joints follow. These assumptions hold only when the rates are well separated"; the second half here is a paraphrase.
- **Correction (applied):** "As [Section 4 ...](...) notes, the planner assumes that the trajectory it sends is the trajectory the joints follow, an assumption that holds only for trajectories the joint controllers can follow."

### C5. Adjacent numerals
- **Where:** `:433`
- **Correction (applied):** "The check found joint 2's speed 7.25% above its limit and ..."

### C6. Concision and precision
- `:18`: "so every quoted number is reproduced exactly by rerunning the programs" became "so rerunning the programs reproduces every quoted number exactly" (active voice).
- `:26`: "The decoupled approach is the one that the textbooks ... develop first, and the one this series follows" became "The textbooks of Lynch and Park and of Siciliano et al. develop the decoupled approach first, and this series follows it" (same claim; see D9).
- `:283`: "The check in the output matters as much as the result" (an abstract claim of importance) became "The acceleration check in the output qualifies this result"; "this simple pass" became "this forward-backward pass".
- `:347`: "computes position, velocity and acceleration" became "computes the position, velocity and acceleration".

### C7. Count of profiles (for the technical reviewer)
- **Where:** `:181`
- **Text:** "The table compares the five profiles of Sections 2 and 3 for the same move of the running example."
- **Problem:** The table has four rows (cubic, quintic, trapezoidal, S-curve). The triangular profile of Section 3.1 does not apply to this move ($D = 1.5$ rad $\ge v^2/a = 0.5$ rad), so it is not a missing row. Left unchanged because the brief forbids this stage to change numbers.
- **Correction:** "The table compares the four profiles of Sections 2 and 3 ..." (or "the profiles", without a count).

### C8. Claim about the acceleration violation (for the technical reviewer)
- **Where:** `:283`
- **Text:** "The duration converges as the grid is refined (1.8207 s with 250 intervals, 1.8178 s with 4000), but the small violation does not vanish on its own."
- **Problem:** The program prints the peak joint acceleration only for $N = 2000$ (2.0023 rad/s²), so the claim about refinement is not supported by the quoted output. A copy of `timeopt.py` modified only to print the peak acceleration for each grid in the convergence loop (scratch copy, not in the article) gave joint 2 peaks of 2.0155, 2.0094, 2.0047 and 2.0012 rad/s² for $N$ = 250, 500, 1000 and 4000: the violation shrinks roughly in proportion to $1/N$, although it stays above the limit at every finite $N$ tried.
- **Correction:** Technical reviewer to confirm, then for example: "... but the violation only shrinks with the grid (to 2.0012 rad/s² with 4000 intervals) and remains at every finite resolution." Any new number must come from the writer's program, extended to print it, with `run.sh` and the quoted output updated together.

### C9. Source of jerk limits (for the technical reviewer)
- **Where:** `:39`
- **Text:** "Jerk limits come from the structure rather than the motor: a sudden change of acceleration excites vibration in the links, gearboxes and payload."
- **Problem:** Stated as absolute; jerk limits are also set for drive and current-loop bandwidth and for the comfort of passengers or the safety of payloads. A qualifier ("mainly") would keep the statement true.
- **Correction:** Technical reviewer to decide; for example "Jerk limits come mainly from the structure rather than the motor: ...".

### C10. Ambiguous second derivative of the line path (for the technical reviewer)
- **Where:** `:250`
- **Text:** "$\sigma''$ follows from differentiating the forward kinematics twice and setting the gripper's acceleration along the path to zero."
- **Problem:** What is set to zero is the second derivative of the gripper position with respect to $s$ (the straight line is linear in $s$), not a time acceleration; "acceleration along the path" can be read as the tangential acceleration in time.
- **Correction:** For example "... and setting $d^2 p/ds^2$, the second derivative of the gripper position with respect to $s$, to zero."

### Lint suggestions kept

None. The three `sentence-length` suggestions introduced during the developmental revision (`:16` and two at `:393`) were removed by splitting the sentences.

Verdict (copy): **pass**. C1-C6 are applied; C7-C10 concern technical content that this stage may not change and are handed to the technical reviewer.

<!-- Later stages (fact-check, technical review, resolution, QA) add their sections below. -->
