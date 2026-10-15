<!-- audit: {"slug":"noise-interference-and-limits-of-detection","type":"article","series":"sensor-systems","priority":"P2","before":{"purpose":4,"structure":3,"accuracy":4,"evidence":3,"language":3,"consistency":2,"publishing":2},"findings":{"blocking":0,"shouldFix":5,"optional":3}} -->
# Audit: Noise, Interference and the Limits of Detection

- Path: `src/content/blog/noise-interference-and-limits-of-detection.mdx` · Route: `/blog/noise-interference-and-limits-of-detection` · Type: article · Series `sensor-systems`, entry 5 of 7 · Words: 3230
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- structure 3: opening paragraph 3 is a prose outline ("The entry first introduces ..., then ..., then ..., It then turns to ..., and ends by ...").
- evidence 3: references not in house format. The "1928" date for Johnson and Nyquist is correct (both papers in *Phys. Rev.* 32, 1928) but uncited; flagged for the fact-checker.
- language 3: seven title-case H2s; "%" spacing; "the fact that" (line 36); a 62-word sentence on ground-loop remedies (line 139).
- consistency 2: the symbol $f_c$ means the filter cut-off frequency in §1.3 (and in the signal-conditioning entry) and the 1/f corner frequency in §2.3 (line 86 "the **corner frequency** $f_c$", line 96 "$e_w\sqrt{f_c \ln(f_2/f_1)}$"), two different quantities in one article. The previous entries are referred to as "the sensing-principles entry", "the signal-conditioning entry" without links.
- publishing 2: description 302 characters.

Accuracy recomputed: thermal noise 4.07 / 2.41 nV/√Hz; kT/C 64.4 µV; shot 0.420, resistor 0.129 pA/√Hz, total 0.220 nA, SNR 2505 (68.0 dB); 1/f 67.9 nV, white 31.5 nV, bridge 7.58 nV, total 75.2 nV = 0.114 g; 87 785 counts = 16.42 bits = 98.9 dB; noise-free 13 300 (13.70 bits); 72.3 nA, 3.18 GΩ, 25.3 µV; 3.14 µV peak. All correct.

## Priority

P2.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 302 characters. |
| P2 | Should fix | H2 headings | language | Title case. |
| D1 | Should fix | lines 86–101 | consistency | $f_c$ used for two quantities. |
| P3 | Should fix | References | evidence | House format, alphabetical. |
| D2 | Should fix | lines 17, 56, 82 | consistency | Earlier entries named without links at first mention. |
| D3 | Optional | line 24 | structure | Prose outline. |
| C1 | Optional | line 36 | language | "The odd unit comes from the fact that". |
| C2 | Optional | line 139 | language | 62-word sentence. |

### D1. One symbol, two meanings
- **Text:** "It is described empirically by the **corner frequency** $f_c$ at which its density equals the white noise floor $e_w$" against §1.3 "the filter's cut-off frequency $f_c$".
- **Correction:** Write the 1/f corner as $f_\text{nc}$ in §2.3 (equation, integral, worked numbers). The NoiseDensity diagram does not use the symbol, so no regeneration is needed.

### P1. Description
- **Correction:** "Learn what limits the smallest detectable change: thermal, shot and flicker noise, amplifier noise, averaging and dither, interference, and a full noise budget." (161)

## Revision log (wave 1)
- Consistency/technical notation: the 1/f corner frequency is now $f_\text{nc}$ ("noise corner frequency", bold at definition) in §2.3 (definition, equation, integral, worked numbers), so $f_c$ means only the filter cut-off, as in §1.3 and the signal-conditioning entry. Numbers unchanged; the NoiseDensity diagram uses no symbol, so no regeneration.
- Structure: opening outline condensed; the ground-loop paragraph rewritten as a short mechanism plus three remedies.
- Prose/style: seven H2s to sentence case; "%" spacing; "the fact that" removed; "very low current noise" → "low"; "extends down to very low frequencies" → "extends down towards DC"; RC expanded.
- Metadata: description 158 characters.
- References: house format, alphabetical.
- Cross-references: links to the first, previous, sensing-principles (§7.1), signal-conditioning (§6) and next entries.
- Remaining warnings: none. Suggestions: RMS at line 28 (the heading uses the abbreviation; the body expands it at first use), sentence length at 82 and 196.
- Flags for independent review: fact-check "Johnson–Nyquist noise, after the two physicists who measured and explained it in 1928" (Phys. Rev. 32, 1928; uncited in the entry).
- Vietnamese translation affected: yes: the symbol change $f_c \to f_\text{nc}$ in §2.3 must be copied into the Vietnamese math; description, opening, ground-loop paragraph and "towards DC" wording.

## Revision log (wave 2 resolution)

Date: 2026-10-15. Resolves `reviews/sensor-systems.md`.

- T1: the NoiseDensity figure label now reads f_nc (generator `scripts/generate-diagrams.py` and regenerated `src/components/diagrams/NoiseDensity.astro`; only that component changed).
- S1: "built together on one chip" -> "in one package" (line 213).
- Vietnamese follow-up: S1 wording; the Vietnamese entry still writes the 1/f corner as $f_c$ in its prose (nine places), now inconsistent with the shared figure.
- Lint: 0 errors, 0 warnings; syntax: compiles.
