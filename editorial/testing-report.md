# Testing and validation report

Date: 15 October 2026. Scope: the Editorial Operating System (`plugins/editorial-os`, `editorial/`, the CI gates) and the revised ACRR content on branch `claude/editorial-operating-system-olemit`. Every result below comes from a command that was run, with the output quoted or summarized. Where something was not tested, this report says so.

Environment: Linux cloud container, Node 22.22, Python 3.13 with NumPy 2.5, Claude Code 2.1.296, Vale 3.24, Playwright Chromium.

## 1. Release check of the site

| Check | Command | Result |
|---|---|---|
| Type and template check, build, search index, URL guard | `SITE_URL=https://acrr.asia npm run build` | exit 0; `astro check` 0 errors; 314 pages built; Pagefind "Indexed 2 languages", "Indexed 103 pages"; `check-site-url: ok (rss.xml, sitemap-0.xml, sitemap-index.xml, vi/rss.xml: no localhost URLs)` |
| Internal links and fragments | `npm run check:links` | "All internal links resolve." (314 pages, 9,716 internal references in the scratch build of the same tree) |
| House-style errors | `npm run -s eos -- lint --quiet` | exit 0; "63 file(s): 0 error(s), 1 warning(s), 380 suggestion(s)". The warning is the unnumbered "Conventions used throughout the series" section of the first DSP entry, kept on purpose and justified in its review record. |
| Built-site checks (titles, descriptions, headings, KaTeX errors, Example labels, canonical and hreflang) | `npm run -s eos -- validate-site dist` | "No issues." on all 314 pages, English and Vietnamese |
| Editorial gate | `npm run -s eos -- gate` | "Editorial gate: passed. 63 item(s): 63 ready." |
| Series publication gate | `node scripts/series-pipeline.mjs gate` | "No failures." All nine series `ready`, each with a content-hash stamp matching the current text |

## 2. Editorial process results

| Stage | Result |
|---|---|
| Audit (phase 3) | 64 items scored; 15 P1, 48 P2, 1 P3; 13 blocking, 312 should-fix and 160 optional findings (`editorial/audit/audit-report.md`) |
| Revision (phase 4) | 99 content files changed since the audit baseline `e21dcc8` (2,201 insertions, 1,474 deletions); each change is logged in `editorial/audit/items/<slug>.md` |
| Independent review (phase 5) | 10 reports (9 series, 1 standalone): 1 blocking, 38 should-fix and 45 optional findings in total, each with evidence |
| Resolution and QA gate | Every blocking and should-fix finding was confirmed fixed by an independent QA editor; none was reopened. QA raised one new should-fix finding (serial commas in Machine Learning Fundamentals), which was fixed and confirmed before recording. |
| Scores (rubric of 28) | 48 articles: 26 to 28, mean 26.79; 6 insights and notes: 27 to 28, mean 27.17; 9 series overviews: 27 to 28, mean 27.67. No critical condition (C1 to C9) holds on any item. |
| Code and numbers | QA reran every Python block in each series it gated and compared the printed output (for example 13 of 13 identical in DSP, 11 of 11 in Machine Learning) and recomputed the numbers touched by fixes |

Each item's record is in `editorial/records/<type>/<slug>.json`, with its stages, scores, findings, reviewers, changes and what was not verified.

## 3. Plugin suite

| Test | Result |
|---|---|
| `claude plugin validate plugins/editorial-os` | "Validation passed" |
| Project-scope install through the repository's own marketplace | `claude plugin list` shows `editorial-os@acrr`, version 1.0.0, scope project, enabled |
| Agents usable by Claude Code | The final QA gates (including those for Machine Learning Fundamentals and Identity and Access Control) were run by the plugin's `editorial-os:qa-editor` agent, and the Machine Learning fix by `editorial-os:copy-editor` |
| PostToolUse hook | Returns lint findings as `additionalContext` for an edited content file; returns nothing for a non-content file (README) |
| `eos syntax` | "All files compile." for every MDX file |
| `eos vale-style` with Vale 3.24 | The generated style flags a planted "colour" (error) and "cutting-edge" (warning) |
| Portability: a Hugo-style layout with no `package.json` and no git | `init`, `status`, `lint`, `fix`, `hook`, `record` (pass and fail cases), stale detection after an edit, and `gate` (fail, then pass) all behaved as specified. Two defects found by this test were fixed in `bc55aaa`: the project root is now found from the `editorial/` folder, and the gate fails when no file matches the configured content types. |
| Integrity of the gate | A record goes `review-stale` when its file changes, and the gate fails until the item is reviewed and recorded again (shown in the portability test and on ACRR during this work) |

Not tested: other operating systems, agent hosts other than Claude Code, site generators other than Astro (the Hugo example configuration was tested only on a synthetic Hugo-style layout, not a real Hugo site), and the advisory `editorial-review.yml` workflow (it needs the `ANTHROPIC_API_KEY` secret, which is not set; without it the workflow skips with a summary message).

## 4. Known gaps and next actions

1. **`ANTHROPIC_API_KEY` secret is missing.** The AI review workflows (`editorial-review.yml`, `series-review.yml`) skip without it. The deterministic gates do not need it. Next action: add the secret in the repository settings.
2. **Vietnamese article bodies lag the English revision.** Series pages, insights, descriptions and the Identity entries are in step. The bodies of the other 14 translated articles were not retranslated, and the Vietnamese Machine Learning overview lags its revised English. Next action: retranslate them under `docs/translation-vi.md`.
3. **`updatedAt` was not set** on articles whose technical content changed, although standards 8.1 asks for it. Setting it now changes every file's hash and requires re-recording, so it is left for a decision. Next action: either set `updatedAt` (and the Vietnamese copies) and re-record, or exclude date-only edits from the content hash.
4. **380 lint suggestions remain**, most of them `serial-comma` and acronym suggestions; QA lowered the language score to 3 where real serial commas remain. None blocks publication.
5. **Unverified reference details** (for example some page ranges and issue numbers) are listed in each record's `notVerified` field. None is presented as verified.

## 5. Deployment

Recorded after the merge, from the deploy workflow's own logs: see the pull request and the final project message.
