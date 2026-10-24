# Phase 3, batch 2: control, signal processing and sensors

Library audit combined with the first live review (adoption plan, Phase 3). Recommendations only: no page was edited, merged or retired.

- Pages: the rest of Foundations of Control Systems, Digital Signal Processing and Sensor Systems (14 pages), plus the re-review of two batch 1 findings after the code-ligature fix (PR #57).
- Captures: https://acrr.asia at `7e20c2c`, run https://github.com/acrr-asia/acrr/actions/runs/40085671258 (2026-10-24 10:26 UTC); phone dark-mode tiles read only where they hold a figure, table, code or equation.
- Reviewers: three independent live-review passes. Every script was re-run and every worked number recomputed; no technical error was found on any page.

## Decisions

| Page | Live-review decision | Library decision | Critical / major / minor |
|---|---|---|---|
| article/pid-control-of-process-variables | revision requested | retain | 0 / 1 / 4 |
| article/stability-and-eigenvalues | revision requested | retain | 0 / 1 / 1 |
| article/state-feedback-controller-design | revision requested | retain | 0 / 1 / 2 |
| article/from-signal-processing-to-digital-control | accepted with follow-up | retain | 0 / 0 / 3 |
| series/foundations-of-control-systems | revision requested | retain | 0 / 1 / 0 |
| article/designing-fir-and-iir-filters | revision requested | retain and update | 0 / 1 / 1 |
| article/z-transform-poles-and-stability | accepted with follow-up | retain and update | 0 / 0 / 3 |
| series/digital-signal-processing | accepted | retain | 0 / 0 / 0 |
| article/sampling-quantization-and-data-conversion | accepted with follow-up | retain | 0 / 0 / 3 |
| article/signal-conditioning | accepted with follow-up | retain | 0 / 0 / 2 |
| article/noise-interference-and-limits-of-detection | accepted with follow-up | retain | 0 / 0 / 3 |
| article/sensing-principles | accepted with follow-up | retain | 0 / 0 / 1 |
| article/smart-sensors-and-mems | accepted with follow-up | retain | 0 / 0 / 2 |
| article/calibration-and-multisensor-fusion | accepted with follow-up | retain | 0 / 0 / 3 |

All routine risk. No merge, reclassification or retirement is recommended.

Re-review of batch 1 (captures above): the code-ligature findings are closed (inside-a-microcontroller L1, signals-and-systems-in-discrete-time L4); inside-a-microcontroller is now accepted with follow-up.

## The five major findings

- **Cut equations that hide a result, at 1280 px as well as on phones:** pid-control-of-process-variables (the velocity form ends at "u_k ="), state-feedback-controller-design (the closed-loop characteristic polynomial ends at "s² −"), designing-fir-and-iir-filters (the A(ω) definition in 2.2, and Kaiser's order formula in 3.4, of which only "M" is visible, although the worked value and Exercise 1 depend on it). stability-and-eigenvalues fits at 1280 px but loses equations that two exercises use at 360 px. The fix is the one used in dft-and-fft: break each equation over lines.
- **series/foundations-of-control-systems: publication dates.** The entry cards show 11 October, 20 September and 27 September 2026. The repository's first commit is 11 October; the three articles were added on 12 October as example content and published as real in `483fb23` (12 October) with their sample dates kept. Standards define `publishedAt` as the first publication date. Correcting it needs San's confirmation of the real date (the repository points to 12 October), and touches three articles and their Vietnamese translations (copied field), whose review records then go stale. The same pre-launch sample dates are on numerical-integration-notes (4 October) and six insights (5 to 11 October); not recorded as findings yet.

## Content points (minor)

- pid-control-of-process-variables: Section 4.4 points to 5.3 for the windup demonstration, which is in 5.4.
- noise-interference-and-limits-of-detection: "nearly five bits of resolution gained" has no stated reference; on the page's own effective-resolution definition the gain is about 3 bits.
- calibration-and-multisensor-fusion: a quotation opens with a closing mark; the 7-column data table hides the 10 kg point even at 1280 px.
- z-transform-poles-and-stability and designing-fir-and-iir-filters have no plot (no pole-zero plot, no response plot); sensing-principles and signal-conditioning describe circuits only in words. These are the "retain and update" cases.
- Missing links between pages that teach the same thing: PID and digital control (windup, derivative filter, hold delay), state feedback back to digital control, smart sensors to the serial-buses article.

## Overlap noticed (complementary, linked, no merge)

- Aliasing: sampling-quantization-and-data-conversion and DSP entry 1.
- Unit-circle stability: z-transform-poles-and-stability 4.3 and stability-and-eigenvalues 7 (only through Related articles; an in-text link is optional).
- Butterworth filters: designing-fir-and-iir-filters 4.1 and signal-conditioning 6.2.
- Windup, derivative filtering, hold delay: pid-control-of-process-variables and from-signal-processing-to-digital-control (no links either way).
- Complementary filter, inverse-variance weighting, Kalman update: calibration-and-multisensor-fusion (deeper) and sensing-and-state-estimation (robotics entry 4).
- Noise bandwidth: noise-interference ENBW table and the dft-and-fft window table.

## Capture tooling

- The rendering check missed inline equations wider than the screen (noise-interference showed a 364 px page with an empty overflow list: one inline square root). `scripts/live-capture.mjs` now also measures inline KaTeX.
- On the tallest page (calibration, 64 phone tiles) many tiles showed body text in a fallback font, which a local capture of the same commit does not; to watch on the next run.
