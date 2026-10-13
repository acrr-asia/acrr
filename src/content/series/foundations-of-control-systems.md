---
title: "Foundations of Control Systems"
description: "A series on how feedback shapes the behavior of dynamical systems, from first principles to state-space models, stability and state-feedback design."
category: "Robotics and Control"
status: "published"
objectives:
  - "Explain how feedback changes the stability and speed of a system's response, and how sensitive that response is to model errors and disturbances."
  - "Describe a linear time-invariant system in both input-output form and state-space form."
  - "Relate the eigenvalues of a system matrix to stability and transient behavior."
  - "Recognize the assumptions and limits of a model before designing a controller around it."
---

The series is for readers who know calculus and basic linear algebra (matrix products, inverses, eigenvalues and eigenvectors) and can read Python. It also uses complex numbers and linear differential equations with constant coefficients; everything beyond that, including the Laplace transform and the matrix exponential, is introduced where it is first needed.

The entries build one line of argument. The first sets out the vocabulary of a feedback loop, the requirements a controller must meet, the transfer function and the step-response measures used throughout. The second applies proportional feedback to the simplest possible plant, a first-order system, and shows what feedback changes: speed, stability and sensitivity, at the price of an offset. A single equation cannot describe a mass on a spring or a robot joint, so the third entry introduces state-space models and relates them to the transfer function. The fourth explains why the eigenvalues of the system matrix decide stability and transient behavior, and where they stop being enough. The fifth uses feedback from the measured state to place those eigenvalues, and examines what such a design assumes about the model, the actuator and the measurements. The input-output view comes first because it gives the performance measures in their simplest form; the state-space view follows because it handles several variables and leads directly to design.

All entries use SI units with time in seconds, angular frequencies and eigenvalues in radians per second, the 2% criterion for settling time, and $j$ for the imaginary unit. The code uses Python 3, with NumPy from the third entry on.
