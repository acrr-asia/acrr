# Live review: Sensing and State Estimation: An Overview

- URL: https://acrr.asia/blog/sensing-and-state-estimation
- Source: `src/content/blog/sensing-and-state-estimation.mdx` (Introduction to Robotics, entry 4)
- Commit deployed: `7e20c2c`
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40087219510 (2026-10-24 10:51 UTC): 18 desktop-light, 34 mobile-light, 34 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-24. The reviewer did not write or revise this article.
- Risk: routine (a technical explainer; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Request revision. One major presentation finding (L1): the update equations of the worked example (Section 4) and the covariance equations of the Kalman filter (Section 5.1) are cut on a phone, and the fused variance of Section 4 is cut even at 1280 px. These are the central results of the page. No substantive or technical finding.

**Library decision: retain and update.** This is ACRR's only introduction to Bayesian state estimation and the Kalman filter, and other series depend on it by deep link: Calibration and Multisensor Fusion (Sensor Systems) links to its Sections 4, 5, 7.1 and 8 (inverse-variance weighting is shown to be the Section 4 update; its complementary filter extends Section 7.1), and State Feedback Controller Design (Foundations of Control Systems) points to it for the Kalman gain as an optimal observer. The overlap with Calibration and Multisensor Fusion is complementary, not duplication: that article works the complementary filter and consistency tests quantitatively, this one gives the estimation framework. The 13 October audit's findings (description, outline-style opening, separate series-close section, no exercises, reference details) were fixed in wave 1 and wave 2 and are visible on the live page. Any revision must keep the heading text of Sections 4, 5, 7.1 and 8, whose anchors other articles link to.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: a student or engineer who has the series' geometry and kinematics but no probability beyond the basics, and needs to understand how a robot knows where it is.
- Problem: kinematics and transforms assume the pose and joint angles are known; in practice sensors are indirect, noisy, biased, late and partial, so the reader needs a principled way to combine a model with measurements and to know how good the result is.
- Outcome: describe a belief by mean and covariance; explain the predict–update cycle and the Bayes filter; compute a one-dimensional Kalman update and prediction by hand; read the matrix Kalman filter and its assumptions; choose among KF, EKF, UKF and particle filter; apply the engineering details (frames, time stamps, angle wrapping, Mahalanobis gating, tuning, initialization).
- Distinctive contribution: a single hand-checkable corridor example that runs from the Gaussian update through prediction to the gating test and the exercises, plus a list of the engineering details that usually decide whether an estimator works, tied back to the series' frames and angle-wrapping material.
- Evidence: derivations and worked numbers; a fusion figure computed from the example; three exercises with answers; Bar-Shalom et al. (2001), Durrant-Whyte and Bailey (2006), Julier and Uhlmann (1997), Kalman (1960), Thrun et al. (2005).
- Limitations: EKF, UKF, particle filters and SLAM are described, not derived or worked; no code; the Kalman filter's optimality is stated, not proved.

The benefit is delivered. The opening links the three earlier entries and states the single idea (predict with a model, correct with a measurement); Section 2 supplies only the probability that is used; each later section builds on the corridor example. Spot checks recomputed in this review (python3): $K = 0.735$, $\hat x = 10.44$ m, $P = 0.066\ \text{m}^2$ ($\sigma = 0.26$ m); after ten moves with $Q = 0.04$, $\sigma = 0.68$ m; $d^2 = 0.36/0.34 = 1.06$ and, for a 12.0 m reading, $4.0/0.34 = 11.8$; the 99% chi-square bound for one degree of freedom is 6.63 (standard table value, not recomputed: scipy is not installed). The fusion figure matches the numbers in its caption. Value density: Section 8 is the most useful passage for practitioners and is rarely found in introductions; Section 7.2 (SLAM) is short and honest about being only a pointer. The title's "An Overview" undersells a page that includes a full worked filter, but it is not misleading. Value category: conceptual understanding. Format: explainer.

## C. Substantive findings

None.

## D. Visual and structural findings

### L1. The core update equations are cut

- Location: Section 4, the display "$K = \dots$, $\hat x = \hat x^- + K(z - \hat x^-)$, $P = (1 - K)P^-$": at 360 px it ends at "$\hat x = \hat x^- + K\,(z$" and the variance update is hidden (mobile-light-13). Section 4, the numerical display: at 1280 px "$P = 0.265 \times 0.25 = 0.066\ \text{m}^2$" is hidden (desktop-light-07); at 360 px only $K = 0.735$ is visible (mobile-light-13). Section 4, the prediction display: $P^- = 0.106$ hidden at 360 px (mobile-light-15). Section 5.1: at 360 px the measurement model $\mathbf z_k = H\mathbf x_k + \mathbf v_k$ (mobile-light-15) and both covariance equations, $P^- = APA^{\mathsf T} + Q$ and $P = (I - KH)P^-$, and the end of the gain formula (mobile-light-16) are hidden.
- Problem: these displays put two or three equations side by side, wider than the column. The hidden parts scroll sideways inside the box with no visible cue.
- Why it matters: the variance update is the half of the result that makes estimation more than averaging ("uncertainty shrinks"), and the covariance equations are half of the Kalman filter. A phone reader sees the gain but not what it does to the uncertainty; a desktop reader does not see the fused variance that the next display and Exercise 2 start from.
- Required action: one equation per line (or an `aligned` block) for the three Section 4 displays; in Section 5.1, put the two model equations on separate lines and stack the predict and update equations in a single column instead of two.
- Priority: major
- Acceptance condition: on new captures, $P = 0.066\ \text{m}^2$ is visible at 1280 px, and at 360 px (light and dark) every equation named above is fully visible without sideways scrolling.

The predict–update Mermaid diagram (Section 3.3) and the fusion figure (Section 4) are correct in dark mode (mobile-dark-10, 14). At 360 px the fusion figure's last tick and axis label ("position x (m)") are cut at the right edge (mobile-light-14), and the estimator table scrolls sideways (mobile-light-20): both are the site-level behaviors already recorded (figure minimum width without scroll cue; 7rem minimum table-cell width).

## E. Technical and source findings

None. `facts.json`: HTTP 200 on all three viewports, no horizontal page scroll, no overflowing elements, 0 KaTeX errors, 0 broken images, 0 console errors.

Not verified in this review: the reference details (the wave-1 and wave-2 reviews checked Kalman, Julier and Uhlmann and Durrant-Whyte and Bailey against primary or secondary sources; Bar-Shalom et al. and Thrun et al. were not re-fetched).

## F. Required changes

Mandatory:

- [ ] L1: stack the displays of Section 4 and Section 5.1 so that they fit at 360 px, and the Section 4 numerical display at 1280 px. Keep the heading text of Sections 4, 5, 7.1 and 8 (inbound fragment links).

Optional:

- [ ] Section 3.3 diagram: the two-line node labels read as one phrase ("Predict with the motion model mean moves, uncertainty grows"); a colon or dash after "model" would separate the action from its effect.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
