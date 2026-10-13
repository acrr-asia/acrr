<!-- audit: {"slug":"closing-the-sim-to-real-gap","type":"insight","series":null,"priority":"P2","before":{"purpose":2,"structure":3,"accuracy":4,"evidence":3,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":1,"shouldFix":4,"optional":1}} -->
# Audit: Is the Sim-to-Real Gap Something to Close or to Measure?

- Path: `src/content/insights/closing-the-sim-to-real-gap.md` · Route: `/insights/closing-the-sim-to-real-gap` · Type: insight (Research question) · Words: 378
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 2: no framing paragraph; the body opens with "## Established" (standards 6.4 requires one paragraph on the question and why it matters).
- structure 3: three sections in the right order; Interpretation is well reasoned.
- accuracy 4: claims are standard and qualified ("usually", "often"); the trajectory metric is correctly limited ("mixes dynamics error with measurement and initial-state error").
- evidence 3: Established claims are common knowledge in robotics, but nothing links to a source or to an in-depth article.
- language 3: two sentences of 52 and 56 words (lines 14, 18); "One reasonable reading" stacks hedges.
- consistency 3: does not link to the site's treatment of validation (`verifying-and-validating-a-simulation`, Section 4), which defines the comparison the insight proposes, nor to the companion insight `control-vs-learning-approaches`, which uses the same term.
- publishing 2: description 184 characters and a noun phrase, not a sentence.

## Priority

P2: required structure missing (framing paragraph, links), description over length; content sound.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| D1 | Blocking | line 12 | structure | No framing paragraph before "## Established" (standards 6.4, critical condition C7). |
| D2 | Should fix | whole file | consistency | No links to in-depth articles (standards 6.4, 8.2). |
| P1 | Should fix | `:3` | publishing | Description 184 characters, not a sentence. |
| C1 | Should fix | lines 14, 18 | language | Sentences of 52 and 56 words. |
| C2 | Should fix | line 22 | language | "One reasonable reading is that ... should be tested rather than assumed away. Some gap is expected to remain": hedge plus restatement. |
| C3 | Optional | line 30 | language | 60-word final sentence of Interpretation. |

### D1. Framing paragraph
- **Correction:** one paragraph: the question (defect to remove, or property to measure and report) and why it matters (it decides what evidence a reader should ask for before trusting a policy trained in simulation).

### D2. Links
- **Correction:** link "validation" to `/blog/verifying-and-validating-a-simulation#4-validation` (comparison of a model with measurements, with uncertainty) and the term to `/insights/control-vs-learning-approaches`.

### P1. Description
- **Text:** "A short research question on the gap between simulated and real robot behavior for learned controllers, and why it may be more useful as a measured property than as a defect to remove."
- **Correction:** a sentence of at most 165 characters (see revision log).

### C1. Long sentences
- **Text (line 18):** "Two widely used mitigation ideas are domain randomization, which varies ... and system identification, which fits ..."
- **Correction:** one sentence per technique, with each term in bold at its definition.

## Revision log (wave 1)

- Structure: added the framing paragraph (the question, and why it decides what evidence a claim about a simulation-trained robot needs). Three sections unchanged in order.
- Prose: the 52-word opening sentence of Established split; the 56-word mitigation sentence split into one sentence per technique, with **domain randomization**, **system identification** and **sim-to-real gap** in bold at definition; "One reasonable reading ... should be tested rather than assumed away. Some gap is expected to remain" tightened; the 60-word metric sentence split.
- Cross-references: added `/blog/verifying-and-validating-a-simulation#4-validation` (the gap as a validation question) and `/insights/control-vs-learning-approaches`.
- Metadata: description rewritten as one sentence (163 characters). Front-matter copied fields unchanged; no `updatedAt` (insights have none).
- Remaining suggestion: `sentence-length` at line 20 reports 54 words; the paragraph's sentences are 6, 27 and 21 words, so this is a splitter artifact around bold markup.
- Flags for independent review: none new; technical content unchanged.
- Vietnamese translation affected: yes: new framing paragraph, new link sentence on validation and the closing link to the comparison insight, new description.
