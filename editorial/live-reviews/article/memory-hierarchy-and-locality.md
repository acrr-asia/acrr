# Live review: The Memory Hierarchy and Locality

- URL: https://acrr.asia/blog/memory-hierarchy-and-locality
- Source: `src/content/blog/memory-hierarchy-and-locality.mdx` (Parallel and High-Performance Computing, entry 2)
- Commit deployed: `7e20c2c` (no change to the source since)
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40129647345 (2026-10-24 20:29 UTC): 40 desktop-light, 69 mobile-light, 69 mobile-dark tiles (dark tiles read where they hold the cache-lookup diagram, tables and code)
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-30. The reviewer did not write or revise this article.
- Risk: routine (a technical tutorial; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Accept with follow-up. No critical or major finding; one minor finding (L1) stays open.

**Library decision: retain.** The entry turns the B and I of the roofline into something a programmer can change: it measures the hierarchy of the reference machine (latency plateaus, huge pages, prefetching, STREAM-style bandwidth), explains cache organization, and counts misses exactly with a small simulator whose every number is then derived by hand. Loop order, blocking and layout are each measured and explained. No other ACRR page covers this, and the later entries rely on it. It is long (49 min) but every section serves the central question.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: a programmer who knows C and Python, has read entry 1 (the roofline and honest measurement) and wants to know why the same loop can move eight times as many bytes when written differently.
- Problem: predicting and reducing the bytes a loop moves through the memory hierarchy.
- Outcome: read cache parameters, compute set indices and classify misses as compulsory, capacity or conflict; choose loop order, tile size and data layout; recognize power-of-two conflicts and pad them away; measure latency and sustainable bandwidth and relate them by Little's law.
- Distinctive contribution: an exact miss-counting simulator that the reader can run, with every count (512, 3584, 33 792, 6144, the unpadded blocked case) derived by hand, next to measurements of the same effects on real hardware (a factor of 22 from loop order, 8 times from a power of two, 4.9 from layout).
- Evidence: measured programs with output; the simulator; Wulf and McKee (1995), McCalpin (1995), Patterson (2004), Hennessy and Patterson (2017), Drepper (2007), Bryant and O'Hallaron (2016), Hong and Kung (1981), Lam, Rothberg and Wolf (1991), Goto and van de Geijn (2008), Little (1961), Williams et al. (2009).
- Limitations: one shared virtual machine (L3 behavior and clock hidden, as the text says); exact LRU is a model, not any processor; coherence is left to entry 3.

The benefit is delivered. Spot-checked by computation: N_sets = 49 152/(64 x 12) = 64; the offset 52 and index 8 of 0x7ffd1234; 90.6/13.4 = 6.8; 13.4 x 32/24 = 17.9 GB/s; 17.9 GB/s x 150 ns = 2700 bytes (about 42 lines); 2048/384 = 5.3; and the whole simulator output, re-run from the listing (traversal and matrix-multiply tables, including 3584 conflict misses for n = 64 and 1024 misses for Exercise 2). Exercises 1, 3 and 4 also check out.

Value category: practical implementation. Format: explainer (with measured examples).

Overlap: Section 1 restates the roofline of the insight Compute-Bound or Memory-Bound? The Roofline Idea and of entry 1 and links to both; the blocking intensity b/16 (b/8 with the other tile order) is derived here and cross-referenced from entry 1 (Section 5.2) and entry 4 (T/8 for GPU tiles); the triad measurement is reused in entries 1, 3 and 4 and is labeled consistently (13.4 GB/s, 17.9 with write-allocate). These are deliberate and consistent.

## C. Substantive findings

None.

## D. Visual and structural findings

### L1. Simulator output: the miss breakdown is hidden at desktop width

- Location: Section 3.3 (traversal output) and Section 4.4 (matrix-multiply output); desktop-light tiles of those sections (montage d10 right column, d12 and d13).
- Problem: the printed lines are wider than the code box at 1280 px; each ends at "(compulsory 512, ca" or "(compulsory 1536, ca", so the capacity, conflict and write-back columns that the following paragraphs explain cannot be seen without discovering the sideways scroll.
- Why it matters: the hand derivations below each block refer to those columns (3584 conflict misses, about 30 000 conflict misses for the unpadded blocked loop), and Exercise 2 asks the reader to compare a prediction with the same output. The text restates the key numbers, so nothing is lost, but the reader cannot check them against the table at a glance.
- Required action: shorten the printed label column (for example `n=64 ld=64 col` instead of `n=64  ld=64  column order` padded to 34 characters) so that each line fits at 1280 px; the counts are deterministic, so re-running the simulator after the change reproduces them.
- Priority: minor
- Acceptance condition: at 1280 px every simulator output line is visible to its last column.

Otherwise the layout is clean: the cache-lookup flowchart (Mermaid) is legible in light and dark mode at both widths, the level table, the huge-page table and the summary table fit, and code blocks scroll inside their boxes. Known site-level issues: at 360 px the tile-intensity equation of Section 4.3 is slightly cut and wide code and tables scroll without a cue; the result (b/16) is restated in the text and the summary table, so it is not recorded separately.

## E. Technical and source findings

No technical or source errors found. The GCC report of Section 5.2 is labeled as produced with `-march=sapphirerapids` because the reference machine was no longer available, which is the honest form. `facts.json`: HTTP 200 on all viewports, no horizontal page scroll, no overflowing elements, 0 KaTeX errors, 0 broken images, 0 console errors.

## F. Required changes

Mandatory: none.

Optional:

- [ ] L1: make the simulator output lines fit at 1280 px.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
