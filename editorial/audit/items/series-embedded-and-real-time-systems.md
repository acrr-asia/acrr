<!-- audit: {"slug":"embedded-and-real-time-systems","type":"series","series":"embedded-and-real-time-systems","priority":"P2","before":{"purpose":3,"structure":2,"accuracy":3,"evidence":3,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":4,"optional":1}} -->
# Audit: Embedded and Real-Time Systems

- Path: `src/content/series/embedded-and-real-time-systems.md` · Route: `/series/embedded-and-real-time-systems` · Type: series overview · 5 entries, published, no planned entries · Words: about 150
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 3: reader and prerequisites are explicit; what each entry contributes is folded into one long sentence.
- structure 2: a single 150-word paragraph mixes audience, sequence and conventions; standards 6.5 asks for the sequence rationale, how the entries connect and the shared conventions, each identifiable.
- accuracy 3: objective 4, "verify that deadlines are met by measurement", contradicts the fifth entry, whose argument is that measurement alone cannot establish a worst case (§3.2, §4.1 "the bound has to be established by analysis and checked by measurement").
- evidence 3: no claims needing sources.
- language 3: 90-word third sentence; DMA, UART, SPI, CAN not expanded (lint `acronym-expansion`).
- consistency 3: conventions (C11, Cortex-M at 48 MHz, invented register names, SI and binary prefixes, Python 3) are stated only partly.
- publishing 2: description 189 characters (limit 165) and a verbless fragment.

## Priority

P2: metadata and structure defects a reader of the series page would notice; the entries do not depend on the overview's wording.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `embedded-and-real-time-systems.md:3` | publishing | Description 189 characters, not a sentence. |
| D1 | Should fix | `:13` | structure | One paragraph; no sequence rationale or account of how entries connect. |
| D2 | Should fix | `:10` | accuracy | Objective 4 promises verification "by measurement", which entry 5 argues is impossible on its own. |
| C1 | Should fix | `:13` | language | 90-word sentence; DMA, UART, SPI, I2C, CAN unexpanded. |
| D3 | Optional | `:13` | consistency | Conventions incomplete (48 MHz clock, invented register names, units). |

### P1. Description
- **Text:** "A series on the computers inside machines: microcontroller architecture, interrupts and DMA, on-board and in-vehicle buses, real-time operating systems and scheduling, and measuring timing."
- **Problem:** 189 characters; fragment (standards 8.1).
- **Correction:** one sentence of at most 165 characters saying what the reader learns.

### D1. Sequence rationale
- **Text:** "It starts from the vocabulary of real-time systems ... and ends by measuring execution time, latency, jitter, processor load and memory use on real hardware to check those predictions."
- **Problem:** The order (hardware, then data movement, then buses, then the software organization, then measurement) is described but not justified; the overview does not say that each entry removes a limit of the previous one (superloop → interrupts/DMA → RTOS → measurement).
- **Correction:** three paragraphs: reader and prerequisites; sequence with each entry's contribution and why it comes there; conventions.

### D2. Objective 4 overclaims
- **Text:** "Explain real-time scheduling and verify that deadlines are met by measurement."
- **Problem:** Entry 5 §3.2 "Why the observed maximum is not the worst case" and §4.1 bullet 4 state that a bound must be established by analysis and checked by measurement. The objective as written promises the opposite.
- **Correction:** "Explain real-time scheduling, calculate worst-case response times and check them against measurements."

### C1. Long sentence, unexpanded abbreviations
- **Text:** third sentence of line 13 (90 words); "DMA", "UART, SPI, I2C and CAN".
- **Correction:** split; expand at first use.

### D3. Conventions
- **Correction:** state C11, generic 32-bit Arm Cortex-M at 48 MHz, invented register layouts, SI time units with binary memory prefixes, Python 3 standard library, POSIX for the desktop examples.

## Revision log (wave 1)
- Structure: body rewritten as three paragraphs: reader and prerequisites (unchanged content, plus "no prior embedded experience" from entry 1); the sequence, with each entry's contribution and the limit of the previous entry it removes (D1); shared conventions (D3), including POSIX for desktop examples.
- Objectives: objective 4 changed from "Explain real-time scheduling and verify that deadlines are met by measurement" to "Explain real-time scheduling, calculate worst-case response times and check them against measurements" (D2; evidence: entry 5 §3.2 and §4.1, which state that measurement alone cannot establish a worst case). The other three objectives are unchanged, and each is still covered by its entry (series review table).
- Prose: the 90-word sentence split; DMA, UART, SPI, I2C, CAN and POSIX expanded at first use (C1).
- Metadata: description now 151 characters, one sentence (P1). `status`, `category`, no `plannedEntries` untouched.
- Remaining warnings: none (lint 0 errors, 0 warnings).
- Flags for independent review: series editor to confirm the reworded objective 4 matches entries 4 and 5.
- Vietnamese translation affected: yes. `src/content/series/vi/embedded-and-real-time-systems.md` needs its description, body and objective 4 updated (the meaning of objective 4 changed: "calculate worst-case response times and check them against measurements" instead of "verify by measurement").
