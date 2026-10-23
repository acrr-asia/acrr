# Adopting the editorial strategy: gap analysis and implementation order

Prepared 23 October 2026 against `master` at `d1f4e7b`. Scope: [`strategy.md`](strategy.md) (the Editorial Strategy and Operating System supplied by San) compared with what the repository already enforces: [`standards.md`](standards.md) v1.0, the `editorial-os` plugin (`plugins/editorial-os/`), the review records in `editorial/records/`, the series pipeline (`scripts/series-pipeline.mjs`, `reviews/`), the 13 October audit (`editorial/audit/`) and the CI workflows. This document proposes; it changes no content, publishes nothing and retires nothing.

## 1. Summary

About half of the strategy is already enforced, mostly the pre-publication half. ACRR has independent technical, fact-check, developmental, copy and QA stages; a rubric with critical conditions; content-hash review records that make any edit re-reviewable; a series gate; and CI that blocks publication on any failure. At the time of writing `eos status` reports 120 of 120 English items `ready`.

The gaps are concentrated in four places:

1. **Before drafting.** There is no idea-approval or research-readiness gate, no reader-value contract and no value category. Items enter the pipeline as drafts.
2. **After deployment.** The only post-publication check (`scripts/verify-live.mjs`) confirms that each page returns HTTP 200 with the expected `<h1>`. No one inspects the rendered public page, so Gates 7 to 9 (live review, structured revision, final acceptance) do not exist. Under the strategy, every one of the 120 published items is honestly in the state "Published, awaiting live review".
3. **Trust and classification visible to readers.** Readers cannot tell a tutorial from a review or an opinion; there is no author or editor information, no corrections, AI-use or sponsorship policy, and no way to report an error.
4. **Library value.** The 13 October audit measured correctness, evidence, language and publishing quality. It did not ask the strategy's questions: distinctive contribution, overlap with other ACRR pages, value density, or retain/merge/rewrite/retire.

Recommended order: governance files and the editorial queue first (no content touched, no review record invalidated), then live-review tooling, then one combined pass over the library that serves as both the strategy's audit (Section 9) and each page's first live review (Section 5), then the trust pages, and only then metadata that changes content files, behind a hash migration that keeps existing records valid. Priorities C to E (newsletter, analytics, commercial offers, legal registration) wait on San's decisions and on legal advice.

## 2. What already exists

| Strategy section | Already in the repository | Assessment |
|---|---|---|
| 1. Positioning, audience | `standards.md` 2.1-2.2, `eos.config.json` `publication.identity` / `audience` | Partly. Audience is "second-year students upwards"; the strategy names engineers, researchers, graduate students and advanced learners, and adds AI, scientific methods and a reporting stream. |
| 1. Pillars distinguishable on the site | Sections Blog, Series, Insights, Learning; seven topical categories; Insight `kind` | Partly. Pillars map to sections, but no page states its format (tutorial, review, opinion, reported, sponsored). There is no reporting content. |
| 2. Reader-value contract, value category | None | Gap. |
| 2. Reject, merge, rewrite, reclassify, retire | Audit remediation plan (revise only) | Gap for merge, reclassify and retire; no redirect mechanism (static GitHub Pages). |
| 3. Roles and independence | `standards.md` 3: nine roles, "the reviewer of a stage is never its author" | Mostly. Needs mapping to the strategy's five roles and a chief-editor role with live-site authority. Human verification (Section 13) is not required anywhere: publication is fully autonomous by San's earlier instruction. |
| 4. Gate 1 idea, Gate 2 research | None | Gap. |
| 4. Gate 3 draft, Gate 4 technical, Gate 5 editorial | `standards.md` 4 steps 5-7; agents `technical-reviewer`, `fact-checker`, `developmental-editor`, `copy-editor` | Mostly. Gate 5 lacks the explicit test "technically correct but does not contribute"; the visual review questions (Section 7) are not asked or recorded. |
| 4. Gate 6 pre-publication | `eos lint`, `eos validate-site`, build, `check:links`, `series-pipeline gate`, `qa-editor`, `eos gate` in `publication-gate.yml` and `deploy.yml` | Strong for technical checks. Missing: author field, content type, usage rights for third-party assets, disclosures, AI-use disclosure. |
| 4. Gate 7 live inspection | `verify-live.mjs` (HTTP 200 and `<h1>` match on every sitemap page) | Gap. Deployment check only; the strategy says a deployment check is not editorial approval. |
| 4. Gate 8 revision, Gate 9 acceptance and maintenance | Review-record `history`; series re-review on edit | Gap: no structured live findings, no accepted state, no maintenance trigger, no reader error reports. |
| 5. Central editorial queue | `eos status` (derived per file), review records | Partly. Records carry stage outcomes, scores, findings counts, reviewers and history, but there is no explicit workflow status, value category, chief-editor status, outstanding findings list or disclosure field, and nothing exists for an item before it is a file. |
| 5. Status model | `eos status` stages: draft, lint-errors, needs-review, needs-fixes, review-stale, ready | Gap: six derived stages against fifteen editorial states. |
| 5. Live-review report A-G | None | Gap. |
| 6. Communication principles | `standards.md` 5.7 (fact, interpretation, recommendation), 6.x structure, 7.1 source hierarchy; Insight sections Established / Interpretation / Open questions | Mostly. Missing: answer-first openings for decision-oriented pieces, explicit comparison criteria (Principle 5), specific limitations (Principle 7). |
| 7. Visual standard | Mermaid at build time, generated SVG diagrams with token colours, `Figure.astro` captions, `validate-site` alt-text and oversized-figure checks | Strong technically. Missing: recorded visual decisions, chart-integrity checklist (provenance, units, what the chart does not establish). |
| 8. Templates A-E | `standards.md` 6.2-6.4 (series entry, standalone, insight) | Partly. No comparison, research-review or reporting template. |
| 9. Library audit | `editorial/audit/` (13 October, 64 items, rubric scores) | Partly; dimensions differ (see gap 4 above). |
| 10. Priority A-E backlog | Priority A partly; B partly (tags, related posts, series pager, search) | See Section 5. |
| 11. Sponsorship | None; no sponsored content exists | Gap only when commercial work begins; policy can be written now. |
| 12. KPIs | Editorial-quality data exists in records; no analytics, no feedback | Editorial KPIs computable now; reader KPIs need data that does not exist. |
| 13. Legal (Vietnam) | None | Outside the repository; needs counsel. |
| 14. Operating review | `eos status`, series pipeline status | Partly; no review log with decisions and owners. |

## 3. Gaps, numbered for tracking

| # | Gap | Strategy | Priority |
|---|---|---|---|
| G1 | No idea proposal (Gate 1) or research log (Gate 2); no reader-value contract or value category | 2, 4 | A |
| G2 | No central queue with explicit workflow status, chief-editor status, outstanding findings, disclosures | 5 | A |
| G3 | No chief-editor live-site review of the public page; no live-review reports; no accepted state | 4 (Gates 7-9), 5 | A |
| G4 | Human verification of substantive claims and separate review of high-risk articles are not required; the chief-editor role is unassigned | 3, 13 | A (decision) |
| G5 | No visible content classification (tutorial, explainer, comparison, research review, reporting, analysis, reference, sponsored) | 1, 10A | A |
| G6 | No author, editor or publisher information; no corrections, AI-use or sponsorship policy page; no reader error-reporting channel | 4 (Gate 9), 10A | A (needs San's information) |
| G7 | Library never assessed for distinctive contribution, overlap, value density or retain/merge/retire | 9 | A |
| G8 | No merge or retire mechanism (redirect stubs, link-checker support, preserved content) | 2 | A |
| G9 | Editorial review does not record the visual questions or the "correct but adds nothing" test; no chart-integrity checklist | 4 (Gate 5), 7 | B |
| G10 | Templates for comparison, research review and reporting are missing; answer-first rule absent | 6, 8 | B |
| G11 | `updatedAt` not set on revised items; changing it would make every record stale (open item since 15 October) | 4 (Gate 9) | B |
| G12 | Vietnamese originals (`originalLang: "vi"`, the Machine Learning from the Ground Up series) are excluded from EOS review | 3, 4 | A |
| G13 | No usage-rights record for third-party figures, code or data | 4 (Gate 6), 13 | B |
| G14 | No maintenance trigger (standards or software versions changing) | 4 (Gate 9) | B |
| G15 | No reporting stream content, type or template | 1 | B (no content yet) |
| G16 | No newsletter, feedback mechanism or analytics; reader KPIs have no data | 10C, 12 | C |
| G17 | No media kit, offers, terms or conflict-of-interest register | 10D, 11 | D |
| G18 | No legal classification, data-protection, advertising or copyright review | 13 | Before any new activity |

## 4. Constraints that shape the order

- **Review records are hash-locked.** Any change to a content file (front matter included) makes its record `review-stale` and fails CI until it is reviewed again. A front-matter field added to all items at once would stale all 120 records. Therefore: everything editorial that can live outside content files does (queue, contracts, live reviews), and the one change that must touch front matter (visible classification, `updatedAt`) waits for a hash migration that keeps unchanged reviews valid.
- **Other work in flight.** The Bayesian Deep Learning series is being written on `series/bdl-part-N` branches by a separate session, and the Vietnamese Machine Learning series by another thread. Neither branch touches `editorial/standards.md`, `editorial/eos.config.json` or the plugin today (checked against `series/bdl-part-3` and `series/bdl-part-4`). Each phase below must keep the gate accepting their existing records, so their pull requests do not fail because of this work.
- **Live access.** This container cannot reach https://acrr.asia. GitHub Actions can (the `verify` job of `deploy.yml` fetches every page). Live screenshots must therefore be taken in a workflow, or on San's device, not here.
- **Content integrity.** No author biography, contact detail, audience figure or legal status may be written without San supplying it. Reader-value contracts for existing items are reconstructed from the text and labelled as reconstructed, never presented as the author's original intent.
- **No retirement without San.** Retire and merge are recommendations until San confirms each one.

## 5. Implementation order

Each phase is one pull request (Phase 4 may be several), leaves CI green, and lists its acceptance condition.

### Phase 0. Adopt the strategy (this pull request)

Adds `editorial/strategy.md` (San's text, with a status line) and this plan. No content, engine or workflow change.

*Accept when:* San agrees with the reading and the order, and answers the decisions in Section 6.

### Phase 1. Governance and the editorial queue (no content files touched)

*Status: implemented 23 October 2026 (standards v2.0, editorial-os 1.1.0, 120 queue entries). Not yet done: the gate runs the queue rules as warnings (`queue.enforce: "warn"`) until the open series branches carry queue entries; Vietnamese originals (G12) are still outside the engine.*

- `standards.md` v2.0: incorporate the strategy as policy. Map roles (Author; Technical reviewer = Subject-Matter Editor plus Fact-Checker; Managing editor = Managing, Developmental and Copy Editors; Chief editor = Editorial Director plus QA final acceptance plus live review; Publisher = San). Replace the twelve steps with the nine gates, keeping the existing stages inside Gates 3-6. Add the value-before-volume tests, the value categories, the answer-first and comparison principles, the visual questions and chart integrity, and templates A-E. Update audience and identity in `standards.md` and `eos.config.json` (neither is part of any content hash).
- Editorial queue: one file per item, `editorial/queue/<type>/<slug>.json` (per-item files so parallel threads do not conflict), with a JSON schema in the plugin. Fields follow strategy Section 5: id, URL, source, author and reviewers, format, value category, reader-value contract, workflow status (the fifteen states), technical, editorial and chief-editor status, outstanding findings, disclosures, history. Proposals (Gate 1) are queue entries with no source file yet.
- Seed the queue for the 120 English items and the Vietnamese originals: status `published-awaiting-live-review`, technical and editorial status taken from the existing record, chief-editor status `none`, contract empty.
- Templates in `plugins/editorial-os/templates/`: idea proposal, research log, live-review report (sections A-G), and article templates A-E.
- `eos queue` (list, validate, transition) and `eos status` reporting both the derived stage and the queue status. The gate gains one rule for **new** items only: an item first published after the adoption date needs an approved contract in its queue entry. Existing items are not affected, so no current pull request breaks.

*Accept when:* every published item has a valid queue entry; `eos queue validate` and the existing gate pass on `master` and on the open series branches.

### Phase 2. Live-review tooling

*Status: tooling implemented 23 October 2026 (`scripts/live-capture.mjs`, `.github/workflows/live-review.yml`, skill `live-review`, `eos queue review` and `eos queue finding`). Captures go to the `live-captures` branch instead of a workflow artifact, because artifact downloads are blocked from the working container while `git fetch` is not. Acceptance condition met 23 October 2026: `/blog/dft-and-fft` went through live review (revision requested for a major finding), revision, redeployment and re-review on new captures, and was accepted with follow-up (`editorial/live-reviews/article/dft-and-fft.md`).*

- A `live-review` workflow (manual dispatch, and after each deploy for changed pages) that opens the public URL in Chromium, captures desktop and 360-pixel screenshots in light and dark mode, and records rendering facts (KaTeX errors, clipped or oversized figures, horizontal scroll, broken images, contents bar behaviour). Screenshots are uploaded as a workflow artifact; facts go to the job summary.
- A chief-editor procedure (skill and agent) that reads the screenshots, the page and the queue entry, and writes `editorial/live-reviews/<type>/<slug>.md` in the A-G format, with each finding's location, problem, why it matters, required action, priority and acceptance condition, and updates the queue. Re-review closes a finding only against a new capture of the updated URL.
- `deploy.yml` keeps `verify-live.mjs` as the deployment check; its summary states that it is not editorial acceptance.

*Accept when:* one item goes through publish, live review, revision, republish and re-review, and its queue history shows every step with the public URL.

### Phase 3. Library audit combined with first live review

One reading of each published page answers both strategy Section 9 (audit dimensions, value-density test, remediation decision with rationale and owner) and Section 5 (live-review report), so the library is read once, not twice. Order: P1 items from the 13 October audit and series foundations first, then items with the most overlap risk, then the rest. Output per item: a live-review report, a reconstructed contract (labelled as such), a value category, a format, and one of retain, retain and update, rewrite, merge, reclassify, retire. A site-level overlap map lists articles that explain the same concept in different series.

Recommendations only: no content is edited, merged or retired in this phase.

*Accept when:* every item has a report and a decision, and San has confirmed or rejected each merge, reclassify and retire.

### Phase 4. Remediation, in risk order

Critical technical errors and misleading claims first, then rewrites, then merges and retirements San confirmed (with a redirect stub page per retired URL, link-checker support for stubs, and the useful content moved first), then minor follow-ups. Each change goes through the existing review stages, a new record and, for series, a new stamp, followed by the Phase 2 live re-review.

*Accept when:* no critical or major live finding is open, and every retired URL resolves to its replacement.

### Phase 5. Trust pages (needs San's information)

Editorial policy (the gates in reader language), corrections policy with the reporting channel San chooses, AI-use disclosure that describes the actual process truthfully, sponsorship and independence policy (stating that no sponsored content exists, if that is true), and author, editor and publisher information San supplies. Both languages. These are static pages, not hash-locked.

*Accept when:* a reader can find who publishes ACRR, how it is reviewed, how AI is used, how to report an error and how corrections are shown.

### Phase 6. Metadata migration and visible classification

- Hash v2 in `eos`: the content hash ignores a configured list of metadata-only front-matter fields (`updatedAt`, `format`, `valueCategory`). `eos rehash` rewrites a record's hash only when its v1 hash still matches the file, so a review stays valid only for unchanged text. The gate accepts both forms during the transition, so open series branches keep passing.
- Add `format` (and optionally `valueCategory`) to the content schema and front matter, filled from Phase 3; show a format label on cards and article headers in both languages; backfill `updatedAt` where a substantive revision is recorded.
- Record schema v2 with an eighth rubric dimension, reader value, required only for records written after this phase.

*Accept when:* every page shows its format; adding the fields leaves `eos gate` green with no re-review of unchanged text.

### Phase 7. Discovery and reporting (Priority B)

Internal links between related concepts from the Phase 3 overlap map; series ordering and completeness review; navigation across formats; a maintenance register (items that depend on a standard or software version, with what to watch). The reporting stream (template D, right-of-reply and quotation rules, source records) is set up when the first reported piece is proposed, not before, so the site never shows an empty section.

### Phase 8. Audience, commercial and legal (Priorities C to E)

Newsletter, feedback mechanism and analytics only after the personal-data review in strategy Section 13; KPIs computed from real data with baselines before targets; media kit with real figures only; commercial terms and a conflict-of-interest register when San has offers to scope. These are San's decisions and need counsel; the repository can hold the checklists and registers.

Editorial-quality KPIs (strategy Section 12, first list) become computable at the end of Phase 1 from the queue and records, and can be reported by `eos status`.

## 6. Decisions needed from San

1. **Who is the chief editor, and where is a human required?** The strategy requires human verification of substantive claims and a separate review of high-risk articles; the current pipeline publishes autonomously with independent AI agents. Options: Claude performs live reviews and San spot-checks; San approves every live review; or Claude for routine pages and San for high-risk ones (reporting, claims about named people or organisations, safety-relevant guidance, anything commercial). **Decided 23 October 2026: the third.** Claude accepts routine technical pages after live review; San approves the high-risk categories listed here. Phase 1 writes this into `standards.md` and the queue (a `riskLevel` field and a `chiefEditor` sign-off naming who accepted the page).
2. **Reader error reports.** Which channel may the site show: GitHub issues on the repository, an email address, or a form? None exists, and none can be invented.
3. **Author and publisher information.** What may be published about who writes, edits and publishes ACRR?
4. **AI-use disclosure wording.** The truthful description is that articles are drafted and reviewed with AI agents under the standards; San decides the wording and whether a human-verification statement can be made.
5. **Commercial status.** Whether any sponsorship or partnership exists or is planned, so the sponsorship policy states the truth.

## 7. Not verified

- The Vietnamese legal instruments named in strategy Section 13 (Press Law No. 126/2025/QH15, Decrees No. 237/2026/ND-CP and No. 147/2024/ND-CP, Law No. 75/2025/QH15, Law No. 91/2025/QH15) were not checked in this analysis; they need confirmation by counsel.
- The 120-item count and readiness come from `eos status` on `master` at `d1f4e7b`; the open BDL branches add items not counted here.
