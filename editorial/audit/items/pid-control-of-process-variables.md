<!-- audit: {"slug":"pid-control-of-process-variables","type":"article","series":"industrial-automation","priority":"P2","before":{"purpose":4,"structure":4,"accuracy":4,"evidence":3,"language":3,"consistency":4,"publishing":2},"findings":{"blocking":0,"shouldFix":3,"optional":4}} -->
# Audit: PID Control of Process Variables

- Path: `src/content/blog/pid-control-of-process-variables.mdx` · Route: `/blog/pid-control-of-process-variables` · Type: article (series entry) · Series `industrial-automation`, entry 4 of 5 · Words: 3,719 (`eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 4: builds-on (entries 1-3 and the control series) and conventions (percent of span, seconds, $e = r - y$, Python 3) stated.
- structure 4.
- accuracy 4: both Python programs re-run (as one script, since the second calls `run`); all six result lines and both windup lines identical. Recomputed: $t_{28} = 129.80$ s, $t_{63} = 329.90$ s, $\tau = 300.1$ s; ZN 6.00/100 s; SIMC 3.33/240 s; Exercise 1 (5.63, 13.3 s; 3.13, 20 s), Exercise 3 (90 s, 16 s, 1.88), level SIMC settings (2.0/40 s; 0.19/420 s; $k'K_cT_i$ = 4.0 and 3.99), Exercise 5 ($\omega_n$ = 0.025 rad/s, period 290.2 s, $\zeta$ = 0.354).
- evidence 3: Ziegler–Nichols and Skogestad entries without pages; "4th edition" form.
- language 3: "very slowly", "simply the last sample", "quite different"; 77- and 64-word sentences.
- consistency 4: cross-series references checked (below).
- publishing 2: description 392 characters, a list of every section; five level-2 headings in title case.

Cross-series references to Foundations of Control Systems, checked against the current files: the series has five entries (`introduction-to-control-systems`, `feedback-and-system-behavior`, `state-space-models-primer`, `stability-and-eigenvalues`, `state-feedback-controller-design`); its first entry introduces the loop (plant, sensor, controller, actuator, reference, error; `introduction-to-control-systems.mdx:23-26`), lists "Tracking" and "Disturbance rejection" (`:39-40`) and introduces the Laplace variable with the transfer function (`:49`); `feedback-and-system-behavior.mdx:56` shows that proportional feedback alone leaves a steady-state error on a first-order plant. All four references are accurate. The control series is being revised in the same wave; the Series Editor should re-check these after both are merged.

## Priority

P2.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 392 characters |
| P2 | Should fix | `:21, 48, 86, 116, 289` | publishing | Headings in title case ("Process Control Vocabulary", "Models of Process Dynamics", "The PID Law", "A Digital PID Controller", "The Four Classic Process Variables") |
| C1 | Should fix | `:390-394` | evidence | References: no volume/pages for Skogestad and Ziegler–Nichols, title case on article titles, "4th edition" |
| C2 | Optional | `:195`, `:265`, `:297` | language | Intensifiers "very slowly", "simply the last sample", "quite different" |
| C3 | Optional | `:297`, `:164` | language | 77-word and 64-word sentences |
| C4 | Optional | `:102`, `:386` | consistency | "PI" and "OPC UA" not expanded at first use |
| C5 | Optional | `:7-10` | consistency | Tag "control-theory" is hyphenated while the other tags in the series use spaces; tags are copied by the translation and are not changed in this wave |

### C1. References
- **Correction:** S. Skogestad, ..., *Journal of Process Control*, vol. 13, no. 4, pp. 291–309, 2003 (Crossref record for DOI 10.1016/S0959-1524(02)00062-8, fetched); J. G. Ziegler and N. B. Nichols, ..., *Transactions of the ASME*, vol. 64, pp. 759–768, 1942 (no issue number confirmed; left out); article titles in sentence case as published; "4th ed.".

## Revision log (wave 1)
- Prose: bumpless-transfer sentence split; SIMC level-example sentence split ("is just the choice" → "lies only in the choice"); "very slowly" → "slowly"; "simply the last sample" → "only the last sample"; "quite different" → "different". (C2, C3)
- Terminology: "proportional–integral (PI)" and "OPC Unified Architecture (OPC UA)" expanded at first use. (C4)
- Headings: five level-2 headings to sentence case. (P2)
- Metadata: description 392 → 157 characters. (P1)
- References: alphabetical; "4th ed."; Skogestad completed (vol. 13, no. 4, pp. 291–309; Crossref record for DOI 10.1016/S0959-1524(02)00062-8); Ziegler–Nichols completed (vol. 64, pp. 759–768; issue not confirmed, so omitted); article titles in sentence case. (C1)
- Cross-references: the four references to Foundations of Control Systems checked and accurate (see audit); unchanged.
- Technical content: unchanged; both programs re-run together, output identical.
- Remaining warnings: none. Suggestions: sentence-length (50-66 words, mostly in the summary paragraph and the transition, read naturally), acronym false positives (ISA expanded in the same sentence, SIMC expanded inline, ASME in a journal title).
- Flags for independent review: Series Editor: Foundations of Control Systems is being revised in the same wave; re-check that its first entry still introduces the Laplace variable with the transfer function and lists tracking and disturbance rejection, and that `feedback-and-system-behavior` still shows the proportional offset on a first-order plant. Tag `control-theory` (hyphenated, unlike the series' other tags) left unchanged because tags are copied by translations.
- Vietnamese translation affected: no translation of this article exists.

## Independent review (wave 2)
- Fact-check: pass (cross-series references to Foundations of Control Systems re-checked in the current files: loop vocabulary, Tracking/Disturbance rejection, Laplace transform in Section 3.2, proportional offset in Section 2.3 of the second entry; all accurate).
- Technical: pass (both blocks re-run as one script, output identical; instability of the ZN loop without limits and the no-overshoot claim confirmed by re-run; all exercises and the integrating-loop damping formula recomputed).
- Findings concerning this item: F3 (Optional, line 15). Report: `reviews/industrial-automation.md`.
- Not verified: bibliographic details of Skogestad (2003), Ziegler and Nichols (1942) and the three books (consistent with reviewer knowledge, not fetched).

## Revision log (wave 2 resolution)
- F3 (optional): introduction (line 15) "in the great majority of loops" replaced by "in most loops" (unsourced quantitative claim removed).
- No Vietnamese translation exists. eos lint: 0 errors, 0 warnings; eos syntax: pass.
