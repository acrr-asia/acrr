<!-- audit: {"slug":"feedback-and-system-behavior","type":"article","series":"foundations-of-control-systems","priority":"P1","before":{"purpose":3,"structure":2,"accuracy":3,"evidence":1,"language":3,"consistency":2,"publishing":2},"findings":{"blocking":1,"shouldFix":6,"optional":2}} -->
# Audit: Feedback and System Behavior

- Path: `src/content/blog/feedback-and-system-behavior.mdx` · Route: `/blog/feedback-and-system-behavior` · Type: article (series entry) · Series `foundations-of-control-systems`, entry 2 of 5 · Words: 774 (`eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 3: good framing paragraph, but it does not link what it builds on (first entry) or state units and the Python version.
- structure 2: unnumbered sections, no Summary or References; the stabilization claim that serves objective 1 is one sentence with no example; the central result (one factor $a/(a + bk)$ sets the offset, the sensitivity and the disturbance effect) is never stated, so the two perturbation cases look like isolated numbers.
- accuracy 3: all numbers recomputed and correct (0.8; 0.833/0.769; 1.200/0.840; poles −1, −2, −5, −10). The claim "Delays ... can turn a large gain into oscillation or instability" is right but unsupported.
- evidence 1: no references; the limits section asserts without derivation or link.
- language 3: clear; "simply" (line 30, lint); "The answer is less obvious than it first looks" is a teaser.
- consistency 2: re-derives the first-order transfer function that the first entry should own; structure differs from entries 4-5.
- publishing 2: description 168 characters; `series-sections` warnings.

## Priority

P1: required sections missing; the entry carries objective 1 of the series and is referred to by three articles outside the series.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Blocking | whole file | publishing | Summary and References missing (standards 6.2) |
| D1 | Should fix | headings | structure | Sections unnumbered |
| D2 | Should fix | `:18` | purpose | Opening does not link the first entry or state conventions (units, Python 3) |
| D3 | Should fix | `:50` | structure | Feedback changing stability (objective 1) is one conditional sentence, no worked case |
| D4 | Should fix | `:92-124` | evidence | The perturbation results are not generalized: the factor $1/(1 + bk/a)$ that governs offset, sensitivity and disturbance effect is not derived |
| D5 | Should fix | `:126-130` | evidence | Limits asserted without any quantitative illustration or link (delay, saturation, noise) |
| C1 | Should fix | `:3` | publishing | Description 168 characters |
| C2 | Optional | `:30` | language | "With $a = b = 1$ this is simply $u = r$" (intensifier) |
| C3 | Optional | `:18` | language | "The answer is less obvious than it first looks." teaser sentence |

### P1. Summary and References missing
- **Where:** whole file; `eos lint` `series-sections` ×2.
- **Correction:** add a numbered Summary (table of results, closing paragraph leading to the state-space primer) and `### References` (Åström and Murray; Franklin et al.).

### D1. Unnumbered sections
- **Where:** `:20`, `:32`, `:75`, `:92`, `:126`
- **Correction:** number them, with subsections in the closed-loop section.

### D2. Opening
- **Where:** `:18`
- **Text:** "Feedback is the central idea of control engineering: measure what a system is doing ..."
- **Problem:** no link to the first entry it builds on; no statement that $x$, $u$, $r$ are in arbitrary consistent units with time in seconds, or of the Python version (previous review F17 left this open).
- **Correction:** add a second opening paragraph.

### D3. Stabilization
- **Where:** `:50`
- **Text:** "if the plant were unstable ($a < 0$, so that $x$ grows without input), any gain with $a + bk > 0$ would make the closed loop decay."
- **Problem:** objective 1 ("how feedback changes the stability ... of a system's response") deserves a worked case. Recomputed for $a = -1$, $b = 1$: open loop grows as $e^{t}$; any $k > 1$ stabilizes; $k = 4$ gives pole $-3$ and $x_{ss} = 4/3\,r$ (the output settles above the reference). Also: no constant open-loop input can hold an unstable plant at $r$.
- **Correction:** a short subsection with this example.

### D4. Sensitivity not generalized
- **Where:** `:96-98`, `:124`
- **Text:** "What feedback has done is make the output move about five times less"
- **Problem:** the "five times" is the factor $a/(a + bk) = 1/(1 + L_0)$ with $L_0 = bk/a$, which also gives the offset (`:53`) and the disturbance ratio (`:98`). Derived: relative sensitivity of $x_{ss}$ to $a$ is $-a/(a + bk)$ in closed loop and $-1$ in open loop. Recomputed with the entry's numbers: relative change −16.7% open loop vs −3.9% closed loop, ratio 0.23, consistent with 0.2 for a small change.
- **Correction:** add a subsection deriving the factor and connecting the three results.

### D5. Limits unsupported
- **Where:** `:128-130`
- **Text:** "Delays and unmodelled dynamics can turn a large gain into oscillation or instability"
- **Correction:** add the sampled-loop gain limit computed in `from-signal-processing-to-digital-control` (largest stable $k \approx 20$ at $T = 0.1$ s for $a = b = 1$; recomputed $\coth(0.05) = 20.02$), the initial input $u(0) = kr$ for saturation, and noise entering as $k\,n$.

### C1. Description
- **Text:** "How closing the loop changes the speed of a simple first-order system and how sensitive its output is to plant errors and disturbances, checked with a short simulation." (168)
- **Correction:** shorten below 165 and say what the reader learns.

### C2, C3. Wording
- Remove "simply"; replace the teaser with the statement it delays.

## Revision log (wave 1)

- **Structure:** sections numbered 1-6 with subsections (1.1-1.2, 2.1-2.4, 4.1-4.2); second opening paragraph linking the first entry and stating units and Python 3. The transfer-function derivation of $b/(s + a)$ now refers back to the first entry's Section 3.3 (which owns it) instead of re-deriving it; the pole discussion moved into 2.2. New 2.4: worked stabilization example ($a = -1$, $b = 1$: any $k > 1$ stabilizes; $k = 4$ gives pole $-3$, $x_{ss} = 4r/3$; recomputed analytically and by Euler simulation, 1.3333). New 4.2: loop gain $L_0 = bk/a$ and the single factor $1/(1 + L_0)$ behind offset, disturbance shift and relative sensitivity (derived; checked against the entry's own numbers: −16.7% and −3.9% simulated vs −20% and −4% predicted). Section 5 expanded into three limits with numbers: sampled-loop gain limit about 20 at $T = 0.1$ s (from `from-signal-processing-to-digital-control`, recomputed $\coth 0.05 = 20.02$), $u(0) = kr$, noise multiplied by $k$. New Summary with table and closing transition to the primer; References.
- **Prose:** teaser sentence and "simply" removed; explicit Euler defined; step-size justification added; "you" voice removed ("what is wanted"); time-constant column given units.
- **Metadata:** description rewritten (144 characters); `updatedAt: 2026-10-13` added here and in the Vietnamese file.
- **References:** Åström and Murray (2021); Franklin, Powell and Emami-Naeini (2019) (verified as above).
- **Code:** unchanged; both blocks re-run, output matches the text.
- Remaining warnings: none.
- **Flags for independent review:** (technical) Section 4.2 sensitivity derivation and its stated condition $a > 0$; Section 2.4 statement that no constant open-loop input can hold an unstable plant at a reference. (series) the sampled-gain figure depends on the DSP series article staying as it is.
- **Vietnamese translation affected: yes.** Meaning changes: description; new opening paragraph 2; teaser sentence removed and "it can make an unstable plant stable" added to the opening; 1.1 now says the plant is the first entry's example and gives $b/(s+a)$ there (the derivation sentence formerly in the pole paragraph is gone); proportional feedback defined; 2.2 merges the former pole paragraph; 2.4 new (stabilization example); Section 3 adds Euler definition and step-size remark; 4.2 new (loop gain and $1/(1 + L_0)$); the sentence "Removing the offset itself takes more than proportional action" moved to 4.2; Section 5 expanded (delay with sampled-loop limit, saturation, noise); Summary and References new; table header "Time constant (s)" and units "1 s", "0.1 s" added; all headings numbered.

## Independent review (wave 2)

- Reviewer: independent reviewer (fact-check, technical, series), commit `9232ed9`, 2026-10-13. Report: `reviews/foundations-of-control-systems.md`.
- Fact-check verdict: pass.
- Technical verdict: fail until T1 is resolved.
- Findings concerning this item: T1.
- Not verified: none.

## Revision log (wave 2 resolution)

- T1: Section 5 sentence corrected; a larger gain now reads as improving speed, sensitivity and offset, and the offset never reaches zero (`:167`).
- Lint 0/0/0; syntax passes. No front matter changed.
- Vietnamese translation affected: yes. Section 5's opening sentence changed meaning (larger gain improves the offset as well, without removing it).
