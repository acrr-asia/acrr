# Live review: Measurement Systems and Sensor Characteristics

- URL: https://acrr.asia/blog/measurement-systems-and-sensor-characteristics
- Source: `src/content/blog/measurement-systems-and-sensor-characteristics.mdx` (Sensor Systems, entry 1)
- Commit deployed: `1eb85d4`
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/39980397404 (2026-10-23 15:43 UTC): 18 desktop-light, 32 mobile-light, 32 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-23. The reviewer did not write or revise this article.
- Risk: routine (a technical explainer; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Accept with minor follow-up. The page delivers its contract, every number on it was recomputed in this review, and the desktop page has no defect. Four minor findings remain open: three are narrow-screen presentation (L1 to L3), one is a terminology clash with the control series (L4).

**Library decision: retain.** This is the vocabulary entry of the Sensor Systems series, and the later entries depend on it by name: Calibration and Multisensor Fusion reuses its uncertainty budget and links to its Section 5 anchors, and the PT100 example runs through entries 3 and 7. The 13 October audit found only form problems (description, headings, percent spacing, reference format); all were fixed in wave 1 and are visible on the live page. Nothing elsewhere on the site covers measurement vocabulary and GUM uncertainty; a rewrite, merge or reclassification would gain nothing.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineering student or engineer with basic circuit analysis, calculus and elementary statistics (the series prerequisites) who has to specify, read a datasheet for, or report a result from a sensor.
- Problem: lacking a precise vocabulary for what a measurement is and how good a sensor is, and not knowing how to state an uncertainty.
- Outcome: describe the measurement chain; distinguish sensor, transducer and actuator, and self-generating from modulating sensors; use the static characteristics (range, sensitivity, linearity with a stated reference line, resolution, hysteresis, drift, cross-sensitivity) and the first-order dynamic model; separate systematic from random error; build a GUM uncertainty budget and report $U$ with $k$; do a two-point calibration; choose a sensor by a question list.
- Distinctive contribution: one running example (a PT100) carried through transfer function, sensitivity, nonlinearity, uncertainty and loading with every number computed, and a worked budget that shows where effort pays; the explicit decision to use "self-generating" and "modulating" because "active" and "passive" are used both ways.
- Evidence: worked calculations in the text; IEC 60751:2022 coefficients; JCGM 100:2008 (GUM) and JCGM 200:2012 (VIM); Bentley (2005); Fraden (2016); Regtien and Dertien (2018).
- Limitations: one sensor type worked in detail; second-order dynamics only described; no correlated uncertainty contributions or degrees of freedom (taken up in the series' last entry); sensing principles, conditioning and conversion deferred.

The benefit is delivered. Spot checks recomputed in this review: $R(100) = 138.506\ \Omega$; average sensitivity 0.385 Ω/°C, local slopes $R_0(A + 2BT)$ = 0.3908 and 0.3793 Ω/°C; endpoint nonlinearity at 50 °C 0.1444 Ω, 0.375 °C; $1 - e^{-1}, 1 - e^{-3}, 1 - e^{-5}$ = 63.2%, 95.0%, 99.3%, and $\tau \ln 100 = 18.4$ s ("about 20 s"); −3 dB = 0.708; $u_c = \sqrt{0.0158^2 + 0.050^2 + 0.0029^2} = 0.0525$ °C, $U = 0.105 \to 0.11$ °C; $g = 100/98.7 = 1.0132$ and $1.0132 \times 49.6 = 50.25$ °C; $I^2R = 0.139$ mW. Value density: no section is padding; Section 5.3 (the budget and the sentence on where effort pays) and the Section 7 question table are the parts a reader will reuse.

Overlap with other ACRR articles: the first-order time constant (63%, and the settling rule of thumb) also appears in Introduction to Control Systems (Section 3.3), with consistent numbers, and this page points to the control series for the models; the uncertainty vocabulary is developed further, by design and with links, in Calibration and Multisensor Fusion. See L4 for the one place where the overlap creates a clash. Value category: conceptual understanding (with reference value: the question table and the budget are revisitable). Format: explainer.

## C. Substantive findings

### L4. "Transfer function" means something different here and in the control series

- Location: Section 3.1, first sentence ("The **transfer function** (or characteristic curve) relates the sensor's output to its input"), and Section 4 (link to Foundations of Control Systems).
- Problem: on this page "transfer function" is the static input-output curve $R(T)$. Section 4 then sends the reader to the control series, whose first entry defines the transfer function as the Laplace-domain ratio $G(s) = Y(s)/U(s)$. The page does not say that the two uses differ. (The series' last entry, Calibration and Multisensor Fusion, does distinguish "the dynamic counterpart of the static transfer function of the first entry".)
- Why it matters: a reader who follows the link meets the same bold term with a different definition, in the very section (dynamic characteristics) where both meanings apply.
- Required action: one clause in Section 3.1, for example "(the static characteristic; the control series uses the same term for the Laplace-domain description of a dynamic system)", or call it the "static transfer function" at first use.
- Priority: minor
- Acceptance condition: the live page's Section 3.1 states that this is the static sense of the term and distinguishes it from the dynamic transfer function.

## D. Visual and structural findings

### L1. Display equations cut at 360 px

- Location: Section 3.1, $R(100)$ (mobile-light-11); Section 5.2, $u_c$ and $U$ (mobile-light-21); Section 6, the two-point calibration (mobile-light-23); the same tiles in dark mode.
- Problem: at 360 px each display is wider than the column and its right end is hidden behind an unmarked sideways scroll: the result "= 138.51 Ω" of $R(100)$; the definition "$U = k\,u_c$" (the reader sees "U ="); the value "= 1.0132" of $g$.
- Why it matters: small, because each hidden value is restated in the next paragraph; but the definition of $U$ is the formula the section is about.
- Required action: put each pair on its own line (two displays or an `aligned` block), or a site-level scroll cue for wide equations.
- Priority: minor
- Acceptance condition: on new 360 px captures all three displays are fully visible, or a visible cue shows that they scroll.

### L2. Uncertainty budget table: result column hidden at 360 px

- Location: Section 5.3, the budget table (mobile-light-21 and 22, mobile-dark-22).
- Problem: at 360 px only Contribution, Information and Evaluation are visible; the fourth column, the standard uncertainties 0.016, 0.050 and 0.003 °C, sits beyond the scroll shadow.
- Why it matters: the column is the outcome of each row; the values reappear in the combined-uncertainty sentence, so the reader is slowed rather than misled.
- Required action: merge Evaluation and Standard uncertainty into one column ("Type A: $s/\sqrt{n}$ = 0.016 °C"), so that three columns fit at 360 px.
- Priority: minor
- Acceptance condition: at 360 px every standard uncertainty in the table is visible without scrolling.

### L3. Nonlinearity figure clipped at 360 px

- Location: Section 3.3, the PT100 nonlinearity plot (mobile-light-13, mobile-dark-13).
- Problem: the generated figure keeps its 26rem minimum width, so at 360 px the axis stops at 80 °C, the axis label reads "tem", and the return of the curve to zero at 100 °C (which the caption names) is hidden.
- Why it matters: the caption says the error is zero at both ends; the phone reader sees only one.
- Required action: the site-level scroll cue or lower minimum width for generated figures (also recorded on Introduction to Control Systems, L3, and Feedback and System Behavior, L2).
- Priority: minor (site-wide behavior)
- Acceptance condition: at 360 px the whole plot, both ends of the curve included, is visible, or a visible cue shows that it scrolls.

At 1280 px every equation, table and figure fits (desktop-light-03 to 14). The Mermaid measurement chain is top-to-bottom and fits at 360 px in both themes (mobile-light-05 and 06, mobile-dark-05 and 06); the plot and the tables render correctly in dark mode.

## E. Technical and source findings

None. `facts.json`: HTTP 200 on all three viewports, no horizontal page scroll, no overflowing elements, 0 KaTeX errors, 0 broken images, 0 console errors.

Not verified in this review: the statement that Fraden's handbook calls a sensor needing excitation "active" (Section 2.3; the book was not available), and the IEC 60751 coefficients against the standard's text (they match the widely published values $A = 3.9083 \times 10^{-3}$, $B = -5.775 \times 10^{-7}$).

## F. Required changes

Mandatory: none.

Optional:

- [ ] L4: distinguish the static transfer function from the control series' dynamic one.
- [ ] L1: split the three displays for narrow screens.
- [ ] L2: three-column budget table.
- [ ] L3: scroll cue or smaller minimum width for generated figures (site-level).
- [ ] Opening, second paragraph: "It assumes only the prerequisites of the series" does not say what they are; naming them (basic circuit analysis, calculus, elementary statistics) or linking the series page would let a reader arriving from search check them.
- [ ] Section 4.1: "rises towards"; American usage prefers "toward", which What Is a Robot? and Introduction to Control Systems use (not a house rule; the glossary does not list it).

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
| L3 | | | |
| L4 | | | |
