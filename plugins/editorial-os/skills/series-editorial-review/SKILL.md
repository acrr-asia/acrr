---
name: series-editorial-review
description: Integrated review of a complete article series as one publication - purpose, audience, scope and objectives; sequence and its rationale; prerequisites and conceptual dependencies; terminology, notation, assumptions and depth across entries; overlap, contradictions and gaps; transitions, cross-references and promises; the series overview. Use when a series is complete or revised, unless the project defines its own series-review skill (then use that).
---

# Series editorial review

A series passes only when every entry has passed its own review and the series as a whole passes this one. If the project has its own series-review skill (for example `.claude/skills/series-review/SKILL.md`), use it instead; this skill is the generic version.

`eos` means `node <plugin-root>/scripts/eos.mjs`.

## 1. Collect

- The series overview (the item whose type has `isSeriesIndex`) and every entry, in order: `eos lint <series-id>` lists them and checks ordinal cross-references ("the third entry" links to entry 3) and numbered section references ("Section 4.2 of the first entry").
- Read the overview, then **every entry in full, in order**. Keep notes per entry: concepts introduced (where), concepts used (where first used), notation and symbols, conventions and versions assumed, claims later entries rely on, references to other entries, and promises ("a later entry ...").

## 2. Review dimensions

| Dimension | Question |
|---|---|
| Purpose, audience, scope | Does the overview state who the series is for, what it covers and excludes, and what the reader can do at the end? Are the objectives checkable? |
| Sequence and rationale | Is the order the best order for the stated reader? Is the reason for it stated? Would moving or splitting an entry help? |
| Prerequisites and dependencies | Is everything an entry relies on either a stated prerequisite or introduced in an earlier entry (and referred to)? Does anything rely on a later entry? |
| Consistency | Terms, symbols, notation, units, sign and coordinate conventions, language versions and depth agree across entries. The same quantity has the same symbol. |
| Overlap, contradiction, gaps | Is anything explained twice (should be a back-reference)? Does any entry contradict another? Is a topic the objectives require missing? |
| Continuity | Does each entry open by connecting to what came before and close by leading to the next? Does the last entry close the series against its objectives? |
| Cross-references and links | Every "the n-th entry", "Section x.y" and link is correct; every promise is kept. |
| Overview completeness | The overview lists the role of each entry (directly or through entry descriptions), the prerequisites and the shared conventions, and promises nothing the entries do not deliver. |
| Delivery | Does the series deliver every stated objective? Map each objective to the entries and sections that meet it. |

Severity, evidence and format: `references/review-protocol.md` (prefix S).

## 3. Report

Write `<auditDir>/series-<id>.md` (or the project's series report path) with: header (series, entries, commit, date), Summary with `Findings: <b> blocking, <s> should fix, <o> optional.`, Objectives coverage table, Concept introduction map, Notation and conventions table, Cross-reference map, Findings, and a Verification log (lint, build, link check, what was recomputed).

## 4. Resolve and close

Apply the findings (reorder, revise entries, add missing material within scope, update the overview), propagate changes to dependent entries, re-run `eos lint <series-id>`, then re-review the changed entries individually (`editorial-review`) because their records are now stale. Add a Resolution section. The series is complete when no blocking or should-fix findings remain, every entry has a current passing record (`eos gate`), and the project's series gate (if any) passes.
