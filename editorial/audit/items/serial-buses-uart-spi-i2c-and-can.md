<!-- audit: {"slug":"serial-buses-uart-spi-i2c-and-can","type":"article","series":"embedded-and-real-time-systems","priority":"P2","before":{"purpose":4,"structure":4,"accuracy":4,"evidence":3,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":6,"optional":3}} -->
# Audit: Serial Buses: UART, SPI, I2C and CAN

- Path: `src/content/blog/serial-buses-uart-spi-i2c-and-can.mdx` · Route: `/blog/serial-buses-uart-spi-i2c-and-can` · Type: article · Series `embedded-and-real-time-systems`, entry 3 · Words: about 5000
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 4.
- structure 4: common frame (§1.2) applied to each bus, then comparison.
- accuracy 4: CAN CRC script reproduces output; all worked numbers recomputed (Verification).
- evidence 3: references not in house format; the Davis et al. title is in sentence case here but in title case in `fieldbuses-and-industrial-ethernet.mdx:373`; ISO titles paraphrased with colons; no years on the ISO entries.
- language 3: sentences of 50–66 words (lines 42, 192, 303, 325); British "resynchronising", "resynchronise", "resynchronisation"; "RC oscillator" unexpanded; RTS/CTS and GPS expanded in a non-standard form or not at all; "CAN FD" used in Conventions before "flexible data rate" is expanded in §5.8.
- consistency 3: spelling variants; the Davis attribution at line 225 ("a result worked out in detail by Davis ...") reads differently from the corrected wording of the fourth entry §2.4 (series review S2).
- publishing 2: description 303 characters; H2 headings in title case; duplicate H3 heading "The frame" (lines 46 and 227).

## Priority

P2.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 303 characters. |
| P2 | Should fix | `:21, 335` | publishing | H2 headings in title case. |
| P3 | Should fix | `:46, 227` | publishing | Duplicate heading "The frame" (lint `heading-duplicate`). |
| C1 | Should fix | `:42, 246, 340` | consistency | British spellings of "resynchronize". |
| C2 | Should fix | `:42, 192, 303, 325` | language | Sentences of 50–66 words. |
| P4 | Should fix | `:413–423` | evidence | References not in house format; Davis title capitalization differs from the published title. |
| D1 | Optional | `:225` | consistency | Davis attribution worded differently from entry 4 §2.4. |
| C3 | Optional | `:17, 19, 71, 82, 346` | language | Abbreviation forms (UART/SPI/I2C/CAN bold-then-expansion; CAN FD; RC; RTS/CTS; GPS). |
| C4 | Optional | passim | language | "+0.16 %", "80 %" (space before %). |

### P3. Duplicate heading
- **Text:** "### 2.1 The frame" and "### 5.4 The frame".
- **Correction:** "### 2.1 The UART frame", "### 5.4 The CAN data frame". No link in `src/content` targets either anchor (grep for `#21-the-frame`, `#54-the-frame`: none).

### P4. References
- **Text:** "R. I. Davis, A. Burns, R. J. Bril and J. J. Lukkien, "Controller Area Network (CAN) schedulability analysis: Refuted, revisited and revised", *Real-Time Systems*, 35(3), 2007."
- **Problem:** house format needs `vol. 35, no. 3, pp. 239–272` and the comma inside the closing quote. The published title (Springer page for doi 10.1007/s11241-007-9012-7, fetched 2026-10-13) is "Controller Area Network (CAN) schedulability analysis: Refuted, revisited and revised"; pages 239–272. This entry already uses that capitalization; `fieldbuses-and-industrial-ethernet.mdx:373` (out of scope) uses title case.
- **Correction:** house format with verified pages; report the out-of-scope variant to the orchestrator.

### D1. Davis attribution
- **Text:** "The response-time analysis of the fourth entry applies to CAN messages with that non-preemption taken into account, a result worked out in detail by Davis, Burns, Bril and Lukkien (2007)."
- **Correction:** "...applies to CAN messages once that non-preemption is taken into account; Davis, Burns, Bril and Lukkien (2007) gave the corrected form of that analysis."

## Verification (auditor's spot checks)

Ran the CAN frame script (identical output). Recomputed: 0.5/9.5 = 5.26%; (0.5 − 1/16)/9.5 = 4.61%; 48e6/(16·115 200) = 26.04 → 115 385 baud, +0.16%; 16e6 → 8.68 → 111 111, −3.55%; ln(0.7/0.3) = 0.8473; 967 Ω, 1770 Ω, 5901 Ω; Exercise 2 885 Ω, 2950 Ω; 81 clocks at 400 kHz = 202.5 µs (28.9× 7 µs); worst-case 8-byte frame 135 bits, 270 µs, 47%; Exercise 4 95 bits, 380 µs, 38%; Exercise 1 9615 baud; binary forms of 0x65A, 0x652, 0x6A0, 0x100, 0x0FF and the arbitration outcomes. Bus length: (375 − 175)/5 = 40 m, (750 − 175)/5 = 115 m. All correct.

## Revision log (wave 1)
- Structure: the duplicate H3 headings were renamed "2.1 The UART frame" and "5.4 The CAN data frame". No link anywhere in `src/content` targets the old anchors.
- Prose:
  - The introduction now expands UART, SPI, I2C and CAN in plain text; the bold definitions stay in their sections.
  - CAN FD is expanded in the Conventions paragraph.
  - The long sentences in §1.2, §4.5, §5.5 and §5.6 are split; the §5.6 error-state sentence became three sentences.
  - RTS and CTS are now expanded in the standard form, and GPS is expanded.
  - In the SPI signal table, "serial clock" and "chip select" moved into the Purpose column.
- Consistency:
  - "resynchronising", "resynchronise" and "resynchronisation" are now spelled with -z-.
  - The space before % is removed in prose.
  - The Davis et al. sentence in §5.3 now matches the corrected wording of entry 4 §2.4: "...applies to CAN messages once that non-preemption is taken into account; Davis, Burns, Bril and Lukkien (2007) gave the corrected form of that analysis."
- Metadata: description cut from 303 to 153 characters. Two H2 headings are now in sentence case.
- References:
  - All entries are in house format and in alphabetical order.
  - The Davis et al. entry keeps the published sentence-case title. Pages 239–272 were added from the Springer article page for doi 10.1007/s11241-007-9012-7, fetched 2026-10-13.
  - The ISO 11898-1/-2 titles are given in their original form, with years.
  - "3rd edition" became "3rd ed.".
- Technical corrections: none. All numbers were recomputed and the CAN script reproduces its output.
- Remaining warnings: none. Remaining suggestions:
  - Acronym-expansion items that are the expansions themselves or not abbreviations: NXP (company name); RS-232/RS-485 and TIA (standard names); the SPI signal names (SCLK/SCK, COPI/MOSI, CIPO/MISO, CS/SS), explained in the table and the paragraph after it; CPOL and CPHA, SCL and SDA (each expanded in parentheses right after the bold term); "AND" in "wired-AND"; START and STOP (condition names); RTR, IDE, DLC and CRC, expanded in the Purpose column of the frame table.
  - "FD" at line 19: expanded as "CAN with flexible data rate (CAN FD)".
  - Sentences of 49–50 words in §5.8, Exercise 3 and the closing paragraph are left: they read clearly.
- Flags for independent review: none new. The Di Natale et al. book subtitle ("Theory and Practice"?) was not verified; the title is left as it was.
- Out-of-scope reference for the orchestrator: `src/content/blog/fieldbuses-and-industrial-ethernet.mdx:373` writes the Davis et al. title in title case ("Controller Area Network (CAN) Schedulability Analysis: Refuted, Revisited and Revised"). The published title is "Controller Area Network (CAN) schedulability analysis: Refuted, revisited and revised", vol. 35, no. 3, pp. 239–272, 2007.
- Vietnamese translation affected: no translation exists. No `updatedAt`: published 2026-10-13.

## Independent review (wave 2)
- Report: `reviews/embedded-and-real-time-systems.md` (reviewed commit 9232ed9, 2026-10-14).
- Fact-check: pass (UM10204 rev. 7.0 details verified on the NXP PDF; Di Natale subtitle verified, F3 optional). Technical: pass (CAN script and CRC check value reproduce; all numbers recomputed).
- Findings: F3, T2 (optional).
- Not verified: I2C Fm/Fm+ table values (line 164–166) and CAN fault-confinement thresholds (line 325) against the document text (UM10204 Table 10 not in the fetched part; ISO 11898-1 paywalled).

## Revision log (wave 2 resolution)

- F3 (optional): the Di Natale et al. title now includes the subtitle "Theory and Practice", checked on Springer on 2026-10-15.
- T2 (optional): §5.1 now glosses characteristic impedance and reflection in one added sentence.
- There is no Vietnamese translation.
