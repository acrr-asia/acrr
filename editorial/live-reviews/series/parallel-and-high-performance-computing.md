# Live review: Parallel and High-Performance Computing (series overview)

- URL: https://acrr.asia/series/parallel-and-high-performance-computing
- Source: `src/content/series/parallel-and-high-performance-computing.md` (five entries, status published, no planned entries)
- Commit deployed: `7e20c2c` (no change to the source since)
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40129647345 (2026-10-24 20:29 UTC): 4 desktop-light, 7 mobile-light, 7 mobile-dark tiles (the page has no figure, table, code or equation, so no dark tile needed close reading)
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-30. The reviewer did not write or revise this page.
- Risk: routine (a series front door for technical tutorials; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Accept. The overview meets the series-page requirements, every statement on it was checked against the entries, and no finding is open.

**Library decision: retain.** The page is the series' entry point. Its three paragraphs give the reader and the prerequisites (with links to the series Numerical Simulation for Engineers and to the roofline insight), a sequence rationale (measures and models first, then the hardware from the inside out: caches, threads, vector units and GPUs, message passing) and the conventions all five entries share. The five objectives map one to one onto the entries. Nothing on the page needs to change.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineer or student who writes numerical or data-processing code in C or Python and is deciding whether and where to start the series.
- Problem: knowing what the five entries cover, why in this order, what they assume and which conventions they share.
- Outcome: the reader knows the prerequisites (linked), the order and its reason, the shared conventions (wall-clock seconds, speedup against the best sequential program, 8-byte doubles, row-major C, GCC 13.3, OpenMP 5.2, Open MPI 4.1.6, Python 3.13 and NumPy 2.5, one four-core virtual machine, other hardware labeled as assumed) and five checkable objectives.
- Distinctive contribution: it states the dependency chain and a measurement policy (one stated machine; everything else assumed and labeled) that every entry follows.
- Evidence: the entries. Checked in this review: the conventions appear in each entry's opening (entry 1 defines T_1 as the best sequential program, entry 3 obtains T_1 without OpenMP, entry 4 labels every GPU figure as assumed, entry 5 labels the cluster as assumed); the toolchain versions match the entries' convention paragraphs; each objective is the subject of one entry; the five cards' reading times (45, 49, 42, 37 and 41 min) match the article pages.
- Limitations: an overview; the total reading time (214 minutes from the card estimates) is not stated.

The benefit is delivered. The first screen gives the title, a one-sentence description, the category, the Published status, "Start with entry 1" and the start of the reader paragraph; the progress bar shows 5 of 5. At 360 px everything stacks in reading order (description, objectives, progress, entries) and nothing is cut.

Value category: reference value. Format: reference.

Overlap: the series uses the numerical-simulation series as its source of workloads (entry 4 links to Solving Large Linear Systems, entry 5 to it and to Finite Differences for Heat and Waves) and the insight Compute-Bound or Memory-Bound? The Roofline Idea as its starting point; both are linked from the overview. The overlap map should record the insight and entry 1 as a short and a long treatment of the roofline.

## C. Substantive findings

None.

## D. Visual and structural findings

None. Layout, cards, progress bar and objectives render correctly at 1280 and 360 px.

## E. Technical and source findings

None. `facts.json`: HTTP 200 on all viewports, no horizontal page scroll, no overflowing elements, 0 broken images, 0 console errors.

## F. Required changes

Mandatory: none.

Optional: none.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| (none) | | | |
