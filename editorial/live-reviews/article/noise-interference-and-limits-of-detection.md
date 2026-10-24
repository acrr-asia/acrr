# Live review: Noise, Interference and the Limits of Detection

- URL: https://acrr.asia/blog/noise-interference-and-limits-of-detection
- Source: `src/content/blog/noise-interference-and-limits-of-detection.mdx` (Sensor Systems, entry 5 of 7)
- Commit deployed: `7e20c2c` (master after PR #57)
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40085671258 (captured 2026-10-24 10:26 UTC): 18 desktop-light, 34 mobile-light, 34 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-24. The reviewer did not write or revise this article.
- Risk: routine (a technical explainer; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Accept with follow-up. No critical or major finding; three minor findings remain open (L1 to L3). The contract is delivered and every worked number checked is right.

**Library decision: retain.** The page is the series' only treatment of noise physics, amplifier noise, interference coupling and detection limits, and it ends in a noise budget that the next entries reuse: the calibration entry compares its residual scatter with that budget. Nothing else on ACRR covers this ground. The fixes are presentation and one wording point, not content, so "retain and update" is not needed.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineer or student building a sensor channel who knows basic circuits and statistics and wants to know what limits the smallest change the channel can resolve.
- Problem: telling noise from interference, estimating each noise source, combining them, and knowing which remedy acts on which problem.
- Outcome: compute thermal, shot and 1/f noise and the noise bandwidth of a filter; choose an amplifier for a given source resistance; use averaging and dither within their limits; recognize the four interference coupling paths and their remedies; build a noise budget and state effective resolution, noise-free resolution and a detection limit.
- Distinctive contribution: one channel (the series' load cell, plus the photodiode of entry 2) carried from physics to a complete noise budget, with every number derived on the page and tied back to the converter choice of the previous entry.
- Evidence: derivations and worked numbers on the page; Horowitz and Hill (2015), Motchenbacher and Connelly (1993), Ott (2009), Pallàs-Areny and Webster (2001).
- Limitations: white, shot and 1/f noise only (no popcorn or avalanche noise); interference treated qualitatively with order-of-magnitude examples; no measurement procedure for the budget.

The benefit is delivered. The opening separates noise from interference, Sections 1 to 4 build the tools, Section 5 covers interference, and Section 6 puts the pieces together into the budget and answers the title's question. Each section serves the central question; the summary table and the interference checklist make the page reusable. I recomputed the numbers: thermal noise 4.07 and 2.41 nV/√Hz; kT/C 64.4 µV for 1 pF; shot noise 0.42 pA/√Hz, feedback-resistor noise 0.13 pA/√Hz, 0.22 nA in a 251 kHz noise bandwidth, SNR 2500 (68 dB); 1/f part 67.9 nV, white part 31.5 nV, 74.8 nV together; amplifier terms 10, 0.035 and 2.41 nV/√Hz, total 10.3 nV/√Hz; dither bias 0.093 q at σ = 0.25 q and 0.002 q at σ = 0.5 q (Fourier series of the sawtooth error, first harmonic attenuated by exp(−2π²σ²)); 72.3 nA, 3.18 GΩ, 72 mV and 25.3 µV for capacitive coupling; 3.14 µV peak for the loop; budget 75.2 nV, 0.114 g, 88 000 counts (16.4 bits, 98.9 dB), 13 300 noise-free steps (13.7 bits); 3σ exceeded once in 741 trials. All match the page. The page is worth its reading effort (17 minutes). Value category: conceptual understanding. Format: explainer.

Overlap: the equivalent noise bandwidth idea also appears for windows in "Spectra: The DFT and the FFT" (DSP series), and dither in "Sampling, Quantization and Data Conversion" (the previous entry, which this page cites and builds on). Neither repeats this page's treatment; a cross-link from the ENBW table to the DFT article's window table would help readers of both series (optional).

## C. Substantive findings

### L2. "Nearly five bits of resolution gained" does not state its baseline

- Location: Section 4, paragraph "The dither must be large enough", last sentences; desktop-light-09, mobile-light-18.
- Problem: averaging 256 dithered samples brings the random error to about q/28, and the page calls this "nearly five bits of resolution gained" (log2 28 ≈ 4.8, measured against one step q). Measured the way Section 6.1 defines effective resolution (full scale over RMS error), the single quantized reading already has an RMS error of q/√12 ≈ 0.29 q, so the gain is 0.29/0.036 ≈ 8, three bits. The sentence compares an RMS error with a step size.
- Why it matters: a reader who applies the page's own definition of effective resolution gets three bits, not five, and may doubt either the arithmetic or the definition.
- Required action: name the baseline, for example "about q/28, a random error 28 times smaller than one step (eight times smaller than the q/√12 of a single quantized reading)", or state the gain in the terms of Section 6.1.
- Priority: minor
- Acceptance condition: the sentence states what the gain is measured against, and the figure agrees with that baseline.

## D. Visual and structural findings

### L1. Page scrolls sideways at 360 px (cause found)

- Location: Section 2.2, paragraph "The photodiode of the sensing-principles entry", the inline expression $\sqrt{2 \times 1.602 \times 10^{-19} \times 0.55 \times 10^{-6}} \approx 0.42$; mobile-light-09 and 10 (the "≈" is cut at the right edge).
- Problem: `facts.json` reports a page-level horizontal scroll at 360 px (page width 364 px against a 360 px viewport) on both mobile captures; its list of overflowing blocks is empty because it checks only images, tables, figures, code and display equations. I rebuilt the page at this commit and measured every element at 360 px: the only element wider than the viewport is this inline KaTeX expression. KaTeX cannot break a line inside a square root, so the whole radical stays on one line and pushes past the text column. The other pages in this batch do not scroll.
- Why it matters: the whole page moves sideways under the reader's thumb on a phone, and the end of the expression is cut.
- Required action: move the expression to a display equation, or write it in two steps (for example "$i_n = \sqrt{2qI}$ with $I = 0.55$ µA gives about 0.42 pA/√Hz"), so that no inline expression is wider than about 300 px.
- Priority: minor
- Acceptance condition: on new captures `facts.json` shows `horizontalScroll: false` at 360 px, and the shot-noise sentence is fully visible on mobile-light.

### L3. Section 2.3 worked equation: the white-noise part is cut at 360 px

- Location: Section 2.3, the display equation with two underbraces after "the band from 0.1 to 10 Hz contains"; mobile-light-12, mobile-dark-12.
- Problem: at 360 px the right half of the equation (the white part and its value "≈ 31.5 nV") is hidden behind an unmarked sideways scroll; the next sentence then gives the total, 74.8 nV, which depends on it.
- Why it matters: a phone reader sees one of the two terms of the sum the paragraph reports. The value reappears in the budget table of Section 6.1, so it is recoverable, but not at the point it is used.
- Required action: stack the two terms (one underbraced term per line, for example in a `gathered` block), so each fits in the text column.
- Priority: minor
- Acceptance condition: at 360 px both terms and both values are visible without sideways scrolling.

Site-level issues already recorded affect this page: the noise-density figure (Section 2.3) is scaled and still cut at 360 px with no scroll cue (the "1000" axis label and the "white" annotation are hidden), and the interference checklist table (Section 5.5) loses most of its "Remedies" column at 360 px because of the 7rem minimum cell width. Dark mode renders the figure, tables and equations correctly (mobile-dark-11, 12, 24, 25). No ligature artifacts.

The page already uses the right representations: one figure for the 1/f corner, a filter table, the coupling checklist, the budget table and a summary table. A schematic of the four coupling paths would be a possible addition but is not required; the checklist carries the comparison.

## E. Technical and source findings

No technical errors found; all worked numbers recomputed (Section B). `facts.json`: HTTP 200 on all three viewports, 0 KaTeX errors, 0 broken images, 0 console errors, one h1, headings in order. References are textbooks, cited generally rather than per claim; the 1928 date for Johnson and Nyquist and the 3σ convention are standard and correct, though uncited on the page (acceptable for an explainer).

## F. Required changes

Mandatory: none (no critical or major finding).

Optional (minor, follow-up):

- [ ] L1: rewrite the Section 2.2 inline square root so the page no longer scrolls sideways at 360 px.
- [ ] L2: state the baseline of "nearly five bits".
- [ ] L3: stack the two underbraced terms of the Section 2.3 equation.
- [ ] Link the equivalent-noise-bandwidth table to the window table of "Spectra: The DFT and the FFT".

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
| L3 | | | |
