# Live review: Designing FIR and IIR Filters

- URL: https://acrr.asia/blog/designing-fir-and-iir-filters
- Source: `src/content/blog/designing-fir-and-iir-filters.mdx` (Digital Signal Processing for Engineers, entry 4)
- Commit deployed: `7e20c2c`
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40085671258 (2026-10-24 10:26 UTC): 25 desktop-light, 45 mobile-light, 45 mobile-dark tiles (dark tiles read where they hold a table, code or the diagram)
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-24. The reviewer did not write or revise this article.
- Risk: routine (a technical tutorial; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Request revision. One major presentation finding (L1): two display equations that the worked designs depend on are cut off at desktop width, and on a phone. Everything else is minor.

**Library decision: retain and update.** This is the most practically useful entry of the series: one specification is designed as an FIR and as an IIR filter, compared, and then quantized, and every number on the page reproduces. Nothing on the site covers the same ground (Signal Conditioning treats analog Butterworth filters as components, and From Signal Processing to Digital Control reuses the bilinear transform by link under the name Tustin). The update is L1 (mandatory) and L2 (a response plot, optional but the most valuable addition).

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineer with the series' z-transform and DFT background who must turn a pass/stop specification into coefficients that run on real hardware.
- Problem: choosing FIR or IIR, computing coefficients that meet a tolerance scheme, and implementing them without finite word length breaking the filter.
- Outcome: specify a filter; design a linear-phase FIR filter by the window method (Hamming, Kaiser); design a Butterworth IIR filter by the bilinear transform with prewarping; compare the two; choose structures and word lengths (second-order sections, scaling, saturation) that keep the result stable.
- Distinctive contribution: one running specification designed both ways and then quantized, with orders, attenuations, pole radii, noise gains and a limit cycle reproduced by four runnable scripts.
- Evidence: derivations; four scripts with their real output; a window table measured for the entry; Kaiser's formulas; IEEE Std 754-2019, Oppenheim and Schafer (2010), Parks and McClellan (1972), Proakis and Manolakis (2007).
- Limitations: no Parks-McClellan, Chebyshev or elliptic design computed (stated on the page); no plot of any response.

The benefit is delivered. The opening states the practical question and the plan; the specification table is the spine; Sections 2 to 4 design and compare; Sections 5 and 6 explain why the comparison table's "must be checked, and preserved under rounding" matters, with the coefficient-quantization script as the decisive demonstration (12 fractional bits push a direct-form pole to radius 1.0995 while the sections stay at 0.9424). All four scripts were rerun for this review and print exactly the published output; the exercise answers were recomputed (Exercise 1: M = 268 Blackman and 207 Kaiser; Exercise 3: 178.6 Hz; Exercise 4: Q14 coefficients −18727/16384 and 6763/16384, radius 0.64248; Exercise 5: dead band 50); the noise gains of 6.3 were recomputed (3.49 and 11 921 with unrounded coefficients). The comparison table's claim that IIR favors low delay also holds for this example: the order-17 Butterworth design has a group delay of 15 samples at DC rising to 28 at 100 Hz, against a constant 33 for the FIR design (computed for this review; the page does not give these numbers, which would strengthen the "Phase" row). Value category: practical implementation. Format: tutorial.

Missing piece (L2): a filter-design tutorial whose every result is a number never shows a magnitude response against the tolerance scheme. One plot of the three designs would show at a glance what the tables state: the Hamming design's unused passband margin, Kaiser's tighter fit and Butterworth's monotone roll-off.

Overlap: Section 3.5 (decimation) and 6.3 (rounding noise as q²/12) build on Sampling, Quantization and Data Conversion by link, without repeating it; Section 4.2 (bilinear transform) is the source that From Signal Processing to Digital Control cites. Section 4.1's Butterworth prototype overlaps Signal Conditioning 6.2 in subject, from the design rather than the circuit side; no merge is warranted.

## C. Substantive findings

None beyond L1 (a presentation defect that hides results; see D).

## D. Visual and structural findings

### L1. Two display equations cut off at desktop width

- Location: Section 2.2, the linear-phase equation after "factoring out the delay to the center gives" (desktop-light-04; mobile-light-07); Section 3.4, Kaiser's formulas after "in rad/sample:" (desktop-light-08; mobile-light-15). Also, less important, the numeric coefficient arrays in Section 4.3 (desktop-light-12: "a = [1, −1.142981, 0.41280" cut).
- Problem: at 1280 px the 2.2 equation ends at "= e^(−j…" so the definition "= e^(−jωM/2) A(ω)" is hidden, yet the next sentence begins "where the amplitude response A(ω) is real". The 3.4 display shows the piecewise β formula and then a lone "M": the order formula M = (A − 8)/(2.285 Δω) is entirely hidden, although the next paragraph computes M = 58.5 from it and Exercise 1 asks the reader to use it. At 360 px even less is visible. They scroll sideways inside their box, with no visible cue.
- Why it matters: these are the definition of A(ω), on which the linear-phase argument rests, and the order estimate the Kaiser design and an exercise depend on. A reader who does not discover the hidden scroll meets a symbol that is never shown being defined.
- Required action: break the 2.2 equation over two lines (an `aligned` block, with "= e^(−jωM/2) A(ω)" on its own line); set Kaiser's order formula as a separate display below the β cases; split the two 4.3 arrays onto separate lines.
- Priority: major
- Acceptance condition: on new captures the full 2.2 equation, both of Kaiser's formulas and both 4.3 arrays are visible without sideways scrolling at 1280 px, and at 360 px no line of the 2.2 equation or of the order formula is cut.

### L2. No magnitude-response plot of the designs

- Location: Sections 3.3, 3.4 and 4.4 (desktop-light-06 to 14).
- Problem: the Hamming, Kaiser and Butterworth designs are reported only as worst-case numbers; there is no plot of any response against the tolerance scheme, although the scripts already compute the responses.
- Why it matters: minor; the numbers are right and sufficient, but a plot would let the reader see the trade-offs Section 3.3 and 4.5 describe (the unused passband margin of fixed windows, the equal ripple in both bands, the monotone Butterworth roll-off) instead of inferring them.
- Required action: add one generated figure: magnitude in dB from 0 to 500 Hz of the order-66 Hamming, order-60 Kaiser and order-17 Butterworth designs, with the specification's passband and stopband limits drawn as a mask, and a caption that says what to notice. Data from the article's own scripts.
- Priority: minor
- Acceptance condition: on new captures the figure appears in Section 3 or 4.5, legible at 1280 and 360 px and in dark mode, with all three curves inside the mask at 100 and 150 Hz.

Layout otherwise sound. The SOS diagram is legible in light and dark mode (mobile-dark-29); tables fit at 1280 px. At 360 px the window table's transition-width column, which the design procedure uses, and the IIR column of the comparison table sit under the scroll shadow (site-level: 7rem minimum cell width and no scroll cue); the Butterworth pole formula, the order inequality and the SOS diagram are cut at 360 px (site-level). The desktop contents sidebar scrolls to show "8. Summary" and "References" (by design). No code ligatures seen.

## E. Technical and source findings

None. KaTeX rendered without errors; HTTP 200 on all three viewports, no page-level horizontal scroll, no overflowing element, no console error (`facts.json`). Long lines in the scripts and in the 6.2 output scroll inside their code boxes at 1280 px; the printed values themselves are fully visible.

## F. Required changes

Mandatory:

- [ ] L1: split the Section 2.2 equation and Kaiser's formulas (and the 4.3 arrays) so that they fit.

Optional:

- [ ] L2: magnitude-response plot of the three designs against the tolerance mask.
- [ ] Section 4.5, "Phase" row: give the IIR design's group delay across the passband (about 15 samples at DC, 28 at 100 Hz, computed for this review) beside the FIR's constant 33.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
