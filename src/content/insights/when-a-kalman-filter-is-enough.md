---
title: "When Is a Kalman Filter Enough?"
description: "Learn when a Kalman filter is the right estimator, when its nonlinear variants or a particle filter are needed, and which questions about the choice remain open."
publishedAt: 2026-10-11
kind: "Comparison"
tags:
  - control-theory
  - robotics
  - state-estimation
---

A robot or a process seldom measures its state directly, so it estimates it, and the usual starting point is the Kalman filter. This note asks when that filter is enough and when a more expensive estimator is justified, a choice that sets both the computing cost and the kind of failure to expect. The estimators themselves are described and compared in [Sensing and State Estimation](/blog/sensing-and-state-estimation), the last entry of the Introduction to Robotics series.

## Established

Take the model $x_{k+1} = F x_k + w_k$, $z_k = H x_k + v_k$, with known matrices $F$ and $H$. Suppose the noises $w_k$ and $v_k$ are zero-mean, white and Gaussian, independent of each other and of a Gaussian initial state, with known covariances $Q$ and $R$. Then the Kalman filter computes $\mathbb{E}[x_k \mid z_{1:k}]$ and its covariance exactly. That conditional mean is the minimum mean-square-error estimate among all estimators, linear or not. If the noise is not Gaussian but has the same covariances, the filter remains the best among linear estimators, though a nonlinear estimator may do better.

For nonlinear models, the extended Kalman filter (EKF) linearizes the dynamics and measurement functions about the current estimate. The unscented Kalman filter (UKF) instead passes a small, deterministic set of sample points through the nonlinear functions, and usually captures nonlinear effects better than the EKF at a similar cost. Both still summarize belief as a single Gaussian, and neither is optimal in general. Particle filters use weighted samples, so they can represent multimodal, non-Gaussian beliefs. The price is computation, which grows with the number of particles, and that number often has to grow quickly with the state dimension.

## Interpretation

One reading is that the deciding question is not whether the model is nonlinear, but whether the uncertainty is small compared with the scale on which the nonlinearity acts. That suggests a rough guide:

- Linear model, roughly Gaussian noise: a Kalman filter.
- Nonlinear model, with one Gaussian still a fair summary of belief: an EKF when the nonlinearity is mild over the spread of the uncertainty, a UKF when it is stronger.
- Genuinely multimodal belief, such as several distinct location hypotheses: a particle filter.

Under this reading, the sensible habit is to start with the simplest filter and move up only when evidence shows it failing.

## Open questions

- How can a silently broken Gaussian assumption be detected? Checks on the normalized innovation squared, which should follow a chi-square distribution when the model holds, are one tool, but their power against heavy tails or multimodality is unclear.
- How should $Q$ and $R$ be chosen? $Q$ must absorb unmodeled dynamics, and a filter with poor covariances still runs and still reports a covariance, which may be misleadingly confident.
- Can the ratio of uncertainty to nonlinearity scale behind the guide above be estimated online, so the choice of filter need not wait for an observed failure?
