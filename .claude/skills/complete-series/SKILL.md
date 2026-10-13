---
name: complete-series
description: Autonomous editorial pipeline for ACRR series - discover unfinished series, write the missing entries, run the series review on every completed series, fix its findings, pass the publication gate, publish through master and verify the live pages. Use when asked to complete, finish or publish series, or to resume that work. Optional argument - one series id; without it, every unfinished series.
---

# Complete and publish series

This is the end-to-end workflow for finishing series, the way a technical publisher takes a book from outline to print: research, drafting, technical review, series-wide review, copyediting, validation, publication and post-publication checks. Every step reads its state from the repository, so the workflow can be interrupted and resumed at any point, and re-running a finished step changes nothing.

Read `CLAUDE.md` first, in particular "Content-integrity rules" and "Languages". They apply to every word written here.

## 0. Find where things stand

```sh
node scripts/series-pipeline.mjs status
```

Each series is in one stage. Work on it from that stage; never redo a later one.

| Stage | Meaning | Next step |
|---|---|---|
| `needs-writing` | Planned entries remain, or the series is not marked published | Step 1 |
| `needs-review` | Complete, no review report | Step 2 |
| `needs-fixes` | Report has unresolved blocking or should-fix findings | Step 3 |
| `review-stale` | The series changed after its review was stamped | Step 2 (a new review of the whole series) |
| `ready` | Complete, reviewed, resolved, current | Step 5 if not yet on `master` |

Before writing anything, check for work in progress: open pull requests and branches named `series/<id>` or `review/<id>`, and articles already in `src/content/blog/` with `series: <id>`. Continue them rather than starting again; never create a second article for an entry that already exists (search titles and slugs).

## 1. Write the missing entries

1. Audit the series: read the series file, every existing article in order, and the reviews of related series. List missing entries, gaps in `seriesOrder`, drafts, unfulfilled promises ("a later entry ...", "the next entry ..."), inconsistent terminology and missing prerequisites. Decide the remaining entries and their order; the `plannedEntries` are the starting outline, not a contract.
2. Write each entry as `src/content/blog/<slug>.mdx` with `series` and `seriesOrder`. Follow the house style of the existing entries of the series (and, for a new series, of a recent long-form series such as `sensor-systems`): an opening that states what the entry builds on and assumes, concepts introduced before their details, worked examples whose numbers you recomputed, code you ran (quote real output), diagrams (Mermaid or the generated SVG components) only where they earn their place, exercises with answers where useful, a summary table, a closing paragraph that leads to the next entry, and references that you are certain exist. No URLs that you have not been given; no fabricated facts.
3. Link the earlier entries forward to the new ones where they promise them, in the English article and in its Vietnamese translation if one exists.
4. When no planned entries remain: set `status: "published"`, remove `plannedEntries`, rewrite the series body so it no longer says "planned", and make the same changes in `src/content/series/vi/<id>.md` (the build checks that status and the number of planned entries match).
5. Run `npm run build:local` and `npm run check:links`; fix anything they report.

## 2. Review the whole series

Run the series review exactly as `.claude/skills/series-review/SKILL.md` prescribes (`/series-review <id>`), on all entries, old and new, as one publication. It writes `reviews/<id>.md`. A reviewer other than the author of the new entries (for example a separate agent with no part in the writing) gives the most useful review.

## 3. Resolve the findings

Apply every blocking and should-fix finding, and the optional ones that are clear improvements; apply the same change to existing Vietnamese translations of any corrected sentence. Add a `## Resolution` section after the report's Summary saying what was applied and how. Then re-read the whole series as a second pass for defects the corrections introduced, fix them, and record that pass in the Resolution section. Repeat until a full pass finds nothing blocking or should-fix. A significant revision of one article means re-checking the whole series, not only that article.

## 4. Gates

All of these must pass; none may be skipped, weakened or worked around to finish sooner:

```sh
SITE_URL=https://acrr.asia npm run build    # types, schemas, Mermaid, KaTeX, search index, sitemap/RSS guard
npm run check:links                          # every internal link and #fragment
node scripts/series-pipeline.mjs stamp <id>  # only after step 3: records the reviewed content hash
node scripts/series-pipeline.mjs gate        # every complete series has a current, resolved review
```

Also check each new page in `dist/blog/<slug>.html` for `katex-error`, Mermaid figures wider than about 600px, and text glued to inline elements (see `CLAUDE.md`). `stamp` refuses a report without a Resolution (when it has findings) or without a Verification log. Any edit to a series after stamping makes the gate fail until the series is reviewed again and re-stamped.

## 5. Publish

Publication is a merge to `master`: `.github/workflows/deploy.yml` builds, re-runs the link check and the gate, deploys to GitHub Pages and then runs the `verify` job, which fetches every page in the sitemap from https://acrr.asia and checks it returns HTTP 200 with the expected title.

1. Commit on a branch (one series, or one coherent group of series, per pull request) and open a pull request. `.github/workflows/publication-gate.yml` runs the same gates on it.
2. When the gate is green, merge.
3. Watch the **Deploy to GitHub Pages** run for the merge commit to the end, including `verify`. Read its summary ("Live verification of https://acrr.asia: passed").
4. Do not report anything as published until that run has succeeded and the verify job has passed. If deployment or verification fails, diagnose and fix it, or report the exact failure and what is needed.

## 6. Report

Keep a record in the pull request description and in the final message: series completed, articles published (route and title), review results (counts by severity, what was fixed, anything unresolved), gate and build results, the deploy and verify run links, and any remaining blocker with its impact and the action needed.

## Protect what is already there

Change only the files the step needs. Never rewrite history on `master`, never commit `dist/`, `.astro/`, `node_modules/` or secrets, and never edit unrelated articles beyond the forward links of step 1.3 and the corrections of step 3.
