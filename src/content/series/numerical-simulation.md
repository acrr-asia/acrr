---
# Authoring note: when a planned entry is written, publish it as an article in
# src/content/blog (with `series` and `seriesOrder`) and remove it from plannedEntries.
# Remove it from the Vietnamese translation (src/content/series/vi/numerical-simulation.md) as well.
title: "Numerical Simulation for Engineers"
description: "A planned series on computing what equations predict: discretising differential equations, finite differences for heat and waves, solving large linear systems, the finite element method, and checking that a simulation can be trusted."
category: "Mathematical Foundations"
status: "planned"
objectives:
  - "Turn partial differential equations with boundary conditions into finite-dimensional problems."
  - "Analyse explicit and implicit finite-difference schemes for accuracy and stability."
  - "Choose direct or iterative methods for the large linear systems that discretisation produces."
  - "Explain the finite element method from its variational form, and verify and validate a simulation."
plannedEntries:
  - title: "From Differential Equations to Discrete Problems"
    description: "The equations of heat, waves and fields, boundary conditions, and the idea of discretisation."
  - title: "Finite Differences for Heat and Waves"
    description: "Explicit, implicit and Crank-Nicolson schemes, and how accuracy and stability are analysed."
  - title: "Solving Large Linear Systems"
    description: "Gaussian elimination and Cholesky factorisation, and iterative methods from Jacobi to conjugate gradients."
  - title: "The Finite Element Method"
    description: "Weak forms, Galerkin's method, elements and meshes, from one dimension to two."
  - title: "Verifying and Validating a Simulation"
    description: "Convergence studies, comparison with known solutions and experiments, and reporting the limits of a model."
---

This series is planned and has not started publishing. It assumes calculus, basic linear algebra and the ordinary differential equations met in the control systems series. The outline below describes the intended scope and may change before any entry is written.
