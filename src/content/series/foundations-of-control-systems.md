---
# Authoring note: when a planned entry is written, publish it as an article in
# src/content/blog (with `series` and `seriesOrder`) and remove it from plannedEntries.
title: "Foundations of Control Systems"
description: "A series on how feedback shapes the behavior of dynamical systems, from first principles to state-space models."
category: "Robotics and Control"
status: "in-progress"
objectives:
  - "Explain how feedback changes the stability and speed of a system's response, and how sensitive that response is to model errors and disturbances."
  - "Describe a linear time-invariant system in both input-output form and state-space form."
  - "Relate the eigenvalues of a system matrix to stability and transient behavior."
  - "Recognize the assumptions and limits of a model before designing a controller around it."
plannedEntries:
  - title: "Stability and Eigenvalues"
    description: "How the eigenvalues of the system matrix determine whether the state of a linear system decays, oscillates, or grows."
  - title: "Designing a State-Feedback Controller"
    description: "Pole placement for a simple linear system, and what it assumes about the model and the available measurements."
---

This series is intended for readers who are comfortable with calculus and basic linear algebra. Each entry introduces one idea, states the assumptions it relies on, and points to the next idea in the sequence.
