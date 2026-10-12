---
name: handoff
description: Save ACRR session memory — update the short-term working notes (in-progress task, next steps, open questions) and record lasting decisions or lessons in long-term memory. Use at the end of a work session, before a context reset, when the user says "remember this", or after a non-obvious decision or a bug whose cause others would trip over again.
---

# Project memory

Cloud sessions start from a fresh clone, so memory that is not committed is lost. Three layers, from most to least volatile:

| Layer | File | Holds | Loaded |
| --- | --- | --- | --- |
| Short-term | `.claude/memory/working-notes.md` | Current task, state, next steps, open questions for the user | Every session (imported by CLAUDE.md) |
| Long-term (why) | `.claude/memory/decisions.md` | Dated decisions and lessons with their reason | On demand: read before changing something it mentions |
| Long-term (rules) | `CLAUDE.md` | Stable rules, commands, architecture, gotchas | Every session |

## Update short-term memory

Rewrite `working-notes.md` (do not append forever; keep it under ~40 lines). Keep the headings: **Current focus**, **State** (what is done, what is uncommitted, branch), **Next steps** (concrete, ordered), **Open questions** (for the user), **Last updated** (date). When a task is finished, clear it back to "None" rather than leaving stale notes.

## Update long-term memory

Add an entry to the top of `decisions.md` when something was decided or learned that a future session would otherwise re-litigate or rediscover: a design choice and its rejected alternative, a user preference, a root cause. Format:

```
## YYYY-MM-DD — <short title>
Decision/lesson in one or two sentences. **Why:** the reason. **Applies to:** files or areas.
```

Promote an entry into CLAUDE.md (Gotchas or Architecture) when it has become a rule every session must follow, and keep CLAUDE.md accurate when code changes make a line in it false. Do not copy into memory what the code or git history already says plainly.

## Never store

Secrets, tokens, `.env` values, personal data about the author beyond what is published on the site, or the user's email.

## Finish

Commit the memory files together with the work they describe.
