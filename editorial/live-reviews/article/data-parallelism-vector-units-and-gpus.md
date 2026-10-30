# Live review: Data Parallelism: Vector Units and GPUs

- URL: https://acrr.asia/blog/data-parallelism-vector-units-and-gpus
- Source: `src/content/blog/data-parallelism-vector-units-and-gpus.mdx` (Parallel and High-Performance Computing, entry 4)
- Commit deployed: `7e20c2c` (no change to the source since)
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40129647345 (2026-10-24 20:29 UTC): 30 desktop-light, 57 mobile-light, 57 mobile-dark tiles (dark tiles read where they hold the GPU hierarchy diagram and code)
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-30. The reviewer did not write or revise this article.
- Risk: routine (a technical tutorial; no reporting, named-party claims, safety guidance or commercial relationship; GPU figures are labeled as assumed)

## A. Decision

Accept with follow-up. No critical or major finding; two minor findings (L1, L2) stay open.

**Library decision: retain.** The entry covers what no other ACRR page does: CPU vector units measured on the reference machine, the GPU execution and memory model, and a cost model for when offloading pays. It is honest about its limits (the machine has no GPU; every GPU listing is labeled as an illustration that was not compiled or run, and every GPU figure as assumed), and it connects each half to the roofline of entry 1 and the layouts of entry 2. The 16 October review findings were resolved before publication.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: a programmer who has read entries 1 to 3 and wants to know what vector instructions and GPUs can do for a numerical loop.
- Problem: predicting whether a loop gains from vectorization or from a GPU, and why.
- Outcome: read compiler vectorization reports; recognize dependences, aliasing, branches, strides and ordered reductions as blockers; explain warps, occupancy, coalescing and shared-memory tiling; estimate with a roofline-style model whether moving a computation to a GPU repays the transfer.
- Distinctive contribution: one roofline argument carried through CPU lanes, GPU memory and the host link, with the measured CPU half (3.6 times for a compute-bound loop, 1.4 to 1.6 for axpy, nothing more from 512-bit vectors) and a break-even size for offloading derived in closed form and checked by a script.
- Evidence: measured kernels with compiler reports and disassembly; `offload.py` with its output; Flynn (1966, 1972), Hennessy and Patterson (2017), Hwu, Kirk and El Hajj (2022), Intel (2024), Lindholm et al. (2008), Little (1961), OpenMP 5.2, the GCC manual.
- Limitations: no GPU measurement; assumed machine figures; vendor-specific vocabulary (CUDA); FP64 throughput left to product documentation.

The benefit is delivered. Every section serves the question; the summary table answers it in question-and-answer form. Spot-checked by computation: 28.40/7.79 = 3.6 and 30.14/7.79 = 3.9; 22.3 x 0.083 = 1.86; 0.237/0.051 = 4.6; 1000 GB/s x 0.5 us = 5 x 10^5 bytes (62 500 loads); 65 536/64 = 1024 threads, 32 warps, 50%; the offload table rows for axpy n = 10^6 and matmul n = 128; the break-even n > 12/(25e9 x 1.9e-12) = 252.6 and n/12 = 21.1 FLOP/byte; Exercises 3, 5 (5 s, 0.54 s, 40.5 s) and 6 (4 FLOP/byte, 16 KiB). Reading effort (37 min) is justified.

Value category: conceptual understanding. Format: explainer.

Overlap: Section 2.3's axpy bandwidth discussion and Section 6's roofline-on-the-link argument build on the insight Compute-Bound or Memory-Bound? The Roofline Idea and on entry 1, and say so; the floating-point reassociation of Section 2.5 links to the insight on floating-point rounding rather than repeating it. No harmful overlap.

## C. Substantive findings

None.

## D. Visual and structural findings

### L1. Break-even result cut off in Section 6.2

- Location: Section 6.2, the display equation "n > 12 / (B_link (1/P_cpu - 1/P_gpu)) = ... ≈ 252.6"; desktop-light (montage d12, right column) and mobile-light (montage g12).
- Problem: at 1280 px the equation ends at "≈ 25", with "2.6" hidden; at 360 px only "= 25 ×" is visible. The box scrolls sideways, without a cue.
- Why it matters: the number is the section's result. The next sentence restates it ("the program's search, n = 253"), so the reader is not misled, but the equation itself reads as a wrong value at desktop width, where the site-level issue is not expected.
- Required action: split the equation (for example the general form on one line and "= 12 / (25 x 10^9 x 1.9 x 10^-12) ≈ 252.6" on the next, in an `aligned` block).
- Priority: minor
- Acceptance condition: at 1280 px the whole equation, including 252.6, is visible; at 360 px no line hides the result.

### L2. Opening quotation mark rendered as a closing one before inline math

- Location: Section 1.1, "(called **axpy**, for "a times x plus y")"; desktop-light (montage d02) and mobile-light (montage g02).
- Problem: the page shows ”a times x plus y” with a closing curly quote at the start. The source uses a straight `"` directly before `$a$`, and the typographer chooses the closing form when the next character is math.
- Why it matters: a visible typographic slip in the first paragraph.
- Required action: write the opening quote as “ in the source (or restructure the phrase); the same pattern affects the "+" node in entry 1 (performance-models-and-scaling-laws L1), so a site-wide search for a straight quote followed by `$` or a symbol is worth doing once.
- Priority: minor
- Acceptance condition: the phrase renders with an opening “ at the start.

Otherwise the layout is clean: the register-width table, the offload output and the summary table read well; code and output blocks scroll inside their boxes; the GPU hierarchy flowchart is legible in light and dark mode. Known site-level issue: at 360 px the flowchart's last two nodes ("Warps", "Threads") are off-screen without a scroll cue, and the T_gpu equation of Section 6.1 is cut; not recorded separately.

## E. Technical and source findings

No technical or source errors found. GPU listings and figures are labeled as illustrations or assumptions throughout, as the content-integrity rules require. `facts.json`: HTTP 200 on all viewports, no horizontal page scroll, no overflowing elements, 0 KaTeX errors, 0 broken images, 0 console errors.

## F. Required changes

Mandatory: none.

Optional:

- [ ] L1: split the Section 6.2 break-even equation.
- [ ] L2: fix the opening quote before "a times x plus y".

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
