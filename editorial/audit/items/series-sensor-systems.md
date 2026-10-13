<!-- audit: {"slug":"sensor-systems","type":"series","series":"sensor-systems","priority":"P1","before":{"purpose":2,"structure":2,"accuracy":4,"evidence":3,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":4,"optional":1}} -->
# Audit: Sensor Systems

- Path: `src/content/series/sensor-systems.md` · Route: `/series/sensor-systems` · Type: series overview · 7 entries, published, no planned entries · Words: 80 (from `eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 2: the reader and prerequisites are stated, but the page does not say why the entries come in this order or what the reader can do at the end beyond the objectives list.
- structure 2: a single 80-word paragraph whose second sentence is a 59-word list of entry topics; standards Section 6.5 asks for the sequence rationale, how the entries connect and the shared conventions.
- evidence 3: an overview makes no claims needing sources; no issue beyond the entries.
- language 3: one 59-word sentence (lint `sentence-length`).
- consistency 3: the body does not mention the load-cell channel that entries 3 to 7 share, nor the conventions (SI, GUM vocabulary, RMS noise at 300 K, Python 3.13 and NumPy 2.5 in entry 7) the entries rely on.
- publishing 2: description 242 characters (limit 165), and it is a fragment ("A series on ..."), not a sentence.

## Priority

P1: the series front door; every entry depends on it, and its description is the series card and meta description.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `sensor-systems.md:3` | publishing | Description 242 characters and not a complete sentence. |
| D1 | Should fix | `sensor-systems.md:14` | structure | No sequence rationale or account of how entries connect (standards 6.5). |
| D2 | Should fix | `sensor-systems.md:14` | consistency | Shared conventions not stated. |
| C1 | Should fix | `sensor-systems.md:14` | language | 59-word list sentence. |
| D3 | Optional | `sensor-systems.md:11` | purpose | Objective 5 "State and combine measurement uncertainties, and calibrate and fuse sensors" bundles three outcomes; acceptable, but "calibrate" is less checkable than "fit a calibration curve with its uncertainty". Left: changing objectives changes the series contract checked by the series review. |

### P1. Description too long
- **Where:** `src/content/series/sensor-systems.md:3`
- **Text:** "A series on the measurement chain, from a physical quantity to a trustworthy number: what a measurement is, how sensors convert physical effects into signals, and how those signals are conditioned, converted, cleaned, calibrated and combined."
- **Problem:** 242 characters (standards 8.1: one complete sentence, 70–165); verbless fragment.
- **Correction:** "Follow a measurement from a physical quantity to a trustworthy number: sensing, signal conditioning, conversion, noise, smart sensors, calibration and fusion." (159 characters)

### D1. Sequence rationale and connections missing
- **Where:** line 14
- **Text:** "It starts with what a measurement is and follows the signal from the physical world to a number that can be trusted, in seven entries: measurement and sensor characteristics, sensing principles, ..."
- **Problem:** Lists the entries (which the page lists anyway) without saying why the order is the order of the measurement chain, that entry 1 supplies the vocabulary every later entry uses, or that one load-cell channel is carried from entry 3 to entry 7.
- **Correction:** Rewrite the body as: audience and prerequisites; the order (the chain of entry 1, stage by stage); the running examples (PT100 in entries 1, 3 and 7; load cell in 3 to 7); conventions.

### D2. Shared conventions
- **Problem:** Entries rely on SI units, VIM/GUM vocabulary (entry 1), noise as RMS at 300 K (entry 5), Python 3.13 with NumPy 2.5 (entry 7). The overview names none of them.
- **Correction:** One short paragraph of conventions.

### C1. Long list sentence
- **Text:** the 59-word second sentence quoted under D1.
- **Correction:** Replaced by the restructured body (D1).

## Revision log (wave 1)
- Structure: body rewritten from one 80-word paragraph into four short paragraphs: audience and prerequisites; sequence rationale (the order of the measurement chain, entry 1 as vocabulary, entries 2–5 stage by stage, entry 6 the integrated chain, entry 7 calibration and fusion); the two running examples (PT100 in entries 1, 3, 7; load cell in entries 3–7); shared conventions (SI, VIM/GUM, RMS noise at 300 K, Python 3 with NumPy in entry 7). Every statement checked against the entries.
- Metadata: description rewritten as one sentence, 158 characters. Title, status, category, objectives unchanged.
- Prose: the 59-word list sentence removed.
- Remaining suggestions: `acronym-expansion` for "PT100" (line 18): the sentence glosses it as "platinum resistance thermometer"; entry 1 explains the designation.
- Flags for independent review: series editor to confirm the overview against standards 6.5; D3 (objective 5 bundles three outcomes) left for the series editor.
- Vietnamese translation affected: yes. `src/content/series/vi/sensor-systems.md` body and description should be retranslated from the new English body (meaning expanded: sequence rationale, running examples, conventions). No copied field changed.
- Note: the series content hash changes with this wave, so `reviews/sensor-systems.md` will need a new review and `stamp` before the publication gate passes.
