<!-- audit: {"slug":"digital-signal-processing","type":"series","series":"digital-signal-processing","priority":"P2","before":{"purpose":3,"structure":3,"accuracy":4,"evidence":4,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":4,"optional":2}} -->
# Audit: Digital Signal Processing for Engineers (series overview)

- Path: `src/content/series/digital-signal-processing.md` · Route: `/series/digital-signal-processing` · Type: series overview · 5 entries, status published · Words: 105 (`eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 3: audience and prerequisites are stated, but the prerequisite "the sensor series" is not named or linked.
- structure 3: one paragraph; the sequence rationale (why time domain, then z-domain, then spectra, then design, then control) is implicit; the shared conventions are not mentioned.
- accuracy 4: every claim in the body matches the entries.
- evidence 4: n/a for an overview (no claims needing sources).
- language 3: British "analyses"; 53-word sentence; DFT, FFT, FIR, IIR not expanded.
- consistency 3: "analyses" against the American variant of the objectives ("analyze", "discretize").
- publishing 2: description 211 characters.

## Priority

P2.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 211 characters. |
| D1 | Should fix | `:14` | structure | No sequence rationale or account of how the entries connect (standards 6.5); no mention of the shared conventions table in entry 1. |
| D2 | Should fix | `:14` | purpose | "the idea of sampling that the sensor series introduces": the series and entry are not named or linked. |
| C1 | Should fix | `:14` | language | "analyses" (British); DFT, FFT, FIR and IIR not expanded; 53-word sentence. |
| C2 | Optional | `:7–11` | language | Objectives begin "Use" and "Treat", weaker than the assessable verbs standards 6.5 suggest; each is covered by an entry (see the series audit), so the wording is acceptable. Not changed, because the Vietnamese objectives would have to change with them. |
| C3 | Optional | `:2` | publishing | Title "Digital Signal Processing for Engineers" is fine (40 characters, headline style). |

### D1/D2/C1. Body
- **Correction:** rewrite the body as two or three short paragraphs: reader and prerequisites (with a link to *Sampling, Quantization and Data Conversion*), the sequence and why, and the shared conventions (entry 1's table; Python 3 and NumPy).

### P1. Description
- **Correction:** one sentence of 70–165 characters.

## Revision log (wave 1)
- Structure: body rewritten from one paragraph into three: reader and prerequisites (now naming and linking *Sampling, Quantization and Data Conversion* and the Sensor Systems series), the sequence and why each entry uses the one before, and the shared conventions of entry 1's table (D1, D2).
- Language: "analyses" removed (American variant); DFT, FFT, LTI, FIR and IIR expanded; 53-word sentence gone; no serial comma.
- Metadata: description replaced (211 → 146 characters): "How to analyze sampled signals and systems with the z-transform and the DFT, design digital filters and carry the same tools into digital control."
- Objectives: unchanged (C2 left as optional; changing them would require the Vietnamese objectives to change too).
- Remaining warnings: none. Suggestion kept: `acronym-expansion` IIR at `:16`, a false positive (expanded in the same phrase, "finite and infinite impulse response (FIR and IIR)").
- Flags for independent review: series editor: confirm that "each uses the tools of the one before" is a fair description of entry 3, which relies on entry 2 only for the DTFT definition.
- Vietnamese translation affected: yes. `src/content/series/vi/digital-signal-processing.md` should be updated: the English description was shortened and rephrased (same scope), and the body now names and links the prerequisite entry, explains the order of the entries, and mentions the shared conventions table. Objectives and copied fields are unchanged, so the build pairing is unaffected.
