---
title: "When Is a Kalman Filter Enough?"
description: "A short comparison of the Kalman filter, its nonlinear variants and particle filters, with a rough guide to choosing between them and a list of what stays hard."
publishedAt: 2026-10-11
kind: "Comparison"
tags:
  - control-theory
  - robotics
  - state-estimation
example: true
---

*This is an illustrative example insight, not a research result.*

## Established

Take the model $x_{k+1} = F x_k + w_k$, $z_k = H x_k + v_k$, with known matrices $F$ and $H$. Suppose the noises $w_k$ and $v_k$ are zero-mean, white and Gaussian, independent of each other and of a Gaussian initial state, with known covariances $Q$ and $R$. Then the Kalman filter computes $\mathbb{E}[x_k \mid z_{1:k}]$ and its covariance exactly. That conditional mean is the minimum mean-square-error estimate among all estimators, linear or not. If the noise is not Gaussian but has the same covariances, the filter remains the best among linear estimators, though a nonlinear estimator may do better.

For nonlinear models, the extended Kalman filter (EKF) linearizes the dynamics and measurement functions about the current estimate. The unscented Kalman filter (UKF) instead passes a small, deterministic set of sample points through the nonlinear functions. Both still summarize belief as a single Gaussian, and neither is optimal in general. Particle filters use weighted samples, so they can represent multimodal, non-Gaussian beliefs. The price is computation, which grows with the number of particles, and that number often has to grow quickly with the state dimension.

## Interpretation

One reading is that the deciding question is not whether the model is nonlinear, but whether the uncertainty is small compared with the scale on which the nonlinearity acts. That suggests a rough guide:

- Linear model, roughly Gaussian noise: a Kalman filter.
- Mildly nonlinear model, with one Gaussian still a fair summary of belief: an EKF or UKF.
- Genuinely multimodal belief, such as several distinct location hypotheses: a particle filter.

Under this reading, the sensible habit is to start with the simplest filter and move up only when evidence shows it failing.

## Open questions

- How can a silently broken Gaussian assumption be detected? Checks on the normalized innovation squared, which should follow a chi-square distribution when the model holds, are one tool, but their power against heavy tails or multimodality is unclear.
- How should $Q$ and $R$ be chosen? $Q$ must absorb unmodelled dynamics, and a filter with poor covariances still runs and still reports a covariance, which may be misleadingly confident.
- Can the ratio of uncertainty to nonlinearity scale behind the guide above be estimated online, so the choice of filter need not wait for an observed failure?
