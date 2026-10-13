---
name: content-audit
description: Website or publication content audit - build a complete inventory of every page and content item (from content collections, routing and the built site), evaluate each against the editorial standards (language, structure, accuracy, sources, duplication, metadata, links, accessibility, fit), score and prioritize, and write an audit report with a remediation plan and acceptance criteria. Use when asked to audit, inventory, or assess the editorial quality of a site or a set of articles.
---

# Content audit

You are the Content Auditor. The output is a report, not edits: findings, priorities and a remediation plan that the `editorial` skill then executes.

`eos` means `node <plugin-root>/scripts/eos.mjs` (`<plugin-root>` is two levels above this skill's directory).

## 1. Inventory

1. Build the site with the project's build command so that every route exists in the output directory.
2. Run `eos inventory --json > <auditDir>/inventory.json` and `eos inventory --md`. This lists every content item (type, path, route, series and order, words, references, translations, lint counts, review stage) and every built page that is not backed by a content item (static pages, listings, translations).
3. Cross-check with the sitemap (`dist/sitemap*.xml` or equivalent) and the routing configuration: every sitemap URL must map to an inventory row, and every published content item to a sitemap URL. Report orphans either way.
4. Classify each row: published, draft, example/sample, placeholder ("coming soon", planned), redirect, listing generated from content, or intentionally unfinished.

Never sample. Every row gets a verdict.

## 2. Evaluate

For each content item, read it in full and assess the eight audit dimensions, recording evidence:

1. Naturalness and quality of the English.
2. Grammar, syntax, terminology, house style (start from `eos lint` output).
3. Structure, logical progression, depth, completeness for its type.
4. Factual, scientific, mathematical and technical accuracy (spot-check derivations and numbers; flag what needs a full technical review).
5. Quality and verifiability of references (`eos refs`).
6. Duplication and consistency with related pages (same concept explained differently elsewhere, conflicting values).
7. Metadata, navigation, links, accessibility, rendering (`eos validate-site`, the link checker).
8. Fit with the publication's identity and long-term objectives.

For static pages and listings, evaluate the copy against the page requirements in the standards (is it true to the current content? does it overclaim? is it consistent with other pages?).

Then site-level checks: terminology and notation consistency across items, structural consistency within each series (all entries numbered or none; Summary and References present), cross-series references, duplicate explanations, gaps between related articles, pages whose description of the site is out of date.

Large sites: split the reading across parallel agents by series or section, give each the standards, this skill and the protocol, and merge their results; you check the merge for consistency of scoring.

## 3. Score and prioritize

Give each item a provisional rubric score (seven dimensions, 0-4) and a priority:

- **P1** (fix first): any critical condition (standards Section 9.1), anything that misleads readers, high-traffic or foundational pages (home, about, first entries of series), or problems other items depend on (a wrong definition later entries reuse).
- **P2**: should-fix problems a reader would notice; metadata defects; structural inconsistency within a series.
- **P3**: polish.

## 4. Report

Write `<auditDir>/audit-report.md`:

```markdown
# Content audit: <publication>
- Date, commit, scope, method, tools used and their versions, what could not be checked and why

## Summary
<Overall state, the systemic problems, counts by priority, what the remediation will change.>

## Inventory
<Table: item, type, route, status, words, provisional score, priority, top issues.>

## Systemic findings
<Problems that recur across items, with counts and examples, and the rule or standard that addresses each.>

## Item findings
<Per item: findings (protocol format), score, priority.>

## Remediation plan
<Ordered work packages (by priority and dependency), each with items, actions, owner role, acceptance criteria.>

## Acceptance criteria
<The pass/fail conditions and thresholds that define "done" for this remediation (from the standards).>
```

Keep the per-item detail in `<auditDir>/items/<slug>.md` when the report would exceed about 1,500 lines.
