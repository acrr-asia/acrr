---
title: "Model-Based Control and Learned Policies"
description: "A short comparison of model-based control and learning-based policies, separating what is well established from interpretation and open questions."
publishedAt: 2026-10-11
kind: "Comparison"
tags:
  - control-theory
  - machine-learning
  - robotics
---

## Established

Model-based control designs a feedback law from a mathematical model of the system. For a linear model with a quadratic cost, the linear-quadratic regulator (LQR) gives an optimal state-feedback gain. Classical tools such as gain and phase margins describe how much model error certain closed loops can tolerate. Model predictive control (MPC) solves a finite-horizon optimization at every step, using a model, and can represent input and state constraints explicitly.

Learning-based methods, such as reinforcement learning, improve a policy using data gathered from interaction, in simulation or on hardware. They do not need a closed-form model of the dynamics, and they can represent nonlinear behavior that is hard to write down by hand. Their typical costs are large amounts of data and weaker formal guarantees: a trained policy usually comes without a stability proof unless extra structure is added. A policy trained in simulation can also perform worse on hardware, because simulated and real dynamics differ. This difference is often called the sim-to-real gap.

## Interpretation

These approaches read better as two ends of a spectrum than as rivals. The deciding factors appear to be how much reliable model knowledge exists and how costly a failure would be. When a reasonably accurate model is available and safety matters, model-based design offers analysis that a learned policy often cannot. When the dynamics or contacts are too complex to model well, learning may be the more practical route.

Hybrids try to combine the two: learning a correction on top of a nominal controller, or learning the model that an MPC then uses. How well they succeed likely depends on the particular system and on how the learned part is constrained.

## Open questions

- How can the stability or safety of a learned component be certified without the certificate costing more than the training itself?
- Which benchmarks compare the two families fairly, counting data, design effort, and robustness rather than only final reward?
- When a learned correction is added to a nominal controller, under what conditions do the guarantees of the nominal design survive?
