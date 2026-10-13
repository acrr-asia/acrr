# Series review: Sensor Systems

- Series: `sensor-systems` (7 articles, status published, 0 planned entries)
- Reviewed commit: 6c525b1
- Date: 2026-10-13
- Content hash: sha256:d214e5d863d0866055d0238f76455c62ae06192919ece9aad9392ae54fce0343

## Summary

The series is technically strong. It follows the measurement chain in a sensible order (measurement and characteristics, sensing principles, conditioning, conversion, noise, smart sensors, calibration and fusion), each entry builds explicitly on the earlier ones, and the load-cell channel works well as a running example across entries 3 to 7. Every worked number in the seven entries was recomputed, and all four Python listings of entry 7 were run with Python 3.13 and NumPy 2.5. Every printed output matches exactly. The build, the type check and the link check pass.

There are two blocking problems:
- Entry 7 presents its load-cell calibration data as if they were measured, without saying that they were made up for the example, and then treats their agreement with the noise budget as a "useful check". It also compares one-second averages with a figure for a 0.1–10 Hz band.
- Entry 4 says that a rounding SAR converter *adds* half an LSB to its DAC voltages. It must subtract it.

The should-fix items are as follows:
- Entry 1 has two imprecise definitions: the active/passive naming, which is the opposite of Fraden's, and threshold confused with dead band. It also has one inaccurate cross-reference.
- Three links name a series but point to an article.
- Entry 4 refers to a planned series as if it existed.
- Entry 5 gives one count slightly wrong.
- Entry 7 has four problems:
  - Its tilt sign convention disagrees with a right-handed gyroscope axis.
  - It uses the Laplace variable and s-domain transfer functions, which no entry introduces and which clash with the first entry's static "transfer function".
  - It uses the chi-square distribution without saying what it is.
  - Its exercise section repeats the body of the entry, and no other entry has one.

The other author notes were checked and need no change:
- The British -ise spelling is consistent across all seven entries and the series file. The one exception, "quantization", is used the same way everywhere (F19).
- ILAC-G24:2007 / OIML D 10:2007 and ISO/TS 28037:2010 are real documents with the titles given, and the text describes what they contain correctly.
- The Student t factor of 2.78 for four degrees of freedom and the $E_n$ criterion $|E_n| \le 1$ are correct.
- The VIM paraphrases of calibration, adjustment, verification, calibration hierarchy and metrological traceability match JCGM 200:2012.
- The claim that a steady-state angle-only Kalman filter takes the complementary-filter form is correct (derivation in the verification log).
- The double use of $s$ is resolved in the text.

The series is not ready as published until F1 and F2 are corrected.

Findings: 2 blocking, 10 should fix, 7 optional (Phase 1). One further should-fix item (F20) was added during the correction phase at the request of the series editor.

## Resolution

Applied on 2026-10-13 on branch `review/sensor-systems`, at the owner's request. All blocking and should-fix findings and all optional findings except F19 were applied as recommended, with the deviations listed below.

- **F1.** The load-cell table is labelled as constructed rather than measured, and the closing sentences were replaced as recommended. The §6.3 script is now introduced as working on "three illustrative thermometer readings".
- **F2–F11 and F14–F18.** Applied with the recommended wording, with two deviations:
  - **F7, entry 6 part.** Superseded by F20.
  - **F2.** The nested parenthesis was later simplified to commas (second pass).
- **F12.** §9 (Exercises) was deleted and §10–§11 renumbered §9–§10; no link pointed to their anchors. The one new point from Exercise 1 (0.077 Ω ≈ 0.20 °C, about half the end-point figure) was added to §3.4.
- **F13.** The bullet list was condensed to one sentence, as recommended.
- **Entry 7 length.** The prose of entry 7, without code, fell from about 7 180 to about 6 860 words. The cuts (exercises and recap) outweigh the definitions added for F1, F9, F10 and F11.
- **F19.** Not applied. "Quantization" is a deliberate, consistent term-of-art exception. Changing it would alter the title of entry 4 and the series objectives.
- **F20 (editor's finding).** Entry 6 now reads "the serial buses that the [Embedded and Real-Time Systems](/series/embedded-and-real-time-systems) series covers". The Vietnamese sentence links `/vi/series/embedded-and-real-time-systems` (the page is built). No individual article of that series is linked.
- **Second pass (re-read of all seven entries after the corrections):**
  - **Should fix.** Entry 7 §3.4 said that the load-cell residuals "alternate in sign". The residuals are +5.5, −5.4, +3.8, +12.9, −43.0, +26.2, so they do not. The sentence also said that "their size matches the noise budget", which presented made-up data as agreeing with the budget. It now reads: the residuals "change sign irregularly with no visible bow, and their size is of the order the noise budget leads one to expect".
  - **Polish.** The F2 replacement sentence had nested parentheses; they were replaced by commas in both languages.
  - **Third check.** No other blocking or should-fix problem was found. The changed passages were checked again after these two fixes, with the same result.
- **Vietnamese translations:**
  - **Entry 1** (`src/content/blog/vi/measurement-systems-and-sensor-characteristics.mdx`): F3, F4, F5, F6 and F17.
  - **Entry 4** (`vi/sampling-quantization-and-data-conversion.mdx`): F2 and F7. The Vietnamese DSP sentence already used the future tense; "dự kiến" (planned) was added.
  - **Entry 5** (`vi/noise-interference-and-limits-of-detection.mdx`): F8.
  - **Entry 6** (`vi/smart-sensors-and-mems.mdx`): F16, F18 and F20.
  - **Entry 7:** has no translation.
  - **Series file:** unchanged. Neither the English nor the Vietnamese series file needed a change.
- **Re-run results:**
  - **Build.** `npm run build:local` passed with 0 errors and 0 warnings from `astro check`. Pagefind indexed 77 pages in 2 languages; the localhost warning is the expected one for `build:local`.
  - **Links.** `npm run check:links` reported "Checked 198 pages and 5523 internal references in dist. All internal links resolve."
  - **Dist checks** (English and Vietnamese pages):
    - Mermaid `min-width` at most 437 px;
    - 0 `katex-error`;
    - no glued inline text.
  - **Recomputed values.** The entry 7 listings are unchanged, so their verified outputs still hold. Every number added or changed was recomputed:
    - 13 300;
    - 0.20 °C;
    - code 10 for 2.000 V under rounding.

Line numbers in the findings refer to the reviewed commit 6c525b1, not to the corrected articles.

- **Editor's change after the review (F7, entry 4 part):** the Digital Signal Processing for Engineers series was completed and published together with this series, so the entry-4 sentence that called it "planned" would have become false. Like F20, it now links the series page without calling it planned: "The digital half is the subject of the [Digital Signal Processing for Engineers](/series/digital-signal-processing) series." The Vietnamese sentence was changed to match. No other text changed; the build and link check were re-run.

## Objectives coverage

| Objective (from the series file) | Covered by | Assessment |
|---|---|---|
| Describe a measurement system as a chain from measurand to number, and characterise a sensor by its static and dynamic properties. | Entry 1 §2–4, §7 | Met. Two definitions are imprecise (F3, F4). |
| Explain the main physical principles by which sensors convert a quantity into an electrical signal. | Entry 2 (whole) | Met. |
| Design the analog front end of a sensor: excitation, bridges, amplification and filtering. | Entry 3 (whole) | Met, including a complete worked channel. |
| Explain sampling, quantization and data conversion, and the noise that limits what can be detected. | Entry 4 (whole), entry 5 (whole) | Met. One error in the SAR example (F2). |
| State and combine measurement uncertainties, and calibrate and fuse sensors. | Entry 1 §5–6, entry 7 (whole) | Met. The calibration example breaches the content-integrity rule on examples (F1). |

## Findings

| ID | Severity | Article | Location | Dimension | Finding |
|---|---|---|---|---|---|
| F1 | Blocking | `src/content/blog/calibration-and-multisensor-fusion.mdx` | §3.2 (lines 105, 145) | Fit with site rules / Technical accuracy | Made-up calibration data presented as measured, and their agreement with the noise budget treated as evidence; the bandwidths compared also differ. |
| F2 | Blocking | `src/content/blog/sampling-quantization-and-data-conversion.mdx` | §5.1 (line 175) | Technical accuracy | A rounding SAR converter subtracts half an LSB from the DAC voltages; the text says it adds it. |
| F3 | Should fix | `src/content/blog/measurement-systems-and-sensor-characteristics.mdx` | §2.3 (lines 63–68) | Terminology | "Self-generating (or active)" and "modulating (or passive)" are given as the only naming; Fraden, cited by the series, uses the opposite. |
| F4 | Should fix | `src/content/blog/measurement-systems-and-sensor-characteristics.mdx` | §3.4 (line 109) | Technical accuracy | Threshold is equated with dead band; the VIM defines them differently. |
| F5 | Should fix | `src/content/blog/measurement-systems-and-sensor-characteristics.mdx` | §2.1 (line 51) | Cross-article references | "Each stage has its own section of this series" is inaccurate: the stages are covered by entries, and the output stage by none. |
| F6 | Should fix | entries 1 and 7 | entry 1 line 123; entry 7 lines 341, 592 | Cross-article references | The link texts "control systems series" and "robotics series" point to single articles. |
| F7 | Should fix | `src/content/blog/sampling-quantization-and-data-conversion.mdx` (also `smart-sensors-and-mems.mdx`) | entry 4 §2.1 (line 75); entry 6 §4.4 (line 149) | Cross-article references | The digital signal processing series is planned but is described as one that "treats" the topic. |
| F8 | Should fix | `src/content/blog/noise-interference-and-limits-of-detection.mdx` | §6.1 (line 188) | Technical accuracy | The noise-free resolution is about 13 300 steps, not 13 400. |
| F9 | Should fix | `src/content/blog/calibration-and-multisensor-fusion.mdx` | §7.1 (lines 345, 353) | Stated conventions | Positive θ tips x upwards, which is a negative right-hand rotation about y, so a y-axis gyroscope reads −θ̇, not θ̇. |
| F10 | Should fix | `src/content/blog/calibration-and-multisensor-fusion.mdx` | §7.2 (lines 357–367) | Concept introduction / Terminology | The Laplace variable, s-domain transfer functions and the final-value theorem are used without introduction, and "transfer function" means the static curve in entry 1. |
| F11 | Should fix | `src/content/blog/calibration-and-multisensor-fusion.mdx` | §6.3 (line 296) | Concept introduction | The chi-square distribution is used without saying what it is. |
| F12 | Should fix | `src/content/blog/calibration-and-multisensor-fusion.mdx` | §9 (lines 516–561) | Writing quality | The exercises repeat the body (Ex. 1 = §3.4, Ex. 3 ≈ §4.2, Ex. 5 ≈ §6.2), and no other entry has exercises. |
| F20 | Should fix | `src/content/blog/smart-sensors-and-mems.mdx` | §4.4 (line 149) | Cross-article references | Added by the series editor: the Embedded and Real-Time Systems series is being completed for publication, so calling it "planned" is about to become false; refer to it by name and link its series page. |
| F13 | Optional | `src/content/blog/calibration-and-multisensor-fusion.mdx` | §11 (lines 580–592) | Writing quality | The entry-by-entry recap repeats the series description and the series navigation. |
| F14 | Optional | `src/content/blog/calibration-and-multisensor-fusion.mdx` | §8.1 (line 462) | Writing quality | "A large part of the error budget of the best filter": 0.25° is more than the whole 0.14° RMS error. |
| F15 | Optional | `src/content/blog/calibration-and-multisensor-fusion.mdx` | §7.4 (line 454) | Technical accuracy | The Kalman/complementary equivalence is correct but does not state its noise assumptions. |
| F16 | Optional | `src/content/blog/smart-sensors-and-mems.mdx` | §3.1 (line 75) | Technical accuracy | The differential capacitor cancels the even-order (quadratic) nonlinearity, not "the first-order" one, and unlike the half bridge it is not exactly linear. |
| F17 | Optional | `src/content/blog/measurement-systems-and-sensor-characteristics.mdx` | §1.2 (line 32) | Technical accuracy | Uncertainty is described as an interval, whereas the VIM and the entry's own §5.2 treat it as a dispersion parameter. |
| F18 | Optional | entries 6 and 7 | entry 6 line 57; entry 7 line 20 | Writing quality | "section 4.2" and "section 5" are lower case, while every other section reference is capitalised. |
| F19 | Optional | series-wide | entry 4 title, all entries | Terminology | "Quantization" uses -z in a series that otherwise uses -ise. It is consistent everywhere and is the IEEE spelling. |

### F1. Made-up calibration data presented as measured
- **Where:** `src/content/blog/calibration-and-multisensor-fusion.mdx:105` and `:145`, section "3.2 A worked example: the load cell"
- **Text:** "The load-cell channel of the signal-conditioning entry … is calibrated with six reference masses from 0 to 10 kg." … "The residual standard deviation, $s = 2.63 \times 10^{-5}$ mV/V, corresponds to $s/b = 0.13$ g, close to the 0.11 g root-mean-square (RMS) noise that the noise budget of the noise entry predicted for this channel. The calibration data and the noise analysis agree, which is itself a useful check."
- **Problem:** The table of indications was constructed for the example: its residuals are hand-set values, and nothing in the text says so. The CLAUDE.md content-integrity rules require examples to be labelled and forbid presenting results as obtained when they are not. The closing sentence treats agreement between constructed data and the noise budget as evidence, which is circular. The comparison is also not like with like. The 0.11 g figure (entry 5 §6.1) is for the 0.1–10 Hz band, while each indication here is "an average over one second", which has a much narrower noise bandwidth.
- **Recommended correction:** Label the data as illustrative where they are introduced: "The indications below are illustrative values, constructed for this example rather than measured; each stands for an average over one second, in millivolts per volt of excitation." Replace the last two sentences of the paragraph after the output with: "The illustrative data were given a scatter of this size, comparable to the 0.11 g RMS that the noise budget of the noise entry gives over 0.1–10 Hz. With real data the comparison is a useful check: a one-second average has a narrower band and should be somewhat quieter than that figure, so a residual scatter well above the noise budget points to an effect that neither the model nor the budget includes."

### F2. Rounding SAR: the half-LSB has the wrong sign
- **Where:** `src/content/blog/sampling-quantization-and-data-conversion.mdx:175`, section "5.1 Successive approximation"
- **Text:** "(A converter that rounds to the nearest code, as in Section 3.1, adds half an LSB to the DAC voltages; the search is the same.)"
- **Problem:** Under the convention of §3.1, the code reaches $k$ when the input reaches $(k - \tfrac12)q$. Each trial must therefore compare the input with $kq - q/2$: half an LSB is *subtracted* from the DAC voltage, or equivalently added to the input. With the 2.000 V example ($2.000/0.206 = 9.70$ LSB), subtracting gives code 10, the nearest code, while adding gives code 9.
- **Recommended correction:** "(A converter that rounds to the nearest code, as in Section 3.1, compares the input with thresholds half an LSB lower, $kq - q/2$ (equivalently, it adds half an LSB to the input); the search is the same, and for this input it would end at code 10.)"

### F3. Active and passive sensors: the naming varies between texts
- **Where:** `src/content/blog/measurement-systems-and-sensor-characteristics.mdx:63–68`, section "2.3 Active and passive sensors"
- **Text:** "A **self-generating** (or active) sensor produces an electrical output from the measurand's own energy … A **modulating** (or passive) sensor changes an electrical property …"
- **Problem:** This naming is common, but Fraden's *Handbook of Modern Sensors*, cited in entries 1, 2, 3, 6 and 7, uses the opposite convention: a passive sensor needs no external energy, and an active sensor needs excitation. A reader who checks the cited handbook finds the reverse meaning without warning. The series itself uses "self-generating" and "modulating" from then on, so only the parenthetical aliases are at risk.
- **Recommended correction:** After the two bullets, add: "The words *active* and *passive* are used both ways round in the literature (Fraden's handbook, for one, calls a sensor that needs excitation *active*), so this series uses the unambiguous terms self-generating and modulating."

### F4. Threshold and dead band are different quantities
- **Where:** `src/content/blog/measurement-systems-and-sensor-characteristics.mdx:109`, section "3.4 Resolution, threshold and hysteresis"
- **Text:** "The **threshold** (or dead band) is the smallest input change, starting from zero, that produces any output at all."
- **Problem:** The VIM, which this entry says it follows (line 34), defines these separately. The *discrimination threshold* (4.16) is the largest change in the quantity being measured that causes no detectable change in the indication. The *dead band* (4.17) is the maximum interval through which the quantity can be changed *in both directions* without producing a detectable change, typically from backlash or friction, at any operating point. Equating the two is imprecise.
- **Recommended correction:** "- The **threshold** is the smallest input change, starting from zero, that produces a detectable output. The related **dead band** is the largest interval through which the input can be changed in both directions, at any operating point, without a detectable change in output; it is typically caused by friction or backlash."

### F5. "Each stage has its own section of this series"
- **Where:** `src/content/blog/measurement-systems-and-sensor-characteristics.mdx:51`, section "2.1 From measurand to number"
- **Text:** "Each stage has its own section of this series."
- **Problem:** The series is divided into entries, not sections, and the sections of entry 1 are numbered §1–§8, so "section" is misleading. Not every stage has an entry either: digital processing is covered only by calibration (entry 7), and the output stage by none.
- **Recommended correction:** "Later entries take up these stages in turn."

### F6. Link texts that name a series but point to one article
- **Where:** `src/content/blog/measurement-systems-and-sensor-characteristics.mdx:123`; `src/content/blog/calibration-and-multisensor-fusion.mdx:341` and `:592`
- **Text:** "using the models of the [control systems series](/blog/introduction-to-control-systems)"; "already outlined in the [robotics series](/blog/sensing-and-state-estimation#71-fusing-complementary-sensors)"; "The [robotics series](/blog/sensing-and-state-estimation) shows the same ideas at work"
- **Problem:** Each link text names a whole series but leads to a single article, so the text does not match the target. The control-systems models that entry 1 relies on are spread over two articles: second order in `introduction-to-control-systems` and first order in `feedback-and-system-behavior`.
- **Recommended correction:** Entry 1: "using the models of the [Foundations of Control Systems](/series/foundations-of-control-systems) series". Entry 7 line 341: "already outlined in the [state-estimation entry](/blog/sensing-and-state-estimation#71-fusing-complementary-sensors) of the robotics series". Entry 7 line 592: "The [state-estimation entry](/blog/sensing-and-state-estimation) of the robotics series shows …".

### F7. A planned series described as existing
- **Where:** `src/content/blog/sampling-quantization-and-data-conversion.mdx:75`, section "2.1 Oversampling"; `src/content/blog/smart-sensors-and-mems.mdx:149`, section "4.4 Digital interfaces"
- **Text:** "The digital signal processing series treats the digital half." / "the serial buses that the planned embedded-systems series covers"
- **Problem:** `src/content/series/digital-signal-processing.md` and `embedded-and-real-time-systems.md` both have `status: "planned"`. The first sentence presents the DSP series as existing. The second calls the embedded series planned but uses the present tense.
- **Recommended correction:** "The planned digital signal processing series is to treat the digital half." / "the serial buses that the planned embedded-systems series is to cover".

### F8. Noise-free resolution: 13 300, not 13 400
- **Where:** `src/content/blog/noise-interference-and-limits-of-detection.mdx:188`, section "6.1 A noise budget for the load-cell channel"
- **Text:** "The **noise-free resolution** is the full scale divided by the peak-to-peak noise: about 13 400 steps, or 13.7 bits."
- **Problem:** The total in the table is 75.2 nV RMS, so the peak-to-peak noise is 6.6 × 75.2 = 496 nV, and 6.6 mV / 496 nV = 13 300. With the rounded 0.5 µV the result is 13 200. Neither gives 13 400. The 13.7 bits figure is correct ($\log_2 13\,300 = 13.70$).
- **Recommended correction:** "about 13 300 steps, or 13.7 bits".

### F9. Tilt sign convention and the gyroscope axis
- **Where:** `src/content/blog/calibration-and-multisensor-fusion.mdx:345` and `:353`, section "7.1 What each sensor offers"
- **Text:** "Take a sensor that rotates about its y axis by a tilt angle $\theta$, with its z axis pointing up when $\theta = 0$, and positive $\theta$ tipping the x axis upwards." … "The gyroscope measures the rotation rate $\omega = \dot\theta$".
- **Problem:** In a right-handed sensor frame, a positive (right-hand) rotation about +y takes the x axis towards −z. The x axis maps to $(\cos\theta, 0, -\sin\theta)$, so it tips *down*. The angle defined in the text is therefore a negative rotation about y, and a y-axis gyroscope reads $-\dot\theta$. The accelerometer formulas $a_x = g\sin\theta$, $a_z = g\cos\theta$ are right for the stated θ. As written, a reader who implements the equations with a real right-handed IMU gets the gyroscope term with the wrong sign, and the filter diverges.
- **Recommended correction:** Add after the first sentence: "With right-handed sensor axes, this tilt is a rotation about the *negative* y axis, so a y-axis gyroscope reports $-\dot\theta$; below, $\omega$ denotes the rate of $\theta$, that is, the gyroscope's y reading with its sign reversed." Change "The gyroscope measures the rotation rate $\omega = \dot\theta$" to "The gyroscope measures the rotation rate, here $\omega = \dot\theta$".

### F10. Laplace variable and s-domain transfer functions not introduced
- **Where:** `src/content/blog/calibration-and-multisensor-fusion.mdx:357–367`, section "7.2 The complementary filter"
- **Text:** "With $s$ the Laplace variable (not the residual standard deviation of Section 3), …" / "their transfer functions sum to exactly one" / "$\lim_{s \to 0} s \cdot \ldots = b_\omega \tau$"
- **Problem:** The series lists its prerequisites as circuit analysis, calculus and elementary statistics (series file, line 14). The Laplace transform appears nowhere in this series or in the linked control-systems articles, yet §7.2 uses it, with integration written as $1/s$ and the final-value theorem, without saying what any of these are. The term "transfer function" is also defined in entry 1 §3.1 as the *static* characteristic curve, and entries 1 and 4 use it in that sense; here it silently changes meaning. The disambiguation of $s$ itself is already present and adequate.
- **Recommended correction:** Before the equation: "The filter is easiest to describe in the Laplace domain, the standard tool for linear dynamic systems: a signal $x(t)$ is represented by its Laplace transform $x(s)$, a function of the complex frequency $s$; integration becomes division by $s$; and a linear filter is described by its *transfer function*, the ratio of output to input transforms (the dynamic counterpart of the static transfer function of the first entry). With $s$ the Laplace variable (not the residual standard deviation of Section 3), …". Before the limit, write: "by the final-value theorem (the steady value of a signal is the limit of $s$ times its transform as $s \to 0$)".

### F11. The chi-square distribution used without saying what it is
- **Where:** `src/content/blog/calibration-and-multisensor-fusion.mdx:296`, section "6.3 Consistency checks"
- **Text:** "follows a **chi-square** distribution with $n - 1$ degrees of freedom when the readings are consistent"
- **Problem:** The series assumes only elementary statistics. Nothing in this series says what the distribution is; only the robotics series does, in a parenthesis. The thresholds 5.99 and 9.21 depend on it.
- **Recommended correction:** "follows a **chi-square** distribution (the distribution of a sum of squares of independent standard Gaussian variables) with $n - 1$ degrees of freedom, one fewer than the number of readings because $\hat x$ was estimated from them, when the readings are consistent".

### F12. Exercises that repeat the entry
- **Where:** `src/content/blog/calibration-and-multisensor-fusion.mdx:516–561`, section "9. Exercises"
- **Text:** Exercise 1 asks for the least-squares residuals of the PT100 line, and its answer repeats "−0.077, +0.015, +0.062, +0.062, +0.015 and −0.077 Ω", given verbatim in §3.4 (line 190). Exercise 3 repeats the readings $+9.893$ / $-9.744$ m/s² of §4.2 (line 222) and its 0.27 % gravity error. Exercise 5 recomputes the shared-reference example of §6.2 with one number changed.
- **Problem:** Three of the five exercises repeat worked material from the same entry. The author asked for redundancy to be trimmed in this long entry (about 6,750 words of prose). No other entry of the series has an exercise section, so the structure is also inconsistent. The one new point, that the least-squares line halves the end-point nonlinearity (0.20 °C against 0.375 °C), belongs in §3.4.
- **Recommended correction:** Delete §9 and renumber §10–§11 as §9–§10. Nothing links to these anchors. Add to §3.4 after the residuals: "The largest, 0.077 Ω or about 0.20 °C, is about half of the 0.375 °C found against the end-point line in the first entry, because the least-squares line splits the bow between positive and negative errors."

### F20. The embedded-systems series is about to be published (editor's finding)
- **Where:** `src/content/blog/smart-sensors-and-mems.mdx:149`, section "4.4 Digital interfaces"
- **Text:** "the serial buses that the planned embedded-systems series covers"
- **Problem:** Raised by the series editor during the correction phase. The Embedded and Real-Time Systems series is being completed and will be published, so "planned" is about to become false. This supersedes the entry-6 half of F7. Its series page `/series/embedded-and-real-time-systems` already exists. Its articles are not yet on master, so they must not be linked.
- **Recommended correction:** "the serial buses that the [Embedded and Real-Time Systems](/series/embedded-and-real-time-systems) series covers"; in Vietnamese, link `/vi/series/embedded-and-real-time-systems`, which is built.

### F13. The series recap repeats the series description
- **Where:** `src/content/blog/calibration-and-multisensor-fusion.mdx:580–592`, section "11. The Series as a Whole"
- **Text:** Seven bullets that summarise each entry ("The first entry defined measurement, …").
- **Problem:** The list restates the series description and the entries' own summaries, and the series navigation block already links every entry. Only the closing paragraph adds anything.
- **Recommended correction:** Replace the bullets with one sentence: "Together, the seven entries have followed a measurement from the physical world to a number that can be trusted: from what a measurement is, through sensing, conditioning, conversion and noise, to integrated sensors and, here, calibration and fusion." Keep the closing paragraph.

### F14. "A large part of the error budget"
- **Where:** `src/content/blog/calibration-and-multisensor-fusion.mdx:462`, section "8.1 How large the error is"
- **Text:** "an offset of only 10 ms between gyroscope and accelerometer creates disagreements of up to 0.25°, a large part of the error budget of the best filter."
- **Problem:** The best filter in §7.3 has a 0.14° RMS error, so 0.25° exceeds the whole of it. "A large part" understates the point.
- **Recommended correction:** "… disagreements of up to 0.25°, more than the 0.14° RMS error of the best filter in Section 7.3."

### F15. Kalman/complementary equivalence: state the assumptions
- **Where:** `src/content/blog/calibration-and-multisensor-fusion.mdx:454`, section "7.4 From the complementary filter to the Kalman filter"
- **Text:** "A Kalman filter whose state is the angle alone, with the gyroscope rate as its input and the accelerometer tilt as its measurement, settles to a fixed gain when the noise levels are constant, and its update then has exactly the form of the discrete complementary filter, with $1 - \alpha$ as the gain."
- **Problem:** The claim is correct (derivation in the verification log), but it holds for a particular model: the gyroscope's noise enters as white process noise, and the accelerometer's as white measurement noise. The resulting gain then fixes τ. Saying so also explains why the hand-tuned τ of §7.3, which must cope with a bias and a 2 Hz disturbance that are not white, differs from what such a Kalman filter would choose.
- **Recommended correction:** After "as its measurement", insert "(the gyroscope's noise entering as white process noise and the accelerometer's as white measurement noise)", and append to the sentence: "; the noise variances then determine $\alpha$, and so $\tau$, instead of the designer".

### F16. Differential capacitor: which nonlinearity cancels
- **Where:** `src/content/blog/smart-sensors-and-mems.mdx:75`, section "3.1 The accelerometer"
- **Text:** "Like the half bridge of the signal-conditioning entry, the differential arrangement doubles the signal, cancels the first-order nonlinearity, and rejects changes that affect both sides equally."
- **Problem:** $2\varepsilon_0 A x/(d^2 - x^2) = (2C_0 x/d)\,(1 + x^2/d^2 + \dots)$. The even-order (quadratic) term cancels and a cubic term remains, so the arrangement is not exactly linear, unlike the half bridge of entry 3, which is. "First-order nonlinearity" is ambiguous, because the first-order term is the signal itself.
- **Recommended correction:** "… the differential arrangement doubles the signal, cancels the even-order (quadratic) part of the nonlinearity, leaving only a small cubic term of relative size $x^2/d^2$, and rejects changes that affect both sides equally."

### F17. What uncertainty is
- **Where:** `src/content/blog/measurement-systems-and-sensor-characteristics.mdx:32`, section "1.2 Every measurement is uncertain"
- **Text:** "a statement of its **uncertainty**: a quantified range within which the true value is believed to lie with stated confidence."
- **Problem:** VIM 2.26 defines measurement uncertainty as a non-negative parameter that characterises the dispersion of the values attributed to the measurand. A "range … with stated confidence" is the coverage interval of an *expanded* uncertainty. §5.2 of the same entry then defines standard uncertainty as a standard deviation, which matches the VIM but not this sentence.
- **Recommended correction:** "a statement of its **uncertainty**: a quantified measure of the doubt about the result, such as a standard deviation or the half-width of an interval within which the true value is believed to lie with stated probability."

### F18. Capitalisation of cross-entry section references
- **Where:** `src/content/blog/smart-sensors-and-mems.mdx:57`; `src/content/blog/calibration-and-multisensor-fusion.mdx:20`
- **Text:** "the second-order sensor of the first entry (section 4.2)"; "([section 5](/blog/measurement-systems-and-sensor-characteristics#5-errors-and-uncertainty))"
- **Problem:** Every other numbered section reference in the series is capitalised ("Section 3.3", "Section 6").
- **Recommended correction:** "Section 4.2", "Section 5".

### F19. "Quantization" in an -ise series
- **Where:** all entries; title of entry 4 ("Sampling, Quantization and Data Conversion")
- **Text:** "**Quantization** discretises amplitude."
- **Problem:** The series uses British -ise forms (characterise, discretises, normalised, realisation, optimised). "Quantization" (with "quantizer" and "quantizes") is the only -ize family. It is consistent in all seven entries and the series file, and it is the spelling of IEEE Std 1241 and of most British technical writing on converters.
- **Recommended correction:** Leave as is, as a deliberate term-of-art exception. Switching would change the title of entry 4 and the series objectives for no gain in clarity.

## Concept introduction map

| Concept | First used (path:line) | Introduced where (path:line, or "not introduced") | Assessment |
|---|---|---|---|
| Measurand, measurement, unit, SI | entry 1:26 | entry 1:26–28 | Good. |
| Measurement uncertainty | entry 1:32 | entry 1:32, 162 | Introduced; wording imprecise (F17). |
| VIM, GUM | entry 1:34 | entry 1:34 | Good. |
| Self-generating / modulating sensor | entry 1:67 | entry 1:65–70 | Good; aliases conflict with Fraden (F3). |
| Static transfer function | entry 1:78 | entry 1:78 | Good; meaning later changed in entry 7 (F10). |
| Time constant, natural frequency, damping ratio | entry 1:131, 137 | entry 1:127–137, with a link to the control series | Adequate. |
| Standard, combined and expanded uncertainty, Type A/B | entry 1:162 | entry 1:162–175 | Good. |
| Energy domain | entry 2:20 | entry 2:20 | Good. |
| Gauge factor, strain | entry 2:67 | entry 2:67–73 | Good. |
| ADC | entry 3:18 | entry 3:18; entry 4:17 | Good. |
| Decibel | entry 3:28 | entry 3:28 | Good. |
| Operational amplifier, virtual ground | entry 3:104 | entry 3:104–121 | Good. |
| CMRR, common mode | entry 3:138 | entry 3:136–145 | Good. |
| Sampling, aliasing, Nyquist frequency | entry 4:19 | entry 4:19–42 | Good. |
| LSB, quantization step | entry 4:81 | entry 4:81–84 | Good. |
| SINAD, ENOB | entry 4:138 | entry 4:138 | Good. |
| Noise spectral density, white noise, ENBW | entry 5:36 | entry 5:36–56 | Good. |
| Allan deviation | entry 5:126 | entry 5:126 | Briefly, adequate. |
| MEMS, smart sensor | entry 2:192 (as "microfabricated"); entry 6:21 | entry 6:21–22 (and series body) | Good. |
| Coriolis effect | entry 6:94 | entry 6:94 | Good. |
| Covariance, correlation coefficient | entry 7:60 | entry 7:60 | Good. |
| Least squares, design matrix | entry 7:79, 111 | entry 7:79–111 | Good. |
| Student t distribution | entry 7:182 | not introduced (named only) | Acceptable at this level: used only for a coverage factor. |
| Chi-square distribution | entry 7:296 | not introduced in this series | F11. |
| Laplace variable, s-domain transfer function, final-value theorem | entry 7:357 | not introduced in this series or the linked articles | F10. |
| Kalman filter | entry 7:268 | robotics entry `sensing-and-state-estimation` §4–5, linked | Good. |
| Specific force | entry 7:216 | entry 7:216 | Good. |

## Versions, defaults and conventions

| Assumption | Where it appears | Stated in the text? | Assessment |
|---|---|---|---|
| SI as revised in 2019 | entry 1:28 | Yes | Correct. |
| IEC 60751 coefficients, range 0–850 °C | entry 1:78–84, 241 | Yes (2008 and 2022 editions) | Correct. |
| VIM JCGM 200:2012, GUM JCGM 100:2008 | entry 1:34; entry 7:20, 26 | Yes | Correct. |
| Decibels as voltage ratios ($20\log_{10}$) | entry 3:28 | Yes | Good. |
| Ideal op-amp model, then real departures | entry 3:106 | Yes | Good. |
| Unipolar converter, 0 to $V_\text{ref}$ | entry 4:24 | Yes | Good. |
| $q = \text{FSR}/2^N$ and the mid-tread (rounding) convention | entry 4:84–95 | Yes | Good; SAR parenthetical wrong (F2). |
| IEEE Std 1241-2010 | entry 4:125, 225 | Yes | Real edition; whether a later revision supersedes it was not checked. |
| Noise temperature 300 K; unqualified noise is RMS | entry 5:24 | Yes | Good. |
| Peak-to-peak as 6.6σ (99.9 %) | entry 5:32 | Yes | Good. |
| Mains 50 or 60 Hz | entry 3:206; entry 5:133 | Yes | Good. |
| g as acceleration of gravity, not gram | entry 6:90 | Yes | Good. |
| Python 3.13, NumPy 2.5 | entry 7:20 | Yes | Verified: Python 3.13.16 and NumPy 2.5.3 reproduce every output. |
| Degrees in text, radians in code | entry 7:20 | Yes | Good. |
| Tilt sign and axis convention | entry 7:345 | Partly | Disagrees with right-handed gyroscope sign (F9). |
| $g_n = 9.80665$ m/s² against local gravity | entry 7:222 | Yes | Good. |
| ISO/IEC 17025:2017, ISO/TS 28037:2010, ILAC-G24:2007 / OIML D 10:2007 | entry 7:52, 202, 236 | Yes | Titles correct; see verification log. |

## Series-level notes

- **Cross-reference map.** Every "previous entry", "next entry", "first entry", "the signal-conditioning entry", "the noise entry" and similar reference was checked against its target, and all are true. Two exceptions are covered by findings: F5 ("section of this series") and F7 (a planned series in the present tense). The promises in entries 1–6 that a later entry would treat a topic are all fulfilled:
  - entry 1 promises quantization and calibration in practice;
  - entry 3 promises anti-aliasing and the noise bandwidth;
  - entry 4 promises dither;
  - entry 6 promises fusion and time alignment.
  Every internal link resolves (`check:links`) and every fragment exists.
- **Robotics references.** The robotics-series claims in entries 6 and 7 hold against `sensing-and-state-estimation.mdx`:
  - the Kalman update in §4 matches inverse-variance weighting;
  - §7.1 outlines the complementary filter;
  - §8 covers late measurements and chi-square gating.
- **Terminology.** "Self-generating/modulating", "excitation", "ratiometric", "quarter/half/full bridge", "LSB", "ENBW" and "noise-free resolution" are used consistently. The letter $s$ has several meanings, each defined where it is used:
  - entry 1: sample standard deviation;
  - entry 6 §2: a scale factor;
  - entry 6 §4.2: $s(T)$, a sensitivity;
  - entry 7 §3: residual standard deviation;
  - entry 7 §7: the Laplace variable, explicitly disambiguated at line 357.
  Entry 7 §4.2 deliberately writes $s_f$ for the scale factor to avoid a clash. This is acceptable.
- **Spelling.** British -ise and "behaviour", "centre", "metre", "fibre", "modelled" and "aluminium" are used throughout. "Analog" is American, but it is used consistently (29 occurrences, no "analogue"). The only -ize family is "quantization" (F19).
- **VIM paraphrases.** These were checked against JCGM 200:2012 as recalled:
  - calibration (2.39, two steps) and adjustment (3.11, with its note on recalibration);
  - verification (2.44) and calibration hierarchy (2.40, uncertainty increasing along it);
  - metrological traceability (2.41), resolution (4.14), drift (4.21) and influence quantity (2.52);
  - repeatability, precision and trueness (2.21, 2.15, 2.14).

  All are faithful except threshold/dead band (F4) and the description of uncertainty (F17). "Accuracy combines both" (entry 1:158) is the ISO 5725-1 reading rather than VIM 2.13's wording, but it is consistent with the VIM's definition and was left.
- **Structure.** Every entry has an introduction, numbered sections, a summary table, a forward pointer and a reference list. Entry 7 alone had an exercise section (F12) and a full recap (F13).
- **Illustrative data.** The load-cell calibration table is unlabelled (F1). The other numerical examples in entry 7 are visibly hypothetical ("Suppose", "If the z axis reads", simulated data with stated parameters):
  - the thermometer readings of §6.3;
  - the six-position readings of §4.2;
  - the interval model of §5.
  The resolution adds an explicit "illustrative" label to §6.3 as well.
- **Frontmatter.** All seven entries have category "Engineering", `publishedAt` 2026-10-13, `series: sensor-systems` and `seriesOrder` 1–7 with no gaps, and they share the tags "sensors" and "measurement".

## Verification log

- `npm run build:local`: passed (type check, build, Mermaid and KaTeX rendering, Pagefind; localhost-URL warning only, as expected for `build:local`).
- `npm run check:links`: passed ("Checked 198 pages and 5524 internal references in dist. All internal links resolve.").
- dist checks (`dist/blog/<slug>.html` for the seven entries):
  - Mermaid `min-width`: entry 1: 142 px; entry 6: 437 px; entry 7: 142 px and 323 px. All are under 600 px.
  - `katex-error`: 0 in every entry.
  - No text glued to inline elements. The only pattern hits are KaTeX-internal `lo<span>g` spans.
- Recomputed (Python 3.13.16, NumPy 2.5.3), all correct unless a finding says otherwise:
  - **Entry 1:**
    - PT100: $R(100) = 138.51$ Ω; local slopes 0.391 and 0.379 Ω/°C; end-point nonlinearity 0.1444 Ω = 0.375 °C.
    - First-order response: 63.2 / 95.0 / 99.3 %, and the 1 % settling time $4.6\tau = 18.4$ s.
    - Uncertainty budget: 0.0158, 0.050 and 0.0029 °C → $u_c = 0.0525$, $U = 0.105 \to 0.11$ °C.
    - Two-point gain 1.01317, giving 50.25 °C.
    - Self-heating 0.1385 mW.
  - **Entry 2:**
    - NTC: 33.62 / 3.588 / 0.698 kΩ; −4.44 %/K.
    - Capacitor: 8.854 pF, +0.089 pF.
    - Piezoelectric leakage: $e^{-10} = 0.0045$ %.
    - Responsivity 0.548 A/W.
    - Nernst slope 59.16 and 61.54 mV.
  - **Entry 3:**
    - Quarter bridge 2.4975 mV.
    - Difference-amplifier CMRR 54.0 dB.
    - $R_G = 50.05$ Ω.
    - Transimpedance bandwidth 159 kHz; charge-amplifier cut-off 0.159 Hz; RC cut-off 9.95 Hz.
    - Butterworth at 50 Hz: 14.15 / 27.97 / 55.92 dB.
    - Butterworth at 3 Hz: 0.958 / 0.996 / 0.99997.
  - **Entry 4:**
    - Anti-aliasing attenuation 76.34 dB against 72.25 dB for 12 bits.
    - $q$ = 0.806 mV / 50.4 µV / 0.197 µV; $u_q = 0.233$ mV.
    - SQNR 74.01 / 98.09 dB; ENOB 13.99.
    - Jitter limits 38.9 ns and 0.121 ns.
    - Load cell: 3686 and 58 982 codes; 2.71 g and 0.170 g per code.
    - SAR DAC voltages 1.650 / 2.475 / 2.0625 / 1.856 V. The input is 9.70 LSB, so rounding gives code 10 (F2).
  - **Entry 5:**
    - 99.90 % within ±3.29σ; one in 741 beyond 3σ.
    - Thermal noise 4.07 and 2.41 nV/√Hz; kT/C noise 64.4 µV.
    - Photodiode: shot noise 0.420 pA/√Hz, resistor noise 0.129 pA/√Hz, total 0.220 nA; SNR 2505 (68.0 dB).
    - Amplifier noise: 1/f part 67.9 nV, white part 31.5 nV, total 74.8 nV.
    - Total density 10.29 nV/√Hz.
    - Load-cell budget: bridge 7.58 nV; total 75.2 nV = 0.114 g; 87 800 counts = 16.42 bits = 98.9 dB.
    - Noise-free resolution 13 300 (F8).
    - Capacitive coupling 72.3 nA, 3.18 GΩ, 25.3 µV. Magnetic coupling 3.14 µV.
    - Dither: exact expected-code bias max 0.093 q at σ = 0.25 q and 0.0023 q at σ = 0.5 q; 0.577 q / 16 = q/27.7; 3.9 readings per second.
    - ENBW by numerical integration: 1.571 / 1.111 / 1.026.
  - **Entry 6:**
    - Accelerometer: 9.94 nm per g, 0.994 fF per g.
    - Thermomechanical noise $7.21 \times 10^{-4}$ m/s²/√Hz = 73.5 µg/√Hz; 0.735 mg in 100 Hz; 7.3 pm; 0.73 aF.
    - Gyroscope: drive velocity 1.257 m/s, Coriolis acceleration 0.0439 m/s² = 4.47 mg.
    - $\Delta V_\text{BE}$ 53.76 mV and 0.179 mV/K.
  - **Entry 7:**
    - Reference-ratio penalty 3.08 / 11.8 / 0.50 %.
    - All four listings were run as published. The outputs are identical to the quoted text, digit for digit:
      - least-squares fit and use of the curve;
      - fusion and consistency;
      - complementary-filter simulation;
      - time alignment.
    - Load cell: offset 10.56 g; sensitivity −0.066 %; $s/b = 0.132$ g; curve minimum $s/(b\sqrt6) = 0.054$ g; covariance ratio 1.27.
    - Student t: $t_{0.95}(4) = 2.776$ by numerical integration of the t density; $P(|t_4| < 2) = 0.884$; $U = 0.142 \times 2.78 = 0.39$ g.
    - PT100 least-squares residuals −0.077 / +0.015 / +0.062 Ω; slope 0.385055; the quadratic fit is exact.
    - Six-position test: offset 0.0745 m/s² = 7.6 mg; scale factor 1.00121; gravity error 0.27 %; tilt error $\phi^2/2$ at 1° = 0.015 %.
    - Gyroscope: 0.0032 °/s; Earth rate 15.04 °/h = 0.00418 °/s.
    - Calibration interval 2.67 years.
    - Shared-reference mean 0.0513 °C; independence figure 0.037 °C.
    - Chi-square(2) quantiles 5.991 and 9.210.
    - Consistency example: $z_{12} = -0.707$; shift 3.2u.
    - Exercises: 10.252 m, 0.24 m, 0.64, 1.4; 1.0039; 0.990; 0.054 / 0.058 / 0.041 °C.
    - Tilt rate 25.13 °/s; 0.25°; clock drift 0.18 s per hour.
- Steady-state Kalman filter versus complementary filter:
  - **Model.** State θ; prediction $\theta^-_k = \hat\theta_{k-1} + \omega_k\Delta t$ with variance $P^-_k = P_{k-1} + Q$, where $Q$ is the gyroscope noise integrated over $\Delta t$. Measurement $z_k = \theta_{a,k}$ with variance $R$.
  - **Update.** $\hat\theta_k = \theta^-_k + K_k(z_k - \theta^-_k) = (1 - K_k)(\hat\theta_{k-1} + \omega_k\Delta t) + K_k\,\theta_{a,k}$.
  - **Steady state.** With $Q$ and $R$ constant, the Riccati recursion $P^- \leftarrow P^- R/(P^- + R) + Q$ converges to $P^-_\infty = \tfrac12\bigl(Q + \sqrt{Q^2 + 4QR}\bigr)$, so $K_\infty = P^-_\infty/(P^-_\infty + R)$ is constant. The update is then exactly the complementary filter with $\alpha = 1 - K_\infty$, and for $Q \ll R$, $K_\infty \approx \sqrt{Q/R}$ and $\tau \approx \Delta t\sqrt{R/Q}$.
  - **Numerical check.** The recursion converges to the closed form, giving $K = 0.001000$ and $0.000250$ for two noise settings. Claim confirmed.
- References checked:
  - Fraden, 5th ed., Springer 2016.
  - Regtien and Dertien, 2nd ed., Elsevier 2018.
  - Bentley, 4th ed., Pearson 2005.
  - Webster and Eren, 2nd ed., CRC 2014.
  - Pallàs-Areny and Webster, 2nd ed., Wiley 2001.
  - Horowitz and Hill, 3rd ed., CUP 2015.
  - Franco, 4th ed., McGraw-Hill 2015.
  - Oppenheim and Schafer, 3rd ed., Pearson 2010.
  - Kester, Newnes 2005.
  - IEEE Std 1241-2010 (title correct).
  - Motchenbacher and Connelly, Wiley 1993.
  - Ott, Wiley 2009.
  - Senturia, Kluwer 2001.
  - Kaajakari, Small Gear 2009.
  - Gabrielson, IEEE Trans. Electron Devices 40(5):903–909, 1993.
  - Taylor, 2nd ed., University Science Books 1997.
  - Thrun, Burgard and Fox, MIT Press 2005.
  - JCGM 200:2012 and JCGM 100:2008 (titles correct).
  - ISO/IEC 17025:2017 (title correct).
  - ISO/TS 28037:2010, *Determination and use of straight-line calibration functions*. Its scope covers straight-line calibration with uncertainty in the response only, in both variables, and with correlation, as the text says.
  - ILAC-G24:2007 / OIML D 10:2007, *Guidelines for the determination of calibration intervals of measuring instruments*. It describes the staircase (automatic adjustment) method and the control-chart method, among others, as the text says.
  - $E_n = (x_1 - x_2)/\sqrt{U_1^2 + U_2^2}$ with $|E_n| \le 1$ satisfactory is the standard proficiency-testing criterion (ISO/IEC 17043, ISO 13528).
  - GUM Annex G gives the t-distribution coverage factor ($t_{95}(4) = 2.78$).

  All these are real and correctly cited as far as can be checked offline.
- Not verified:
  - The exact wording of the VIM and of the ILAC/OIML and ISO/TS documents. These were checked from knowledge of the documents, not against copies, because there is no network access to the standards.
  - Whether ILAC-G24 / OIML D 10 and IEEE Std 1241 have later editions that supersede the cited ones. The cited editions are real; the articles do not claim that they are current.
  - Material constants quoted as typical: the quartz coefficient of 2.3 pC/N, silicon's Young's modulus range, the type K Seebeck coefficient and the piezoresistive gauge factor of about 100. These were checked only for plausibility against standard values.
