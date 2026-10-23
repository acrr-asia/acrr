# Live review: Sensor Systems (series overview)

- URL: https://acrr.asia/series/sensor-systems
- Source: `src/content/series/sensor-systems.md` (seven entries, status published, no planned entries)
- Commit deployed: `1eb85d4`
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/39980397404 (2026-10-23 15:43 UTC): 4 desktop-light, 7 mobile-light, 7 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-23. The reviewer did not write or revise this page.
- Risk: routine (a series front door for technical explainers; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Accept with minor follow-up. The overview meets standards 6.5 and every promise on it is kept by the entries. One minor finding (L1) concerns the entry cards the page shows: none of the seven entry descriptions is a sentence saying what the reader will learn.

**Library decision: retain.** The page is the series' entry point; the 13 October revision replaced a single list paragraph with the sequence rationale, the two running examples and the shared conventions, and this review checked each of those statements against the entries. Nothing on it should be merged elsewhere or reclassified.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineering student or engineer comfortable with basic circuit analysis, calculus and elementary statistics, deciding whether and where to start the series.
- Problem: knowing what the seven entries cover, why they come in this order, which examples connect them and which conventions they share.
- Outcome: the reader can follow the measurement chain the series uses as its spine, knows that a PT100 and a load-cell channel recur, knows the units, the VIM/GUM vocabulary and the noise conventions, and has five checkable objectives.
- Distinctive contribution: the order is the order of the measurement chain set out in the first entry, and two running examples are traced entry by entry.
- Evidence: the entries. Checked in this review: the PT100 illustrates nonlinearity in entry 1, excitation and lead-wire errors in entry 3 and the curvature of a straight-line calibration fit in entry 7 (Section 3, residuals −0.077 to +0.062 Ω); the load-cell channel is built in entry 3 (Section 7), sampled and quantized in entry 4, given a noise budget in entry 5 and calibrated in entry 7 (Section 3.2); entry 5 computes noise at 300 K as RMS values; entry 7's code is Python 3 with NumPy.
- Limitations: an overview; total reading time (about 134 minutes from the card estimates, 38 of them for entry 7) is not stated.

The benefit is delivered. The opening screen gives the title, a one-sentence description, the category, the Published status and "Start with entry 1"; the four paragraphs that follow (reader and order, stages, running examples, conventions) each add something the entry list does not. The objectives begin with assessable verbs (describe, explain, design, state and combine). Entry 6 (smart sensors and MEMS) is the main subject of no objective; standards 6.5 does not require one per entry, so this is noted, not a finding. Value category: reference value. Format: reference.

Overlap: within the site, entry 4 (sampling and conversion) and entry 5 (noise) touch the Digital Signal Processing for Engineers series (sampling, aliasing, quantization noise); that overlap belongs in the site-level overlap map of adoption-plan Phase 3, and the entries' own reviews should judge it.

## C. Substantive findings

None.

## D. Visual and structural findings

### L1. Entry cards: the seven descriptions are fragments, most of them topic lists

- Location: the Entries list, cards 1 to 7 (desktop-light-02 to 04; mobile-light-04 to 07).
- Problem: the card summaries come from the entries' `description` fields, and every one is a verbless fragment, six of them ending in a topic list, rather than one sentence saying what the reader will learn: "What a measurement is and how to describe a sensor: the measurement chain, static and dynamic characteristics, error, uncertainty and calibration." (entry 1), "The physical effects behind most sensors, ..." (entry 2), "The analog electronics between sensor and converter: ..." (entry 3), "How a sensor voltage becomes numbers: ..." (entry 4), "What limits the smallest detectable change: ..." (entry 5), "What changes when sensor and electronics share a package: ..." (entry 6), "How to calibrate sensors with traceable uncertainty and fuse several: ..." (entry 7). Standards 8.1 asks for one complete sentence that says what the reader will learn and no list of every section; the Identity and Access Control overview shows the form ("Learn how ...").
- Why it matters: minor; the cards are still informative, but on the series front door they read as tables of contents and differ in form from other series, and the same text is the meta description and the RSS summary of each entry.
- Required action: rewrite the seven entry descriptions as one sentence each (70 to 165 characters) stating what the reader will learn, through the normal review stages of each entry (the change stales their review records), and update the Vietnamese descriptions in the same commit.
- Priority: minor
- Acceptance condition: on new captures every entry card of this page shows a one-sentence description of what the reader will learn, and no card is a list of the entry's sections.

Layout: at 1280 px entries and objectives side by side; at 360 px objectives and progress first, then the entry timeline; legible in light and dark mode (mobile-light-01 to 07, mobile-dark-01 to 07). `facts.json`: HTTP 200 on all three viewports, no horizontal scroll, no overflowing element, no console error.

## E. Technical and source findings

None. The statements about running examples and conventions were checked against the entries (see B).

## F. Required changes

Mandatory:

- None.

Optional:

- [ ] L1: one-sentence descriptions for the seven entries.
- [ ] Objective 5 ("State and combine measurement uncertainties, and calibrate and fuse sensors") bundles three outcomes (audit D3, left open); "fit a calibration curve and state its uncertainty" would be easier to check.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
