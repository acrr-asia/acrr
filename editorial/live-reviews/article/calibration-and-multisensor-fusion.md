# Live review: Calibration and Multisensor Fusion

- URL: https://acrr.asia/blog/calibration-and-multisensor-fusion
- Source: `src/content/blog/calibration-and-multisensor-fusion.mdx` (Sensor Systems, entry 7 of 7)
- Commit deployed: `7e20c2c` (master after PR #57)
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40085671258 (captured 2026-10-24 10:26 UTC): 34 desktop-light, 64 mobile-light, 64 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-24. The reviewer did not write or revise this article.
- Risk: routine (a technical tutorial; no reporting, named-party claims, safety guidance or commercial relationship; the standards it cites are named as references, not assessed)

## A. Decision

Accept with follow-up. No critical or major finding; three minor findings (L1 to L3) remain open. The contract is delivered: all four scripts reproduce their printed output exactly, and every number checked in the prose is right.

**Library decision: retain.** The page is long (38 minutes, about 5,800 words) and joins two subjects, calibration and fusion, but the length is earned: each section carries a derivation or a script whose output the text interprets, and the two halves are tied together by the argument that calibration makes fusion work (Section 7.3's bias-corrected run). Splitting it would break that link and leave the series without its closing synthesis. It goes well beyond the qualitative treatment of complementary filtering in the robotics series, which it cites.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineer responsible for a measurement channel (the series' load cell, thermometers, an IMU) who knows the GUM vocabulary of the first entry and has to calibrate sensors and combine several of them.
- Problem: producing a calibration with a defensible uncertainty, keeping it valid in the field and over time, and fusing several imperfect sensors without overstating the result.
- Outcome: fit a calibration curve and propagate its uncertainty, including covariance and the Student t factor; choose field references and calibration intervals; fuse readings by inverse-variance weighting, recognize correlated errors, test consistency (z, χ², Birge ratio); design and tune a complementary filter and relate it to a Kalman filter; detect and remove time offsets.
- Distinctive contribution: one worked, reproducible path from a least-squares calibration to sensor fusion, with four NumPy scripts whose real output the text interprets, and the explicit demonstration that calibrating the gyroscope bias first improves the fused tilt from 0.58° to 0.14° RMS.
- Evidence: derivations on the page; four scripts (re-run for this review with Python 3 and NumPy 2.5.3: outputs identical to the page); JCGM 100 and 200, ISO 28037, ISO/IEC 17025, ILAC-G24/OIML D 10, Fraden (2016), Taylor (1997), Thrun et al. (2005).
- Limitations: illustrative data, labelled as such; straight-line and quadratic models only; one-axis tilt; Kalman filter discussed, not implemented.

The benefit is delivered. The opening says what Sections 1 to 5 and 6 to 8 cover; each section serves the central question; the summary table and the closing paragraph tie the series' objectives together. Beyond the scripts I recomputed: reference-ratio penalties 3.1%, 11.8% and 0.5%; offset 10.6 g, sensitivity 0.07% low, s/b = 0.13 g; curve contribution at the center s/(b√n) = 0.054 g; covariance omission +27%; t(0.975, 4) = 2.78 and U = 0.39 g; PT100 straight-line residuals −0.077, +0.015, +0.062, +0.062, +0.015, −0.077 Ω (Callendar–Van Dusen with the IEC 60751 coefficients), 0.20 °C; six-position offset 0.0745 m/s² (7.6 mg) and scale factor 1.0012; gravity error up to 0.27%; tilt error 0.015% at 1°; bias uncertainty 0.003 °/s; Earth rate 0.0042 °/s; interval 2.7 years; correlated-thermometer mean 0.051 °C against 0.053 and 0.037 °C; z = −0.71 for sensors 1 and 2; discrete complementary filter derivation and α = 0.990; 25.1 °/s and 0.25° for a 10 ms offset; 50 ppm = 0.18 s/h. All match. The sign convention of Section 7.1 (positive tilt is a rotation about −y) is correct. Value category: practical implementation. Format: tutorial.

Overlap: "Sensing and State Estimation: An Overview" (robotics series) outlines the complementary filter, the Kalman update and innovation gating; this page cites it at each point and adds the quantitative treatment, so it is the deeper of the two (record in the Phase 3 overlap map: complementary filter and inverse-variance weighting, robotics entry 4 and sensor entry 7). "Measurement Systems and Sensor Characteristics" (entry 1) introduces the uncertainty vocabulary that this page extends; no repetition beyond a one-paragraph recap.

## C. Substantive findings

No substantive findings.

## D. Visual and structural findings

### L1. Opening quotation mark printed as a closing one

- Location: Section 1.1, last paragraph, "for example ”± 0.1 °C with k = 2”"; desktop-light-03.
- Problem: the quotation opens with a right double quotation mark (”) instead of a left one (“). The typographer turns a straight quote followed by "±" into a closing mark; I confirmed it in a build of this commit (the built HTML has `”±`). No other page in the site build has this pattern.
- Why it matters: small, but visible in the first screenfuls of a page that is otherwise typographically clean.
- Required action: write the opening mark explicitly as “ in the source (or rephrase without quotation marks, for example "an expanded uncertainty of ±0.1 °C with $k = 2$").
- Priority: minor
- Acceptance condition: the live page shows “± 0.1 °C with k = 2” with a left opening mark, or the rephrased text.

### L2. Calibration data table: the 10 kg point is hidden at desktop width

- Location: Section 3.2, the table of reference masses and indications; desktop-light-08 (and mobile-light-14, where only the 0 and 2 kg columns are visible).
- Problem: the table has seven columns; with the site's 7rem minimum cell width it is wider than the text column even at 1280 px, so the last column (10 kg, 2.000815 mV/V) sits under the scroll shadow. At 360 px four of the six data points are hidden.
- Why it matters: the reader is asked to follow a fit of six points and sees five (one at 360 px: two); the values do reappear in the script below, so nothing is lost, only made harder to read.
- Required action: transpose the table to two columns (reference mass, indication) and six rows, which fits at every width.
- Priority: minor
- Acceptance condition: all six data points are visible without sideways scrolling at 1280 px and at 360 px.

### L3. Section 2 and 3.1 equations cut at 360 px, hiding the covariance formula

- Location: Section 2, the law of propagation of uncertainty; Section 3.1, the display with b, a and S_xx and the display with u²(b), u²(a) and u(a, b); mobile-light-11, 12 and 13.
- Problem: at 360 px each of these displays is wider than the screen and scrolls sideways without a cue. In the third, u(a, b) = −x̄s²/S_xx is entirely off-screen, yet the next paragraph begins "The covariance is negative whenever …", which is about that formula. In the first, the covariance term of the propagation law is cut.
- Why it matters: the negative covariance is the point Section 3.3 builds on (ignoring it overstates the uncertainty by 27%); a phone reader does not see the formula the text discusses.
- Required action: put each multi-formula display on separate lines (a `gathered` or `aligned` block: one formula per line), and break the propagation law after the first sum.
- Priority: minor
- Acceptance condition: at 360 px every formula of these three displays, in particular u(a, b), is visible without sideways scrolling.

Site-level issues already recorded affect this page: code listings scroll sideways at 360 px and some comment lines reach the edge of the code box at 1280 px; the two Mermaid diagrams fit. Dark mode renders the diagrams, code and equations correctly (mobile-dark-14, 45). No ligature artifacts.

Capture note (not a page finding): in this run, most desktop-light tiles after the first and several mobile-light tiles of this page (for example desktop-light-02, 05, 21 and mobile-light-02) show the body text in a wider fallback serif instead of Noto Serif, while the first tiles show Noto Serif. A local build of the same commit, captured the same way, renders Noto Serif throughout and loads the font files normally. The page is the tallest in the batch (30,197 px at 1280, 49,146 px at 360); the change is probably a capture artifact of very tall pages, not a reader-facing defect. It should be confirmed on the next capture run; if it recurs on the live site in a normal browser, it becomes a site-level font finding.

## E. Technical and source findings

No technical errors found. All four scripts were re-run: output identical to the page. `facts.json`: HTTP 200 on all three viewports, no horizontal page scroll at 360 px, 0 KaTeX errors, 0 broken images, 0 console errors, one h1. Not re-verified in this review: the publication status of ISO 28037:2026 and the 2022 edition of ILAC-G24/OIML D 10 (both recorded as verified on the issuers' sites in the wave 2 revision log of the 13 October audit item); I did not re-check the issuers' sites.

## F. Required changes

Mandatory: none (no critical or major finding).

Optional (minor, follow-up):

- [ ] L1: correct the opening quotation mark in Section 1.1.
- [ ] L2: transpose the Section 3.2 data table to two columns.
- [ ] L3: stack the Section 2 and 3.1 display equations so they fit at 360 px.
- [ ] Next capture run: confirm that the fallback font on this page was a capture artifact.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
| L3 | | | |
