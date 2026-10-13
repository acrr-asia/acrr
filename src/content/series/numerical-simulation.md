---
title: "Numerical Simulation for Engineers"
description: "A five-entry course on computing what differential equations predict, from discretization and finite differences to linear solvers, finite elements and verification."
category: "Mathematical Foundations"
status: "published"
objectives:
  - "Discretize a partial differential equation with its boundary and initial conditions into a finite algebraic problem, and state the order of accuracy of the result."
  - "Analyze explicit and implicit finite-difference schemes for accuracy and stability, and choose a time step accordingly."
  - "Choose a direct or an iterative method for the large sparse linear systems that discretization produces, and predict its cost."
  - "Derive the finite element method from the weak form of a boundary value problem, and explain how its error depends on mesh size and element degree."
  - "Verify a simulation code and result by measuring the observed order and estimating the numerical error, and validate a model against measurements with stated uncertainties."
---

This series is for engineers and students who use simulation results and want to know how they are produced and how far they can be trusted. It assumes calculus, basic linear algebra and the ordinary differential equations (ODEs) of the [Foundations of Control Systems](/series/foundations-of-control-systems) series; the [notes on numerical integration of ODEs](/blog/numerical-integration-notes) are useful background for the time stepping in the second entry.

The five entries follow a simulation from its equations to a result that can be defended, and each one supplies what the next needs. The first entry introduces the heat, wave and Poisson equations, turns a differential equation into a finite set of algebraic equations, and defines the vocabulary of error. The second adds time and shows that the choice between explicit and implicit schemes is decided by stability. Both kinds of problem end in large sparse linear systems, which the third entry solves with direct and iterative methods. The fourth derives the same kind of system a second way, from the weak form of the equation, so that meshes can follow any shape. The fifth asks how much the result of the whole chain can be trusted: it verifies the code and the solution and validates the model against measurements.

All entries share a few conventions. The Poisson equation is written $-\nabla^2 u = f$, so that the matrices it produces are positive definite; capital $U$ denotes a discrete approximation and lowercase $u$ the exact solution; quantities are in SI units. The code uses Python 3 with NumPy in double precision, and the main convergence rates and stability limits are checked by short experiments whose printed output is shown.
