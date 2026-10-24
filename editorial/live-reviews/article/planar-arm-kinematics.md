# Live review: Forward and Inverse Kinematics of a Planar Arm

- URL: https://acrr.asia/blog/planar-arm-kinematics
- Source: `src/content/blog/planar-arm-kinematics.mdx` (Introduction to Robotics, entry 3)
- Commit deployed: `7e20c2c`
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40087219510 (2026-10-24 10:51 UTC): 15 desktop-light, 26 mobile-light, 26 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-24. The reviewer did not write or revise this article.
- Risk: routine (a technical tutorial; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Request revision. One major presentation finding (L1): at 360 px several display equations are cut where the hidden part is the result (the workspace radius loses the $\cos\theta_2$ term that the next sentence relies on, the shoulder-angle formula loses its second $\operatorname{atan2}$ argument, the Newton update loses $\Delta\mathbf q_k$ and $\mathbf q_{k+1}$, the worked example loses $y$ and $\phi$). One minor finding (L2): the worked example's $\phi = 75^\circ$ is also hidden at 1280 px.

**Library decision: retain and update.** The page is the series' worked bridge from transforms to motion: forward kinematics, the workspace, closed-form and numerical inverse kinematics, the Jacobian and singularities, all on one arm with one set of numbers. No other ACRR article covers inverse kinematics or the manipulator Jacobian; Configuration Space and the Motion Planning Problem and Trajectories and Time Scaling build on it (joint space as configuration space, joint velocity limits) and link to it rather than repeat it. The 13 October audit's findings (description, headings, missing Craig reference, incomplete Denavit–Hartenberg citation, unlinked entries, no exercises, garbled dexterous-workspace sentence) were fixed in wave 1 and are visible on the live page. Only the equation layout needs work.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: a student or engineer who has the previous entry's homogeneous transforms and wants to command a robot arm in terms of where its gripper should be.
- Problem: tasks are stated in gripper coordinates but arms are driven through joints; the reader needs to convert in both directions and to understand why the inverse direction has several, infinitely many or no answers and misbehaves near certain postures.
- Outcome: compute the forward kinematics and workspace of a two-link arm; solve its inverse kinematics in closed form with $\operatorname{atan2}$ and choose between the two solutions; derive the Jacobian and its singular configurations; run Newton and damped-least-squares iterations and know when each fails; explain redundancy and what carries over to six-joint arms (spherical wrist, up to eight solutions, interior singularities).
- Distinctive contribution: one example arm ($l_1 = 1.0$, $l_2 = 0.7$, $\theta = (30^\circ, 45^\circ)$) carried through every section, including the two IK postures, Newton's convergence sequence and a side-by-side Newton versus damped step for an unreachable target.
- Evidence: derivations and worked numbers; a figure of the two postures and the workspace; three exercises with answers; Craig (2005), Denavit and Hartenberg (1955), Lynch and Park (2017), Pieper (1968), Siciliano et al. (2009).
- Limitations: planar two-link arm only; Denavit–Hartenberg and product of exponentials named but not developed; no dynamics; no code.

The benefit is delivered. The opening states the asymmetry between the two directions and that most of the entry is about the inverse; each section answers one question in the order a practitioner meets it. Spot checks recomputed in this review (python3, numpy): forward kinematics $(1.047, 1.176)$; $c_2 = 0.7071$ and the second solution $(66.6^\circ, -45^\circ)$, which maps back to the same point; Newton from $(0^\circ, 90^\circ)$ gives errors $0.478$, $0.113$, $1.16 \times 10^{-2}$, $1.80 \times 10^{-4}$, $6.3 \times 10^{-8}$, as printed; for the target $(1.75, 0.05)$ from $(0^\circ, 1^\circ)$ the first Newton step is $(166.6^\circ, -401.6^\circ)$ and the first damped step ($\lambda = 0.1$) is $(1.80^\circ, -1.33^\circ)$; the damped iteration settles $0.0507$ from the target, which equals the target's distance from the outer radius; $\det J = 0.495$ and $0.122$. The figure caption matches the geometry (the $\theta_2 = 45^\circ$ elbow lies below the base–target line). Value density: no section is padding; Section 6.3's numerical comparison is the most useful passage and the one least often found in introductory texts. Value category: practical implementation (with strong conceptual content). Format: tutorial.

## C. Substantive findings

None.

## D. Visual and structural findings

### L1. Key equations cut at 360 px

- Location: at 360 px: Section 3, $r = \sqrt{x^2 + y^2} = \sqrt{l_1^2 + l_2^2 + 2 l_1 l_2 \cos\theta_2}$ ends at "$2l_1l_2$ c" (mobile-light-08); Section 4.2, the shoulder-angle formula ends after "$l_2\sin\theta_2$," (mobile-light-10); Section 6.2, the Newton step shows only $\mathbf e_k$ and "$\Delta\mathbf q_k = J($" (mobile-light-15); Section 2.2, the example shows $x$ only, with $y$ and $\phi$ hidden (mobile-light-06), and the transform product loses its last factor $\mathrm{Trans}(l_2, 0)$ (mobile-light-05).
- Problem: each display is wider than the phone column. The rest scrolls sideways inside the box, with no visible cue.
- Why it matters: these are results the text relies on immediately: "which depends only on the elbow angle" refers to the hidden $\cos\theta_2$; the shoulder angle is the second half of the closed-form solution; the Newton update is the method of Section 6.
- Required action: break these displays over lines: the two forms of $r$ on two lines; $\theta_1$ with the second $\operatorname{atan2}$ on its own line (or define $\beta = \operatorname{atan2}(l_2\sin\theta_2, l_1 + l_2\cos\theta_2)$ first); the three Newton equations one per line; the example's $x$, $y$, $\phi$ in an `aligned` block.
- Priority: major
- Acceptance condition: on new captures at 360 px (light and dark), the four displays named above are fully visible without sideways scrolling.

### L2. Worked example's orientation hidden at desktop width

- Location: Section 2.2, the example display; desktop-light-03.
- Problem: at 1280 px the display ends after $y = \dots = 1.176$; "$\phi = 75^\circ$" is hidden to the right.
- Why it matters: small (the value is $\theta_1 + \theta_2$), but the example is carried through the entry.
- Required action: covered by the `aligned` block proposed in L1.
- Priority: minor
- Acceptance condition: $\phi = 75^\circ$ visible at 1280 px.

The figure in Section 4.3 is correct in dark mode (mobile-dark-11); at 360 px its "θ₂ = 45°" label is cut at the right edge (mobile-light-11), which is the site-level figure behavior already recorded (figures keep 60 percent of their natural width; no scroll cue). The summary table wraps but stays readable at 360 px.

## E. Technical and source findings

None. `facts.json`: HTTP 200 on all three viewports, no horizontal page scroll, no overflowing elements, 0 KaTeX errors, 0 broken images, 0 console errors.

Not verified in this review: the bibliographic details of the five references (not re-fetched; the wave-2 review checked Denavit and Hartenberg against two secondary sources). Pieper's condition is stated as a sufficient condition (intersecting axes), which is correct; the parallel-axes case is not mentioned, as the audit noted.

## F. Required changes

Mandatory:

- [ ] L1: split the displays of Sections 2.2, 3, 4.2 and 6.2 so that they fit at 360 px.

Optional:

- [ ] L2: covered by L1.
- [ ] Section 8: one clause noting that Pieper's result also covers three consecutive parallel axes would make the sufficient condition complete.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
