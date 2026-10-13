# Changelog

## 1.0.0 (2026-10-13)

First release, built for and verified on ACRR (https://acrr.asia).

- Skills: `editorial` (orchestrator), `content-audit`, `editorial-review`, `series-editorial-review`, `style-guide`.
- Agents: `developmental-editor`, `copy-editor`, `fact-checker`, `technical-reviewer`, `qa-editor`.
- Engine `scripts/eos.mjs`: `init`, `inventory`, `lint`, `fix`, `status`, `record`, `gate`, `validate-site`, `refs`, `check-external`, `vale-style`, `syntax`, `hook`, `hash`.
- PostToolUse hook that adds lint findings for an edited content file to Claude's context.
- JSON Schemas for the configuration and review records; templates for a new site.
- Verified with Node 22.22 and Claude Code 2.1.296 on Linux.
