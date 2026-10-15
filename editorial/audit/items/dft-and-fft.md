<!-- audit: {"slug":"dft-and-fft","type":"article","series":"digital-signal-processing","priority":"P2","before":{"purpose":4,"structure":4,"accuracy":4,"evidence":3,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":5,"optional":5}} -->
# Audit: Spectra: The DFT and the FFT

- Path: `src/content/blog/dft-and-fft.mdx` · Route: `/blog/dft-and-fft` · Type: article (series entry) · Series `digital-signal-processing`, entry 3 of 5 · Words: 3189 (`eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 4
- structure 4
- accuracy 4: three Python blocks rerun, identical output; four-point DFT, FFT counts, exercise answers checked.
- evidence 3: five real, correctly detailed references, but commas outside the closing quotes, "3rd edition", and not alphabetical.
- language 3: "simply", "very", "clearly"; two sentences of 57 and 60 words.
- consistency 3: title-case headings.
- publishing 2: description 312 characters; heading 1.1 uses "DTFT" before it is expanded.

## Priority

P2.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 312 characters, a list of contents. |
| C1 | Should fix | `:21`, `:92`, `:107` | consistency | Title-case headings ("The Discrete Fourier Transform", "What the DFT Assumes: Periodicity", "The Fast Fourier Transform"). |
| C2 | Should fix | `:379–383` | evidence | House citation format: comma belongs inside the closing quotation mark ("title," *Journal*); "3rd edition" → "3rd ed."; order Cooley, Harris, Heideman, Oppenheim, Welch. |
| C3 | Should fix | `:23` | language | Heading "1.1 From the DTFT to a computable transform" uses the abbreviation before the text expands it at `:25`. |
| C4 | Should fix | `:294` | language | 60-word sentence that mixes the measured value, the method used to obtain it and the conclusion. |
| C5 | Optional | `:55` | language | "The DFT is simply a change of basis". |
| C6 | Optional | `:263` | language | "Windows with very low side lobes". |
| C7 | Optional | `:349` | language | "how clearly the peaks separate". |
| C8 | Optional | `:242` | language | 57-word sentence on the Hamming coefficients. |
| C9 | Optional | `:375` | language | 57-word closing sentence; "IIR" used without expansion in this article. |

### P1. Description
- **Correction:** one sentence, 70–165 characters, e.g. what the DFT computes, why the FFT is fast, and how leakage and windows shape a measured spectrum.

### C1. Headings
- **Correction:** "1. The discrete Fourier transform", "2. What the DFT assumes: periodicity", "3. The fast Fourier transform". No link targets these anchors; case change keeps slugs anyway.

### C2. References
- **Text:** `"An algorithm for the machine calculation of complex Fourier series", *Mathematics of Computation*`
- **Correction:** `"An algorithm for the machine calculation of complex Fourier series," *Mathematics of Computation*` and alphabetical order. Bibliographic details (volumes, issues, pages) were verified by the series review and are unchanged.

### C3. Abbreviation in heading
- **Correction:** "1.1 From the discrete-time Fourier transform to the DFT" (DFT is expanded in the opening at `:17`).

### C4–C9
- C4 `:294`: split into: what the 160.2 Hz bin reads, what leakage alone contributes (with the method), and the conclusion.
- C5 `:55`: "The DFT is a change of basis".
- C6 `:263`: "Windows with lower side lobes, such as the Blackman window, suit ...".
- C7 `:349`: "how well the peaks separate".
- C8 `:242`: split the parenthesis into its own sentence.
- C9 `:375`: split; "infinite impulse response" is not needed here, since the sentence does not use IIR; lint flags the summary table row at `:375`? (it refers to the next-entry title "Designing FIR and IIR Filters" in link text; acceptable, see revision log).

### Accuracy spot-checks (no defect found)
- Python blocks: identical output (Python 3.13.16, NumPy 2.5.3).
- Four-point DFT of {1, 2, 3, 4} = {10, −2+2j, −2, −2−2j}; Exercise 2 inverse gives $x[1] = 2$; Exercise 3 $524\,288$ vs $4\,294\,967\,296$, factor 8192; Exercise 1 $48\,000/65\,536 = 0.732$ Hz; Exercise 5 $|X[40]| = 512$.
- Hamming 25/46 note and the 1.75/1.78 dB explanation (previous review F10) are correct.

## Revision log (wave 1)
- Structure: none needed.
- Prose: Hamming parenthesis made its own sentence (57-word sentence); the main-lobe/side-lobe sentence in §4.2 split; the §5.2 interpretation paragraph split into four sentences (60-word and 48-word sentences); closing paragraph split; "simply" (§1.2), "very low" (§5.1), "how clearly" (Exercise 4) removed or replaced ("lower side lobes, such as the Blackman window", "how well").
- Terminology/style: three headings to sentence case; heading 1.1 "From the DTFT to a computable transform" → "From the discrete-time Fourier transform to the DFT" (abbreviation no longer used before its expansion; no link targeted the old anchor `#11-from-the-dtft-to-a-computable-transform`, checked by grep of `src/`).
- Metadata: description replaced (312 → 149 characters): "What the discrete Fourier transform computes, why the FFT makes it cheap, and how leakage, windows and scaling decide what a measured spectrum shows."
- References: commas moved inside the closing quotation marks; "ed."; alphabetical order (Cooley, Harris, Heideman, Oppenheim, Welch). Details unchanged.
- Technical corrections: none. All three Python blocks rerun: identical output.
- Remaining warnings: none. Suggestions kept: `acronym-expansion` IIR at `:375` (inside the linked title "Designing FIR and IIR Filters"), ASSP at `:381` (part of the journal name *IEEE ASSP Magazine*, which is cited as published).
- Flags for independent review: fact-check the Gauss attribution in §3.1 ("later traced back to work by Gauss that was not published in his lifetime") against Heideman, Johnson and Burrus (1984); the earlier series review recorded it as not verified.
- Vietnamese translation affected: no translation of this article exists.

## Independent review (wave 2)
- Report: `reviews/digital-signal-processing.md` (reviewed commit 49941d2, 2026-10-14).
- Fact-check: pass. Wave-1 flag resolved: Heideman, Johnson and Burrus state that Gauss's 1805 treatise "was not published in his lifetime" (published 1866); Cooley–Tukey, Harris, Heideman et al. and Welch citations confirmed.
- Technical: pass. Findings: S6 (optional: version wording :19), T2 (optional: grammar :300).
- Code: three blocks rerun, outputs identical; window table, leakage levels and exercises recomputed.
- Not verified: Harris's 1.78 dB Hamming scalloping loss (:253; table cell illegible in the scan, computation consistent).

## Revision log (wave 2 resolution)
- Date: 2026-10-15. Report: `reviews/digital-signal-processing.md`, section Resolution.
- Changes: S6 applied at :19 (code run with the versions stated in the first entry). T2 applied at :300 (scalloping-loss sentence rewritten). No code changed.
- `eos lint`: 0 errors; the only warning in the series is entry 1's justified `heading-numbering`. `eos syntax`: pass.
