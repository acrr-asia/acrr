---
name: editorial-review
description: Full multi-stage editorial review of one article, insight or page - developmental edit, copy edit, fact-check, technical review, publishing checks and the QA decision - producing a single traceable report and an eos review record. Use when asked to review, edit or approve one piece of content for publication.
---

# Editorial review of one item

This is step 4-10 of the `editorial` orchestrator for a single item. Use it when only one item is in scope.

`eos` means `node <plugin-root>/scripts/eos.mjs`.

1. **Prepare.** `eos lint <path>`; read the standards and `references/review-protocol.md`; create `<auditDir>/<slug>.md` with a header (item, commit, date, type, required stages).
2. **Developmental** - run the `developmental-editor` agent on the item (mode: revise if the user asked for revision, otherwise report). Its findings go under `## Developmental review`.
3. **Copy** - run the `copy-editor` agent (same mode). `## Copy edit`.
4. **Fact-check** - run the `fact-checker` agent on the current text. `## Fact-check`.
5. **Technical** - run the `technical-reviewer` agent on the current text. `## Technical review`.
6. **Resolve** - apply or answer every blocking and should-fix finding; write `## Resolution` with what was applied and how; re-run the reviewer of any blocking finding on the changed passage.
7. **Publishing** - run the project's validation commands, then `eos validate-site` and `eos lint`; write `## Publishing checks` with the results.
8. **QA** - run the `qa-editor` agent; it records the decision with `eos record`.

Report back: the decision, total score, findings by severity (fixed and open), what was not verified, and the record path.

If an agent is unavailable, the stage may be performed in the main session only if the main session did not write the text in this pass; otherwise mark the stage `fail` and stop before QA.
