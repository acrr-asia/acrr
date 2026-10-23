# Live review: Signals and Systems in Discrete Time

- URL: https://acrr.asia/blog/signals-and-systems-in-discrete-time
- Source: `src/content/blog/signals-and-systems-in-discrete-time.mdx` (Digital Signal Processing for Engineers, entry 1)
- Commit deployed: `1eb85d4`
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/39980397404 (2026-10-23 15:43 UTC): 23 desktop-light, 42 mobile-light, 42 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-23. The reviewer did not write or revise this article.
- Risk: routine (a technical tutorial; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Request revision. One major presentation finding (L1): the display equations that carry the article's results are cut off at the right edge, one of them at desktop width (Section 6.2) and most of the central ones on a phone (difference equation, convolution sum, frequency-response derivation). The other findings are minor.

**Library decision: retain.** This is the foundation entry of the DSP series; all four later entries link its conventions table, and the series depends on its definitions of LTI systems, the difference-equation convention, convolution and BIBO stability. The content is correct (re-checked below) and well ordered, and no other ACRR page covers discrete-time signals and systems. The revision needed is to the presentation of its equations, not to its substance.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineering student or engineer with calculus, complex numbers and the idea of sampling, starting the DSP series with samples already in memory.
- Problem: knowing what frequency means for a sequence and which systems can be analyzed, and describing such a system by a difference equation and an impulse response.
- Outcome: convert hertz to radians per sample and explain discrete-time aliasing and periodicity; test linearity, time invariance, causality, memory and BIBO stability; write and run a difference equation in the series' sign convention; compute a convolution by hand; read causality, stability and DC gain from $h[n]$; compute a first frequency response.
- Distinctive contribution: one compact path from sequences to frequency response, fixing the notation and sign conventions the whole series uses, with two worked systems (three-point moving average and exponential smoother) carried through every section, a mains-interference example and two scripts whose output is shown.
- Evidence: derivations in the text; two Python and NumPy scripts with their output; Oppenheim and Schafer (2010), Oppenheim, Willsky and Nawab (1997), Proakis and Manolakis (2007).
- Limitations: no z-transform (entry 2), no DFT (entry 3), no filter design or finite word length (entry 4); sample values treated as unquantized.

The benefit is delivered. The two running examples make each new idea concrete, the property table and the summary table give the reader something to keep, and the ending hands over cleanly to the z-transform entry. Spot checks recomputed in this review: $\ln 0.05/\ln 0.9 = 28.4$ (first sample above 95% at $n = 28$); $\tau = -0.01/\ln 0.9 = 94.9$ ms; the three-point average's gain at 10, 25, 60 and 75 Hz for $f_s = 150$ Hz (0.9424, 0.6667, 0.206, 0.3333); the smoother at $\omega = 0.1\pi$, $a = 0.9$: $|H| = 0.319$, phase $-62.6°$; $(1 - a)/(1 + a) = 0.0526$; the convolution table; Exercises 1, 3, 4 and 5. All correct.

Value density: high; no section is padding, and Section 5 (reading properties from $h[n]$) turns the definitions of Section 2 into tests, which is the right reuse rather than repetition. Value category: conceptual understanding. Format: explainer.

Overlap noticed: BIBO stability is also defined, for continuous time, in [Stability and Eigenvalues](/blog/stability-and-eigenvalues) (control series); mains-interference removal and first-order low-pass filtering also appear, on the analog side, in [Signal Conditioning](/blog/signal-conditioning) and [Noise, Interference and Limits of Detection](/blog/noise-interference-and-limits-of-detection). These are complementary treatments (discrete against continuous, digital against analog), not duplicates; cross-links between them belong in the Phase 7 overlap map.

## C. Substantive findings

### L1. Key display equations cut off at the right edge

- Location: Section 6.2, the derivation of $H(e^{j\omega})$ for the three-point average (desktop-light-17: ends at "$= \tfrac13(1 + 2$c", the final form $(1 + 2\cos\omega)e^{-j\omega}$ hidden; mobile-light-32: ends after the first "$= \tfrac13$"). At 360 px also: Section 2.2, the linearity equation (mobile-light-13); Section 3.1, both forms of the difference equation (mobile-light-16 and 17); Section 4.2, the convolution sum, second form (mobile-light-22); Section 6.1, the eigenfunction derivation with its $H(e^{j\omega})$ label and the sinusoid-in, sinusoid-out line (mobile-light-30 and 31); Section 6.3, the closed form $\frac{1 - a}{1 - ae^{-j\omega}}$ (mobile-light-34). Dark mode identical (mobile-dark-16, 30, 32).
- Problem: each equation is wider than the text column and scrolls sideways inside its box, with nothing on the page to say so. On a phone the reader sees the left-hand side and the start of the right-hand side of almost every central equation of the article.
- Why it matters: these are the results the sections exist to derive (the series' difference-equation convention, the convolution sum, the frequency response, the zero that removes mains interference). A reader who does not discover the hidden scroll reads an incomplete formula exactly where the argument depends on it; the 6.2 case affects desktop readers too.
- Required action: break the long equations over lines (an `aligned` block with one step per line for 6.1, 6.2 and 6.3; the two forms of 3.1 and of 4.2 each on its own line, with the second sum below the first where needed; the linearity equation is short enough to fit if set on two lines). The same treatment was applied to Spectra: The DFT and the FFT after its live review.
- Priority: major
- Acceptance condition: on new captures, the Section 6.2 equation is fully visible at 1280 px, and at 360 px no line of the equations listed above is cut, light and dark.

## D. Visual and structural findings

### L2. Exponential-smoother diagram: feedback path off-screen at 360 px, and no caption

- Location: Section 3.2, the Mermaid block diagram (desktop-light-10; mobile-light-19, mobile-dark-19).
- Problem: at 360 px only "x[n]", "× (1 − a)", the adder and "y[n]" are visible; "one-sample delay" is cut and "× a" and the return arrow, the feedback that makes the system recursive, are off-screen with no scroll cue. The figure has no caption (`facts.json`: one SVG figure without a title).
- Why it matters: the diagram's purpose is to show the feedback loop, and that is the part a phone reader does not see.
- Required action: a top-to-bottom layout (`flowchart TB`, with the delay and the multiplier under the adder) that fits at 360 px, or the site-level scroll cue for wide figures; and a caption, for example "Figure 1. The exponential smoother: the output, delayed by one sample and scaled by $a$, is added to the scaled input."
- Priority: minor
- Acceptance condition: at 360 px the delay, the "× a" block and the feedback arrow are visible, or a visible cue shows the figure scrolls; the figure has a caption.

### L3. System-properties table: last column hidden at desktop width, half the table hidden on a phone

- Location: Section 2.2, the table of five systems against five properties (desktop-light-08; mobile-light-15 and 16).
- Problem: at 1280 px the sixth column's header reads "BIBO sta..." under the scroll shadow; at 360 px only "System", "Linear" and "Time-invariant" are visible.
- Why it matters: the table is the summary of Section 2.2 and the stability column is the property Section 5 builds on.
- Required action: shorten the headers so the table fits at 1280 px ("Stable" for "BIBO stable"; "Memory-less" or "Static"), and consider transposing it (properties as rows, the four systems as columns) so that it also fits at 360 px.
- Priority: minor
- Acceptance condition: all six columns visible at 1280 px; at 360 px every cell readable without the reader having to discover a sideways scroll.

### L4. Code-font ligatures in the scripts

- Location: Section 4.3, `difference_equation` (`if n - k >= 0` drawn with a single "≥" glyph; desktop-light-13, mobile-light-25).
- Problem: the monospace font's ligatures render Python operators as mathematical symbols. Copy-and-paste still yields `>=`.
- Why it matters: small here (one operator, and the reader of this article is not learning Python), but a reader retyping the script types a character Python rejects.
- Required action: the site-level fix recorded as L1 in the live review of [Inside a Microcontroller](/blog/inside-a-microcontroller) (disable ligatures for code in `prose.css`); nothing to change in this article.
- Priority: minor
- Acceptance condition: `>=` shows as two characters in Section 4.3 on new captures.

The page otherwise uses the right representations: a conventions table, a systems table, a property matrix, a convolution worked as a table, a block diagram, two scripts with output, a summary table. A plot of the two frequency responses (moving average and smoother, $0 \le \omega \le \pi$) would make Sections 6.2 and 6.3 easier to grasp at a glance; this is optional, since the text gives the key values.

## E. Technical and source findings

### L5. Exercise 5 asks "how many samples" and answers with an index

- Location: Section 7, Exercise 5 and its answer (desktop-light-20; mobile-light-36).
- Problem: the question asks how many samples the step response "takes" to first reach 95%; the answer gives the index of the first such sample, $n = 59$, which with the series' convention that the step starts at $n = 0$ is the 60th sample. Section 3.3 uses the same index wording ("so at $n = 28$") without the count question, so it is clear there.
- Why it matters: a reader who counts samples answers 60 and concludes they are wrong when they are not.
- Required action: ask for the index ("at which sample index does its step response first reach 95%?") or give both in the answer ("at $n = 59$, the 60th sample after the step").
- Priority: minor
- Acceptance condition: the question and the answer of Exercise 5 use the same quantity.

No other technical or source errors found. The 13 October audit's and the wave 2 review's technical points (the 60 Hz gain of 0.21, the sufficiency condition for removing interference, the prerequisites) are correctly reflected on the live page. `facts.json`: HTTP 200 on all three viewports, one h1, no horizontal page scroll at 360 px, no overflowing page elements, 0 KaTeX errors, 0 broken images, 0 console errors.

## F. Required changes

Mandatory:

- [ ] L1: split the wide display equations (Section 6.2 at all widths; Sections 2.2, 3.1, 4.2, 6.1, 6.3 at 360 px).

Optional:

- [ ] L2: top-to-bottom layout and a caption for the Section 3.2 diagram.
- [ ] L3: shorter headers (or a transposed layout) for the Section 2.2 property table.
- [ ] L4: site-level ligature fix (no article change).
- [ ] L5: make Exercise 5's question and answer refer to the same quantity.
- [ ] Section 1.1 mentions "an arrow ... to mark $n = 0$" but never shows the notation; either show it once or drop the arrow.
- [ ] A frequency-response plot for Sections 6.2 and 6.3.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
| L3 | | | |
| L4 | | | |
| L5 | | | |
