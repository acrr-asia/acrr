<!-- audit: {"slug":"machine-learning-fundamentals","type":"series","series":"machine-learning-fundamentals","priority":"P2","before":{"purpose":3,"structure":2,"accuracy":4,"evidence":4,"language":3,"consistency":3,"publishing":4},"findings":{"blocking":0,"shouldFix":3,"optional":2}} -->
# Audit: Machine Learning Fundamentals

- Path: `src/content/series/machine-learning-fundamentals.md` · Route: `/series/machine-learning-fundamentals` · Type: series overview · 4 entries, status published, no planned entries · Words: 100 (`eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 3: reader and prerequisites are stated, but the page does not say why the entries come in this order.
- structure 2: one paragraph; Section 6.5 asks for the sequence rationale, what each entry contributes and how they connect, and the shared conventions. The paragraph lists topics but not entries, and conventions (Python and NumPy versions, fixed seeds, MSE without the factor 1/2, the 0/1 coding of classes) are only in the first entry.
- accuracy 4
- evidence 4: no claims needing sources.
- language 3: one 47-word sentence (`:13`) that strings five topics together.
- consistency 3: "numpy" for the proper name NumPy.
- publishing 4: description 139 characters; four objectives, each starting with an assessable verb, each covered (see the series audit).

## Priority

P2: the front door of a complete series; structural gaps against Section 6.5 a reader would notice, no misleading content.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| D1 | Should fix | `:13` | structure | No sequence rationale and no account of what each entry contributes. |
| D2 | Should fix | `:13` | consistency | Shared conventions (versions, seeds, MSE definition, class coding) not stated on the overview. |
| C1 | Should fix | `:13` | language | 47-word sentence listing the whole syllabus. |
| C2 | Optional | `:13` | consistency | "numpy" → "NumPy" (proper name of the library). |
| C3 | Optional | `:3` | publishing | Description "A series on the core ideas ..." is a noun phrase, not a sentence. |

### D1. Missing sequence rationale
- **Where:** `:13`
- **Text:** "It builds supervised learning from first principles: the learning problem as minimizing a loss over examples, gradient descent and its stochastic variants, why flexible models overfit and how regularization limits that, and how to evaluate a model honestly, ..."
- **Problem:** Standards 6.5 require the overview to say why the entries come in this order and how they connect. The order (problem, optimizer, generalization, evaluation) is deliberate: each entry resolves a question the previous one leaves open, but the page does not say so.
- **Correction:** a paragraph per the revision below, naming the four entries and the question each answers.

### D2. Shared conventions
- **Where:** `:13`
- **Text:** "Every example uses small synthetic data sets in Python with numpy, so that the true answer is known and each number can be reproduced."
- **Problem:** The versions (Python 3.13, NumPy 2.5.3), the stated-seed policy, the MSE convention (no factor 1/2) and the class coding $y \in \{0,1\}$ are shared by all entries but stated only in entry 1.
- **Correction:** add one paragraph of conventions.

### C1. Long sentence
- **Where:** `:13`
- **Text:** the sentence quoted in D1 (47 words).
- **Problem:** Standards 5.2; it also does the job of D1 badly.
- **Correction:** replaced by the per-entry paragraph.

## Revision log (wave 1)

- Structure: body rewritten as three short paragraphs: (1) reader and prerequisites; (2) the sequence rationale, naming each entry and the question it answers and how the next entry takes it up; (3) shared conventions (Python 3.13 and NumPy 2.5.3, stated seeds, synthetic data with known Bayes risk, MSE as the plain average, classes coded 0 and 1, numbered sections cited as "Section 3.2 of the first entry").
- Metadata: description rewritten as one sentence of 156 characters naming the four entries; objectives unchanged (all four are met; changing them would desynchronize the Vietnamese translation's objectives).
- Terminology: "numpy" → "NumPy".
- Remaining warnings: none expected.
- Flags for independent review: none.
- Vietnamese translation affected: yes, `src/content/series/vi/machine-learning-fundamentals.md` body and description no longer match the English (the English body now explains the sequence and conventions). No copied field changed.
