<!-- audit: {"slug":"programmable-logic-controllers","type":"article","series":"industrial-automation","priority":"P2","before":{"purpose":4,"structure":4,"accuracy":4,"evidence":3,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":4,"optional":3}} -->
# Audit: Programmable Logic Controllers

- Path: `src/content/blog/programmable-logic-controllers.mdx` · Route: `/blog/programmable-logic-controllers` · Type: article (series entry) · Series `industrial-automation`, entry 2 of 5 · Words: 4,420 (`eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 4: builds-on, coverage, edition (IEC 61131-3:2013 with the 2025 edition noted) and Python version stated.
- structure 4: hardware → scan cycle → I/O → software model → languages → practice → exercises → summary.
- accuracy 4: both Python programs re-run, output identical (`min 13.5 ms, max 23.5 ms, mean 18.5 ms`; the four scaling lines). Scaling (12.8 mA → 5.5 bar, 15 206.4 counts, 0.000 36 bar per count), Exercise 1 (31/46 ms, 10/31 = 32 %), Exercise 2 (16.80 mA, 3.20 m, 1.685 mA), Exercise 5 (321.4 Ω) recomputed.
- evidence 3: references not in house format; three standards undated; not alphabetical.
- language 3: a 76-word sentence (`:23`) and a 71-word sentence (`:149`); intensifiers.
- consistency 3: reference format; otherwise consistent with entry 1's notation (`stop_ok`, seal-in, TON/TOF/TP).
- publishing 2: description 263 characters; six level-2 headings in title case.

## Priority

P2: should-fix metadata and style problems a reader would notice; no accuracy problem.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 263 characters, a list of sections |
| P2 | Should fix | `:19, 46, 117, 190, 236, 378` | publishing | Level-2 headings in title case ("What a Programmable Logic Controller Is", "The Scan Cycle", "Inputs and Outputs", "The IEC 61131-3 Software Model", "The Five Languages", "Writing Reliable PLC Programs") |
| C1 | Should fix | `:453-459` | evidence | References not in house format or order; "2nd edition"; NE 43 entry puts the number before the organization; IEC titles not in original capitalization; IEC 61131-2 and IEC 61508 undated |
| C2 | Should fix | `:23`, `:149` | language | 76-word and 71-word sentences |
| C3 | Optional | `:65`, `:99`, `:144` | language | "very hard to reason about", "the third entry cares so much about network timing", "clearly distinguishable" |
| C4 | Optional | `:238` | language | "IEC 61131-3:2013 defines two textual and two graphical languages, plus Sequential Function Chart" does not say which, before the subsections name them |
| C5 | Optional | `:105` | language | 58-word watchdog sentence |

### C1. References
- **Correction:** alphabetical (Bolton; IEC 61131-2:2017; IEC 61131-3:2013; IEC 61508:2010; John and Tiegelkamp; NAMUR; Petruzella); "2nd ed."; IEC titles as published: "Industrial-process measurement and control – Programmable controllers – Part 2: Equipment requirements and tests" (edition 4.0, 2017, confirmed on IEC webstore/VDE/SCC listings); "Programmable controllers – Part 3: Programming languages" (2013); IEC 61508 parts 1–7, edition 2.0, 2010; NAMUR as organization: "NAMUR, *Standardization of the Signal Level for the Failure Information of Digital Transmitters*, NE 43, 2021."

### C2. Long sentences
- **Text (23):** "That origin explains three features that remain today: the program is executed cyclically, as if every **rung** of a relay drawing (one horizontal path ...) were being energized continuously; one of the main languages still looks like a relay drawing; and the controller is built to work in the cabinet the relays used to occupy, ..."
- **Text (149):** "Recommendation NE 43 of NAMUR, an international association of users of automation technology in the process industries, standardizes the signal levels and is widely followed: a transmitter signals measurements ... at or above 21 mA."
- **Correction:** split each into two or three sentences without changing content.

## Revision log (wave 1)
- Structure: none needed. The introduction of Section 5 now names the five languages by kind (graphical: LD, FBD; textual: ST, IL; plus SFC) before the subsections. (C4)
- Prose: the 76-word sentence on the relay origin split into four; the NE 43 sentence split (NAMUR introduced first, then the levels); the watchdog and edge-detection sentences split; "very hard" → "hard"; "clearly distinguishable" → "cannot be mistaken for"; "cares so much about network timing" → "analyzes network timing in detail". (C2, C3, C5)
- Headings: six level-2 headings to sentence case ("The five languages" kept: Section 5 follows the third edition, which the introduction states). (P2)
- Metadata: description 263 → 142 characters. (P1)
- References: alphabetical, "2nd ed."; IEC 61131-2 dated 2017 with its published title (edition 4.0; IEC webstore, VDE, SCC listings); IEC 61131-3:2013 with year; IEC 61508 cited as the series, undated; NAMUR as organization with document number and year. (C1)
- Technical content: unchanged; both Python programs re-run, output identical; exercise arithmetic recomputed.
- Remaining warnings and why they stay: none. Suggestions: sentence-length (46-51 words, each a single list or chain the split would weaken), acronym false positives (FALSE, ON, OFF, MIX; PNP and NPN are transistor type names; NE is a document prefix), one `reference-format` (IEC 61508 undated: the text cites the standard family and its machinery counterparts, not an edition).
- Flags for independent review: fact-check that IEC 61508 parts 1-7 are still edition 2.0 (2010) if the reference should be dated; NE 43 receiver thresholds remain deferred to the current edition (as resolved in the previous review).
- Vietnamese translation affected: no translation of this article exists.

## Independent review (wave 2)
- Fact-check: pass, with one not-verified item (below). NE 43 2021 edition and title, IEC 61131-2:2017 Ed. 4.0, IEC 61131-3:2025 date verified.
- Technical: fail until T2 is resolved (both Python blocks re-run, output identical; all exercise arithmetic and the Exercise 4 statement-order trace recomputed; T2 is a wording error about which scan resets the mix timer).
- Findings concerning this item: T2 (Should fix, line 342). Report: `reviews/industrial-automation.md`.
- Not verified: removal of Instruction List by IEC 61131-3:2025 (lines 17, 194, 356, 445, 447): official abstracts mention only an Annex B list of removed features; supported by secondary sources only. Book editions of Bolton and John and Tiegelkamp not fetched.

## Revision log (wave 2 resolution)
- T2: Section 5.3 (line 342) now says the mix timer resets in the scan in which the state changes from MIX to DRAIN.
- Not-verified IL removal: qualified at lines 17, 194, 356 and 447 to what the IEC-derived abstract of IEC 61131-3:2025 supports (its published scope lists ST, LD, FBD and SFC and no longer lists Instruction List); Annex B was not accessible.
- No Vietnamese translation exists. eos lint: 0 errors, 0 warnings; eos syntax: pass.
