<!-- audit: {"slug":"real-time-operating-systems-and-scheduling","type":"article","series":"embedded-and-real-time-systems","priority":"P2","before":{"purpose":4,"structure":4,"accuracy":4,"evidence":3,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":4,"optional":4}} -->
# Audit: Real-Time Operating Systems and Scheduling

- Path: `src/content/blog/real-time-operating-systems-and-scheduling.mdx` · Route: `/blog/real-time-operating-systems-and-scheduling` · Type: article · Series `embedded-and-real-time-systems`, entry 4 · Words: about 4300
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 4.
- structure 4: kernel concepts, then theory, then resources, then a worked design that ties ISR load (entry 2) into RTA.
- accuracy 4: all three Python programs reproduce their output; RTA iterations and exercises recomputed.
- evidence 3: references lack volume/issue/page in house form; Davis title capitalization to be kept consistent with the published title.
- language 3: a 93-word sentence (line 15) and a 62-word one (line 19); "actually" twice, "really" once; "analysable", "normalise", "utilisation" (code comment) are British.
- consistency 3: "RTOS" used in Conventions (line 19) before it is expanded in §1.1; POSIX expanded after the abbreviation.
- publishing 2: description 401 characters; three H2 headings in title case.

Note on "utilization": the lint `phrases` rule flags every "utilization" (glossary: "utilize → use"). Here it is the technical quantity $U = \sum C_i/T_i$ of scheduling theory (Liu and Layland's "utilization bound"); "use" would be wrong. Kept everywhere it names that quantity.

## Priority

P2.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 401 characters. |
| P2 | Should fix | `:21, 84, 270, 317` | publishing | H2 headings in title case. |
| C1 | Should fix | `:15, 19` | language | Sentences of 93 and 62 words. |
| P3 | Should fix | `:425–435` | evidence | References not in house format. |
| C2 | Optional | `:31, 76, 360` | language | "actually", "really" add nothing. |
| C3 | Optional | `:68, 156, 280` | consistency | British "normalise", "utilisation", "analysable". |
| C4 | Optional | `:17, 19` | language | RTOS used before expansion; "POSIX, the Portable Operating System Interface". |
| A1 | Optional | `:295` | evidence | Mars Pathfinder account is uncited ("widely reported"); fact-checker to confirm or add a source. |

### C1. Long sentences
- **Text (line 15):** the paragraph's third sentence, "[The second] moved urgent data handling into interrupt service routines (ISRs) and direct memory access (DMA), and showed how to pass data safely ...".
- **Text (line 19):** "Code is C11; the periodic-task example uses the real-time interface of POSIX, ... so that it can be compiled on a desktop, and other RTOS concepts are described without any particular kernel's API, because ..."
- **Correction:** split; move the RTOS abbreviation to its first use.

### P3. References
- **Correction:** house format with volume, issue and pages verified (2026-10-13): Liu and Layland, JACM vol. 20, no. 1, pp. 46–61 (MIT JACM bibliography); Leung and Whitehead, vol. 2, no. 4, pp. 237–250 (NJIT research portal); Joseph and Pandya, vol. 29, no. 5, pp. 390–395 (Utah Computer Journal bibliography); Audsley et al., pp. 284–292 (York RTS publications page); Sha et al., vol. 39, no. 9, pp. 1175–1185; Davis et al., pp. 239–272 (Springer). Alphabetical order.

## Verification (auditor's spot checks)

Ran all three Python programs (identical output). Recomputed by hand: U = 0.8333; bounds 0.828, 0.780, ln 2; τ3 iteration 3 → 6 → 7 → 9 → 10; Set C U = 0.971, RM τ2 4 → 6 → 8 > 7; ISR increments 0.0375, 0.0875, 0.2479 ms and margins 2.46, 2.41, 1.75 ms; Exercises 1–5. All correct.

## Revision log (wave 1)
- Prose:
  - The 93-word opening sentence and the 62-word Conventions sentence are split.
  - The sentences in §2.4 (timeline) and §2.5 (why kernels use fixed priorities) are split.
  - "actually" (twice) and "really" removed.
- Terminology/style:
  - RTOS is now expanded at its first use (opening paragraph, not bold); the bold definition stays in §1.1.
  - POSIX is expanded in the standard form.
  - "analysable" became "analyzable", and the code comments "normalise" and "utilisation" became "normalize" and "utilization". These are comment-only changes; the program output is unchanged.
- "utilization" kept: it is the technical quantity $U=\sum C_i/T_i$ of scheduling theory (the Liu and Layland utilization bound), not a synonym for "use". The glossary rule "utilize → use" does not apply to it, and replacing it would be wrong. (After another editor's glossary update the linter no longer warns on it.)
- Metadata: description cut from 401 to 154 characters. Four H2 headings are now in sentence case.
- References:
  - All in house format and in alphabetical order.
  - Volume, issue and pages were added only where verified (2026-10-13): Liu and Layland (MIT JACM bibliography), Leung and Whitehead (NJIT research portal), Joseph and Pandya (Utah Computer Journal bibliography), Audsley et al. (York RTS publications), Sha et al. (Wikipedia citation with DOI 10.1109/12.57058), Davis et al. (Springer).
- Technical corrections: none. All three programs and the exercises were recomputed.
- Remaining warnings: none. Remaining suggestions:
  - ACM is part of a journal name.
  - Sentences of 50 and 46 words are left (opening paragraph, §4).
- Flags for independent review: the Mars Pathfinder statement (§3.3) is uncited (A1).
- Vietnamese translation affected: no translation exists. No `updatedAt`: published 2026-10-13.
