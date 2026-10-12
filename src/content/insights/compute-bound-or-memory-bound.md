---
title: "Compute-Bound or Memory-Bound? The Roofline Idea"
description: "A short concept explanation of the roofline idea: how arithmetic throughput and memory bandwidth together bound performance, and what that implies for choosing what to optimise."
publishedAt: 2026-10-05
kind: "Concept explanation"
tags:
  - performance
  - parallel-computing
  - engineering
example: true
---

*This is an illustrative example insight, not a research result, and the machine numbers below are hypothetical.*

## Established

A kernel's speed is limited either by how fast the processor can do arithmetic or by how fast data can reach it. The roofline model states this as an upper bound: $P \le \min(P_{\mathrm{peak}},\, B\,I)$. Here $P_{\mathrm{peak}}$ is peak arithmetic throughput, $B$ is sustainable memory bandwidth, and $I$ is arithmetic intensity, the operations performed per byte moved between main memory and the processor.

The two limits meet at the ridge point $I^* = P_{\mathrm{peak}}/B$. Below it a kernel cannot exceed the bandwidth limit; above it the arithmetic limit applies. The bound is not a prediction: latency, poor vectorization or load imbalance can keep real code well below it.

Hypothetical machine: $P_{\mathrm{peak}} = 1000$ GFLOP/s and $B = 100$ GB/s, so $I^* = 10$ FLOP/byte. The update $y \leftarrow y + a x$ on double-precision vectors does 2 operations per element. If each operand crosses the memory interface once (vectors much larger than the cache, so nothing is reused between sweeps), it moves 24 bytes per element: read $x$, read $y$, write $y$. Then $I = 2/24 \approx 0.083$ FLOP/byte and $B\,I \approx 8.3$ GFLOP/s, about 1/120 of peak.

## Interpretation

The model works as a triage tool: compute $I$, compare it with $I^*$, then choose where to spend effort. In the example, doubling arithmetic throughput leaves the bound at 8.3 GFLOP/s, while doubling bandwidth doubles it. Vectorization work would probably be wasted; the productive direction is moving fewer bytes, for instance by fusing loops over the same data. Conversely, a kernel with $I$ well above $I^*$ and measured performance far below the roof suggests looking beyond bandwidth, for example at instruction mix or load imbalance, or at memory traffic larger than the idealised byte count.

Intensity belongs to the algorithm and its data layout as much as to the machine, and $I^*$ differs between machines, so one program can be memory-bound on one and compute-bound on another.

## Open questions

- How well do one peak figure and one bandwidth figure describe machines with several cache levels, mixed instruction types, or accelerators?
- For irregular access, such as sparse or pointer-based structures, can $I$ be defined without running the code, since the bytes moved depend on cache behaviour and the input?
- If a kernel is limited by memory latency rather than bandwidth, this triage would mislead. How can that case be told apart cheaply from measurements?
