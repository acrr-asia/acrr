# Series review: Critical Thinking and Reasoning

- Series: `critical-thinking` (13 articles, status published, 0 planned entries)
- Reviewed commit: b7cf217
- Date: 2026-10-20

## Summary

The series is a coherent thirteen-entry course that moves from meaning and argument, through a four-entry short course in formal logic, to evidence, values, decisions, fallacies and creativity. Its technical content is in good shape: every worked number, verdict, derivation and counter-model recomputed in this pass is correct, and all three Python listings reproduce their quoted output exactly. A first review wave (reviewers A, B and C) raised 90 findings, 84 on the entries and the overview and 6 on the Vietnam AI strategy insight: 30 blocking, 30 should fix and 30 optional (A: 27, of which 11 blocking, 6 should fix and 10 optional; B: 33, with 13, 10 and 10; C: 30, with 6, 14 and 10). All were applied except four optional or allowed items (B31, C21 and C30 were left by choice, and C24 was not addressed); see the Resolution section. This independent second pass found two blocking problems that the first wave missed, both originality defects against the HKU source modules. The tenth entry still paraphrases the HKU values module in its definitions of value, its descriptive and normative contrast, its intrinsic-value points and its accounts of relativism, absolutism, contextualism and formal justice (S1). The ninth entry reuses the HKU worked example of two dice and "at least one six" (S2). The other second-pass findings are residues of the corrections: summary rows that no longer match rewritten bodies (S3, S6, S11), a few borderline paraphrases (S5, S8, S13), two factual slips (S7, S9), one cross-reference that points to the wrong entry (S12) and minor consistency items. The series is not ready to stamp until S1 and S2 are resolved.

Findings (second pass): 2 blocking, 11 should fix, 12 optional.

## Resolution

First-wave findings, as resolved by the authors (condensed from their resolution notes). No section of any entry was renumbered; renamed headings are noted. Vietnamese translations of the entries were made after the second-pass fixes, from the corrected English text; every later English correction was applied to them in the same commit. The Vietnamese series file was updated with the shared reference change, and the Vietnamese insight was updated for C25 to C29.

Group A (entries 1 to 5):
- A1: Entry 1 §1.2 rewritten as "What it adds to knowledge and to criticism", with three new topic sentences and engineering examples; the rules-versus-creativity contrast was removed; §1.1 definition attributed to Lau (2011).
- A2: Entry 1 §3 rebuilt on the Delphi split between skills and dispositions; swimming analogy replaced by a debugger-manual analogy; the four obstacle attitudes were deleted; the CCTDI list was replaced by attributed Delphi habits in an original table.
- A3: Confirmation-bias example now cites Wason (1960) and entry 12 §6.3; Wason added to references.
- A4: Mercier and Sperber (2011) cited and framed as their argument.
- A5: "from P1–P3 to C".
- A6: Lau (2011) cited in §1.1; author form "J. Y. F. Lau"; Facione publisher corrected.
- A7: Thermometer circle replaced by heartbeat/live-node circle; resistor example removed; Exercise 3(b) now 9 and 3; 3(c) now equilateral and equiangular.
- A8: Entry 2 definitions of sufficient and necessary, too wide and too narrow, stipulative, verbal-dispute resolution, §7.2 lead and category mistake rewritten; §5.4 renamed "Necessary according to what?" and recast as a table; further n-gram echoes rewritten.
- A9: Statement defined as what a declarative sentence asserts.
- A10: "negatively related".
- A11: Entry 3 §7.3 rebuilt around three original questions; five-label list, colour example and "deductive in disguise" paragraph removed.
- A12: Entry 3 §8 rewritten as three conditions derived from the purpose of an argument, with Govier (2010) cited; mistaken-inference table replaced by original postmortem statements.
- A13: Hidden-assumption procedure rewritten; §6.3 renamed "Background conditions behind a named cause" and rewritten.
- A14: Lines 23, 35, 142, 165, 169 and 276 reworded with new examples; plain "counterexample".
- A15: Fixed within the new §8 item 1.
- A16: "is usually presented in this shape".
- A17: "the fourth entry introduces them and the sixth gives them precise meanings".
- A18: Pointer to entry 8 §3 added.
- A19: Entry 4 §4.2 rewritten from scratch; sweeping-claims sentence deleted.
- A20: Entry 4 §§1.1 to 1.4, 4.1, 4.3 and 4.4 re-conceived with new examples.
- A21: Faithful instances (12, 8 and 4) in §5.2 and Exercise 6.
- A22: Entry 4 §2.1 statement definition revised (see S6 for the summary row).
- A23: Copi 14th ed. dated 2011 and Lau given as "J. Y. F. Lau" throughout the series.
- A24: "the sixth and seventh entries make them precise".
- A25: "the laws of thermodynamics".
- A26: Region numbers added to Figures 3 and 4 (generator updated and regenerated).
- A27: Standard-form middle-term example (316L alloys).

Group B (entries 6 to 9):
- B1, B3: Entry 6 §3.3 renamed "Explosion in truth-table terms" and rewritten as a back-reference to entry 4.
- B2: §7.4 strategies reordered and rewritten.
- B4: §8.3 now refers back to entry 4 §5.3.
- B5: Named forms cite entry 3 §5; no longer bolded as new terms.
- B6: Duplicate table columns removed.
- B7: "(Section 5.1)".
- B8: Field and test-bench instance (see S17).
- B9, B10, B11: Model definition, bound-variable wording and incompleteness hypothesis corrected.
- B12: Entry 8 §1 rewritten as the odometry running case.
- B13: §2 rebuilt on Hempel and Popper with a new §2.2; §3 now uses Kuhn's five characteristics (Kuhn, 1977).
- B14: §4 rebuilt on Pearl and Mackie; old §4.4 is now §4.3.
- B15: §5.5 rewritten around the CI table; methods now in Mill's order.
- B16: §6 restructured, with a new §6.2 on Hill's considerations (see S8).
- B17: §8 rebuilt on firmware, A/B and salt-spray examples.
- B18: §9.1 tied to the entry's own examples; §9.2 reduced to replication and publication bias (Rosenthal, 1979).
- B19: Summary row separates INUS from trigger and standing conditions.
- B20: Theory-choice criteria cite Kuhn (1977) only.
- B21: 0.5^10 and 0.95^10 added.
- B22: Captions and figure numbers for entries 8 and 9 (see S16 for the rest of the series).
- B23: Roulette replaced by a spare-parts expected-cost example.
- B24: Gambler's fallacy cases replaced (flaky test, bit generator, tool wear, hourly job).
- B25: Probability scale rewritten; round-robin slot replaces the die.
- B26: Random-sample definition rewritten; fish replaced.
- B27: Three-sensor safety case; server rack replaces speed cameras.
- B28: Margin target is 2 points (n = 2401).
- B29: Question word order fixed.
- B30: Entry 11 promise reworded.
- B31: No change (optional; de Méré kept with its historical attribution).
- B32: "removes selection bias".
- B33: "Python 3 (run with 3.13)".

Group C (entries 10 to 13, overview and insight):
- C1: Entry 10 §10 now cites confirmation bias, entry 12 §6.3.
- C2: Entry 10 §8 rewritten from Mill, Dworkin and Hursthouse on one running case.
- C3: §3.1 restricted to a substantive "ought", with degenerate cases set aside (see S11 for the summary row).
- C4: Hohfeld figure row labels removed, legend and caption corrected.
- C5: Summary row for analogical arguments corrected.
- C6: §5.2 attributes vulgar relativism to Williams (1972); Exercise 3 now tests revising the judgment.
- C7: "sometimes used loosely".
- C8: Entry 11 §§1.1, 1.2, 2.1, 2.3, 3.2 and 5.1 rewritten from primary sources (Pólya, ISO 5807, Waterman et al., Franklin).
- C9: §4.1 opens with Baron and Hershey; §4.2 states the Kahneman and Klein conditions first.
- C10, C11, C12: Maximin wording, decision-tree notation and the three-way tie corrected or added.
- C13: Self-refuting example replaced by the style-guide rule.
- C14: Cross-reference corrected to entry 10 §§3.1 and 3.3.
- C15: Broad-sense rationale and family definitions rewritten as questions (see S13).
- C16: Svenson (1981) cited.
- C17: Quantifier-shift example corrected.
- C18: Copi dated 2011.
- C19: Entry 13 fully rewritten on primary sources (Runco and Jaeger, Boden, Campbell, Guilford, Wallas, Sio and Ormerod, Duncker, Jansson and Smith, Diehl and Stroebe, Janis).
- C20: "(Lau and Chan, 2004–2026)"; one Pólya reference.
- C21: Left as allowed (Double Diamond unnamed).
- C22: The overview's originality sentence depends on the entries (see S1, S2).
- C23: Overview now names entries four, nine and twelve for Python listings.
- C24: Not addressed (see S22).
- C25 to C29 (insight): SMEs, missing targets and "at least", baseline sentence, model tiers and clean power corrected in English and Vietnamese.
- C30 (insight): No change, as allowed.

### Second pass

Second-pass findings, as resolved by the authors (condensed from their resolution notes) and confirmed against the current text in the third pass. Section numbers were kept in every entry.

- S1: Entry 10 rewritten around its own examples and primary sources. §1.1 reads one judgment ("this design is bad") three ways instead of the three-family taxonomy; §1.2 uses a post-incident-report table and Williams's thick concepts (survey point gone, Exercise 1 matched); §2.2 is about means outliving their conditions (two-approval rule); §2.3 is Moore's isolation test; §3.2 is organized around the attack surface of a valid argument; §3.3 is a table with engineering counterexamples; §4 starts from Plato's question and a coding-standard case ("rules are compressed reasons"); §5.1 gives a new definition and sets out the argument from disagreement as invalid; §5.3 contrasts an exceptionless universal with a default with conditions, and the situation with the judge; §6.1 uses two release decisions. The top-level topic order still follows the module, which the overview discloses ("topics and their order were suggested by").
- S2: Entry 9 §2.1 uses an independent nightly-build example (0.2 and 0.3, so 0.44, not 0.5); listing 1 counts a 10 × 10 grid and prints 11/25.
- S3: Entry 1 summary rows replaced ("What does it add?"; "willingness to reconsider").
- S4: Entry 2 §6 renamed "Unclear claims: ambiguity, vagueness and incomplete meaning"; "obscurity" now names only the definition defect.
- S5: Entry 2 §6.3 opens from the Rust example with an original table of engineering words; §7.4 opens from a migration risk register and covers hedges, truth by meaning and truth by logical form.
- S6: Entry 4 summary row now matches §2.1.
- S7: Wason task now described as P and Q chosen, not-Q skipped.
- S8: Entry 8 §6.1 is a table of causal-graph structures in a new order with replication as the check for chance; the placebo appears only in §8.2.
- S9: Hill now said to exempt none of his viewpoints, temporality included.
- S10: Publication-bias sentence rewritten.
- S11: Entry 10 summary row qualified to a substantive normative conclusion.
- S12: Entry 12 opening credits the third entry (Section 4.2) and the fourth for form.
- S13: Entry 12 §1.1 draws the fact/reasoning contrast inside the regulator argument; the broad sense rests on discussion moves; §1.3 illustrates a bias by availability.
- S14: Entry 3 references in alphabetical order.
- S15: Weston is 4th ed., Hackett, 2009 in both entries 3 and 12; "drivers?," fixed. Not done (optional): the in-text Copi form in entry 8 (line 127) and the Kuhn page range.
- S16: Declined (optional): figures are numbered only where the text cites them by number. Justified.
- S17: Three-predicate instance in entry 7 §6.2.
- S18: Entry 3 §8 item 2 now names the two cases it covers and sends the third to condition 1.
- S19: Bayesian network: a distribution per node conditional on its parents.
- S20: "the flowcharts in this series".
- S21: Entry 11 §2.2 is one timed decomposition of the CI pipeline (21 minutes; savings 0, 4 and 3.5).
- S22: Overview paragraph on what the series leaves out added.
- S23: Rephrased as "the equation $2 + 2 = 5$".
- S24: Entry 9 §9.1 links "positively correlated" to entry 8's "associated" (Section 6.1).
- S25: Entry 6 §3.3 cites "The fourth entry, Section 4.5".

### Third pass (verification)

An independent verifier checked every S resolution against the current text of the named files, re-ran the n-gram scans and a structural read for S1 and S2, re-ran both entry 9 listings, recomputed the new numbers, checked every section cross-reference in the 13 entries and ran the linter (details in the Verification log). All 25 S findings are resolved or justifiably declined, apart from two optional S15 items. One residue of the is-ought qualification remains, recorded as **T1** (Should fix): the introduction of entry 10 (`src/content/blog/reasoning-about-values.mdx:20`) still says the entry "explains why facts alone never yield an 'ought'", the unqualified claim that C3 corrected in §3.1 and S11 corrected in the summary. Paste-ready correction: "explains why facts alone do not yield a substantive 'ought'". Optional residues, not blocking: S15's Copi in-text form in entry 8 and the Kuhn page range; entry 2 §7.4 ("The sixth entry gives tautology a precise definition") names no section. Until T1 is fixed, the series has one open Should fix finding.

Resolution of the third pass (lead): T1 fixed: the introduction of entry 10 now reads "explains why facts alone do not yield a substantive 'ought'", matching §3.1 and the summary (Vietnamese translation updated to match). Two optional residues from the verification were also applied: entry 8 now cites "(Mill, 1843; Copi et al., 2011)", and entry 2 §7.4 now names "the sixth entry (Section 3.1)". Two translator observations were applied to entry 11 (English and Vietnamese): the dangling "where they are" in §6.1 now reads "where probabilities for the states are available", and Peters and Waterman (1982), already in the reference list, is now cited in §3.2. No blocking or should-fix finding remains open.

## Objectives coverage

| Objective (from the series file) | Covered by | Assessment |
|---|---|---|
| Explain what critical thinking is and analyze a claim or argument into its meaning, premises, conclusion and hidden assumptions. | Entry 1 (§§1–5), entry 2 (meaning, definitions, ambiguity), entry 3 (§§1–3, §6) | Met. |
| Evaluate arguments for validity, soundness and inductive strength, using Venn diagrams, truth tables, natural deduction and quantifier logic where the argument has a formal structure. | Entry 3 (§§4, 7, 8), entry 4, entry 5 (Venn test), entry 6 (§5 truth tables, §7 natural deduction), entry 7 (counter-models, quantifier rules) | Met. |
| Assess causal, scientific and statistical claims: design a fair comparison, apply the rules of probability and Bayes' theorem, and interpret samples and significance tests. | Entry 8 (§§2–8, fair test in §8), entry 9 (§§2, 5, 6–8) | Met. |
| Analyze value judgments and decisions: separate factual from evaluative premises, test principles for consistency and compare options with explicit criteria. | Entry 10 (§§1.2, 3, 6, 7), entry 11 (§§5–7) | Met (entry 10 text subject to S1). |
| Identify common fallacies and cognitive biases in real reasoning, and apply structured techniques for generating and developing new ideas. | Entry 12, entry 13 | Met. |

## Findings

| ID | Severity | Article | Location | Dimension | Finding |
|---|---|---|---|---|---|
| S1 | Blocking | `src/content/blog/reasoning-about-values.mdx` | §§1.1, 1.2, 2.2, 2.3, 4, 5.1, 5.3, 6.1 (lines 26–33, 41, 61–67, 111–115, 121, 131–133, 139) | Content integrity (originality) | Several definitions, contrasts and example pairings closely paraphrase HKU value modules U01 to U06, in the source's order; the first wave did not flag them. |
| S2 | Blocking | `src/content/blog/probability-and-statistical-reasoning.mdx` | §2.1 (line 61); §2.4 listing (lines 87, 94–97, 118) | Content integrity (originality) | The worked example of two dice and "at least one six" (the tempting 1/6 + 1/6 = 1/3, then 36 outcomes with six and six overlapping, giving 11/36) is the HKU T01 §4 example. |
| S3 | Should fix | `src/content/blog/what-is-critical-thinking.mdx` | §8 Summary (lines 219, 221) | Completeness / originality residue | The summary row "What is it not?" still lists HKU's three contrasts that A1 removed from the body, and the "dispositions" row names humility, which the body does not mention. |
| S4 | Should fix | `src/content/blog/meaning-clarity-and-definitions.mdx` | §3.2 (line 82), §6 heading (line 175), Summary (lines 285, 288) | Terminology | "Obscurity" names two different things: a defect of a definiens (§3.2) and the family of ambiguity, vagueness and incomplete meaning (§6). |
| S5 | Should fix | `src/content/blog/meaning-clarity-and-definitions.mdx` | §6.3 (lines 204, 208); §7.4 (lines 244–247) | Content integrity (originality, borderline) | §6.3 and §7.4 still follow HKU M08 §3 and M10 in definition, word list and sequence. |
| S6 | Should fix | `src/content/blog/what-logic-studies.mdx` | §8 Summary (line 262) | Consistency | The summary defines a statement as "A declarative sentence that is true or false", which contradicts the corrected §2.1 and §2.2 (A22 residue). |
| S7 | Should fix | `src/content/blog/what-logic-studies.mdx` | §1.1 (line 25) | Technical accuracy | The description of the Wason selection task says most people "choose cards that cannot refute the rule"; the usual choice is P and Q, and the P card can refute. |
| S8 | Should fix | `src/content/blog/scientific-reasoning-and-causation.mdx` | §6.1 (lines 164–171); §8.2 (line 231) | Content integrity (originality, borderline); redundancy | The rival-explanation list still follows HKU S06's order and keeps its remedy for chance and its placebo illustration of a side effect; the placebo is also defined twice. |
| S9 | Should fix | `src/content/blog/scientific-reasoning-and-causation.mdx` | §6.2 (lines 186, 193) | Technical accuracy (attribution) | "Apart from temporality, Hill treated none of these as a necessary or sufficient test" misattributes: Hill wrote that none of his viewpoints, temporality included, can be required as a sine qua non. |
| S10 | Should fix | `src/content/blog/scientific-reasoning-and-causation.mdx` | §9.2 (line 251) | Writing quality | "Second, **publication bias**: means studies that find an effect are published more readily..." is ungrammatical. |
| S11 | Should fix | `src/content/blog/reasoning-about-values.mdx` | §12 Summary (line 288) | Consistency / accuracy | The summary row restates the unqualified is-ought claim ("No purely descriptive premises entail a normative conclusion") that C3 corrected in §3.1. |
| S12 | Should fix | `src/content/blog/fallacies-and-cognitive-biases.mdx` | Opening (line 15) | Cross-article references | "The fourth entry showed that an argument can have true premises and a true conclusion and still be invalid": this point is made in the third entry, §4.2 (table, fifth row). |
| S13 | Should fix | `src/content/blog/fallacies-and-cognitive-biases.mdx` | §1.1 (lines 23–25), §1.3 (line 41) | Content integrity (originality, borderline) | §1.1 opens with HKU F01's device (a miscount as a mistake of fact against a mistake of reasoning), and §1.3 repeats F08's point that anchoring is a bias but not a fallacy. |
| S14 | Optional | `src/content/blog/arguments-and-their-structure.mdx` | References (lines 313–315) | Reference format | Govier is listed before Dennett, so the reference list is out of alphabetical order. |
| S15 | Optional | several | e3:247, e3:321, e8:127, e8:292, e12:287, e12:291 | Reference format / consistency | Weston's edition, the in-text form of the Copi citation, missing chapter pages for Kuhn and the punctuation after question-mark titles differ across entries. |
| S16 | Optional | several | See detail | Writing quality (figures) | Figure captioning and numbering are inconsistent: entries 8 and 9 caption and number every figure, while other entries leave Mermaid diagrams uncaptioned and SVG captions unnumbered. |
| S17 | Optional | `src/content/blog/predicate-logic.mdx` | §6.2 (line 164) | Technical accuracy | The "engineering instance" of the invalid monadic form adds a fourth predicate ("test-bench units"), so it is not a faithful instance in the sense of entry 4 §5.2. |
| S18 | Optional | `src/content/blog/arguments-and-their-structure.mdx` | §8 item 2 (line 254) | Technical accuracy | "The puzzling arguments of Section 4.4 are valid only because their conclusions are necessary or their premises impossible" does not fit the first puzzling case, a conclusion that repeats a premise. |
| S19 | Optional | `src/content/blog/scientific-reasoning-and-causation.mdx` | §7.1 (line 209) | Technical accuracy | A Bayesian network attaches a conditional distribution to each node given its parents, not "conditional probabilities" to each arrow. |
| S20 | Optional | `src/content/blog/strategic-thinking-and-decisions.mdx` | §2.3 (line 78) | Factual consistency | "The diagrams in this series follow the same conventions" (ISO 5807) is not true of the series' argument maps, causal graphs or the decision tree's chance node. |
| S21 | Optional | `src/content/blog/strategic-thinking-and-decisions.mdx` | §2.2 (line 74) | Content integrity (originality, borderline) | The two kinds of decomposition (a process of steps that turn inputs into outputs; a system of interacting components) follow HKU G04's two sections. |
| S22 | Optional | `src/content/series/critical-thinking.md` | Line 14 | Purpose, audience and scope | The overview still does not say what the series leaves out (C24, unresolved). |
| S23 | Optional | `src/content/blog/what-logic-studies.mdx` | §2.1 (line 57) | Publishing | The opening quotation mark before the inline math "$2 + 2 = 5$" renders as a straight `"` in `dist/`, while every other quotation mark is typographic. |
| S24 | Optional | `src/content/blog/probability-and-statistical-reasoning.mdx` | §9.1 (line 322); entry 8 line 164 | Terminology | Entry 8 defines **association** and says entry 9 §9.1 "states it in terms of probability", but §9.1 defines **correlated** without linking the two terms. |
| S25 | Optional | `src/content/blog/sentential-logic.mdx` | §3.3 (line 120) | Cross-article references | "The fourth entry showed, where it compared validity with consistency" names no section (it is §4.5). |
| T1 | Should fix | `src/content/blog/reasoning-about-values.mdx` | Introduction (line 20) | Consistency / accuracy | "explains why facts alone never yield an 'ought'" restates the unqualified is-ought claim corrected in §3.1 (C3) and the summary (S11). Replace with "explains why facts alone do not yield a substantive 'ought'". |

### S1. Entry 10 paraphrases the HKU values module

- **Where:** `src/content/blog/reasoning-about-values.mdx:26–33` (§1.1), `:41` (§1.2), `:61–67` (§§2.2–2.3), `:111–115` (§4), `:121` (§5.1), `:131–133` (§5.3), `:139` (§6.1)
- **Text and source (HKU `value.md`):**
  - §1.1: "A **value** ... is a standard by which actions, people, objects or states of affairs are judged better or worse", followed by personal, moral (with "Moral values applied to laws and institutions are often called **political values**") and aesthetic families. Source, `value.md:47–51`: "Values are standards or ideals with which we evaluate actions, people, things, or situations", with personal, moral ("Those which are used to evaluate social institutions are sometimes also known as political values") and aesthetic values, in the same order.
  - §1.2: "First, many normative claims contain descriptive content ... asserts a fact ... and adds an evaluation of that fact ... Second, a report *about* people's values is descriptive. 'Most respondents think the policy is fair' can be checked with a survey". Source, `value.md:169–171`: "a moral claim ... can include some descriptive elements ... the normative component lies in the additional value judgement", then "descriptive claims about moral beliefs in themselves are not normative. A few years back a survey ...". Both points come in the same order, with a survey as the example.
  - §§2.2–2.3: "Someone can desire a means because of a false belief about its effects ... Wanting something for its own sake does not make it intrinsically valuable ... one thing can have both kinds of value", then "Many traditions hold that persons have intrinsic value, which is why basic rights are not thought to depend on a person's usefulness or wealth; environmental ethics asks whether species or wild places have value". Source, `value.md:79, 88, 99, 105–106`: desire "based on a false belief"; desiring as an end without its being intrinsically valuable; "one and the same thing ... may have instrumental value as well as intrinsic value"; a person's intrinsic value as "the moral foundation of basic human rights regardless of occupation, economic status"; "objects of environmental concern ... wild plants". The same four points come in the same order, ending with the same pair of examples.
  - §4: after the dilemma, "it is not an argument against any religious belief ... Its lesson is general ... Authorities can be good evidence about values; they do not remove the need to judge". Source, `value.md:229`: "these arguments are not arguments against the existence of God ... the basis of moral values ... are not determined by any authority. We have to exercise our own rational judgment".
  - §5.1: "there are no objective moral facts, and an action is right or wrong only *relative to* a society, a person or a framework". Source, `value.md:251`: "(1) there are no objective normative facts, and (2) what is right or wrong is relative to particular societies or persons, or moral frameworks".
  - §5.3: "**Moral absolutism** ... holds that the action is always required or always forbidden, whatever the circumstances and consequences", followed by Kant on lying, contextualism ("whether it is right depends on the circumstances"), lying to save someone against a wrongful lie, and "Contextualism is not relativism. The contextualist says that ... there is a fact ...; the relativist denies that". Source, `value.md:277, 291–297`: "some actions are morally required or morally prohibited regardless of the situation and the potential consequences", the same Kant example, the same contrast of lying to save a life with officials' lies, and "both moral absolutism and contextualism agree that morality is objective ... Moral relativism would deny this".
  - §6.1: "cases alike in all relevant respects should be judged alike. If one contractor is penalized ... and another is not, the difference needs a reason ... arbitrary or discriminatory". Source, `value.md:321`: "treat like cases alike. If someone goes to prison for stealing, it would be inconsistent ... to let another thief walk free, if the two cases are alike in all relevant respects ... discriminatory".
  - Borderline, part of the same pattern: §3.2 ("The gap does not make facts irrelevant ... needs both kinds of premise", with a principle plus descriptive premises) follows `value.md:185`; §3.3 refutes the nature and tradition bridges in the way `value.md:183` does.
- **Problem:** The first wave rated entry 10 on §§5.2, 6.2 and 8 only. The sections listed above keep HKU's definitions, the order of its points and several of its example pairings, with light rewording. The 6-gram scan finds only one or two shared strings per section ("is valuable as a means to", "alike in all relevant respects"), because these are paraphrases rather than copies. The brief treats any close paraphrase as a content-integrity breach. While these passages stand, the overview's sentence "the text, examples and figures of this series are original" (series file, line 22) is not true of this entry.
- **Recommended correction:** Rewrite each listed passage from the primary sources the entry already cites (Hume, Moore, Plato's *Euthyphro*, Kant, Williams, Rawls), with the entry's own order and examples, and drop the HKU devices: the three-family taxonomy with the political-values aside, the "descriptive content / reports of values" pair with a survey, the persons and environment pair, the "not against God, therefore judge for yourself" sequence, the two-clause relativism definition, the absolutism and contextualism definitions with the "both are objective" contrast, and the stealing-style illustration of formal justice. Starting points that are ready to paste:
  - §1.1: "Arguments about what to do appeal to standards: a safety margin, fairness between users, the elegance of a proof, the cost of a design. Such a standard is a **value**, and a claim that applies one is a **value judgment** ... The same words can appeal to different kinds of standard. 'This design is bad' may mean that it harms someone (a moral standard), that it fails its purpose (an instrumental one) or that it is ugly (an aesthetic one), and the first question about a value argument is which is meant."
  - §5.1: "**Moral relativism** holds that a moral judgment is true or false only by the standards of some group or framework, so that no framework's verdicts are more correct than another's."
  - §6.1: Restate formal justice through the release example of §6.2 or the review policy of §3.1, not through a penalty imposed on one party and withheld from another.
  
  Re-run the n-gram scan and a side-by-side read against `value.md` afterward.

### S2. Entry 9 reuses the HKU two-dice example

- **Where:** `src/content/blog/probability-and-statistical-reasoning.mdx:61`, §2.1; the listing at `:87`, `:94–97` and its output at `:118`
- **Text:** "With two fair dice, the chance of at least one six is not $1/6 + 1/6 = 1/3$. Of the 36 equally likely pairs, 6 have a six on the first die and 6 on the second, but the pair (6, 6) is in both groups, so only 11 pairs qualify and the probability is $11/36 \approx 0.306$."
- **Problem:** This is the worked example of HKU `stat.md:105–109` (T01 §4): "Suppose I roll two dice. What is the probability that I will get at least one 6? ... 1/6 + 1/6, which is 1/3 ... 36 possible outcomes ... six are outcomes in which the first die shows a 6, and six ... the second". The setup, the error and the correction are the same. B23 to B28 replaced the other HKU illustrations in this entry, but this one was not flagged. The listing in §2.4 repeats it.
- **Recommended correction:** Replace it with an engineering case of overlapping events, for example: "Two independent servers are each unavailable at a given moment with probability 0.1. The chance that at least one is unavailable is not $0.1 + 0.1 = 0.2$: the sum counts the moment when both are down twice, so $P = 0.1 + 0.1 - 0.01 = 0.19$, and the complement rule gives the same, $1 - 0.9^2 = 0.19$." (Recomputed: 0.19.) In the first listing, replace the dice enumeration with an enumeration of the four server states using `Fraction(1, 10)` (exact result 19/100), or delete it and keep the de Méré and three-door parts. Update the lead-in at line 87 and the quoted output at line 118 to match the rerun output.

### S3. Entry 1 summary does not match the rewritten body

- **Where:** `src/content/blog/what-is-critical-thinking.mdx:219` and `:221`, §8 Summary
- **Text:** "What is it not? | Mere knowledge of facts, fault-finding for its own sake, or the opposite of creativity." and "... practice and dispositions such as open-mindedness and humility."
- **Problem:** A1 replaced the three "is not" contrasts in §1.2 (memory of facts, being argumentative, hindering creativity: HKU `critical.md:58–62`) with "Knowledge is not judgment", "Criticism is a means, not the goal" and "Evaluation needs something to evaluate". The summary row still states the HKU triad in the HKU order. "Humility" appears nowhere in §3.4, whose habits are inquisitive, open-minded, fair-minded, honest about biases, prudent and willing to reconsider.
- **Recommended correction:** Use "What does it add? | Judgment beyond knowledge; criticism in the service of the best-supported conclusion; and the selection half of a cycle whose other half is generating options." for the first row, and "... practice and dispositions such as open-mindedness and willingness to reconsider." for the second.

### S4. "Obscurity" used for two concepts

- **Where:** `src/content/blog/meaning-clarity-and-definitions.mdx:82` (§3.2), `:175` (§6 heading), `:285` and `:288` (Summary)
- **Text:** "**Obscurity.** The definiens is harder to understand than the definiendum." and "## 6. Obscurity: ambiguity, vagueness and incomplete meaning"
- **Problem:** The term means a defect of definitions in §3.2 and the family of ambiguity, vagueness and incomplete meaning in §6. The two summary rows (lines 285 and 288) use it in both senses, one row after the other. Standards 5.3 require one term per concept.
- **Recommended correction:** Rename §6 "Unclear claims: ambiguity, vagueness and incomplete meaning". Change its first sentence to "A claim can be unclear in three distinct ways ..." and the summary question to "What are the ways a claim can be unclear?". Keep "obscurity" for the definition defect.

### S5. Entry 2 §§6.3 and 7.4 follow HKU M08 §3 and M10

- **Where:** `src/content/blog/meaning-clarity-and-definitions.mdx:204, 208` (§6.3) and `:244–247` (§7.4)
- **Text:** "they relate a thing to a standard, a rival or a purpose, and when that second term is left unstated, the claim has **incomplete meaning**. Typical examples are 'better', 'faster', 'similar', 'efficient', 'secure', 'important' and 'useful' ... Any two things are similar in some respects and different in others." and §7.4: a lead asked whether the release will be ready replies "It will be ready when it is ready"; "Call a statement **empty** when it rules out no possibility that the listener cared about"; then tautologies, then analytic statements as the wider class, then an analytic statement offered in a design review.
- **Problem:** HKU `meaning.md:458` defines incomplete meaning as dependence on "some further parameter", gives "useful, important, similar and better", and adds "Practically all objects are useful and important only in some respects but not others". HKU `meaning.md:583–591` defines an empty statement relative to "the relevant conversational context". It opens with a person asked whether someone will come who replies "If I come, I will come", then treats tautologies, then calls analytic statements the wider class whose members are empty when offered to someone who already knows the meaning. The entry keeps that sequence and its opening scenario. Each piece is standard; together they read as a light rewording (borderline, so Should fix).
- **Recommended correction:** §6.3: define the idea through the entry's own example first ("'Rust is safer than C' cannot be checked until one says: safer against which failures?") and present the word list as the entry's own engineering vocabulary (for example "faster", "secure", "scalable", "efficient"), without the "in some respects" sentence. §7.4: open with the unfalsifiable hedge or the design-review example, define emptiness in the entry's own terms, and use a tautology example that is not a reply to a "will it happen?" question.

### S6. Entry 4 summary contradicts §2.1 on statements

- **Where:** `src/content/blog/what-logic-studies.mdx:262`, §8 Summary
- **Text:** "Statement | A declarative sentence that is true or false; questions and commands are not statements."
- **Problem:** After A22, §2.1 (line 57) defines statements as "what a declarative sentence claims", and §2.2 (line 65) says that one sentence can make different statements. The summary still identifies a statement with a sentence, the inconsistency that A9 and A22 removed elsewhere (entry 2, line 26).
- **Recommended correction:** "Statement | What a declarative sentence claims, which is true or false; questions and commands make no statement."

### S7. Wason selection task misdescribed

- **Where:** `src/content/blog/what-logic-studies.mdx:25`, §1.1
- **Text:** "most choose cards that cannot refute the rule and skip one that can (Wason, 1968)"
- **Problem:** The classic result is that most people choose the P card and the Q card. The P card can refute the rule, and the Q card cannot; the card they skip that could refute it is not-Q. "Choose cards that cannot refute the rule" says that every card chosen is uninformative, which is wrong for P.
- **Recommended correction:** "most choose the card showing $P$, which is right, and the card showing $Q$, which cannot refute the rule, and skip the card showing not-$Q$, which can (Wason, 1968)."

### S8. Entry 8 §6.1 still follows HKU S06

- **Where:** `src/content/blog/scientific-reasoning-and-causation.mdx:164–171`, §6.1; placebo also at `:231`
- **Text:** The structures come in the order chance ("A comparison period without $A$ shows whether $B$ was unusual at all"), reverse direction, feedback, common cause, selection and bundled cause ("in medicine, a patient's expectation of benefit, the **placebo effect**, comes bundled with any visible treatment").
- **Problem:** HKU `sci.md:343–374` lists accidental, B causes A, causal loop, common cause, minor cause and side effect. Its remedy for the accidental case is to "consider a *control situation* where A is absent", and its side-effect example is the placebo effect. The entry keeps the HKU order (with "minor cause" dropped and "selection" inserted), the remedy for chance and the placebo illustration. The B16 resolution note says the list is "in a new order", but it is not. The placebo is also defined in bold here and again in §8.2 (line 231), contrary to standards 6.1 (no repeated explanation).
- **Recommended correction:** Order the structures by Pearl's graph patterns, which §7.1 introduces: common cause (fork), selection (collider), reverse direction, feedback, a bundled cause, and chance last as the statistical residue. Reword the chance check, for example: "a pre-registered metric, or the same search run on a period without an outage, shows whether one hit among 40 is surprising". Drop the medical aside from the bundled-cause bullet, so that the placebo is introduced once, in §8.2.

### S9. Hill and temporality

- **Where:** `src/content/blog/scientific-reasoning-and-causation.mdx:186` and `:193`, §6.2
- **Text:** "**Temporality**: ... This one is required." and "Apart from temporality, Hill treated none of these as a necessary or sufficient test".
- **Problem:** Hill (1965) wrote that none of his nine viewpoints "can bring indisputable evidence for or against the cause-and-effect hypothesis and none can be required as a *sine qua non*". He did not exempt temporality. That a cause must precede its effect is a conceptual point made by later commentators, not Hill's own qualification, so the text attributes to Hill a view he did not state.
- **Recommended correction:** At line 186: "**Temporality**: the supposed cause comes before the effect, in every case. A cause cannot follow its effect, so this consideration is the one that cannot be waived." At line 193: "Hill himself wrote that none of his considerations can be required as a *sine qua non*; they are weighed together."

### S10. Ungrammatical sentence on publication bias

- **Where:** `src/content/blog/scientific-reasoning-and-causation.mdx:251`, §9.2
- **Text:** "Second, **publication bias**: means studies that find an effect are published more readily than those that do not, so the record overstates the evidence."
- **Problem:** The colon and "means" leave the sentence without a working main clause. This is a published grammatical error introduced in the B18 rewrite.
- **Recommended correction:** "Second, **publication bias**: studies that find an effect are published more readily than those that do not, so the published record overstates the evidence."

### S11. Entry 10 summary restates the unqualified is-ought claim

- **Where:** `src/content/blog/reasoning-about-values.mdx:288`, §12 Summary
- **Text:** "Is-ought gap | No purely descriptive premises entail a normative conclusion; make the bridging premise explicit and test it."
- **Problem:** C3 qualified §3.1 (line 73) to a *substantive* normative conclusion and set aside degenerate cases. Inconsistent descriptive premises entail every conclusion, as entry 4 §4.5 and entry 6 §3.3 teach. The summary repeats the version that C3 judged false.
- **Recommended correction:** "Is-ought gap | Purely descriptive premises do not validly yield a substantive normative conclusion; make the bridging premise explicit and test it."

### S12. Entry 12 cites the wrong entry for a point about invalidity

- **Where:** `src/content/blog/fallacies-and-cognitive-biases.mdx:15`
- **Text:** "The [fourth entry](/blog/what-logic-studies) showed that an argument can have true premises and a true conclusion and still be invalid."
- **Problem:** The demonstration is the third entry's §4.2 table (fifth row, "Some primes are odd. 7 is odd. So 7 is prime", marked invalid with true premises and a true conclusion), which entry 3 Exercise 4(c) also uses. The fourth entry shows that validity depends on form and refutes forms by instances, but it gives no example with true premises and a true conclusion. Standards 9.1 C6 treats a reference that does not say what is claimed as a defect. It is rated Should fix here because entry 4 §5.2 makes a related point.
- **Recommended correction:** "The [third entry](/blog/arguments-and-their-structure) (Section 4.2) showed that an argument can have true premises and a true conclusion and still be invalid, and the [fourth](/blog/what-logic-studies) traced validity to form."

### S13. Entry 12 §§1.1 and 1.3 echo HKU F01 and F08

- **Where:** `src/content/blog/fallacies-and-cognitive-biases.mdx:23` and `:25` (§1.1), `:41` (§1.3)
- **Text:** "Someone who records a supply voltage as 3.3 V when it is in fact 3.1 V has made a mistake of fact ... Someone who concludes ... has made a mistake of reasoning" and "A person anchored by an irrelevant number (Section 6.2) has drawn no inference".
- **Problem:** HKU `fallacy.md:42` opens with the same device: "Fallacies are mistakes of reasoning, as opposed to making mistakes that are of a factual nature. If I counted twenty people in the room when there were in fact twenty-one, then I made a factual mistake". `fallacy.md:400` makes the §1.3 point with the same example: "a cognitive bias need not be a fallacy. The anchoring phenomenon ... does not seem to be a case where we have made an erroneous deduction". The C15 rewrite of the broad-sense rationale also keeps F01's two non-argument cases, a self-contradiction and a loaded question. Each move is defensible alone, but together they reproduce the source's opening sequence (borderline).
- **Recommended correction:** Open §1.1 with the regulator argument alone and draw the contrast inside it: "The premise 'the voltage is low' may be false because the meter is miscalibrated; that would be a mistake of fact. The inference from it is bad even if the premise is true; that is a mistake of reasoning." In §1.3, illustrate a bias without an inference by availability (for example, judging outage frequency by the last memorable outage) instead of anchoring.

### S14. Reference order in entry 3

- **Where:** `src/content/blog/arguments-and-their-structure.mdx:313–315`
- **Text:** Copi, then "T. Govier, ...", then "D. C. Dennett, ...".
- **Problem:** Standards 7.3 require alphabetical order of first author. Govier was inserted (A12) above Dennett.
- **Recommended correction:** Move the Govier entry below Dennett.

### S15. Reference consistency across entries

- **Where:** `arguments-and-their-structure.mdx:321` against `fallacies-and-cognitive-biases.mdx:291`; `arguments-and-their-structure.mdx:247` against `scientific-reasoning-and-causation.mdx:127`; `scientific-reasoning-and-causation.mdx:292`; `fallacies-and-cognitive-biases.mdx:287`
- **Text:** "A. Weston, *A Rulebook for Arguments*, 4th ed., Hackett, 2009." against "5th ed., Hackett, 2017."; "(Copi et al., 2011)" against "(Mill, 1843; Copi, Cohen and McMahon, 2011)"; the Kuhn chapter has no page range; and "...fellow drivers?" *Acta Psychologica*" has no comma after the question mark, while entries 1 and 8 write "?,".
- **Problem:** Standards 7.3 call for volume, issue and pages where they exist and for consistent forms across a series.
- **Recommended correction:** Cite one Weston edition in both entries. Use "Copi et al., 2011" in text everywhere. Add the chapter's page range to Kuhn (1977) after checking it against the book (pp. 320–339 in *The Essential Tension*, not verified here). Write "drivers?," as the other entries do.

### S16. Figure captions and numbering

- **Where:** Uncaptioned Mermaid diagrams: `what-is-critical-thinking.mdx:154`; `arguments-and-their-structure.mdx:88, 97, 113`; `reasoning-about-values.mdx:49, 145`; `strategic-thinking-and-decisions.mdx:58, 82, 253`; `creativity-and-generating-ideas.mdx:98`. Unnumbered SVG captions: `meaning-clarity-and-definitions.mdx:131`; `reasoning-about-values.mdx:228`; `strategic-thinking-and-decisions.mdx:110, 243`; `creativity-and-generating-ideas.mdx:83`.
- **Problem:** B22 numbered and captioned every figure in entries 8 and 9; entries 5 to 7 already numbered theirs. The remaining entries do not, so the series has two figure conventions. Standards 6.1 ask for a caption that says what to look at.
- **Recommended correction:** Number the figures in each entry and give each Mermaid diagram a one-line italic caption, in the form entries 8 and 9 use.

### S17. Predicate-logic instance is not faithful

- **Where:** `src/content/blog/predicate-logic.mdx:164`, §6.2
- **Text:** "some field units run old firmware; some test-bench units that run old firmware have overheated; so some field units have overheated."
- **Problem:** The second premise has the form $\exists x\,(Bx \land Gx \land Hx)$, not $\exists x\,(Gx \land Hx)$. As an "instance" of the three-predicate form it breaks the faithfulness requirement that entry 4 §5.2 states, although it is still invalid.
- **Recommended correction:** "some field units run old firmware; some overheated units run old firmware; so some field units have overheated. The overheated units may all be on the test bench." This keeps three predicates and avoids the reading B8 worried about.

### S18. Over-general sentence on the puzzling cases

- **Where:** `src/content/blog/arguments-and-their-structure.mdx:254`, §8 item 2
- **Text:** "The puzzling arguments of Section 4.4 are valid only because their conclusions are necessary or their premises impossible".
- **Problem:** §4.4 has three cases. The first, a conclusion that repeats a premise, is valid for neither reason; item 1 handles it.
- **Recommended correction:** "The other two puzzling arguments of Section 4.4 are valid only because ...".

### S19. Bayesian network wording

- **Where:** `src/content/blog/scientific-reasoning-and-causation.mdx:209`, §7.1
- **Text:** "When each arrow carries conditional probabilities, the network becomes a **Bayesian network**".
- **Problem:** In a Bayesian network, each node carries a conditional probability distribution given its parents. A node with two parents has one table, not one per arrow.
- **Recommended correction:** "When each variable is given a probability distribution conditional on its direct causes, the network becomes a **Bayesian network** ...".

### S20. Overclaim about diagram conventions

- **Where:** `src/content/blog/strategic-thinking-and-decisions.mdx:78`, §2.3
- **Text:** "ISO 5807 standardizes these symbols ..., and the diagrams in this series follow the same conventions."
- **Problem:** Several of the series' diagrams are not flowcharts: argument maps with an "and" junction circle (entry 3), causal graphs (entries 8 and 9), a stadium-shaped terminal end in a means-end chain (entry 10) and the circle used for the chance node in this entry's decision tree. In ISO 5807 a circle is a connector.
- **Recommended correction:** "..., and the flowcharts in this series follow the same conventions."

### S21. Decomposition echoes HKU G04

- **Where:** `src/content/blog/strategic-thinking-and-decisions.mdx:74`, §2.2
- **Text:** "A **system** can be decomposed into components and the interactions between them ... A **process** can be decomposed into steps that turn inputs into outputs".
- **Problem:** HKU `strategy.md:187` describes a process as "a procedure composing of many steps which convert one or more inputs into one or more outputs" and treats system decomposition in a second section. The idea is generic, and the overlap is the paired definitions (borderline, so Optional).
- **Recommended correction:** Define decomposition once, through the CI problem the entry already uses (pipeline stages and the services they depend on), and drop the paired process and system definitions.

### S22. Overview does not state what is left out (C24 unresolved)

- **Where:** `src/content/series/critical-thinking.md:14`
- **Text:** "It assumes no background in philosophy or logic. Entries four, nine and twelve include a few short Python 3 listings ...; nothing else beyond the site's usual prerequisites is needed."
- **Problem:** The series-review dimension "Purpose, audience and scope" asks the overview to say what the series leaves out. C24 proposed a sentence for this, but it was not applied or answered.
- **Recommended correction:** Add "It does not cover modal or many-valued logics, formal decision theory beyond expected value and simple decision rules, or the psychology of reasoning beyond the biases in the twelfth entry."

### S23. Straight quotation mark next to inline math

- **Where:** `src/content/blog/what-logic-studies.mdx:57`; `dist/blog/what-logic-studies.html`
- **Text:** `and "$2 + 2 = 5$" all make statements`
- **Problem:** The opening quotation mark before the KaTeX span is not converted to a typographic one; the built page shows `&quot;<span class="katex">`, while the rest of the page uses typographic quotes.
- **Recommended correction:** Write the typographic quotation marks “ and ” around the math directly in the source, or rephrase as "the false equation $2 + 2 = 5$".

### S24. Association and correlation not linked

- **Where:** `src/content/blog/scientific-reasoning-and-causation.mdx:164` and `src/content/blog/probability-and-statistical-reasoning.mdx:322`
- **Text:** Entry 8 defines "An **association** between $A$ and $B$ ...; Section 9.1 of the next entry states it in terms of probability", and entry 9 §9.1 defines "$A$ and $B$ are **positively correlated** when ...".
- **Problem:** The promised probabilistic statement uses a different term without saying that it is the same notion. Entry 8's own Figure 3 caption and Mermaid label also say "correlated" and "observed correlation".
- **Recommended correction:** At entry 9 line 322: "In probability terms, $A$ and $B$ are **positively correlated** (associated, in the previous entry's informal term) when ...".

### S25. Missing section number in a back-reference

- **Where:** `src/content/blog/sentential-logic.mdx:120`, §3.3
- **Text:** "The [fourth entry](/blog/what-logic-studies) showed, where it compared validity with consistency, that ..."
- **Problem:** Standards 8.1 ask cross-references to cite numbered sections. The section is §4.5.
- **Recommended correction:** "The [fourth entry](/blog/what-logic-studies) (Section 4.5) showed that ...".

## Concept introduction map

| Concept | First used (path:line) | Introduced where (path:line, or "not introduced") | Assessment |
|---|---|---|---|
| Critical thinking | what-is-critical-thinking.mdx:17 | what-is-critical-thinking.mdx:23 | Good. |
| Statement (claim) | what-is-critical-thinking.mdx:43 (informal) | meaning-clarity-and-definitions.mdx:26; what-logic-studies.mdx:57 | Good in the bodies; entry 4 summary conflicts (S6). |
| Argument, premise, conclusion | what-is-critical-thinking.mdx:170 (informal) | arguments-and-their-structure.mdx:23 | Acceptable: entry 1 uses them in an informal worked example before entry 3 defines them. |
| Validity, soundness, counterexample | what-is-critical-thinking.mdx:171 | arguments-and-their-structure.mdx:133, 142, 165 | Good. |
| Inductive strength | what-is-critical-thinking.mdx:171 | arguments-and-their-structure.mdx:220 | Good. |
| Logical connectives ¬ ∧ ∨ → ↔ | arguments-and-their-structure.mdx:17 (informal); series file line 22 | what-logic-studies.mdx:69–91; sentential-logic.mdx:66–75 | Good; staging stated in entries 2–4. |
| Logical form, consistency, entailment, equivalence | arguments-and-their-structure.mdx:161 | what-logic-studies.mdx:97, 117, 125, 155 | Good. |
| Categorical statement, Venn diagram, Boolean reading | what-logic-studies.mdx:175 | categorical-logic-and-venn-diagrams.mdx:31–42, 67, 97 | Good. |
| WFF, truth table, tautology, ⊨, ⊢ | meaning-clarity-and-definitions.mdx:246 (tautology, forward pointer) | sentential-logic.mdx:40, 66, 104, 112, 229 | Good. |
| Material conditional | what-logic-studies.mdx:91 (deferred) | sentential-logic.mdx:205–221 | Good. |
| Quantifier, interpretation, model, counter-model | meaning-clarity-and-definitions.mdx:186 (scope, pointer) | predicate-logic.mdx:46, 127–133, 155 | Good. |
| Hypothesis, test implication, HD method | scientific-reasoning-and-causation.mdx:26 | scientific-reasoning-and-causation.mdx:26, 34 | Good. |
| Cause, INUS, standing condition and trigger | arguments-and-their-structure.mdx:207 (background conditions) | scientific-reasoning-and-causation.mdx:96–106 | Good. |
| Association / correlation | scientific-reasoning-and-causation.mdx:164 | scientific-reasoning-and-causation.mdx:164; probability-and-statistical-reasoning.mdx:322 | Two terms not linked (S24). |
| Confounder, randomization, blinding | scientific-reasoning-and-causation.mdx:169 | scientific-reasoning-and-causation.mdx:169, 225, 231 | Good. |
| Probability, conditional probability, independence | scientific-reasoning-and-causation.mdx:62 (informal) | probability-and-statistical-reasoning.mdx:27, 65, 77 | Good. |
| Bayes' theorem, likelihood ratio, confirmation | scientific-reasoning-and-causation.mdx:62 (promise) | probability-and-statistical-reasoning.mdx:160, 203, 213 | Good; the promise is kept. |
| Confidence interval, p-value, significance level | probability-and-statistical-reasoning.mdx:21 | probability-and-statistical-reasoning.mdx:250, 297–300 | Good. |
| Value, descriptive and normative claims, is-ought gap | strategic-thinking-and-decisions.mdx (not before) | reasoning-about-values.mdx:26, 39, 73 | Introduced, but the wording is subject to S1. |
| Utility, rights, Hohfeld positions | probability-and-statistical-reasoning.mdx:154 (utility, forward) | reasoning-about-values.mdx:195, 209, 221–226; strategic-thinking-and-decisions.mdx:268 | Good. |
| Expected value, decision rules, EVPI | probability-and-statistical-reasoning.mdx:146 | probability-and-statistical-reasoning.mdx:146; strategic-thinking-and-decisions.mdx:196–262 | Good. |
| Fallacy, cognitive bias | what-is-critical-thinking.mdx:94 | what-is-critical-thinking.mdx:94; fallacies-and-cognitive-biases.mdx:25, 41 | Good. |
| System 1 and System 2 | what-is-critical-thinking.mdx:116 | what-is-critical-thinking.mdx:116 | Good; entry 12 refers back. |
| Creativity (original and effective) | what-is-critical-thinking.mdx:39 | creativity-and-generating-ideas.mdx:26 | Good. |

## Versions, defaults and conventions

| Assumption | Where it appears | Stated in the text? | Assessment |
|---|---|---|---|
| Python 3 version for listings | what-logic-studies.mdx:217 (3.13); probability-and-statistical-reasoning.mdx:21 (3.13); fallacies-and-cognitive-biases.mdx:17 ("Python 3") | Yes | Adequate. Entry 12's listing uses exact integer arithmetic, so its output does not depend on the version. |
| Seeded `random` output | probability-and-statistical-reasoning.mdx:106, 268 | Yes (seed and 3.13) | Reproduced exactly on 3.13.16. |
| Logical symbols | series file line 22; sentential-logic.mdx:22 | Yes | Consistent throughout (no ⊃, ~ or &). |
| Inclusive "or" as default | what-logic-studies.mdx:85–87; sentential-logic.mdx:75 | Yes | Consistent. |
| "Some" means at least one | categorical-logic-and-venn-diagrams.mdx:44 | Yes | Consistent with entry 7. |
| Boolean (modern) reading of categorical statements | categorical-logic-and-venn-diagrams.mdx:23, 97 | Yes | Consistent with predicate-logic.mdx:61. |
| Lemmon-style natural deduction with dependencies | sentential-logic.mdx:229; predicate-logic.mdx:182 | Yes | Consistent. |
| Truth values T and F | sentential-logic.mdx:22 | Yes | Consistent. |
| Money and utility units | strategic-thinking-and-decisions.mdx:21 (thousands of dollars); reasoning-about-values.mdx:195 (illustrative units) | Yes | Adequate. |
| One-sided and two-sided tests, α | probability-and-statistical-reasoning.mdx:304, 365 | Yes | Adequate. |
| z and t multipliers for a 95% interval | probability-and-statistical-reasoning.mdx:254 | Yes | Adequate. |
| Decision-tree notation | strategic-thinking-and-decisions.mdx:251 | Yes (diamond in place of square) | Adequate; see S20 for the separate ISO claim. |
| Flowchart symbols (ISO 5807) | strategic-thinking-and-decisions.mdx:78 | Yes | Overstated for the series as a whole (S20). |
| SI units and number formatting | throughout | Yes | Consistent (thin-space thousands in math, commas in prose). |

## Series design

**Purpose, audience and scope.** The overview names the reader (anyone who wants to reason carefully, with no background in philosophy or logic), the prerequisites (school algebra and a few Python 3 listings) and five checkable objectives. It still does not say what is out of scope (S22).

**Sequence and rationale.** The order follows "the order in which a careful reasoner meets a claim", and the overview explains it: meaning, then argument, then formal logic, then evidence, values, decisions, errors and generation. The order works for the stated reader. The logic block (entries 4 to 7) moves cleanly from informal form, through categorical and sentential logic, to predicate logic, and each later entry refers back rather than repeating (B1, B3 and B4 resolved this).

**Prerequisites and dependencies.** Nothing depends on a later entry. Forward pointers (entries 2, 3 and 4 to entries 6 and 7 for symbols; entry 8 to entry 9 for Bayes and correlation; entry 9 to entry 11 for utility) are all kept.

**Notation and depth.** Notation is uniform. The depth is deliberately uneven but stated: entries 6, 7, 9 and 11 are computational, with derivations and exercises, and entries 1, 10, 12 and 13 are conceptual with worked cases. Every entry has exercises with answers, a summary table and references.

**Overview completeness.** The description matches the entries, the objectives are covered (see the table above) and the Python prerequisite sentence is now accurate (C23). The originality sentence ("the text, examples and figures of this series are original") will hold only after S1 and S2, and preferably S5, S8 and S13, are resolved.

## Series-level notes

- **Originality.** After the first wave's corrections, verbatim overlap with the HKU modules is negligible. A 6-word scan finds only formulas, truth-table rows, standard phrases ("deciding what to believe or do", "post hoc ergo propter hoc"), the cited bat-and-ball item and the quoted Franklin sentence. The second pass therefore relied on a side-by-side reading of each module. Entries 5, 6, 7 and 13 are clean. Entries 3 and 4 are now original in wording and examples. Entry 8 is original except for the residue in S8. Entry 10 had not been rewritten outside §§5.2, 6.2 and 8 and is the main problem (S1). Entry 9 kept one HKU worked example (S2). Entries 1, 2, 11 and 12 keep a few borderline structural echoes (S3, S5, S13, S21).
- **Corrections that left their summaries behind.** Three summary tables were not updated when their bodies were corrected (S3, S6, S11). When findings are resolved, every summary row should be checked against the section it summarizes.
- **Terminology.** "Statement", "valid/strength", "hidden assumption", "contrary/contradictory", "confirms/disconfirms" and "bridging premise" are used consistently across entries. The exceptions are "obscurity" in entry 2 (S4) and association against correlation across entries 8 and 9 (S24).
- **Cross-reference map.** Every "(nth entry, Section x.y)" reference in the 13 entries was checked against the target's current headings, including the sections renamed in the first wave: entry 1 §1.2, entry 2 §5.4, entry 3 §6.3, entry 6 §3.3, entry 8 §§1 to 9, entry 10 §8, entry 11 §§1.1, 1.2, 2.1, 2.3 and 5.1, and entry 13 throughout. All resolve to sections that say what is claimed, except S12; S25 lacks a section number. "Next entry" links all match the series order. Entry 13 closes the series against the five objectives.
- **References.** All 13 entries use the simplified IEEE format. Copi (2011) and Lau ("J. Y. F. Lau") are now uniform. The remaining inconsistencies are minor (S14, S15). Several entries list textbooks they never cite in the body (Copi, Hurley, Lau, Lau and Chan). This is acceptable as "sources relied on" and was not raised as a finding.
- **Tone and structure.** Numbering, opening paragraphs, summaries and closing hand-offs are uniform. Figure conventions are the one visible structural difference (S16).

## Verification log

- `npm run build:local`: not re-run in this pass, as instructed. The caller reports `SITE_URL=https://acrr.asia npm run build` and `npm run eos -- validate-site` passing on the current tree. `dist/` was built at 20:59:23. HEAD (b7cf217, 20:59:57) changes only reference lines (the Critical Thinking Web entry) and does not affect any check below.
- `npm run check:links`: re-run on the existing `dist/`: "Checked 449 pages and 14119 internal references in dist. All internal links resolve."
- `npm run eos -- lint` on the 13 entries and the series file: 0 errors, 0 warnings, 57 suggestions (sentence length, serial-comma heuristics, "clearly"); none is reported as a finding.
- Rendered pages: no Mermaid diagram in the 13 entries has a min-width above 348 px (limit about 600 px). There is no text glued to inline elements; the three regex hits were inside KaTeX markup, plus the straight quote reported as S23.
- Code listings re-run with Python 3.13.16 (`python3 -I`):
  - Entry 4 §6.2: output `A is a knight, B is a knave`, identical to the text. The Exercise 7 variant (`says_a = b`, `says_b = not a`) prints nothing, as stated.
  - Entry 9 listing 1: `11/36`, `0.5177`, `0.4914`, `0.333` / `0.667`, identical.
  - Entry 9 listing 2: `expected 10, sd 3.13, z 2.24, one-sided p = 0.0257`, `0.936`, `0.948`, identical.
  - Entry 12 §6.5: `0.768`, `0.458`, `0.237`, identical.
- Recomputed with Python, all correct:
  - Entry 1: 45 km/h; bracket \$5; 160 samples/s.
  - Entry 2: T = 43 200 min; allowance 43.2 min; availability 99.775% and 99.907%.
  - Entry 3: 0.999, 0.9, 0.5.
  - Entry 6: the eight-row table (T F T F F F T T); the short-method examples; Exercise 1(d) witness; Exercise 4(a); the deployment argument.
  - Entry 8: 50/51 = 0.980; 0.098, 0.196 and 0.392 m; 0.5^10 = 0.00098; 0.95^10 = 0.599; 120 − 95 = 25 mA.
  - Entry 9: 11/36; 0.857; 0.9975; 0.1976; false-to-true alarm ratio 4.06; posterior after one alarm 0.198, after two 0.923; margins 0.031, 2401 and 9604; Exercise 3 0.048 and 0.024; 1 − 0.95^20 = 0.642; Exercise 4 exact 0.0176 and 0.0352; Exercise 2 0.269; Simpson rates 20/17%, 5/4%, 8/14.4%; ±1 and ±2 SD 68.27% and 95.45%; simulation SE 0.0015; spare part 500.
  - Entry 10: net utilities 40 and 70; h > 90.
  - Entry 11: weighted 3.50/3.65/3.60 and unweighted 19/17/18; three-way tie at 3.575 when d = 0.025; Exercise 4 3.40/3.75/3.80; EV 43/57/45; Laplace 40/53.3/50; regret table; lines 47 − 20q, 59 − 10q and 33 + 60q; crossover 0.371; perfect-information value 76 and EVPI 19; Exercise 6 41/43/27, 68 and 25; pump −19.2, −24 and −10, EVPI 9.2, q < 0.286.
  - Entry 12: 0.041, 0.255, 0.0905, 0.328, 0.0893.
  - Entry 13: 72, 48, 22, ⌈log2 1000⌉ = 10, ⌈log2 3000⌉ = 12.
  - S2 replacement: 1 − 0.9² = 0.19.
- Verdicts rechecked by hand: Venn region assignments in entry 5 §§3.2, 4.3–4.6 and Exercise 3(a)–(d); counter-models in entry 7 §§6.2 and 7.2 and Exercise 4; the quantifier derivations in entry 7 §7.3 and Exercise 5, including the ∃E and ∀I restrictions; Hohfeld correlatives and opposites against `CtValHohfeld.astro` (labels, legend and caption agree); region numbers in `CtVennValid.astro` and `CtVennInvalid.astro` against the prose.
- Originality: a 5- and 6-word n-gram scan of each entry against its HKU module (`/home/user/hku-think/{critical,meaning,arg,logic,venn,sl,pl,sci,stat,value,strategy,fallacy,creativity}.md`), then a side-by-side structural read of the module sections behind every entry. The source passages quoted in S1, S2, S5, S8, S13 and S21 were located by line. The Hohfeld definitions in entry 10 §9.1 share a formula with HKU U10, but they are Hohfeld's standard definitional schema and were not raised.
- Not verified:
  - The page range of Kuhn's chapter in *The Essential Tension* (S15).
  - Hill's exact wording, which is quoted in S9 from memory of Hill (1965, p. 299). The point that he did not exempt temporality is held with confidence, but the exact page was not checked here.
  - Bibliographic details of references added in the first wave (Govier 7th ed. 2010; Rosenthal 1979; Kuhn 1977; Svenson 1981; Boden 2004; Campbell 1960; Gentner 1983; Jansson and Smith 1991): consistent with what is known, but not checked against catalog records.
  - The URL of the *Critical Thinking Web* was not fetched.
- Third pass (independent verification, English text at commit 4c5f134; later commits add only Vietnamese translations, which were not reviewed here):
  - S resolutions: each of S1 to S25 checked against the current text of the named file and line. All resolved or justifiably declined (S16), except the optional S15 items (Copi in-text form in entry 8, Kuhn page range). New finding T1 (Should fix), `reasoning-about-values.mdx:20`.
  - Originality: 6-word n-gram scan of all 13 entries against their HKU modules (critical, meaning, arg, logic, venn, sl, pl, sci, stat, value, strategy, fallacy, creativity). Every run of 6 or more words is a standard term or definition ("deciding what to believe or do", "if and only if there is no possible situation", "X is a necessary condition for Y", "it is not the case that", "there is at least one x such that", "lie within one standard deviation of the mean", "after this, therefore because of this", the Hohfeld schemas), a truth-table row or formula, the cited bat-and-ball item, Franklin's quoted sentence, or a reference title. 5-word scan of entries 9 and 10: only formulas, standard phrases and reference titles. Side-by-side read of entry 10 against `value.md` U01 to U06: the flagged devices are gone and the examples are the entry's own; the top-level order follows U01 to U10, as the overview discloses. Entry 9 §2.1 and listing 1 no longer share an example with `stat.md`.
  - Listings re-run with Python 3.13.16 (`python3 -I`), extracted from the article: entry 9 listing 1 (`11/25`, `0.5177`, `0.4914`, `0.333` / `0.667`) and listing 2 identical to the quoted output. Entries 10 and 11 have no listings.
  - Recomputed: entry 9 §2.1, 0.2 + 0.3 − 0.06 = 0.44 = 1 − 0.8 × 0.7 = 11/25; entry 11 §2.2, 1 + 4 + 6 + max(9, 5) + 1 = 21, halving the short shard saves 0, the long shard 4 (max(4.5, 5) = 5), caching 4 → 0.5 saves 3.5. All correct.
  - Cross-references: a script extracted every "Section X.Y" reference (prefix and "of the Nth entry" forms) in the 13 entries and resolved it against the target's current headings: 219 resolved; the five unresolved hits were parser mis-attributions, each checked by hand and correct. Cross-entry references were read in context (for example e12:15 → e3 §4.2, e12:145 → e8 §9.1 and e9 §3.4, e9:324 → e8 §6.1, e6:120 → e4 §4.5, e10:41 → e2 §7.1, e11:29 → e10 §2.1); all say what they claim.
  - `npm run eos -- lint --quiet`: 90 files, 0 errors, 1 warning (in `signals-and-systems-in-discrete-time.mdx`, outside this series). Lint of the 13 entries, the series file and the insight: 0 errors, 0 warnings, 66 suggestions.
