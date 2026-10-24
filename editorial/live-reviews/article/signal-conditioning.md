# Live review: Signal Conditioning: Bridges, Amplifiers and Analog Filters

- URL: https://acrr.asia/blog/signal-conditioning
- Source: `src/content/blog/signal-conditioning.mdx` (Sensor Systems, entry 3)
- Commit deployed: `7e20c2c`
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40085671258 (2026-10-24 10:26 UTC): 22 desktop-light, 43 mobile-light, 43 mobile-dark tiles (dark tiles read where they hold a figure or a table)
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-24. The reviewer did not write or revise this article.
- Risk: routine (a technical explainer; the isolation paragraph mentions dangerous voltages and patient-connected equipment only to say when isolation is needed, and gives no procedure, so it is not safety guidance in the sense of standards 3)

## A. Decision

Accept with minor follow-up. The page delivers its contract, every number checked is right, and nothing is cut at 1280 px. Two minor findings: the amplifier circuits and the complete channel, the core of the article, are described only in words (L1), and on a phone the two figures, the bridge equation and the table column the text points to are partly hidden (L2).

**Library decision: retain.** The entry is the series' only treatment of analog front ends, and its load-cell channel is the running example that the sampling, noise and calibration entries build on; the DSP series' filter-design entry covers digital filters, not these circuits. The useful update is L1 (figures), which is optional.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineering student or engineer comfortable with basic circuit analysis who must connect a small sensor signal to an ADC.
- Problem: designing the analog front end between a sensor and a converter: excitation, bridge, amplification, current and charge conversion, filtering and protection.
- Outcome: choose excitation and lead-wire connections; compute bridge outputs and nonlinearity; use op-amp, instrumentation-amplifier gain and CMRR; convert current and charge; choose a filter order; assemble a ratiometric load-cell channel.
- Distinctive contribution: one signal followed through the five jobs of conditioning in order, closing with a complete, numerically consistent load-cell channel that the next entries digitize, budget and calibrate.
- Evidence: worked numbers; two generated figures (bridge, Butterworth responses); Fraden (2016), Franco (2015), Horowitz and Hill (2015), Pallàs-Areny and Webster (2001).
- Limitations: ideal circuits plus a list of imperfections; no schematics of the amplifiers; the noise budget is left to entry 5.

The benefit is delivered. The opening names the five jobs, and the sections follow them in order; the closing Section 7 assembles them into one channel whose numbers agree with the rest of the series (2 mV/V at 3.3 V gives 6.6 mV; gain 450 gives 2.97 V and the ratiometric fraction 0.9 that Sampling, Quantization and Data Conversion 3.4 uses). Worked numbers were recomputed for this review: the PT100 values (0.385 mV/°C, 0.14 mW at 100 °C, 2.6 °C for 1 Ω of leads); the divider (about 2.5 mV on 2.5 V); the quarter bridge (2.4975 mV, nonlinearity x/2 = 0.1%) and the half- and full-bridge expressions from the bridge equation; the CMRR table (250 µV and 25 µV); the difference-amplifier CMRR with 0.1% resistors ((1 + G)/(4ε) = 500, 54 dB); R_G = 50.05 Ω; the ±2.5 mV × 600 span (0.15 to 3.15 V); the transimpedance bandwidth (159 kHz) and charge-amplifier corner (0.159 Hz); the RC cut-off (9.95 Hz) and the Butterworth table (0.196, 0.040, 0.0016 at 50 Hz; 0.958, 0.996, 0.99997 at 3 Hz). The Wheatstone figure matches the equation (R2 is the lower left arm, V_A its midpoint). Value category: practical implementation. Format: explainer.

Missing piece (L1): the in-amp of 4.1 is explained as a three-op-amp circuit in a bulleted description, the transimpedance and charge amplifiers of 5.1 and 5.2 by connection sentences, and the op-amp circuits of Section 3 by a table of connections. A reader without the circuits in mind has to draw them; standards 6.8 prefers a block or circuit diagram for components and relationships. The prose is clear enough to follow, so this is minor.

Overlap: Section 6.2's Butterworth response formula appears again, as an analog prototype, in Designing FIR and IIR Filters 4.1; the two treat it from the circuit and the design side and do not need merging. The noise and interference remarks of 6 and 6.2 defer, by link, to Noise, Interference and the Limits of Detection.

## C. Substantive findings

### L1. Amplifier circuits and the complete channel shown only in words

- Location: Section 3 (table of op-amp circuits), 4.1 (instrumentation amplifier), 5.1 and 5.2 (transimpedance and charge amplifiers), and Section 7 (complete channel) (desktop-light-08 to 19).
- Problem: there is no schematic of the three-op-amp instrumentation amplifier or of the two virtual-ground converters, and no block diagram of the Section 7 channel (bridge, in-amp with reference offset, fourth-order filter, ADC sharing the excitation as its reference).
- Why it matters: minor; the descriptions are accurate, but these circuits are the article's main content and the ratiometric connection of Section 7 is easiest to grasp as a picture of one supply feeding both the bridge and the ADC reference.
- Required action: add, through `scripts/generate-diagrams.py`, a schematic of the three-op-amp in-amp (with R, R_G and the reference terminal labeled as in the text) and a block diagram of the Section 7 channel; optionally a combined figure of the transimpedance and charge amplifiers. Captions should say what to notice (the gain resistor between the input op-amps; the shared 3.3 V line).
- Priority: minor
- Acceptance condition: on new captures the in-amp schematic appears in 4.1 and the channel diagram in Section 7, each legible at 1280 and 360 px and in dark mode, with labels that match the text.

## D. Visual and structural findings

### L2. Figures, the bridge equation and the 3 Hz column partly hidden at 360 px

- Location: Section 2.1, the Wheatstone figure (mobile-light-08 and 09: the R3/V_B side is cut) and the bridge equation (mobile-light-09: ends at "R_2/(R_1 + R_2) −", the subtracted R_4/(R_3 + R_4) hidden); Section 6.2, the Butterworth figure (mobile-light-32, mobile-dark-32: the "first order" and "second order" curve labels are off-screen and the remaining labels are about 6 px high) and the order table (mobile-light-33: the "|H| at 3 Hz" column is under the scroll shadow).
- Problem: at 360 px these elements are wider than the column and scroll without a cue (site-level), and in each case the hidden part is one the text relies on: the bridge equation's second divider, the labels that tell the Butterworth curves apart, and the column the next paragraph introduces with "The last column shows the other benefit of a higher order".
- Why it matters: minor; the caption and prose restate most of it, but a phone reader cannot see which curve is which or the numbers the paragraph discusses.
- Required action: split the bridge equation over two lines; in the Butterworth figure, label the curves inside the plot area (or in the caption) and raise the label size; drop the "Attenuation" column of the order table (it repeats |H| at 50 Hz in dB) or merge it into the 50 Hz column, so that the 3 Hz column fits.
- Priority: minor
- Acceptance condition: at 360 px the full bridge equation is visible, all three Butterworth curves are identifiable from legible labels, and the 3 Hz column of the order table is visible without scrolling.

Layout otherwise sound: all five tables fit at 1280 px; both figures are correct in dark mode (mobile-dark-09, mobile-dark-32). Site-level issues also present: the quarter-bridge, CMRR and first-order-filter displays are cut at 360 px; tables use the 7rem minimum cell width. No code on the page.

## E. Technical and source findings

None. KaTeX rendered without errors; HTTP 200 on all three viewports, no page-level horizontal scroll, no overflowing element, no broken image, no console error (`facts.json`). Optional precision: Section 7 step 4 gives the full-load fraction as 0.9 while step 2 sets the in-amp reference "slightly above 0 V"; the fraction is 0.9 plus that offset divided by 3.3 V, which calibration absorbs, and a clause would say so.

## F. Required changes

Mandatory:

- None.

Optional:

- [ ] L1: in-amp schematic and channel block diagram (optionally the two virtual-ground converters).
- [ ] L2: split the bridge equation, label the Butterworth curves legibly, make the 3 Hz column fit at 360 px.
- [ ] Section 4, CMRR table: keep "100 dB (10⁵)" on one line at 360 px (it wraps after the exponent).
- [ ] Section 7 step 4: note that the reference offset adds to the 0.9 fraction and is removed by calibration.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
