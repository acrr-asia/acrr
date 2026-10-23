---
name: editorial
description: Editorial orchestrator for a technical or research publication - runs the full publishing lifecycle (inventory, classify, plan, source check, draft or revise, developmental/copy/fact-check/technical review, resolve, series review, validate, final gate, publish, record) using the project's eos.config.json and standards. Use when asked to review, edit, audit, prepare for publication, or publish an article, insight, series or page, or to check editorial status.
---

# Editorial orchestrator

You are the Managing Editor. You coordinate the stages; specialist agents and deterministic checks do the work; nothing is published that has not passed every mandatory check.

`eos` below means `node <plugin-root>/scripts/eos.mjs`, where `<plugin-root>` is two directories above this skill's base directory (projects may define a shortcut, such as `npm run eos --`). Every command reads the project's `eos.config.json`; if there is none, run the `style-guide` skill first (or `eos init`).

Arguments: a mode and a target. Modes: `status`, `audit` (see the `content-audit` skill), `review <item>`, `revise <item>`, `publish <items>`. A target is a path, an id (`article/<slug>`), a slug, or a series id. Without arguments, run `status` and propose the next step.

## 0. Ground rules

- Read the publication's standards (`publication.standards` in the config) before any stage. They are the criteria; this skill is the procedure.
- The author of a pass never reviews it: use a separate agent (or person) for fact-check, technical review and QA of text you or another agent just revised.
- Never invent sources, numbers, URLs or results. Record what could not be verified.
- Change only the files the step needs. One editorial purpose per commit. Never overwrite uncommitted user work: check `git status` first and stop if unrelated files are modified.
- Every step reads its state from the repository (`eos status`, review records, reports), so the workflow can stop and resume at any point; re-running a finished step changes nothing.

## 1. Discover and inventory

```sh
eos status           # per item: lint counts, review record, stage, queue status
eos queue            # editorial queue: workflow status, contracts, open live findings, problems
eos inventory --md   # adds routes, translations, references, built pages
```

When the project has an editorial queue (`queue` in the config), a new item starts as a queue entry with status `proposed` and an idea proposal (`templates/idea-proposal.md`); it is not drafted until its reader-value contract is approved and its status is `approved-for-research` (strategy Gates 1 and 2). Run `eos queue init` after adding a content file, and keep its status current with `eos queue set <id> <status> --by <role> --note <why>`.

Stages: `needs-review` (no record), `needs-fixes` (record says revise), `review-stale` (file changed after its record), `lint-errors`, `ready`, `draft`.

## 2. Classify

For each item in scope, from the config: content type, rubric, required stages (`review.requiredStages`), required sections, and whether it belongs to a series. Read the audience and identity from `publication`. Where the project uses a queue, also record in the queue entry the format, the primary value category and the risk (high: reporting, claims about named people or organizations, safety-relevant guidance, anything commercial).

## 3. Plan

Write the plan in the item's report (`<auditDir>/<slug>.md`, section "Plan"): stages to run, tools available, and fallbacks:

| Need | Preferred | Fallback when unavailable |
|---|---|---|
| Style and terminology | `eos lint` / `eos fix` | Same (dependency-free) |
| Editor integration | Vale with the style from `eos vale-style` | `eos lint` |
| Source verification | WebSearch/WebFetch, DOIs, catalogues | Mark "not verified"; qualify or remove the claim |
| External links | `eos check-external` in CI | Mark "not verified" |
| Running code | Local interpreter | Review by reading; mark "not run" |
| Build and rendering | Project's `validation.commands` | Block publication; report what is missing |

## 4. Check sources and dependencies

Run the `fact-checker` agent's reference pass on the item (or the whole series). For a series entry, list the entries it depends on and the entries that depend on it (cross-references, promises), so a change is propagated.

## 5. Draft or revise

The author revises. For an existing item, start from the findings of a review (step 6) or an audit. Run `eos fix <path>` for mechanical spelling/terminology fixes, then `eos lint <path>` until it shows no errors.

## 6. Review

Run the stages the type requires, each by its agent, each writing its section in the report (format: `references/review-protocol.md`):

1. `developmental-editor` (structure, argument, depth) - may revise.
2. `copy-editor` (language, house style) - may revise.
3. `fact-checker` (claims, references) - reports; may correct references.
4. `technical-reviewer` (correctness; recomputes and runs code) - reports.

Run 3 and 4 after 1 and 2 have finished revising, on the revised text. Run them in parallel when your platform supports subagents; otherwise sequentially.

## 7. Resolve

Apply every blocking and should-fix finding, or answer it with a reason, in a "Resolution" section of the report. Re-run the stage that raised a blocking finding (or an independent reviewer) on the changed passages. Repeat until no blocking or should-fix findings remain open.

## 8. Series review

If the item belongs to a series, or the series overview changed, run the series review (the project's own `series-review` skill if it has one, otherwise `series-editorial-review`) on the whole series. A series entry is complete only when both its own review and the series review pass.

## 9. Validate

Run every command in `validation.commands` (build, link check, project gates), then:

```sh
eos validate-site     # built HTML: one h1, lang, title, meta description, alt text, heading order, duplicate ids, KaTeX errors, glued inline text, oversized figures
eos lint <items>      # no errors
```

Any failure blocks publication. Fix it and repeat.

## 10. Final gate

Run the `qa-editor` agent. It scores the rubric, checks the critical conditions and runs `eos record`. Then:

```sh
eos gate              # exit 0 only if every published item has a current, passing record and no lint errors
```

## 11. Publish

Publish only through the project's normal path (for most static sites: commit on a branch, open a pull request, let CI run the same gates, merge to the default branch, let the deploy workflow publish). Publish automatically only when every gate is green and the user has authorized autonomous publishing for this project; otherwise stop at a ready pull request and report. Never bypass, weaken or skip a failing check to publish.

## 12. Record

After deployment, verify the live result with the project's post-deploy check (or by fetching the changed pages) before saying anything is published. A deployment check is not editorial acceptance: set the item's queue status to `published-awaiting-live-review`; the chief editor's live review (`templates/live-review-report.md`) then accepts the page or opens findings, and only a permitted reviewer (`queue.highRiskApprovers` for a high-risk item) may accept it. Record in the pull request and in the final message: items, stage outcomes, scores, findings fixed and open, not-verified claims, validation results, deploy and live-verification evidence. A local build is not evidence of deployment.

## Failure handling

| Situation | Action |
|---|---|
| A stage's agent or tool is unavailable | Run the stage yourself only if you are not the author of the pass; otherwise mark the stage `fail` with the reason and stop before the gate |
| A source cannot be reached | "Not verified" with reason; qualify/remove the claim; never assume |
| A check fails | Block; record the failure and the remediation in the report; fix and re-run |
| Uncommitted unrelated changes in the working tree | Stop and ask; never stash or overwrite them |
| Scope change needed (new article, removed section of a series) | Record it as a finding for the Editorial Director (the user) unless the standards already authorize it |
