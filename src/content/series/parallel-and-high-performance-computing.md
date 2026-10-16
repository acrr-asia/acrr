---
title: "Parallel and High-Performance Computing"
description: "A five-entry course on making computations faster with parallel hardware, from performance models and caches to threads, vector units, GPUs and message passing."
category: "Computing Systems"
status: "published"
objectives:
  - "Compute speedup, efficiency and the Amdahl and Gustafson bounds for a program, and use the roofline bound to decide whether a kernel is limited by arithmetic or by memory traffic."
  - "Explain how caches exploit locality, and restructure a loop nest or a data layout to reduce the number of cache misses it causes."
  - "Write a correct shared-memory parallel loop, and identify and remove data races, false sharing and load imbalance in one."
  - "Explain how vector units and GPUs execute data-parallel code, and estimate when offloading a computation to an accelerator pays for its data transfer."
  - "Predict the communication cost of a message-passing program with the latency-bandwidth model, and use it to estimate strong and weak scaling."
---

This series is for engineers and students who write numerical or data-processing code and want it to run faster on the parallel hardware they already have: a multicore laptop, a workstation with a graphics processor, or a cluster. It assumes the reader can read C and Python and knows what a loop, an array and a function call cost in ordinary sequential code; the [Numerical Simulation for Engineers](/series/numerical-simulation) series supplies the kinds of computation (sparse linear systems, stencils on grids) used as examples, and the insight [Compute-Bound or Memory-Bound?](/insights/compute-bound-or-memory-bound) introduces the roofline idea that the first entry develops.

The order follows the question a performance engineer asks first, then the hardware from the inside out. The first entry sets up the measures and models (speedup, efficiency, the laws of Amdahl and Gustafson, work and span, the roofline bound) that every later entry uses to judge a result. Most programs are limited by memory before they are limited by arithmetic, so the second entry treats the memory hierarchy and the locality that caches reward. The third entry adds threads that share one memory, with the races, synchronization costs and false sharing that come with them. The fourth goes down to the data parallelism inside a core, in vector instructions, and out to the thousands of lanes of a graphics processor. The fifth leaves shared memory altogether: processes on separate nodes that cooperate only by sending messages, and the communication cost that then decides how far a program scales.

All entries share a few conventions. Times are wall-clock times in seconds unless stated otherwise; "speedup" always compares with the best sequential program, not with the parallel program run on one processor. Data are double-precision (8-byte) floating-point numbers unless stated otherwise, and arrays in C are stored in row-major order. The code uses C11 compiled with GCC 13, OpenMP for threads and Open MPI 4.1 for message passing, with Python 3 for the models. Measured timings come from one stated machine, a four-core virtual machine, and describe that machine only; numbers for other hardware are labeled as assumed.
