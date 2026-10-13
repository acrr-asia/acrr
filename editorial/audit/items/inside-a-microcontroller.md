<!-- audit: {"slug":"inside-a-microcontroller","type":"article","series":"embedded-and-real-time-systems","priority":"P1","before":{"purpose":4,"structure":4,"accuracy":4,"evidence":3,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":5,"optional":3}} -->
# Audit: Inside a Microcontroller

- Path: `src/content/blog/inside-a-microcontroller.mdx` · Route: `/blog/inside-a-microcontroller` · Type: article · Series `embedded-and-real-time-systems`, entry 1 · Words: 4924 (from `eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 4.
- structure 4: context (§1), concept (§2), mechanism (§§3–6), firmware structure (§7), exercises, summary; roadmap redundancy already cut by the series review (F8).
- accuracy 4: recomputed every number (see Verification); the timer script and the GPIO program reproduce their printed output exactly.
- evidence 3: references not in house format (Section 7.3): "3rd edition" instead of "3rd ed.", ISO standard without a year, title not in its original form, list not alphabetical; Arm DDI 0403 has no year or revision.
- language 3: four sentences of 53–74 words; "OR in the bit"; "internal RC oscillator (resistor-capacitor)" puts the expansion after the abbreviation; British "zero-initialised" twice; "%" written with a space (standards 5.5: no space before %).
- consistency 3: spelling variant ("zero-initialised" vs "initialized" in the same exercise).
- publishing 2: description 332 characters; five H2 headings in title case (lint `heading-case`).

## Priority

P1: the foundational first entry; every later entry cites its §1.2 vocabulary and §§3–6.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 332 characters; a list of every section. |
| P2 | Should fix | `:23, 70, 104, 219, 322, 348` | publishing | H2 headings in title case. |
| C1 | Should fix | `:427, 432` | language | "zero-initialised" (British) next to "initialized". |
| C2 | Should fix | `:89, 223, 248, 380, 382` | language | Sentences of 53–74 words. |
| P3 | Should fix | `:453–460` | evidence | References not in house format, not alphabetical; ISO entry lacks year. |
| C3 | Optional | `:217, 244` etc. | language | "12 %", "a few percent": space before % (standards 5.5). |
| C4 | Optional | `:238, 355, 198` | language | "RC oscillator (resistor-capacitor)", "hardware abstraction layer, HAL", "OR in the bit". |
| A1 | Optional | `:456` | evidence | Arm DDI 0403 cited without year or issue; flag for fact-checker. |

### P1. Description
- **Text:** "What embedded and real-time systems are and the vocabulary of deadlines, latency and jitter, then the parts of a microcontroller and how firmware drives them: the CPU core, flash and SRAM, ..."
- **Correction:** "The timing vocabulary of real-time systems and the parts of a microcontroller, from core and memory map to clocks, timers, GPIO and ADC, and how firmware drives them." (rewritten as a sentence in revision)

### P2. Heading case
- **Text:** "## 2. The Microcontroller as a System on a Chip", "## 4. Reset, Startup and Clocks", "## 7. How Firmware Drives the Hardware" and others.
- **Correction:** sentence case; anchors are unchanged because slugs are lowercase.

### C1. Spelling variant
- **Text:** "6 KiB of zero-initialised ones"; "The zero-initialised ones (`.bss`)".
- **Correction:** "zero-initialized" (standards 5.1).

### C2. Long sentences
- **Text (line 223, 74 words):** "On Cortex-M cores, that place is described by the **vector table** ... (A chip whose flash sits at a higher address ...) The first word is the initial value of the stack pointer, the second the address of the **reset handler**, the function that runs first; the following words are ..."
- **Correction:** split at the semicolons; similar for lines 89 (register list), 248 (clock gating), 380, 382.

### P3. References
- **Text:** "J. Yiu, *The Definitive Guide to ARM Cortex-M3 and Cortex-M4 Processors*, 3rd edition, Newnes, 2014." and "ISO/IEC 9899:2011, *Information Technology: Programming Languages: C*, International Organization for Standardization."
- **Correction:** "3rd ed."; ISO title in its original form "Information technology – Programming languages – C" with year 2011; alphabetical order.

### C4. Abbreviation order and jargon
- **Correction:** "internal resistor-capacitor (RC) oscillator"; "a hardware abstraction layer (HAL)"; "combine it with the bit by a bitwise OR".

### A1. Arm manual edition
- **Text:** "Arm Limited, *Armv7-M Architecture Reference Manual*, document ARM DDI 0403."
- **Problem:** no issue letter or year; the content cited (memory map, exception entry) is stable across issues, so not wrong, but incomplete. Not verified here (no access to Arm's document index from this session). Flag for the fact-checker.

## Verification (auditor's spot checks)

Ran the timer-settings Python (output identical), compiled and ran the GPIO program with GCC (output identical). Recomputed with python3: 1/48 MHz = 20.83 ns; 4000 B, 8000/65536 = 12.2%; 20 ppm × 86 400 s = 1.728 s; 65 536/48 MHz = 1.365 ms; 2^32/48 MHz = 89.48 s; log2 2400 = 11.23; 3.3/4096 = 0.806 mV; 15/12 MHz = 1.25 µs; Exercise 1 2.083 µs; Exercise 2 2.417 V; Exercise 4 log2 1920 = 10.91. All correct.

## Revision log (wave 1)
- Structure: no reorganization needed (the series review had already cut the duplicated roadmap).
- Prose: split the long sentences at §2.2 (core registers), §4.1 (vector table), §4.3 (clock gating) and the two closing sentences of §7.2. "OR in the bit" became "set the bit with a bitwise OR". "Timers are the most used peripheral" softened to "among the most used peripherals" (an unsupported superlative).
- Terminology/style: "zero-initialised" became "zero-initialized" (twice). "internal RC oscillator (resistor-capacitor)" became "internal resistor-capacitor (RC) oscillator". The HAL is now expanded in the standard form. Removed the space before % in prose.
- Metadata: description cut from 332 to 154 characters; the six title-case H2 headings are now sentence case (anchors unchanged).
- References: house format ("2nd ed.", "3rd ed."); ISO/IEC 9899 title in its original form, with the year 2011; alphabetical order. No source was added or removed.
- Cross-references: unchanged; all anchors still resolve, because the heading slugs are case-insensitive.
- Technical corrections: none needed. All numbers and both programs were recomputed and reproduce.
- Remaining warnings and why they stay: none. Remaining suggestions:
  - acronym-expansion for DMA, UART, SPI and CAN at lines 65–66: these are entry titles inside links in the §1.3 table, and the terms are expanded where they are discussed.
  - GNU, RISC(-V), ARM DDI and MIT are proper names or document numbers.
  - SRAM at line 95 is the heading of §2.3; it is expanded in the first sentence of that section.
  - "OR" at line 198 is the bitwise operation.
  - "Reference has no year" for Arm DDI 0403: see the flag below.
  - The 58-word count at line 223 comes from the linter joining a parenthetical sentence to the next one; three sentences of 46 words are left as they read clearly.
- Flags for independent review: the fact-checker should give Arm DDI 0403 its issue and year (A1); this was not verified in this session.
- Vietnamese translation affected: no translation exists (`src/content/blog/vi/inside-a-microcontroller.mdx` absent). No `updatedAt`: published 2026-10-13.
