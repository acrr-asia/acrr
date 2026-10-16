# Editorial review: Distributed Memory and Message Passing

- Path: `src/content/blog/distributed-memory-and-message-passing.mdx` · Route: `/blog/distributed-memory-and-message-passing` · Type: article (series entry) · Series `parallel-and-high-performance-computing`, entry 5 of 5 (last)
- Stages in this report: developmental (EOS 6.1) and copy edit (EOS 6.2), done by an editor who did not write the entry. Later sections (fact-check, technical review, resolution, QA) are added by their reviewers.
- Read for this review: the series overview, the article in full, the headings and cited sections of the four earlier entries, `finite-differences-for-heat-and-waves` (Sections 2.1, 2.2) and `solving-large-linear-systems` (Section 4.2). The reproduction script and outputs in the author's work directory (`run.sh`, `model.out`) were consulted as evidence only.

## Developmental review

The entry does its job well. The opening links what it builds on, says what it covers and states versions, machine and units. Each numbered section opens with its concept (distributed memory before MPI calls, blocking semantics before eager and rendezvous, the affine model before the ping-pong, collective semantics before their algorithms, decomposition before ghost cells), the worked examples are run with real output, limits are stated in 3.4, 5.4 and 6.4, and the exercises have answers. The `##` headings are unchanged; no `###` heading was renamed or renumbered, so no fragment changed (the only inbound fragment link, `#6-predicting-scaling` from the first entry, is intact).

Numbers spot-checked while reading (not a substitute for the technical stage): the collective table of 4.3 (rows p = 8), the 0.74 µs eager estimate of 4.4, the speedups and medians of 5.3, the relative difference 2.6e-13, the machine model of 6.1, the p = 4096 block rows of 6.2 and 6.3, and Exercises 1, 3 and 4. All agree except the item in D5.

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| D1 | Optional | `:16`, opening | structure | Second opening paragraph is a sentence-by-sentence table of contents ("It shows ... It measures ... It ends by ..."). Applied. |
| D2 | Should fix | `:615–617`, Section 8 closing | purpose | The closing restates every entry, overstates ("its last model draws on all of the earlier ones") and ends on a claim that Section 6.1 and 6.4 contradict ("predicts which design achieves that before a line of the program is tuned"). Applied. |
| D3 | Should fix | `:165`, Section 2.4 | evidence | "Both safe versions worked at every size tried, up to 8,000,000 bytes": the quoted run and `run.sh` show one size per safe version (506 doubles with `sendrecv`, 1,000,000 with `isend`). Deferred to the technical reviewer. |
| D4 | Should fix | `:36`, Section 1.3 | evidence | "a Version 5.0 followed in 2025" is an uncited factual claim, not in the reference list. Deferred to the fact-checker. |
| D5 | Should fix | `:549`, Section 6.3 | accuracy | The Gustafson check "0.0297 + 0.9703 × 4096 = 3974.4 ... against 3974.2 ... They differ only by f_s": the 0.2 difference shown comes from rounding f_s, not from f_s (0.03). Deferred to the technical reviewer. |
| D6 | Optional | `:429–458`, Section 5.3 | structure | "Checking against a serial run" also carries the speedups and the subnormal-number episode; the heading undersells the subsection. Not applied (heading kept to avoid changing a fragment; the content is in the right place). |

### D1. Opening reads as a list of contents
- **Where:** `:16`, opening paragraphs
- **Text:** "It shows blocking and nonblocking point-to-point messages ... It measures and models the cost of a message, derives the cost of collective operations, and distributes the grid ... It ends by predicting the scaling of that stencil on an assumed cluster."
- **Problem:** Standards 6.1 and the agent brief ask the introduction to set up what follows without a prose table of contents; each sentence names one section. It also carries a serial comma (C1).
- **Correction (applied):** the paragraph now states the line of argument (message-passing model, then a cost model built on it, then its use for collectives, the distributed stencil and scaling) and ties the end to the last series objective.

### D2. Closing restates and overclaims
- **Where:** `:615–617`, Section 8, the two paragraphs after the table
- **Text:** "This entry completes the series, and its last model draws on all of the earlier ones." ... "a simple, stated model of the cost of moving data predicts which design achieves that before a line of the program is tuned."
- **Problem:** Standards 6.2 item 6 asks the last entry to lead back to the series objectives; the paragraph listed the five objectives in paraphrase and then recapped each entry, without saying where this entry meets its own objective. The model of Section 6 does not draw on the fourth entry's GPU material. The final claim conflicts with `:499` ("Such a model gives the shape of a scaling curve, not a run time to a few percent") and `:560` ("its predictions checked against a few real runs").
- **Correction (applied):** the first paragraph now names where the fifth objective is met (Sections 3, 4 and 6) and links each earlier entry to what this entry actually uses from it (the speedup laws, $t_c$ and locality, the hybrid model of Section 1.4, the data-movement comparison of the offload model). The final sentence now reads "A simple, stated model of the cost of moving data shows which design can achieve that before the program is tuned, and measurements on the target machine then confirm it." No technical claim was added: every link back restates something the earlier entries or this entry's sections already establish.

### D3. "Every size tried" is not shown
- **Where:** `:165`, Section 2.4
- **Text:** "Both safe versions worked at every size tried, up to 8,000,000 bytes."
- **Problem:** The quoted output (`:154–159`) and the reproduction script run `sendrecv` only at 506 doubles and `isend` only at 1,000,000 doubles. A sweep of sizes is not in evidence.
- **Correction (for the technical reviewer):** either run both safe modes at several sizes (for example 505, 506, 10^4, 10^6) and keep the sentence, or narrow it to what is shown: "Both safe versions completed at the sizes shown, including 8,000,000 bytes for the nonblocking one." Text left unchanged.

### D4. MPI 5.0 date uncited
- **Where:** `:36`, Section 1.3
- **Text:** "the version cited here is Version 4.1 (Message Passing Interface Forum, 2023), and a Version 5.0 followed in 2025."
- **Problem:** A dated factual claim with no reference (standards 7.2). The reference list cites only Version 4.1.
- **Correction (for the fact-checker):** verify against the MPI Forum's published documents; if confirmed, add the Version 5.0 document to the references or attribute it; otherwise remove the clause. Text left unchanged.

### D5. Gustafson check: shown difference is a rounding artifact
- **Where:** `:549`, Section 6.3
- **Text:** "$f_s + (1 - f_s)\,p$ gives $0.0297 + 0.9703 \times 4096 = 3974.4$ for blocks at $p = 4096$, against 3974.2 from the model. They differ only by $f_s$"
- **Problem:** Recomputed in Python 3 from the article's own model (blocks, $p = 4096$, $t_c = 1.149$ ns, $\alpha = 2$ µs, $\beta = 0.1$ ns/byte): $T_p = 1.18421$ ms, $f_s = 0.029733$, model $S_s = 3974.215$, Gustafson $f_s + (1-f_s)p = 3974.245$. The true difference is $f_s \approx 0.03$, so both round to 3974.2. The 3974.4 in the text comes from using the rounded $f_s = 0.0297$ ($0.9703 \times 4096 = 3974.35$), which makes the displayed difference 0.2, about seven times $f_s$, so the numbers shown contradict the sentence that explains them.
- **Correction (for the technical reviewer):** use the unrounded value, for example "gives $0.02973 + 0.97027 \times 4096 \approx 3974.25$ ... against 3974.22 from the model. They differ by exactly $f_s$ ...". Text left unchanged.

### D6. Section 5.3 heading
- **Where:** `:429`, "5.3 Checking against a serial run"
- **Problem:** The subsection also reports speedups and the subnormal-number imbalance. Optional; a rename such as "Checking and timing against a serial run" would change the fragment. No inbound link targets it today (grep of `src/content/blog/*.mdx`), so the author may rename it if desired.

### Changes made (developmental)
- Rewrote the second opening paragraph (D1).
- Rewrote the two closing paragraphs of Section 8 (D2).

**Developmental verdict: pass.** Blocking 0, should fix 4 (D2 applied; D3, D4, D5 deferred to the technical and fact-check stages, which own those dimensions), optional 2 (D1 applied, D6 not applied). No should-fix finding within this stage's remit remains open.

## Copy edit

`npm run eos -- lint` before: 0 errors, 0 warnings, 16 suggestions. `npm run eos -- fix --rules spelling-variant,terminology`: 0 fixes applied. Manual checks: no em dashes, contractions, "we", "simply", "obviously", "clearly" or "of course"; headings are in sentence case; abbreviations (MPI, GCC, KVM, SPMD, RDMA, GB/s) expanded at first use; American spelling throughout. After: 0 errors, 0 warnings, 7 suggestions (listed under C6).

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| C1 | Should fix | `:16`; `:615` (old text) | language | Serial commas ("derives the cost of collective operations, and distributes"; "judging when an accelerator pays, and predicting"). Fixed. |
| C2 | Should fix | `:499` (81 words), `:615` (82 words, old text) | language | Two sentences far over the 45-word guideline, each joining three or more separate points. Fixed. |
| C3 | Optional | `:161`, `:253`, `:259`, `:376`, `:456`, `:475` | language | Sentences of 48–51 words flagged by `sentence-length`. Five split; `:259` kept (C6). |
| C4 | Optional | `:456`, `:458`, `:549` | language | Imprecise or throat-clearing wording: "The cause was arithmetic"; "The general lesson is that"; "Weak scaling is far kinder". Fixed. |
| C5 | Should fix | `:612`, Summary table | accuracy | "global sums to a small multiple of rounding error" understates the observed discrepancy. Deferred to the technical reviewer. |
| C6 | Optional | lint suggestions kept | language | Seven suggestions kept, with reasons below. |

### C1. Serial commas
- **Where:** `:16`, `:615`
- **Problem:** Standards 5.1: no serial comma.
- **Correction (applied):** both sentences were rewritten (with D1 and D2) without the serial comma.

### C2. Overlong sentences
- **Where:** `:499`, `:615`
- **Text:** "The four processes share one machine's memory system and are disturbed by its other tenants, the processes do not arrive at each exchange at the same moment, and $t_c$ is not one number: in a separately timed four-process run, ..."
- **Correction (applied):** split into "The four processes share one machine's memory system and are disturbed by its other tenants, and they do not arrive at each exchange at the same moment. Nor is $t_c$ one number. In a separately timed four-process run, ... against the predicted 0.575 s. The processes compete for the shared memory system and a smaller subdomain uses the caches differently (...)." The closing sentence at `:615` was replaced in D2.

### C3. Other long sentences
- **Correction (applied):** `:161` deadlock sentence split before the definition; `:253` split at the semicolon and the half-performance check turned into a full sentence ("The half-performance size can be checked against the large-message fit. A 25,620-byte message achieves ..."); `:376` amplification-factor parenthesis split into two sentences; `:456` "The cause lay in the arithmetic itself." as its own sentence; `:475` the two practical costs of blocks given as separate sentences.

### C4. Wording
- **Correction (applied):** "The cause was arithmetic:" → "The cause lay in the arithmetic itself."; "The general lesson is that every process waits ..." → "Every process waits ..."; "Weak scaling is far kinder." → "Weak scaling is far more favorable." LogP sentence: "..., which the affine model folds into $\alpha$." → "... The affine model folds both into $\alpha$." (the relative clause was ambiguous between the overhead and the gap).

### C5. Summary: "a small multiple of rounding error"
- **Where:** `:612`, Summary row "How is it checked?"
- **Text:** "The grid must match a serial run exactly; global sums to a small multiple of rounding error."
- **Problem:** Section 5.3 reports a relative difference of $2.6 \times 10^{-13}$ in the change norm, about 1,200 times the double-precision unit roundoff ($1.1 \times 10^{-16}$). That is well within the error bound of a reordered sum of $10^6$ terms, but "a small multiple" misdescribes it.
- **Correction (for the technical reviewer):** for example "global sums agree only to within the rounding error of a reordered sum ($2.6 \times 10^{-13}$ relative here)." Text left unchanged.

### C6. Lint suggestions kept
- `:18` `GNU` (acronym-expansion): the project's own name, whose expansion is recursive; "GNU Compiler Collection (GCC)" is already expanded.
- `:36` `MPICH` (acronym-expansion): product name, not an abbreviation the reader needs expanded.
- `:259` sentence of 48 words: a single list of the four LogP parameters; splitting it would separate the list from its introduction.
- `:621` `ACM`, `:622` `MIT`, `:623` `MPP`, `CS`: inside reference entries (venue, publisher and a cited title), which keep their original form.
- Program output keeps "Karp-Flatt" with a hyphen and "us" for microseconds: quoted output is not edited.

### Changes made (copy)
- Language: serial commas removed (2), long sentences split (7), four imprecise phrasings replaced, one ambiguous relative clause resolved.
- No technical claim, number, equation, code block, quoted output, unit, citation or link target changed. Two links in the closing now wrap "third entry" and "fourth entry" instead of "The third entry" (same targets).

**Copy-edit verdict: pass.** Blocking 0, should fix 3 (C1, C2 fixed; C5 deferred to the technical reviewer), optional 3 (C3, C4 applied; C6 kept with reasons). Final `npm run eos -- lint`: 0 errors, 0 warnings, 7 suggestions.
