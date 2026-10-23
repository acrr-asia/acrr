---
name: live-review
description: Chief editor's live-site review - inspect a published page as readers see it (captures of the public URL on a wide and a 360-pixel screen, light and dark), judge it against its reader-value contract and the standards, write the live-review report, record findings and the decision in the editorial queue, and re-review after revisions. Use after a deployment, when an item is published-awaiting-live-review, or when asked to review the live site.
---

# Live review (chief editor)

You are the chief editor reviewing the **public page**, not its source (standards 4.4, strategy Gates 7 to 9). A build, a deployment, `verify-live` or a green gate is not acceptance. You did not write or revise the page in this pass; if you did, stop and hand the review to an independent run.

## 1. Get the captures

The `Live review captures` workflow (`.github/workflows/live-review.yml`) runs after every deployment for the pages that changed, and on demand (`routes`: `changed`, `all`, or a list of routes). It force-pushes the latest run to the `live-captures` branch:

```sh
git fetch --depth 1 origin live-captures
git worktree add --detach /tmp/live-captures FETCH_HEAD    # or: git archive FETCH_HEAD | tar -x -C <dir>
cat /tmp/live-captures/run.json /tmp/live-captures/index.md
```

`run.json` names the deployed commit and the run. Each page has a folder (`blog__dft-and-fft` for `/blog/dft-and-fft`) with `facts.json` and screen-sized tiles: `desktop-light-NN.jpg` (1280 px), `mobile-light-NN.jpg` and `mobile-dark-NN.jpg` (360 px). Check that the run's commit is the one that contains the version you are reviewing; if the page is not in the run, start one (`actions_run_trigger` on `live-review.yml` with `routes: "<route>"`) and wait for it. A local build or `npm run preview` is not the live page; use it only to locate a defect you already saw in the captures.

## 2. Read the page as a reader

1. Read the queue entry (`editorial/queue/<type>/<slug>.json`): format, value category, risk, contract (if `missing` or `reconstructed`, write a reconstructed contract from the page and label it so; never present it as the author's intent), open findings.
2. Read `facts.json` for every viewport: HTTP status, h1, horizontal scroll at 360 px, elements wider than the screen, KaTeX errors, broken images, console errors, truncation. Each is a lead, not a verdict: confirm it on the tiles.
3. Look at every desktop tile in order, then every mobile-light tile, then the mobile-dark tiles. Check, in this order: the title and opening screen; whether the main answer and the argument are clear; the structure and flow of sections; equations, code, tables, diagrams, images and captions (legible, not clipped, correct in dark mode, captions that say what to notice); references and internal links; related content and navigation; missing content, rendering defects, inconsistencies.
4. Read the text itself where the tiles are not enough to judge the argument (the built page or the source), but report locations as the reader sees them (section heading, figure number, paragraph).
5. Ask the value questions (standards 2.4, strategy 9): what will the intended reader learn or be able to do; is it delivered; what is missing; is the page worth its reading effort; does each major section serve the central question; is anything repeated; would a table, figure or procedure replace a long passage (standards 6.8); does the ending add something.

## 3. Write the report

Copy `templates/live-review-report.md` to `editorial/live-reviews/<type>/<slug>.md` and fill sections A to G. Every finding has a location, the problem, why it matters, the required action, a priority (critical: wrong or misleading, or the page is unusable; major: a reader would be held back or misled in part; minor: polish) and an acceptance condition that can be seen on the live page. "Improve clarity" is not a finding. Separate mandatory from optional changes in F.

Record each critical, major or minor finding in the queue with the same id:

```sh
eos queue finding <type/slug> add --id L1 --priority major --location "Section 3, Figure 2 (360 px)" \
  --problem "..." --why "..." --action "..." --acceptance "..."
```

## 4. Decide and record

| Decision | When | Command |
|---|---|---|
| accepted | No open critical or major finding; the contract is delivered | `eos queue review <id> accepted --by <you> --ref <report>` |
| accepted-with-follow-up | As above, with minor findings left open | `eos queue review <id> accepted-with-follow-up --by <you> --ref <report>` |
| revision-requested | Any critical or major finding | `eos queue review <id> revision-requested --by <you> --ref <report>` |
| blocked | The page must not stay as it is and cannot be fixed by revision alone | `eos queue review <id> blocked ...` and tell the user |
| retirement-recommended | The page fails the value tests and should be merged or retired | `eos queue review <id> retirement-recommended ...`; never retire or merge without San's explicit confirmation |

Who may accept (standards 3): Claude may accept a page whose `risk` is `routine`. A page whose `risk` is `high` (reporting, claims about named people or organizations, safety-relevant guidance, anything commercial) is accepted only by San. Record `--by San` only when San has approved that page in writing (quote or link the approval in `--note`); otherwise record `revision-requested` or leave it at `in-review` and ask San. The engine refuses a high-risk acceptance by anyone else and any acceptance without a risk level or with open critical or major findings.

## 5. Revision and re-review

The author revises the source through the normal stages (any content change makes the review record stale, so it is reviewed and re-recorded), the page is redeployed, and the capture workflow runs for it. Then mark each fixed finding `fixed-awaiting-re-review` while waiting, and close it only after you see its acceptance condition met on the new captures:

```sh
eos queue finding <id> closed L1 --note "checked on live captures of <commit>, mobile-light-04: table scrolls inside its frame"
```

Fill section G of the report (finding, captures checked, condition met, closed), then record the new decision. `eos queue validate` must pass before you finish.
