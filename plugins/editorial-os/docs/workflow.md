# Publishing workflow

This is the lifecycle the `editorial` skill runs. Each step reads its state from the repository and leaves a file behind, so the workflow can stop at any point and resume, and re-running a finished step changes nothing.

`eos` means `node <plugin-root>/scripts/eos.mjs` (ACRR: `npm run eos --`).

## Overview

| # | Step | Owner (role) | Tool | Leaves behind |
|---|---|---|---|---|
| 1 | Discover and inventory | Managing Editor | `eos status`, `eos inventory --md` | Inventory in the audit report |
| 2 | Classify | Managing Editor | config `content.types`, `review.requiredStages` | Type, rubric and stages per item |
| 3 | Plan | Managing Editor | item report, "Plan" section | Stages, tools, fallbacks |
| 4 | Check sources and dependencies | Research/Fact-Checking Editor | `fact-checker` agent, `eos refs` | Reference findings; list of dependent entries |
| 5 | Draft or revise | Author | `eos fix`, `eos lint`, `eos syntax` | Revised file with no lint errors |
| 6 | Review | Developmental, Copy, Fact-Checking, Subject-Matter Editors | the four agents | One section per stage in the item report |
| 7 | Resolve | Author and Managing Editor | report, "Resolution" section | Every blocking and should-fix finding fixed or answered |
| 8 | Series review | Series Editor | project series skill or `series-editorial-review` | Series report (ACRR: `reviews/<id>.md`, stamped) |
| 9 | Validate | Technical Publishing Editor | `validation.commands`, `eos validate-site`, `eos lint` | Clean build, link check and site validation |
| 10 | Final gate | QA Editor | `qa-editor` agent, `eos record`, `eos gate` | Review record per item; gate exit 0 |
| 11 | Publish | Managing Editor | pull request, CI, merge, deploy workflow | Merged commit, deployment |
| 12 | Record | Managing Editor | post-deploy live check | Evidence in the pull request and the final report |

## Stages of an item

`eos status` derives one stage per item:

| Stage | Meaning | Next action |
|---|---|---|
| `draft` | `draft: true` in front matter | Not published; not gated |
| `lint-errors` | `eos lint` reports errors | Fix them (step 5) |
| `needs-review` | No review record | Review (step 6) |
| `needs-fixes` | Record decision is not `publish` | Resolve and re-review (steps 7, 10) |
| `review-stale` | File changed after the record was written | Re-review the changed passages, then re-record |
| `ready` | Current passing record, no lint errors | Publishable |

## Editorial queue

When the config has a `queue` section, every item also has an entry in `<queue.dir>/<type>/<slug>.json` (schema `schema/queue-entry.schema.json`). The record answers "did this file pass review"; the queue answers "where is this item in the publication workflow". The queue covers what happens before a file exists (proposal and research, with the reader-value contract) and after it is deployed (the chief editor's live review, findings, acceptance, maintenance, merge and retirement). It is not hashed, so editing it never makes a review stale.

| Status | Meaning |
|---|---|
| `proposed` | Idea proposal submitted (`templates/idea-proposal.md`); no file yet |
| `approved-for-research` | Contract approved; research log in progress (`templates/research-log.md`) |
| `drafting` | Draft in progress |
| `technical-review`, `editorial-review` | Review stages running |
| `revision-required` | Findings to resolve before publication |
| `ready-to-publish` | Current passing record; gates green |
| `published-awaiting-live-review` | Deployed; the chief editor has not yet reviewed the live page |
| `revision-required-after-publication` | Live findings open |
| `accepted` | Live page accepted by a permitted reviewer |
| `maintenance` | Accepted, and something it depends on has changed |
| `rejected`, `merged`, `retired`, `blocked` | Exceptional states (`merged` needs `mergedInto`, `retired` needs `redirect`) |

`eos queue validate` checks: every item has an entry; statuses and enums are valid; accepted items have a chief-editor acceptance with a reviewer and a report; high-risk items are accepted only by `queue.highRiskApprovers`; no accepted item has an open critical or major finding; items started or published from `queue.contractRequiredFrom` have an approved contract. `eos gate` adds these problems as failures when `queue.enforce` is `error`, reports them when it is `warn`, and ignores them when it is `off`.

## Live review

After deployment the chief editor reviews the public page (`skills/live-review`): captures of the live URL on a wide and a 360-pixel screen, light and dark, with rendering facts (ACRR: `.github/workflows/live-review.yml` and `scripts/live-capture.mjs`, published to the `live-captures` branch). The report (`templates/live-review-report.md`) goes to `editorial/live-reviews/<type>/<slug>.md`; findings are recorded with `eos queue finding`, the decision with `eos queue review`, which moves the queue status (`accepted`, `revision-required-after-publication`, `blocked`) and refuses an acceptance with open critical or major findings, without a risk level, or of a high-risk item by someone not in `queue.highRiskApprovers`. A finding is closed only after its acceptance condition is seen on new captures of the revised page.

## Review record

`eos record <file> --from review.json` writes `editorial/records/<type>/<slug>.json`. The input names the result of each required stage, the seven rubric scores (0 to 4), any critical conditions, finding counts, claims that were not verified, the changes made and the reviewers. The engine computes the decision: `publish` only when every required stage passed, no critical condition is present, no finding is open, the total meets the type's minimum and no dimension is below the per-dimension minimum. It also stores the file's content hash and appends to the record's history, so the record is an audit trail.

Rubric dimensions: purpose, structure, accuracy, evidence, language, consistency, publishing. The thresholds and the critical conditions are defined in the publication's standards manual; ACRR's are in `editorial/standards.md`, Policy E.

## Gates

| Gate | Where | Blocks |
|---|---|---|
| Hook | Claude Code, after each edit of a content file | Nothing; it adds the file's lint findings to Claude's context |
| `eos lint --quiet` | CI | Any `error`-severity rule |
| `eos validate-site` | CI, after the build | Missing or duplicate h1, missing `lang` or title, description length, missing alt text, KaTeX errors, heading jumps, duplicate ids, empty links, text glued to inline elements, oversized figures, house spelling on non-content pages |
| `eos gate` | CI | Any published item without a current passing record, or with lint errors |
| Project gates | CI (ACRR: build, `check:links`, `series-pipeline.mjs gate`) | Whatever the project defines |

In ACRR, `publication-gate.yml` runs all of these on every pull request to `master`, and `deploy.yml` runs them again before deploying, so nothing that fails a gate is published even if it reaches `master`.

## Independence

The author of a pass never reviews it. In practice: the agent or person who revised an item does not run its fact-check, technical review or QA; those are separate agent runs started with only the file, the standards and the review protocol. When a stage cannot be run independently, it is marked `fail` with the reason and the item stops before the gate.

## Evidence

A claim is "verified" only when a source was actually read (a fetched page, a standard's text, a calculation that was run). Everything else is "not verified", written into the record's `notVerified` list, and the text is qualified or the claim removed. A local build is not evidence of deployment; only the post-deploy check is.
