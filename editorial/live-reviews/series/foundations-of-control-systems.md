# Live review: Foundations of Control Systems (series overview)

- URL: https://acrr.asia/series/foundations-of-control-systems
- Source: `src/content/series/foundations-of-control-systems.md` (series overview, 5 entries, status published)
- Commit deployed: `7e20c2c` (master after PR #57); the source is unchanged since the wave 2 resolution of 13 October (`60c0823`)
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40085671258 (2026-10-24 10:26 UTC): 3 desktop-light, 6 mobile-light, 6 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-24. The reviewer did not write or revise this page.
- Risk: routine (a series overview; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Request revision, for one major finding that is not in the overview's own text: the entry cards show publication dates for entries 1 to 3 (11 October, 20 September, 27 September 2026) that are not their first publication dates (L1). The overview's own text, objectives and layout are correct and need no change.

**Library decision: retain.** The overview is the series' front door and does its job: who the series is for, what it assumes, why input-output comes before state space, how the five entries build on each other, the shared conventions, four objectives and a "Start with entry 1" button. The 13 October audit's findings (no sequence rationale, incomplete prerequisites, missing conventions, an untrue "each entry introduces one idea") are resolved on the live page. Nothing to merge, reclassify or retire.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: someone with calculus, basic linear algebra and some Python, deciding whether and where to start learning feedback control.
- Problem: what the series covers, in what order, what it assumes, and what the reader will be able to do at the end.
- Outcome: choose a starting point; know the prerequisites (and that the Laplace transform and matrix exponential are introduced in the entries); know the four objectives and the shared conventions.
- Distinctive contribution: one paragraph that states the line of argument through the five entries (loop vocabulary and measures; proportional feedback on a first-order plant; state-space models; eigenvalues and their limits; state feedback and its assumptions) and why the input-output view comes first.
- Evidence: none needed beyond the entries; each claim about an entry was checked against its source.
- Limitations: an orientation page; it teaches nothing itself.

The benefit is delivered. Checks made against the entries: entry 1 sets out the loop, requirements, transfer function and step-response measures and defines the 2% criterion (its Section 4.1); entry 2 shows speed, stability and sensitivity at the price of an offset; entry 3 introduces state-space models and the transfer function; entry 4 (reviewed in this batch) ends with where the eigenvalue test stops being enough; entry 5 (reviewed in this batch) examines model, actuator and measurement assumptions in its Section 6; entries 1 and 2 use only the standard library and NumPy first appears in entry 3; the four objectives are each met by an entry, as entry 5's closing paragraph also maps out. About 270 words of body; nothing repeated beyond what the entry cards necessarily restate. Value category: reference value (orientation). Format: reference.

Overlap noticed: none for the overview. The [Industrial Automation](/series/industrial-automation) overview names this series as a prerequisite for its PID entry; this overview does not mention where its ideas are applied (PID control in process plants, digital control in the DSP series). An optional "where next" sentence would serve readers who finish the series (F).

## C. Substantive findings

### L1. Entry dates for entries 1 to 3 are not first publication dates

- Location: the Entries list (desktop-light-02, mobile-light-04): entry 1 "11 Oct 2026", entry 2 "20 Sept 2026", entry 3 "27 Sept 2026"; the dates come from `publishedAt` in `src/content/blog/introduction-to-control-systems.mdx`, `feedback-and-system-behavior.mdx` and `state-space-models-primer.mdx`.
- Problem: standards Section 8 (Policy D) defines `publishedAt` as the first publication date. The repository's first commit is dated 11 October 2026, so the two September dates precede the repository itself; all three files were added on 12 October (commit `09a35ae`) as labelled example content (`example: true`) and published as real on 12 October (commit `483fb23`, which also added the deployment workflow), keeping the dates they had as samples. No record of an earlier publication was found. On the overview the result also reads as if the series began in September with entry 2 and entry 1 came last.
- Why it matters: a publication date is a factual claim to the reader; here it overstates how long the series (and the site) have existed and misorders the entries' history.
- Required action: San to confirm the correct first publication date (the repository evidence points to 12 October 2026, when the pages were first published as original content). Then set `publishedAt` in the three English files and their Vietnamese translations (`src/content/blog/vi/`, same field, which `pairTranslations` requires to match) and keep `updatedAt: 2026-10-13`. This edits pages already accepted in batch 1, so their review records become stale and need re-recording. The same pre-launch sample dates are carried by `numerical-integration-notes` (4 October) and six insights dated 5 to 11 October; they should be checked in the same pass (site-level, not recorded here).
- Priority: major
- Acceptance condition: on new captures the cards of entries 1 to 3 show the confirmed first publication dates, and no entry shows a date earlier than its first publication.

## D. Visual and structural findings

None. At 1280 px the text and entries timeline sit beside the objectives and progress sidebar; at 360 px the sidebar moves above the entries, which reads well. Dark mode is correct (button, badge, timeline and progress bar in the dark tokens, mobile-dark-04). `facts.json`: HTTP 200 on all three viewports, no horizontal scroll at 360 px, no overflowing elements, no console errors.

## E. Technical and source findings

None. The overview makes no technical claim that is not delivered by an entry (checked as listed in B).

## F. Required changes

Mandatory:

- [ ] L1: correct the first publication dates of entries 1 to 3 (after San confirms them), in English and Vietnamese.

Optional:

- [ ] A closing sentence pointing to where the series' ideas are applied: [PID Control of Process Variables](/blog/pid-control-of-process-variables) and [From Signal Processing to Digital Control](/blog/from-signal-processing-to-digital-control).

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
