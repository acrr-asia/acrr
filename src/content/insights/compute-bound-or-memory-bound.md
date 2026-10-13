---
title: "Compute-Bound or Memory-Bound? The Roofline Idea"
description: "Learn how the roofline model combines arithmetic throughput and memory bandwidth into one performance bound and shows which resource is worth optimizing."
publishedAt: 2026-10-05
kind: "Concept explanation"
tags:
  - performance
  - parallel-computing
  - engineering
---

Before optimizing a numerical kernel, it helps to know which resource limits it: the processor's arithmetic or the delivery of data from memory. Effort spent on the wrong one changes nothing. This note explains the roofline model, a simple bound that answers that question from two machine figures and one property of the code, and where the answer stops being reliable.

## Established

A kernel's speed is limited either by how fast the processor can do arithmetic or by how fast data can reach it. The **roofline model** of Williams, Waterman and Patterson (*Communications of the ACM*, vol. 52, no. 4, pp. 65–76, 2009) states this as an upper bound: $P \le \min(P_{\mathrm{peak}},\, B\,I)$. Here $P$ is the attainable performance, $P_{\mathrm{peak}}$ is peak arithmetic throughput, $B$ is sustainable memory bandwidth, and $I$ is the **arithmetic intensity**, the number of operations performed per byte moved between main memory and the processor.

The two limits meet at the ridge point $I^* = P_{\mathrm{peak}}/B$. Below it a kernel cannot exceed the bandwidth limit; above it the arithmetic limit applies. The bound is not a prediction: latency, poor vectorization or load imbalance can keep real code well below it.

Take a hypothetical machine with $P_{\mathrm{peak}} = 1000$ giga floating-point operations per second (GFLOP/s) and $B = 100$ gigabytes per second (GB/s), so $I^* = 10$ floating-point operations (FLOP) per byte. The update $y \leftarrow y + a x$ on double-precision vectors does 2 operations per element. If each operand crosses the memory interface once (vectors much larger than the cache, so nothing is reused between sweeps), it moves 24 bytes per element: read $x$, read $y$, write $y$. Then $I = 2/24 \approx 0.083$ FLOP/byte and $B\,I \approx 8.3$ GFLOP/s, about 1/120 of peak.

## Interpretation

The model works as a triage tool: compute $I$, compare it with $I^*$, then choose where to spend effort. In the example, doubling arithmetic throughput leaves the bound at 8.3 GFLOP/s, while doubling bandwidth doubles it. Vectorization work would probably be wasted; the productive direction is moving fewer bytes, for instance by fusing loops over the same data. Conversely, a kernel with $I$ well above $I^*$ and measured performance far below the roof suggests looking beyond bandwidth, for example at instruction mix or load imbalance, or at memory traffic larger than the idealized byte count.

Intensity belongs to the algorithm and its data layout as much as to the machine, and $I^*$ differs between machines, so one program can be memory-bound on one and compute-bound on another. Operation counts alone, such as the flop counts used to compare linear solvers in [Solving Large Linear Systems](/blog/solving-large-linear-systems#7-direct-or-iterative), bound only the arithmetic side; the roofline adds the data side, which for sparse matrices with few operations per stored entry is often the one that binds.

## Open questions

- How well do one peak figure and one bandwidth figure describe machines with several cache levels, mixed instruction types, or accelerators?
- For irregular access, such as sparse or pointer-based structures, can $I$ be defined without running the code, since the bytes moved depend on cache behavior and the input?
- If a kernel is limited by memory latency rather than bandwidth, this triage would mislead. How can that case be told apart cheaply from measurements?
