# Series review: Introduction to Robotics

- Series: `introduction-to-robotics` (4 articles, status published, 0 planned entries)
- Reviewed commit: a429fd8 (the four articles and the series file have no uncommitted changes)
- Date: 2026-10-13
- Previous review: first review (10 findings) applied in 1c95247; this is the second review.

## Summary

All ten corrections from the first review are in the text: the series prerequisites, torque, inertia and backlash, the ISO 8373 edition, quaternions, `atan2`, the two Denavit–Hartenberg variants, the statistics terms, the Kálmán spelling, the covariance sentence and the occupancy grid. Every worked number in the four entries was recomputed and is correct. The build, the type check and the link check pass.

This stricter second pass found four should-fix problems, mostly about conventions:
- Entry 1 says accelerometers measure the body's acceleration, while entry 4 relies on an accelerometer at rest measuring gravity.
- Entry 2 gives one body-frame axis convention as if it were the only one.
- Entry 3 never says that its Jacobian and Newton formulas need angles in radians, although its examples are in degrees.
- Entry 4 reuses the letters $A$ and $B$ for a discrete-time model, without saying so, right after linking to a primer where they mean the continuous-time matrices.

The four optional items are notation and wording. There are no blocking findings, and the series is ready as published once the should-fix items are corrected.

Findings: 0 blocking, 4 should fix, 4 optional.

## Objectives coverage

| Objective (from the series file) | Covered by | Assessment |
|---|---|---|
| Describe a robot as mechanical structure, actuators, sensors, and computation connected by a control loop. | Entry 1 §1–4 | Met. |
| Represent the position and orientation of rigid bodies using coordinate frames and rotation matrices. | Entry 2 (whole) | Met. Quaternions are now introduced (§3.3). |
| Explain forward and inverse kinematics for a simple planar arm. | Entry 3 §2–6 | Met. |
| Outline the sense, plan, and act structure used in many robot software architectures. | Entry 1 §5 | Met. |
| Explain why a robot must estimate its state, and how a Kalman filter combines a motion model with noisy measurements. | Entry 4 §1–5 | Met. The discrete-time convention of the model is not stated (F4). |

## Findings

| ID | Severity | Article | Location | Dimension | Finding |
|---|---|---|---|---|---|
| F1 | Should fix | `src/content/blog/what-is-a-robot.mdx` | §2.4 (line 115) | Technical accuracy / Factual consistency | Accelerometers are said to measure "the acceleration … of the body"; at rest they measure gravity, which entry 4 (line 204) relies on |
| F2 | Should fix | `src/content/blog/coordinate-frames-and-transformations.mdx` | §8 (line 247) | Stated versions and defaults | The body frame is given as "$x$ forward, $z$ up", although $x$ forward, $z$ down is equally common (aircraft, underwater vehicles) |
| F3 | Should fix | `src/content/blog/planar-arm-kinematics.mdx` | §5.1 (lines 139–156), §6.2–6.3 (lines 184–208) | Stated versions and defaults | The Jacobian and the Newton and damped least-squares steps require angles in radians, but this is never stated and every example is in degrees |
| F4 | Should fix | `src/content/blog/sensing-and-state-estimation.mdx` | §1.1 (line 27), §5.1 (lines 145–152) | Stated versions and defaults / Cross-article references | The Kalman model's $A$, $B$ (and $H$) are discrete-time, while the linked state-space primer defines $A$, $B$ (and $C$) for the continuous-time form |
| F5 | Optional | `src/content/blog/what-is-a-robot.mdx` | §2.2 (line 85), §2.3 (lines 103, 109) | Terminology | $N$ is the number of bodies and then the gear ratio; $J$ is the number of joints and then (as $J_m$) an inertia, a few paragraphs apart |
| F6 | Optional | `src/content/blog/coordinate-frames-and-transformations.mdx` | §5 (lines 176, 192) | Stated versions and defaults | The worked example treats the lidar reading as if the lidar sat at the robot frame's origin, without saying so |
| F7 | Optional | `src/content/blog/planar-arm-kinematics.mdx` | §2.3 (line 77) | Writing quality | "Both produce the same forward kinematics" now follows three formulations (two DH variants and product of exponentials) |
| F8 | Optional | `src/content/blog/sensing-and-state-estimation.mdx` | §3.3 (line 103), §4 (line 109) | Concept introduction | The notation $\hat x$ (estimate) and the superscript $-$ (prediction, before the measurement) is used without being explained |

### F1. What an accelerometer measures
- **Where:** `src/content/blog/what-is-a-robot.mdx:115`, section "2.4 Sensing"
- **Text:** "**inertial measurement units** (accelerometers and gyroscopes) measure the acceleration and rotation rate of the body"
- **Problem:** An accelerometer measures specific force: the body's acceleration minus the acceleration due to gravity. At rest it reads 1 g upwards, although the body's acceleration is zero. Entry 4 depends on exactly that: "the **accelerometer**, at rest, measures the direction of gravity, which gives an absolute but noisy and motion-disturbed reference for tilt" (`src/content/blog/sensing-and-state-estimation.mdx:204`). As written, entry 1 contradicts entry 4: a reader who takes "measure the acceleration" literally would expect a reading of zero at rest.
- **Recommended correction:** "**inertial measurement units** measure the motion of the body: gyroscopes its rotation rate, and accelerometers its acceleration combined with gravity (an accelerometer at rest reads the pull of gravity, which is what later lets it serve as a tilt reference)".

### F2. One body-frame convention presented as the only one
- **Where:** `src/content/blog/coordinate-frames-and-transformations.mdx:247`, section "8. Common Mistakes"
- **Text:** "A camera's optical frame (often $z$ forward, $x$ right, $y$ down) treated as a body frame ($x$ forward, $z$ up)"
- **Problem:** The camera convention is qualified with "often", but the body frame is not qualified at all. Ground robots commonly use $x$ forward, $y$ left, $z$ up. Aircraft, many drones and underwater vehicles, which entry 1 uses as examples (lines 16, 40), commonly use $x$ forward, $y$ right, $z$ down, with a world frame of north, east, down. Both are right-handed. Mixing these two body conventions is itself one of the mistakes this table is meant to prevent.
- **Recommended correction:** "A camera's optical frame (often $z$ forward, $x$ right, $y$ down) treated as a body frame (for ground robots usually $x$ forward, $y$ left, $z$ up; for aircraft and many drones $x$ forward, $y$ right, $z$ down)".

### F3. Radians are required but not stated
- **Where:** `src/content/blog/planar-arm-kinematics.mdx:139-156` (§5.1), `:184-194` (§6.2), `:208` (§6.3)
- **Text:** "$J(\mathbf q) = \frac{\partial f}{\partial \mathbf q}$"; "starting from $\mathbf q_0 = (0^\circ, 90^\circ)$ … converging to $(30^\circ, 45^\circ)$"; "The first Newton step asks for joint changes of about $167^\circ$ and $-402^\circ$."
- **Problem:** The Jacobian entries, such as $-l_1\sin\theta_1 - l_2\sin(\theta_1+\theta_2)$, are derivatives with respect to angles in radians, in metres per radian. So $\Delta\mathbf q = J^{-1}\mathbf e$ comes out in radians. A reader who follows the examples and works in degrees gets steps 57.3 times too large. The entry states its length unit ("Lengths are in metres", line 71) but not its angle unit. Recomputed with angles in radians, the printed numbers are correct: the step is $(166.6^\circ, -401.6^\circ)$ after conversion, and the damped step is $(1.80^\circ, -1.33^\circ)$. Entry 2 (line 243) and entry 4 (line 34) both state their angle convention.
- **Recommended correction:** After "Lengths are in metres." (line 71), add: "Angles are shown in degrees for readability, but every formula that differentiates with respect to an angle (the Jacobian of Section 5 and the iterations of Section 6) assumes radians, so convert before computing, as the previous entry recommends."

### F4. Discrete-time $A$ and $B$ after a link to the continuous-time primer
- **Where:** `src/content/blog/sensing-and-state-estimation.mdx:27` and `:145-152`, sections "1.1 State" and "5.1 The equations"
- **Text:** "The [primer on state-space models](/blog/state-space-models-primer) in the control systems series introduced the idea"; "$\mathbf x_k = A\,\mathbf x_{k-1} + B\,\mathbf u_k + \mathbf w_k, \qquad \mathbf z_k = H\,\mathbf x_k + \mathbf v_k$"
- **Problem:** The linked primer defines the model in continuous time, "$\dot{x} = Ax + Bu, \qquad y = Cx + Du$" (`src/content/blog/state-space-models-primer.mdx:45`). There, $A$ is the matrix of "how the state evolves on its own" per unit time. Entry 4 uses the same letters for a discrete-time step model, in which $A$ maps one sample to the next (for a linear time-invariant system sampled every $\Delta t$, $A_{\text{d}} = e^{A\Delta t}$), and it names the output matrix $H$ instead of $C$. The entry never says "discrete-time"; the closest it comes is "from one time step to the next" (line 71). A reader coming from the primer can take the primer's $A$ for the Kalman filter's and get a wrong filter. For example, the primer's mass–spring–damper $A$ has a zero diagonal entry, while the discrete transition matrix of a stationary system is close to the identity.
- **Recommended correction:** After the model equations (line 150), add: "These are **discrete-time** models, written for the instants $k = 0, 1, 2, \dots$ at which the filter runs. The matrix $A$ maps the state at one step to the next, so it is not the $A$ of the continuous-time form $\dot{\mathbf x} = A\mathbf x + B\mathbf u$ in the state-space primer: for a linear time-invariant system sampled every $\Delta t$ seconds, the discrete matrix is $e^{A\Delta t}$. The measurement matrix $H$ plays the role of the primer's output matrix $C$."

### F5. $N$ and $J$ each used for two quantities in entry 1
- **Where:** `src/content/blog/what-is-a-robot.mdx:85`, `:103`, `:109`
- **Text:** "For a spatial mechanism with $N$ bodies including the fixed ground and $J$ joints"; "A reduction of ratio $N$ trades speed for torque."; "A motor rotor of inertia $J_m$"
- **Problem:** Within 25 lines, $N$ changes from a count of bodies to a gear ratio, and $J$ from a count of joints to an inertia. Entry 3 then uses $J$ for the Jacobian. Each use is conventional on its own, but the clash is avoidable in the article that sets the series' vocabulary.
- **Recommended correction:** In §2.2, write the mobility formula with $n_b$ bodies and $n_j$ joints: "$M = 6\,(n_b - 1 - n_j) + \sum_{i=1}^{n_j} f_i$". Update the check that follows it to "$n_b = n + 1$ bodies and $n_j = n$ joints". Keep $N$ for the gear ratio and $J_m$ for the motor inertia.

### F6. The lidar is assumed to sit at the robot frame's origin
- **Where:** `src/content/blog/coordinate-frames-and-transformations.mdx:176` and `:192`, section "5. A Worked Example in the Plane"
- **Text:** "Its lidar reports an obstacle at ${}^{R}\mathbf{p} = (3, 0)$: 3 metres straight ahead *of the robot*."; "which recovers the lidar's measurement, as it must."
- **Problem:** The entry's introduction says a lidar reports an obstacle "3 metres ahead *of the lidar*" (line 17). Section 7.1 gives the lidar its own frame in the tree (line 226), and entry 4 stresses that "A lidar range is predicted from the sensor's pose, not the robot base's" (`sensing-and-state-estimation.mdx:216`). The example quietly makes the lidar frame and the robot frame the same. That assumption is reasonable, but the example should say so, especially since the camera in the same section is given an explicit offset.
- **Recommended correction:** "Its lidar, mounted at the origin of the robot frame and facing forward (so that the lidar frame and the robot frame coincide), reports an obstacle at ${}^{R}\mathbf{p} = (3, 0)$: 3 metres straight ahead of the robot."

### F7. "Both" after three formulations
- **Where:** `src/content/blog/planar-arm-kinematics.mdx:77`, section "2.3 More joints, and the general method"
- **Text:** "It is used in two variants, the original and the "modified" form … A more recent alternative, the **product of exponentials** formulation, describes each joint by its axis in a single reference frame. Both produce the same forward kinematics; they differ in bookkeeping."
- **Problem:** The sentence that the first review added introduces two Denavit–Hartenberg variants, so "Both" can now be read as referring to them rather than to DH and the product of exponentials.
- **Recommended correction:** "All of these produce the same forward kinematics; they differ in bookkeeping."

### F8. The notation $\hat x$ and $\hat x^-$ is not explained
- **Where:** `src/content/blog/sensing-and-state-estimation.mdx:103` (first use) and `:109`
- **Text:** "The difference between the actual and the predicted measurement, $z_k - h(\hat x_k^-)$, is the **innovation**"; "with mean $\hat x^- = 10.0$ m and variance $P^- = 0.25\ \text{m}^2$"
- **Problem:** The hat (an estimate, as opposed to the true state $x_k$ in §3.1) and the superscript minus (the prediction, before the measurement is used) appear for the first time inside a formula, and neither is explained anywhere. The reader has to infer them from the example and from the predict/update equations in §5.1.
- **Recommended correction:** Before "The difference between …" at line 103, add: "Write $\hat x_k^-$ and $P_k^-$ for the mean and covariance of the predicted belief (the minus sign marks 'before the measurement'), and $\hat x_k$ and $P_k$ for those of the updated belief; the hat distinguishes an estimate from the true state $x_k$."

## Concept introduction map

| Concept | First used (path:line) | Introduced where | Assessment |
|---|---|---|---|
| Feedback, closed loop | `what-is-a-robot.mdx:32` | Same place, with a link to the control series' introduction | Introduced |
| Degree of freedom, mobility | `what-is-a-robot.mdx:79` | `what-is-a-robot.mdx:79-91` | Introduced |
| Torque, moment of inertia | `what-is-a-robot.mdx:101`, `:109` | Same places (first-review F2), and in the series prerequisites | Introduced |
| Backlash | `what-is-a-robot.mdx:124` | Same place | Introduced |
| Encoder, IMU, lidar | `what-is-a-robot.mdx:115-116` | Same place | Introduced; what an accelerometer measures is imprecise (F1) |
| Matrix, vector, determinant, transpose | `coordinate-frames-and-transformations.mdx:40` | Prerequisite (linear algebra) | Acceptable |
| Rotation matrix, SO(3), SE(3) | `coordinate-frames-and-transformations.mdx:40` | `coordinate-frames-and-transformations.mdx:59-79`, `:156` | Introduced |
| Quaternion | `coordinate-frames-and-transformations.mdx:110` (summary table) | `coordinate-frames-and-transformations.mdx:124` | Introduced in the paragraph that follows the table; acceptable |
| `atan2` | `coordinate-frames-and-transformations.mdx:245` | Same place | Introduced |
| Spherical linear interpolation | `coordinate-frames-and-transformations.mdx:235` | Named only | Acceptable: the context explains its purpose |
| Derivative, partial derivative | `planar-arm-kinematics.mdx:139-144` | Series prerequisites (calculus) | Acceptable |
| Jacobian, singular configuration, null space | `planar-arm-kinematics.mdx:147`, `:166`, `:214` | Same places | Introduced |
| Denavit–Hartenberg, product of exponentials | `planar-arm-kinematics.mdx:77` | Same place, by role | Acceptable for an outlook paragraph |
| Newton's method, damped least squares | `planar-arm-kinematics.mdx:184`, `:200` | Same sections | Introduced |
| State | `sensing-and-state-estimation.mdx:27` | Same place, with a link to the state-space primer | Introduced |
| Random variable, density, mean, variance, covariance, Gaussian | `sensing-and-state-estimation.mdx:52` | `sensing-and-state-estimation.mdx:52-63` | Introduced |
| Innovation | `sensing-and-state-estimation.mdx:103` | Same place | Introduced; its notation is not (F8) |
| Estimate $\hat x$, predicted $\hat x^-$, $P^-$ | `sensing-and-state-estimation.mdx:103` | Not explained | F8 |
| Bayes' rule, Bayes filter | `sensing-and-state-estimation.mdx:105` | Same place | Introduced |
| Discrete-time linear model ($A$, $B$, $H$) | `sensing-and-state-estimation.mdx:148-149` | Not distinguished from the primer's continuous-time model | F4 |
| Sigma points, particles, resampling | `sensing-and-state-estimation.mdx:182`, `:186` | Same places | Introduced |
| Complementary filter, high-/low-pass | `sensing-and-state-estimation.mdx:206` | Same place | Introduced |
| Occupancy grid, loop closure | `sensing-and-state-estimation.mdx:210` | Same place | Introduced |
| Mahalanobis distance, chi-square | `sensing-and-state-estimation.mdx:219` | Same place | Introduced |

## Versions, defaults and conventions

| Assumption | Where it appears | Stated in the text? | Assessment |
|---|---|---|---|
| ISO 8373 edition | Entry 1 line 30, reference line 212 | Yes (2012, revised 2021) | Good |
| Right-handed frames | Entry 2 line 23 | Yes | Good |
| Positive angle direction (counter-clockwise) | Entry 2 line 59 | Yes | Good |
| Euler-angle convention (ZYX, intrinsic) | Entry 2 lines 112, 211 | Yes | Good |
| Quaternion component order and multiplication rule | Entry 2 lines 124, 244 | Yes: $(w, x, y, z)$ and Hamilton's $ijk = -1$; both storage orders named | Good |
| Body-frame axis convention | Entry 2 line 247 | Only one convention given | F2 |
| Camera optical-frame convention | Entry 2 line 247 | Yes ("often") | Good |
| Lidar mounting in the worked example | Entry 2 line 176 | No | F6 (optional) |
| Angle units | Entry 2: examples in degrees, radians advised internally (line 243); entry 3: degrees only, no statement; entry 4: radians (line 34) | Entries 2 and 4 yes, entry 3 no | F3 |
| `atan2` argument order and range | Entry 2 line 245 ($(y, x)$ order implied by "the angle of the point $(\cos\Delta, \sin\Delta)$"; range $(-180^\circ, 180^\circ]$); entry 4 line 218 ($(-\pi, \pi]$) | Yes | Consistent |
| Length units | Entry 2 line 176, entry 3 line 71, entry 4 line 34 | Yes (metres) | Good |
| Relative (not absolute) joint angles | Entry 3 line 43 | Yes | Good |
| Denavit–Hartenberg variant | Entry 3 line 77 | Yes (original and modified) | Good |
| Discrete-time vs continuous-time model | Entry 4 lines 71–74, 148–149 | No | F4 |
| Kalman filter assumptions (linear, Gaussian, known $Q$, $R$) | Entry 4 §5.2 | Yes | Good |
| Loop rates | Entry 1 §4 | Yes, labelled as typical orders of magnitude | Good |

## Series-level notes

**Fixes from the first review.** Each was checked against the current text:
- F1: series file line 16.
- F2: entry 1 lines 101, 109 and 124.
- F3: entry 1 lines 30 and 212.
- F4: entry 2 line 124.
- F5: entry 2 line 245, and entry 3 line 101 (now before the formula).
- F6: entry 3 line 77.
- F7: entry 4 lines 206 and 219.
- F8: entry 4 line 145.
- F9: entry 4 line 56.
- F10: entry 4 line 210.

All are present and technically correct. The one side effect is F7 of this review, an ambiguous "Both" left by the inserted DH sentence.

**Cross-references.** All were re-checked and resolve to sections that say what is claimed:
- entry 1 → the control series' introduction (seriesOrder 1 of `foundations-of-control-systems`), Section 4, and "the last entry";
- entry 2 → entry 1 (geometry, rigid-body freedoms), "the next entry" and "the last entry";
- entry 3 → entry 1 (degrees of freedom, redundancy) and entry 2 (transforms, `atan2`, angle wrapping, gimbal lock);
- entry 4 → entries 1, 2 and 3, and the control series' state-space primer (see F4 for the notation mismatch with that primer).

Every "next entry" sentence names the actual next article, and entry 4 §10 summarises all four entries accurately.

**Terminology.** Pose, frame tree, joint and task space, redundant, underactuated and nonholonomic, Jacobian, innovation and belief are each defined once and reused with the same meaning. Spelling is British throughout (organised, linearising, initialisation, manoeuvring). The exception is "localization", kept as the established technical term. Abbreviations (DOF, IMU, EKF, UKF, SLAM) are expanded on first use.

**Structure and tone.** Consistent: numbered sections, a worked example carried through each entry, a summary table and references. The generated figures of entries 3 and 4 use the articles' own values: `scripts/generate-diagrams.py` sections 8 and 9 compute them from $l_1 = 1.0$, $l_2 = 0.7$, the target at $(30^\circ, 45^\circ)$, and $P^- = 0.25$, $R = 0.09$. The captions agree: the elbow is below the base–target line, which is at $48.3^\circ$, for $\theta_1 = 30^\circ$, and above it for $66.6^\circ$.

**Content rules.** No fabricated figures, results or URLs. All numbers are worked examples or labelled as typical orders of magnitude. The references are real works with plausible details (Brooks 1986; Gat 1998; Nilsson 1984, SRI TN 323; Denavit and Hartenberg 1955; Pieper 1968; Kalman 1960; Julier and Uhlmann 1997; Thrun, Burgard and Fox 2005; Durrant-Whyte and Bailey 2006). The text is in English only, and nothing is presented as ACRR research.

## Verification log

- `npx astro check`: 0 errors, 0 warnings, 0 hints (60 files). `npm run build` and `npm run build:local` were not run, because another agent was building in the same working tree.
- `npx astro build --outDir /tmp/claude-0/-home-user-acrr/33f2b4d6-bdb7-522e-a1ea-9c38c4478b92/scratchpad/review-dist`: completed, 95 pages built. This build included uncommitted files of the concurrent Sensor Systems work, which did not affect it. Pagefind was not run on the scratch build.
- `node scripts/check-links.mjs /tmp/claude-0/-home-user-acrr/33f2b4d6-bdb7-522e-a1ea-9c38c4478b92/scratchpad/review-dist`: 95 pages and 2225 internal references checked; all resolve.
- Mermaid widths in the scratch build, all under 600px:
  - entry 1: 257px and 313px;
  - entry 2: 215px;
  - entry 3: none;
  - entry 4: 309px.
- KaTeX errors: none in the four pages. Text glued to `<strong>`, `<a>`, `<code>` or `<em>`: none.
- Recomputed with python3 (numpy):
  - entry 1:
    - $360^\circ/(4096 \times 100) = 0.000879^\circ$;
    - the serial-arm mobility check $M = n$.
  - entry 2:
    - $R_x(90^\circ)R_z(90^\circ)$ and $R_z(90^\circ)R_x(90^\circ)$ as printed, and their action on $\hat x$;
    - the gimbal-lock example: $(\psi, \phi) = (30^\circ, 10^\circ)$ and $(50^\circ, 30^\circ)$ give equal matrices at $\theta = 90^\circ$, and equal sums give equal matrices at $-90^\circ$;
    - Rodrigues' formula with $\hat{\mathbf u} = \hat z$ reproduces $R_z$;
    - the quarter-turn quaternion $(0.7071, 0, 0, 0.7071)$;
    - the obstacle at $(2, 4)$, the inverse ${}^{R}T_{W}$ and its result $(3, 0)$, and the camera chain result $(1.8, 2.5)$.
  - entry 3:
    - forward kinematics $(1.0472, 1.1761)$;
    - $c_2 = 0.7071$;
    - inverse solutions $(30^\circ, 45^\circ)$ and $(66.64^\circ, -45^\circ)$;
    - $\det J = 0.4950$, and $\det J$ simplifies symbolically to $l_1 l_2 \sin\theta_2$;
    - the Newton errors from $(0^\circ, 90^\circ)$: $0.478, 0.113, 0.0116, 1.8 \times 10^{-4}, 6.3 \times 10^{-8}$, converging to $(30^\circ, 45^\circ)$;
    - the first Newton step from $(0^\circ, 1^\circ)$ towards $(1.75, 0.05)$: $(166.6^\circ, -401.6^\circ)$;
    - the first damped step, with $\lambda = 0.1$: $(1.80^\circ, -1.33^\circ)$;
    - the damped iteration settles at radius $1.7000$, $0.0507$ from the target;
    - all of these with angles in radians internally (see F3).
  - entry 4:
    - $K = 0.7353$, $\hat x = 10.441$ m, $P = 0.0662$ m², $\sigma = 0.257$ m, and $P^-R/(P^-+R) = 0.0662$;
    - the prediction $P^- = 0.106$ m², and $\sigma = 0.683$ m after ten moves;
    - $d^2 = 0.36/0.34 = 1.06$ and $4/0.34 = 11.8$;
    - the chi-square 99% point for one degree of freedom, $z_{0.995}^2 = 6.635$.
- Not verified:
  - The exact ISO 8373:2012 and 2021 wordings, and the publication details of the cited works. These were checked against the reviewer's knowledge, not against the sources.
  - The scratch build was not screenshotted, so rendering at 360px and in dark mode was not re-checked in this pass. None of the four articles changed its figures since the first review, which did check them.
