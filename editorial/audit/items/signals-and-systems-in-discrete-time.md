<!-- audit: {"slug":"signals-and-systems-in-discrete-time","type":"article","series":"digital-signal-processing","priority":"P1","before":{"purpose":4,"structure":3,"accuracy":4,"evidence":3,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":1,"shouldFix":6,"optional":4}} -->
# Audit: Signals and Systems in Discrete Time

- Path: `src/content/blog/signals-and-systems-in-discrete-time.mdx` · Route: `/blog/signals-and-systems-in-discrete-time` · Type: article (series entry) · Series `digital-signal-processing`, entry 1 of 5 · Words: 3389 (`eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 4
- structure 3: the conventions block sits under a level-3 heading directly after the title (no level-2 parent), so the page outline is broken; otherwise the progression (signals, systems, difference equations, convolution, properties, frequency response) is exemplary.
- accuracy 4: both Python blocks rerun (Python 3.13.16, NumPy 2.5.3), outputs byte-identical; key numbers recomputed (below).
- evidence 3: references are real and appropriate but not in house format ("3rd edition" instead of "3rd ed.").
- language 3: British "analogue" and "towards" against the American house variant; "simply", "easily checked"; "95 %" with a space.
- consistency 3: spelling variant and title-case headings differ from the house style now adopted for the site.
- publishing 2: one lint error (heading-levels), description 271 characters, five title-case headings.

## Priority

P1: first (foundational) entry; its conventions anchor `#conventions-used-throughout-the-series` is linked from all four later entries, and it has the series' only lint error.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Blocking | `:27`, "Conventions used throughout the series" | publishing | Level-3 heading directly after the page title (h1 → h3), lint `heading-levels` error. |
| P2 | Should fix | `:3`, front matter | publishing | Description is 271 characters and a list of sections, not one sentence of what the reader learns. |
| C1 | Should fix | `:42`, `:88`, `:132`, `:190`, `:282`, `:306` | consistency | Section headings in title case ("1. Discrete-Time Signals", "4. Impulse Response and Convolution"). |
| C2 | Should fix | `:15`, `:48`, `:162` | language | British spellings "analogue", "towards"; house variant is American (standards 5.1). |
| C3 | Should fix | `:180`, `:270`, `:427`, `:432` | language | "95 %": standards 5.5 require no space before %. |
| C4 | Should fix | `:453–455` | evidence | References use "3rd edition", "2nd edition", "4th edition"; house format is "3rd ed." (standards 7.3). |
| D1 | Should fix | `:40` | structure | The opening's conventions paragraph and the series list are good, but the conventions table needs a level-2 parent for the outline; it is also the only anchor later entries cite. |
| C5 | Optional | `:202` | language | "its impulse response is simply its coefficient list": intensifier. |
| C6 | Optional | `:180` | language | "which is easily checked by substitution": talks down (standards 2.2). |
| C7 | Optional | `:22–25` | consistency | Link text in the series list uses sentence case ("The z-transform, poles and stability") while the closing paragraph and other entries use the published titles. |
| C8 | Optional | `:15`, `:117` | language | Sentence of 51 words in the opening paragraph (`sentence-length` suggestion). |

### P1. Heading-level jump
- **Where:** `src/content/blog/signals-and-systems-in-discrete-time.mdx:27`
- **Text:** "### Conventions used throughout the series"
- **Problem:** The first heading in the body is level 3, so the rendered outline jumps from the `<h1>` title to `<h3>` (standards 5.4; lint `heading-levels` error). The table of contents also shows it as a sub-item of nothing.
- **Correction:** Make it a level-2 heading, "## Conventions used throughout the series". The slug, and therefore the four inbound links from entries 2–5, stay the same.

### P2. Description
- **Where:** `:3`
- **Text:** "The foundation of digital signal processing: sequences and discrete-time frequency, the properties that define linear time-invariant systems, difference equations, the impulse response and convolution, stability in the time domain, and a first look at frequency response."
- **Problem:** 271 characters (limit 165); a list of every section, which standards 8.1 rules out.
- **Correction:** One sentence of 70–165 characters stating what the reader learns.

### C1. Title-case headings
- **Where:** six level-2 headings, e.g. `:282` "5. Reading Properties from the Impulse Response", `:306` "6. Response to Sinusoids: a First Look at Frequency Response".
- **Problem:** House style is sentence case (standards 5.4). Changing only case keeps the slugs, so the internal links at `:60`, `:68`, `:117` still resolve.
- **Correction:** "1. Discrete-time signals", "2. Discrete-time systems", "3. Difference equations", "4. Impulse response and convolution", "5. Reading properties from the impulse response", "6. Response to sinusoids: a first look at frequency response".

### C2. British spellings
- **Where:** `:15` and `:48` "analogue-to-digital converter"; `:162` "towards the new input".
- **Problem:** Standards 5.1 adopt American spelling ("analog" is listed explicitly). The previous series review (F2) had moved the series to British spelling before the house standard was adopted; this reverses that choice by policy, not as a correction of fact.
- **Correction:** "analog-to-digital converter", "toward".

### C3. Space before percent sign
- **Where:** `:180` "95 % of the final value"; `:270`, `:427`, `:432`.
- **Correction:** "95%".

### C4. Reference format
- **Where:** `:453–455`
- **Text:** "*Discrete-Time Signal Processing*, 3rd edition, Pearson, 2010."
- **Correction:** "3rd ed.", "2nd ed.", "4th ed." (details already verified by the series review: Oppenheim and Schafer 3rd ed. 2010; Oppenheim, Willsky and Nawab 2nd ed. 1997; Proakis and Manolakis 4th ed. 2007).

### D1. Conventions block placement
- **Where:** `:27–40`
- **Problem:** See P1; the opening otherwise meets standards 6.2 (what the entry covers, prerequisites with a link, versions Python 3.13 and NumPy 2.5). No restructuring beyond the heading level is needed.
- **Correction:** As P1.

### C5–C8
- C5 `:202`: "is simply its coefficient list" → "is its coefficient list".
- C6 `:180`: "which is easily checked by substitution:" → "as substitution confirms:".
- C7 `:22–25`: use the published titles as link text ("The z-Transform, Poles and Stability", "Spectra: The DFT and the FFT", "Designing FIR and IIR Filters", "From Signal Processing to Digital Control").
- C8 `:15`: split the 51-word last sentence of the opening paragraph.

### Accuracy spot-checks (no defect found)
- Both Python blocks extracted and run with `python3 -I` (Python 3.13.16, NumPy 2.5.3): outputs identical to the article.
- Step-response threshold $\ln 0.05/\ln 0.9 = 28.43$, so $n = 28$; $\tau = -0.01/\ln 0.9 = 94.9$ ms; smoother at $0.1\pi$: $|H| = 0.319$, phase $-62.6°$; gain at $\pi$: $0.0526$ (factor 19); Exercise 5: $59.9$, $n = 59$. All match.
- The $a = 1$ statement corrected by the previous review (F1) is right as now worded.

## Revision log (wave 1)
- Structure: "Conventions used throughout the series" raised from level 3 to level 2 (fixes the h1 → h3 jump, P1/D1). Slug unchanged, so the four inbound links from entries 2–5 still resolve. No reordering was needed.
- Prose: opening sentence of 51 words split; "which is easily checked by substitution" → "as substitution confirms"; "is simply its coefficient list" → "is its coefficient list"; the last sentence of the opening rewritten as two sentences with the same content.
- Terminology/style: "analogue" → "analog" (2), "towards" → "toward"; "95 %" → "95%" (4); six section headings to sentence case (case only; slugs unchanged); link text of the series list now uses the published titles.
- Metadata: description replaced (271 → 161 characters): "How sampled signals and linear time-invariant systems behave: frequency in radians per sample, difference equations, impulse response, convolution and stability."
- References: "3rd/2nd/4th edition" → "ed."; order already alphabetical.
- Cross-references: none renumbered or renamed.
- Technical corrections: none needed. Both Python blocks rerun after editing (Python 3.13.16, NumPy 2.5.3): output identical.
- Remaining warnings and why they stay: `heading-numbering` at `:27` (unnumbered "Conventions used throughout the series" before numbered sections). It is front matter for the whole series, the target of `#conventions-used-throughout-the-series` from entries 2–5; numbering it would renumber every section of the entry and every "Section N" reference to it, and demoting it to a paragraph would remove the anchor. Suggestions kept: `acronym-expansion` at `:23–24` (DFT, FFT, FIR, IIR appear first in the published titles used as link text, and each is expanded later in the same list item).
- Flags for independent review: none technical. Fact-check: the reference details were verified by the earlier series review and only reformatted here.
- Vietnamese translation affected: no translation of this article exists.

## Independent review (wave 2)
- Report: `reviews/digital-signal-processing.md` (reviewed commit 49941d2, 2026-10-14).
- Fact-check: pass (references exist; editions accepted from the earlier review).
- Technical: fail. Findings: T1 (blocking: §6.2 :377, the 60 Hz gain at 150 Hz is 0.21, not "almost untouched", and $f_s$ a multiple of 50 Hz is not sufficient), S1 (should fix: prerequisite paragraph :17), S4 (optional: :276 "shows" → "notes").
- Code: both blocks rerun, outputs identical.
- Not verified: book editions (Oppenheim and Schafer 2010; Oppenheim, Willsky and Nawab 1997; Proakis and Manolakis 2007) not re-checked in this pass.

## Revision log (wave 2 resolution)
- Date: 2026-10-15. Report: `reviews/digital-signal-processing.md`, section Resolution.
- Changes: T1 fixed at :377 (60 Hz gain 0.21 at 150 Hz; $N$-point average removes interference when $f_s = N$ times its frequency; recomputed). S1 fixed at :17 (Laplace transform, $s$-plane poles and feedback vocabulary added to the prerequisites, linking Introduction to Control Systems). S4 applied at :276 ("shows" to "notes"). Anchor `#conventions-used-throughout-the-series` unchanged. No code changed.
- `eos lint`: 0 errors; the only warning in the series is entry 1's justified `heading-numbering`. `eos syntax`: pass.
