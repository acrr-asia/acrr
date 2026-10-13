---
title: "Machine Learning Fundamentals"
description: "A series on the core ideas behind learning from data: models, loss functions, optimization, and how to evaluate what a model has learned."
category: "AI and Machine Learning"
status: "published"
objectives:
  - "Formulate a supervised learning problem in terms of a model, a loss function, and a data set."
  - "Explain gradient-based optimization and the role of the learning rate."
  - "Distinguish training error from generalization error, and explain why held-out evaluation matters."
  - "Identify common sources of data leakage and bias in an evaluation setup."
---

This series is intended for readers who can program and are comfortable with derivatives, vectors and matrices, and the basic ideas of probability (expected value, variance, the normal distribution). It builds supervised learning from first principles: the learning problem as minimizing a loss over examples, gradient descent and its stochastic variants, why flexible models overfit and how regularization limits that, and how to evaluate a model honestly, avoiding data leakage and reporting results with their uncertainty. Every example uses small synthetic data sets in Python with numpy, so that the true answer is known and each number can be reproduced.
