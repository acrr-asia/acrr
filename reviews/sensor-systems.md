# Series review: Sensor Systems

- Series: `sensor-systems` (7 articles, status published, 0 planned entries)
- Reviewed commit: 49941d2 (series files unchanged since the wave-1 commit 594bba0)
- Date: 2026-10-14
- Reviewer: independent wave-2 reviewer (fact-check, technical review, series review). The reviewer wrote and revised none of this text.

## Summary

The series is technically sound and well sequenced. Every worked number in the seven entries was recomputed with Python 3.13.16 and NumPy 2.5.3, and all five Python listings of entry 7 were re-run. Every printed line matches the text exactly, and no arithmetic, derivation or code error was found. The wave-1 revision (descriptions, sentence-case headings, house references, the new overview body, the $f_\text{nc}$ notation in entry 5 and the new closing of entry 7) kept the technical content intact.

There is no blocking finding. The eight should-fix findings fall into four groups:
- Two consistency defects: the noise-density figure in entry 5 still labels the 1/f corner $f_c$, which wave 1 renamed $f_\text{nc}$ in the text; and four passages say that a smart sensor's chain sits "on one chip", where entry 6 itself says it more commonly sits on two dies in one package.
- One misleading technical claim, added in the previous review's correction to entry 7: that one-second calibration averages "should be somewhat quieter" than the 0.1–10 Hz noise budget. Under the series' own 1/f noise model, they need not be.
- Three superseded or withdrawn references: ISO/TS 28037:2010 (withdrawn July 2026), ILAC-G24/OIML D 10:2007 (replaced in 2022) and IEEE Std 1241-2010 (replaced in 2023).
- Two wording defects: a link labeled "robotics series" that points to a single article, and "noise figures" in the overview, where "noise figure" is a defined quantity with a different meaning.

The series can be considered final once the should-fix findings are resolved and the report is stamped.

Findings: 0 blocking, 8 should fix, 5 optional.

## Objectives coverage

| Objective (from the series file) | Covered by | Assessment |
|---|---|---|
| Describe a measurement system as a chain from measurand to number, and characterize a sensor by its static and dynamic properties. | Entry 1, §2–§4 | Met. The chain diagram, static characteristics (§3) and first- and second-order dynamics (§4) are all present. |
| Explain the main physical principles by which sensors convert a quantity into an electrical signal. | Entry 2, all sections; entry 6 §1 and §3 (MEMS realizations) | Met. |
| Design the analog front end of a sensor: excitation, bridges, amplification and filtering. | Entry 3, §1–§7 (complete load-cell channel) | Met. |
| Explain sampling, quantization and data conversion, and the noise that limits what can be detected. | Entry 4 (sampling, quantization, converters); entry 5 (noise, interference, detection limit) | Met. |
| State and combine measurement uncertainties, and calibrate and fuse sensors. | Entry 1 §5 (budget); entry 7 §2–§3 (propagation, curve uncertainty), §1 and §3–§5 (calibration), §6–§8 (fusion) | Met. The objective bundles three outcomes (wave-1 note D3), but each is checkable against a named section. No change is needed. |

## Findings

| ID | Severity | Article | Location | Dimension | Finding |
|---|---|---|---|---|---|
| T1 | Should fix | `src/content/blog/noise-interference-and-limits-of-detection.mdx` | §2.3, figure (line 92); `scripts/generate-diagrams.py:436–437, 456` | consistency | Figure labels the 1/f corner "$f_c$ = 10 Hz"; the text now calls it $f_\text{nc}$ and reserves $f_c$ for the filter cut-off. |
| T2 | Should fix | `src/content/blog/calibration-and-multisensor-fusion.mdx` | §3.2 (line 145) | accuracy | The claim that one-second averages "should be somewhat quieter" than the 0.1–10 Hz budget contradicts the series' 1/f model. |
| S1 | Should fix | Overview and entries 5, 6, 7 | `sensor-systems.md:16`, entry 5 line 213, entry 6 line 82, entry 7 line 535 | consistency | "On one chip" / "on the same chip" contradicts entry 6 §4, which says a MEMS die and an ASIC more commonly share one package. |
| S2 | Should fix | `src/content/blog/sensing-principles.mdx` | §7.2 (line 166) | consistency | The link text "robotics series" points to one article (`/blog/what-is-a-robot`). |
| S3 | Should fix | `src/content/series/sensor-systems.md` | line 20 | accuracy | "Noise figures are root-mean-square values": *noise figure* is a defined quantity (a ratio in dB), not an RMS value. |
| F1 | Should fix | `src/content/blog/calibration-and-multisensor-fusion.mdx` | §3.5 (line 202), References (line 544) | evidence | ISO/TS 28037:2010 was withdrawn on 2026-07-24 and replaced by ISO 28037:2026; the text says it "specifies" these cases. |
| F2 | Should fix | `src/content/blog/calibration-and-multisensor-fusion.mdx` | §5 (line 236), References (line 542) | evidence | ILAC-G24:2007 / OIML D 10:2007 is superseded by the 2022 edition, which has a changed title. |
| F3 | Should fix | `src/content/blog/sampling-quantization-and-data-conversion.mdx` | §4 (line 125), References (line 223) | evidence | IEEE Std 1241-2010 is Inactive-Reserved and superseded by IEEE Std 1241-2023. |
| F4 | Optional | `src/content/blog/measurement-systems-and-sensor-characteristics.mdx` | References (line 243) | evidence | "(The 2008 edition gives the same coefficients.)" could not be verified from public sources. |
| S4 | Optional | `src/content/blog/signal-conditioning.mdx` | §2.1 (line 80) | language | "$x/2 = 0.1$ %": a space before % remains (standards 5.5). |
| S5 | Optional | `src/content/blog/measurement-systems-and-sensor-characteristics.mdx` | §3.3 figure caption (line 104) | consistency | "the straight line through the end points" vs the bold house term "endpoint line" two paragraphs earlier. |
| S6 | Optional | `src/content/series/sensor-systems.md` | line 20 | consistency | "Units are SI throughout", but entries 5–7 quote acceleration in g, mg and µg/√Hz, and entries 3 and 7 use mV/V. |
| S7 | Optional | `src/content/blog/calibration-and-multisensor-fusion.mdx` | §9 closing (line 535) | consistency | "This entry has stated and combined uncertainties": the first part of objective 5 is first met in entry 1 §5. |

### T1. The noise-density figure still uses $f_c$ for the 1/f corner
- **Where:** `src/content/blog/noise-interference-and-limits-of-detection.mdx:92` (the `<NoiseDensity />` figure in §2.3); the label is generated at `scripts/generate-diagrams.py:456`, and the script comment at lines 436–437 also says `f_c`.
- **Text:** The rendered label reads "corner *f*<sub>c</sub> = 10 Hz" (`src/components/diagrams/NoiseDensity.astro:36`; also present in `/tmp/claude-0/b2/blog/noise-interference-and-limits-of-detection.html`). The prose says "the **noise corner frequency** $f_\text{nc}$" (line 86).
- **Problem:** Wave 1 renamed the corner $f_\text{nc}$ so that $f_c$ means only the filter cut-off (entry 5 §1.3 and entry 3 §6.1). Its revision log states that "the NoiseDensity diagram uses no symbol, so no regeneration", but the figure does use the symbol, so the clash the revision meant to remove is still on the page.
- **Recommended correction:** In `scripts/generate-diagrams.py`, change line 456 to `'corner ' + sub('f', 'nc') + '= 10 Hz'`, and the comment at lines 436–437 to `e(f) = e_w sqrt(1 + f_nc / f)` with "corner frequency f_nc = 10 Hz". Then re-run `python3 scripts/generate-diagrams.py src/components/diagrams` and confirm that only `NoiseDensity.astro` changes. The Vietnamese article uses the same component, so it picks up the change automatically.

### T2. "A one-second average … should be somewhat quieter" than the 0.1–10 Hz budget
- **Where:** `src/content/blog/calibration-and-multisensor-fusion.mdx:145`, §3.2.
- **Text:** "With real data the comparison is a useful check: a one-second average has a narrower band and should be somewhat quieter than that figure, so a residual scatter well above the noise budget points to an effect that neither the model nor the budget includes."
- **Problem:** The budget in entry 5 §6.1 is dominated by 1/f noise: 67.9 of 75 nV RMS. Entry 5 §2.3 shows that 1/f noise depends only on the ratio of the band edges, and entry 5 §4 says that "averaging helps only for white noise". A one-second average cuts the upper edge to roughly 0.5 Hz (equivalent noise bandwidth of a 1 s boxcar). But the scatter between six calibration points taken over several minutes also contains 1/f noise down to about 1/(duration of the calibration).
  - Recomputed with the entry-5 model ($e_w = 10$ nV/√Hz, $f_\text{nc} = 10$ Hz), for a 10-minute calibration: 1/f part from 1/600 Hz to 0.5 Hz is $10\sqrt{10 \ln 300} = 75.5$ nV, and the white part in 0.5 Hz is 7.1 nV, about 76 nV in total. That is not quieter than the 75 nV budget.
  - The conclusion of the sentence (a scatter well above the budget signals an unmodeled effect) still holds. The reason given for it does not.
- **Recommended correction:** "With real data the comparison is a useful check. Because the budget is dominated by 1/f noise, one-second averages taken over a calibration lasting minutes are not necessarily quieter than the 0.1–10 Hz figure: averaging narrows the band at the top, but the span of the calibration extends it at the bottom. A residual scatter well above the noise budget therefore points to an effect that neither the model nor the budget includes."

### S1. "On one chip" contradicts entry 6
- **Where:**
  - `src/content/series/sensor-systems.md:16`: "The sixth entry shows how smart sensors and microelectromechanical systems (MEMS) build that chain on one chip."
  - `noise-interference-and-limits-of-detection.mdx:213`: "what happens when those components are built together on one chip".
  - `smart-sensors-and-mems.mdx:82`: "with a charge amplifier (from the signal-conditioning entry) on the same chip".
  - `calibration-and-multisensor-fusion.mdx:535`: "the [sixth] showed the whole chain integrated on one chip".
- **Problem:** Entry 6 §4 (line 106) says: "The sensing element and the electronics may share one die (**monolithic** integration), or, more commonly, a MEMS die and an application-specific integrated circuit (ASIC) are made in separate processes … and placed side by side in one package." Its opening (line 17) also says "in one package". The four passages state the less common case as the rule, and the series contradicts itself.
- **Recommended correction:**
  - Overview line 16: "… build that chain in a single package."
  - Entry 5 line 213: "… when those components are built together in one package".
  - Entry 6 line 82: "… with a charge amplifier (from the signal-conditioning entry) in the same package".
  - Entry 7 line 535: "… showed the whole chain integrated in one package".
  - Apply the same changes to the Vietnamese overview and entries 5 and 6. Entry 7 has no translation.

### S2. "Robotics series" links to a single article
- **Where:** `src/content/blog/sensing-principles.mdx:166`, §7.2.
- **Text:** "(the joint encoders of the [robotics series](/blog/what-is-a-robot))"
- **Problem:** The link text names a series, but the target is the first article of that series. The previous review corrected three links of exactly this kind ("Three links name a series but point to an article"); this one was added in wave 1. Elsewhere the series words such links as "the [state-estimation entry](…) of the robotics series" (entry 7) or links the series page (entry 1 line 125, entry 6 line 149).
- **Recommended correction:** "(the joint encoders described in the [first entry](/blog/what-is-a-robot) of the robotics series)". Alternatively, "(the joint encoders of the [Introduction to Robotics](/series/introduction-to-robotics) series)".

### S3. "Noise figures" in the overview
- **Where:** `src/content/series/sensor-systems.md:20`.
- **Text:** "Noise figures are root-mean-square values at 300 K unless stated otherwise."
- **Problem:** In electronics, *noise figure* is a defined quantity: the ratio, usually in dB, of input to output signal-to-noise ratio. It is not an RMS voltage or current. The phrase is on the front page of a series whose fifth entry is about noise, so a reader with that background would misread it. Entry 5 line 24 states the convention correctly: "a noise voltage written without qualification is a root-mean-square value".
- **Recommended correction:** "Noise voltages and currents are root-mean-square values, computed at 300 K unless stated otherwise." Apply the same change to `src/content/series/vi/sensor-systems.md`.

### F1. ISO/TS 28037:2010 has been withdrawn
- **Where:** `src/content/blog/calibration-and-multisensor-fusion.mdx:202` and References line 544.
- **Text:** "ISO/TS 28037:2010 specifies these cases for straight-line calibration functions." / "ISO/TS 28037:2010, *Determination and use of straight-line calibration functions*, International Organization for Standardization, 2010."
- **Problem:** The ISO catalogue (iso.org/standard/44473) lists ISO/TS 28037:2010 as Withdrawn (stage 95.99, 2026-07-24), replaced by ISO 28037:2026. The new edition has the same title, was published 2026-07, and is at stage 60.60 (iso.org/standard/84405). Its abstract covers uncertainties in both variables and general covariance matrices, so it supports the sentence. The present tense "specifies" now describes a withdrawn document.
- **Recommended correction:** Text: "ISO 28037:2026, which replaced the technical specification ISO/TS 28037:2010, specifies these cases for straight-line calibration functions." Reference: "ISO 28037:2026, *Determination and use of straight-line calibration functions*, International Organization for Standardization, 2026."

### F2. ILAC-G24 / OIML D 10 superseded by the 2022 edition
- **Where:** `src/content/blog/calibration-and-multisensor-fusion.mdx:236` and References line 542.
- **Text:** "ILAC-G24:2007 / OIML D 10:2007, *Guidelines for the determination of calibration intervals of measuring instruments*, … 2007."
- **Problem:** The OIML publishes ILAC-G24:2022 / OIML D 10:2022, *Guidelines for the determination of recalibration intervals of measuring equipment* (oiml.org/en/files/pdf_d/d010-e22.pdf). It states that it supersedes the 2007 edition. The 2022 edition still describes the two methods the text names, "automatic adjustment or 'staircase'" and "control chart", so the body text remains true. Only the reference is out of date. The wave-1 log confirmed the 2007 title but did not notice the newer edition.
- **Recommended correction:** "ILAC-G24:2022 / OIML D 10:2022, *Guidelines for the determination of recalibration intervals of measuring equipment*, International Laboratory Accreditation Cooperation and International Organization of Legal Metrology, 2022." The text at line 236 ("ILAC-G24 / OIML D 10") needs no change.

### F3. IEEE Std 1241-2010 superseded by IEEE Std 1241-2023
- **Where:** `src/content/blog/sampling-quantization-and-data-conversion.mdx:125` ("defined in IEEE Std 1241") and References line 223.
- **Text:** "IEEE Std 1241-2010, *IEEE Standard for Terminology and Test Methods for Analog-to-Digital Converters*, IEEE, 2011."
- **Problem:** standards.ieee.org lists IEEE 1241-2010 as Inactive-Reserved, superseded by IEEE 1241-2023. The 2023 edition has the same title, is Active, and was published 2023-10-06. The 2010 details in the reference are correct (board approval 2010-06-17, published 2011-01-14), but they point the reader to an inactive edition. The wave-1 log flagged this point and left it.
- **Recommended correction:** "IEEE Std 1241-2023, *IEEE Standard for Terminology and Test Methods for Analog-to-Digital Converters*, IEEE, 2023." The body text, which names no edition, can stay. If the author prefers to keep the edition that was actually consulted, append "(superseded by IEEE Std 1241-2023)" to the existing entry instead.

### F4. Coefficients of the 2008 and 2022 editions of IEC 60751
- **Where:** `measurement-systems-and-sensor-characteristics.mdx:243`.
- **Text:** "(The 2008 edition gives the same coefficients.)"
- **Problem:** Public sources available here did not settle it. The IEC 60751:2022 foreword (preview) lists among its changes "formula of resistance versus temperature relationship become the standard specification" and gives α = 3.851 × 10⁻³ °C⁻¹. That α equals $A + 100B$ with the stated coefficients (recomputed: 3.85055 × 10⁻³), which is consistent with unchanged A and B but does not prove it.
- **Recommended correction:** Optional. Either drop the parenthetical, or qualify it as "(The 2008 edition gives the same $\alpha = 3.851 \times 10^{-3}$ °C⁻¹.)".

### S4. Space before %
- **Where:** `signal-conditioning.mdx:80`, "a relative error of about $x/2 = 0.1$ %".
- **Recommended correction:** "$x/2 = 0.1\%$".

### S5. "End points" in the figure caption
- **Where:** `measurement-systems-and-sensor-characteristics.mdx:104`, "relative to the straight line through the end points".
- **Recommended correction:** "relative to the endpoint line". Wave 1 made "endpoint line" the defined house term at line 100.

### S6. "Units are SI throughout"
- **Where:** `sensor-systems.md:20`.
- **Problem:** Entries 5–7 quote accelerations in g, mg and µg/√Hz, and entry 6 explicitly defines g as the acceleration of gravity. Entries 3 and 7 use mV/V. These are deliberate and conventional, but "throughout" overstates the convention.
- **Recommended correction:** "Units are SI, with accelerations also given in multiples of the standard gravity *g* and bridge outputs in millivolts per volt."

### S7. Closing paragraph attributes the uncertainty objective to entry 7 only
- **Where:** `calibration-and-multisensor-fusion.mdx:535`.
- **Text:** "This entry has stated and combined uncertainties, calibrated sensors and fused them."
- **Recommended correction:** "Building on the uncertainty budget of the first entry, this entry has propagated and combined uncertainties, calibrated sensors and fused them."

## Concept introduction map

| Concept | First used (path:line) | Introduced where | Assessment |
|---|---|---|---|
| Measurand, measurement, unit | entry 1:26 | entry 1:26 (bold definitions) | Good |
| Uncertainty; Type A/B; expanded uncertainty | entry 1:32 | entry 1:32, 164–177 | Good |
| Transfer function (static) | entry 1:80 | entry 1:80; dynamic sense distinguished at entry 7:357 | Good |
| Second-order system, natural frequency, damping | entry 1:139 | entry 1:139, referring to the Foundations of Control Systems series (linked at 1:125) | Adequate |
| Decibel | entry 1:145 ("3 dB, a factor of about 0.71") | entry 3:28 | Adequate: entry 1 gives the factor in words |
| Analog-to-digital converter | entry 1:46 | entry 3:18, entry 4:17 | Good |
| Excitation, ratiometric measurement | entry 1:68 | entry 1:68, entry 3:32–39 | Good |
| Operational amplifier, virtual ground | entry 3:104 | entry 3:104–121 | Good |
| Magnitude response, cut-off frequency | entry 3:213 | entry 3:213–219 | Good |
| Sampling, aliasing, Nyquist frequency | entry 3:209 (mention) | entry 4:19–52 | Good |
| RMS, Gaussian distribution | entry 1:177 (Gaussian), entry 4:111 (RMS) | entry 4:111 (RMS expanded); entry 5:30–32 | Adequate: elementary statistics is a stated prerequisite |
| Noise spectral density, white noise, ENBW | entry 3:208 (forward reference) | entry 5:36–56 | Good |
| Allan deviation | entry 5:126 | entry 5:126 (one-line definition) | Adequate |
| MEMS | overview:16, entry 5:213 | expanded at both; defined at entry 6:21 | Good |
| Coriolis effect | entry 6:94 | entry 6:94 | Good |
| I2C, SPI, FIFO | entry 6:115 (diagram), 149 | entry 6:149, linked to the Embedded series | Good |
| Covariance, correlation coefficient | entry 7:60 | entry 7:60 | Good |
| Laplace transform, s-domain transfer function | entry 7:357 | entry 7:357 | Good (previous review's correction holds) |
| Chi-square distribution | entry 7:296 | entry 7:296 | Good |
| Kalman filter | entry 7:268 | robotics state-estimation entry, linked at 7:268 and 7:454 | Good |

No concept is used before it is introduced or referred to.

## Versions, defaults and conventions

| Assumption | Where it appears | Stated in the text? | Assessment |
|---|---|---|---|
| SI units; VIM/GUM vocabulary | all entries | overview:20; entry 1:20, 34 | Stated (see S6 on "throughout") |
| Temperature for noise: 300 K | entries 5, 6 | overview:20; entry 5:24 | Stated (see S3 on wording) |
| RMS for unqualified noise | entry 5 | entry 5:24 | Stated |
| Converter unipolar, 0 to $V_\text{ref}$, $q = \text{FSR}/2^N$, mid-tread rounding | entry 4 | entry 4:24, 87, 95 | Stated |
| Python 3.13, NumPy 2.5 | entry 7 code | entry 7:20; overview says "Python 3 with NumPy" | Stated |
| Angles: degrees in prose, radians in code | entry 7 | entry 7:20 | Stated |
| Tilt sign convention (rotation about −y; gyro y reading negated) | entry 7 §7.1 | entry 7:345 | Stated |
| Tensile strain positive | entry 3 §2.2 | entry 3:86 | Stated |
| Mains 50 or 60 Hz | entries 3, 4, 5 | entry 3:206, entry 5:133 | Stated |
| Standard gravity $g_n$ vs local g | entry 7 §4.2 | entry 7:222 | Stated |
| Edition of IEC 60751 coefficients | entry 1 §3.1 | entry 1:86, ref 243 | Stated (F4 on the parenthetical) |
| Callendar–Van Dusen range 0–850 °C (quadratic form) | entry 1:80 | yes | Stated |

## Series design

**Purpose, audience and scope.** The rewritten overview states the reader (basic circuit analysis, calculus, elementary statistics), what the series follows (a measurand to a trustworthy number) and the objectives. Entries also rely on basic linear algebra (entry 7) and complex frequency (entry 3 §6, entry 7 §7.2). Linear algebra is in the site-wide default reader of standards 2.2, and entry 7 introduces the Laplace domain where it uses it, so no finding. Scope limits are implicit in the chain; the "output" stage of entry 1's chain is not treated by any entry. Entry 1 already words this neutrally ("Later entries take up these stages in turn"), as the earlier review noted.

**Sequence and rationale.** The order is the order of the measurement chain, and the overview now says so. Entry 1 supplies the vocabulary, entries 2–5 follow the signal stage by stage, entry 6 shows the integrated chain and entry 7 closes with calibration and fusion. This is the right order for the stated reader. Entry 7 is long (about 5,800 words of prose) because it carries two outcomes, but each section serves objective 5. Splitting it is not needed.

**Prerequisites and dependencies.** Every backward dependency is explicit and linked: entry 3 reuses entry 2's strain gauge, photodiode and quartz numbers; entry 4 reuses entry 3's channel; entry 5 reuses entries 3 and 4; entry 7 reuses entries 1, 3, 5 and 6. Outward links depend on the Foundations of Control Systems series (entry 1 §4) and on the robotics state-estimation entry, whose fragments `#4-…`, `#5-the-kalman-filter`, `#71-…` and `#8-…` were checked against the current working tree of that file. Nothing depends on a later entry.

**Notation and depth.** Notation is consistent apart from T1, the figure label. $s$ has several meanings, each disambiguated where used (entry 7:357). $f_c$ means only the filter cut-off once T1 is fixed. $q$ is used for both the quantization step (entry 4) and the elementary charge (entries 2, 5, 6), but each use is defined in its own entry and they never meet in one formula. Depth is comparable: every entry has worked numbers and a summary table, and only entry 7 has code, which the overview states.

**Overview completeness.** The page now has the parts that standards 6.5 requires: sequence rationale, how entries connect, the two running examples and the shared conventions. Every statement about the running examples was checked against the entries: PT100 in entry 1 §3, entry 3 §1 and §1.1, and entry 7 §3.4; load cell in entry 3 §7, entry 4 §3.4, entry 5 §6.1 and entry 7 §3.2. The page has three wording defects (S1, S3, S6) and makes no promise that the entries do not keep.

## Series-level notes

- **Cross-reference map.**
  - Every "previous", "next", "first", "fourth" and "last" entry reference resolves to the right article.
  - Section references were checked against the target headings: entry 5 → entry 3 §6, entry 2 §7.1; entry 6 → entry 2 §2.2, entry 3 §2.2, entry 5 §2.1, entry 4 §5.2; entry 7 → entry 1 §3.4, §5, §5.3, §6, entry 3 §7, entry 5 §4, §6.1, entry 6 §3.2, §4.2, §4.3, entry 4 §5.2.
  - Promises are fulfilled: quantization in entry 4, calibration in practice in entry 7, anti-aliasing in entry 4, noise bandwidth in entry 5 §1.3, dither in entry 5 §4, fusion and time alignment in entry 7.
  - Entry 5's quotation of entry 1 ("but noise usually limits it first") matches entry 1:110 exactly.
- **Consistency of shared values.** The values that recur across entries agree everywhere:

  | Value | Uses |
  |---|---|
  | PT100 slope 0.385 Ω/°C | entries 1, 3 |
  | Self-heating 0.14 mW | entries 1, 3 |
  | Strain-gauge numbers (K = 2, 1000 µε, 350 Ω, 0.7 Ω) | entries 2, 3, 5 |
  | Photodiode 0.55 µA | entries 2, 3, 5 |
  | Quartz 23 pC → 0.23 V | entries 2, 3 |
  | Type K 41 µV/K | entries 2, 3 |
  | Load cell 6.6 mV full scale, 0.9 of range | entries 3, 4, 5 |
  | Noise 0.11 g RMS | entries 5, 7 |
  | Thermometer budget 0.016 / 0.050 / 0.003 °C | entries 1, 7 |
- **Structure and tone.** All seven entries now have numbered sentence-case sections, a question/answer Summary table with a forward transition (entry 7 closes against the objectives), and `### References` in house format. Descriptions follow the noun-clause pattern ("What …", "How …") used across the site. This is not reported, because it is a site-wide pattern.
- **Vietnamese translations.** Not reviewed, per the skill. Note for resolution: the wave-1 English changes have not yet reached `src/content/blog/vi/` or `src/content/series/vi/sensor-systems.md` (last changed in f1ca0e4, before wave 1). For example, the Vietnamese entry 5 still writes the 1/f corner as $f_c$ in nine places.

## Verification log

- **Build:** `npm run build` was not run, per the brief, because other reviewers build in parallel. The current full build in `/tmp/claude-0/b2` (SITE_URL=https://acrr.asia, built after wave 1) was inspected; it contains the wave-1 text, for example "noise corner frequency" in entry 5, the new closing of entry 7 and the new overview.
  - KaTeX: `grep -c katex-error` gives 0 for all seven article pages.
  - Mermaid min-width: entry 1 142px, entry 6 437px, entry 7 142px and 323px. All are below 600px.
  - Glued inline text: grep for a letter or punctuation mark immediately before `<strong>`, `<code>`, `<a ` or `<span class="badge` finds 0 cases in the seven pages and the series page.
- **Link check:** `node scripts/check-links.mjs /tmp/claude-0/b2`: "Checked 314 pages and 9667 internal references … All internal links resolve."
- **Lint:** `npm run -s eos -- lint sensor-systems`: 0 errors, 0 warnings, 44 suggestions. The suggestions are sentence length, acronym-expansion false positives (PT100, CMRR, FIFO, RMS, FSR, JCGM, ILAC/OIML expanded in the same sentence, TS, CRC, MIT) and three kept "very". None is re-reported.
- **Syntax:** `npm run -s eos -- syntax` on the series file and the seven articles: "All files compile."
- **Code:** all five Python blocks of entry 7 were extracted and run with Python 3.13.16 and NumPy 2.5.3 (`python3 -I`). Listings 1 and 2 were run together, as the text continues the script. All printed lines are identical to the text: calibration fit; curve inversion (m0 = 4.9927 kg, 0.054 / 0.142 / 0.181 g); fusion and chi-square (weights 0.581/0.163/0.255, 20.123 °C, χ² 1.61 and 19.3, z = −3.51/−0.44/+4.34); complementary-filter simulation (all nine lines); cross-correlation delay (30 ms, 0.536, 0.070).
- **Recomputed (python3 -I).** All values agree with the text.
  - Entry 1: R(100) = 138.506 Ω; slopes 0.3908 and 0.3793 Ω/°C; endpoint deviation 0.144 Ω at 50 °C, which is 0.375 °C; 1 − e^{−1,−3,−5} = 63.2/95.0/99.3%; settling within 1% after 4.6τ = 18.4 s ("about 20 s"); u_c = 0.0525 °C, U = 0.105 → 0.11 °C; g = 1.01317, corrected reading 50.25 °C; I²R = 0.1385 mW.
  - Entry 2: NTC 33.62 / 3.588 / 0.698 kΩ; −β/T² = −4.44%/K (11× platinum); 8.854 pF, +0.089 pF for 1 µm; 0.7 Ω and 0.2%; 23 pC → 0.23 V; e^{−10} = 0.0045%; responsivity 0.548 A/W; Nernst slope 59.16 and 61.54 mV.
  - Entry 3:
    - Quarter bridge 2.4975 mV, relative error x/2 = 0.1%; half and full bridge outputs re-derived from the bridge equation; balance condition R1R4 = R2R3 re-derived.
    - Op-amp numbers: 40% offset error; GBW 10 kHz; CMRR 250 µV / 25 µV; 0.1% resistors → (1+G)/(4ε) = 500 = 54.0 dB.
    - Amplifier and converter interface: R_G = 50.05 Ω; ±2.5 mV × 600 around 1.65 V → 0.15–3.15 V; transimpedance cut-off 159 kHz; charge amplifier 1 s and 0.159 Hz.
    - Filters: RC cut-off 9.947 Hz; Butterworth at 50 Hz: 0.196/0.0400/0.0016, i.e. 14.15/27.97/55.92 dB; at 3 Hz: 0.958/0.996/0.99997.
    - Load-cell channel: 6.6 mV × 450 = 2.97 V; ratiometric fraction 0.9.
  - Entry 4: 76.34 dB vs 72.25 dB; q = 0.806 mV / 50.35 µV / 0.197 µV; u_q = 0.233 mV; SQNR 74.0 / 98.1 dB; ENOB 13.99; jitter limits 38.9 ns and 0.121 ns; 3686 / 58 982 codes → 2.71 / 0.170 g; SAR trace: truncating code 9, rounding (thresholds kq − q/2) code 10.
  - Entry 5:
    - Gaussian bounds: P(|Z| < 3.3) = 99.90%; P(Z > 3) = 1/741.
    - Combination and filters: a source one third of the largest adds 5.4%; ENBW π/2, 1.111, 1.026.
    - Fundamental sources: thermal 4.07 / 2.41 nV/√Hz; kT/C 64.4 µV; shot 0.420 pA/√Hz, resistor 0.129 pA/√Hz, total 0.220 nA in 251 kHz, SNR 2499 (68.0 dB).
    - 1/f example: 67.86 + 31.46 → 74.8 nV.
    - Amplifier noise: 10.29 nV/√Hz; 1 µV/√Hz for 10 MΩ.
    - Dither: the bias of Gaussian dither was computed exactly (sum over codes): maximum 0.093 q for σ = 0.25 q and 0.0023 q for σ = 0.5 q, which confirms "about 0.09 q" and "below 0.01 q". Per-sample error 0.577 q, /16 → q/27.7.
    - Interference: 72.3 nA, 3.18 GΩ, 72 mV, 25.3 µV; 3.14 µV peak, 2.2 µV RMS.
    - Noise budget: total 75.2 nV → 0.114 g; 0.75 g peak-to-peak; 87 785 = 16.42 bits = 98.9 dB; noise-free 13 300 = 13.70 bits.
  - Entry 6: x = 9.94 nm/g; ΔC = 0.994 fF/g; a_n = 7.21 × 10⁻⁴ m/s²/√Hz = 73.6 µg/√Hz, 0.736 mg in 100 Hz, 7.3 pm, 0.73 aF; Coriolis 1.257 m/s → 0.0439 m/s² = 4.47 mg; ΔV_BE 53.8 mV and 0.179 mV/K; scaling k ∝ s, ω₀ ∝ 1/s re-derived; differential-capacitor cubic residual x²/d² re-derived.
  - Entry 7:
    - Uncertainty: reference-ratio penalties 3.08 / 11.8 / 0.50%; t(4 dof, 95%) = 2.78 → U = 0.39 g.
    - Calibration fit: offset 10.56 g; sensitivity −0.066%; s/b = 0.132 g; PT100 least-squares residuals −0.077, +0.015, +0.062, +0.062, +0.015, −0.077 Ω (0.200 °C).
    - Six-position test: 0.0745 m/s² = 7.60 mg; scale factor 1.00121; gravity error 0.26–0.27%; 1 − cos 1° = 0.015%.
    - Gyroscope bias: 0.1/√1000 = 0.0032 °/s; Earth rotation 15.04 °/h = 0.0042 °/s.
    - Calibration interval and correlated sensors: 2.67 years; correlated mean 0.0513 °C vs 0.0375 °C.
    - Complementary filter: discrete form re-derived from τθ̂′ = τω + θ_a − θ̂ by backward difference (α = τ/(τ+Δt) = 0.990); final value b_ω τ re-derived; steady-state angle-only Kalman update re-derived as α = 1 − K.
    - Time alignment: 25.1 °/s → 0.25° per 10 ms; 50 ppm → 0.18 s per hour.
    - T2: 1/f noise of one-second averages over a 10-minute span is 75.5 nV (see T2).
- **Fact-check:**

  | Claim | Location | Status | Source |
  |---|---|---|---|
  | Gabrielson 1993, IEEE Trans. Electron Devices 40(5):903–909 | entry 6 ref | Verified | Penn State research portal record (May 1993) |
  | IEEE 1241-2010 dates; superseded by 1241-2023 | entry 4 ref | Verified; superseded (F3) | standards.ieee.org pages for 1241-2010 and 1241-2023 |
  | IEC 60751:2022 title, edition 3.0, 2022-01-27 | entry 1 ref | Verified | IEC webstore publication 63753 |
  | 2008 and 2022 coefficients identical | entry 1 ref | Not verified (F4) | IEC 60751:2022 preview (α only) |
  | JCGM 100:2008, JCGM 200:2012 titles; both current | entries 1, 7 refs | Verified | BIPM JCGM publications page. JCGM uses a hyphen in the titles; the en dash follows the house example in standards 7.3. |
  | ISO/IEC 17025:2017 current | entry 7 ref | Verified | iso.org/standard/66912 (confirmed 2023) |
  | ISO/TS 28037:2010 withdrawn | entry 7 | Corrected (F1) | iso.org/standard/44473 and 84405 |
  | ILAC-G24/OIML D 10 edition; staircase and control-chart methods | entry 7 | Superseded (F2); methods verified | OIML D 10:2022 PDF |
  | Johnson–Nyquist noise, 1928 | entry 5:62 | Verified | Johnson, Phys. Rev. 32, 97 (1928), DOI 10.1103/PhysRev.32.97; Nyquist, Phys. Rev. 32, 110 (1928), DOI 10.1103/PhysRev.32.110 |
  | Type K ≈ 41 µV/K; 100 K → 4.1 mV | entries 2, 3 | Verified | ITS-90 type K table (Minco): 4.096 mV at 100 °C; slope 40.5 µV/K at 20–30 °C |
  | Quartz ≈ 2.3 pC/N; PZT one to two orders larger | entry 2:126 | Consistent | Wiley-VCH sample chapter (ISBN 3527351892), Table 1.1: α-quartz ~2 pC/N, PZT 200–400 pC/N |
  | Silicon Young's modulus 130–190 GPa | entry 6:30 | Partly verified | Boyd and Uttamchandani, J. MEMS 21(1):243–249, 2012: 131–170 GPa in the (100) plane |
  | Books: Bentley 4th ed. Pearson 2005; Regtien and Dertien 2nd ed. Elsevier 2018; Webster and Eren 2nd ed. CRC 2014; Pallàs-Areny and Webster 2nd ed. Wiley 2001; Franco 4th ed. McGraw-Hill 2015; Kester Newnes 2005; Motchenbacher and Connelly Wiley 1993; Ott Wiley 2009; Kaajakari Small Gear 2009; Senturia Kluwer 2001; Fraden 5th ed. Springer 2016; Taylor 2nd ed. University Science Books 1997 | refs | Existence and edition verified | Publisher and library catalogue listings found by search |
  | Horowitz and Hill 3rd ed. CUP 2015; Oppenheim and Schafer 3rd ed. Pearson 2010; Thrun, Burgard and Fox, MIT Press 2005 | refs | Not looked up in this session | Standard editions |
- **Not verified:**
  - IEC 60751:2008 and :2022 giving identical A and B (F4). The 2022 standard is paywalled; only its α = 3.851 × 10⁻³ °C⁻¹ was seen, and it is consistent.
  - Fraden's use of "active" for sensors that need excitation (entry 1:70). The book was not accessible here; this point was established by the previous review and was not re-verified.
  - KOH (100)/(111) etch-rate ratio "of orders of magnitude" (entry 6:38). This is consistent with the commonly reported ratios of the order of 100:1 or more, but no primary source was fetched.
  - The upper end (≈188 GPa, ⟨111⟩) of the silicon modulus range and the piezoresistive gauge factor "of the order of 100" (entry 6:30, 32). These typical values are uncited; no source was fetched.
  - The bibliographic details of Horowitz and Hill, Oppenheim and Schafer, and Thrun et al. were not looked up online in this session.

## Resolution

- T1 (Should fix): fixed - `scripts/generate-diagrams.py:436-437, 451, 456` now use `f_nc` (comment and label `'corner ' + sub('f', 'nc')`); regenerated to a scratch directory, only `NoiseDensity.astro` differed, installed as `src/components/diagrams/NoiseDensity.astro:36` ("corner f_nc = 10 Hz"). The Vietnamese entry 5 uses the same component.
- T2 (Should fix): fixed - `calibration-and-multisensor-fusion.mdx:145` takes the reviewer's wording, split into two sentences for length. Recomputed (python3 -I, entry-5 model): 1/f part over 1/600 to 0.5 Hz = 75.5 nV, white part 7.1 nV, total 75.9 nV vs the 74.8 nV budget.
- S1 (Should fix): fixed - "in a single package" at `sensor-systems.md:16`; "in one package" at `noise-interference-and-limits-of-detection.mdx:213` and `calibration-and-multisensor-fusion.mdx:535`; "in the same package" at `smart-sensors-and-mems.mdx:82` and also at line 77 ("needs its electronics in the same package"), which preceded it with "on the chip". The heading "4. The electronics on the chip" and the other "on-chip" uses in entry 6 were kept (they describe the ASIC's own circuitry, and the heading anchor is stable).
- S2 (Should fix): fixed - `sensing-principles.mdx:166` now reads "the joint encoders described in the [first entry](/blog/what-is-a-robot) of the robotics series"; that article describes joint encoders (§ on proprioceptive sensors).
- S3 (Should fix): fixed - `sensor-systems.md:20`: "Noise voltages and currents are root-mean-square values, computed at 300 K unless stated otherwise."
- F1 (Should fix): fixed - `calibration-and-multisensor-fusion.mdx:202` and reference line 544 now cite ISO 28037:2026 (verified on iso.org/standard/84405: published 2026-07, stage 60.60, replaces the withdrawn ISO/TS 28037:2010, abstract covers non-negligible errors in both variables and general covariance).
- F2 (Should fix): fixed - reference at `calibration-and-multisensor-fusion.mdx:542` is now ILAC-G24:2022 / OIML D 10:2022, *Guidelines for the determination of recalibration intervals of measuring equipment* (verified in oiml.org d010-e22.pdf: foreword says it supersedes the 2007 edition; methods 6.2 "staircase" and 6.3 "control chart" present). Body text unchanged.
- F3 (Should fix): fixed - reference at `sampling-quantization-and-data-conversion.mdx:223` is now IEEE Std 1241-2023, same title, IEEE, 2023 (verified on standards.ieee.org/ieee/1241/6797: Active, published 2023-10-06). Body text names no edition and is unchanged.

Optional findings applied: F4 (parenthetical removed from `measurement-systems-and-sensor-characteristics.mdx:243`; the identity of the 2008 coefficients could not be verified from an edition-specific primary source, so the claim was dropped rather than qualified), S4 (`signal-conditioning.mdx:80`, `$x/2 = 0.1\%$`), S5 (`measurement-systems-and-sensor-characteristics.mdx:104`, "relative to the endpoint line"), S6 (`sensor-systems.md:20`, units sentence as recommended, split from the VIM/GUM sentence), S7 (`calibration-and-multisensor-fusion.mdx:535`, as recommended). Optional findings not applied: none.

Checks: no heading changed, so the fragments other pages link to (`#21-oversampling`, `#32-quantization-error-as-uncertainty`, `#52-evaluating-uncertainty`) and the links into `sensing-and-state-estimation` are unchanged. `eos lint` on the series file and seven articles: 0 errors, 0 warnings, 44 suggestions; `eos syntax`: all files compile. No code output changed. No build was run (per brief). Vietnamese: no copied field changed; the meaning changes in the overview (S1, S3, S6) and entries 5 and 6 (S1) are left for the translation follow-up, together with the nine $f_c$ for the 1/f corner in the Vietnamese entry 5.

Resolved by the wave-1 author on 2026-10-15; awaiting the reviewer's resolution check.
