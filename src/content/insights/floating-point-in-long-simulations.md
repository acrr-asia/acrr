---
title: "Floating-Point Rounding in Long Simulations"
description: "A short methodological note on how finite precision, summation order and accumulated rounding error can matter in simulations that run for many steps."
publishedAt: 2026-10-07
kind: "Methodological note"
tags:
  - numerical-methods
  - simulation
  - verification
---

## Established

Computers store real numbers with finite precision, so most arithmetic results are rounded. In IEEE 754 round-to-nearest arithmetic, the unit roundoff $u$ is $2^{-24} \approx 6\times10^{-8}$ for binary32 ("single") and $2^{-53} \approx 1.1\times10^{-16}$ for binary64 ("double"). Each basic operation returns the correctly rounded result, so its relative error is at most $u$, barring overflow and underflow.

Floating-point addition is commutative but not associative: $(a+b)+c$ and $a+(b+c)$ can differ. In double precision, $(10^{16}+1)+1$ evaluates to $10^{16}$, while $10^{16}+(1+1)$ evaluates to $10^{16}+2$. Summation order can therefore change results, and a parallel reduction whose order varies between runs can change them from run to run.

Rounding errors accumulate. For plain recursive summation of $n$ terms, the standard worst-case error bound is about $n\,u$ times the sum of the absolute values of the terms. For a hypothetical $10^6$ terms, $n\,u$ is about $0.06$ in single precision and about $10^{-10}$ in double. These are bounds, and actual errors are usually much smaller. A single-precision counter incremented by 1 stops changing at $2^{24} = 16777216$.

## Interpretation

One reading is that rounding is usually a secondary error in a short run, but deserves a check as the number of operations grows. A check seems most warranted when the run is very long, when the result is a small difference between large quantities, when the system amplifies small perturbations (as chaotic systems do), or when the result will support a decision.

Two checks follow, and their cost depends on the code. Repeat the run in higher precision, or accumulate sums with a compensated or pairwise method, and compare. Alternatively, reorder the summation and compare. If the differences are well below the discretization error and the stated accuracy target, rounding is unlikely to be the main concern. Agreement is evidence rather than proof, because it only probes the variations that were tried.

## Open questions

- How should the tolerance for such a comparison be chosen? It plausibly depends on the discretization error and on how sensitive the quantity of interest is to perturbations, but no general rule is evident.
- In a chaotic system, trajectories from different summation orders eventually diverge. Which statistics should be compared instead, and how large a difference is acceptable?
- Under what conditions can mixed precision be used without changing the conclusions drawn from a run?
