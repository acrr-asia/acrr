---
title: "Is the Sim-to-Real Gap Something to Close or to Measure?"
description: "A short research question on the gap between simulated and real robot behavior for learned controllers, and why it may be more useful as a measured property than as a defect to remove."
publishedAt: 2026-10-09
kind: "Research question"
tags:
  - robotics
  - machine-learning
  - simulation
---

## Established

A simulator is a model. To stay computationally tractable, and because the true physics and parameters are only partly known, it simplifies or approximates the physics: contact is usually approximated by a simple model, friction is often described by a few coefficients, actuators are often idealized, and sensors are often noise-free or given only simple noise models. A real robot also has effects such as communication delays, gear backlash and structural flexibility, which a simulator may omit or capture only roughly.

A policy trained on one such model optimizes for that model's behavior. If the real system differs in details the policy depends on, the policy can perform worse or fail. This discrepancy is commonly called the sim-to-real gap.

Two widely used mitigation ideas are domain randomization, which varies simulator parameters such as masses, friction coefficients or sensor noise during training so that the policy sees a range of plausible dynamics instead of one, and system identification, which fits the simulator's parameters to measurements from the real robot so the model matches it more closely.

## Interpretation

One reasonable reading is that the gap is a measurable property of a particular combination of simulator, policy, task and robot, and should be tested rather than assumed away. Some gap is expected to remain, since every simulator is simplified, so the practical question is whether it matters for the task.

A simple way to quantify part of it is to apply the same action sequence, from the same nominal initial state, in simulation and on hardware, and report

$$
\Delta(T) = \max_{0 \le t \le T} \lVert x_{\text{real}}(t) - x_{\text{sim}}(t) \rVert .
$$

This measures trajectory mismatch over a stated horizon $T$ and norm, for one chosen action sequence. It mixes dynamics error with measurement and initial-state error, and it does not capture what the closed-loop policy does with the mismatch, so task-level outcomes, such as the fraction of successful trials under identical conditions, would need reporting alongside it.

## Open questions

- How can the gap be bounded before deployment, when real hardware data are scarce or absent? What kind of evidence would justify such a bound?
- Which model details (contact, friction, actuator dynamics, latency, sensing) matter most for which task, and can that be learned from a small amount of real data?
- Under what conditions would a guarantee, rather than a measurement, become the better way to handle the gap?
