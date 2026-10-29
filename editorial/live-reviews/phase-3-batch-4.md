# Phase 3, batch 4 (part 1): numerical simulation and industrial automation

Library audit combined with the first live review (adoption plan, Phase 3). Recommendations only: no page was edited, merged or retired.

- Pages: Numerical Simulation (5) and the remaining Industrial Automation entries (3). The six Parallel and High-Performance Computing pages captured in the same run were not finished: the reviewer stopped at the account's weekly usage limit and wrote no report.
- Captures: https://acrr.asia at `7e20c2c`, run https://github.com/acrr-asia/acrr/actions/runs/40129647345 (2026-10-24 20:29 UTC); phone dark-mode tiles read only where they hold a figure, table, code or equation.
- Reviewers: two independent live-review passes. Code blocks re-run and worked numbers recomputed; no technical error found.

## Decisions

| Page | Live-review decision | Library decision | Critical / major / minor |
|---|---|---|---|
| article/finite-differences-for-heat-and-waves | revision requested | retain and update | 0 / 1 / 2 |
| article/finite-element-method | revision requested | retain and update | 0 / 1 / 1 |
| article/solving-large-linear-systems | revision requested | retain and update | 0 / 1 / 1 |
| article/verifying-and-validating-a-simulation | revision requested | retain and update | 0 / 1 / 1 |
| series/numerical-simulation | accepted | retain | 0 / 0 / 0 |
| article/programmable-logic-controllers | in review (high risk: San decides) | retain | 0 / 0 / 4 |
| article/fieldbuses-and-industrial-ethernet | accepted with follow-up | retain and update | 0 / 0 / 3 |
| article/networked-automation-and-digital-twins | in review (high risk: San decides) | retain | 0 / 0 / 3 |

## For San

- **Two more pages classed high risk** because they give safety-relevant guidance: programmable-logic-controllers (do not retain a "motor running" latch, define outputs on CPU stop, keep emergency stops on safety-rated hardware) and networked-automation-and-digital-twins (security architecture for networks that control plant, how much authority a digital twin has over a running process). Neither has a critical or major finding; the reviewer recommends acceptance with follow-up for both. With logic-and-sequential-control, three industrial automation pages now wait for San.
- networked-automation was classed high risk for its operational-technology security guidance, while token-based-authentication (batch 1) was classed routine. San's answer on whether security guidance is high risk settles both.

## Major findings

All four are cut display equations that hide a result, at 1280 px for three pages (the truncation-error expansion and implicit-scheme form in finite differences; the weak form's flux term in the finite element method; the conjugate-gradient search-direction update) and at 360 px for verification and validation (the Richardson extrapolation formula the section is named after).

After four batches, cut display equations are the most common major finding (14 pages so far). A site-level change would help every page at once: a visible scroll cue on wide display equations (as tables have), and a smaller equation size on narrow screens. Breaking equations over lines in each article is still needed where the cut hides a result.

## Content points (minor)

- programmable-logic-controllers: Section 5 says each language shows the same task, but there is no SFC chart; IEC 62061 and ISO 13849-1 are named but missing from the references.
- fieldbuses-and-industrial-ethernet and serial-buses-uart-spi-i2c-and-can repeat the same CAN material with no link either way (also recorded in batch 3).
- networked-automation: the ISA-95 flowchart repeats the table below it.
- solving-large-linear-systems: "A‘s" (opening quotation mark for an apostrophe), the same site-level typography issue as batch 3.

## Overlap noticed

- Numerical Simulation entry 3 and gradient-descent-and-its-variants (condition number, steepest descent): not linked.
- Entry 3 and distributed-memory-and-message-passing (Jacobi iteration), gaussian-processes-and-kernels and scaling-bayesian-deep-learning (Cholesky, conjugate gradients): linked.
- Entry 5 and the insights what-makes-a-simulation-trustworthy and floating-point-in-long-simulations; entry 5 section 4.2 and measurement-systems-and-sensor-characteristics (GUM uncertainty): linked.
- fieldbuses and serial-buses (CAN): not linked.
