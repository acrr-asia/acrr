# Live review: Smart Sensors and MEMS

- URL: https://acrr.asia/blog/smart-sensors-and-mems
- Source: `src/content/blog/smart-sensors-and-mems.mdx` (Sensor Systems, entry 6 of 7)
- Commit deployed: `7e20c2c` (master after PR #57)
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40085671258 (captured 2026-10-24 10:26 UTC): 16 desktop-light, 30 mobile-light, 30 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-24. The reviewer did not write or revise this article.
- Risk: routine (a technical explainer; no reporting, named-party claims, safety guidance or commercial relationship; no product or manufacturer is named)

## A. Decision

Accept with follow-up. No critical or major finding; two minor findings (L1, L2) remain open. The contract is delivered and every worked number checked is right.

**Library decision: retain.** The page explains why MEMS sensors need their electronics in the package (the femtofarad arithmetic), what fundamentally limits them (thermomechanical noise), and what integration costs a system designer (hidden filters, timing, self-heating). The robotics series uses IMUs without this background; the calibration entry builds on its self-test and timing points. No other ACRR page covers it.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineer who has followed the discrete measurement chain of the earlier entries and now meets integrated sensors (phone-grade accelerometers, gyroscopes, pressure sensors) in a design.
- Problem: understanding what a MEMS sensor does internally, what limits it, and what a smart sensor's built-in processing changes for the user.
- Outcome: explain silicon's mechanical advantages and scaling; compute an accelerometer's deflection, capacitance change and thermomechanical noise floor; explain the Coriolis gyroscope and its bias drift; describe on-chip temperature compensation, self-test and digital interfaces; weigh integrated against discrete designs.
- Distinctive contribution: one representative design carried through numbers (5 kHz, 100 fF, 2 µm gaps, 1 µg) that show why the electronics must be in the package and where the mechanical noise floor lies, with the user-side costs of integration made explicit.
- Evidence: derivations and worked numbers on the page; Fraden (2016), Gabrielson (1993) for thermomechanical noise, Kaajakari (2009), Senturia (2001).
- Limitations: a representative design, not product data; no fabrication detail beyond the two process families; no magnetometers or environmental sensors.

The benefit is delivered. Sections 1 to 3 give the mechanics and sensors, Section 4 the electronics, Section 5 the costs, with a comparison table that a reader can reuse. I recomputed: deflection 9.94 nm per g; 0.99 fF per g; thermomechanical noise 7.2 × 10⁻⁴ m/s²/√Hz = 73.5 µg/√Hz, 0.74 mg RMS in 100 Hz, 7.3 pm and 0.73 aF; Coriolis velocity 1.26 m/s and 0.044 m/s² (4.5 mg) at 1 °/s; ΔV_BE 53.8 mV and 0.179 mV/K for N = 8 at 300 K; silicon density 0.30 of steel's; the differential-capacitance expansion (cubic term of relative size x²/d²). The figure's labels agree with the equation (C2 on the side whose gap narrows to d − x). All match. Value category: conceptual understanding. Format: explainer.

Overlap: gyroscope bias and accelerometer tilt also appear in "Sensing and State Estimation: An Overview" (robotics series), linked from Section 3.2; I2C and SPI are the subject of "Serial Buses: UART, SPI, I2C and CAN" (embedded series); delta-sigma conversion is in "Sampling, Quantization and Data Conversion" (linked). The page treats each from the sensor's side and does not repeat them.

## C. Substantive findings

No substantive findings.

## D. Visual and structural findings

### L1. Differential-capacitance equation: the result is cut at 360 px

- Location: Section 3.1, the display equation after "Each gap forms a capacitor"; mobile-light-09, mobile-dark-09.
- Problem: at 360 px the equation ends at "ε₀A(1/(d − x) − 1/(d + x)) =" and the two results, 2ε₀Ax/(d² − x²) and ≈ 2C₀x/d, are hidden behind an unmarked sideways scroll. Desktop is fine.
- Why it matters: 2C₀x/d is the result the next paragraph and the worked numbers use ("2 × 100 fF × 9.9 nm / 2 µm"). The phone reader sees the setup without the conclusion; it is restated only in the summary table.
- Required action: break the equation over two lines (an `aligned` block: the definition on the first, "= 2ε₀Ax/(d² − x²) ≈ 2C₀x/d" on the second).
- Priority: minor
- Acceptance condition: at 360 px the whole equation, including ≈ 2C₀x/d, is visible without sideways scrolling.

### L2. The I2C/SPI link goes to the series page, not the article on those buses

- Location: Section 4.4, first paragraph, link "Embedded and Real-Time Systems"; desktop-light-11.
- Problem: the sentence says the buses are what that series "covers" but links the series overview, from which the reader has to find the entry. ACRR has an article on exactly these buses, "Serial Buses: UART, SPI, I2C and CAN" (`/blog/serial-buses-uart-spi-i2c-and-can`).
- Why it matters: a reader who wants the bus details is one click further from them than necessary; standards 8.1 asks for the first mention to link the most specific page.
- Required action: link "the serial buses" (or the series name) to the serial-buses article, keeping the series name in the text.
- Priority: minor
- Acceptance condition: the link in Section 4.4 opens `/blog/serial-buses-uart-spi-i2c-and-can`.

Site-level issues already recorded affect this page: the Section 4 Mermaid diagram is cut at 360 px (the "Non-volatile memory" node is off-screen, no scroll cue; mobile-light-16), and the integration comparison table (Section 5) loses part of its "Smart sensor" column at 360 px (7rem cells). The accelerometer figure is scaled at 360 px with the right "fixed electrode" label clipped; it remains readable. Dark mode correct for the figure, the diagram and the equations (mobile-dark-09, 16). No ligature artifacts.

The page's two visuals (accelerometer schematic, smart-sensor block diagram) are the right ones. A gyroscope sketch (drive and sense axes) would help Section 3.2 but is optional.

## E. Technical and source findings

No technical or source errors found (Section B). `facts.json`: HTTP 200 on all three viewports, no horizontal page scroll at 360 px, 0 KaTeX errors, 0 broken images, 0 console errors, one h1. One wording that is strong but defensible: "A digital link is immune to the interference and ground-loop problems of the noise entry" holds for the link itself (a few hundred millivolts do not flip a bit), not for the sensor's own analog front end; the sentence is scoped to the link, so no finding.

## F. Required changes

Mandatory: none (no critical or major finding).

Optional (minor, follow-up):

- [ ] L1: split the Section 3.1 differential-capacitance equation over two lines.
- [ ] L2: link the bus mention in Section 4.4 to "Serial Buses: UART, SPI, I2C and CAN".
- [ ] Optional: a drive-and-sense sketch for the gyroscope in Section 3.2.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
