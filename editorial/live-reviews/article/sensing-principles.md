# Live review: Sensing Principles: How Physical Effects Become Electrical Signals

- URL: https://acrr.asia/blog/sensing-principles
- Source: `src/content/blog/sensing-principles.mdx` (Sensor Systems, entry 2 of 7)
- Commit deployed: `7e20c2c` (master after PR #57)
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40085671258 (captured 2026-10-24 10:26 UTC): 16 desktop-light, 30 mobile-light, 30 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-24. The reviewer did not write or revise this article.
- Risk: routine (a technical explainer; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Accept with follow-up. No critical or major finding; one minor finding (L1) remains open. The contract is delivered and every worked number checked is right.

**Library decision: retain.** The page is the series' survey of transduction principles and the only place on ACRR that explains, side by side, why a thermocouple measures a difference, why a piezoelectric sensor cannot weigh, and why a pH meter needs temperature. Later entries (signal conditioning, noise, smart sensors) lean on its numbers (the 350 Ω gauge, the 0.55 A/W photodiode). It is concise (13 minutes) and not padded.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineering student or engineer new to sensors who knows basic circuit theory and wants to understand what is inside the sensors they select.
- Problem: thousands of sensor products seem unrelated; the reader needs the few physical effects behind them and what each implies for use.
- Outcome: classify a sensor by energy domain and family, state the governing equation of each family, estimate a typical signal size, and say what each principle cannot do (static force for piezoelectric, absolute temperature for thermocouples, temperature-independent slope for pH).
- Distinctive contribution: each principle with one governing equation, one worked number from typical constants and one practical consequence, ending in a selection table by measurand.
- Evidence: textbook physics and typical material constants; Fraden (2016), Pallàs-Areny and Webster (2001), Regtien and Dertien (2018), Webster and Eren (2014).
- Limitations: survey depth; typical constants rather than product data; no conditioning circuits (left to the next entry).

The benefit is delivered. The opening states three questions the page answers, and each is answered in its section (thermocouple reference junction, piezoelectric leakage, Nernst slope). The families table (Section 1) and the selection table (Section 9) frame the survey. I recomputed: NTC 33.6, 3.59 and 0.70 kΩ, −4.44%/K at 25 °C (11 times platinum's 0.39%/K); strain gauge 0.7 Ω; 8.85 pF and +0.089 pF for 1 µm; quartz 23 pC and 0.23 V; RC = 0.1 s and e^−10 = 0.0045%; type K 4.1 mV per 100 K; responsivity 0.548 A/W; Nernst 59.16 and 61.54 mV per pH. All match. The typical constants (quartz d11 ≈ 2.3 pC/N, type K ≈ 41 µV/K near room temperature, PZT one to two orders larger) agree with standard values. Value category: conceptual understanding. Format: explainer.

Overlap: optical encoders and IMU sensors are introduced in "What Is a Robot?" and "Sensing and State Estimation: An Overview" (robotics series); this page links the first and treats the physics those pages assume, so the overlap is complementary. Capacitive MEMS sensing is developed further in "Smart Sensors and MEMS" (entry 6), which links back here.

## C. Substantive findings

No substantive findings. Every section serves the central question; nothing is repeated; the summary table adds a reusable index.

## D. Visual and structural findings

### L1. No diagram for the two arrangements the text depends on

- Location: Section 4.1 (the LVDT bullet) and Section 6 (thermocouple measuring and reference junctions); desktop-light-07 and 09.
- Problem: the page has no figure at all. Two of its explanations are spatial: the LVDT's primary and two secondaries around a moving core, whose difference voltage changes sign with direction; and the thermocouple circuit, whose output depends on two junctions, one of them at the instrument terminals. Both are described only in prose.
- Why it matters: the thermocouple point is one of the three questions the opening promises to answer; a reader who has not seen the circuit has to reconstruct where the "reference junction" is. A small schematic answers it at a glance (standards 6.8).
- Required action: add one schematic (generated with `scripts/generate-diagrams.py`, as the series' other figures are) of the thermocouple circuit showing the measuring junction, the reference junction at the instrument terminals and the cold-junction sensor; optionally a second for the LVDT.
- Priority: minor
- Acceptance condition: the live page shows a captioned thermocouple schematic in Section 6, legible at 360 px in light and dark mode.

Site-level issues already recorded affect this page: at 360 px the families table (Section 1) shows only two of its four columns and the selection table (Section 9) hides most of its "Typical deciding factor" column, because of the 7rem minimum cell width (mobile-light-04, 05, 23, 24). Display equations all fit at 360 px. Dark mode correct (mobile-dark-24). No ligature artifacts.

## E. Technical and source findings

No technical or source errors found (Section B). `facts.json`: HTTP 200 on all three viewports, no horizontal page scroll at 360 px, 0 KaTeX errors, 0 broken images, 0 console errors, one h1. Internal links (previous entry, signal-conditioning entry, robotics first entry, next entry) resolve to the intended pages; the robotics link points to "What Is a Robot?", which does introduce joint encoders.

## F. Required changes

Mandatory: none (no critical or major finding).

Optional (minor, follow-up):

- [ ] L1: add a thermocouple circuit schematic to Section 6 (and optionally an LVDT schematic to Section 4.1).

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
