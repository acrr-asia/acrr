---
title: "Bayesian Deep Learning"
description: "Give neural networks calibrated uncertainty: posteriors, sampling, Laplace, variational inference, ensembles, Gaussian processes, priors and scaling."
category: "AI and Machine Learning"
status: "in-progress"
objectives:
  - "Explain what a posterior distribution over network parameters or functions is, how the posterior predictive is formed, and how epistemic and aleatoric uncertainty differ."
  - "Compare the main approximate-inference families for neural networks (Markov chain Monte Carlo, Laplace approximations, variational inference and ensembles) by their assumptions, cost and failure modes."
  - "Relate neural networks to Gaussian processes and kernel methods, and explain how priors, symmetries and identifiability shape a Bayesian neural network."
  - "Choose a method that scales to a given model and data set, and evaluate predictive uncertainty with calibration, proper scoring rules and selective prediction."
  - "Describe current research directions in Bayesian deep learning and state the open problems each one addresses."
plannedEntries:
  - title: "Chapter 7: Laplace Approximations: Introduction"
  - title: "Chapter 8: Linearized Laplace Approximations"
  - title: "Chapter 9: The Differential Geometric Perspective on Laplace"
  - title: "Chapter 10: Analytic, Low-Cost Functionality from Laplace"
  - title: "Chapter 11: Model Selection with the Marginal Likelihood"
  - title: "Chapter 12: Introduction to Variational Inference"
  - title: "Chapter 13: Gaussian Mean-Field Variational Inference"
  - title: "Chapter 14: Dropout-Based Variational Inference"
  - title: "Chapter 15: Natural-Gradient-Based Variational Inference"
  - title: "Chapter 16: Particle-Based Variational Inference"
  - title: "Chapter 17: Variational Inference in Function Space"
  - title: "Chapter 18: Sequential Variational Inference"
  - title: "Chapter 19: Ensembles: Introduction and Connections with Approximate Bayesian Inference"
  - title: "Chapter 20: Hybrid Ensemble Sampling Methods"
  - title: "Chapter 21: Practical Applications of Deep Ensembles"
  - title: "Chapter 22: PAC-Bayesian Deep Neural Network Ensembles"
  - title: "Chapter 23: Introduction to Kernel Methods"
  - title: "Chapter 24: Deep Kernel Learning"
  - title: "Chapter 25: Deep Gaussian Processes"
  - title: "Chapter 26: Deep Kernel Processes and Deep Kernel Machines"
  - title: "Chapter 27: Meta-Learning Deep Kernel Gaussian Processes"
  - title: "Chapter 28: Introduction to Priors"
  - title: "Chapter 29: Statistical Properties of Priors"
  - title: "Chapter 30: Informative Priors"
  - title: "Chapter 31: Function-Space Priors"
  - title: "Chapter 32: Symmetries in Bayesian Neural Networks"
  - title: "Chapter 33: Symmetries and Sampling"
  - title: "Chapter 34: Learning Inductive Bias and Symmetries"
  - title: "Chapter 35: Interpretable and Identifiable Deep Generative Models via Bayesian Pyramids"
  - title: "Chapter 36: Bayesian Mixture of Experts in Bayesian Deep Learning"
  - title: "Chapter 37: Scalable Bayesian Deep Learning by Single Forward Pass Inference"
  - title: "Chapter 38: Scalable Gaussian Processes"
  - title: "Chapter 39: Last-Layer Inference"
  - title: "Chapter 40: Scalable Laplace Approximations"
  - title: "Chapter 41: Learned Compression with Deterministic Codes"
  - title: "Chapter 42: Learned Compression with Stochastic Codes"
  - title: "Chapter 43: Bayesian Large Language Models"
  - title: "Chapter 44: Confidence-Based Selective Classification"
  - title: "Chapter 45: Biomedical Data Imputation"
  - title: "Chapter 46: Deep Bayesian Spatio-Temporal Modeling of Wildfires"
  - title: "Chapter 47: Software for Bayesian Deep Learning"
  - title: "Chapter 48: Subspace Inference"
  - title: "Chapter 49: Implicitly Bayesian Prediction Rules"
  - title: "Chapter 50: Diffusion Models"
  - title: "Chapter 51: Prior-Data Fitted Networks"
  - title: "Chapter 52: Advances in Singular Learning Theory for Bayesian Deep Learning"
  - title: "Chapter 53: Active Learning and Experimental Design"
  - title: "Chapter 54: Causal-Aware Bayesian Deep Learning"
  - title: "Chapter 55: Credal Bayesian Deep Learning and Imprecise Probability"
  - title: "Chapter 56: Bayesian Reinforcement Learning"

---

The series is written for readers who have trained neural networks and want to know how far to trust their predictions. It assumes the material of the [Machine Learning Fundamentals](/series/machine-learning-fundamentals) series (empirical risk, gradient descent, regularization and honest evaluation), basic probability including Bayes' theorem, and linear algebra at the level of eigenvalues and positive-definite matrices. Code examples use Python 3.13 with NumPy 2.5.3 only, so that every computation is visible; each listing gives its random seed and its real output.

The series publishes ACRR's two-volume collection of notes on Bayesian deep learning in full: its 56 chapters, in ten parts, each appear as one entry, with the citation markers of the original removed and the figures redrawn for the site. Ten overview entries, written for the site with their own NumPy examples and references to the primary literature, introduce the series and each part. The overview of a part comes first and its chapters follow it. Chapters not yet published are listed below as planned.

The first entry sets out the problem every later entry solves: the posterior over parameters, the posterior predictive and why it cannot be computed exactly for a neural network. Parts I to IV present the main families of approximate inference, in decreasing order of how directly they target the exact posterior: sampling methods (Part I) draw from the posterior itself, Laplace approximations (Part II) fit a Gaussian at one mode, variational inference (Part III) optimizes the best member of a tractable family, and ensembles (Part IV) combine several independently trained modes.

Part V changes the point of view from weights to functions, through kernels and Gaussian processes. Parts VI and VII ask what a prior over network weights or functions says, and how the symmetries of a network make its parameters unidentifiable. Part VIII deals with cost: methods that bring Bayesian inference to large models, such as last-layer inference and single-forward-pass methods. Part IX turns to practice: how predictive uncertainty is evaluated and used, in large language models, selective classification and scientific applications, and which software supports it. Part X surveys current research directions.

The overview entries share one notation; the chapters keep the notation of the original, which each chapter defines where it is used. $\theta$ denotes the parameters, $\mathcal{D} = \{(x_n, y_n)\}_{n=1}^N$ the training data, $p(\theta)$ the prior, $p(\mathcal{D} \mid \theta)$ the likelihood and $p(\theta \mid \mathcal{D})$ the posterior; $x^*$ and $y^*$ are a test input and its output. $P$ is the number of parameters, $C$ the number of classes and $\sigma$ the standard deviation of Gaussian observation noise. A Gaussian prior on each weight has standard deviation $s_0$ (or precision $\alpha = 1/s_0^2$ where that is clearer), $M$ is the number of Monte Carlo samples and $J$ the number of ensemble members.
