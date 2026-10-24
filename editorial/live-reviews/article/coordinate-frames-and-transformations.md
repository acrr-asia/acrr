# Live review: Coordinate Frames and Rigid-Body Transformations

- URL: https://acrr.asia/blog/coordinate-frames-and-transformations
- Source: `src/content/blog/coordinate-frames-and-transformations.mdx` (Introduction to Robotics, entry 2)
- Commit deployed: `7e20c2c`
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40087219510 (2026-10-24 10:51 UTC): 17 desktop-light, 29 mobile-light, 29 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-24. The reviewer did not write or revise this article.
- Risk: routine (a technical explainer; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Request revision. One major presentation finding (L1): several display equations are wider than the column, and the hidden parts are results the argument depends on (the second product of Section 3.2 on every screen; on a phone also the second equation of Section 2.1, the matrix $K$ of Rodrigues' formula, the inverse translation of Section 4.3 and the results of the Section 5 worked example). One minor typographic finding (L2).

**Library decision: retain and update.** This is the geometry entry the rest of the robotics series and the motion-planning series stand on: Forward and Inverse Kinematics of a Planar Arm composes its homogeneous transforms, Sensing and State Estimation uses its frames and angle wrapping, and Configuration Space and the Motion Planning Problem uses $SE(2)$ and $SE(3)$ as configuration spaces. It is the only ACRR page that covers rotation matrices, Euler angles, quaternions and the frame tree; nothing on it repeats another article. The 13 October audit's findings (description length, title-case headings, British spellings, unlinked first entry, no exercises, reference format) were fixed in wave 1 and are visible on the live page. The content is correct and worth its reading effort; only the equation layout needs work, so neither a rewrite nor a merge would gain anything.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: a student or engineer who knows matrix multiplication and trigonometry, has read the series' first entry and is about to meet arm kinematics and state estimation.
- Problem: every sensor and link reports positions in its own frame; the reader needs a precise, mechanical way to convert positions and orientations between frames and to avoid the usual frame bugs.
- Outcome: build and invert 2D and 3D rotation matrices and homogeneous transforms; explain why 3D rotations do not commute; choose among rotation matrices, Euler angles, axis–angle and quaternions knowing gimbal lock and the $q$/$-q$ ambiguity; chain transforms through a frame tree; recognize the common mistakes (order, inversion, units, quaternion ordering, angle wrapping, axis conventions).
- Distinctive contribution: label-cancelling notation used consistently from the definition to a worked mobile-robot example and a frame tree, with a table of common mistakes and their symptoms that ties the mathematics to the bugs practitioners actually hit.
- Evidence: derivations and worked numbers in the text; three exercises with answers; Craig (2005), Lynch and Park (2017), Siciliano et al. (2009).
- Limitations: no derivation of quaternion multiplication or slerp; Euler-angle conventions beyond yaw–pitch–roll only counted, not listed; no code.

The benefit is delivered. The opening states the problem with concrete examples (lidar, camera, map) and the conventions; each section adds one layer (frames and notation, planar rotation, spatial rotation and its representations, rigid transforms, a worked example, the active/passive distinction, the frame tree and time, mistakes). Spot checks recomputed in this review (python3, numpy): $R_x(90^\circ)R_z(90^\circ)$ and $R_z(90^\circ)R_x(90^\circ)$ as printed, and their images of $\hat{x}$, $(0,0,1)$ and $(0,1,0)$; the gimbal-lock pair $(\psi,\phi) = (30^\circ,10^\circ)$ and $(50^\circ,30^\circ)$ give the same matrix at $\theta = 90^\circ$; ${}^{W}T_{R}(3,0,1) = (2,4,1)$; ${}^{R}T_{W}$ as printed; the camera chain gives $(1.8, 2.5)$; the reading of $R_z R_y R_x$ as intrinsic yaw–pitch–roll in Section 6 is right. Value density: no section is padding; the common-mistakes table and Section 7.2 (time-stamped transforms) are the passages a textbook chapter usually lacks. Overlap: Section 7.1 previews the planar-arm entry and Section 3.3's quaternions reappear only as a mention in Sensing and State Estimation; both are handled with links, not repetition. Value category: conceptual understanding (practical implementation close behind, through the mistakes table). Format: explainer.

## C. Substantive findings

None. The text is correct and complete for its contract.

## D. Visual and structural findings

### L1. Display equations cut where the argument depends on them

- Location: Section 3.2, the pair of products (desktop-light-05: the third column of $R_z(90^\circ)R_x(90^\circ)$ is hidden; mobile-light-09: the whole second product is hidden). At 360 px also: Section 2.1, the second equation ${}^{A}\mathbf p = {}^{A}R_{B}\,{}^{B}\mathbf p$ (mobile-light-06, entirely off-screen although the next paragraph begins "The second equation says"); Section 3.3, the matrix $K$ in Rodrigues' formula (mobile-light-12); Section 4.3, the translation column of the inverse (mobile-light-15); Section 5, the results ${}^{W}\mathbf p = (2,4,1)$ and ${}^{R}T_{W}(2,4,1) = (3,0,1)$ and the matrix ${}^{R}T_{C}$ (mobile-light-16, 17). Section 3.1, $R_z(\theta)$, is also hidden at both widths (desktop-light-05, mobile-light-08), which matters less because it is the familiar planar matrix.
- Problem: each of these displays puts two equations side by side, wider than the text column. The hidden part scrolls sideways inside its box, but nothing tells the reader it is there.
- Why it matters: Section 3.2 exists to show that the two products differ; a reader who sees only one product (phone) or a truncated second one (desktop) does not see the point. On a phone the worked example of Section 5, the page's main demonstration, shows its setup but not its answers.
- Required action: put each of these pairs on separate lines (one equation per display, or an `aligned`/`gathered` block), and set $R_x$, $R_y$, $R_z$ in Section 3.1 one per line.
- Priority: major
- Acceptance condition: on new captures, both products of Section 3.2 and $R_z(\theta)$ are fully visible at 1280 px; at 360 px every equation listed above is fully visible without sideways scrolling, light and dark.

### L2. Opening quotation mark instead of apostrophe after a math symbol

- Location: Section 2.1 ("weighting $B$‘s axes"), Section 4.1 ("into $A$‘s orientation", "of $B$‘s origin"); desktop-light-04 and 08.
- Problem: the possessive after an inline math symbol is rendered as a left single quotation mark (‘) instead of an apostrophe (’).
- Why it matters: small, but visible three times in the core sections.
- Required action: write the apostrophe as ’ in the source after the math (or rephrase, for example "the axes of $B$").
- Priority: minor
- Acceptance condition: the three possessives show an apostrophe on the live page.

The frame-tree Mermaid diagram (Section 7.1) fits the column at both widths and is correct in dark mode (mobile-dark-20); the three tables scroll sideways at 360 px with the site's scroll shadow (site-level: 7rem minimum cell width, already recorded). The page uses the right representations: matrices with worked numbers, a comparison table of orientation representations, a tree diagram and a mistakes table.

## E. Technical and source findings

None. `facts.json`: HTTP 200 on all three viewports, no horizontal page scroll, no overflowing elements, 0 KaTeX errors, 0 broken images, 0 console errors.

Not verified in this review: the bibliographic details of the three textbooks (not re-fetched; existence and editions are well known and match).

## F. Required changes

Mandatory:

- [ ] L1: split the side-by-side display equations of Sections 2.1, 3.1, 3.2, 3.3, 4.3 and 5 so that each fits at 360 px.

Optional:

- [ ] L2: apostrophes after inline math.
- [ ] Section 8, "Using ${}^{A}T_{B}$ where ${}^{B}T_{A}$ was needed": "points reflected through the frame's origin" is loose (the error applies the inverse motion, not a reflection); "points moved by the inverse transform" would be exact.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
