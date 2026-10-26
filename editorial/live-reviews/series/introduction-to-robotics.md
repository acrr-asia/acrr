# Live review: Introduction to Robotics (series overview)

- URL: https://acrr.asia/series/introduction-to-robotics
- Source: `src/content/series/introduction-to-robotics.md` (four entries, status published, no planned entries)
- Commit deployed: `7e20c2c`
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40087219510 (2026-10-24 10:51 UTC): 3 desktop-light, 6 mobile-light, 6 mobile-dark tiles (the page has no figure, table, code or equation, so the dark tiles were not inspected individually)
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-24. The reviewer did not write or revise this page.
- Risk: routine (a series front door for technical explainers; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Accept with minor follow-up. The overview meets standards 6.5, and every statement on it was checked against the four entries. Two minor findings: serial commas in two learning objectives (L1), and no pointer to the Motion Planning for Robots series, which continues this one (L2).

**Library decision: retain.** The page is the series' entry point and does its job: prerequisites, the sequence rationale with what each entry contributes, the shared conventions and five checkable objectives. The 13 October audit's findings (no sequence rationale, no conventions, serial comma in the description) were fixed in wave 1 and are visible; its optional finding on serial commas in the objectives was left open then and is recorded here as L1. Nothing should be merged or reclassified.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: a student or engineer comfortable with basic linear algebra, trigonometry and calculus, who has met torque and inertia, deciding whether and where to start robotics on ACRR.
- Problem: knowing what the four entries cover, why in this order, what is assumed and which conventions they share.
- Outcome: the reader knows the path from the whole machine to frames, kinematics and estimation, that probability is introduced only in entry 4, that feedback comes from the control series but is not required, and the units and frame conventions; five objectives say what they will be able to do.
- Distinctive contribution: an order stated as "the order in which each idea becomes necessary", with each entry's dependency on the previous one spelled out (entry 4 begins where entries 2 and 3 assumed known poses).
- Evidence: the entries. Checked in this review: entry 1 fixes degrees of freedom, redundancy and proprioceptive/exteroceptive sensing and has a "Sense–plan–act" section (5.1), which covers objective 4; entry 2 covers rotation matrices, Euler angles, quaternions, homogeneous transforms and the frame tree; entry 3 covers forward kinematics, closed-form and numerical IK, the Jacobian and singularities; entry 4 introduces probability in its Section 2 and works a Kalman filter by hand; all four state SI units, right-handed frames, column vectors and radians in computation; their worked examples are hand-checkable (recomputed in the entry reviews of the same date).
- Limitations: an overview; total reading time (about 63 minutes from the card estimates) is not stated.

The benefit is delivered. The opening screen gives the title, a one-sentence description, the category, the Published status and "Start with entry 1"; the body adds what the entry list cannot (the dependency chain and conventions); the entry cards' descriptions are complete "Learn ..." sentences. The objectives begin with assessable verbs (describe, represent, explain, outline, explain) and promise nothing the entries do not deliver. Value category: reference value. Format: reference.

Overlap: the entries' reviews of the same date map the overlap with other series (Sensing and State Estimation with Calibration and Multisensor Fusion; Forward and Inverse Kinematics of a Planar Arm with the Motion Planning for Robots series); all of it is handled by links, not repetition.

## C. Substantive findings

None.

## D. Visual and structural findings

### L1. Serial commas in two learning objectives

- Location: Learning objectives, items 1 ("mechanical structure, actuators, sensors, and computation") and 4 ("the sense, plan, and act structure"); desktop-light-02, mobile-light-03 and 04.
- Problem: both use the serial comma; standards 5.6 (no serial comma) applies to all visitor-facing English text. The body and description on the same page follow the house style, so the two styles appear side by side.
- Why it matters: small, but visible on a series front door; the 13 October audit left it only because the Vietnamese file mirrors the objectives, which is a translation update, not a reason to keep the error.
- Required action: remove the two serial commas (item 4 may read better as "the sense–plan–act structure", matching entry 1's heading) and update the Vietnamese objectives in the same commit if their wording changes.
- Priority: minor
- Acceptance condition: neither objective shows a serial comma on the live page.

### L2. No pointer to the series that continues this one

- Location: end of the body text, before the entry list (desktop-light-02, mobile-light-03).
- Problem: the Motion Planning for Robots series states that it continues this series, and the last entry here names motion planning as a topic that builds on it, but the overview does not mention or link it.
- Why it matters: a reader who finishes the series, or who wants to know where it leads before starting, has no route from the front door to the next series.
- Required action: one sentence after the conventions paragraph, for example "The [Motion Planning for Robots](/series/motion-planning) series continues from here, using the two-link arm and the frames of entries 2 and 3."
- Priority: minor
- Acceptance condition: the live overview links the Motion Planning for Robots series.

Layout is correct at both widths: on desktop the objectives and progress sit beside the entry list; at 360 px they stack above it (mobile-light-04). The progress bar reads "4 of 4 entries published".

## E. Technical and source findings

None. `facts.json`: HTTP 200 on all three viewports, no horizontal page scroll, no overflowing elements, 0 KaTeX errors, 0 broken images, 0 console errors.

## F. Required changes

Mandatory: none.

Optional:

- [ ] L1: remove the serial commas in objectives 1 and 4 (and mirror in the Vietnamese file).
- [ ] L2: link the Motion Planning for Robots series.
- [ ] State the total reading time (about an hour) in the body.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
