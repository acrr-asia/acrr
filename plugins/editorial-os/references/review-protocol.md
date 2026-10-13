# Review protocol (shared by every editorial-os stage)

Every review stage, whichever role performs it, follows these rules so that findings from different stages can be merged, resolved and audited in one place.

## Inputs every stage reads first

1. The publication's standards (the file named by `publication.standards` in `eos.config.json`, usually `editorial/standards.md`). Its policies and rubric are the review criteria; this protocol only fixes the format.
2. The glossary (`glossary.json`) and the configured language variant.
3. The item itself, in full. Never sample or skim. For a series entry, also the series overview and the entries it refers to.
4. The deterministic results: `node <plugin>/scripts/eos.mjs lint <item>` (and, for publishing checks, the build and `eos validate-site`). Do not re-report what the linter reports unless you disagree with it; cite the rule instead.

## Independence

The reviewer of a stage must not be the author of the text in that pass. An agent that has just written or revised an item does not fact-check, technically review or QA it in the same session. If no independent reviewer is available, say so in the record (`notes`) and lower nothing silently.

## Severity

- **Blocking**: wrong (technically, factually, mathematically), fabricated, a reference that does not exist or does not support the claim, a false cross-reference, a content-integrity breach, a failed build or link, missing required sections or metadata. Must be fixed before publication.
- **Should fix**: misleading, imprecise or ambiguous; a concept used before it is introduced; an unstated version, unit or convention that matters; inconsistent terminology; structural problems a reader would notice; prose that obscures meaning; generic or padded writing.
- **Optional**: polish and style beyond the standards.

Be specific and conservative. Report only what you can point to, with a quotation. Do not report personal preferences as defects.

## Finding format

```markdown
| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| D1 | Should fix | `path:41`, Section 2 "..." | structure | one line |

### D1. Short title
- **Where:** `path:line`, section "Heading"
- **Text:** "exact quotation"
- **Problem:** what is wrong and why, with evidence (a standard and clause, a recomputation, a source, the contradicting passage with its path:line)
- **Correction:** replacement text ready to paste, or a precise instruction
```

Prefix IDs by stage: D (developmental), C (copy), F (fact-check), T (technical), S (series), P (publishing), Q (QA). Dimensions are the rubric keys: `purpose`, `structure`, `accuracy`, `evidence`, `language`, `consistency`, `publishing`.

## Evidence rules

- A technical correction needs a derivation, a recomputation (say what you ran and the result), or a primary source.
- A factual correction needs a source of the kind the standards accept; name it precisely.
- When a claim cannot be verified with the tools available, record it under **Not verified** with the reason (no network, paywalled, no tool to run the code), and recommend the smallest defensible change: qualify the claim, attribute it, or remove it. Never "correct" toward a guess.
- Never introduce a reference, URL, number or quotation you have not verified.

## Output of a stage

A stage writes its findings to the audit or review report named by the orchestrator (default `editorial/audit/<item-slug>.md`, one section per stage) and returns:

- the counts by severity;
- the blocking findings in one line each;
- its stage verdict: `pass` (no blocking or should-fix findings left), `fail`, or `n/a` with a reason.

## Resolution

The author (or the revising agent) applies every blocking and should-fix finding, or answers it with a reason in a **Resolution** section of the report. Optional findings are applied when they are clear improvements. After resolution, the stage that raised a blocking finding (or an independent reviewer) confirms the fix.

## Recording the outcome

At the end, the QA stage writes a review input file and records it:

```json
{
  "stages": { "developmental": "pass", "copy": "pass", "factCheck": "pass", "technical": "pass", "publishing": "pass", "qa": "pass" },
  "scores": { "purpose": 4, "structure": 4, "accuracy": 4, "evidence": 3, "language": 4, "consistency": 4, "publishing": 4 },
  "critical": [],
  "findings": { "blocking": 2, "shouldFix": 7, "optional": 3, "open": 0 },
  "notVerified": ["Claim X at path:120: source paywalled; text now attributes the figure to its source"],
  "changes": ["Restructured Section 3 so the concept precedes the protocol fields", "Corrected the overshoot formula (recomputed: 16.3%)"],
  "reviewers": ["developmental-editor", "copy-editor", "fact-checker", "technical-reviewer", "qa-editor"],
  "reportRef": "editorial/audit/<slug>.md",
  "notes": ""
}
```

```sh
node <plugin>/scripts/eos.mjs record <path> --from review.json
```

`eos record` recomputes the content hash, adds the lint counts, evaluates the thresholds of the publication's configuration and writes `decision: publish` only if every requirement holds. It never overrides a failing condition; fix the item and record again.
