<!-- audit: {"slug":"measuring-timing-latency-and-resource-use","type":"article","series":"embedded-and-real-time-systems","priority":"P2","before":{"purpose":4,"structure":4,"accuracy":4,"evidence":3,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":4,"optional":4}} -->
# Audit: Measuring Timing, Latency and Resource Use

- Path: `src/content/blog/measuring-timing-latency-and-resource-use.mdx` · Route: `/blog/measuring-timing-latency-and-resource-use` · Type: article · Series `embedded-and-real-time-systems`, entry 5 · Words: 3843 (from `eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 4.
- structure 4: inputs and outcomes, instruments, execution time, latency, load, memory, workflow; ending closes the series against its objectives.
- accuracy 4: deterministic programs reproduce their output; the wake-up experiment is framed as one session, as the series review required (F6).
- evidence 3: references not in house format; the Wilhelm et al. author list spells "J. Staschulat", while the Chalmers research record lists "Jan Stachulat" (to be checked by the fact-checker against the ACM record).
- language 3: sentences of 55–65 words (lines 17, 51, 457); "actually" twice, "simply" once.
- consistency 3: "start-up" (lines 124, 330, 386) where entries 1 and 2 write "startup"; "analysed" in the Mermaid label; SPI and I2C not expanded in this entry.
- publishing 2: description 360 characters; three H2 headings in title case.

"utilization" at line 316 names the scheduling quantity of the fourth entry and is kept (see the fourth entry's audit).

## Priority

P2.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 360 characters. |
| P2 | Should fix | `:21, 118, 388` | publishing | H2 headings in title case. |
| C1 | Should fix | `:17, 51, 457` | language | Sentences of 55–65 words. |
| P3 | Should fix | `:459–467` | evidence | References not in house format or order. |
| C2 | Optional | `:45, 131, 380` | language | "actually", "simply". |
| C3 | Optional | `:124, 330, 386, 395` | consistency | "start-up" vs "startup"; "analysed". |
| C4 | Optional | `:19, 457` | language | SPI and I2C unexpanded; POSIX expanded after the abbreviation. |
| A1 | Optional | `:461` | evidence | "J. Staschulat" vs "Jan Stachulat" in one bibliographic record; fact-checker to confirm. |

### C1. Long sentences
- **Text (line 457):** "It began with the vocabulary of deadlines, latency and jitter and the parts of a microcontroller; moved data ...; and ended by measuring the quantities that calculation depends on." (62 words)
- **Correction:** split into two sentences.

## Verification (auditor's spot checks)

Ran the combined Python script (identical output). Compiled and ran the cycle-counter, stack-painting and wake-up programs. The first two reproduce their output exactly. The wake-up program on this session's host gave "absolute: min 76.8 us, median 120.9 us, ... max 4774.6 us" and "relative: ... 280.4 ms behind the grid". These are different numbers with the same pattern, as the text says to expect. Recomputed: 40 × 86.8 µs = 3.47 ms; 0x2000 = 8192 cycles = 170.7 µs; ln 0.01/ln(1 − 10⁻⁶) = 4.6 × 10⁶ runs, 18 420 s = 5.1 h; load 30%; 43 100 B (16.4% of 256 KiB), 7372 B (11.2% of 64 KiB); maxima/median ratios 68.8, 47.8, 132. All correct.

## Revision log (wave 1)
- Prose:
  - Split the long sentences in the opening paragraph, in the Conventions paragraph and in §2.1.
  - Rewrote the series-closing paragraph as two sentences.
  - Removed "actually" (twice) and "simply".
  - "The simplest and most widely used method" became "The simplest method" (the superlative was unsupported).
- Terminology/style:
  - "start-up" became "startup" (three times), matching entries 1 and 2.
  - The Mermaid label "analysed" became "analyzed".
  - SPI and I2C were added to the Conventions abbreviation list.
  - POSIX is now expanded in the standard form.
  - Removed the space before % in prose. Program output (`71 %`) and KaTeX are unchanged.
- "utilization" (§5.1) kept as the scheduling quantity; see the fourth entry's log.
- Metadata: description cut from 360 to 154 characters. Three H2 headings changed to sentence case.
- References: house format, alphabetical. Added the volume and issue of Wilhelm et al. (7(3) → vol. 7, no. 3); article number and pages not added (not verified).
- Technical corrections: none. The wake-up program was rerun on this session's host; the numbers differ from the printed run with the same pattern, as the text states, so the printed output was left as the series review recorded it.
- Remaining warnings: none. Remaining suggestions:
  - GNU, ARM DDI, MIT and ACM are proper names.
  - Several sentences of 46–51 words were left, because they read clearly.
- Flags for independent review: fact-checker to confirm the spelling "J. Staschulat" against the ACM record; the Chalmers record has "Jan Stachulat" (A1). Arm DDI 0403 year.
- Vietnamese translation affected: no translation exists. No `updatedAt`, because the entry was published 2026-10-13.

## Independent review (wave 2)
- Report: `reviews/embedded-and-real-time-systems.md` (reviewed commit 9232ed9, 2026-10-14).
- Fact-check: fail until F1 is resolved (Arm DDI 0403 issue/year). The spelling "J. Staschulat" is confirmed (authors' preprint, CiteDrive); the Chalmers record is wrong, so no change is needed. Technical: pass (deterministic programs reproduce; the wake-up rerun shows the same pattern).
- Findings: F1 (should fix).
- Not verified: the printed wake-up output (one session, not reproducible by design); "an earlier session ... up to 38 ms" (line 287, no kept output); Wilhelm et al. article number and pages.

## Revision log (wave 2 resolution)

- F1: the Arm reference now gives the issue and year, "ARM DDI 0403E.e, 2021". There is no Vietnamese translation.
