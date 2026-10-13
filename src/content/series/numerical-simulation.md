---
title: "Numerical Simulation for Engineers"
description: "A series on computing what equations predict: discretizing differential equations, finite differences for heat and waves, solving large linear systems, the finite element method, and checking that a simulation can be trusted."
category: "Mathematical Foundations"
status: "published"
objectives:
  - "Turn partial differential equations with boundary conditions into finite-dimensional problems."
  - "Analyze explicit and implicit finite-difference schemes for accuracy and stability."
  - "Choose direct or iterative methods for the large linear systems that discretization produces."
  - "Explain the finite element method from its variational form, and verify and validate a simulation."
---

This series is for engineers and students who use simulation results and want to know how they are produced and how far they can be trusted. It assumes calculus, basic linear algebra and the ordinary differential equations met in the control systems series. Over five entries it goes from the heat, wave and Poisson equations and their boundary conditions to finite-difference schemes and their stability, from the sparse linear systems that discretization produces to direct and iterative solvers, from the weak form of a boundary value problem to finite elements in one and two dimensions, and finally to verification and validation: measuring a code's order of accuracy, estimating the numerical error of a result, and comparing a model with measurements. The series checks its main convergence rates and stability limits with short Python experiments.
