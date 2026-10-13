# Series review: Introduction to Robotics

- Series: `introduction-to-robotics` (4 articles, status published, 0 planned entries)
- Reviewed commit: working tree on top of 369dd60 (entry 4, its figure and the completed series file not yet committed)
- Date: 2026-10-13
- Trigger: the series-complete hook, after the series file was edited to `status: "published"` with no planned entries.

## Summary

The series is technically sound and well ordered. It moves from what a robot is, to geometry, to kinematics, to estimation, with every cross-reference resolving and every worked number recomputing exactly. All five objectives are met. There are no blocking findings.

The main weaknesses are in the new review dimensions:
- The series states its prerequisites as "basic linear algebra and trigonometry", but entry 1 relies on mechanics (torque, inertia, backlash), entries 3 and 4 on calculus, and entry 4 on statistics terms (Mahalanobis distance, chi-square) that are named but never introduced.
- Quaternions and `atan2` are used before they are explained.
- Two references omit the edition or variant they mean: the ISO 8373 definition, and the Denavit–Hartenberg convention, which exists in two incompatible forms.

The series is ready as published once the seven should-fix items are corrected. The three optional items are polish.

Findings: 0 blocking, 7 should fix, 3 optional.

## Resolution

All 10 findings (F1–F10) were applied as recommended on 2026-10-13. Afterwards:
- `SITE_URL=https://acrr.asia npm run build` reported 0 errors and 0 warnings, and `npm run check:links` found every internal link resolved;
- the four articles showed no text glued to inline elements and no KaTeX errors.

Line numbers below refer to the reviewed state, not to the corrected articles.

## Objectives coverage

| Objective (from the series file) | Covered by | Assessment |
|---|---|---|
| Describe a robot as mechanical structure, actuators, sensors, and computation connected by a control loop. | Entry 1 §2–4 | Met. |
| Represent the position and orientation of rigid bodies using coordinate frames and rotation matrices. | Entry 2 (whole) | Met. Quaternions, one of the representations offered, are not introduced (F4). |
| Explain forward and inverse kinematics for a simple planar arm. | Entry 3 §2–6 | Met. |
| Outline the sense, plan, and act structure used in many robot software architectures. | Entry 1 §5 | Met. |
| Explain why a robot must estimate its state, and how a Kalman filter combines a motion model with noisy measurements. | Entry 4 §1–5 | Met. |

## Findings

| ID | Severity | Article | Location | Dimension | Finding |
|---|---|---|---|---|---|
| F1 | Should fix | `src/content/series/introduction-to-robotics.md` | Body (line 15) | Concept introduction / Completeness | The stated prerequisites omit the calculus and basic mechanics the series relies on |
| F2 | Should fix | `src/content/blog/what-is-a-robot.mdx` | §2.3 (lines 101–109), §2.4 (line 124) | Concept introduction | Torque, (moment of) inertia and backlash are used without being introduced |
| F3 | Should fix | `src/content/blog/what-is-a-robot.mdx` | §1.1 (line 30), references (line 212) | Stated versions and defaults | ISO 8373 is quoted without an edition, and its definition differs between editions |
| F4 | Should fix | `src/content/blog/coordinate-frames-and-transformations.mdx` | §3.3 (lines 124–130) | Concept introduction | Quaternions and "quaternion multiplication" are used without saying what a quaternion is |
| F5 | Should fix | `coordinate-frames-and-transformations.mdx`, `planar-arm-kinematics.mdx` | Entry 2 line 245; entry 3 lines 104–109 | Concept introduction / Logical flow | `atan2` is used in entry 2 and only explained in entry 3, after its first use there too |
| F6 | Should fix | `src/content/blog/planar-arm-kinematics.mdx` | §2.3 (line 77) | Stated versions and defaults | "The Denavit–Hartenberg convention" has two variants in common use that attach frames differently |
| F7 | Should fix | `src/content/blog/sensing-and-state-estimation.mdx` | §7.1 (line 206), §8 (line 219) | Concept introduction | Mahalanobis distance, the chi-square distribution and high-/low-pass weighting are named but not introduced |
| F8 | Optional | `src/content/blog/sensing-and-state-estimation.mdx` | §5.1 (line 145) vs references (line 249) | Terminology | "Rudolf Kálmán" in the text, "R. E. Kalman" in the references and "Kalman filter" throughout |
| F9 | Optional | `src/content/blog/sensing-and-state-estimation.mdx` | §2 (line 56) | Writing quality | "becomes correlatedly unsure" is awkward |
| F10 | Optional | `src/content/blog/sensing-and-state-estimation.mdx` | §7.2 (line 210) | Concept introduction | "occupancy grid" is not explained |

### F1. The stated prerequisites are incomplete
- **Where:** `src/content/series/introduction-to-robotics.md:15`, series introduction
- **Text:** "This series is intended for readers who are comfortable with basic linear algebra and trigonometry."
- **Problem:** The series also relies on:
  - **calculus:** differentiation with respect to time and partial derivatives (entry 3 §5.1, "Differentiating the forward kinematics with respect to time"; entry 4 §6.1, Jacobians $\partial f/\partial \mathbf x$) and integrals (entry 4 line 53, "the density integrates to 1");
  - **basic mechanics:** torque and inertia (entry 1 §2.3).

  Probability is also needed, but entry 4 introduces it. A reader who arrives with only the stated background will meet these without warning.
- **Recommended correction:** "This series is intended for readers who are comfortable with basic linear algebra, trigonometry and calculus (derivatives), and who have met torque and inertia in introductory mechanics. The probability it needs is introduced where it is used."

### F2. Torque, inertia and backlash are not introduced
- **Where:** `src/content/blog/what-is-a-robot.mdx:101-109` (§2.3 "Actuation") and `:124` (§2.4 "Sensing")
- **Text:** "Actuators turn commands into forces and torques."; "A motor rotor of inertia $J_m$ is felt at the joint as an inertia of $N^2 J_m$"; "Backlash and elasticity in the gearbox sit between the encoder and the link"
- **Problem:** The transmission argument (torque multiplied by $N$, reflected inertia $N^2 J_m$) is the technical core of §2.3, yet neither quantity is said to be what it is. Backlash recurs in §6 ("friction, flexibility, backlash") without a definition.
- **Recommended correction:**
  - Line 101: "Actuators turn commands into forces and **torques** (a torque is the rotational counterpart of a force: the turning effect of a force applied at a distance from an axis, in newton-metres)."
  - Line 109, first sentence: "The transmission also changes how the motor's own **inertia** (its moment of inertia: the resistance of a rotating body to changes in its rotation rate) appears at the joint."
  - Line 124: "**Backlash** (the small free play between meshing gear teeth) and elasticity in the gearbox sit between the encoder and the link…".

### F3. ISO 8373 is quoted without an edition
- **Where:** `src/content/blog/what-is-a-robot.mdx:30` and `:212`
- **Text:** "The international vocabulary standard for robotics, ISO 8373, captures the same idea in its own terms: a programmed, actuated mechanism with a degree of autonomy that moves within its environment to perform tasks."; "ISO 8373, *Robotics — Vocabulary*, International Organization for Standardization."
- **Problem:** ISO 8373 has been revised, and its definition of "robot" changed between editions. The 2012 edition speaks of a mechanism "programmable in two or more axes" that moves "within its environment"; the 2021 edition speaks of performing "locomotion, manipulation or positioning". The paraphrase combines elements of both and names no edition.
- **Recommended correction:** "The international vocabulary standard for robotics, ISO 8373, captures the same idea in its own terms. Its 2012 edition describes an actuated mechanism, programmable in two or more axes, with a degree of autonomy, that moves within its environment to perform intended tasks; the 2021 revision rephrases it around locomotion, manipulation and positioning." Reference: "ISO 8373, *Robotics — Vocabulary*, International Organization for Standardization (2012; revised 2021)."

### F4. Quaternions are not introduced
- **Where:** `src/content/blog/coordinate-frames-and-transformations.mdx:124-130`, section "3.3 Four representations of orientation"
- **Text:** "**Unit quaternions.** The same rotation is encoded as the four numbers … Quaternions compose by quaternion multiplication, need only a cheap renormalisation to stay valid…"
- **Problem:** The paragraph explains how a rotation is encoded as four numbers but never says what a quaternion is, or what "quaternion multiplication" means. Entry 4 relies on quaternions again (orientation estimation), and entry 2's own mistakes table depends on component order.
- **Recommended correction:** Insert before "The same rotation is encoded…": "A **quaternion** is a four-component number $q = w + x\,i + y\,j + z\,k$, introduced by William Rowan Hamilton in 1843 as an extension of the complex numbers, with $i^2 = j^2 = k^2 = ijk = -1$; quaternions are multiplied like polynomials using those rules, and the product does not commute, just as rotations do not. Written as $(w, x, y, z)$, a unit quaternion (one of length 1) encodes a rotation:".

### F5. `atan2` is used before it is explained
- **Where:** `src/content/blog/coordinate-frames-and-transformations.mdx:245` (first use); `src/content/blog/planar-arm-kinematics.mdx:104` (used) and `:109` (explained)
- **Text:** "for example with $\operatorname{atan2}(\sin\Delta, \cos\Delta)$"; "Using the two-argument arctangent, rather than $\arccos c_2$, returns the angle in the correct quadrant"
- **Problem:** `atan2` first appears in entry 2's table of mistakes, with no explanation. Entry 3 uses it in a formula and explains it five lines later.
- **Recommended correction:**
  - In entry 2, line 245, write "for example with $\operatorname{atan2}(\sin\Delta, \cos\Delta)$, the two-argument arctangent, which returns the angle of the point $(\cos\Delta, \sin\Delta)$ in the full range $(-180^\circ, 180^\circ]$".
  - In entry 3, move the sentence at line 109 before the formula at line 103: "The angle is recovered with the two-argument arctangent $\operatorname{atan2}(s, c)$ (introduced in the previous entry), which, unlike $\arccos c_2$, returns the angle in the correct quadrant and stays accurate when $c_2$ is close to $\pm 1$:".

### F6. The Denavit–Hartenberg convention has two variants
- **Where:** `src/content/blog/planar-arm-kinematics.mdx:77`, section "2.3 More joints, and the general method"
- **Text:** "The best known is the **Denavit–Hartenberg** convention (1955), which describes each link with four parameters."
- **Problem:** Two Denavit–Hartenberg conventions are in common use: the original (sometimes called "standard") and the modified form popularised by Craig's textbook. They attach each link's frame at a different joint, so parameter tables written for one are wrong in the other. A reader taking parameters from two sources will meet both.
- **Recommended correction:** "The best known is the **Denavit–Hartenberg** convention (1955), which describes each link with four parameters. It is used in two variants, the original and the 'modified' form popularised by Craig's textbook, which attach the link frames at different joints, so a parameter table must always say which it follows."

### F7. Statistical and signal-processing terms are named but not introduced
- **Where:** `src/content/blog/sensing-and-state-estimation.mdx:219` (§8 "Outliers") and `:206` (§7.1)
- **Text:** "the squared Mahalanobis distance $d^2 = \nu^{\mathsf T} S^{-1} \nu$ follows a chi-square distribution when the models are right"; "a simpler **complementary filter** does it with fixed high-pass and low-pass weighting"
- **Problem:** §2 introduces the probability the entry needs, carefully. These three terms are then used without that care: the reader is given a formula and a threshold (6.63) without knowing what the distance measures or why that number.
- **Recommended correction:**
  - Line 219: "…the squared **Mahalanobis distance** $d^2 = \nu^{\mathsf T} S^{-1} \nu$, which measures the innovation in units of its own expected spread, is distributed as **chi-square** (the distribution of a sum of squared standard Gaussian variables, one per measurement dimension) when the models are right, so implausibly large values can be detected with a fixed threshold."
  - Line 206: "…a simpler **complementary filter** does it with fixed weights: it keeps the gyroscope's contribution to fast changes and the accelerometer's to slow ones (high-pass and low-pass filtering respectively)."

### F8. Kálmán and Kalman
- **Where:** `src/content/blog/sensing-and-state-estimation.mdx:145` and `:249`
- **Text:** "Rudolf Kálmán published the general version of this calculation in 1960."; "R. E. Kalman, …"
- **Problem:** The text uses the Hungarian spelling, while the reference and the filter's name use the spelling under which he published. Readers may wonder whether these are the same person.
- **Recommended correction:** "Rudolf E. Kálmán (who published as R. E. Kalman) gave the general version of this calculation in 1960."

### F9. "Correlatedly unsure"
- **Where:** `src/content/blog/sensing-and-state-estimation.mdx:56`
- **Text:** "A robot that is unsure of its heading, for example, becomes correlatedly unsure of its sideways position as it drives."
- **Problem:** Awkward, and the point (the covariance couples the two errors) is obscured.
- **Recommended correction:** "A robot that is unsure of its heading, for example, becomes unsure of its sideways position as it drives, and the two errors are linked: if the heading is off to the left, the position is too."

### F10. "Occupancy grid" is not explained
- **Where:** `src/content/blog/sensing-and-state-estimation.mdx:210`
- **Text:** "(landmark positions, or an occupancy grid)"
- **Problem:** A term of art, used once, without explanation.
- **Recommended correction:** "(landmark positions, or an occupancy grid: a grid of cells over the floor plan, each holding the probability that it is occupied)".

## Concept introduction map

| Concept | First used (path:line) | Introduced where | Assessment |
|---|---|---|---|
| Feedback, closed loop | `what-is-a-robot.mdx:32` | Same place, with a link to the control series' introduction | Introduced |
| Degree of freedom, mobility | `what-is-a-robot.mdx:79` | `what-is-a-robot.mdx:79-91` | Introduced |
| Torque, moment of inertia | `what-is-a-robot.mdx:101` | Not introduced | F2 |
| Backlash | `what-is-a-robot.mdx:124` | Not introduced | F2 |
| Encoder, IMU, lidar | `what-is-a-robot.mdx:115-116` | Same place | Introduced |
| Matrix, vector, determinant, transpose | `coordinate-frames-and-transformations.mdx:40` | Prerequisite (linear algebra) | Acceptable |
| Rotation matrix, SO(3), SE(3) | `coordinate-frames-and-transformations.mdx:40` | `coordinate-frames-and-transformations.mdx:59-79, 156` | Introduced |
| Quaternion | `coordinate-frames-and-transformations.mdx:110` | Not introduced (only its encoding of a rotation) | F4 |
| `atan2` | `coordinate-frames-and-transformations.mdx:245` | `planar-arm-kinematics.mdx:109` | Used early; F5 |
| Derivative, partial derivative, integral | `planar-arm-kinematics.mdx:141` | Not in the stated prerequisites | F1 |
| Jacobian, singular configuration, null space | `planar-arm-kinematics.mdx:144` | Same section | Introduced |
| Newton's method, damped least squares | `planar-arm-kinematics.mdx:186` | Same section | Introduced |
| State | `sensing-and-state-estimation.mdx:27` | Same place, with a link to the state-space primer | Introduced |
| Random variable, density, mean, variance, covariance, Gaussian | `sensing-and-state-estimation.mdx:52` | `sensing-and-state-estimation.mdx:52-63` | Introduced |
| Bayes' rule, Bayes filter | `sensing-and-state-estimation.mdx:105` | Same place | Introduced |
| Mahalanobis distance, chi-square distribution | `sensing-and-state-estimation.mdx:219` | Not introduced | F7 |
| High-pass / low-pass filtering | `sensing-and-state-estimation.mdx:206` | Not introduced | F7 |
| Occupancy grid | `sensing-and-state-estimation.mdx:210` | Not introduced | F10 (optional) |

## Versions, defaults and conventions

| Assumption | Where it appears | Stated in the text? | Assessment |
|---|---|---|---|
| ISO 8373 edition | Entry 1 line 30 | No | F3 |
| Right-handed frames | Entry 2 line 23 | Yes | Good |
| Positive angle direction (counter-clockwise) | Entry 2 line 59 | Yes | Good |
| Euler angle convention (ZYX, intrinsic) | Entry 2 line 112 | Yes | Good |
| Quaternion component order | Entry 2 lines 127–130, 244 | Implied by the formula (scalar first); both library orders named in §8 | Good; F4 makes it explicit |
| Angle units | Entries 2 and 3 examples in degrees; entry 2 §8 advises radians internally; entry 4 line 34 radians | Yes | Good |
| Length units | Entry 2 line 176, entry 3 line 71, entry 4 line 34 | Yes (metres) | Good |
| Camera optical frame vs body frame | Entry 2 line 247 | Yes | Good |
| Relative (not absolute) joint angles | Entry 3 line 43 | Yes | Good |
| Denavit–Hartenberg variant | Entry 3 line 77 | No | F6 |
| Kalman filter assumptions (linear, Gaussian, known $Q$, $R$) | Entry 4 §5.2 | Yes | Good |
| Loop rates | Entry 1 §4 | Yes, labelled as typical orders of magnitude | Good |

## Series-level notes

**Cross-references.** All inter-entry references were checked and resolve:
- entry 1 → the control series' introduction (link) and "the last entry" (estimation);
- entry 2 → entry 1 (rigid-body freedoms) and entries 3 and 4 ("next" and "last");
- entry 3 → entry 1 (degrees of freedom, redundancy) and entry 2 (transforms, angle wrapping, gimbal lock);
- entry 4 → entries 1, 2 and 3, and the control series' state-space primer (link).

Every "next entry" sentence names the actual next article, and entry 4 closes the series with an overview of all four entries.

**Terminology.** Terms are consistent across entries:
- pose; frame and frame tree;
- joint space and task space;
- redundant, underactuated and nonholonomic (defined in entry 1, reused in entry 3);
- Jacobian (defined in entry 3, reused in entry 4).

Spelling is British throughout (organised, linearising, initialisation), except "localization", which entry 4 uses consistently as the established technical term (as in SLAM), in the same way the identity series keeps "authorization".

**Structure and tone.** Consistent: numbered sections, worked examples carried through each entry, a summary table, and references at the end. Entries 3 and 4 each have a generated figure computed from their own formulas, as the project requires.

**Frontmatter.** Category, `series` and `seriesOrder` (1–4, contiguous) are consistent. Tags reuse the existing `control-theory` and `linear algebra` where relevant.

**Content rules.**
- No fabricated figures; all numbers are worked examples and are labelled as such.
- Loop rates are labelled as typical orders of magnitude.
- English only.
- No external links; references are cited by author, title and year.

## Verification log

- `npm run build:local`: passed. `astro check` reported 0 errors and 0 warnings, the build completed, and Pagefind indexed 27 pages. The expected localhost warning appeared because `SITE_URL` was not set.
- `npm run check:links`: passed. It checked 79 pages and 1867 internal references; all resolve.
- Mermaid widths in `dist/blog/*.html`, all under 600px: entry 1: 257, 313px; entry 2: 215px; entry 3: none (its figure is generated SVG); entry 4: 309px.
- Text glued to inline elements, and KaTeX errors: none in the four pages.
- Generated figures (`PlanarArmIK`, `GaussianFusion`) were screenshotted in light and dark mode. The pages have no horizontal overflow at 360px.
- Recomputed:
  - entry 1:
    - encoder resolution $360°/(4096 \times 100) = 0.00088°$;
    - Grübler–Kutzbach mobility of a 6R serial arm = 6.
  - entry 2:
    - $R_x(90°)R_z(90°)$ and $R_z(90°)R_x(90°)$ as printed;
    - the gimbal-lock example gives equal matrices;
    - the lidar point $(2, 4)$, the inverse transform, and the camera chain result $(1.8, 2.5)$.
  - entry 3:
    - forward kinematics $(1.047, 1.176)$ and $\det J = 0.495$;
    - the second inverse solution $(66.6°, -45°)$;
    - the Newton and damped-least-squares figures, recomputed when the entry was written.
  - entry 4:
    - $K = 0.735$, $\hat x = 10.44$ m, $P = 0.066$ m², $\sigma = 0.26$ m;
    - the prediction $P^- = 0.106$ m², and $\sigma = 0.68$ m after ten moves;
    - $d^2 = 1.06$ and $11.8$, and the chi-square 99% bound for one degree of freedom $= 6.635$.
- Not verified:
  - The ISO 8373 wording in each edition (F3), and that the modified Denavit–Hartenberg convention is the one popularised by Craig's textbook (F6). These were checked against the reviewer's knowledge, not re-read from the sources in this run.
  - The publication details of the cited books and papers were likewise not re-checked against the originals.
