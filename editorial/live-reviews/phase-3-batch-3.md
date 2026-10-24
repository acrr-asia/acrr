# Phase 3, batch 3: robotics, motion planning and embedded systems

Library audit combined with the first live review (adoption plan, Phase 3). Recommendations only: no page was edited, merged or retired.

- Pages: Introduction to Robotics, Motion Planning and Embedded and Real-Time Systems (15 pages).
- Captures: https://acrr.asia at `7e20c2c`, run https://github.com/acrr-asia/acrr/actions/runs/40087219510 (2026-10-24 10:51 UTC); phone dark-mode tiles read only where they hold a figure, table, code or equation.
- Reviewers: three independent live-review passes, interrupted twice by the usage limit; every tile a finding cites was viewed after the interruption. Every deterministic program was re-run and every worked number recomputed; no technical error was found on any page.

## Decisions

| Page | Live-review decision | Library decision | Critical / major / minor |
|---|---|---|---|
| article/coordinate-frames-and-transformations | revision requested | retain and update | 0 / 1 / 1 |
| article/planar-arm-kinematics | revision requested | retain and update | 0 / 1 / 1 |
| article/sensing-and-state-estimation | revision requested | retain and update | 0 / 1 / 0 |
| article/trajectories-and-time-scaling | revision requested | retain and update | 0 / 2 / 2 |
| series/introduction-to-robotics | accepted with follow-up | retain | 0 / 0 / 2 |
| article/configuration-space-and-the-planning-problem | accepted with follow-up | retain | 0 / 0 / 1 |
| article/graph-search-dijkstra-and-a-star | accepted with follow-up | retain | 0 / 0 / 3 |
| article/sampling-based-planning-prm-and-rrt | revision requested | retain and update | 0 / 1 / 2 |
| article/path-tracking-and-reactive-avoidance | accepted with follow-up | retain | 0 / 0 / 1 |
| series/motion-planning | accepted | retain | 0 / 0 / 0 |
| article/interrupts-polling-and-dma | accepted with follow-up | retain | 0 / 0 / 3 |
| article/real-time-operating-systems-and-scheduling | accepted with follow-up | retain | 0 / 0 / 2 |
| article/serial-buses-uart-spi-i2c-and-can | revision requested | retain and update | 0 / 1 / 3 |
| article/measuring-timing-latency-and-resource-use | accepted with follow-up | retain | 0 / 0 / 3 |
| series/embedded-and-real-time-systems | accepted with follow-up | retain | 0 / 0 / 1 |

All routine risk. No merge, reclassification or retirement is recommended.

## The eight major findings

- **Cut equations that hide a result** (five pages): coordinate-frames (the second product of 3.2, the point of the section, cut on desktop), sensing-and-state-estimation (the fused variance P = 0.066 hidden at 1280 px), trajectories (spline recurrence, end condition and stretch factor cut at 1280 px), planar-arm-kinematics and serial-buses (results cut at 360 px; serial-buses shows "= 5" instead of 5.26 %). Fix as in dft-and-fft: break the equations over lines. sensing-and-state-estimation: calibration-and-multisensor-fusion links to its section headings by fragment, so a revision must keep the heading text.
- **No figure where the argument is visual** (two pages): trajectories-and-time-scaling has no figure at all (velocity profiles and the phase-plane argument only in prose and program output); sampling-based-planning never draws a roadmap or a tree. Both reviewers asked for figures built from the articles' own programs (standards 6.8). San may judge a missing figure optional when the text is clear; then both become minor and the pages can be accepted.

## Content and typography points (minor)

- Possessives after inline maths or an asterisk render with an opening quotation mark: "A*‘s", "RRT*‘s", "τ3‘s" and five more in the RTOS article. The smart-quote step turns `'` after a non-letter into ‘; a site-level fix is better than editing each page (see also batch 1's `”+”`).
- serial-buses-uart-spi-i2c-and-can repeats the CAN material of fieldbuses-and-industrial-ethernet (Sections 2.3 and 4) with no link either way: cross-links recommended, not a merge.
- trajectories-and-time-scaling says readers can rerun the programs, but helpers are omitted from the listings (the 1.818 s time-optimal result could not be recomputed for that reason).
- Introduction to Robotics does not link to Motion Planning, which says it continues it; serial commas in two of its objectives.
- Series card descriptions written as "How ..." fragments (embedded entries 2 to 5), as in batch 1 (sensor systems).
- Unlabelled Mermaid diagrams (no caption) on most embedded pages; overlapping labels in the path-tracking layers diagram.

## Overlap noticed (complementary, linked unless stated)

- CAN: serial-buses and fieldbuses-and-industrial-ethernet (not linked; recorded as a finding).
- Inverse-variance weighting, complementary filter, Kalman: sensing-and-state-estimation, calibration-and-multisensor-fusion, state-feedback-controller-design (observer).
- Visibility graph and Minkowski inflation: motion-planning entries 1 and 2; D* Lite: entries 2 and 5; clearance bound D: entries 1 and 3; occupancy grid: shared with sensing-and-state-estimation.
- Jacobian and motion bound: planar-arm-kinematics, coordinate-frames, configuration-space, trajectories.
- Davis et al. CAN response-time remark: RTOS article and fieldbuses.
