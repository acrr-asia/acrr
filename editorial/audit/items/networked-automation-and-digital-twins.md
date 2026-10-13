<!-- audit: {"slug":"networked-automation-and-digital-twins","type":"article","series":"industrial-automation","priority":"P2","before":{"purpose":4,"structure":4,"accuracy":4,"evidence":3,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":4,"optional":3}} -->
# Audit: Networked Automation and Digital Twins

- Path: `src/content/blog/networked-automation-and-digital-twins.mdx` · Route: `/blog/networked-automation-and-digital-twins` · Type: article (series entry) · Series `industrial-automation`, entry 5 of 5 · Words: 4,466 (`eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 4.
- structure 4: enterprise levels → OPC UA → MQTT → choice table → security → digital twins with a worked example and its limits.
- accuracy 4: the leak program re-run, output identical (`leak alarm at t = 941 s`, mean residual −9.76 mm). Recomputed: steady states 1.25/1.75 m, $A/k$ = 250 s, $\bar r$ = −9.29 mm (−4.65 mm for 0.0005 m³/s), $L$ = 0.0274 for 8 mm; Exercise 2 (100 vs 5 000 values per second).
- evidence 3: Kritzinger et al. without pages; title case on titles; undated standard series.
- language 3: "simply follows the fault"; several 50-60-word sentences.
- consistency 3: the series overview has no objective for this entry, so the closing paragraph closes the series against the layers rather than against stated objectives (series finding).
- publishing 2: description 392 characters; four level-2 headings in title case.

## Priority

P2.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 392 characters |
| P2 | Should fix | `:19, 116, 128, 142` | publishing | Headings in title case ("The Levels of a Manufacturing Enterprise", "Choosing How to Connect", "Security: Zones and Conduits", "Digital Twins") |
| C1 | Should fix | `:345-351` | evidence | References: Kritzinger et al. without volume/issue/pages in house form; article title in title case; IEC 62541 listed before IEC 62443, so not in order |
| D1 | Should fix | `:341` | structure | Closing paragraph does not relate the series to its objectives (depends on the overview gaining a fifth objective) |
| C2 | Optional | `:266` | language | "until the twin simply follows the fault" |
| C3 | Optional | `:15`, `:110`, `:136` | language | Sentences of 60, 59 and 57 words |
| C4 | Optional | `:114` | consistency | MQTT used as a name; the ISO/IEC 20922 title expands it. Acceptable |

### C1. References
- **Correction:** W. Kritzinger, M. Karner, G. Traar, J. Henjes and W. Sihn, "Digital twin in manufacturing: A categorical literature review and classification," *IFAC-PapersOnLine*, vol. 51, no. 11, pp. 1016–1022, 2018 (Crossref record for DOI 10.1016/j.ifacol.2018.08.474, fetched). ISO/IEC 20922:2016 kept with its year. Standard series (IEC 62264-1, IEC 62541, IEC 62443, ISO 23247) stay undated: the text cites them as series.

### D1. Closing against the objectives
- **Where:** `:341`
- **Correction:** keep the layered recapitulation (it is the series' argument) and add one sentence naming what the reader can now do, matching the objectives.

## Revision log (wave 1)
- Structure: the closing paragraph now ends with one sentence stating what a reader of the five entries can do, mapped to the five series objectives (including the new fifth). (D1)
- Prose: PubSub brokerless/broker-based sentence split into two; DMZ sentence split; "until the twin simply follows the fault" → "until the twin follows the fault itself". (C2, C3)
- Headings: four level-2 headings to sentence case. (P2)
- Metadata: description 392 → 151 characters. (P1)
- References: alphabetical; Kritzinger et al. completed to vol. 51, no. 11, pp. 1016–1022 (Crossref record for DOI 10.1016/j.ifacol.2018.08.474), title in sentence case; ISO/IEC 20922:2016 given its full title and both organizations; standard titles in their published capitalization. (C1)
- Technical content: unchanged; the leak program re-run, output identical; residual formula and Exercise 4 recomputed.
- Remaining warnings: none. Suggestions: `reference-format` ×4 (standard series IEC 62264-1, IEC 62443, IEC 62541, ISO 23247 cited as series or undated, as the text cites them); sentence-length (several 46-61-word sentences that are lists of parallel items); "actually" at line 104 ("the values actually used", contrasted with requested intervals) is meaningful; acronym false positives (SCADA, IT, OT, ANSI, ISA are expanded in the same sentence; MQTT, OLE, DCOM, IFAC are names).
- Flags for independent review: none on accuracy.
- Vietnamese translation affected: no translation of this article exists.
