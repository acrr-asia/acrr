# Editorial review: Performance Models: Speedup, Scaling Laws and the Roofline

- Path: `src/content/blog/performance-models-and-scaling-laws.mdx` · Route: `/blog/performance-models-and-scaling-laws` · Type: article, series entry 1 of 5 (`parallel-and-high-performance-computing`)
- Reviewed against: `editorial/standards.md` 1.0, `editorial/glossary.json`, `plugins/editorial-os/references/review-protocol.md`, the series overview and the four later entries (headings and the passages that cite this entry)
- Stages in this report: developmental (EOS step 6.1) and copy (6.2), both by an editor who did not write the entry. Line numbers refer to the revised file.

## Developmental review

The entry does its job for the stated reader. The opening states what it covers, what it builds on (the roofline insight), what it assumes, and the conventions for the whole series. Each section opens with its concept before the formula. The argument runs in order: measures, then strong scaling, weak scaling, work and span, the roofline, and measurement practice. Every model is followed by a worked example or a program with its output. Limits are stated section by section, and the Summary leads to the second entry. The eight `##` headings and every existing `###` heading are unchanged. One `###` heading was added, so no fragment that another entry links to changed (eleven distinct fragments are linked from the later entries and all still resolve).

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| D1 | Optional | `:14`, opening | purpose | The opening listed the models as a separate sentence, which read as a table of contents in prose. |
| D2 | Should fix | `:20-22`, Conventions | structure | One 207-word paragraph mixed units, software versions and the reference machine. |
| D3 | Should fix | `:157`, Section 2.4 (formerly 2.3) | structure | The limits of Amdahl's law sat at the end of the subsection on the Karp-Flatt estimate. |
| D4 | Should fix | `:173`, Section 3.1 | consistency | The symbol $n_1$ was used without being defined. |
| D5 | Should fix | `:499`, Section 5.5 | consistency | "the diagnosis of Section 5.1" pointed at a section that contains no diagnosis. |
| D6 | Should fix | `:585`, Section 6.3 | structure | The pointer to the second entry repeated the one in Section 1.4. |
| D7 | Optional | `:312`, Section 4.3 | consistency | "Section 6 shows such a difference" could name the subsection. |
| D8 | Should fix (for fact-checker) | `:398`, Section 5.4 | evidence | Two hardware claims have no source. |
| D9 | Should fix (for fact-checker) | `:60`, Section 2.1 | evidence | The claim that Amdahl's 1967 paper has no formula needs checking against the paper. |

### D1. Opening reads as a list of contents
- **Where:** `src/content/blog/performance-models-and-scaling-laws.mdx:14`, opening paragraph
- **Text:** "They are run time, speedup and efficiency; ... The entry ends with the rules for measuring performance so that the numbers mean what they claim."
- **Problem:** The second half of the paragraph listed the sections without saying what each one answers (standards 6.1, the introduction sets up what follows "without a table of contents in prose").
- **Correction (applied):** Each model is now paired with the question it answers: "Run time, speedup and efficiency say how much faster a program is; the laws of Amdahl and Gustafson bound how far it scales; ... It closes with rules for measuring performance, so that the numbers mean what they claim."

### D2. Conventions paragraph carries two topics
- **Where:** `:20`, after the **Conventions** paragraph
- **Text:** "A floating-point operation (FLOP) is one addition ... figures for other hardware are labeled as assumed." (207 words, lint `paragraph-length`)
- **Problem:** Units and software versions are one topic and the reference machine is another. The later entries cite this machine as "the reference machine", but the term was never introduced as a defined term (standards 5.2, one topic per paragraph; 5.3, define at first use).
- **Correction (applied):** The paragraph is split in two. The second opens "Every timing comes from one **reference machine**: ...". "4 cores" became "four cores", as elsewhere in the entry. GiB, which the entry uses ("16 GiB of memory"), is added to the list of binary units.

### D3. Limits of Amdahl's law placed under the wrong subsection
- **Where:** `:157`, formerly the last paragraph of Section 2.3 "Estimating the serial fraction from measurements"
- **Text:** "Amdahl's law has three limits. It assumes that the parallel part divides evenly ..."
- **Problem:** The paragraph is about the law as a whole and is the bridge to Section 3, not part of the Karp-Flatt estimate. Section 3 has the matching subsection "3.3 Where weak scaling breaks down", and Section 2 had no counterpart.
- **Correction (applied):** A new subsection, `### 2.4 What Amdahl's law leaves out`, holds the paragraph, which now opens "The law has three limits." The fragment `#23-estimating-the-serial-fraction-from-measurements`, linked from the fifth entry (`distributed-memory-and-message-passing.mdx:503`), is unchanged and still points at the Karp-Flatt material it cites.

### D4. Undefined symbol $n_1$
- **Where:** `:173`, Section 3.1
- **Text:** "If $T(p, n)$ is the run time of a problem of size $n$ on $p$ processors, the weak-scaling efficiency is $T(1, n_1)/T(p, p\,n_1)$"
- **Problem:** $n_1$ is not defined (standards 5.5, every symbol is defined at first use).
- **Correction (applied):** "... on $p$ processors and $n_1$ is the problem size given to one processor, the weak-scaling efficiency is ...". The formula itself is unchanged.

### D5. Cross-reference to a diagnosis that Section 5.1 does not contain
- **Where:** `:499`, Section 5.5, last paragraph
- **Text:** "The bound is a ceiling for the diagnosis of Section 5.1, not a prediction."
- **Problem:** Section 5.1 states the bound and refers to the insight; it makes no diagnosis.
- **Correction (applied):** "The bound is a ceiling that shows which resource limits a kernel, not a prediction of its speed."

### D6. Repeated pointer to the second entry
- **Where:** `:585`, Section 6.3
- **Text:** "The second entry explains why the cost of an access depends on which level of the hierarchy holds the data."
- **Problem:** This repeats Section 1.4 almost word for word ("The [second entry] explains why the cost of an access depends on where the data resides"). Standards 6.1 say there should be no redundancy.
- **Correction (applied):** The sentence in 6.3 is cut. The linked first mention in 1.4 remains.

### D7. Cross-reference to a whole section
- **Where:** `:312`, Section 4.3
- **Text:** "Section 6 shows such a difference in a real measurement."
- **Correction (applied):** "Section 6.3 shows ...", where the `-ffast-math` result appears.

### D8. Unsourced hardware claims (for the fact-checker)
- **Where:** `:398` and `:462`, Section 5.4
- **Text:** "Intel has built Xeon processors with one and with two 512-bit FMA units per core" and "on some processors heavy vector load lowers the clock instead"
- **Problem:** Both are factual claims about products with no citation (standards 7.2). Both are plausible and are used only to qualify the peak estimate.
- **Correction:** The fact-checker confirms both against Intel documentation, such as the Intel 64 and IA-32 Architectures Optimization Reference Manual, and adds the source to the References. If no source can be confirmed, the claims should be attributed or softened. The text is left as written.

### D9. Characterization of Amdahl's paper (for the fact-checker)
- **Where:** `:60`, Section 2.1
- **Text:** "G. M. Amdahl argued, in prose and without a formula, that ..."
- **Problem:** This is a claim about the content of a primary source. It is the usual account, but it must be checked against the paper itself (pp. 483–485).
- **Correction:** Verify the claim. Text left as written.

**Developmental verdict: pass.** The five should-fix findings of this stage (D2 to D6) are applied. D8 and D9 are handed to the fact-check stage. They are not this stage's to resolve, and they remain open there.

## Copy edit

`npm run eos -- fix --rules spelling-variant,terminology` applied 0 fixes: the spelling is already American and the house terms are already used. Before the edit, lint showed 0 errors, 0 warnings and 5 suggestions; after it, 0 errors, 0 warnings and 5 suggestions (kept, see C6). There are no em dashes, contractions, "simply/obviously/clearly/of course" or banned phrases. "We" appears only in the derivation step of Section 3.2 ("Substituting this $f$ ..., we find"), which is allowed. Headings are in sentence case.

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| C1 | Should fix | `:16, 240, 264, 318, 336, 680` | language | Serial commas in prose lists (house style: none). |
| C2 | Should fix | `:308, 640, 645`, math at `:310, 497` | consistency | Digit grouping with spaces (`50 000`, `10 000`, `249\,999`), while the series uses commas (`4,096` in the fifth entry, `20{,}000` in math). |
| C3 | Optional | `:14` | language | "is only worth its complexity if" places "only" ambiguously. |
| C4 | Optional | `:336` | language | A 50-word sentence with three verbs, ending in a serial comma. |
| C5 | Optional (for technical reviewer) | `:645`, Exercise 4 answer | accuracy | The answer writes $T_p$ for the 10,000-processor case after writing $T_{100}$ for the first case. |
| C6 | — | lint suggestions | language | Five suggestions kept, with reasons. |
| C7 | Optional | `:392`, Section 5.3 | language | "while the shared host was evidently busier" states an inference as an observation. |

### C1. Serial commas
- **Where:** `:16` "in sequential code, and is comfortable"; `:240` "..., and the processors are identical"; `:264` "evaluates Brent's level-by-level schedule, and compares"; `:318` "depends on data reuse, and measures"; `:336` "will use, and times ten repetitions"; `:680` "reach memory, and how blocking"
- **Problem:** Standards 5.1 call for no serial comma unless leaving it out creates ambiguity.
- **Correction (applied):** The comma is removed in each case. At `:240` the list is reordered ("..., the processors are identical and any processor can run any ready task without first fetching its data") so that "its data and the processors" cannot be misread. The serial comma is **kept** in two places, under the ambiguity exception: the description ("bound run time by work and span, and place a kernel"), where removing it gives "work and span and place", and `:511` "cold caches and translation buffers, and a processor clock", where the middle item contains "and". The code comment at `:517` is code and was not touched.

### C2. Digit grouping
- **Correction (applied):** Prose `50 000` became `50,000`, and `10 000` became `10,000` (three places). In math, `249\,999 + 2 = 250\,001` became `249{,}999 + 2 = 250{,}001`, and `98\,304` became `98{,}304`. This matches the `{,}` form used elsewhere in the series. Values are unchanged. Four-digit numbers (1024, 1000) are left without commas to match the program output beside them.

### C3. Placement of "only"
- **Correction (applied):** "A parallel program is worth its complexity only if it is faster".

### C4. Long sentence in Section 5.3
- **Text:** "It allocates three arrays ... (320 MB each, ...), initializes them in parallel so that each thread touches the pages it will use, and times ten repetitions of the triad."
- **Correction (applied):** "It allocates three arrays ... and initializes them in parallel, so that each thread touches the pages it will use. It then times ten repetitions of the triad."

### C5. Notation in the Exercise 4 answer (for the technical reviewer)
- **Where:** `:645`
- **Text:** "On 100 processors, $\max(10^4, 10^3) = 10^4 \le T_{100} \le ...$ ... On 10,000 processors, $\max(100, 1000) = 1000 \le T_p \le 1100$"
- **Problem:** The answer is inconsistent within itself. $T_{10000}$ (or $T_{10^4}$) would match the first case. Equations are outside the copy editor's remit, so the text is left as it is.

### C6. Lint suggestions kept
- `14:316 sentence-length` (46 words): a semicolon list of four parallel clauses, one item per model, only one word over the guide. Splitting it would break the parallel structure.
- `20:451 acronym-expansion` "GNU": part of the proper name "GNU Compiler Collection", which is itself the expansion of GCC. GNU is a recursive name, not an abbreviation with a useful expansion.
- `336:221 acronym-expansion` "STREAM": the name of McCalpin's benchmark, written in capitals by its author. It is not an abbreviation.
- `505:90 sentence-length` (48 words): a single list of six parallel failure modes that the following subsections take up. Splitting it would separate items of one list.
- `685:93 acronym-expansion` "ACM": appears only inside reference entries, in the journal title *Journal of the ACM* / *Communications of the ACM*, which keeps the original form (standards 7.3).

### C7. "evidently busier"
- **Where:** `:392`
- **Problem:** The host's load was not observed. It is inferred from the low rates. The meaning is clear from "made while", so this is left for the author, with a suggested change to "presumably busier" or "when the shared host was apparently busier". The text is unchanged, because the change would alter how strongly the claim is made.

**Copy verdict: pass.** C1 and C2, the should-fix findings, are applied. C5 is handed to the technical reviewer. C7 is optional and left to the author.

### Changes made in these two stages
- Opening: the models are now tied to the questions they answer; "only" is placed correctly.
- Conventions: split into units and software, and the reference machine (now a defined term); "four cores"; GiB listed.
- New `### 2.4 What Amdahl's law leaves out` holds the paragraph on the law's limits. No existing heading was renamed or renumbered.
- Section 3.1: $n_1$ defined. Section 4.2: list reordered. Section 4.3: "Section 6.3". Section 5.3: long sentence split. Section 5.5: cross-reference fixed. Section 6.3: duplicate pointer cut.
- Serial commas removed (six places, two kept for ambiguity). Digit grouping set to commas in prose and `{,}` in math.
- No technical claim, number, equation, code block, program output, unit, citation or link target was changed.

### Open for later stages
- Fact-check: D8 (Intel FMA unit counts; vector-load clock reduction), D9 (Amdahl's paper has no formula).
- Technical review: C5 ($T_p$ versus $T_{10000}$ in the Exercise 4 answer).
- Translation: none exists yet (`src/content/blog/vi/` has no file for this entry), so nothing is marked for update.

<!-- Later stages (fact-check, technical review, resolution, QA) add their sections below. -->
