<!-- audit: {"slug":"evaluating-models-honestly","type":"article","series":"machine-learning-fundamentals","priority":"P2","before":{"purpose":4,"structure":4,"accuracy":4,"evidence":3,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":5,"optional":5}} -->
# Audit: Evaluating Models Honestly

- Path: `src/content/blog/evaluating-models-honestly.mdx` · Route: `/blog/evaluating-models-honestly` · Type: article (series entry) · Series `machine-learning-fundamentals`, entry 4 of 4 · Words: 4267 (`eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 4
- structure 4
- accuracy 4: all four Python blocks rerun (Python 3.13.16, NumPy 2.5.3): identical output. Recomputed: Hoeffding $m \ge \ln 40/0.005 = 737.8$ (738); union-bound deviations 0.195 ($M = 50$) and 0.136 ($M = 1$); Exercise 1, 6622.9 (6623); standard errors 0.0252 (0.85) and 0.0266 (0.83), half-width 0.0495; Hoeffding half-width for $m = 200$, 0.0960. All correct.
- evidence 3: eight real works, but "58(301), 1963" style, no pages, not alphabetical; most of them are not attached to the claim they support (Ambroise and McLachlan, Cawley and Talbot, Dietterich, Quiñonero-Candela et al. are never mentioned in the text).
- language 3: "actually" ×4 in Section 1.1; "simply"; "clearly" in Exercise 4; a 197-word paragraph (Section 2.2) and sentences of 50–94 words.
- consistency 3: six title-case headings; "95 %" etc.; MSE and SGD not expanded.
- publishing 2: description 370 characters.

## Priority

P2.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 370 characters. |
| C1 | Should fix | `:19`, `:34`, `:98`, `:180`, `:292`, `:312` | consistency | Title-case headings. |
| C2 | Should fix | `:401–408` | evidence | Reference format and order. |
| D1 | Should fix | `:194`, `:178`, `:298`, `:318` | evidence | Cited works not tied to the claims they support. |
| D2 | Should fix | `:397` | structure | The closing paragraph does not close against the series objectives and ends with an overclaim: "underlie every supervised learning method, however large". |
| C3 | Optional | `:23` | language | "actually" four times. |
| C4 | Optional | `:74` | language | 197-word paragraph mixing the example's reading with the general union-bound argument. |
| C5 | Optional | `:298`, `:38`, `:178` | language | Sentences of 94, 50 and 64 words. |
| C6 | Optional | `:114`, `:320`, `:366` | consistency | MSE and SGD not expanded; "Is the first clearly better?". |
| C7 | Optional | `:114` | accuracy | "chose $\lambda$ by looking at the true risk": entry 3 looked at the fresh-data MSE, an estimate of it. |

### D1. Sources not attached to claims
- **Where:** `:194` ("one of the best-documented forms of leakage"), `:178` (nested CV), `:298` (distribution shift), `:318` (McNemar's test)
- **Problem:** standards 6.1 require evidence for non-trivial claims; the reference list contains the supporting works, but the reader cannot tell which supports what.
- **Correction:** attribute in the text: Ambroise and McLachlan (2002) at the feature-selection leakage; Cawley and Talbot (2010) at nested CV; Quiñonero-Candela et al. (2009) at distribution shift; Dietterich (1998) at McNemar's test.

### D2. Closing paragraph
- **Where:** `:397`
- **Text:** "The same four ideas, a loss, an optimizer, a control on capacity, and an honest evaluation, underlie every supervised learning method, however large."
- **Problem:** standards 6.2 ask the last entry to close against the series objectives; the sentence claims universality the series does not show, and has a 63-word sentence before it.
- **Correction:** one sentence per entry, a sentence naming the four objectives as met, and a bounded final sentence.

## Revision log (wave 1)

- Structure: Section 2.2's 197-word paragraph split where it moves from the example to the general argument; closing paragraph rewritten to close against the four series objectives (D2).
- Evidence: in-text attributions added for Ambroise and McLachlan, Cawley and Talbot, Quiñonero-Candela et al., and Dietterich (D1).
- Prose: "actually" removed (Section 1.1 now speaks of "the model that will be deployed" and "the cases it will meet in use"); "simply" cut; "Is the first clearly better?" → "Does this show that the first is better?"; long sentences in Sections 2.1, 3.3, 5.1 and 6.1 split; C7 corrected to "looking at the fresh-data mean squared error (MSE), a near-exact estimate of the true risk".
- Terminology/style: headings to sentence case; "95%", "99%", "94%", "85%", "50%" in prose (the code comment "25 %" is code and was left unchanged so that the code block stays byte-identical); MSE and SGD expanded at first use.
- Metadata: description one sentence, 164 characters.
- References: house format, alphabetical, verified: Ambroise and McLachlan, PNAS vol. 99, no. 10, pp. 6562–6566 (scan of the paper; title in its original sentence case); Cawley and Talbot, JMLR vol. 11, pp. 2079–2107 (jmlr.org page); Dietterich, *Neural Computation* vol. 10, pp. 1895–1923 (ML Anthology record; issue 7 kept from the original entry); Hoeffding, JASA vol. 58, no. 301, pp. 13–30; Kaufman et al., *ACM TKDD* vol. 6, no. 4, art. 15 (IUCC research portal; page range not stated there, so "art. 15" only; title in its original case); Quiñonero-Candela et al. as editors ("Eds."); Stone, JRSS B vol. 36, no. 2, pp. 111–147 (scan of the paper). "Dataset Shift in Machine Learning" keeps its published title (the glossary's "data set" rule exempts titles of works).
- Cross-references: section slugs unchanged except case-insensitive ones (no change in slug); links to `#33-empirical-risk` still valid.
- Technical corrections: none to code or numbers; C7 is a wording correction.
- Remaining suggestions and why they stay: `sentence-length` at `:180` (64 words) and `:300` (48 words) are artefacts of the sentence splitter, which does not break before a sentence that starts with bold text ("**Nested cross-validation**", "**Distribution shift**"); the real sentences are under 40 words. `acronym-expansion` ACM and MIT at `:408–409` are publisher/journal names in references.
- Flags for independent review (fact-check): (1) Cawley and Talbot (2010) attribution "the resulting optimism can be as large as the differences between the learning methods being compared" paraphrases their abstract from memory; confirm the wording. (2) Dietterich (1998) "recommends McNemar's test when each model can be trained only once": confirm against the paper's conclusions. (3) Dietterich issue number 7 not confirmed by the record consulted. (4) Kaufman et al. page range (art. 15) not confirmed.
- Vietnamese translation affected: no translation exists. `publishedAt` 2026-10-13, so no `updatedAt`.

## Revision log (wave 2 resolution)

Resolves `reviews/machine-learning-fundamentals.md` T3, S1, F3 (entry 4 part).
- T3: label shift now defined with $P(\mathbf{x} \mid y)$ fixed (Lipton, Wang and Smola, ICML 2018, abstract, checked 2026-10-15); the sentence was split and the Section 5.1 paragraph split before "Distribution shift" to clear two new length suggestions (`:300–302`).
- S1: standard error and 95% confidence interval defined in Section 6.1 (`:320`); figures unchanged (recomputed 0.0252 and 0.0495).
- F3: Stone (1974) attached to cross-validation as a sentence after the $k$-fold steps (`:110`); Kaufman et al. (2012) attached at the end of the first leakage paragraph (`:186`).
- Code and outputs unchanged; no heading changed. Lint: 0 errors, 0 warnings; syntax compiles.
- Meaning changes for the translation follow-up (no translation exists yet): Sections 3.1, 4.1, 5.1, 6.1.

## Revision log (QA findings)

Resolves `reviews/machine-learning-fundamentals.md` Q1.
- Prose: serial comma removed at `:30`, `:78`, `:116`, `:239`, `:300`, `:302`, `:306` and in the checklist row at `:333`. Kept: `:17` and `:401` (items contain "and"), `:398` (removal would read as "averages that hide ... label errors"), `:357` (groups "evaluate ... or use nested cross-validation" before "and report"); `:186` is independent clauses around a parenthetical.
- Lint: 0 errors, 0 warnings. No heading, anchor, code or number changed.
