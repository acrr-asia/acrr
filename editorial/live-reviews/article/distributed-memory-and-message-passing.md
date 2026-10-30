# Live review: Distributed Memory and Message Passing

- URL: https://acrr.asia/blog/distributed-memory-and-message-passing
- Source: `src/content/blog/distributed-memory-and-message-passing.mdx` (Parallel and High-Performance Computing, entry 5)
- Commit deployed: `7e20c2c` (no change to the source since)
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40129647345 (2026-10-24 20:29 UTC): 35 desktop-light, 63 mobile-light, 63 mobile-dark tiles (dark tiles read where they hold the two diagrams, tables and code)
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-30. The reviewer did not write or revise this article.
- Risk: routine (a technical tutorial; no reporting, named-party claims, safety guidance or commercial relationship; cluster figures are labeled as assumed)

## A. Decision

Accept with follow-up. No critical or major finding; one minor finding (L1) stays open.

**Library decision: retain.** The entry closes the series: MPI point-to-point semantics shown through a real size-dependent deadlock (505 doubles complete, 506 hang), a fitted latency-bandwidth model from a measured ping-pong, collective costs, a halo-exchange Jacobi solver checked bitwise against a serial run, and strong and weak scaling predicted on an assumed cluster. Its stencil links into the Numerical Simulation series (Finite Differences for Heat and Waves, Solving Large Linear Systems), which gives both series a concrete bridge. Nothing else on the site covers message passing.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: a programmer who has read the earlier entries (speedup laws, memory, threads) and needs to run a computation across machines that share no memory.
- Problem: writing correct MPI exchanges and predicting how far a distributed stencil computation scales.
- Outcome: write blocking and nonblocking exchanges that cannot deadlock; fit and use t(m) = α + βm and n_1/2; estimate broadcast, allreduce and barrier costs and choose an algorithm by size; decompose a grid into strips or blocks with ghost cells; predict strong and weak scaling and say which term limits it.
- Distinctive contribution: a measured deadlock threshold explained by the eager limit, a fit that shows one straight line does not describe the machine (two protocols, two lines), and a scaling model whose surface-to-volume argument is checked by the numbers it prints.
- Evidence: measured programs with output (Open MPI 4.1.6 on the reference machine); Python models; Hockney (1994), Culler et al. (1993), Thakur, Rabenseifner and Gropp (2005), Patarasuk and Yuan (2009), Gropp, Lusk and Skjellum (2014), Karp and Flatt (1990), the MPI Forum standards 4.1 and 5.0.
- Limitations: all "messages" are shared-memory copies on one machine; cluster figures are assumed; topology, contention and noise are discussed but not modeled.

The benefit is delivered. Spot-checked by computation: the three fits of Section 3.3 re-run from the ping-pong table (0.423 us and 6.99 GB/s; 0.366 and 2.13; 3.086 and 8.30; worst ratios 2.33 and 1.22); 25 620 B at 4.15 GB/s; the collective table rows for p = 8, 64 and 1024; 2(0.366 + 8/2130) = 0.74 us; S(2) = 1.75, S(4) = 2.98 and 3.52 from the medians; t_c = 1.149 ns; the strong-scaling row p = 4 strips (19.298 ms); the weak-scaling check 0.029733 + 0.970267 x 4096 = 3974.24; and Exercises 1, 3 and 4 (51.2, 42.8 and 21.2 us; S = 1800 and 3630).

Value category: practical implementation. Format: explainer (with measured examples).

Overlap: the Jacobi stencil and its stability condition come from the Numerical Simulation entries Finite Differences for Heat and Waves and Solving Large Linear Systems, which this entry links instead of re-deriving; the Gustafson and Karp-Flatt material is reused from entry 1 and linked. Deliberate and consistent.

## C. Substantive findings

None.

## D. Visual and structural findings

### L1. Fit and comparison output lines cut at desktop width

- Location: Section 3.3, the output of the fit script ("all sizes / m <= 4000 (eager) / m >= 8192", each ending in "measured/mod..."), and Section 5.3, the comparison output (run times lose their "s" or the last digits); desktop-light tiles of those sections (montage d07 and d11).
- Problem: the printed lines are wider than the code box at 1280 px, so the worst measured-to-model ratio of each fit, which the next paragraph discusses (2.33 and 1.22), is hidden.
- Why it matters: small; the paragraph states the values, but the reader cannot see the column it refers to without discovering the sideways scroll.
- Required action: shorten the printed labels (for example "all", "eager", "large") or move the ratio to its own line, so that each line fits at 1280 px; re-run the script so that the shown output stays genuine.
- Priority: minor
- Acceptance condition: every line of both output blocks is visible to its end at 1280 px.

Otherwise the layout is clean: the rendezvous sequence diagram and the ghost-row diagram are legible in light and dark mode at both widths; the summary table fits; code and output blocks scroll inside their boxes. Known site-level issues: at 360 px the strips-and-blocks ratio equation of Section 5.5 and the wide model tables scroll without a cue (results restated in the text). A trivial one: at 360 px a comma after inline math "β" in Section 6.4 wraps to the start of the next line.

## E. Technical and source findings

No technical or source errors found. The statement that Open MPI 4.1.6 implements MPI 3.1 and that the functions used are unchanged in 4.1 is accurate; MPI 5.0 (2025) is cited as the latest version. `facts.json`: HTTP 200 on all viewports, no horizontal page scroll, no overflowing elements, 0 KaTeX errors, 0 broken images, 0 console errors.

## F. Required changes

Mandatory: none.

Optional:

- [ ] L1: make the Section 3.3 and 5.3 output lines fit at 1280 px.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
