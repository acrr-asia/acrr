---
title: "What Makes a Simulation Trustworthy?"
description: "Learn how verification and validation differ, what a convergence study shows, and why trust in a simulation depends on the use it is put to."
publishedAt: 2026-10-09
kind: "Methodological note"
tags:
  - simulation
  - numerical-methods
  - verification
---

Simulation results are used to size components, tune controllers and argue that a design is safe, often by readers who did not write the code. This note separates what can be established about a simulation's correctness from the judgment of whether it can be trusted for a given purpose, and lists what is still hard. The [fifth entry of the Numerical Simulation series](/blog/verifying-and-validating-a-simulation) treats the same ground in depth.

## Established

Two questions are conventionally kept apart. **Verification** asks whether the equations are being solved correctly: is the code free of defects, and does the numerical error shrink as the step size or mesh is refined? **Validation** asks whether the right equations are being solved: do the model's predictions agree with measurements of the real system, within a stated uncertainty?

For a numerical method of order $p$, the global error should scale roughly as $h^p$ once the step size $h$ is small enough. Halving $h$ should therefore reduce the error of a first-order method such as explicit Euler by about a factor of two, and the error of the classical fourth-order Runge–Kutta method by about a factor of sixteen; the [notes on numerical integration](/blog/numerical-integration-notes) measure both. Observing the expected rate in a refinement study is evidence that the implementation is correct, and failing to observe it is a warning sign.

Some methods also have qualitative failure modes. Explicit Euler applied to an undamped oscillator makes the energy grow with every step. That growth is a numerical artifact, not physics.

## Interpretation

One reading is that trust is a property of a simulation together with its intended use, not of the simulation alone. A model can be adequate for predicting a trend and inadequate for predicting a safety margin. Passing verification checks does not establish validity, because a perfectly solved wrong model is still wrong.

A trustworthy report therefore states its assumptions, its parameter values, the step sizes it tested, and the regime in which a comparison with reality has been made, since outside that regime a prediction is an extrapolation.

## Open questions

- How should model-form uncertainty, meaning the error that comes from the equations themselves, be quantified when no experimental data exist?
- How large a gap between simulation and the real system is acceptable for a given decision, and who decides?
- What is the most compact way to show readers a convergence study and its assumptions without burying them in detail?
