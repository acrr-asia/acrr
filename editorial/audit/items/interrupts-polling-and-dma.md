<!-- audit: {"slug":"interrupts-polling-and-dma","type":"article","series":"embedded-and-real-time-systems","priority":"P2","before":{"purpose":4,"structure":4,"accuracy":4,"evidence":3,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":4,"optional":3}} -->
# Audit: Interrupts, Polling and DMA

- Path: `src/content/blog/interrupts-polling-and-dma.mdx` · Route: `/blog/interrupts-polling-and-dma` · Type: article · Series `embedded-and-real-time-systems`, entry 2 · Words: 4101 (from `eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 4.
- structure 4: mechanism, cost, hazards, choice; the decision table earns its place.
- accuracy 4: the series-review corrections (F1, F3, F9) are in place and correct; numbers recomputed (see Verification).
- evidence 3: references not in house format ("2nd edition", ISO title form, no year, not alphabetical).
- language 3: sentences of 51–57 words (lines 21, 107, 164); "truly in parallel"; FIFO and LR expanded in a non-standard form; "%" with a space.
- consistency 3: SRAM not expanded in this entry (line 254).
- publishing 2: description 286 characters; three H2 headings in title case.

## Priority

P2: metadata and heading defects, long sentences; content sound.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 286 characters. |
| P2 | Should fix | `:25, 134, 248, 317` | publishing | H2 headings in title case. |
| C1 | Should fix | `:21, 107, 164` | language | Sentences of 51–57 words. |
| P3 | Should fix | `:391–398` | evidence | References not in house format or order. |
| C2 | Optional | `:29, 87, 254` | language | "first-in, first-out hardware buffer, a FIFO"; "the link register LR"; "SRAM" unexpanded. |
| C3 | Optional | `:239` | language | "the two run truly in parallel" (intensifier). |
| C4 | Optional | passim | language | "2.4 %" (space before %). |

### P1. Description
- **Text:** "Three ways to move data between peripherals and memory: polling, interrupts and direct memory access. How each works, what it costs ..." (three sentences, 286 characters).
- **Correction:** one sentence ≤ 165 characters.

### C1. Long sentences
- **Text (line 21):** "The entry explains each mechanism, quantifies its latency and its cost in processor time with the timing vocabulary of [Section 1.2 ...] (event, latency, jitter, deadline), treats the problem that interrupts create ..., and ends with a way to choose."
- **Text (line 107):** "(The bound assumes the higher-priority interrupt occurs at most once during the wait; if it can recur, each recurrence adds its execution time, the same reasoning that the fourth entry formalizes as response-time analysis.)"
- **Text (line 164):** the 54-word definition of the single-producer, single-consumer ring buffer.
- **Correction:** split into two sentences each.

### P3. References
- **Correction:** "2nd ed.", "3rd ed."; ISO title "Information technology – Programming languages – C", 2011; alphabetical.

## Verification (auditor's spot checks)

Ran the load-comparison Python (identical output). Compiled and ran the ring-buffer program with `gcc -std=c11 -O2 -pthread` (identical output). Recomputed: 115 200/10 = 11 520 B/s, 86.8 µs; 12 cycles at 48 MHz = 0.25 µs; 15.25 µs ≈ 61× entry time; U = 11 520 × 100/48e6 = 2.4%, 100 000 → 20.8%, 480 000 → 100%; 256/10 kHz = 25.6 ms, 39.1 interrupts/s; Exercise 2 29.25 µs; Exercise 4 10 ms. All correct.

## Revision log (wave 1)
- Prose: the long sentences at lines 21, 107 and 164 are now two sentences each. "truly" removed. FIFO is expanded in the standard form. The register list in §3.1 no longer nests abbreviations in parentheses: LR and PC are not used again in this entry. SRAM is expanded as "static RAM (SRAM)". The space before % is removed.
- Metadata: description cut from 286 to 158 characters (one sentence). Four H2 headings are now in sentence case.
- References: house format, alphabetical, ISO/IEC 9899 in its original title with its year. The clause note "(atomics: clause 7.17)" is kept.
- Technical corrections: none. The series-review corrections F1, F3 and F9 were checked and are kept.
- Remaining warnings: none. Remaining suggestions:
  - CAN at line 389 is in a link to the next entry's title.
  - ARM DDI and MIT are proper names.
  - "Reference has no year" for Arm DDI 0403 (fact-checker flag, as in entry 1).
- Flags for independent review: Arm DDI 0403 issue and year.
- Vietnamese translation affected: no translation exists. No `updatedAt`: published 2026-10-13.
