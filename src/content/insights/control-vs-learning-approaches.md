---
title: "Model-Based Control and Learned Policies"
description: "Learn what model-based control and learned policies each offer, what is established about them, and when one is the more practical choice."
publishedAt: 2026-10-11
kind: "Comparison"
tags:
  - control-theory
  - machine-learning
  - robotics
---

A controller can be designed from a mathematical model of the system, or a policy can be learned from data gathered by interacting with it. The two families are often presented as competitors. This note separates what is established about each from an interpretation of when each is the better choice, for engineers deciding how to control a system whose model is only partly known.

## Established

**Model-based control** designs a feedback law from a mathematical model of the system. The [Foundations of Control Systems](/series/foundations-of-control-systems) series builds this approach from first principles, ending with [state-feedback design](/blog/state-feedback-controller-design). For a linear model with a quadratic cost, the linear-quadratic regulator (LQR) gives an optimal state-feedback gain. Classical tools such as gain and phase margins describe how much model error certain closed loops can tolerate. Model predictive control (MPC) solves a finite-horizon optimization at every step, using a model, and can represent input and state constraints explicitly.

**Learning-based methods**, such as reinforcement learning, improve a policy using data gathered from interaction, in simulation or on hardware. They do not need a closed-form model of the dynamics, and they can represent nonlinear behavior that is hard to write down by hand. Their typical costs are large amounts of data and weaker formal guarantees: a trained policy usually comes without a stability proof unless extra structure is added. A policy trained in simulation can also perform worse on hardware, because simulated and real dynamics differ; that difference is the [sim-to-real gap](/insights/closing-the-sim-to-real-gap). The [Machine Learning Fundamentals](/series/machine-learning-fundamentals) series covers the underlying ideas of learning from data and of evaluating what a model has learned.

## Interpretation

One reading is that the two approaches are ends of a spectrum rather than rivals, and that two factors decide between them: how much reliable model knowledge exists, and how costly a failure would be. When a reasonably accurate model is available and safety matters, model-based design offers analysis that a learned policy often cannot. When the dynamics or contacts are too complex to model well, learning may be the more practical route.

Hybrids try to combine the two: learning a correction on top of a nominal controller, or learning the model that an MPC controller then uses. How well they succeed depends on the particular system and on how the learned part is constrained, and no general answer is evident.

## Open questions

- How can the stability or safety of a learned component be certified without the certificate costing more than the training itself?
- Which benchmarks compare the two families fairly, counting data, design effort and robustness rather than only final reward?
- When a learned correction is added to a nominal controller, under what conditions do the guarantees of the nominal design survive?
