# Live review: Sampling, Quantization and Data Conversion

- URL: https://acrr.asia/blog/sampling-quantization-and-data-conversion
- Source: `src/content/blog/sampling-quantization-and-data-conversion.mdx` (Sensor Systems, entry 4)
- Commit deployed: `7e20c2c`
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40085671258 (2026-10-24 10:26 UTC): 17 desktop-light, 31 mobile-light, 31 mobile-dark tiles (dark tiles read where they hold the figure or a table)
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-24. The reviewer did not write or revise this article.
- Risk: routine (a technical explainer; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Accept with minor follow-up. The page is clean at 1280 px, its numbers are right and it delivers its contract. Three minor findings, all about reading it on a phone or moving around the series: the aliasing figure's labels are too small and partly cut at 360 px (L1), the SQNR result is cut at 360 px (L2), and references to "the first entry" are not linked (L3).

**Library decision: retain.** This entry is the hub that five other pages link to for sampling, quantization and converters (Designing FIR and IIR Filters 3.5 and 6.3, Smart Sensors and MEMS on delta-sigma, Inside a Microcontroller 6.2, Noise, Interference and the Limits of Detection on dither, and the DSP series overview as a prerequisite). It is the only place on the site that explains converter specifications and architectures. Nothing should be merged or reclassified.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineering student or engineer following Sensor Systems who has a conditioned analog voltage and needs to know what the converter does to it.
- Problem: choosing a sampling rate, an anti-aliasing filter, a resolution and an architecture, and knowing what error each contributes.
- Outcome: explain aliasing and the sampling theorem; size an anti-aliasing filter against the converter's resolution; compute the quantization step, its uncertainty and the ideal SQNR; read INL, DNL, SINAD, ENOB and jitter specifications; choose between SAR, delta-sigma and other architectures.
- Distinctive contribution: sampling and quantization tied to the series' running load-cell channel and to the rectangular-distribution uncertainty of entry 1, with a worked number at each step.
- Evidence: derivations and worked numbers; one generated figure; IEEE Std 1241-2023, Kester (2005), Oppenheim and Schafer (2010), Pallàs-Areny and Webster (2001).
- Limitations: delta-sigma noise shaping qualitative only; no code; digital-to-analog conversion in one paragraph.

The benefit is delivered. The opening separates the two approximations (time and amplitude) and says how each loses information, which frames the rest. Each section answers part of the contract, in the order a designer meets the decisions; the summary table restates the answers. Worked numbers were recomputed for this review: 76.3 dB for the fourth-order filter at 90 Hz against 72.2 dB for one 12-bit step; q = 0.806 mV, 50.4 µV and 0.197 µV; u_q = 0.233 mV; SQNR 74.0 and 98.1 dB; 3686 codes and 2.7 g, 58 982 codes and 0.17 g; ENOB 13.99 for 86 dB; jitter limits 38.9 ns and 0.121 ns; the SAR table (q = 0.20625 V, code 9 truncating, code 10 rounding). The aliasing figure is drawn from the stated frequencies (9 Hz sampled at 10 Hz gives the 1 Hz samples shown). Value category: conceptual understanding. Format: explainer.

Optional addition, not a finding: a staircase figure for 3.1 (the ideal transfer function and the ±q/2 error band) would help readers who have not seen one. The delta-sigma section is qualitative but adequate for the series' scope, and it already states the latency cost that matters for multiplexed inputs.

Overlap: the DSP series' first entry explains aliasing from the sequence side (frequencies differing by 2π are identical) and names this entry as its prerequisite; the two are complementary. Noise, Interference and the Limits of Detection develops the dither remark of 3.2 with a simulation; again by link, not repetition.

## C. Substantive findings

None.

## D. Visual and structural findings

### L1. Aliasing figure: labels too small and legend cut at 360 px

- Location: Section 1.1, the aliasing figure (mobile-light-05, mobile-dark-05; compare desktop-light-03).
- Problem: at 360 px the figure is scaled to about half its desktop size; the axis labels and the legend ("solid: 9 Hz signal · dashed: 1 Hz alias · dots: samples") are roughly 6 px high, and the right edge, with the last sample at t = 1 s and the end of the legend, is cut (the figure keeps 60 percent of its natural width, so it scrolls without a cue).
- Why it matters: minor; the caption repeats the key, so the figure can still be understood, but its own labels are not readable on a phone.
- Required action: in `scripts/generate-diagrams.py`, move the legend into the caption or onto two lines and raise the label font size so that it renders at least at the caption's size at 360 px; regenerate.
- Priority: minor
- Acceptance condition: at 360 px every label of the figure is legible at caption size and the legend is fully visible.

### L2. SQNR result cut at 360 px

- Location: Section 3.3, the SQNR display (mobile-light-14: ends at "≈ 6.0"); also the identity in 1.1 (mobile-light-04: the final "= cos(2πf n/f_s)" is cut).
- Problem: at 360 px the right-hand side "≈ 6.02 N + 1.76 dB", the result the section exists to give, is hidden beyond the column (site-level scroll issue). In 1.1 the conclusion of the identity is hidden.
- Why it matters: minor; "6 dB per bit" appears in the next sentence and the formula in the summary table, but the display itself shows no result.
- Required action: put "SQNR ≈ 6.02 N + 1.76 dB" on its own line under the exact expression (an `aligned` block), and split the 1.1 identity at its second equals sign.
- Priority: minor
- Acceptance condition: at 360 px the full SQNR approximation and the conclusion of the 1.1 identity are visible without sideways scrolling.

### L3. "The first entry" is never linked

- Location: Section 3.2 ("the situation the first entry treated as a Type B evaluation"), 3.4 ("as the first entry warned") and 4.1 ("the linearity error in the first entry") (desktop-light-07 to 09).
- Problem: the previous and next entries are linked, but the three references to the series' first entry, Measurement Systems and Sensor Characteristics, are plain text, including the one that asks the reader to recall its Type B uncertainty.
- Why it matters: minor navigation; a reader arriving from search or from the DSP series (which links here as a prerequisite) does not know which page "the first entry" is.
- Required action: link the first mention in 3.2 to `/blog/measurement-systems-and-sensor-characteristics` (its Section 5.2, "Evaluating uncertainty", is the passage meant: `#52-evaluating-uncertainty`).
- Priority: minor
- Acceptance condition: on the live page, "the first entry" in Section 3.2 is a working link to the first entry of Sensor Systems.

Layout otherwise sound: all four tables fit at 1280 px; the figure is correct in dark mode (mobile-dark-05). At 360 px the architecture table's speed and use columns sit under the scroll shadow (site-level, 7rem minimum cell width). No code on the page.

## E. Technical and source findings

None. KaTeX rendered without errors; HTTP 200 on all three viewports, no page-level horizontal scroll, no overflowing element, no broken image, no console error (`facts.json`). The 13 October audit's recomputation and the wave-2 update of the standard to IEEE Std 1241-2023 stand.

## F. Required changes

Mandatory:

- None.

Optional:

- [ ] L1: legible labels and full legend for the aliasing figure at 360 px.
- [ ] L2: split the SQNR display and the 1.1 identity.
- [ ] L3: link "the first entry" in Section 3.2.
- [ ] Section 3.1: a staircase figure of the ideal transfer function and its ±q/2 error.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
| L3 | | | |
