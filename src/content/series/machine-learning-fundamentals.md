---
title: "Machine Learning Fundamentals"
description: "Four entries build supervised learning from first principles: the learning problem, gradient descent, overfitting and regularization, and honest evaluation."
category: "AI and Machine Learning"
status: "published"
objectives:
  - "Formulate a supervised learning problem in terms of a model, a loss function, and a data set."
  - "Explain gradient-based optimization and the role of the learning rate."
  - "Distinguish training error from generalization error, and explain why held-out evaluation matters."
  - "Identify common sources of data leakage and bias in an evaluation setup."
---

This series is for readers who can program and are comfortable with derivatives, vectors and matrices, and the basic ideas of probability (expected value, variance, the normal distribution). Each entry recalls any further idea it needs, such as eigenvalues, covariance matrices or a concentration inequality, where it first uses it.

The four entries follow the questions a learning problem raises, in the order they arise. The first entry, *Learning from Data*, states the problem: a model, a loss function and a data set, with risk as the quantity to make small and the training error as an optimistic estimate of it. The second, *Gradient Descent and Its Variants*, answers how the training error is minimized when there is no closed-form solution, and why the learning rate decides whether the iteration converges. The third, *Generalization, Overfitting, and Regularization*, asks how far the minimized training error can drift from the risk as models grow more flexible, and how penalties and early stopping limit the drift. The fourth, *Evaluating Models Honestly*, shows how to estimate the risk from finite data without fooling oneself: validation and test sets, cross-validation, data leakage, bias in the evaluation setup, and reporting with uncertainty.

All entries share the same conventions. Examples are written in Python 3 with NumPy, and the quoted outputs were produced with Python 3.13 and NumPy 2.5.3. Every data set is synthetic and generated with a stated seed, so the true relation and the irreducible error are known and each number can be reproduced with the stated NumPy version (other versions may produce different random streams). The mean squared error is the plain average of squared errors (no factor of one half), classes in binary classification are coded 0 and 1, and sections are numbered so that later entries can cite them.
