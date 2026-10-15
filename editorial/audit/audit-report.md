# ACRR website audit report

- Site: https://acrr.asia (repository `acrr-asia/acrr`)
- Baseline audited: `master` at `2ace6e3` (13 October 2026), after the house spelling pass (`21132bc`, `e21dcc8`); item audits were made at `e21dcc8`
- Standards applied: `editorial/standards.md` v1.0 (Policies A to E, rubric, critical conditions C1 to C9)
- Method: the `content-audit` skill of `plugins/editorial-os`. Deterministic checks (`eos inventory`, `eos lint`, `eos refs`, `eos validate-site`, the site build and `scripts/check-links.mjs`) on every item and every built page; then a full reading of every item by ten editors working in parallel, one per series plus one for the insights, the standalone article and Learning, each writing an item audit and a scope audit before revising anything.
- Detail: one audit per item in [`items/`](items/), one per series in [`series/`](series/); the independent reviews that followed are in `reviews/<series-id>.md` and [`review/standalone.md`](review/standalone.md).

## 1. Inventory

| Kind | Count | Notes |
|---|---|---|
| Articles (English) | 48 | 47 in nine series and one standalone article (`numerical-integration-notes`) |
| Series overviews | 9 | all complete (status published, no planned entries) |
| Insights | 6 | Established / Interpretation / Open questions |
| Learning entries | 6 | all "planned", no URLs (correct: none exist) |
| Static pages | Home, Blog, Series, Insights, Learning, About, 404, tags index | plus 5 category listings and 95 tag pages |
| Vietnamese translations | 21 articles, 9 series, 6 insights | under `/vi`; 142 built pages |
| Built pages | 314 | 172 English, 142 Vietnamese |
| References | 224 entries (176 distinct works) at baseline | 316 entries (241 distinct) after revision |

The full machine inventory (routes, translations, references, lint counts, review stage per item) is produced by `npm run eos -- inventory --md`.

## 2. Overall assessment

The technical substance was strong. Every code block in the corpus was re-run and reproduced its printed output, and almost every worked number recomputed correctly. The previous series reviews had already removed most technical errors. The weaknesses were editorial and site-wide:

| Dimension (0 to 4) | Mean before | Main cause |
|---|---|---|
| Purpose | 3.34 | openings that listed sections instead of stating the reader, the question and the conventions |
| Structure | 3.16 | missing Summary or References in some entries; closing sections placed after the Summary; duplicate and unnumbered headings |
| Accuracy | 3.84 | few errors; most found were stale facts (standards and RFCs superseded since writing) |
| Evidence | 2.80 | reference lists missing or in many formats; named results without a source; "The specifications" lists of bare RFC numbers |
| Language | 2.95 | mixed British and American spelling; title-case headings; long sentences; intensifiers; contractions |
| Consistency | 2.86 | the same work cited in different forms; cross-references by ordinal with no link; tag labels in several styles |
| Publishing | 2.17 | meta descriptions of 190 to 465 characters (search engines show about 160); heading-level jump; a glued inline link |

Priority: 15 items P1 (foundational entries, items with a blocking finding, and overviews that failed section 6.5 of the standards), 48 P2, 1 P3. Findings at audit: 13 blocking, 312 should fix, 160 optional.

## 3. Site-wide findings

1. **Spelling variant.** The corpus mixed British and American spelling, in some articles within one paragraph. Decision: American English (standards 4.1), applied mechanically by `eos fix` to prose only (292 changes in 40 files; reference titles exempt), then by hand where the rule cannot see (diagram labels, code comments, printed program output).
2. **Meta descriptions.** All 63 English items had descriptions of 189 to 423 characters that listed the sections. They are the search-result snippet and the card summary. Remediation: one sentence of 70 to 165 characters saying what the reader learns. Vietnamese descriptions inherited the problem (34 pages over 170 characters in `/vi`).
3. **Headings.** About 146 headings in title case; house style is sentence case. Duplicate subheadings in three articles made fragment links ambiguous. One article jumped from h1 to h3.
4. **References.** Six Identity entries had no References list, only "The specifications" with bare RFC numbers; the Foundations entries 1 to 3 had none. Formats varied ("2nd edition", "22(3), 1951", commas outside quotation marks, unsorted). Remediation: simplified IEEE format (standards 5.4), alphabetical, with volume, issue and pages only where verified.
5. **Cross-references.** Mentions of other entries ("the first entry", "the previous entry") were rarely linked; about 40 in the Identity series alone. Remediation: link at first mention; `eos lint` checks that an ordinal points to the entry it names.
6. **Series overviews.** None met section 6.5 of the standards: no stated reader and prerequisites, no reason for the order of the entries, no shared conventions; three series had objectives that no entry delivered or that contradicted an entry.
7. **Insights** had no framing paragraph and no links to the in-depth articles on the same subject (blocking under C7).
8. **Stale facts.** NIST SP 800-63B revision 3 (withdrawn 2025), the IETF browser-based-apps draft (now RFC 10017), WebAuthn Level 3 (W3C Recommendation 2026), IEC/IEEE 60802 (published 2026), IEC 61784 (2023 editions), IEEE 1241 (2010 edition inactive).
9. **Tag labels** in three styles (`control-theory`, `machine learning`, `fft`, `iec 61131-3`): normalized to plain terms with their proper capitalization; tag URLs are unchanged.
10. **Static pages.** Home described the site as "at an early stage" with planned series, although all nine series were complete; About described the review process only in general terms; British spellings on Home, About, Learning and the Explore menu; the Vietnamese 404 page glued "hoặc" to a link. Remediation: Home states the published scope with counts computed from the content; About gains an "Editorial standards" section that describes the review stages (not people); spelling fixed; 404 fixed.

## 4. Per-item scores before revision

Scores are the audit's provisional scores (0 to 4 per dimension, total out of 28). Findings are blocking / should fix / optional.

| Item | Type | Scope | Priority | Pur | Str | Acc | Evi | Lang | Cons | Pub | Total | Findings |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [series-identity-and-access-control](items/series-identity-and-access-control.md) | series | identity-and-access-control | P1 | 2 | 2 | 4 | 3 | 3 | 3 | 3 | 20 | 0/4/1 |
| [authenticators-passwords-otp-passkeys](items/authenticators-passwords-otp-passkeys.md) | article | identity-and-access-control | P2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 19 | 0/7/2 |
| [authorization-models](items/authorization-models.md) | article | identity-and-access-control | P2 | 3 | 3 | 4 | 2 | 3 | 3 | 2 | 20 | 0/6/2 |
| [oauth-grants-and-client-types](items/oauth-grants-and-client-types.md) | article | identity-and-access-control | P2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 19 | 0/6/1 |
| [sender-constrained-tokens](items/sender-constrained-tokens.md) | article | identity-and-access-control | P2 | 3 | 3 | 4 | 2 | 3 | 3 | 2 | 20 | 0/5/2 |
| [service-to-service-authentication](items/service-to-service-authentication.md) | article | identity-and-access-control | P2 | 3 | 2 | 4 | 2 | 3 | 3 | 2 | 19 | 0/6/2 |
| [sessions-and-cookies](items/sessions-and-cookies.md) | article | identity-and-access-control | P2 | 3 | 3 | 4 | 2 | 3 | 3 | 2 | 20 | 0/6/2 |
| [token-based-authentication](items/token-based-authentication.md) | article | identity-and-access-control | P1 | 3 | 3 | 4 | 2 | 3 | 3 | 2 | 20 | 0/7/3 |
| [feedback-and-system-behavior](items/feedback-and-system-behavior.md) | article | foundations-of-control-systems | P1 | 3 | 2 | 3 | 1 | 3 | 2 | 2 | 16 | 1/6/2 |
| [introduction-to-control-systems](items/introduction-to-control-systems.md) | article | foundations-of-control-systems | P1 | 3 | 2 | 3 | 1 | 3 | 2 | 2 | 16 | 1/7/2 |
| [foundations-of-control-systems](items/series-foundations-of-control-systems.md) | series | foundations-of-control-systems | P2 | 3 | 2 | 4 | 4 | 3 | 3 | 3 | 22 | 0/3/1 |
| [stability-and-eigenvalues](items/stability-and-eigenvalues.md) | article | foundations-of-control-systems | P2 | 4 | 3 | 3 | 3 | 3 | 2 | 2 | 20 | 1/4/2 |
| [state-feedback-controller-design](items/state-feedback-controller-design.md) | article | foundations-of-control-systems | P2 | 4 | 3 | 4 | 3 | 3 | 2 | 2 | 21 | 0/5/2 |
| [state-space-models-primer](items/state-space-models-primer.md) | article | foundations-of-control-systems | P1 | 2 | 2 | 3 | 1 | 3 | 2 | 2 | 15 | 1/6/2 |
| [evaluating-models-honestly](items/evaluating-models-honestly.md) | article | machine-learning-fundamentals | P2 | 4 | 4 | 4 | 3 | 3 | 3 | 2 | 23 | 0/5/5 |
| [generalization-overfitting-and-regularization](items/generalization-overfitting-and-regularization.md) | article | machine-learning-fundamentals | P2 | 4 | 4 | 4 | 3 | 3 | 3 | 2 | 23 | 0/5/5 |
| [gradient-descent-and-its-variants](items/gradient-descent-and-its-variants.md) | article | machine-learning-fundamentals | P2 | 4 | 4 | 4 | 3 | 3 | 3 | 2 | 23 | 0/5/4 |
| [learning-from-data](items/learning-from-data.md) | article | machine-learning-fundamentals | P1 | 4 | 4 | 4 | 3 | 3 | 3 | 2 | 23 | 0/4/5 |
| [machine-learning-fundamentals](items/series-machine-learning-fundamentals.md) | series | machine-learning-fundamentals | P2 | 3 | 2 | 4 | 4 | 3 | 3 | 4 | 23 | 0/3/2 |
| [coordinate-frames-and-transformations](items/coordinate-frames-and-transformations.md) | article | introduction-to-robotics | P2 | 3 | 3 | 4 | 3 | 3 | 3 | 2 | 21 | 0/6/2 |
| [planar-arm-kinematics](items/planar-arm-kinematics.md) | article | introduction-to-robotics | P2 | 4 | 3 | 4 | 2 | 3 | 3 | 2 | 21 | 0/7/2 |
| [sensing-and-state-estimation](items/sensing-and-state-estimation.md) | article | introduction-to-robotics | P2 | 3 | 2 | 4 | 2 | 3 | 3 | 2 | 19 | 0/8/3 |
| [introduction-to-robotics](items/series-introduction-to-robotics.md) | series | introduction-to-robotics | P2 | 3 | 2 | 4 | 4 | 3 | 3 | 4 | 23 | 0/3/1 |
| [what-is-a-robot](items/what-is-a-robot.md) | article | introduction-to-robotics | P1 | 3 | 3 | 4 | 2 | 3 | 3 | 2 | 20 | 1/7/3 |
| [calibration-and-multisensor-fusion](items/calibration-and-multisensor-fusion.md) | article | sensor-systems | P2 | 4 | 2 | 4 | 3 | 3 | 3 | 2 | 21 | 0/5/4 |
| [measurement-systems-and-sensor-characteristics](items/measurement-systems-and-sensor-characteristics.md) | article | sensor-systems | P1 | 4 | 3 | 4 | 3 | 3 | 3 | 2 | 22 | 0/5/3 |
| [noise-interference-and-limits-of-detection](items/noise-interference-and-limits-of-detection.md) | article | sensor-systems | P2 | 4 | 3 | 4 | 3 | 3 | 2 | 2 | 21 | 0/5/3 |
| [sampling-quantization-and-data-conversion](items/sampling-quantization-and-data-conversion.md) | article | sensor-systems | P2 | 4 | 4 | 4 | 3 | 3 | 3 | 2 | 23 | 0/3/3 |
| [sensing-principles](items/sensing-principles.md) | article | sensor-systems | P2 | 3 | 3 | 4 | 3 | 3 | 3 | 2 | 21 | 0/5/3 |
| [sensor-systems](items/series-sensor-systems.md) | series | sensor-systems | P1 | 2 | 2 | 4 | 3 | 3 | 3 | 2 | 19 | 0/4/1 |
| [signal-conditioning](items/signal-conditioning.md) | article | sensor-systems | P2 | 4 | 3 | 4 | 3 | 3 | 3 | 2 | 22 | 0/4/3 |
| [smart-sensors-and-mems](items/smart-sensors-and-mems.md) | article | sensor-systems | P2 | 4 | 3 | 4 | 3 | 2 | 3 | 2 | 21 | 0/5/2 |
| [designing-fir-and-iir-filters](items/designing-fir-and-iir-filters.md) | article | digital-signal-processing | P2 | 4 | 4 | 4 | 3 | 3 | 2 | 2 | 22 | 0/6/4 |
| [dft-and-fft](items/dft-and-fft.md) | article | digital-signal-processing | P2 | 4 | 4 | 4 | 3 | 3 | 3 | 2 | 23 | 0/5/5 |
| [from-signal-processing-to-digital-control](items/from-signal-processing-to-digital-control.md) | article | digital-signal-processing | P2 | 4 | 4 | 4 | 3 | 3 | 3 | 2 | 23 | 0/5/4 |
| [digital-signal-processing](items/series-digital-signal-processing.md) | series | digital-signal-processing | P2 | 3 | 3 | 4 | 4 | 3 | 3 | 2 | 22 | 0/4/2 |
| [signals-and-systems-in-discrete-time](items/signals-and-systems-in-discrete-time.md) | article | digital-signal-processing | P1 | 4 | 3 | 4 | 3 | 3 | 3 | 2 | 22 | 1/6/4 |
| [z-transform-poles-and-stability](items/z-transform-poles-and-stability.md) | article | digital-signal-processing | P2 | 3 | 4 | 4 | 3 | 3 | 3 | 2 | 22 | 0/5/3 |
| [inside-a-microcontroller](items/inside-a-microcontroller.md) | article | embedded-and-real-time-systems | P1 | 4 | 4 | 4 | 3 | 3 | 3 | 2 | 23 | 0/5/3 |
| [interrupts-polling-and-dma](items/interrupts-polling-and-dma.md) | article | embedded-and-real-time-systems | P2 | 4 | 4 | 4 | 3 | 3 | 3 | 2 | 23 | 0/4/3 |
| [measuring-timing-latency-and-resource-use](items/measuring-timing-latency-and-resource-use.md) | article | embedded-and-real-time-systems | P2 | 4 | 4 | 4 | 3 | 3 | 3 | 2 | 23 | 0/4/4 |
| [real-time-operating-systems-and-scheduling](items/real-time-operating-systems-and-scheduling.md) | article | embedded-and-real-time-systems | P2 | 4 | 4 | 4 | 3 | 3 | 3 | 2 | 23 | 0/4/4 |
| [serial-buses-uart-spi-i2c-and-can](items/serial-buses-uart-spi-i2c-and-can.md) | article | embedded-and-real-time-systems | P2 | 4 | 4 | 4 | 3 | 3 | 3 | 2 | 23 | 0/6/3 |
| [embedded-and-real-time-systems](items/series-embedded-and-real-time-systems.md) | series | embedded-and-real-time-systems | P2 | 3 | 2 | 3 | 3 | 3 | 3 | 2 | 19 | 0/4/1 |
| [finite-differences-for-heat-and-waves](items/finite-differences-for-heat-and-waves.md) | article | numerical-simulation | P2 | 4 | 4 | 3 | 3 | 3 | 3 | 2 | 22 | 0/6/2 |
| [finite-element-method](items/finite-element-method.md) | article | numerical-simulation | P2 | 4 | 4 | 4 | 3 | 3 | 3 | 2 | 23 | 0/5/3 |
| [from-differential-equations-to-discrete-problems](items/from-differential-equations-to-discrete-problems.md) | article | numerical-simulation | P1 | 4 | 4 | 4 | 3 | 3 | 3 | 2 | 23 | 0/5/3 |
| [numerical-simulation](items/series-numerical-simulation.md) | series | numerical-simulation | P2 | 3 | 2 | 4 | 4 | 2 | 3 | 2 | 20 | 0/4/1 |
| [solving-large-linear-systems](items/solving-large-linear-systems.md) | article | numerical-simulation | P2 | 4 | 4 | 4 | 3 | 3 | 3 | 2 | 23 | 0/6/2 |
| [verifying-and-validating-a-simulation](items/verifying-and-validating-a-simulation.md) | article | numerical-simulation | P2 | 4 | 4 | 4 | 3 | 3 | 3 | 2 | 23 | 0/6/2 |
| [fieldbuses-and-industrial-ethernet](items/fieldbuses-and-industrial-ethernet.md) | article | industrial-automation | P2 | 4 | 4 | 3 | 2 | 3 | 3 | 2 | 21 | 0/5/3 |
| [logic-and-sequential-control](items/logic-and-sequential-control.md) | article | industrial-automation | P1 | 4 | 4 | 4 | 3 | 3 | 3 | 2 | 23 | 0/4/4 |
| [networked-automation-and-digital-twins](items/networked-automation-and-digital-twins.md) | article | industrial-automation | P2 | 4 | 4 | 4 | 3 | 3 | 3 | 2 | 23 | 0/4/3 |
| [pid-control-of-process-variables](items/pid-control-of-process-variables.md) | article | industrial-automation | P2 | 4 | 4 | 4 | 3 | 3 | 4 | 2 | 24 | 0/3/4 |
| [programmable-logic-controllers](items/programmable-logic-controllers.md) | article | industrial-automation | P2 | 4 | 4 | 4 | 3 | 3 | 3 | 2 | 23 | 0/4/3 |
| [industrial-automation](items/series-industrial-automation.md) | series | industrial-automation | P1 | 3 | 2 | 4 | 4 | 2 | 2 | 2 | 19 | 0/4/1 |
| [closing-the-sim-to-real-gap](items/closing-the-sim-to-real-gap.md) | insight | standalone | P2 | 2 | 3 | 4 | 3 | 3 | 3 | 2 | 20 | 1/4/1 |
| [compute-bound-or-memory-bound](items/compute-bound-or-memory-bound.md) | insight | standalone | P2 | 2 | 3 | 4 | 2 | 3 | 3 | 2 | 19 | 1/4/1 |
| [control-vs-learning-approaches](items/control-vs-learning-approaches.md) | insight | standalone | P2 | 2 | 3 | 4 | 3 | 3 | 2 | 3 | 20 | 1/4/1 |
| [floating-point-in-long-simulations](items/floating-point-in-long-simulations.md) | insight | standalone | P2 | 2 | 3 | 4 | 3 | 3 | 3 | 3 | 21 | 1/3/1 |
| [learning](items/learning.md) | learning | standalone | P3 | 3 | 4 | 3 | 4 | 3 | 3 | 4 | 24 | 0/2/1 |
| [numerical-integration-notes](items/numerical-integration-notes.md) | article | standalone | P1 | 2 | 2 | 4 | 1 | 3 | 3 | 2 | 17 | 1/6/2 |
| [what-makes-a-simulation-trustworthy](items/what-makes-a-simulation-trustworthy.md) | insight | standalone | P2 | 2 | 3 | 4 | 3 | 3 | 2 | 2 | 19 | 1/5/1 |
| [when-a-kalman-filter-is-enough](items/when-a-kalman-filter-is-enough.md) | insight | standalone | P2 | 2 | 3 | 4 | 3 | 3 | 3 | 3 | 21 | 1/3/1 |

Thresholds (standards Policy E): an article needs 24, an insight or series overview 22, and at least 3 in every dimension. Before revision no item met the publishing threshold, because of the meta descriptions alone.

## 5. Remediation plan

| Order | Work | Owner (role) | Acceptance criteria |
|---|---|---|---|
| 1 | House spelling, terminology and phrases, site-wide | Copy Editor (with `eos fix`) | `eos lint` reports no `spelling-variant` or `terminology` errors; reference titles unchanged |
| 2 | Static pages: Home, About, Learning, Explore menu, 404 | Managing Editor | No claim the content does not support; counts computed from content; no glued inline text in `dist/` |
| 3 | Per scope, P1 items first: openings, structure, descriptions, headings, references, cross-reference links, overview per 6.5 | Developmental and Copy Editors (one editor per scope) | Item audit's blocking and should-fix findings applied or answered in its revision log; `eos lint` 0 errors; `eos syntax` passes; copied front-matter fields unchanged |
| 4 | Independent review of every scope | Fact-Checking Editor, Subject-Matter Editor, Series Editor (an editor who did not revise the scope) | Report in `reviews/<id>.md` with evidence for every finding and a not-verified list |
| 5 | Resolution of the review | Author | Every blocking and should-fix finding fixed or answered in a Resolution section |
| 6 | Final gate per item | QA Editor (independent) | Resolution confirmed; rubric thresholds met; no critical condition; `eos record` decision "publish"; `eos gate` passes; series stamped |
| 7 | Publishing checks for the whole site | Technical Publishing Editor | Build, `check:links`, `eos validate-site` (English pages) and the series gate pass in CI |
| 8 | Vietnamese descriptions and series pages brought in step with the revised English | Translation (follow-up) | Vietnamese meta descriptions within limits; series overviews translate the current English |

Steps 1 to 7 are complete; the outcome per item is in each review record (`editorial/records/`) and summarized in the Testing and Validation Report. Step 8 is reported there with its status.
