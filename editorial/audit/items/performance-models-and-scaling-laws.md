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

## Fact-check

Stage EOS 6.3, by a reviewer who did not write or revise the entry. Line numbers refer to the file as it stands after the copy edit.

**Tool limits.** In this session WebFetch and direct HTTPS (curl) could not reach any bibliographic host (DNS failure for WebFetch; the egress proxy refused dblp.org, doi.org, api.crossref.org, openmp.org and gcc.gnu.org). Only WebSearch worked. So each reference below was checked against the publisher, catalogue or standards-body records that the search results quote (ACM, Crossref, IEEE Xplore, WorldCat, Intel, the author's own publication page). No primary text was opened. Where the check rests on secondary sources only, the Verification table says so.

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| F1 | Should fix | `:398`, Section 5.4 | evidence | (D8, first claim) The statement that Intel built Xeons with one and with two 512-bit FMA units per core is true but has no citation. It is a hardware fact about machines other than the reference machine. |
| F2 | Should fix | `:684`, References | evidence | The Amdahl entry has no volume number (AFIPS Conference Proceedings, vol. 30). |
| F3 | Should fix | `:689`, References | evidence | The Hoefler and Belli entry has no page numbers (article 73, pp. 73:1–73:12). |
| F4 | Optional | `:462`, Section 5.4 | evidence | (D8, second claim) "on some processors heavy vector load lowers the clock instead" is true and hedged. It could name its source. |
| F5 | Optional | References | evidence | DOIs exist and could be added (standards 7.3 prefers DOIs to URLs). |

### F1. Number of AVX-512 FMA units per core (D8, first claim)
- **Where:** `:398`, Section 5.4 "The peak arithmetic rate"
- **Text:** "Intel has built Xeon processors with one and with two 512-bit FMA units per core, and the virtual machine reports only a generic model name"
- **Problem:** The claim is correct, but it is not attributed. CLAUDE.md requires that figures for hardware other than the reference machine be cited or labeled as assumed, and standards 7.2 apply. Evidence: Intel's product specification pages list "# of AVX-512 FMA Units" as 1 for the Xeon Silver 4114 and 2 for the Xeon Gold 6148. The table of contents of the *Intel 64 and IA-32 Architectures Optimization Reference Manual* (order no. 248966; revisions 042b and 050 as indexed) has a Skylake-server example titled "Identifying One or Two FMA Units" (Example 17-24 in one revision, 17-30 in another). A Dell HPC white paper on Skylake BIOS settings and Colfax Research's AVX-512 study agree: two-unit models reach 32 DP FLOP/cycle and one-unit models 16.
- **Correction:** Keep the sentence and attribute it: "Intel has built Xeon processors with one and with two 512-bit FMA units per core (its optimization manual shows how to tell the two apart), and the virtual machine ...". Add to the References: `Intel Corporation, *Intel 64 and IA-32 Architectures Optimization Reference Manual*, order no. 248966, <revision and year as printed on the copy consulted>.` Whoever resolves this must open the manual to read the revision and year. I could not, and the citation must not be completed by guessing. If the manual cannot be opened, write "Intel's product specifications list one or two AVX-512 FMA units per core, depending on the Xeon model" and leave the reference out. Do not invent a citation for a specification page that was not fetched.

### F2. Amdahl reference: volume missing
- **Where:** `:684`
- **Text:** "in *Proceedings of the AFIPS Spring Joint Computer Conference*, pp. 483–485, 1967."
- **Problem:** The IEEE Xplore record of the 2007 reprint (document 4785615) gives the source as "AFIPS Conference Proceedings, Vol. 30 (Atlantic City, N.J., Apr. 18–20), AFIPS Press, Reston, Va., 1967, pp. 483–485". Gustafson (1988) cites it the same way. Standards 7.3 call for the volume when there is one.
- **Correction:** `G. M. Amdahl, "Validity of the single processor approach to achieving large scale computing capabilities," in *AFIPS Conference Proceedings, Spring Joint Computer Conference*, vol. 30, pp. 483–485, 1967.`

### F3. Hoefler and Belli reference: pages missing
- **Where:** `:689`
- **Problem:** The ACM proceedings record (DOI 10.1145/2807591.2807644; the authors' publication page at USI/ETH) gives "pages 73:1–73:12", Austin, TX, November 2015.
- **Correction:** `... in *Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis (SC15)*, pp. 73:1–73:12, 2015.`

### F4. Frequency reduction under vector load (D8, second claim)
- **Where:** `:462`
- **Text:** "on some processors heavy vector load lowers the clock instead"
- **Problem:** None in substance. Intel support documentation says that AVX-512 code may make a processor run below its marked frequency to stay within its thermal design power. Its example is the Xeon 4114, with a base frequency of 1.1 GHz in AVX-512 mode and 2.2 GHz otherwise. The claim is already hedged and makes no figure depend on it.
- **Correction (optional):** "on some processors, as Intel documents for its Xeon Scalable processors, heavy AVX-512 load lowers the clock instead". If the F1 manual reference is added, cite it here only after confirming that the manual covers frequency behavior. Otherwise leave the sentence as it is.

### F5. DOIs
- **Correction (optional):** Roofline 10.1145/1498765.1498785; Gustafson 10.1145/42411.42415; Hoefler and Belli 10.1145/2807591.2807644 (all confirmed in Crossref/ACM records as quoted by search). Karp and Flatt: the DOI could not be confirmed, so add none.

### D9 resolved: Amdahl's paper has no formula
The claim "argued, in prose and without a formula" (`:60`) agrees with the secondary literature. A. Karbowski, "Amdahl's and Gustafson-Barsis laws revisited" (arXiv:0809.1177, 2008), says: "although in the original Amdahl's paper there were no equations, one may present his concept formally based on the verbal description." The excerpts of the paper found by search give its argument in words and numbers: a housekeeping fraction of about 40% of executed instructions, which he judged sequential, and from it an upper limit on throughput of five to seven times the sequential rate. They give no equation. Gustafson (1988) also restates the bound as 1/s in his own notation. I could not open the three-page primary text, so the claim is listed under Not verified as "not checked against the primary text". No change is needed: two independent secondary sources support it and none contradicts it. If the resolver wants the wording to rest only on what was verified, "argued in prose, with numerical estimates rather than a formula" is equally accurate.

### Verification table

| Claim | Location | Status | Source |
|---|---|---|---|
| Amdahl 1967, AFIPS SJCC, pp. 483–485 | `:60`, `:684` | Verified; volume added (F2) | IEEE Xplore 4785615 (reprint record); Gustafson 1988 reference list |
| Amdahl's paper states the argument without a formula | `:60` | Verified (secondary) | Karbowski, arXiv:0809.1177; excerpts of the paper |
| Hennessy and Patterson, 6th ed., Morgan Kaufmann, 2017, give the formula form | `:60`, `:688` | Bibliography verified (ISBN 978-0-12-811905-1, Dec. 2017); content not opened | Elsevier and retailer catalogue records |
| Gustafson, CACM 31(5):532–533, 1988; scaled speedup $s + p\,N$ form, 1024-processor context | `:163`, `:687` | Verified | ACM record, DOI 10.1145/42411.42415 |
| Karp and Flatt, CACM 33(5):539–543, 1990; "experimentally determined serial fraction", formula $e = (1/S - 1/p)/(1 - 1/p)$ | `:147–150`, `:691` | Verified (citation from catalogue; formula from secondary sources) | ACM CACM listing; IxDF index; lecture notes and arXiv:1902.02104 reproducing the formula |
| Graham, BSTJ 45(9):1563–1581, 1966; list scheduling | `:238`, `:686` | Verified | Nokia Bell Labs record; archive.org scan listing |
| Brent, JACM 21(2):201–206, 1974; level-by-level bound | `:238`, `:685` | Verified | Brent's publication page (ANU), reprint header "Vol. 21, No. 2, April 1974, pp. 201-206"; Lemma 2 |
| Williams, Waterman and Patterson, CACM 52(4):65–76, 2009 | `:318`, `:694` | Verified | Crossref 10.1145/1498765.1498785; DBLP listing |
| McCalpin, TCCA Newsletter, pp. 19–25, Dec. 1995; STREAM triad | `:336`, `:692` | Verified (secondary reference lists) | McKee, "Reflections on the memory wall" (ACM CF 2004) and other reference lists; McCalpin's own page hosts the paper |
| STREAM counts 24 bytes per triad element | `:339–341` | Verified | STREAM convention (McCalpin's documentation, as quoted by search); consistent with entry 2 |
| Hoefler and Belli, SC15; reviewed published results and proposed rules | `:505`, `:689` | Verified; pages added (F3) | ACM record 10.1145/2807591.2807644; abstract (120 papers reviewed, rules proposed) |
| IEEE Std 1003.1-2017, Issue 7, IEEE, 2018 | `:690` | Verified | WorldCat/IEEE listing (published 2018; superseded by 1003.1-2024) |
| `CLOCK_MONOTONIC` cannot be set and is not affected when the time is set | `:509` | Verified | POSIX.1-2017 `clock_getres` page (man-pages 3p mirror of IEEE Std 1003.1-2017) |
| `clock()` returns processor time | `:509` | Verified (C17 7.27.2.1, from knowledge; not fetched) | ISO/IEC 9899 |
| OpenMP 5.2, November 2021; `omp_get_wtime` returns elapsed wall-clock time in seconds | `:509`, `:693` | Release verified; routine text verified in 5.0/5.1, assumed unchanged in 5.2 | OpenMP ARB press release (9 Nov 2021); OpenMP 5.1 spec HTML |
| Intel Xeons with one or two 512-bit FMA units | `:398` | Verified; citation needed (F1) | Intel product specifications (Silver 4114: 1; Gold 6148: 2); Intel optimization manual ToC; Dell and Colfax |
| Vector load can lower the clock | `:462` | Verified | Intel support article on AVX-512 frequency (Xeon 4114: 1.1 GHz AVX-512 base vs 2.2 GHz) |
| AVX-512 register holds eight doubles; one FMA = 16 FLOP | `:398` | Verified | Arithmetic (512/64 = 8, two operations per lane) |
| Under `-std=c11` GCC does not contract to FMA by default | `:598` | Verified (compiled, see T log) | GCC behavior: `-std=cNN` implies `-ffp-contract=off` (gcc-patches 2013; GCC mailing list, Sept. 2023); disassembly |
| GCC `-march=native` prefers 256-bit vectors | `:598` | Verified (compiled) | `gcc -Q --help=target` shows `-mprefer-vector-width=256`; also for `-march=sapphirerapids`, the target entry 4 says the reference machine selected |
| Reference-machine description (KVM, 4 cores, 2.1 GHz, AVX-512, 48 KiB/2 MiB/260 MiB, 16 GiB, GCC 13.3, Python 3.13) | `:20–22` | Partly verified (see Not verified) | Matches the series brief and the writer's run. GCC 13.3.0 and Python 3.13 confirmed; the VM was re-provisioned before this check |
| Write-allocate on the reference machine's caches | `:332` | Not verified from a fetched source | Standard for x86 write-back memory (Intel SDM vol. 3); consistent with entry 2 Section 2.3 |

### Not verified
- Amdahl's paper has no formula (`:60`): the primary text was not opened (no fetch access). Supported by two secondary sources. No change required.
- Reference-machine hardware (`:22`): `lscpu` in this session reports a different host, an Intel Xeon @ 2.80 GHz (family 6, model 85, stepping 7), with 32 KiB L1d and 1 MiB L2 per core, a 33 MiB L3 and 15 GiB. The VM had been up for 5 minutes, so it was re-provisioned after the writer's run. The article's figures match the series brief and entry 4 (`-march=native` selected `sapphirerapids`), so I consider them the writer's machine, but I could not re-read them. The article should stay as it is.
- Hennessy and Patterson's presentation of Amdahl's law (`:60`): the book was not opened. The bibliographic record is verified.
- OpenMP 5.2 wording for `omp_get_wtime` (`:509`): only the 5.0 and 5.1 texts were seen.
- Write-allocate policy (`:332`) and `clock()` semantics (`:509`): from standard documentation known to the reviewer, not fetched in this session.
- Karp and Flatt DOI: not confirmed, so none is proposed.

**Fact-check verdict: fail** (0 blocking, 3 should fix, 2 optional). Every reference exists and supports the claim attributed to it. The verdict becomes pass once F1 to F3 are applied.

## Technical review

Stage EOS 6.4, by a reviewer who did not write or revise the entry. Scratch files: `/tmp/claude-0/hpc/review/performance-models-and-scaling-laws/`.

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| T1 | Should fix | `:128–141`, Section 2.2 | accuracy | The program shown prints a last line, `p* = sqrt((1-f)/c) = 30.8`, that the quoted output leaves out. |
| T2 | Should fix | `:645`, Exercise 4 answer | accuracy | "a machine of about 1000 processors would give nearly the same run time" is not supported by the bounds. |
| T3 | Should fix | `:596`, Section 6.3 | consistency | The 17% `-ffast-math` gain comes from one execution of each build, which is what Section 6.2 (`:581`) says cannot be told apart from the 15% noise. |
| T4 | Optional | `:645`, Exercise 4 answer | consistency | (C5) $T_p$ for the 10,000-processor case, after $T_{100}$ for the first case. |

### T1. Quoted output is missing the last printed line
- **Where:** `:119–141`
- **Problem:** The code block ends with `print(f"p* = sqrt((1-f)/c) = {((1-f)/c)**0.5:.1f}")`. Running the two article blocks together (`amdahl_article.py`) prints every quoted line exactly and then `p* = sqrt((1-f)/c) = 30.8`. The writer's `output.txt` has that line too. The quoted output stops at `p=128`. The brief requires real output, trimmed only with a visible "...".
- **Correction:** Append the line `p* = sqrt((1-f)/c) = 30.8` after `p=128  S=  5.42  E= 0.04` at `:140`.

### T2. Exercise 4: "about 1000 processors would give nearly the same run time"
- **Where:** `:645`
- **Text:** "so the 10,000 processors run at an efficiency of at most 10%; a machine of about 1000 processors would give nearly the same run time."
- **Problem:** Under the bounds of the exercise, $p = 1000$ gives $\max(1000, 1000) = 1000 \le T_{1000} \le 1000 + 1000 = 2000$. Against $1000 \le T_{10^4} \le 1100$, the guaranteed run time is almost twice as long. The bound guarantees no more than 1.1 times the 10,000-processor time only once $W/p \le 100$, that is $p \ge 10^4$. The bound alone does not support the sentence. It holds only if the real run time on 1000 processors is near its lower bound, which the exercise does not say.
- **Correction:** "... so the 10,000 processors run at an efficiency of at most 10%. No machine can finish in fewer than $D = 1000$ steps, and 1000 processors already guarantee $T_{1000} \le 2000$, so ten times as many processors buy at most a factor of two."

### T3. The `-ffast-math` timing difference is near the stated noise
- **Where:** `:596`, and the rule at `:581`
- **Text:** "The compiler then splits the sum into vector partial sums and the median fell by about 17%" against "A claimed improvement smaller than that [about 15%], measured from one execution of each version, cannot be told apart from the noise of this machine."
- **Problem:** The four builds were "executed once each" (`:587`). 0.811 → 0.667 ms is 17.8% and 0.800 → 0.667 ms is 16.6%, only just above the 15% spread the article itself measured. By its own rule this one comparison barely qualifies. The mechanism is correct: the disassembly shows `vfmadd231pd` with several vector partial sums under `-ffast-math`, against `vmulpd` followed by an in-order chain of scalar `vaddsd` under `-O3 -march=native`. On the re-provisioned host the `-ffast-math` build ran 2.4 times faster (median 0.582 against 1.434 ms), so the effect is real. Its size depends on the machine and is not established by one run.
- **Correction:** "The compiler then splits the sum into vector partial sums. In this single execution the median fell by about 17%, close to the 15% run-to-run spread of Section 6.2, so this run alone shows the direction of the change rather than its size. The result changed in its 14th significant digit ..."

### T4. Exercise 4 notation (C5 resolved)
- **Where:** `:645`
- **Text:** "$\max(100, 1000) = 1000 \le T_p \le 1100$"
- **Problem:** The first case writes $T_{100}$. By the Conventions (`:18`) $T_p$ is the run time on $p$ processors, so $T_p$ is not wrong, but it is inconsistent within the answer. The values are right (recomputed below).
- **Correction (optional):** "$\max(100, 1000) = 1000 \le T_{10^4} \le 1100$". If T2 is applied, its new sentence uses $T_{1000}$ in the same style.

### Checks with no finding
- **Definitions:** speedup against the best sequential program, relative speedup, efficiency, cost, overhead $T_o = pT_p - T_1$ and cost-optimality are all standard. $E = T_1/(T_1 + T_o)$ follows from $pT_p = T_1 + T_o$. Work, span, parallelism, greedy scheduler, arithmetic intensity, ridge point and write-allocate are standard too.
- **Derivations:** Amdahl bound and limit $1/f$. Efficiency bound $1/(1 + f(p-1))$: $S/p = 1/(fp + 1 - f)$. Half efficiency at $p = 1 + 1/f$. Overhead optimum: $d/dp[(1-f)/p + cp] = 0$ gives $p^* = \sqrt{(1-f)/c}$. The claim that a $\log_2 p$ overhead moves the peak but keeps it holds: $(1-f)/p^2 = c/(p\ln 2)$ gives a finite $p^* = (1-f)\ln 2/c$. Karp-Flatt inversion. Gustafson $S_s = f_s + (1-f_s)p = p - f_s(p-1)$. The Amdahl-Gustafson equivalence: $f + (1-f)/p = 1/(f_s + (1-f_s)p)$, verified algebraically and numerically. Dense LU weak scaling: $n \propto \sqrt p$, run time $\propto \sqrt p$, so 8 times at 64 times. Greedy bound $W/p + D$ and its factor-2 corollary. Brent's $\lceil a/p\rceil \le (a-1)/p + 1$ for integer $a \ge 1$, summing to $(W-D)/p + D$. Tree span $\lceil\log_2 n\rceil$ (asserted in the program for $n = 8, 1000, 10^6$). Matrix-multiplication intensities $n/12$, $0.125$, $b/8$; the blocked traffic $16n^3/b$ checked from $(n/b)^2$ blocks times $16nb$ bytes. Roofline and ridge point.
- **Special cases:** $p = 1$ gives $S = 1$ in every model (rows $p=1$ of all tables). $f = 0$ gives $S = p$. $f_s = 0$ gives $S_s = p$. $f_s = 1$ gives $S_s = 1$.
- **Units:** GFLOP/s = GB/s × FLOP/byte. Bytes per element 24 and 32. MB and MiB used as defined (`:20`). 320 MB per array, 960 MB in total (915.5 MiB) beyond 260 MiB.
- **Code:** all seven code blocks were extracted from the article. The C programs (`triad.c`, `fmapeak.c`, `timing.c`) and the Python programs (`reduction.py`, `gustafson.py`, `roofline.py`) are byte-identical to the writer's files. `amdahl.py` differs only by an unused `best` variable and a blank `print()`, and its output matches apart from T1. The FMA kernel compiles to 12 independent `vfmadd132pd` on `zmm` registers in the loop, as described.
- **GCC claims (`:596–598`), compiled with GCC 13.3.0:** with `-std=c11 -O3 -march=native` the triad uses `vmulpd` + `vaddpd` on `ymm`; with `-std=gnu11` it uses `vfmadd132pd`/`vfmadd213pd`. This holds for `-march=native` (now `cascadelake`) and for `sapphirerapids`, `emeraldrapids` and `graniterapids`, all with 256-bit vectors (`-mprefer-vector-width=256`). The dot product is scalar at `-O2`. At `-O3 -march=native` it is a vector multiply followed by seven in-order `vaddsd`. With `-ffast-math` it uses vector FMA partial sums. All as the text states.
- **Consistency with the series:** notation ($T_p$, $S$, $E$, $f$, $f_s$, $W$, $D$, $P_{\mathrm{peak}}$, $B$, $I$, $I^*$, $\alpha$, $\beta$) matches the series brief and the later entries. Entry 2 cites 90.6 GFLOP/s for one core, 7.08 FLOP/byte, 0.125 FLOP/byte without reuse, $b/8$ and 12.3–13.2 GB/s; all agree with this entry. Entry 3 uses $T_p \le W/p + D$. Entry 5 uses Karp-Flatt $e$ and $f_s + (1-f_s)p$. All eleven cross-entry fragments resolve, including the four this entry links to (`#6-predicting-scaling`, `#6-load-balance-and-scheduling`, `#4-blocking-for-reuse`, `#2-vector-instructions-on-a-cpu`).
- **Labels:** every timing is tied to the reference machine and called noisy. $B$ and $P_{\mathrm{peak}}$ are called estimates for this VM. The two-FMA-unit count is marked "not a confirmed figure". The 1.0 s/4 s and 10.0/12.0/3.5 s examples are labeled assumed. Nothing is presented as run that was not.

### Recomputation and run log
Recomputed with Python 3.13.16 (`recompute.py`). Every value agrees with the text.
- 1.2: $S(4) = 2.857$ → 2.86; relative 3.429 → 3.43; $E = 0.714$ → 0.71. 1.3: cost 14.0, $T_o = 4.0$, $E = 10/14 = 0.714$.
- 2.1: $p = 21$, $S(21) = 10.50$; table re-generated, identical. 2.2: $p^* = 30.82$, integer maximum at $p = 31$, $S = 9.038$; $S(8) = 5.69 > S(128) = 5.42$; Amdahl at 32 = 12.549 → 12.55. 2.3: $e = 0.0833$.
- 3.1: $S_s(1024) = 972.85$. 3.2 table identical. 3.3: $64^{1.5}/64 = 8$.
- 4.3: table identical. $991/976.56 - 1 = 1.5\% < 2\%$. Blocked plan $249{,}999 + 2 = 250{,}001 < 250{,}006$.
- 5.2: $2000/12 = 166.67$; $2/24 = 0.0833$. 5.3: $24 \times 4\times10^7/t$ gives 13.17, 12.28, 49.74, 47.06 GB/s for the quoted times, matching 13.2, 12.3, 49.7, 47.1. $13.2/49.7 = 0.27$ ("roughly a quarter"). $32/24 = 1.33$. 5.4: $4 \times 2.1 \times 32 = 268.8$. Four-thread median of {339.7, 347.2, 354.0, 364.2, 366.8} = 354.0; one-thread median = 90.6. Implied clocks 2.766 and 2.831 GHz; with one unit, 5.53 and 5.66 GHz ("about 5.5"). FLOP/cycle 42.1 and 43.1. 5.5: $I^* = 7.08$; 1.18% and 1.77% of peak; $24 \times 64^2 = 98{,}304$ B = 96 KiB; roofline table identical.
- 6.2: max/median per execution 1.71, 1.46, 1.12, 1.62, 1.10 ("up to about 1.7"). Median spread $0.834/0.727 - 1 = 14.7\%$ ("about 15%"). GFLOP/s from the medians 2.78, 2.53, 2.51, 2.62, 2.88 (identical). 6.3: $13.2 \times 0.125 = 1.65$ (text "1.6", from the unrounded 13.17 × 0.125 = 1.646). $-O0/-O2$ medians $3.448/0.800 = 4.3$ ("about four times"). `-ffast-math` 16.6–17.8% (T3). 14th significant digit differs (…93**6**799 against …93**7**785).
- Exercises: Ex1 19.753 → 19.75, $E = 0.617$, limit 50. Ex2 0.0526, 0.0588, 0.0612. Ex3 57.7, $f = 0.001733$. Ex4 bounds 10,000–11,000 and 1000–1100; speedups ≥ 90.9 and ≥ 909.1, ≤ 1000; efficiency ≤ 10%. Ex5 $I = 0.1667$, 8.33 GFLOP/s, 2.35% ("about 2.4%").

Runs (GCC 13.3.0, `flock /tmp/claude-0/hpc/bench.lock`, each locked run under 20 s). **The host had changed:** `lscpu` now reports a KVM guest on an Intel Xeon @ 2.80 GHz (model 85, stepping 7, AVX-512), with 32 KiB L1d, 1 MiB L2 and 33 MiB L3. So these runs check behavior and order of magnitude, not the reference machine's figures.
- Deterministic outputs: the dot product printed `14.440159752936799` for the `-O0`, `-O2` and `-O3 -march=native` builds and `14.440159752937785` for `-ffast-math`, exactly as quoted. The triad check printed `a[N-1]=7.0`.
- Triad (`-O3 -march=native -fopenmp`, `OMP_PROC_BIND=close`): 1 thread best 11.7, median 11.4 GB/s. 4 threads best 42.5, median 38.8 GB/s. Five further 4-thread runs gave best 42.6–44.8 GB/s. The ratio of one core to four is 0.27, the same "roughly a quarter" as the article.
- FMA microbenchmark (`-O2 -march=native`): 1 thread 64.1–79.2 GFLOP/s, 4 threads 242.0–293.5 GFLOP/s (median 272.7). Scaling with four threads is near-linear, as in the article. On this host the implied 4-thread clock, 272.7/128 = 2.13 GHz, is below the reported 2.8 GHz. That is consistent with the article's caveat that heavy vector load can lower the clock (`:462`).
- Dot-product timing (`-O2`, five executions): medians 1.393–1.839 ms. By flags: `-O0` 3.199, `-O2` 1.408, `-O3 -march=native` 1.434, `-ffast-math` 0.582 ms. Qualitatively the same as the article: `-O0` is far slower, `-O3 -march=native` brings no gain, and `-ffast-math` is faster with a different last digit.

**Technical verdict: fail** (0 blocking, 3 should fix, 1 optional). Every equation, derivation and quoted number is correct. Every deterministic output reproduces exactly, and the code in the article is the code that produced the output. The verdict becomes pass once T1 to T3 are applied.

## Resolution

EOS step 7, by the author. Every should-fix finding of the fact-check and technical stages is applied with the reviewers' proposed text, unless noted. No measured number was changed: none of the findings required it, and the reference machine is no longer available for re-runs. `npm run eos -- lint` on the article: 0 errors, 0 warnings (5 suggestions kept, as listed in C6).

| ID | Severity | Resolution |
|---|---|---|
| F1 | Should fix | Applied with the fallback wording, because the optimization manual could not be opened and no revision or year can be cited. Section 5.4 now reads "Intel's product specifications list one or two AVX-512 FMA units per core, depending on the Xeon model, and the virtual machine ...". No reference was added. |
| F2 | Should fix | Applied: the Amdahl reference now reads "in *AFIPS Conference Proceedings, Spring Joint Computer Conference*, vol. 30, pp. 483–485, 1967." |
| F3 | Should fix | Applied: pages 73:1–73:12 added to Hoefler and Belli. |
| F4 | Optional | Applied in the proposed form, with no citation: "on some processors, as Intel documents for its Xeon Scalable processors, heavy AVX-512 load lowers the clock instead". The manual was not added (F1), so it is not cited here either. |
| F5 | Optional | Applied only for the three DOIs the reviewer confirmed: Williams et al. 10.1145/1498765.1498785, Gustafson 10.1145/42411.42415, Hoefler and Belli 10.1145/2807591.2807644, written as ", doi: ...". None was added for Karp and Flatt. |
| D9 | Note | No change. Two secondary sources support "in prose and without a formula", and the primary text is still listed under Not verified. |
| T1 | Should fix | Applied: `p* = sqrt((1-f)/c) = 30.8` appended to the quoted output in Section 2.2. It matches the writer's `output.txt`. |
| T2 | Should fix | Applied: the Exercise 4 answer now ends "No machine can finish in fewer than $D = 1000$ steps, and 1000 processors already guarantee $T_{1000} \le 2000$, so ten times as many processors buy at most a factor of two." |
| T3 | Should fix | Applied: Section 6.3 now says that in this single execution the median fell by about 17%, close to the 15% run-to-run spread of Section 6.2, so the run shows the direction of the change rather than its size. The sentence on the 14th significant digit is kept. |
| T4 | Optional | Applied: $T_p$ changed to $T_{10^4}$ in the Exercise 4 answer. |

Developmental and copy findings (D1–D8, C1–C7) were resolved by the editors in their own stages, as recorded above. The author did not reopen them.

## QA

EOS step 10, 2026-10-16, by an independent QA editor who did not write, review or revise the entry. Record: `editorial/records/article/performance-models-and-scaling-laws.json`.

**Decision: revise** (total 23/28; critical C1 and C8 hold because of Q1). The entry is publishable once Q1 is applied and QA is recorded again.

| Dimension | Score | Reason below 4 |
|---|---|---|
| purpose | 4 | |
| structure | 4 | |
| accuracy | 2 | Q1: the OpenMP reduction is described as a tree combine, which GCC 13.3 does not do and the specification does not require. |
| evidence | 3 | The two Intel hardware statements in Section 5.4 are attributed but have no reference entry (the fact-checker could not open the documents). |
| language | 3 | "evidently busier" (Q2, copy C7) states an inference as an observation. |
| consistency | 3 | In-text citations have no years, while entries 2, 4 and 5 give them (series F18, deferred). OpenMP is not expanded here, but entry 2 expands it. |
| publishing | 4 | |

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| Q1 | Blocking | `:311`, Section 4.3 | accuracy | OpenMP reductions are said to combine partial sums by a tree. |
| Q2 | Optional | `:393`, Section 5.3 | language | "evidently busier" (copy C7, not applied). |

### Q1. OpenMP reductions are not tree combines
- **Where:** `src/content/blog/performance-models-and-scaling-laws.mdx:311`, Section 4.3
- **Text:** "Each processor sums a contiguous block of $n/p$ numbers sequentially, then the $p$ partial sums are combined by a tree. ... This is how the reduction operations of OpenMP and of message-passing libraries work, as the third and fifth entries show."
- **Problem:** The OpenMP specification leaves the order of combination unspecified, and the third entry says so (Section 2.3, `threads-and-shared-memory-parallelism.mdx:136`). GCC 13.3, the compiler of the series, combines the per-thread copies one after another with atomic updates. A QA compile of a `reduction(+:s)` loop with `gcc -std=c11 -O2 -fopenmp -fdump-tree-ompexp` shows `__atomic_load_8` and `.ATOMIC_COMPARE_EXCHANGE`, with no tree. The tree combine is correct for MPI, as the fifth entry shows in Section 4.2 (binomial tree, recursive doubling). So the sentence states something false about OpenMP, and the third entry does not show what the sentence says it shows.
- **Correction:** Replace the last sentence of the paragraph with: "Library reductions follow the same pattern of private partial sums combined at the end. An OpenMP `reduction` clause leaves the order of combination unspecified, and GCC 13.3 adds each thread's partial sum into the result with an atomic update, one after another. Message-passing libraries typically combine the partial sums along a tree. The third and fifth entries show both."

### Q2. "evidently busier" (optional)
- **Where:** `:393`
- **Text:** "Earlier trial runs, made while the shared host was evidently busier, gave medians as low as 17 GB/s"
- **Correction:** "made while the shared host was apparently busier".

### Checks
- `eos lint`: 0 errors, 0 warnings, 5 suggestions, each justified in the copy edit. `eos validate-site dist`: no issues. `dist/blog/performance-models-and-scaling-laws.html` is newer than the source, and its title and description are correct.
- Every blocking and should-fix finding of D, C, F and T, and the series findings F4, F7 and F10, is present in the text.
- Recomputation: QA reran `amdahl.py` (identical except for trailing spaces in the header line), the Gustafson program, the tree-reduction program and `roofline.py` (all identical). In Python, QA recomputed the Section 2-3 figures, Exercises 1-3 and 5, the triad rates, the FMA medians and implied clocks, the ridge point and its percentages, the 14.7% spread and the 16.6-17.8% `-ffast-math` change. All agree with the text.
- Every quoted timing block appears verbatim in the writer's `output.txt`.
- References checked against the fact-check table: Amdahl, Gustafson and Brent. All agree.
- Cross-references to entries 2-5 and to the two insights resolve and say what is claimed, except the third-entry half of Q1.
- The opening states the purpose, prerequisites and conventions. The ending leads to the second entry.

### Not verified
- Reference-machine timings: the VM is gone, and the text presents them as measurements of that stated machine.
- The primary text of Amdahl (1967), Hennessy and Patterson, and the OpenMP 5.2 wording for `omp_get_wtime`.
- The Intel documents behind the two Section 5.4 attributions.
- The series review is resolved but not yet stamped (`series-pipeline gate`: "never stamped").

## Resolution of the QA findings

- Q1 (blocking): applied. Section 4.3 now says that an OpenMP `reduction` leaves the order of combination unspecified, that GCC 13.3 combines with atomic updates one after another (the QA editor checked this with `-fdump-tree-ompexp`), and that message-passing libraries typically combine along a tree. It also says that the third entry treats the OpenMP clause and the fifth the message-passing reductions. This wording differs slightly from the QA editor's last sentence, which had both entries showing both cases.
- Q2 (optional): applied ("apparently busier", the copy edit's C7).

### QA, second pass (after the resolution of Q1 and Q2)

**Decision: publish** (total 26/28). No critical condition holds, and no finding is open. The record `editorial/records/article/performance-models-and-scaling-laws.json` was written again; its history keeps the earlier revise record.

| Dimension | Score | Reason below 4 |
|---|---|---|
| purpose | 4 | |
| structure | 4 | |
| accuracy | 4 | |
| evidence | 3 | The two Intel hardware statements in Section 5.4 are attributed but have no reference entry. |
| language | 4 | |
| consistency | 3 | In-text citations have no years (series F18, deferred), and OpenMP is not expanded here, though entry 2 expands it. |
| publishing | 4 | |

- **Q1 resolved.** The passage at `:311` now says three things. An OpenMP `reduction` leaves the order of combination unspecified. GCC 13.3 adds each thread's partial sum with an atomic update, one after another. Message-passing libraries typically combine the partial sums along a tree.
- The passage agrees with entry 3, Section 2.3 (`threads-and-shared-memory-parallelism.mdx:136`, "The order of combination is unspecified"), and with entry 5, Section 4.2 (binomial-tree reduction, recursive doubling). The GCC statement matches the QA check with `-fdump-tree-ompexp`.
- The author's last sentence, "The third entry treats the OpenMP clause and the fifth the message-passing reductions", is more accurate than the QA text it replaced, and it is accepted.
- **Q2 resolved:** the text now reads "apparently busier".
- The article diff touches only lines 311 and 393.
- `eos lint`: 0 errors, 0 warnings, 5 suggestions (unchanged and justified). `eos validate-site dist`: no issues. The rebuilt page is newer than the source and renders the new passage, with no glued inline elements.
- This edit changes the series content hash, so the series review has to be stamped against the current text.
