# Live review: Feedback and System Behavior

- URL: https://acrr.asia/blog/feedback-and-system-behavior
- Source: `src/content/blog/feedback-and-system-behavior.mdx` (Foundations of Control Systems, entry 2)
- Commit deployed: `1eb85d4`
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/39980397404 (2026-10-23 15:43 UTC): 12 desktop-light, 21 mobile-light, 21 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-23. The reviewer did not write or revise this article.
- Risk: routine (a technical explainer; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Accept with minor follow-up. The page delivers what it sets out to do, every number on it was reproduced in this review, and no finding is critical or major. Four minor presentation findings remain open (L1 to L4); all but L3 come from site-wide styling rather than from the article text.

**Library decision: retain.** The entry is the series' account of what proportional feedback does, and four articles outside the series (From Signal Processing to Digital Control, PID Control of Process Variables, Logic and Sequential Control, and Following a Plan: Path Tracking and Reactive Obstacle Avoidance) link to it for exactly that, as do four entries of its own series. The wave 1 revision of 13 October added what the audit found missing (the stabilization example, the single factor $1/(1 + L_0)$, quantified limits, Summary and References), and this review found no technical error. Its content does not need to change; a rewrite, merge or reclassification would gain nothing.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineering student or engineer who has met transfer functions and poles (the first entry) and wants to see concretely what closing a loop changes.
- Problem: knowing what proportional feedback actually buys and what it costs, rather than assuming that feedback simply "makes the output correct".
- Outcome: compute the closed-loop pole, time constant and steady-state offset of a first-order loop; show that feedback can stabilize an unstable plant and state the minimum gain; explain why feedback reduces sensitivity to plant errors and disturbances by $1/(1 + L_0)$; name what limits the gain in practice.
- Distinctive contribution: the smallest model that shows every effect, with one factor ($1/(1 + L_0)$) tying offset, disturbance rejection and sensitivity together, checked by a short standard-library simulation, and an explicit warning that on the nominal plant feedback does not improve accuracy.
- Evidence: algebra in the text; two Python scripts whose output is quoted; Åström and Murray (2021); Franklin, Powell and Emami-Naeini (2019); the sampled-loop limit from the series' digital-control entry.
- Limitations: first-order, continuous-time, proportional only; delay, saturation and noise are named and quantified but not modeled; integral action is deferred.

The benefit is delivered. The opening states the answer in advance (faster, can stabilize, less sensitive, not more accurate on the nominal plant) and the sections prove it in order. Spot checks recomputed in this review: both scripts re-run (0.8; nominal 1.000/0.800, $a = 1.2$ 0.833/0.769, $d = 0.2$ 1.200/0.840); relative shifts −16.7% and −3.85% against the derivative's −20% and −4%; the stabilization case ($k > 1$, pole −3, $x_{ss} = 4r/3$); the closed-loop relative sensitivity $-a/(a + bk)$ (derived again); the sampled-loop limit $\coth(0.05) = 20.02$.

Value density: no section is padding. Section 4.2 is the most valuable paragraph on the page, because it turns three isolated numbers into one result; the Summary table restates the page usefully as a review sheet. Overlap with other ACRR articles is by design and handled with links: From Signal Processing to Digital Control (Section 2.2) repeats the same plant in discrete time and cites this entry for the offset; PID Control of Process Variables starts where this entry ends. Value category: conceptual understanding. Format: explainer.

## C. Substantive findings

None. The argument, the numbers and the references hold.

## D. Visual and structural findings

### L1. Display equations cut at 360 px

- Location: Section 1.1 (the plant equation), Section 2.3 (the pair $x_{ss}$, $r - x_{ss}$) and Section 2.4 (the stability condition); mobile-light-03, 06 and 08 (and the same tiles in dark mode).
- Problem: at 360 px each display is wider than the column and its right end is hidden behind an unmarked sideways scroll: "$b > 0$" in 1.1, most of the error formula in 2.3, and "$/b = 1$" in 2.4, so the phone reader sees "$k > -a$" as the result.
- Why it matters: small, because the text restates each result nearby and the Summary repeats them, but the 2.4 condition is the conclusion of the subsection.
- Required action: break the three displays for narrow screens (for example the two halves of the 1.1 and 2.3 displays on separate lines, and "$a + bk > 0$" and "$k > -a/b = 1$" as two lines), or a site-level scroll cue for wide equations.
- Priority: minor
- Acceptance condition: on new 360 px captures, all three displays are fully visible, or a visible cue shows that they scroll.

### L2. Both figures lose their right edge at 360 px

- Location: Section 2.1 (proportional loop diagram) and Section 2.3 (step responses); mobile-light-04 and 07.
- Problem: generated diagrams keep a minimum width of 26rem (416 px, `prose.css`), wider than the 328 px column, so the right fifth of each figure is hidden without a cue. In the loop diagram the output $x$ disappears; in the step-response plot the curve labels ("open loop", "$k = 9$", "$k = 4$", "$k = 1$") and the axis label are hidden, and the caption does not say which line style is which, so a phone reader cannot tell the curves apart.
- Why it matters: the step-response plot is the visual proof of the speed-versus-offset trade-off; without labels it is four unnamed curves.
- Required action: a site-level scroll cue for wide figures (the same follow-up as L2 of the DFT and FFT review), and for this plot either labels placed inside the plotting area or a caption that names the line styles (solid $k = 9$, dashed $k = 4$, dotted $k = 1$, thin dashed open loop).
- Priority: minor
- Acceptance condition: at 360 px the curve labels are visible or the caption identifies each line style, and the loop diagram's output is visible or visibly scrollable.

### L3. Step-response plot: time axis without unit

- Location: Section 2.3, the step-response figure; desktop-light-04 and 05.
- Problem: the horizontal axis is labeled "time $t$" with no unit, although the opening states that time is in seconds and the table gives time constants in seconds (standards 6.8, chart integrity: axis labels with units).
- Why it matters: minor; the reader can infer seconds, but the plot is the one place where the reader compares time constants by eye.
- Required action: label the axis "time $t$ (s)" in `scripts/generate-diagrams.py` and regenerate the component.
- Priority: minor
- Acceptance condition: the axis reads "time t (s)" on the live page.

### L4. Punctuation separated from inline math at line ends

- Location: Section 4.1, "**A constant disturbance**" paragraph (desktop-light-06: the line begins ". In open loop"); Section 5, measurement noise item (mobile-light-16: a lone "." after "multiplied by $k$").
- Problem: the browser breaks the line between an inline equation and the full stop that follows it, so a line starts with a period.
- Why it matters: polish; it looks like an error and interrupts reading. The cause is site-wide (KaTeX output followed by punctuation), not this article.
- Required action: site-level: keep trailing punctuation with the preceding equation (for example a no-break wrapper added by the rehype step, or `white-space: nowrap` on equation-plus-punctuation).
- Priority: minor
- Acceptance condition: no line on the page begins with a period or comma at 1280 or 360 px.

Dark mode: both figures, the three tables and both code blocks render correctly (mobile-dark-04 to 12, 17). The page already uses the right representations: a block diagram for the loop, a response plot, comparison tables, a worked simulation and a summary table. No further visual is needed.

## E. Technical and source findings

No technical or source errors found. `facts.json`: HTTP 200 on all three viewports, no horizontal page scroll, no element wider than the screen, 0 KaTeX errors, 0 broken images, 0 console errors; both SVG figures have titles. Both references are standard textbooks, correctly cited.

## F. Required changes

Mandatory:

- None.

Optional:

- [ ] L1: break the three wide displays for narrow screens (or site-level scroll cue).
- [ ] L2: site-level scroll cue for wide figures; name the line styles in the step-response caption.
- [ ] L3: unit on the time axis.
- [ ] L4: keep trailing punctuation with inline equations (site level).
- [ ] First table, first column: at 1280 px "Open loop, $u = r$" and "Feedback, $k = 1$" wrap inside the equation ("$u =$" / "$r$"); a wider first column or `white-space: nowrap` on inline math in table cells would avoid it. The pole column uses a hyphen ("-1") where the text uses a minus sign.
- [ ] Series level (not this page): the series is dated out of order. This entry shows 20 September 2026, the first entry 11 October and the third 27 September, so the related-articles block shows "Introduction to Control Systems, 11 Oct 2026" under an entry that builds on it. If `publishedAt` is right, nothing to do; if the first entry was republished under a new date, its `publishedAt` should be corrected.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
| L3 | | | |
| L4 | | | |
