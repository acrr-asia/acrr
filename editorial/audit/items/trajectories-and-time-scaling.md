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

## Fact-check

Stage: EOS step 6.3, by a reviewer who did not write or revise the entry. Network access was limited: DBLP, Crossref, arXiv, IEEE Xplore and the University of Michigan PDF host were refused by the egress proxy, so bibliographic details were confirmed through web-search listings of publisher, library and citing-paper records. Each status below names what was seen. Line numbers refer to the current file. This stage settles D8, D9 and D11 (D10 is settled in the technical review, T1).

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| F1 | Should fix | `:522`, References | evidence | The Pham reference has no volume, issue or pages (settles D8). |
| F2 | Should fix | `:210`, Section 4.1 | evidence | The forward-backward integration is attributed to both 1985 papers; only the numerical-integration method as later described (Bobrow et al., Pham) can be confirmed (settles D11). |
| F3 | Should fix | `:210`, Section 4.1 | evidence | "The joint acceleration limits used here are the special case ... and the same structure holds" has no source: both 1985 papers treat torque limits, and this entry also imposes joint speed limits. |
| F4 | Should fix | `:26`, Section 1.2 | evidence | "develop the decoupled approach first" is only partly verified (settles D9, first claim). |
| F5 | Should fix | `:311`, Section 5.2 | evidence | What de Boor and Siciliano et al. contain could not be checked against the books (settles D9, third claim). |
| F6 | Optional | `:518`–`:524`, References | evidence | DOIs exist for every journal entry and the two Springer books; standards 7.3 prefer them. |

### F1. Pham (2014): volume, issue and pages
- **Where:** `:522`
- **Text:** "Q.-C. Pham, "A general, fast, and robust implementation of the time-optimal path parameterization algorithm," *IEEE Transactions on Robotics*, 2014."
- **Problem:** Standards 7.3 require volume, issue and pages when they exist. The paper exists (arXiv:1312.6533, v2 of 23 September 2014, Q.-C. Pham, Nanyang Technological University). Citing papers in Springer journals list it as *IEEE Trans. Robot.* 30(6), 1533–1540, December 2014, DOI 10.1109/TRO.2014.2351113. The author's TOPP repository (github.com/quangounet/TOPP) asks users to cite this paper. Two independent search passes gave the same volume, issue, pages and DOI and nothing contradicted them. IEEE Xplore itself could not be reached (proxy refusal).
- **Correction:** "Q.-C. Pham, "A general, fast, and robust implementation of the time-optimal path parameterization algorithm," *IEEE Transactions on Robotics*, vol. 30, no. 6, pp. 1533–1540, 2014." If the resolver can open doi.org/10.1109/TRO.2014.2351113, confirm the page range there; it is listed under Not verified until then.

### F2. Attribution of the forward-backward algorithm (D11)
- **Where:** `:210`
- **Text:** "Their algorithms integrate forward from the start with maximum acceleration and backward from the goal with maximum deceleration, and find the switching points between these curves."
- **Problem:** Shin and McKay's abstract (IEEE TAC, vol. AC-30, no. 6, June 1985, as indexed) says only that the solution "is deduced in an algorithm form using phase-plane techniques". Their switching-point procedure could not be read (the PDF host was refused), so it cannot be confirmed that their algorithm integrates in this way. Bobrow et al. and the later numerical-integration literature (Pham 2014, which calls the method "numerical integration" and builds it from forward and backward integration and a search for switch points on the velocity limit curve) do describe the method this way.
- **Correction:** "Bobrow et al. compute it by integrating forward from the start with maximum acceleration and backward from the goal with maximum deceleration, and by finding the switching points that join these curves; this numerical-integration method is the one most later implementations refine." Keep "and, independently, Shin and McKay treated this problem in 1985", which both papers support.

### F3. The "special case" of acceleration limits needs a source and a qualifier
- **Where:** `:210`
- **Text:** "The joint acceleration limits used here are the special case of a robot whose dynamics are ignored, and the same structure holds."
- **Problem:** The reduction itself is correct by derivation: the torque constraint of the 1985 papers has the form $a(s)\ddot s + b(s)\dot s^2 + c(s) \in [\tau_{\min}, \tau_{\max}]$. With identity inertia, no velocity-product terms and no gravity, it becomes the article's own inequality (`:199`), with $a = \sigma'$, $b = \sigma''$ and $c = 0$. But the cited sources do not state this case, and "the same structure holds" is not exactly true once joint *speed* limits are added. The scaling then also runs along the velocity limit curve where neither $U$ nor $L$ is active, as this entry's own output shows (T1). The case of bounded joint accelerations *and* velocities is treated explicitly by T. Kunz and M. Stilman, "Time-optimal trajectory generation for path following with bounded acceleration and velocity," *Robotics: Science and Systems VIII*, 2012 (DOI 10.15607/RSS.2012.VIII.027; listed by DBLP and the RSS online proceedings, paper p27). Its existence was confirmed. Its text was not read, so only the scope from its abstract is relied on.
- **Correction:** "The joint acceleration limits used here are the special case of a robot with identity inertia and no velocity-dependent or gravity terms; adding joint speed limits contributes one more boundary, which the scaling may follow (Kunz and Stilman treat this case)." Add to References: "T. Kunz and M. Stilman, "Time-optimal trajectory generation for path following with bounded acceleration and velocity," in *Robotics: Science and Systems VIII*, 2012." Alternatively drop the attribution and keep only the derivation (the text then states the reduction as its own and says so).

### F4. Lynch and Park, Siciliano et al. and the decoupled approach (D9, first claim)
- **Where:** `:26`
- **Text:** "The textbooks of Lynch and Park and of Siciliano et al. develop the decoupled approach first, and this series follows it"
- **Problem:** Lynch and Park, Chapter 9 "Trajectory Generation" (pp. 282–305, CUP 2017), defines a trajectory as a path plus a time scaling $s(t): [0, T] \to [0, 1]$, as confirmed from the Northwestern course pages and slides. Siciliano et al. have a "Trajectory Planning" chapter (Springer, 2009, DOI 10.1007/978-1-84628-642-1), but its text was not reachable. "First" (before kinodynamic planning, or as their main treatment) cannot be confirmed for either book and adds nothing.
- **Correction:** "The textbooks of Lynch and Park (Chapter 9) and of Siciliano et al. (Chapter 4) present trajectory generation in this decoupled form, and this series follows it; its limits are stated where they matter." Confirm the Siciliano chapter number against the book before publishing. Otherwise write "in their chapters on trajectory planning".

### F5. Content of de Boor and Siciliano et al. on splines (D9, third claim)
- **Where:** `:311`
- **Text:** "De Boor's book treats these spline systems and their end conditions in detail, and Siciliano et al. apply cubic splines through joint-space points in the same way."
- **Problem:** The de Boor edition is confirmed: *A Practical Guide to Splines*, revised edition, Springer, 2001, Applied Mathematical Sciences 27, ISBN 978-0-387-95366-3 (Springer's catalogue page); the reference is correct. Its treatment of cubic spline interpolation with end conditions (Chapter IV) is standard knowledge of the book but was not read here. For Siciliano et al., only secondary lecture notes (De Luca, Sapienza, "Robotics 1: Trajectory planning") describing splines through joint-space knots were seen, not the book. From the reviewer's knowledge, the book sets up its system in the knot *velocities*, not the knot accelerations, so "in the same way" is likely too strong.
- **Correction:** "De Boor's book treats cubic spline interpolation and its end conditions in detail, and Siciliano et al. use cubic splines through joint-space path points." Before publishing, the resolver either confirms both against the books or removes the Siciliano clause.

### F6. DOIs (optional)
- Bobrow et al.: 10.1177/027836498500400301 (seen in the CiteDrive record). Shin and McKay: 10.1109/TAC.1985.1104009 (seen in a citing source). Pham: 10.1109/TRO.2014.2351113. Siciliano et al.: 10.1007/978-1-84628-642-1. Add them if the series adds DOIs elsewhere; otherwise leave them out (the other entries do not use DOIs, and consistency matters more).

### Verification table

| Claim | Location | Status | Source |
|---|---|---|---|
| Bobrow, Dubowsky and Gibson, IJRR vol. 4, no. 3, pp. 3–17, 1985; minimum time along a given path under torque limits, known dynamics | `:210`, `:518` | Verified | CiteDrive record (DOI 10.1177/027836498500400301, abstract); Springer chapter reference list with the same vol./no./pp. |
| Shin and McKay, IEEE TAC vol. AC-30, no. 6, pp. 531–541, June 1985; phase-plane solution under torque/force limits; independent of Bobrow et al. | `:210`, `:523` | Verified (start page from the PDF header seen in search; end page from citing records) | University of Michigan RTCL PDF listing; N. McKay's CV; Semantic Scholar record |
| Both 1985 papers integrate forward and backward | `:210` | Partly verified | Bobrow et al. and Pham 2014 describe this method; Shin and McKay's procedure not read (F2) |
| Acceleration limits are a special case with the same structure | `:210` | Unsupported as attributed; correct by derivation for acceleration limits only | Derivation (F3); Kunz and Stilman 2012 for acceleration plus velocity limits |
| Pham 2014: singular cases where earlier implementations failed; robust implementation | `:210`, `:522` | Verified (claim); bibliographic detail corrected (F1) | arXiv:1312.6533 abstract ("dynamic singularities ... main cause of failure"); citing records |
| Flash and Hogan, J. Neurosci. vol. 5, no. 7, pp. 1688–1703, 1985; minimum-jerk model of reaching | `:85`, `:520` | Verified | Wikidata record Q28235524; abstract (squared jerk integrated over the movement) |
| The quintic minimizes integrated squared jerk among rest-to-rest motions with zero end accelerations | `:85` | Verified | Flash and Hogan 1985 (point-to-point solution is the fifth-order polynomial); Euler–Lagrange condition $s^{(6)} = 0$ |
| Lynch and Park, *Modern Robotics*, CUP, 2017 | `:521` | Verified | Cambridge Core chapter listing |
| Lynch and Park derive polynomial and trapezoidal scalings and describe the S-curve (seven segments) | `:190` | Verified | Northwestern Modern Robotics Chapter 9 pages and slides (third- and fifth-order polynomials, trapezoidal, S-curve with seven segments) |
| Textbooks "develop the decoupled approach first" | `:26` | Partly verified; reworded (F4) | Lynch and Park Chapter 9 definitions |
| de Boor, *A Practical Guide to Splines*, revised ed., Springer, 2001 | `:519` | Verified | Springer catalogue (ISBN 978-0-387-95366-3, AMS 27) |
| de Boor treats the spline systems and end conditions; Siciliano et al. apply splines "in the same way" | `:311` | Not verified (F5) | n/a |
| Siciliano, Sciavicco, Villani and Oriolo, *Robotics: Modelling, Planning and Control*, Springer, 2009 | `:524` | Verified | ResearchGate / Springer DOI 10.1007/978-1-84628-642-1 |
| Kinodynamic planning = planning geometry and timing together in the state space | `:26` | Verified (standard definition) | Lynch and Park Chapter 10; common usage |
| Trapezoid is minimum time for one axis with symmetric velocity and acceleration limits | `:138`, `:212` | Verified (standard bang-bang result; also derived in Section 4.1) | Lynch and Park Chapter 9; derivation |

### Not verified
- Pham 2014 page range 1533–1540 against IEEE Xplore (unreachable; two consistent citing records). F1 adds it; confirm at the DOI if possible.
- Shin and McKay's switching-point procedure (full text unreachable). F2 narrows the attribution.
- The content of de Boor's Chapter IV and of Siciliano et al.'s Chapter 4 on splines (books not reachable). F5 qualifies the sentence.
- The chapter number of the trajectory-planning chapter in Siciliano et al. (F4).
- The text of Kunz and Stilman 2012 beyond its abstract and listing (F3 relies only on its stated scope).

Verdict (fact-check): **fail** until F1–F5 are applied or answered. No reference was found to be nonexistent; every cited work exists and its listed bibliographic details are right, except that Pham's are incomplete.

## Technical review

Stage: EOS step 6.4, by a reviewer who did not write or revise the entry. Environment: Python 3.13.16, NumPy 2.5.3. Scratch scripts: `/tmp/claude-0/mp/review/trajectories-and-time-scaling/` (`tcheck.py`, `numcheck.py`, `rerun.txt`). This stage settles D10 (T1) and C7 to C10 (T6, T3, T8, T9).

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| T1 | Should fix | `:210`, `:281`, `:510` | accuracy | Switching structure: not every switch is on the velocity limit curve, and with speed limits the optimal scaling also slides along that curve with neither $U$ nor $L$ active (settles D10). |
| T2 | Blocking | `:281`, Section 4.3 | accuracy | "the path speed falls only from 0.84 to 0.83 s⁻¹": at $s = 0.566$ it is 0.8209 s⁻¹, so 0.82. |
| T3 | Should fix | `:283`, Section 4.3 | accuracy | The violation does shrink with the grid (in proportion to $1/N$), and 2.0023 rad/s² understates it: evaluated at the other end of each interval, joint 1 reaches 2.0079 rad/s² (settles C8). |
| T4 | Should fix | `:250`, Section 4.2 | accuracy | "assumes that $\dot s$ varies linearly in $s$": the step time $2\Delta s/(\dot s_k + \dot s_{k+1})$ assumes constant $\ddot s$ (so $\dot s$ linear in *time*); with $\dot s$ linear in $s$ the time from rest would be infinite. |
| T5 | Should fix | `:208`, Section 4.1 | accuracy | The interval $[L, U]$ becomes empty because different joints' requirements conflict, not because "the curvature term alone requires more acceleration than a joint can deliver" (that is only the case $\sigma_i' = 0$). |
| T6 | Should fix | `:181`, Section 3.3 | accuracy | "the five profiles" introduces a table of four (settles C7). |
| T7 | Optional | `:179`, Section 3.3 | accuracy | For $D = 0.05$ rad no constant-acceleration phase exists, so "the fixed ramp time $a/j$" is not what grows. |
| T8 | Optional | `:39`, Section 1.2 | accuracy | Jerk limits stated as coming only from the structure (settles C9). |
| T9 | Optional | `:250`, Section 4.2 | accuracy | "setting the gripper's acceleration along the path to zero" should say $d^2p/ds^2 = 0$ (settles C10). |

### T1. Where the time-optimal scaling switches (D10)
- **Where:** `:210`, also `:281` and the Summary row `:510`
- **Text:** "At every point it uses either the largest acceleration $U$ or the smallest $L$, and it switches between them at points that touch the velocity limit curve." / "they have the bang-bang structure that the theory predicts" / "Bang-bang in the $(s, \dot s)$ plane, touching the velocity limit curve"
- **Problem:** In the phase-plane method a switch from deceleration to acceleration lies on the velocity limit curve, and a switch from acceleration to deceleration lies where a forward maximum-acceleration curve meets a backward maximum-deceleration curve. The second kind is generally below the curve. The program confirms this: at the switch $s = 0.235$, $\dot s = 0.8372$ s⁻¹ against a velocity limit curve of $0.9080$ s⁻¹ (`tcheck.py`). With joint speed limits the optimal scaling can also run *along* the velocity limit curve with neither bound active. On the stretch $s \in [0.566, 0.818]$ of this entry's own output, joint 1 sits at its speed limit with $\ddot q_1 \approx 0$ and joint 2's acceleration lies between $-1.995$ and $-1.477$ rad/s², strictly inside $\pm 2.0$. So "at every point ... either $U$ or $L$" and "bang-bang" are contradicted by the result the text presents.
- **Correction:** `:210`: "They showed that the time-optimal scaling follows the boundary of what is allowed: at every point it uses the largest acceleration $U$ or the smallest $L$, or it runs along the velocity limit curve. It switches from deceleration to acceleration only at points of the velocity limit curve, and from acceleration to deceleration where a forward curve of maximum acceleration meets a backward curve of maximum deceleration." (Combine with F2 and F3 for the next two sentences.) `:281`: "The last four lines show which constraint is active along the path, and they have the structure that the theory predicts." `:510`: "Maximum acceleration, maximum deceleration or the velocity limit curve at every point of the $(s, \dot s)$ plane; a trapezoid on a straight joint-space line".

### T2. Path speed over the lower-bound stretch
- **Where:** `:281`
- **Text:** "the path speed falls only from 0.84 to 0.83 s⁻¹ over this stretch"
- **Problem:** Recomputed with the writer's `time_optimal` ($N = 2000$): $\dot s(0.235) = 0.8372$ and $\dot s(0.566) = 0.8209$ s⁻¹. To two decimals that is 0.84 to 0.82. (The 0.8320 printed at $s = 0.50$ is not the end of the stretch.) The point of the sentence stands.
- **Correction:** "the path speed falls only from 0.84 to 0.82 s⁻¹ over this stretch."

### T3. The acceleration violation and the grid (C8)
- **Where:** `:283`
- **Text:** "The joint accelerations implied by the discretized profile reach 2.0023 rad/s² on joint 2, 0.12% above the limit, ... The duration converges as the grid is refined (1.8207 s with 250 intervals, 1.8178 s with 4000), but the small violation does not vanish on its own."
- **Problem:** With the program's own check extended to every grid (`tcheck.py`), the joint 2 peak evaluated with the geometry at the start of each interval is 2.0155, 2.0094, 2.0047, 2.0023, 2.0012 and 2.0006 rad/s² for $N$ = 250, 500, 1000, 2000, 4000 and 8000. It halves with each doubling, so the violation shrinks in proportion to $1/N$ and tends to zero, although it is positive at every finite $N$. "Does not vanish on its own" reads as the opposite. The same profile evaluated with the geometry at the *end* of each interval gives joint 1 2.0079 rad/s² at $N = 2000$ (0.39%; 2.0626 at $N = 250$, 2.0040 at $N = 4000$). The single quoted figure therefore depends on where in the interval the check looks, and it understates the excess.
- **Correction:** "The joint accelerations implied by the discretized profile exceed the limit slightly, because each pass evaluates the acceleration bounds at one end of a grid interval and assumes they hold across it: evaluated at the start of each interval, joint 2 reaches 2.0023 rad/s² (0.12% above the limit), and evaluated at the end, joint 1 reaches 2.0079 rad/s² (0.39%). Refining the grid shrinks both the error in the duration (1.8207 s with 250 intervals, 1.8178 s with 4000) and the violation, roughly in proportion to the grid spacing, but the violation remains at every finite resolution." The new numbers must be printed by `timeopt.py` (extend the convergence loop to print the peak accelerations at both interval ends), with `run.sh`, `output.txt` and the quoted output block updated together.

### T4. What the step-time formula assumes
- **Where:** `:250`
- **Text:** "The time of each step assumes that $\dot s$ varies linearly in $s$ between grid points."
- **Problem:** The code uses `dt = 2*ds/(sd[:-1] + sd[1:])`, the arithmetic mean of the end speeds. That is exact when $\ddot s$ is constant over the step: then $x = \dot s^2$ is linear in $s$ (the passes' own assumption, $dx/ds = 2\ddot s$) and $\dot s$ is linear in *time*. If $\dot s$ were linear in $s$, the step time would be $\Delta s\,\ln(\dot s_{k+1}/\dot s_k)/(\dot s_{k+1} - \dot s_k)$, which is infinite for the first step from rest. Recomputed: the arithmetic-mean total is 1.8180 s; the linear-in-$s$ formula gives infinity.
- **Correction:** "The time of each step assumes that $\ddot s$ is constant between grid points, so that $x = \dot s^2$ varies linearly in $s$ and the step takes $2\,\Delta s/(\dot s_k + \dot s_{k+1})$."

### T5. Why the acceleration interval becomes empty
- **Where:** `:208`
- **Text:** "or the interval $[L, U]$ becomes empty because the curvature term $\sigma''(s)\,\dot s^2$ alone requires more acceleration than a joint can deliver."
- **Problem:** For a joint with $\sigma_i' \ne 0$, its own constraint can always be met by some $\ddot s$, however large the curvature term. The interval is empty when the intervals allowed by *different* joints no longer overlap. Only when $\sigma_i' = 0$ (Exercise 4) does one joint's curvature term alone decide. In the worked example the velocity limit curve is set by this acceleration condition, below the speed bound, at 538 of the 2001 grid points ($0.214 \le s \le 0.483$), and both $\sigma_i'$ are nonzero there (`tcheck.py`).
- **Correction:** "or the interval $[L, U]$ becomes empty: at that speed the curvature term $\sigma''(s)\,\dot s^2$ demands accelerations that no single value of $\ddot s$ can keep within the limits of all joints at once (with only one joint, this happens only where $\sigma_i'(s) = 0$, as in Exercise 4)."

### T6. Number of profiles in the table (C7)
- **Where:** `:181`
- **Problem:** The table has four rows. The triangular profile does not apply to this move ($D = 1.5$ rad $\ge v^2/a = 0.5$ rad), so no row is missing.
- **Correction:** "The table compares the four profiles of Sections 2 and 3 for the same move of the running example."

### T7. Cause of the growing relative cost (optional)
- **Where:** `:179`
- **Text:** "because the fixed ramp time $a/j$ becomes a larger part of the motion"
- **Problem:** True for the cases that reach $a$ (10% at 1.5 rad, 29% at 0.3 rad). At 0.05 rad no constant-acceleration phase exists and the ramps last $\sqrt{v_p/j} = 0.136$ s each, not $a/j$. As $D \to 0$ the ratio $4(D/2j)^{1/3}/(2\sqrt{D/a})$ grows without bound.
- **Correction:** "because the jerk ramps, whose duration does not shrink in proportion to the distance, take up a larger part of a short motion."

### T8. Source of jerk limits (C9, optional)
- **Correction:** Accept the copy editor's qualifier: "Jerk limits come mainly from the structure rather than the motor: ...". Drive current-rate limits also bound jerk, so the absolute form is not true in general.

### T9. Second derivative of the line path (C10, optional)
- **Problem:** `arm.py:36` solves $J\sigma'' = -(\text{centripetal terms})$ with the comment `d2p/ds2 = 0 on a line`; what is zero is the second derivative of the gripper position with respect to $s$.
- **Correction:** "and $\sigma''$ follows from differentiating the forward kinematics twice with respect to $s$ and setting $d^2p/ds^2$, the second derivative of the gripper position along the line, to zero."

### Log of what was recomputed and run
- `run.sh` rerun (Python 3.13.16, NumPy 2.5.3): output identical to `output.txt` (diff empty), and every output block in the article matches it character for character. All programs are deterministic; no random seeds are involved.
- The five Python listings in the article were extracted and matched line by line against `polynomial.py`, `profiles.py`, `timeopt.py`, `spline.py` and `check.py`: no listing line is missing from its program; the omissions are the ones the text names (the peak-sampling loop, `x_limit`, IK, `path`, `spline_eval`, printing).
- Cubic and quintic: coefficients from the boundary conditions; $\dot s_{\max} = 1.5/T$, $15/(8T)$; $|\ddot s|_{\max} = 6/T^2$, $10/(\sqrt3\,T^2) = 5.7735/T^2$ at $\tau = 0.2113$; quintic end jerk $60/T^3$. All confirmed.
- Section 2.3 durations 2.2500/2.1213 s and 2.8125/2.0809 s: confirmed.
- Trapezoid and triangle formulas; $T = 2.0$ s for joint 1; synchronized $\dot s_{\max} = 0.6667$, $\ddot s_{\max} = 1.3333$, joint 2 peak 0.8 rad/s: confirmed.
- S-curve: all four cases rederived, including $v_p = (D^2 j/4)^{1/3}$, $T = 4(D/2j)^{1/3}$ and the quadratic. Values 2.2000, 1.0000 (peak 0.6), 0.5429 s (peak 0.1842), triangle 0.7746 and 0.3162 s, "about 72% longer" (1.7167): confirmed.
- Time-optimal: $T = 1.8180$ s; quintic 2.2962 s with $\sqrt{5.0918} = 2.2565$; "about 21% faster" (20.8%); 0.12% (0.115%); joint 2 at $-2.0$ rad/s² on $[0.235, 0.566]$ (min $-2.0021$); joint 2 reverses at $s = 0.5995$; line distance 1.1314–1.4142 m from the base; $\theta_2 \in [1.198, 1.721]$, so $\sin\theta_2 > 0$. All confirmed except T2. The convergence and the two-ends check are T3.
- Splines: the tridiagonal equations and both end conditions were rederived. `spline_moments` matches a dense `numpy.linalg.solve` to $4.4 \times 10^{-16}$ for both joints and both end conditions. Strict diagonal dominance was checked row by row. The gripper waypoints (1.065, 0.195), (0.774, 0.662), (0.666, 1.246), (0.520, 1.541) m are confirmed.
- Checking: true peaks of the clamped spline at 1 µs resolution are joint 1 0.890919 rad/s and 2.491554 rad/s², joint 2 1.072468 rad/s and 2.508446 rad/s². These are equal to four decimals to the 1 ms samples, so the motion bound 0.0023 m and the proven clearance $0.0672 - 0.0023 = 0.0649$ m hold. $k = \max(1.0725, \sqrt{1.2542}) = 1.1199$ is confirmed. Knot-time scaling gives knot accelerations that scale exactly by $1/k^2$ ($6.7 \times 10^{-16}$ error), as stated.
- Exercises 1–6: all answers recomputed and confirmed (Exercise 5: $M = (6, -6, 6)$; Exercise 6: 0.023 m and 4.35 ms, stated as 4.3 ms).
- Series consistency: the motion bound matches the first entry, Section 5.3 (`configuration-space-and-the-planning-problem.mdx:367`). All linked fragments exist (first entry 3.2, 4, 5, 5.3; third entry Section 6; `what-is-a-robot` Section 4; `planar-arm-kinematics` Section 5). Limits and link lengths agree with the series overview.
- `eos lint` on the file: 0 errors, 0 warnings, 0 suggestions. No site build was needed (no change was made).

Verdict (technical): **fail** until T1–T6 are applied (T2 is blocking). The derivations, code and quoted outputs are otherwise correct and reproduce exactly.

## Resolution

By the author. The final `eos lint` reports 0 errors, 0 warnings and 0 suggestions. `run.sh` was rerun and its output is identical to `output.txt`. Every `text` output block in the article appears verbatim in `output.txt`. A scratch build had no KaTeX errors, and `check-links` reported no broken link for this page.

| ID | Action | Exact change |
|---|---|---|
| D1–D7, C1–C6 | Applied by the editors | Kept as revised. |
| D8 | Settled by F1 | See F1. |
| D9 | Settled by F4 and F5 | See F4 and F5. |
| D10 | Settled by T1 | See T1. |
| D11 | Settled by F2 | See F2. |
| C7 | Settled by T6 | See T6. |
| C8 | Settled by T3 | See T3. |
| C9 | Settled by T8 | See T8. |
| C10 | Settled by T9 | See T9. |
| F1 | Applied | The Pham reference now reads "*IEEE Transactions on Robotics*, vol. 30, no. 6, pp. 1533–1540, 2014." These details come from two consistent citing records; IEEE Xplore was not reached, so they stay listed under Not verified. |
| F2 | Applied | "Their algorithms integrate forward ..." became "Bobrow et al. compute it by integrating forward from the start with maximum acceleration and backward from the goal with maximum deceleration, and by finding the switching points that join these curves." Shin and McKay are still named only as having treated the problem independently. |
| F3 | Applied with changes (as the coordinator directed) | "The joint acceleration limits used here are the special case ... and the same structure holds." became: "The joint acceleration constraint of this entry is a special case of their torque constraint: for a robot with identity inertia and no velocity-dependent or gravity terms, the torque bound becomes the inequality above. Joint speed limits add one more boundary, which the scaling may follow; Kunz and Stilman treat time-optimal path following with bounded acceleration and velocity." The reduction is stated as the entry's own derivation, and Kunz and Stilman are cited only for the scope given in their abstract. Added to References: "T. Kunz and M. Stilman, "Time-optimal trajectory generation for path following with bounded acceleration and velocity," in *Robotics: Science and Systems VIII*, 2012." |
| F4 | Applied with changes | "The textbooks of Lynch and Park and of Siciliano et al. develop the decoupled approach first, and this series follows it" became "Lynch and Park present trajectory generation in this decoupled form, as a path combined with a time scaling, and this series follows it". The claim about Siciliano et al. could not be confirmed and was dropped, as was any chapter number. |
| F5 | Applied with changes | The sentence became "De Boor's book treats cubic spline interpolation and its end conditions in detail." The Siciliano clause could not be confirmed and was removed. That left Siciliano et al. uncited, so their reference was removed from References. |
| F6 | Not applied | The other entries in the series give no DOIs, and consistency across the series was preferred, as F6 itself allows. |
| T1 | Applied | Section 4.1 now reads: "at every point it uses the largest acceleration $U$ or the smallest $L$, or it runs along the velocity limit curve. It switches from deceleration to acceleration only at points of the velocity limit curve, and from acceleration to deceleration where a forward curve of maximum acceleration meets a backward curve of maximum deceleration." In Section 4.3, "the bang-bang structure" became "the structure", and the speed-limit stretch now ends "follows the velocity limit curve with neither $U$ nor $L$ active". The Summary row became "Maximum acceleration, maximum deceleration or the velocity limit curve at every point of the $(s, \dot s)$ plane; a trapezoid on a straight joint-space line". |
| T2 | Applied | "from 0.84 to 0.83 s⁻¹" became "from 0.84 to 0.82 s⁻¹". |
| T3 | Applied | `timeopt.py` gained `peak_accels`, and its convergence loop now prints, for N = 250, 500, 1000, 2000 and 4000, the duration and the peak joint accelerations with the geometry taken at the start and at the end of each interval. The separate `peak |joint acceleration|` line was removed. `run.sh` was rerun, `output.txt` regenerated, and the article's output block replaced with the new real output. The text now reads: "With 2000 intervals, evaluated at the start of each interval, joint 2 reaches 2.0023 rad/s² (0.12% above the limit); evaluated at the end, joint 1 reaches 2.0079 rad/s² (0.39%). Refining the grid shrinks both the error in the duration (1.8207 s with 250 intervals, 1.8178 s with 4000) and the violation, which halves with each doubling of the grid, but the violation remains at every finite resolution." |
| T4 | Applied | "assumes that $\dot s$ varies linearly in $s$" became "assumes that $\ddot s$ is constant between grid points, so that $x = \dot s^2$ varies linearly in $s$ and the step takes $2\,\Delta s/(\dot s_k + \dot s_{k+1})$". |
| T5 | Applied | The sentence now reads "or the interval $[L, U]$ becomes empty. At that speed the curvature term $\sigma''(s)\,\dot s^2$ demands accelerations that no single value of $\ddot s$ can keep within the limits of all joints at once; with only one joint, this happens only where $\sigma_i'(s) = 0$, as in Exercise 4." |
| T6 | Applied | "the five profiles" became "the four profiles". |
| T7 | Applied | "because the fixed ramp time $a/j$ becomes a larger part of the motion" became "because the jerk ramps, whose duration does not shrink in proportion to the distance, take up a larger part of a short motion". |
| T8 | Applied | "Jerk limits come from the structure" became "Jerk limits come mainly from the structure". |
| T9 | Applied | The sentence now reads "$\sigma''$ follows from differentiating the forward kinematics twice with respect to $s$ and setting $d^2p/ds^2$, the second derivative of the gripper position along the line, to zero". |
| Lint | Applied | Two paragraph-length suggestions caused by the new text were removed by splitting the paragraphs in Sections 4.1 and 4.3 before "Bobrow et al. compute it" and "A practical implementation". |

Still not verified: the Pham page range (not checked against IEEE Xplore), and Kunz and Stilman beyond their abstract (they are cited only for its stated scope).
