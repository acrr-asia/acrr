# Series audit: Sensor Systems (wave 1)

- Series: `sensor-systems`, 7 entries, status published, no planned entries. Previous series review: `reviews/sensor-systems.md` (resolved; its corrections F1–F20 were checked and are all still in place: the illustrative-data label in entry 7 §3.2, the SAR half-LSB sign in entry 4 §5.1, the active/passive note and threshold/dead-band definitions in entry 1, the tilt sign convention and Laplace introduction in entry 7, the 13 300 figure in entry 5).
- Audited at commit `e21dcc8`, 2026-10-13.

## Structural consistency across entries

| Entry | Opening links previous entry | Numbered H2s | Heading case | Summary (table) | Closing transition in Summary | References | Description chars |
|---|---|---|---|---|---|---|---|
| 1 Measurement | n/a (first) | 1–8 | Title case | §8 | Yes, to entry 2 | `### References` | 293 |
| 2 Sensing principles | No ("The previous entry") | 1–10 | Title case | §10 | Yes; also duplicated at end of §9 | `### References` | 288 |
| 3 Signal conditioning | No | 1–8 | Title case | §8 | Yes | `### References` | 274 |
| 4 Sampling | No | 1–7 | Title case | §7 | Yes | `### References` | 293 |
| 5 Noise | No | 1–7 | Title case | §7 | Yes | `### References` | 302 |
| 6 Smart sensors | No | 1–6 | Title case | §6 | Yes, linked | `### References` | 359 |
| 7 Calibration | Yes (linked) | 1–10 | Title case | §9, then §10 "The Series as a Whole" | In §10, not in the Summary; does not refer to objectives | `### References` under §10 | 366 |

Every entry numbers its sections, has a Summary with a question/answer table and a forward transition, and has References. The systemic defects are:

1. **Descriptions** 242–366 characters, all fragments listing section contents (limit 165, one sentence).
2. **Title-case H2 headings** in all seven entries (lint flags only 18 of the 57; all are converted). Fragment slugs are lower case, so no link breaks.
3. **References** not in the house format of standards 7.3 ("5th edition", missing years on standards, headline-cased standard titles, non-alphabetical order). The same eight books recur; they are normalized identically in every entry.
4. **Percent spacing** ("0.2 %") throughout entries 1, 2, 3, 5, 7 against standards 5.5.
5. **British remnants** missed by `eos fix`: "micrometre(s)", "picometres" (entry 6), "standardised" (entry 2), "linearisation" (entry 1 Mermaid label).
6. **Cross-entry mentions** are mostly by description ("the signal-conditioning entry", "the noise entry", "the previous entry") and unlinked at first mention, against standards 8.1. Entry 7 links consistently; entries 2–6 rarely do.
7. **Prose tables of contents** in the openings of entries 1, 2, 5, 6, 7.

## Notation and terminology

- Consistent: self-generating/modulating, excitation, ratiometric, quarter/half/full bridge, LSB, ENBW, noise-free resolution, RMS.
- Clash: $f_c$ is both the filter cut-off (entries 3, 5 §1.3) and the 1/f corner frequency (entry 5 §2.3). Fixed in entry 5 by writing the corner as $f_\text{nc}$.
- $s$ has five meanings across entries, each disambiguated where used (previous review); left.
- "endpoint line" (entries 1, 7) and "end points" (entry 1): unified as "endpoint line", the glossary's closed compound, defined in bold in entry 1 §3.3.

## Overlap and gaps

- No harmful duplication: each later entry refers back (e.g. entry 5 §4 on averaging refers to entry 1; entry 7 §6.2 reuses entry 1's budget).
- Promises: entry 1 promises quantization (entry 4) and calibration in practice (entry 7); entry 3 promises anti-aliasing (4) and noise bandwidth (5); entry 4 promises dither (5); entry 6 promises fusion and time alignment (7). All kept.
- Gap: the "output" stage of the measurement chain in entry 1 §2.1 is not treated by any entry (noted by the previous review's F5, which reworded entry 1 accordingly). No action.

## Overview page (standards 6.5)

Fails 6.5 before revision: no sequence rationale, no account of how entries connect, no shared conventions; description too long. Objectives (5) begin with assessable verbs and are each covered (previous review's coverage table still holds). See `editorial/audit/items/series-sensor-systems.md`.

## Cross-references

- Incoming links from outside the scope: `designing-fir-and-iir-filters.mdx` → entry 4 `#21-oversampling` and `#32-quantization-error-as-uncertainty`; `verifying-and-validating-a-simulation.mdx` → entry 1 `#52-evaluating-uncertainty`; plain links from `signals-and-systems-in-discrete-time`, `from-signal-processing-to-digital-control`, `programmable-logic-controllers`, `inside-a-microcontroller`. None of these anchors change in this wave.
- Outgoing links to the robotics entry `sensing-and-state-estimation` use fragments `#4-...`, `#5-the-kalman-filter`, `#71-fusing-complementary-sensors`, `#8-engineering-details-that-decide-success`; they depend on that series keeping its section numbers and wording.
