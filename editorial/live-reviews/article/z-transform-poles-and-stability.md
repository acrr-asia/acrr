# Live review: The z-Transform, Poles and Stability

- URL: https://acrr.asia/blog/z-transform-poles-and-stability
- Source: `src/content/blog/z-transform-poles-and-stability.mdx` (Digital Signal Processing for Engineers, entry 2)
- Commit deployed: `7e20c2c`
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40085671258 (2026-10-24 10:26 UTC): 20 desktop-light, 36 mobile-light, 36 mobile-dark tiles (dark tiles read where they hold a table, code or the diagram)
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-24. The reviewer did not write or revise this article.
- Risk: routine (a technical tutorial; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Accept with minor follow-up. The contract is delivered, every number checked is right, and nothing on the page is cut or misleading at 1280 px. Three minor findings: the article about poles and zeros never shows a pole-zero plot (L1), several key equations and the ROC column of the transform table are cut at 360 px (L2), and the Mermaid diagram prints a literal caret and has no caption (L3).

**Library decision: retain and update.** The page is the series' bridge between the time-domain first entry and the design entries; the filter-design and digital-control entries depend on its stability triangle, s-to-z mapping and geometric reading of the gain, and it duplicates nothing elsewhere on the site (the discrete-time stability section of Stability and Eigenvalues treats the same unit-circle condition from the state-space side, and the two complement each other). The update is L1: one figure would make the central idea of Section 5 visible instead of described.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineer or student who knows difference equations, impulse responses and BIBO stability from the first entry and wants to analyze a recursive system without summing infinite series.
- Problem: deciding from a difference equation whether a system is stable, how fast its response decays and which frequencies it passes or blocks.
- Outcome: write the transfer function, find poles and zeros, invert by partial fractions, test stability (unit circle, stability triangle), map s-plane poles to the z-plane, and place poles and zeros by hand for a notch filter.
- Distinctive contribution: one path from the definition to a working 50 Hz notch, tied back to the first entry and forward to entries 4 and 5, with the numbers reproduced by two runnable scripts.
- Evidence: derivations; two scripts with their real output; five exercises with answers; Jury (1964), Oppenheim and Schafer (2010), Proakis and Manolakis (2007).
- Limitations: causal sequences only; no contour inversion; no figures beyond one flow diagram.

The benefit is delivered. The opening screen states what the entry builds on and what it will do (the notch design is promised in the second paragraph and delivered in 5.3). Every section serves the central question: 1 defines the tool, 2 connects it to the difference equation, 3 recovers h[n], 4 answers stability, 5 answers frequency response and turns it into a design. No section is padding; the summary table is a usable recap. Worked numbers were recomputed for this review: the partial-fraction coefficients −5/3 and 8/3 and the DC gain 10; the mapping examples (e^(−0.01/0.0949) = 0.900; radius e^(−0.025) = 0.975 at ±0.198 rad); the notch script (|H| = 1.0162 at 0 Hz, 1.0203 at 500 Hz, −3 dB band 46.91 to 53.09 Hz, time constant 49.5 samples); and all five exercise answers (including the 1.105 peak of Exercise 1, the real poles 0.564 and −1.064 of Exercise 2 and r = 0.9937 with 159 samples in Exercise 5). Value category: conceptual understanding. Format: explainer.

What is missing is visual (L1). The page names the pole-zero plot, explains how to read it, and then builds Section 5 on a geometric argument (distances from a point on the unit circle to poles and zeros) without ever drawing it; standards 6.8 asks for a figure where it reduces the effort of understanding the main concept. The text remains clear without it, so this is minor.

Overlap: Section 4.3 (s-to-z mapping) is reused, by link, in From Signal Processing to Digital Control and has a state-space counterpart in Stability and Eigenvalues Section 7; neither repeats the derivation at length. An optional cross-link from 4.3 to Stability and Eigenvalues Section 7 would connect the two views.

## C. Substantive findings

### L1. No pole-zero plot or frequency-response figure

- Location: Sections 2.2, 5.1 and 5.3 (desktop-light-06 to 16; mobile-light-11 to 29).
- Problem: the article explains what a pole-zero plot is and reads the gain geometrically from distances in that plot, but shows no plot. The notch design of 5.3, the clearest case, is given only as coefficients and a table of gains.
- Why it matters: the geometric reading is the main idea of Section 5 and the design method of 5.3; a reader new to it has to construct the picture alone.
- Required action: add one generated figure for the 5.3 notch filter: its pole-zero plot with the unit circle (zeros at e^(±j0.1π), poles at radius 0.98) beside its magnitude response from 0 to 500 Hz, with a caption that says what to notice (the zero on the circle makes the null; the nearby pole restores the gain away from it). Data from the article's own formulas, per the diagram rules.
- Priority: minor
- Acceptance condition: on new captures the figure appears in Section 5.3, readable at 1280 and 360 px and in dark mode, and its values match the script output (null at 50 Hz, about 0.70 at 47 and 53 Hz).

## D. Visual and structural findings

### L2. Key equations and the ROC column cut at 360 px

- Location: Section 1.2 geometric-series equation (mobile-light-05: ends at "(az^−1)^n =", the result 1/(1 − az^−1) and the ROC |z| > |a| hidden); Section 1.3 table (mobile-light-06: the ROC column and the end of the last two denominators hidden); Section 2.1 transfer function (mobile-light-09: the polynomial form ends at "1 + a_1 z^−"); Section 2.2 factored form (mobile-light-10).
- Problem: at 360 px these display equations and the transform table are wider than the column and scroll sideways without a visible cue (the site-level issue already recorded). In 1.2 the hidden part is the result and its region of convergence, which the section exists to establish.
- Why it matters: minor; the ROC is restated in prose below the equation, but a phone reader sees an equation without its answer.
- Required action: split the 1.2 equation over two lines (the sum, then "= 1/(1 − az^−1), |z| > |a|"), and the 2.1 and 2.2 equations at their equals signs (an `aligned` block); the table needs the site-level scroll cue.
- Priority: minor
- Acceptance condition: at 360 px the 1.2 result with its ROC and the full right-hand sides of the 2.1 and 2.2 equations are visible without sideways scrolling.

### L3. Mermaid diagram: literal caret in a label, no caption

- Location: Section 2.1, the flow diagram after "the frequency response is a fourth" (desktop-light-05; mobile-light-09; mobile-dark-09).
- Problem: the node reads "Frequency response H(e^jω)" with a literal caret, where the text uses the typeset exponent; the diagram has no caption. At 360 px its right-hand nodes are cut (site-level issue).
- Why it matters: minor polish; the caret is plain-text notation in a page that otherwise typesets every expression.
- Required action: write the label as "H(e<sup>jω</sup>)" (Mermaid accepts HTML labels) or "H(e^{jω})" in a figure caption, and add a one-line caption ("Four descriptions of one LTI system; H(z) links them").
- Priority: minor
- Acceptance condition: on new captures the label shows a superscript exponent and the diagram has a caption.

Layout otherwise sound: the contents bar and sidebar list every section; tables 4.3 and 7 fit at 1280 px; code blocks are legible in light and dark mode (mobile-dark-27); exercise answers are collapsed. Site-level issues present on this page: no scroll cue for wide equations and the diagram at 360 px; the 7rem minimum cell width (transform table). No code ligatures seen.

## E. Technical and source findings

None. KaTeX rendered without errors; HTTP 200 on all three viewports, no page-level horizontal scroll, no overflowing element, no console error (`facts.json`). Both scripts' outputs are consistent with recomputation for this review (notch script rerun independently). Optional: in 5.2 "the moving average (phase −ω, group delay one sample)" is exact only below ω = 2π/3, where the amplitude changes sign and the phase jumps by π; a parenthetical would make it exact.

## F. Required changes

Mandatory:

- None.

Optional:

- [ ] L1: pole-zero plot and magnitude response of the 5.3 notch filter.
- [ ] L2: split the 1.2, 2.1 and 2.2 equations so that they fit at 360 px.
- [ ] L3: typeset the diagram label and add a caption.
- [ ] Cross-link Section 4.3 to Stability and Eigenvalues Section 7 (discrete-time stability from the state-space side).
- [ ] 5.2: note the π phase jump of the moving average above 2π/3.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
| L3 | | | |
