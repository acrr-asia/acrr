# Live review: Performance Models: Speedup, Scaling Laws and the Roofline

- URL: https://acrr.asia/blog/performance-models-and-scaling-laws
- Source: `src/content/blog/performance-models-and-scaling-laws.mdx` (Parallel and High-Performance Computing, entry 1)
- Commit deployed: `7e20c2c` (no change to the source since)
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40129647345 (2026-10-24 20:29 UTC): 36 desktop-light, 65 mobile-light, 65 mobile-dark tiles (dark tiles read where they hold the reduction-tree diagram, tables and code)
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-30. The reviewer did not write or revise this article.
- Risk: routine (a technical tutorial; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Accept with follow-up. No critical or major finding; one minor finding (L1) stays open.

**Library decision: retain.** The entry is the series' foundation: speedup and efficiency, Amdahl and Gustafson, overheads and the Karp-Flatt metric, work and span with Brent's bound, the roofline with measured peak and bandwidth, and a section on honest measurement. Later entries cite its sections by number. It overlaps with the insight Compute-Bound or Memory-Bound? The Roofline Idea, but the insight is a short decision aid and this entry derives the model and measures its two roofs, so both should stay (the overlap map should record the pair).

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineer or student who writes numerical code and wants to know, before and after parallelizing, how fast it can become.
- Problem: predicting and honestly reporting the speedup of a parallel program, and finding which resource bounds it.
- Outcome: compute Amdahl, Gustafson and overhead-model bounds and the Karp-Flatt fraction; bound a computation by work and span; place a kernel on a measured roofline; time a kernel with a monotonic clock, warm-up, repetitions and a stated baseline.
- Distinctive contribution: every model is evaluated with numbers from one reference machine (about 354 GFLOP/s on four cores and 90.6 on one, about 50 GB/s, a ridge near 7 FLOP/byte, all labeled as estimates) and ends in a reporting checklist that the later entries follow.
- Evidence: derivations; programs with their output; Amdahl (1967), Gustafson (1988), Karp and Flatt (1990), Brent (1974), Graham (1966), Williams et al. (2009), McCalpin (1995), Hoefler and Belli (2015), Hennessy and Patterson (2017), POSIX and OpenMP 5.2.
- Limitations: one shared virtual machine; network and memory-hierarchy effects are deferred to entries 2 and 5.

The benefit is delivered. Each section serves the central question; the summary table and the closing paragraph tie the models to one conclusion. Spot-checked by computation: the overhead table (S = 9.04 at p = 31, p* = 30.82), 12.55 at p = 32, the Karp-Flatt values 0.0526, 0.0588 and 0.0612 (and 0.083 in the exercise), Exercise 1 (19.75, 0.62), Exercise 5 (0.167 FLOP/byte, 8.33 GFLOP/s, 2.4% of 354), the ridge 7.08 and the inferred clocks of 2.77 and 2.83 GHz. Reading effort is justified.

Value category: conceptual understanding. Format: explainer.

Overlap: the insight Compute-Bound or Memory-Bound? The Roofline Idea (see above); the floating-point consequence of reordered sums links to the insight Floating-Point Rounding in Long Simulations instead of repeating it.

## C. Substantive findings

None.

## D. Visual and structural findings

### L1. Opening quotation mark rendered as a closing one after the reduction tree

- Location: Section 4.3, the sentence after the reduction-tree diagram, "Each "+" node is one addition"; desktop-light tile after the Mermaid tree.
- Problem: the page shows `Each ”+” node` with two closing curly quotes. The source has straight quotes around `+`; the typographer treats the first one as closing because a symbol follows it.
- Why it matters: a visible typographic slip next to the section's figure.
- Required action: write “+” in the source, or name the node another way ("Each addition node"). The same pattern affects entry 4 (data-parallelism-vector-units-and-gpus L2).
- Priority: minor
- Acceptance condition: the phrase renders with an opening and a closing quote.

Otherwise the layout is clean: the reduction tree (Mermaid) is legible in light and dark mode, the overhead and summary tables are readable (at 360 px the three-column summary table scrolls, as the 7rem cell minimum makes it), and code and output blocks scroll inside their boxes. Known site-level issue: at 360 px the display equations for lim S(p) (Section 2.1) and S_s(p) = ... = p - f_s(p - 1) (Section 3.1) are cut without a scroll cue; both results are restated in the text and the summary table, so they are not recorded separately.

## E. Technical and source findings

No technical or source errors found; the 16 October finding on OpenMP reductions (not specified as tree combines) is resolved in the text. `facts.json`: HTTP 200 on all viewports, no horizontal page scroll, no overflowing elements, 0 KaTeX errors, 0 broken images, 0 console errors.

## F. Required changes

Mandatory: none.

Optional:

- [ ] L1: fix the quotation marks around "+" in Section 4.3.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
