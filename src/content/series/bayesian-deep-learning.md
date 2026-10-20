---
title: "Bayesian Deep Learning"
description: "Give neural networks calibrated uncertainty: posteriors, sampling, Laplace, variational inference, ensembles, Gaussian processes, priors and scaling."
category: "AI and Machine Learning"
status: "published"
objectives:
  - "Explain what a posterior distribution over network parameters or functions is, how the posterior predictive is formed, and how epistemic and aleatoric uncertainty differ."
  - "Compare the main approximate-inference families for neural networks (Markov chain Monte Carlo, Laplace approximations, variational inference and ensembles) by their assumptions, cost and failure modes."
  - "Relate neural networks to Gaussian processes and kernel methods, and explain how priors, symmetries and identifiability shape a Bayesian neural network."
  - "Choose a method that scales to a given model and data set, and evaluate predictive uncertainty with calibration, proper scoring rules and selective prediction."
  - "Describe current research directions in Bayesian deep learning and state the open problems each one addresses."
---

The series is written for readers who have trained neural networks and want to know how far to trust their predictions. It assumes the material of the [Machine Learning Fundamentals](/series/machine-learning-fundamentals) series (empirical risk, gradient descent, regularization and honest evaluation), basic probability including Bayes' theorem, and linear algebra at the level of eigenvalues and positive-definite matrices. Code examples use Python 3 with NumPy.

The topics and their order follow a two-volume collection of notes on Bayesian deep learning prepared by ACRR. The entries condense that material for the site; their text, examples and figures were written for this series, and they cite the primary literature directly.

The first entry sets out the problem every later entry solves: the posterior over parameters, the posterior predictive and why it cannot be computed exactly for a neural network. The next four entries present the main families of approximate inference in the order of how they treat the posterior. Sampling methods draw from it, Laplace approximations fit a Gaussian at a mode, variational inference optimizes a tractable family, and ensembles combine several independently trained modes.

The sixth entry changes the point of view from weights to functions, through kernels and Gaussian processes. The seventh asks what a prior over network weights or functions says, and how the symmetries of a network make its parameters unidentifiable. The eighth entry deals with cost: methods that bring Bayesian inference to large models, such as last-layer inference and single-forward-pass methods. The ninth turns to practice: how predictive uncertainty is evaluated and used, in selective classification, active learning and large language models. The last entry surveys current research directions.

Notation is shared across the series. $\theta$ denotes the parameters, $\mathcal{D} = \{(x_n, y_n)\}_{n=1}^N$ the training data, $p(\theta)$ the prior, $p(\mathcal{D} \mid \theta)$ the likelihood and $p(\theta \mid \mathcal{D})$ the posterior; $x^*$ and $y^*$ are a test input and its output.
