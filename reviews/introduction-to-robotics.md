# Series review: Introduction to Robotics

- Series: `introduction-to-robotics` (4 articles, status published, 0 planned entries)
- Reviewed commit: 9232ed9 (the four articles and the series file are unchanged since the wave-1 revision 530f71c and have no uncommitted changes)
- Date: 2026-10-13
- Review: independent review (wave 2) of the wave-1 revision; fact-check (F), technical review (T) and series review (S) combined in one report. Previous reviews (two passes, all findings applied) are superseded by this report.

## Summary

The wave-1 revision kept every earlier correction and added an Exercises section to each entry (nine exercises in all), a sequence rationale and shared conventions to the overview, and completed references. Every exercise answer and every worked number in the four entries was recomputed with Python and is correct; the build has no KaTeX errors, no Mermaid diagram wider than the column, no glued inline text, and all internal links resolve. The problems found are small: one answer describes a Mahalanobis distance in the wrong units ("two standard deviations from the prediction"), one reference lists an editor as author (Nilsson, *Shakey the Robot*), and one dated attribution gives the unscented Kalman filter a 1997 origin although Julier, Uhlmann and Durrant-Whyte published the method in 1995. There are no blocking findings; the series is ready as published once the three should-fix items are corrected.
Findings: 0 blocking, 3 should fix, 3 optional.

## Objectives coverage

| Objective (from the series file) | Covered by | Assessment |
|---|---|---|
| Describe a robot as mechanical structure, actuators, sensors, and computation connected by a control loop. | Entry 1, Sections 1–4, Exercises 1–3 | Met. |
| Represent the position and orientation of rigid bodies using coordinate frames and rotation matrices. | Entry 2, Sections 1–7, Exercises 1–3 | Met. |
| Explain forward and inverse kinematics for a simple planar arm. | Entry 3, Sections 2–6, Exercises 1–3 | Met. |
| Outline the sense, plan, and act structure used in many robot software architectures. | Entry 1, Section 5 | Met (brief but adequate; no exercise, which is reasonable for a descriptive objective). |
| Explain why a robot must estimate its state, and how a Kalman filter combines a motion model with noisy measurements. | Entry 4, Sections 1–5, Exercises 1–3 | Met. |

## Findings

| ID | Severity | Article | Location | Dimension | Finding |
|---|---|---|---|---|---|
| T1 | Should fix | `src/content/blog/sensing-and-state-estimation.mdx` | Section 9, Exercise 3 answer (line 250) | accuracy | "about two standard deviations from the prediction": $d = 2.06$ is in innovation standard deviations ($\sqrt S = 0.58$ m), not prediction standard deviations (1.2/0.5 = 2.4). |
| F1 | Should fix | `src/content/blog/sensing-and-state-estimation.mdx` | Section 6.2 (line 184) | evidence | UKF "introduced by Julier and Uhlmann in 1997": the method was published in 1995 (Julier, Uhlmann and Durrant-Whyte, ACC). |
| F2 | Should fix | `src/content/blog/what-is-a-robot.mdx` | References (line 245) | evidence | Nilsson is the editor of SRI Technical Note 323, not its author. |
| T2 | Optional | `src/content/blog/sensing-and-state-estimation.mdx` | Section 9, Exercise 1 (lines 227, 232) | accuracy | "Why does the estimate move less": the move is smaller also because the innovation is half as large; the answer explains only the gain. |
| S1 | Optional | `src/content/blog/what-is-a-robot.mdx` | Opening (line 18) | consistency | Link text "control systems series" points to the first article of that series, not the series page. |
| S2 | Optional | `src/content/blog/planar-arm-kinematics.mdx` | Section 5.2 (line 168) | language | "outwards" (British form; house variant is American). |

### T1. Units of the gating distance in Exercise 3
- **Where:** `src/content/blog/sensing-and-state-estimation.mdx:250`, section "9. Exercises", Exercise 3 answer
- **Text:** "$d^2 = 1.2^2/0.34 = 4.24$, below the bound of 6.63, so the reading is accepted, although it lies about two standard deviations from the prediction."
- **Problem:** Section 8 (line 221) defines $d^2$ as measuring "the innovation in units of its own expected spread", i.e. in standard deviations of the innovation, $\sqrt{S} = \sqrt{0.34} = 0.583$ m. Recomputed (python3): $\sqrt{4.24} = 2.06$ innovation standard deviations; measured against the prediction's standard deviation (0.5 m) the same innovation is 1.2/0.5 = 2.4. "Two standard deviations from the prediction" invites the second reading, and a reader checking it gets 2.4, in the one answer that is meant to teach what the Mahalanobis distance measures.
- **Recommended correction:** replace the clause with: "although it lies about two standard deviations of the innovation ($\sqrt{4.24} = 2.06$, with $\sqrt{S} = 0.58$ m) from the predicted measurement."

### F1. Origin of the unscented Kalman filter
- **Where:** `src/content/blog/sensing-and-state-estimation.mdx:184`, section "6.2 The unscented Kalman filter"
- **Text:** "The **unscented Kalman filter** (UKF), introduced by Julier and Uhlmann in 1997, avoids derivatives."
- **Problem:** The filter was presented in S. J. Julier, J. K. Uhlmann and H. F. Durrant-Whyte, "A new approach for filtering nonlinear systems," Proceedings of the 1995 American Control Conference (IEEE document 529783; checked in the BVB library catalogue record, whose abstract describes the sigma-point parameterization of mean and covariance and the comparison with the EKF). The 1997 SPIE paper cited in the References is the usual reference and is correctly cited, but "introduced ... in 1997" dates the method two years late and drops a co-author of the first paper.
- **Recommended correction:** "The **unscented Kalman filter** (UKF), developed by Julier and Uhlmann in the mid-1990s (their 1997 paper cited below is the usual reference), avoids derivatives." No new reference is needed.

### F2. Nilsson is the editor of *Shakey the Robot*
- **Where:** `src/content/blog/what-is-a-robot.mdx:245`, References
- **Text:** "N. J. Nilsson, *Shakey the Robot*, Technical Note 323, SRI International, 1984."
- **Problem:** The title page of the note (Stanford copy, ai.stanford.edu/~nilsson/OnlinePubs-Nils/shakey-the-robot.pdf) reads "Edited by: Nils J. Nilsson, Director, Artificial Intelligence Center", Technical Note 323, April 1984; SRI's publication page also lists "N. J. Nilsson (Ed.)". The note collects reports by several authors, so listing Nilsson as author misstates the work (standards 7.3).
- **Recommended correction:** "N. J. Nilsson, Ed., *Shakey the Robot*, Technical Note 323, Artificial Intelligence Center, SRI International, 1984." (The Vietnamese translation's reference list needs the same change.)

### T2. "Why does the estimate move less"
- **Where:** `src/content/blog/sensing-and-state-estimation.mdx:227` (question) and `:232` (answer)
- **Text:** "Why does the estimate move less than in the corridor example of Section 4?" / "... so the gain is below one half and the estimate stays nearer the prediction."
- **Problem:** The estimate moves 0.09 m against 0.44 m in Section 4 (recomputed), for two reasons: the gain is smaller (0.308 against 0.735) and the innovation is half as large (0.3 m against 0.6 m). The answer explains only the first, which is what the question means to ask.
- **Recommended correction:** question: "Why does the estimate move a smaller fraction of the way toward the measurement than in the corridor example of Section 4?" (answer unchanged).

### S1. Link text in the opening of entry 1
- **Where:** `src/content/blog/what-is-a-robot.mdx:18`
- **Text:** "The entry uses the idea of feedback from the [control systems series](/blog/introduction-to-control-systems)"
- **Problem:** The link text names a series, the target is that series' first article (line 32 links the same article correctly as "first entry of the control systems series"; the overview links `/series/foundations-of-control-systems`).
- **Recommended correction:** change the target to `/series/foundations-of-control-systems`, or the text to "the [first entry of the control systems series](/blog/introduction-to-control-systems)" and shorten line 32's repeat.

### S2. "outwards"
- **Where:** `src/content/blog/planar-arm-kinematics.mdx:168`, section "5.2 Singular configurations"
- **Text:** "A stretched arm cannot move its gripper straight outwards"
- **Recommended correction:** "straight outward".

## Concept introduction map

| Concept | First used (path:line) | Introduced where | Assessment |
|---|---|---|---|
| Feedback / closed loop | `what-is-a-robot.mdx:32` | Same line, with link to the control series | Adequate. |
| Degree of freedom, mobility formula | `what-is-a-robot.mdx:79, 85` | Same place; Exercise 1 applies the planar form | Adequate. |
| Torque, inertia, transmission | `what-is-a-robot.mdx:101–109` | Same place; prerequisite in the overview | Adequate; Exercise 2 uses only these formulas. |
| Encoder resolution, backlash | `what-is-a-robot.mdx:118–124` | Same place | Adequate; Exercise 3 reuses Section 2.4. |
| Rotation matrix, $SO(3)$, homogeneous transform | `coordinate-frames-and-transformations.mdx:42, 81, 148` | Same places | Adequate. |
| atan2 and angle wrapping | `coordinate-frames-and-transformations.mdx:247` | Same row (defined) | Adequate; used in Exercise 3 and in entries 3 and 4 with back-references. |
| Joint/task space, Jacobian, singularity | `planar-arm-kinematics.mdx:25, 147, 166` | Same places | Adequate. |
| Random variable, density, variance, covariance, Gaussian | `sensing-and-state-estimation.mdx:52–63` | Section 2, as the overview promises | Adequate. |
| Innovation, gain, Bayes filter | `sensing-and-state-estimation.mdx:103–119` | Same places | Adequate. |
| Mahalanobis distance, chi-square, gating | `sensing-and-state-estimation.mdx:221` | Same line | Adequate; Exercise 3 relies on it (see T1). |

## Versions, defaults and conventions

| Assumption | Where it appears | Stated in the text? | Assessment |
|---|---|---|---|
| SI units | All entries; exercises give N·m, kg·m², m, m² | Overview; entry 1 line 18; entry 4 line 34 | Consistent. |
| Radians in computation, degrees in examples | Entries 2–4 and their exercises | Overview; entry 2 line 19; entry 3 line 71; entry 4 line 34 | Consistent; exercises quote degrees and compute correctly. |
| Right-handed frames, column vectors, left multiplication | Entry 2 and later | Overview; entry 2 lines 19, 25 | Consistent. |
| Heading measured counter-clockwise from world $x$ | Entry 2 Section 5, Exercise 1 and 3 ("turn to the left") | Implied by Section 2.1 and the worked example ("heading 90°: its x axis points along the world's y axis") | Adequate. |
| Euler angle order $R_z R_y R_x$ | Entry 2 line 114 | Yes | Adequate. |
| Quaternion order $(w, x, y, z)$ | Entry 2 lines 126–132, 246 | Yes, and the alternative named | Adequate. |
| Relative joint angle $\theta_2$ | Entry 3 line 43 | Yes | Adequate. |
| Discrete-time $A$, $B$ vs continuous primer | Entry 4 line 162 | Yes | Adequate. |
| 99% one-dimensional chi-square gate 6.63 | Entry 4 line 221, Exercise 3 | Yes | Correct ($\chi^2_{1,0.99} = 6.635$). |

## Series design

**Purpose, audience and scope.** The overview names the reader (basic linear algebra, trigonometry, derivatives, introductory mechanics), says that probability is introduced in entry 4 and that the control series is useful but not required, and states the shared conventions. The five objectives each start with an assessable verb and are met (table above). The overview promises nothing the entries do not deliver: the per-entry descriptions match the section contents, and "the worked examples are small enough to check by hand" holds for every worked example and exercise.

**Sequence and rationale.** The overview's numbered list explains the order (machine, then geometry, then kinematics using that geometry, then estimation of the quantities entries 2 and 3 assumed known). The order is right for the stated reader; no entry needs moving, splitting or merging.

**Prerequisites and dependencies.** Nothing depends on a later entry. Entry 4 uses the Jacobian from entry 3 and wrapping from entry 2 with back-references. The new exercises use only material of their own entry (entry 3's exercises reuse its example arm; entry 4's reuse the corridor example).

**Notation and depth.** Symbols agree across entries ($n_b$, $n_j$, $f_i$; ${}^{A}T_{B}$; $\mathbf q$, $\mathbf x$, $J$; $P$, $Q$, $R$, $K$, $S$). With wave 1 every entry has three exercises with answers, so depth is now comparable; entry 1's exercises are proportionately lighter, which fits its descriptive role.

**Overview completeness.** Meets standards 6.5: coverage and order, reader and prerequisites, per-entry contribution, shared conventions, objectives.

## Series-level notes

- Structure is now uniform: unheaded opening (builds on, assumes, conventions), numbered sections, Exercises, Summary table with closing paragraph, References under the Summary. Entry 4's Summary ties back to the objectives and links the series page.
- Cross-references: all ordinal mentions ("first", "previous", "next", "last", "final", "second") name the right entry; the links added in wave 1 point to the right targets (S1 is a link-text mismatch only). "Section 2.2", "Section 2.4", "Section 3", "Section 4.3", "Section 5.2", "Section 8" in the exercises all resolve and say what is claimed. Inbound fragment links from `calibration-and-multisensor-fusion.mdx` to entry 4 still resolve (link check).
- Exercise answers use `<details>`/`<summary>`; they render (the build contains each "Exercise 1–3" and no KaTeX error).
- Wave-1 flag A1 (Pieper's condition stated only for intersecting axes): the sentence states a correct sufficient condition and does not claim it is the only one; no finding.

## Verification log

- Build: not run (instruction for this wave); the current site build at `/tmp/claude-0/b2` (SITE_URL=https://acrr.asia), made after commit 530f71c, contains the wave-1 text (checked: "AAAI Press/MIT Press", the Exercises sections, the Exercise 3 wording of entry 4). The four articles and the series file are unchanged between 530f71c and HEAD 9232ed9.
- `node scripts/check-links.mjs /tmp/claude-0/b2`: 314 pages, 9667 internal references, all resolve.
- Rendering: `grep -c katex-error` = 0 in all four pages; Mermaid min-widths 257 px and 313 px (entry 1), 215 px (entry 2), 309 px (entry 4), all under 600 px; no letter or punctuation glued to `<span`, `<strong>`, `<a ` or `<code` outside markup.
- `npm run -s eos -- lint introduction-to-robotics`: 0 errors, 0 warnings, 6 suggestions (acronym expansion of AAAI, MIT, SRI, SPIE, ASME in reference lists; not re-reported).
- `npm run -s eos -- syntax` on the five files: all compile.
- Recomputed (python3 -I, NumPy), new exercises:
  - Entry 1: Ex. 1 $M = 3(4-1-4)+4 = 1$; Ex. 2 $\tau_j = 20$ N·m, $\omega_j = 60$ rpm, $N^2 J_m = 0.05$ kg·m²; Ex. 3 $360/(2048 \cdot 50) = 0.003516^\circ$ (text 0.0035°). All correct.
  - Entry 2: Ex. 1 $(-1, 1)$; Ex. 2 ${}^{B}T_{A}$ with rows $(0, 1, 0)$, $(-1, 0, 3)$ and ${}^{B}T_{A}(3, 0, 1) = (0, 0, 1)$; Ex. 3 atan2 gives $+20.0^\circ$. All correct.
  - Entry 3: Ex. 1 $c_2 = 0.142857$, $\theta_2 = \pm 81.79^\circ$, atan2 terms $22.62^\circ$ and $32.20^\circ$, $\theta_1 = -9.58^\circ$ / $54.82^\circ$, both solutions map back to $(1.2, 0.5)$, printed partial terms 0.986, 0.214, −0.167, 0.667 correct; Ex. 2 $c_2 = 1.793$; Ex. 3 $\det J = 0.1216$ m², ratio to 0.495 = 0.246 ("about a quarter"); the joint speed needed for unit radial gripper speed is 15.1 rad/s at $\theta_2 = 10^\circ$ against 3.4 rad/s at $45^\circ$ (with $\theta_1 = 30^\circ$), confirming "correspondingly larger". All correct.
  - Entry 4: Ex. 1 $K = 0.3077$, $\hat x = 5.092$ m, $P = 0.02769$ m², $\sigma = 0.166$ m; Ex. 2 $n > 4.6$, $\sigma_4 = 0.475$ m, $\sigma_5 = 0.516$ m (same with unrounded $P = 0.06618$); Ex. 3 $d^2 = 4.235$, $d = 2.06$, $\sqrt S = 0.583$ m, $1.2/0.5 = 2.4$ (T1). Numbers correct; wording of Ex. 3 is T1.
- Recomputed, existing worked numbers: encoder $0.000879^\circ$; $R_x(90^\circ)R_z(90^\circ)$ and $R_z(90^\circ)R_x(90^\circ)$ as printed; gimbal lock pairs equal at $\theta = 90^\circ$ (difference) and at $-90^\circ$ (sum); planar FK $(1.0472, 1.1761)$; Newton errors 0.478, 0.113, 0.0116, $1.8\times10^{-4}$, $6.4\times10^{-8}$ ending at $(30^\circ, 45^\circ)$; first Newton step $(166.6^\circ, -401.6^\circ)$; first damped step $(1.80^\circ, -1.33^\circ)$; damped iteration ends at radius 1.700, 0.0507 from target; Kalman $K = 0.735$, $\hat x = 10.44$, $P = 0.066$, $\sigma = 0.257$; ten moves $\sigma = 0.683$; $d^2 = 1.06$ and $11.8$. All correct.
- References checked: Durrant-Whyte and Bailey vol. 13, no. 2, pp. 99–108, 2006 (BibBase record, DOI 10.1109/MRA.2006.1638022; matches wave-1 check of the article PDF); Julier and Uhlmann pp. 182–193, 1997 (SFB/TR 8 bibliography) and SPIE vol. 3068 (ModelDB citation); Kalman vol. 82, Series D, pp. 35–45, 1960 (UNC Welch–Bishop page); Brooks vol. 2, no. 1, pp. 14–23, March 1986 (J. M. Vidal library entry; Wikipedia "Allen (robot)"); Denavit and Hartenberg vol. 22, no. 2, pp. 215–221 (Wikipedia "Jacques Denavit"; DOI 10.1115/1.4011045 via CiteDrive, no volume data there); Nilsson TN 323, April 1984, edited (F2); ISO 8373:2021 robot definition "programmed actuated mechanism with a degree of autonomy to perform locomotion, manipulation or positioning" (IFR standardisation page), supporting the paraphrase in entry 1 line 30; ISO 8373 earlier definition "actuated mechanism programmable in two or more axes with a degree of autonomy" (AKIT glossary, edition not stated), consistent with the 2012 paraphrase.
- Not verified:
  - Gat, "On Three-Layer Architectures": page numbers (no catalogue reached); the text gives none, so nothing to correct.
  - Brooks journal name: Xplore did not render; some catalogues use "IEEE Journal on Robotics and Automation", the sources reached use "of". Left as is.
  - Kalman issue number (no. 1 commonly cited; the UNC page gives only "Series D"); not in the text.
  - Craig 3rd ed. (2005), Lynch and Park (2017), Siciliano et al. (2009), Bar-Shalom et al. (2001), Thrun et al. (2005), Pieper thesis (1968): standard textbooks and thesis, details not re-fetched this pass (wave-1 audit accepted them).
  - Shakey "built at the Stanford Research Institute from the late 1960s": consistent with the Technical Note's date range, not checked against a dated source this pass.

## Resolution

- T1 (Should fix): fixed - Exercise 3 answer now reads "about two standard deviations of the innovation ($\sqrt{4.24} = 2.06$, with $\sqrt{S} = 0.58$ m) from the predicted measurement", `src/content/blog/sensing-and-state-estimation.mdx:250`.
- F1 (Should fix): fixed - "developed by Julier and Uhlmann in the mid-1990s (their 1997 paper cited below is the usual reference)", `src/content/blog/sensing-and-state-estimation.mdx:184`; no reference added.
- F2 (Should fix): fixed - "N. J. Nilsson, Ed., *Shakey the Robot*, Technical Note 323, Artificial Intelligence Center, SRI International, 1984.", `src/content/blog/what-is-a-robot.mdx:245`.
- Optional applied: T2 (Exercise 1 question reworded, `sensing-and-state-estimation.mdx:227`), S1 (link target changed to `/series/foundations-of-control-systems`, `what-is-a-robot.mdx:18`), S2 ("outward", `planar-arm-kinematics.mdx:168`). Optional not applied: none.

Resolved by the wave-1 author on 2026-10-14; awaiting the reviewer's resolution check.
