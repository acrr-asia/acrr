# Changelog

## 1.2.0 (2026-10-23)

- Live review: skill `live-review` (the chief editor's review of the public page, report, findings, decision, re-review); `eos queue review <id> <decision>` (sets the chief-editor review and moves the queue status; refuses an acceptance with open critical or major findings, without a risk level, or of a high-risk item by a reviewer not in `queue.highRiskApprovers`) and `eos queue finding <id> add | <status> <finding>` (closing a finding needs a note on what was checked live). Accepted limitations no longer count as open findings.

## 1.1.0 (2026-10-23)

- Editorial queue: `eos queue` (list), `queue init`, `queue set`, `queue validate`; schema `schema/queue-entry.schema.json` (workflow status from proposal to accepted after the live-site review, reader-value contract, format, value category, risk, live findings, disclosures, history). Config `queue` (`dir`, `enforce` off/warn/error, `contractRequiredFrom`, `highRiskApprovers`). `eos gate` reports or enforces queue problems according to `queue.enforce`; `eos status` shows each item's queue status.
- Templates: `idea-proposal.md` (Gate 1), `research-log.md` (Gate 2), `live-review-report.md` (the chief editor's live-site review, sections A-G).
- The `editorial` skill and `docs/workflow.md` describe the queue and the live review.

## 1.0.0 (2026-10-13)

First release, built for and verified on ACRR (https://acrr.asia).

- Skills: `editorial` (orchestrator), `content-audit`, `editorial-review`, `series-editorial-review`, `style-guide`.
- Agents: `developmental-editor`, `copy-editor`, `fact-checker`, `technical-reviewer`, `qa-editor`.
- Engine `scripts/eos.mjs`: `init`, `inventory`, `lint`, `fix`, `status`, `record`, `gate`, `validate-site`, `refs`, `check-external`, `vale-style`, `syntax`, `hook`, `hash`.
- PostToolUse hook that adds lint findings for an edited content file to Claude's context.
- JSON Schemas for the configuration and review records; templates for a new site.
- Rules include a `serial-comma` suggestion (when `language.serialComma` is false); contractions joined by a hyphen ("don't-care") are compound terms and not reported; proper nouns may be phrases.
- Verified with Node 22.22 and Claude Code 2.1.296 on Linux.
