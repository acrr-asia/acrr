# Live review: Threads and Shared-Memory Parallelism

- URL: https://acrr.asia/blog/threads-and-shared-memory-parallelism
- Source: `src/content/blog/threads-and-shared-memory-parallelism.mdx` (Parallel and High-Performance Computing, entry 3)
- Commit deployed: `7e20c2c` (no change to the source since)
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40129647345 (2026-10-24 20:29 UTC): 35 desktop-light, 65 mobile-light, 65 mobile-dark tiles (dark tiles read where they hold the fork-join diagram, tables or code)
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-30. The reviewer did not write or revise this article.
- Risk: routine (a technical tutorial; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Accept with follow-up. No critical or major finding; one minor finding (L1) stays open.

**Library decision: retain.** The entry is the series' only treatment of shared-memory programming, and it does what few introductions do: every claim about races, memory ordering, synchronization cost, false sharing and scheduling is backed by a program and its measured output on the series' reference machine, and the measurements are tied back to the models of entry 1 (Amdahl, work and span, roofline). Nothing on the site duplicates it, and the 16 October review findings (OpenMP version wording) are applied.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: a programmer who writes C, has read entries 1 and 2 of the series (speedup, roofline, cache lines) and wants to use several cores on one problem.
- Problem: making a loop faster on several cores without making it wrong, and knowing why a correct parallel loop can still be slow.
- Outcome: use `parallel`, `for`, the data-sharing clauses and `reduction`; recognize and remove a data race; explain what x86 TSO and C11 release/acquire guarantee; estimate barrier, lock and false-sharing costs; choose a schedule for an uneven loop.
- Distinctive contribution: each failure mode is shown happening (lost increments, a hung spin loop, 235 183 store-buffering reorderings in 10^6 trials, a 21-fold false-sharing penalty, a 2.27 static-schedule speedup against the 2.29 bound) and then removed.
- Evidence: measured programs with their output; ISO/IEC 9899:2018, OpenMP 5.2, Lamport (1979), Adve and Gharachorloo (1996), Sewell et al. (2010), Hennessy and Patterson (2017), Little (1961), McCalpin (1995), Williams et al. (2009).
- Limitations: one x86 machine, so weak-memory hardware is described but not measured; OpenMP tasks and locks beyond `critical` are out of scope; vectors and GPUs are left to entry 4.

The benefit is delivered. Every section serves the central question; the summary table restates each result in one row, and the five exercises check the main skills. Spot-checked by computation: Exercise 1 (4.71, 8, 6.7), Exercise 2 (15/64, 4.27, 0.53), 0.264 s and 1.20 s over 5 x 10^6 increments (53 and 240 ns), 0.85 us at 2.1 and 2.8 GHz (about 1800 and 2400 cycles), 2.081 us at 1.37 GFLOP/s (about 2900 FLOP), 122.56/5.81 = 21, the static shares 1/16 and 7/16 of 0.3711 s (0.023 and 0.162 s), and 16/7 = 2.29. Reading effort (42 min) is justified.

Value category: practical implementation. Format: explainer (with measured examples).

Overlap: Exercise 4 (`volatile` is not synchronization) touches the same point as the embedded article Interrupts, Polling and DMA, from the other side (there `volatile` is required for memory-mapped registers and interrupt flags); the two do not contradict each other and need no change, but the overlap map should record it. The triad scaling (Section 2.4) repeats the bandwidth measurement of entry 2 (Section 6.3) on purpose and says so.

## C. Substantive findings

None.

## D. Visual and structural findings

### L1. Litmus-test output: the last outcome column is hidden at desktop width

- Location: Section 4.3 and 4.4, the two output blocks of `litmus.c` ("SB relaxed / SB seq_cst" and "MP relaxed / MP release/acquire"); desktop-light tiles of Section 4.3 to 4.4 (montage d10 and d11).
- Problem: the lines are wider than the code box at 1280 px; the count for the outcome "1,1" is cut after its first digit, so the four outcomes visibly do not add up to 10^6.
- Why it matters: small; the prose quotes the outcome that matters (235 183, and 0 for the stale message), but a reader checking the table cannot see the full row without discovering the sideways scroll.
- Required action: print the four counts on two lines, or drop the repeated "r0,r1 =" label so that each line fits the box at 1280 px. Changing the program output means re-running it or reformatting the printed lines consistently.
- Priority: minor
- Acceptance condition: all four counts of each litmus line visible at 1280 px.

Otherwise the layout is clean on both viewports: the fork-join flowchart is legible in light and dark mode, the race-interleaving and summary tables fit at 360 px (the race table relies on the known 7rem cell minimum and scrolls), and code blocks scroll inside their boxes. Known site-level issues: the display bound `T_p >= max(T1/p, f T1), S(p) <= min(p, 1/f)` of Section 5.2 is cut at 360 px (no scroll cue); the result is restated in the next paragraph and the summary table, so it is not recorded separately.

## E. Technical and source findings

No technical or source errors found. The OpenMP version statement (5.2 cited, 6.0 noted, GCC 13 reporting 201511) is accurate as worded. `facts.json`: HTTP 200 on all viewports, no horizontal page scroll, no overflowing elements, 0 KaTeX errors, 0 broken images, 0 console errors.

## F. Required changes

Mandatory: none.

Optional:

- [ ] L1: make the litmus output lines fit at 1280 px.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
