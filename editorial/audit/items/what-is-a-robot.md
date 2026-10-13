<!-- audit: {"slug":"what-is-a-robot","type":"article","series":"introduction-to-robotics","priority":"P1","before":{"purpose":3,"structure":3,"accuracy":4,"evidence":2,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":1,"shouldFix":7,"optional":3}} -->
# Audit: What Is a Robot? Components and the Sensing-Acting Loop

- Path: `src/content/blog/what-is-a-robot.mdx` · Route: `/blog/what-is-a-robot` · Type: article · Series `introduction-to-robotics`, entry 1 of 4 · Words: 2738
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 3: the opening states the aim, but its second paragraph is a table of contents in prose ("It starts with ..., divides ..., follows ..., and ends with ...") and the prerequisites and conventions are not stated.
- structure 3: sound progression (definition, subsystems, flows, loops, software, difficulties, summary); no exercises although Section 2 has computable quantities (mobility, encoder resolution, transmission).
- accuracy 4: recomputed; no error found (see below).
- evidence 2: the ISO 8373 entry merges two editions under the 2021 title (the 2012 edition is titled *Robots and robotic devices — Vocabulary*); Brooks 1986 lacks volume, issue and pages; Gat is described in the text as a "survey" although it is a book chapter; references not in house format (comma outside quotes, "(eds.)" form).
- language 3: four title-case H2 headings; "clearly", "simply", "actually", "very" (lint); "newton-metres" (British); three sentences of 49-61 words (lines 124, 179, 183).
- consistency 3: "metres" against the site's American spelling; "toward" here but "towards" in entries 2 and 4.
- publishing 2: description 309 characters (limit 165) and a list of every section.

Accuracy spot-check (python3): $360^\circ/(4096 \times 100) = 0.000879^\circ$ (text $\approx 0.00088^\circ$, correct); serial-arm mobility $6(n+1-1-n)+n = n$ (correct); reflected inertia $N^2 J_m$ and $\tau_j = \eta N \tau_m$, $\omega_j = \omega_m/N$ (standard, correct). ISO 8373:2012 paraphrase matches the 2012 definition ("actuated mechanism programmable in two or more axes with a degree of autonomy, moving within its environment, to perform intended tasks").

## Priority

P1: first entry of the series and the foundation of its vocabulary; carries a reference that conflates two standards (blocking under standards 7.3 / C3 risk) and the longest description problem.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 309 characters, lists every section. |
| P2 | Should fix | lines 20, 132, 142, 185 (and 51, 169) | language | Title-case headings ("What Makes a Machine a Robot", "Two Flows: Energy and Information", "Loops Within Loops", "Why Robotics Is Hard"; also "Four Subsystems", "Organizing the Software"). |
| A1 | Blocking | `:212` References | evidence | ISO 8373 entry merges the 2012 and 2021 editions under one title. |
| A2 | Should fix | `:213-215` References | evidence | Missing volume, issue and pages; not house format. |
| A3 | Should fix | `:183` | accuracy | Gat 1998 called a "survey"; it is a book chapter arguing for the three-layer architecture. |
| D1 | Should fix | `:16-18` | purpose | Prose table of contents; no statement of prerequisites or of what the entry builds on. |
| D2 | Should fix | Section 2 | structure | No exercises although mobility, resolution and transmission ratios are computable (standards 6.2 item 5; entries elsewhere on the site carry exercises). |
| C1 | Should fix | `:101` | language | "newton-metres" (British). |
| C2 | Should fix | lines 124, 179, 183 | language | Sentences of 49, 52 and 61 words. |
| C3 | Optional | lines 27, 49, 85, 101 | language | "actually", "clearly", "simply", "very". |
| C4 | Optional | `:214-215` | language | "MIT" and "SRI" unexpanded (publisher and institution names; leave). |

### A1. ISO 8373 reference
- **Where:** `src/content/blog/what-is-a-robot.mdx:212`, References
- **Text:** "ISO 8373, *Robotics — Vocabulary*, International Organization for Standardization (2012; revised 2021)."
- **Problem:** ISO 8373:2012 is titled *Robots and robotic devices — Vocabulary*; *Robotics — Vocabulary* is the title of ISO 8373:2021 (checked: ISO catalogue listings via EFFRA portal and AFNOR shop, 2026-10-13). The text cites both editions, so both need entries.
- **Correction:** two entries: `ISO 8373:2012, *Robots and robotic devices — Vocabulary*, International Organization for Standardization, 2012.` and `ISO 8373:2021, *Robotics — Vocabulary*, International Organization for Standardization, 2021.`

### A2. Incomplete references
- **Text:** "R. A. Brooks, "A Robust Layered Control System for a Mobile Robot", *IEEE Journal of Robotics and Automation*, 1986."
- **Problem:** volume/issue/pages missing (standards 7.3). Verified: vol. 2, no. 1, pp. 14–23, March 1986 (J. M. Vidal's library entry; IEEE Xplore document 1087032). Gat chapter pages not verified (no source reached); publisher confirmed as AAAI Press on the chapter PDF (the book is an AAAI Press/MIT Press co-publication).
- **Correction:** house format; Brooks completed; Gat pages left out and flagged.

### A3. "survey"
- **Text:** "(Erann Gat's 1998 survey is a common reference)"
- **Correction:** "Erann Gat's 1998 chapter".

### D1. Opening
- **Text:** "The approach is from the outside in. It starts with what makes a machine a robot, divides a robot into four subsystems, follows ..."
- **Correction:** replace with one paragraph on what the entry assumes (no robotics background; the feedback idea from the control series) and what the series builds on it.

### P1. Description
- **Correction:** "Learn what makes a machine a robot, the four subsystems every robot shares, and how its control loops and software are organized." (130)

## Revision log (wave 1)
- Structure: opening second paragraph (prose table of contents) replaced by a statement of what the entry assumes (no robotics background; feedback from the linked control series; torque and inertia; SI units). New Section 7 "Exercises" (four-bar mobility, transmission torque/speed/reflected inertia, encoder resolution; answers recomputed with python3: $M = 1$; 20 N·m, 60 rpm, 0.05 kg·m²; $0.0035^\circ$). Summary renumbered 7 → 8.
- Prose: three long sentences split (backlash, subsumption, three-layer architecture); "actually", "clearly", "simply", "very", "in order to" removed.
- Terminology/style: headings in sentence case; "newton-metres" → "newton-meters, N·m".
- Metadata: description rewritten (130 characters).
- References: house format, alphabetical; ISO 8373 split into the 2012 edition (*Robots and robotic devices — Vocabulary*) and the 2021 edition (*Robotics — Vocabulary*) (A1); Brooks completed with vol. 2, no. 1, pp. 14–23 (verified, J. M. Vidal library entry for IEEE Xplore 1087032); Gat publisher given as AAAI Press/MIT Press (AAAI Press verified on the chapter PDF; MIT Press as before).
- Cross-references: links added to the control-series entry in the opening, the [next entry] in the Summary and the [last entry] in Section 2.4.
- Technical corrections: none needed. "Gat's 1998 survey" → "chapter" (A3; it is a book chapter).
- Remaining suggestions: "AAAI", "MIT", "SRI" unexpanded in References (names of publishers/institutions; expanding them in a bibliography is not house practice).
- Flags for independent review: Gat chapter page numbers not verified (not added); exercises are new content for the technical reviewer to check; ISO 8373:2021 wording paraphrase in Section 1.1 ("rephrases it around locomotion, manipulation and positioning") not checked against the standard text.
- Vietnamese translation affected: yes. Changed meaning/structure: new opening paragraph 2; new Section 7 Exercises (three exercises with answers) and Summary renumbered to 8; ISO reference split into two editions; Brooks and Gat reference details; "survey" → "chapter"; description. No `updatedAt` added: `publishedAt` is 2026-10-13, which the brief exempts (the assignment's note that publishedAt is earlier did not match the files).
