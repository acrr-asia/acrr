# ACRR Editorial Standards Manual

Version 2.0, adopted 24 October 2026 (first edition 13 October 2026). Owner: the chief editor (Section 3). Changes follow Section 12.

This manual implements the governing editorial strategy, [`strategy.md`](strategy.md) (value before volume, the nine publication gates, the chief editor's live-site review, the editorial queue). Where the two differ, the strategy states the intent and this manual is corrected. The order in which the strategy is being put into effect, and what is not yet in effect, is in [`strategy-adoption-plan.md`](strategy-adoption-plan.md).

This manual is the editorial policy of ACRR (Advanced Computing & Robotics Research, https://acrr.asia). It defines what is worth publishing, who decides what, how a piece moves from idea to accepted live page, the house style, the rules for evidence and sources, the requirements for each kind of page, and the measurable conditions a piece must meet before it is published. It applies to every reader-facing word on the site: articles, series overviews, insights, Learning entries and the static pages.

The machine-readable half of this manual lives beside it: [`eos.config.json`](eos.config.json) (publication profile, thresholds, rule severities, required review stages, score minimums and the editorial queue settings), [`glossary.json`](glossary.json) (house terms and phrases to avoid) and the editorial queue in `queue/` (Section 4.3). The deterministic checks are run by `plugins/editorial-os/scripts/eos.mjs`; the judgment stages by the skills and agents of the `editorial-os` plugin. Where this manual and those files disagree, this manual states the intent and the files are corrected.

Contents

1. Purpose and principles
2. Identity, audience and voice
3. Editorial roles
4. The editorial workflow
5. Policy A: language and style
6. Policy B: structure, argument and visual communication
7. Policy C: research integrity and technical accuracy
8. Policy D: website-wide consistency and page requirements
9. Policy E: publication readiness (critical conditions, rubric, acceptance criteria)
10. Review records, revisions and corrections
11. Vietnamese translations
12. Governance of these standards

---

## 1. Purpose and principles

ACRR publishes long-form technical writing that readers use to learn a subject and to check their own work. A reader can only trust such writing if every page meets the same standard. The standard has five parts, and each is reviewed independently, because strength in one never compensates for failure in another:

1. **Correctness.** Statements, equations, numbers, code and diagrams are right, and the conditions under which they hold are stated.
2. **Integrity.** Nothing is invented. Facts, interpretations, recommendations and open questions are labeled as what they are. Sources exist and say what they are cited for.
3. **Clarity.** The argument is organized so that a reader in the stated audience can follow it, and the prose is precise, plain and idiomatic.
4. **Consistency.** Terms, notation, spelling, formatting and cross-references agree within a piece, across a series and across the site.
5. **Publishability.** The page builds, renders, links, indexes and reads correctly, on narrow and wide screens, in light and dark mode, with assistive technology.

Grammatically correct text that fails any of these is not ready to publish (Section 9).

Working rules for everyone who edits ACRR content, human or AI:

- Fix the cause, not the sentence. When prose is weak because the argument is weak, restructure the argument.
- Make the smallest defensible change when evidence is insufficient, and record the uncertainty instead of guessing.
- Preserve correct technical content and the author's intended meaning. A rewrite that reads better but says something different is a defect.
- Keep every change traceable: one purpose per commit, a review record per published item (Section 10).

## 2. Identity, audience and voice

### 2.1 Identity

ACRR is an independent technical publication on advanced computing, AI, robotics, control systems and scientific methods. It explains established methods carefully, states assumptions and limits, and keeps established results, interpretations and open questions apart. Its strategy (strategy 1) provides for four pillars: technical publishing, technology and science reporting, insights and analysis, and learning paths and reference resources. The reporting pillar has no published content yet, and no page may suggest that it has. ACRR is run as an independent publication: it does not claim a staffed laboratory, active funded projects, collaborators, citations or readership figures, and no page may imply them (Section 7.5).

The operating principle is reader value, technical credibility and lasting usefulness, not publication volume (Section 2.4).

The site publishes four kinds of content, each with a distinct job:

| Content | Job | Typical length |
|---|---|---|
| Series | A planned sequence that teaches a subject from stated prerequisites to stated objectives | 4-8 entries |
| Article (series entry or standalone) | One topic treated completely: concepts, derivation or mechanism, worked example, limits | 2,500-8,000 words for a series entry; standalone notes may be shorter |
| Insight | A short, explicitly structured piece of judgment: what is established, how ACRR reads it, what is open | 300-1,500 words |
| Learning entry | A pointer to a study resource, with what it covers and its status | One or two sentences |

### 2.2 Audience

The primary readers are engineers, researchers, graduate students and advanced technical learners: practising engineers moving into an adjacent field, researchers who want a careful reference, and students from the later years of a degree upwards. The default reader knows calculus and basic linear algebra and can read Python. Every series states its prerequisites beyond that, and every article states what it builds on. Writing for this reader means:

- define every term the reader cannot be expected to know, once, at first use;
- show the reasoning, not only the result; derive what can be derived in reasonable space and cite what cannot;
- never talk down: no "simply", "obviously" or "it is easy to see".

### 2.3 Voice

The voice is that of a careful senior engineer writing for a colleague: precise, calm, specific and economical. It explains rather than persuades. It prefers a concrete number, a named standard or a worked example to an adjective. It states limits as readily as capabilities. It is impersonal by default ("this entry derives", "the controller reads"); the first person singular is not used, and "we" is used only for a shared reasoning step in a derivation ("we substitute (3) into (5)"), never for an organization.

The voice avoids the habits that make text read as generic or machine-generated (the phrase list in `glossary.json` is enforced by the linter):

- empty openers and closers ("In today's rapidly evolving landscape", "In conclusion");
- claims of importance with no content ("plays a crucial role", "is a game-changer");
- throat-clearing ("It is important to note that");
- hype and marketing words ("cutting-edge", "seamless", "revolutionary", "unlock the power");
- formulaic triads and stacked adjectives where one precise word would do;
- restating the same point in the introduction, the body, a "key takeaways" list and the conclusion;
- false balance and hedging stacked on hedging ("may potentially possibly").

### 2.4 Value before volume

Every piece must pass two separate tests before it enters production, and again when it is audited (strategy 2):

- **Test A, worth the reader's time.** It delivers a specific intellectual or practical benefit that is not adequately available from existing ACRR pages or from a more authoritative source.
- **Test B, ACRR is the right publisher.** ACRR has a reason to publish this version: a better explanation, stronger evidence, a useful synthesis, original reporting, reproducibility, a Vietnam-specific perspective, or a connection between research and engineering practice.

An accurate piece can fail both. A topic label ("introduction to robotics") is not a value proposition.

**Reader-value contract.** Before drafting, the author states, and the managing editor approves: the *reader* (who specifically needs it), the *reader's problem* (question, decision, misconception or task), the *expected outcome*, the *distinctive contribution* beyond existing ACRR pages and readily available sources, the *evidence* that supports it, and the *limitations* (what it will not establish). The contract lives in the item's queue entry (`contract`), not in the content file. If it cannot be completed clearly, the idea does not enter production. For a piece published before this edition, a reviewer may write a *reconstructed* contract from the text; it is labeled as reconstructed and never presented as the author's original intent.

**Value category.** Every piece has one primary category (queue `valueCategory`):

| Category | Required reader benefit |
|---|---|
| Conceptual understanding | Explains a difficult concept or resolves a common misconception |
| Practical implementation | Enables the reader to implement, test or troubleshoot something |
| Technical decision | Helps compare alternatives using explicit criteria |
| Research synthesis | Organizes and critically evaluates evidence from multiple sources |
| Original reporting | Provides verified information, access, observations or perspectives unavailable from routine summaries |
| Reference value | Provides a reliable resource that readers can revisit |
| Critical analysis | Examines a claim, method, system or trend and reaches a reasoned conclusion |

**Format.** Every page also has a format that tells the reader what kind of page it is (queue `format`): tutorial, explainer, comparison, research review, reporting, analysis, reference or sponsored. The format is recorded in the queue now and shown on the site once the metadata migration of the adoption plan (Phase 6) is in place.

**Reject, merge, rewrite, reclassify, retire, keep.** The chief editor may reject a proposal or an article that is technically correct but lacks reader value, repeats existing content or imposes unnecessary reading effort, and may require a published item to be rewritten, merged, reclassified or retired. Retiring or merging a published page keeps its useful content (moved first), leaves a redirect where readers or external links may depend on the URL, and is never done only because traffic is low. Until San decides otherwise, every retirement and merge of a published page needs San's explicit confirmation.

## 3. Editorial roles

The strategy (strategy 3) defines five responsibilities. They may be combined in one person or one workflow, but the checks they stand for may not disappear:

| Strategy role | Responsible for | Carried out by (stages below) |
|---|---|---|
| Author | Central question, research, argument, references, technical work, visual assets, revisions | The writing pass (a person or an agent) |
| Technical reviewer | Correctness, assumptions, equations, code, reproducibility, source quality, limitations; discloses conflicts of interest | Subject-Matter Editor and Research and Fact-Checking Editor |
| Managing editor | Commissioning (Gate 1), structure, reader value, clarity, sourcing, classification, production status, coordination | Managing, Developmental, Copy and Series Editors; Technical Publishing Editor |
| Chief editor | The final editorial decision and the quality of the published website, judged on the live page (Gates 7-9) | Editorial Director role, QA Editor (pre-publication), live-review stage |
| Publisher | Commercial relationships, budgets, contracts, events, operations; never overrides an editorial decision | San |

**Who acts as chief editor (decided by San, 23 October 2026).** Claude performs the chief editor's live review of every page and may accept a *routine* page. A *high-risk* page is accepted only by San: reporting, claims about named people or organizations, safety-relevant guidance, and anything commercial (sponsored or partner content, product comparisons with a commercial relationship). The risk is recorded in the queue entry (`risk`); `eos queue validate` rejects a high-risk item accepted by anyone not listed in `queue.highRiskApprovers`. For a high-risk piece the technical review must also be independent of the author in the strong sense: a separate reviewer, not the author's own re-reading, and for reporting a human check of every quotation and attributed claim (strategy 13, AI-assisted production).

The nine stage roles below implement those responsibilities. They are responsibilities, not people. In ACRR's AI-assisted workflow each is a stage carried out by a skill or a dedicated agent of the `editorial-os` plugin (`plugins/editorial-os/agents/`), and a human may take any role. One rule is absolute: **the reviewer of a stage is never the author of the text under review in that pass.** An agent that wrote or revised a piece does not perform its fact-check, technical review, QA or live review.

| Role | Accountable for | Decides | Implemented by |
|---|---|---|---|
| Editorial Director (chief editor) | This manual, the publication's identity and audience, the acceptance thresholds, exceptions, live-site acceptance | Policy; exceptions; accept, revise, block or retire a live page | The site owner; `editorial` skill (policy mode); live review (Section 4.4) |
| Managing Editor | The plan: what is in scope, the order of work, stage assignments, readiness of each item, the audit trail | Scheduling; when an item moves to the next stage | `editorial` skill (orchestrator) and `eos status` |
| Developmental Editor | Purpose, audience fit, argument, structure, depth, completeness of each piece | Structural changes: reorganize, cut, expand | `developmental-editor` agent |
| Subject-Matter Editor | Technical, scientific and mathematical accuracy: definitions, derivations, equations, code, diagrams, numerical examples | Whether a technical statement is correct and adequately qualified | `technical-reviewer` agent |
| Copy Editor | Grammar, syntax, usage, terminology, house style, concision, consistency within the piece | Wording, within the meaning approved by the other roles | `copy-editor` agent + `eos lint`/`eos fix` |
| Research and Fact-Checking Editor | Factual claims, dates, names, numbers, standards, and every reference: existence, bibliographic details, and that the source supports the claim | Whether a claim may stand, must be qualified, or must go | `fact-checker` agent + `eos refs`, `eos check-external` |
| Series Editor | The series as one publication: scope, sequence, prerequisites, notation, cross-references, promises, overview page | Order of entries, series-level additions and cuts | `series-review` skill (repository) |
| Technical Publishing Editor | MDX/Markdown validity, front matter, metadata, links, math and diagram rendering, accessibility, build | Whether the page is technically publishable | `eos lint`, `eos validate-site`, the build and link checks |
| Quality Assurance Editor | An independent final check of all of the above against Section 9 | The publish/revise decision recorded in the review record | `qa-editor` agent + `eos record`, `eos gate` |

Escalation: any role that finds a problem it cannot resolve with confidence (a disputed technical point, a claim that cannot be verified, a change of scope) records it as an open finding. Open blocking findings stop publication (Section 9.1). A decision that changes the publication's scope or identity goes to the Editorial Director.

## 4. The editorial workflow

### 4.1 The nine gates

The workflow is a sequence of approval gates, not a calendar (strategy 4). Work advances when a gate's acceptance criterion is met. A successful build, deployment or automated check is never editorial approval: technical quality assurance and editorial acceptance are separate controls.

| Gate | What must be true to pass | Evidence left behind | Queue status after it |
|---|---|---|---|
| 1. Idea approval | The managing editor can say in one or two sentences why the piece is worth the intended reader's time (Section 2.4); it does not duplicate an existing page | Proposal (`plugins/editorial-os/templates/idea-proposal.md`), approved contract in the queue entry | `approved-for-research` (or `rejected`) |
| 2. Research readiness | The central argument is supportable from sources actually read, run or derived | Research log (`templates/research-log.md`) | `drafting` |
| 3. Draft completion | A qualified reader can follow the central argument: question, answer, reasoning, evidence, assumptions, alternatives, limitations, references and proposed visuals are present | The draft; `eos lint` has no errors | `technical-review` |
| 4. Technical review | No unresolved critical technical error; limitations that affect the conclusion are stated | `technical-reviewer` and `fact-checker` findings | `editorial-review` |
| 5. Editorial review | The piece delivers a clear, defensible benefit without unnecessary effort; content that is correct but adds nothing is identified and cut; the visual questions (Section 6.8) are answered | `developmental-editor` and `copy-editor` findings; for a series, `reviews/<id>.md` | `revision-required` until resolved, then `ready-to-publish` |
| 6. Pre-publication checks | Title, description, type, dates, references, links, rights to third-party assets, disclosures, accessibility, notation, limitations and uncertainty are correct | `validate-site`, build, link check, `series-pipeline gate`, `qa-editor` record, `eos gate` | `ready-to-publish` |
| 7. Publication and live inspection | The public page meets ACRR's editorial and presentation standards, not only its build requirements | Deployment and `verify-live`; live-review report (Section 4.4) | `published-awaiting-live-review` |
| 8. Feedback and revision | Every live finding is resolved and re-checked on the updated public page, or the page is rejected, retired or accepted with documented non-critical limitations | Findings in the report and the queue; re-review section G | `revision-required-after-publication` until closed |
| 9. Final acceptance and maintenance | The chief editor (Section 3) accepts the live page; the review history is kept; the page is reassessed when its standards, software versions, evidence or assumptions change | Queue `reviews.chiefEditor`, history | `accepted`, later `maintenance` |

Exceptional states: `blocked` (cannot advance; the history says why and what would unblock it), `rejected`, `merged` (with `mergedInto`) and `retired` (with `redirect`).

### 4.2 Operational steps

Inside Gates 3 to 7 every new or revised item passes through the steps below. They are implemented by the `editorial` orchestrator skill and documented operationally in `plugins/editorial-os/docs/workflow.md`; this section states what each step must achieve.

| # | Step | Gate | Role | Output | Check |
|---|---|---|---|---|---|
| 1 | Discover and inventory | — | Managing Editor | `eos inventory` / `eos status` / `eos queue` rows for the items in scope | — |
| 2 | Classify | 1 | Managing Editor | Content type, format, value category, risk, required stages | Queue entry valid |
| 3 | Plan the review | 1-2 | Managing Editor | Which stages and tools apply; what is unavailable and the fallback | — |
| 4 | Check sources and dependencies | 2 | Fact-Checker, Series Editor | Reference list verified or flagged; prerequisites and dependent articles identified | — |
| 5 | Draft or revise | 3 | Author | The text | `eos lint` has no errors |
| 6 | Review | 4-5 | Developmental, Copy, Fact-Checker, Subject-Matter | Findings with severity, location, evidence and a proposed correction | — |
| 7 | Resolve | 5 | Author | Every blocking and should-fix finding applied or answered with a reason | No open blocking findings |
| 8 | Series review | 5 | Series Editor | `reviews/<series>.md`, resolved and stamped | `series-pipeline gate` |
| 9 | Validate | 6 | Technical Publishing Editor | Build, link check, `eos validate-site` | All pass |
| 10 | Final gate | 6 | QA Editor | Review record with scores and decision | `eos gate` |
| 11 | Publish | 7 | Managing Editor | Merge to `master`; deploy; `verify-live` | Deploy workflow gates |
| 12 | Live review | 7-9 | Chief editor | Live-review report; queue status and findings | Section 4.4 |

A step may be repeated; none may be skipped. Steps 9-11 are enforced by CI (`.github/workflows/publication-gate.yml` on every pull request and `deploy.yml` before publication), so a failed mandatory check blocks publication automatically.

### 4.3 The editorial queue

Every item has a queue entry, `editorial/queue/<type>/<slug>.json` (schema `plugins/editorial-os/schema/queue-entry.schema.json`), separate from the content file and from its review record. It holds the item's public URL and source, format, value category, risk, reader-value contract, workflow status (Section 4.1), the status of the technical, editorial and chief-editor reviews, the open live findings, author, reviewers, disclosures and the history of status changes. Because it is not part of the content hash, editing it never makes a review stale.

- `eos queue init` adds an entry for every item that has none; `eos queue set <id> <status>` changes a status and appends to the history; `eos queue` summarizes; `eos queue validate` checks the rules.
- A proposal is a queue entry with no content file yet.
- The rules: an accepted item has a chief-editor acceptance with a reviewer and a live-review report; a high-risk item is accepted only by a person in `queue.highRiskApprovers`; no item is accepted with an open critical or major finding; a merged item names what absorbed it and a retired item its redirect; an item started or first published on or after `queue.contractRequiredFrom` (24 October 2026) has an approved reader-value contract.
- `eos gate` runs these rules according to `queue.enforce`. At adoption the value is `warn` (reported, not blocking), so that series work already in progress is not stopped; it becomes `error` once the open series branches have queue entries.

The 120 items published before this edition were entered with status `published-awaiting-live-review`, contract `missing`: none has yet had a chief editor's review of its live page.

### 4.4 The chief editor's live-site review

After publication the chief editor inspects the actual public URL, not the source (strategy 4, Gate 7; strategy 5). The inspection covers, on a wide and a 360-pixel screen and in light and dark mode: the title and opening screen; the main answer and argument; the structure and flow of sections; equations, code, tables, diagrams, images and captions; references and internal links; related content and navigation; missing content, rendering defects and visual inconsistencies; and whether the page still satisfies its reader-value contract.

The result is a report, `editorial/live-reviews/<type>/<slug>.md`, in the form of `plugins/editorial-os/templates/live-review-report.md` (A. decision; B. reader-value assessment; C. substantive findings; D. visual and structural findings; E. technical and source findings; F. required changes, mandatory and optional; G. re-review). Every finding states its location, the problem, why it matters, the required action, its priority (critical, major or minor) and an acceptance condition that can be checked on the live page; "improve clarity" is not a finding. The findings are copied into the queue entry. The author revises and republishes; the chief editor closes a finding only after seeing its acceptance condition met on the updated public page.

The live review is performed by a reviewer who did not write or revise the page in that pass. Who may accept a page is set in Section 3.

Captures of the live site are taken by the `Live review captures` workflow (`.github/workflows/live-review.yml`, `scripts/live-capture.mjs`) after every deployment, for the pages that changed, and on demand; it publishes screen-sized screenshots and rendering facts to the `live-captures` branch. A local build is not the live page. The procedure is the `live-review` skill of the editorial-os plugin; decisions and findings are recorded with `eos queue review` and `eos queue finding`.

### 4.5 Monitoring, corrections and maintenance

Readers must have a way to report an error; the channel is chosen by San and shown on the About page once chosen. A material correction is made promptly, reviewed like any other change, recorded in the item's review record and queue history, and, where a reader may have relied on the earlier statement, noted in the article (Section 10). An accepted item moves to `maintenance` when a standard, software version, piece of evidence or assumption it depends on changes, and is reassessed.

## 5. Policy A: language and style

### 5.1 Variety of English

- **American English spelling** (Merriam-Webster as the reference dictionary): behavior, color, center, analyze, organize, modeling, labeled, defense, analog, meter. Rationale: it is the convention of IEEE and ACM publications, which dominate the fields ACRR covers, and it was already the majority form in the archive. Enforced by the `spelling-variant` rule; `eos fix` applies it in prose only.
- Proper names, titles of cited works and quotations keep their original spelling (the linter exempts reference lists; quotations must be checked by hand).
- **No serial comma** ("sensors, actuators and controllers"), except where omitting it creates ambiguity ("the libraries, NumPy, and SciPy" vs a list of three). This is the existing house practice and is retained deliberately; it is not machine-enforced.
- **No contractions** in article and insight prose (`contractions` rule). Contractions inside quoted dialogue or code comments are allowed.

### 5.2 Sentences and paragraphs

- One idea per sentence; one topic per paragraph. A sentence over about 45 words and a paragraph over about 170 words are flagged for a second look, not banned.
- Prefer the active voice when the actor matters ("the controller samples the error"); the passive is right when the actor is unknown or irrelevant ("the samples are stored in a ring buffer").
- Put the main clause first and the qualification after it, unless the qualification changes the meaning.
- Use the present tense for what is generally true and for what the text does; the past tense for history and for what a cited author did.
- Cut words that carry no meaning: intensifiers ("very", "extremely", "really"), filler ("in order to" → "to", "due to the fact that" → "because", "utilize" → "use"), and redundant pairs ("each and every").
- Never write "simply", "obviously", "clearly" or "of course" about a technical step.

### 5.3 Terminology

- Use one term for one concept, everywhere. The house forms are in `glossary.json`; add a term there the first time two forms of it are found.
- Define a technical term at its first use in each article, in bold: "the **scan cycle**, the fixed loop in which ...". In a series, a later entry may refer back instead ("the scan cycle (second entry, Section 2)").
- Expand every abbreviation at its first use in each article: "programmable logic controller (PLC)". Very common abbreviations listed under `acronyms.known` in `eos.config.json` (HTTP, CPU, DC, ...) need no expansion.
- Hyphenate compound modifiers before a noun (real-time system, closed-loop response, state-space model, floating-point arithmetic) and leave them open as nouns (in real time, the state space).
- Name versions: "OAuth 2.0", "Python 3", "IEC 61131-3:2013", "TLS 1.3".

### 5.4 Capitalization and headings

- **Titles** of articles, series and insights use headline style (Chicago): capitalize major words. "Stability and Eigenvalues", "When Is a Kalman Filter Enough?"
- **Section headings** use sentence case: capitalize only the first word and proper nouns. "The scan cycle and its response time", not "The Scan Cycle and Its Response Time". Enforced by `heading-case`.
- Headings are short labels (at most about 12 words), have no final punctuation except a question mark, and are unique within a page.
- Series entries number their sections ("## 3. The scan cycle", "### 3.1 Input image") so that cross-references can cite them; all numbered or none within one article, and sequential (`heading-numbering`). The Summary, Exercises and References may be numbered or not, consistently within a series.
- The body never contains a level-1 heading; the page title is the only `<h1>`. Levels never skip (`heading-levels`).

### 5.5 Numbers, units and symbols

- SI units with a space between number and unit (10 kHz, 4–20 mA, 3.3 V); no space before % (2%). Write "percent" only without a numeral.
- Numerals for all measurements and for numbers 10 and above; words for zero to nine in running text when not a measurement.
- An en dash for ranges (4–20 mA, pages 14–21); a minus sign (−) or LaTeX for negative values in prose.
- Mathematical symbols are set in KaTeX (`$...$`), never as plain letters or Unicode approximations in prose. Every symbol is defined at first use, with its unit.
- State conventions that a result depends on: units (degrees or radians), sign and coordinate conventions, indexing from 0 or 1, row or column vectors, quaternion component order.

### 5.6 Punctuation and typography

- Em dashes are not used in prose; use a comma, colon, parentheses or a new sentence. (The house style is restrained; the archive uses almost none.)
- Quotation marks: double quotes; commas and periods inside closing quotes in prose (American style), but outside when quoting code or exact strings ("the header `Authorization`").
- Code identifiers, file names, commands, HTTP fields and literal values go in `code`. Emphasis uses *italics*; **bold** is reserved for a defined term at its point of definition and for the label of a list item.
- Lists: introduce every list with a complete sentence; keep items grammatically parallel; end items with punctuation only if they are full sentences or a single sentence runs through the list.

### 5.7 Fact, interpretation and recommendation

The text must let the reader tell apart:

- **established facts** (stated plainly, with a source or derivation where not common knowledge);
- **interpretations** ("one reading is ...", "this suggests ...");
- **assumptions** (what is taken as given but not established, stated where it is used);
- **hypotheses** ("if ..., we would expect ...");
- **recommendations** ("prefer ... when ...", with the condition);
- **open questions** (stated as questions, with what would settle them).

Insights carry this separation in their structure (`## Established`, `## Interpretation`, `## Open questions`). Articles carry it in the wording. Confident wording never turns an interpretation into an established result. Evidence is proportional to the claim: the stronger or more consequential the claim, the stronger the source (primary papers, standards, original data, reproducible code), and a quantitative claim states its measurement, comparison basis and conditions. A citation is not proof by itself; the text must represent what the source actually supports.

## 6. Policy B: structure, argument and visual communication

### 6.1 Every piece

- **A stated purpose and reader.** The opening paragraph says what the piece covers, what it builds on and, where relevant, what it assumes. Front matter `description` says the same in one sentence of 70-165 characters.
- **Concepts before mechanics.** A concept is introduced (what it is, what problem it solves, its scope) before its details. A section never opens with fields, equations or code for something it has not yet said what it is.
- **A logical progression**: context, concept, mechanism or derivation, worked example, limits and failure modes, summary.
- **Evidence for every non-trivial claim**: a derivation, a calculation the reader can repeat, a measurement, or a citation.
- **Earned elements.** A diagram, table, example or exercise stays only if it shows something the prose cannot show as well. Every figure has a caption that says what to look at.
- **No redundancy.** The same explanation does not appear twice in a piece; across a series, a later entry refers back instead of repeating.
- **A real ending.** The final section summarizes what was established and, in a series, leads to the next entry. No "In conclusion".
- **Answer first, where the reader has a decision or a question.** A comparison, analysis or decision-oriented piece states the question, the answer, why it matters and the conditions under which the answer holds near the beginning. Tutorials whose order of discovery is the point, and narrative reporting, are exceptions.
- **Every major section supports the central question.** A section that does not is removed, moved or justified. The supporting reasons are grouped (the Pyramid Principle as a writing technique); MECE is a diagnostic for categories, not a template to force on every subject.
- **Explicit comparisons.** When methods, tools or systems are compared, the decision criteria (accuracy, latency, compute and memory, cost, robustness, reproducibility, maintainability, security, deployment constraints, fit to the task) are stated before any conclusion, a table is used when several dimensions matter, and a multi-dimensional trade-off is not collapsed into an unsupported ranking.
- **Specific limitations.** Every substantial analysis names its actual limits (assumptions, data quality, external validity, computational cost, hardware, software versions, benchmark bias, incomplete evidence). "Further research is needed" is not a limitation.
- **Actionable where the subject permits.** A practical guide leaves the reader with a tested procedure, a decision framework, a worked example, a reproducible implementation or a checklist. A conceptual piece does not invent an implementation to look practical.
- **Depth, not volume.** Length is justified by the subject. Paragraphs that repeat a conclusion, restate a figure without interpreting it, or give background unrelated to the central question are cut.

### 6.2 Series entry (article with `series`)

In this order:

1. Opening paragraphs (no heading): what this entry builds on (linked), what it covers, and the versions, conventions and tools its examples assume.
2. Numbered sections, each opening with the concept it treats.
3. Worked examples whose numbers have been recomputed; code that has been run, with real output.
4. Limits, assumptions and failure modes, as a section or within the relevant sections.
5. Exercises with answers, where the topic is computational (optional otherwise).
6. **Summary**: a short table or paragraph of the main results, and a closing paragraph that leads to the next entry (or, for the last entry, back to the series objectives).
7. **References**: the sources the entry relies on (Section 7.3).

### 6.3 Standalone article

As a series entry, without the series links. A short research note may omit exercises and the summary table, but not the opening statement of purpose, the limits, or references for any claim that is not derived in the text.

### 6.4 Insight

Front matter `kind` names the genre (Comparison, Concept explanation, Research question, Methodological note, Engineering observation, Emerging idea, Policy analysis). The body has one framing paragraph (what question the insight addresses and why it matters to the reader) followed by exactly three sections in this order: `## Established`, `## Interpretation`, `## Open questions`. "Established" contains only claims that are established and verifiable; "Interpretation" is explicitly ACRR's reading; "Open questions" are genuine questions with what would answer them. An insight links to the articles that treat its subject in depth.

### 6.5 Series overview page

The series file (`src/content/series/<id>.md`) is the series' front door. It states:

- what the series covers and why in that order (the sequence rationale);
- the intended reader and the prerequisites;
- what each entry contributes (the page lists entries automatically; the body says how they connect);
- the conventions shared by all entries (notation, units, language versions), when they matter;
- `objectives`: 3-6 checkable learning outcomes, each beginning with a verb a reader could be assessed on (explain, derive, compute, design, evaluate).

The overview must not promise anything the entries do not deliver.

### 6.6 Learning entry

Title, one-sentence description of what the resource covers and for whom, topic, type, and status. An entry without a real, checked URL is shown as "Coming soon" with no link. Never invent a URL.

### 6.7 Templates by format

The templates standardize quality without forcing every piece into one shape (strategy 8). A series entry follows Section 6.2 and, within it, the template of its format.

| Format | Order of the piece |
|---|---|
| A. Technical explainer (tutorial, explainer) | The question; short answer; prerequisites; conceptual model (a diagram where it helps); technical explanation; worked example; practical application; limitations and failure modes; summary; references and further study |
| B. Comparison or decision analysis | The decision; use case and constraints; evaluation criteria; evidence and method of comparison; comparison table or chart; trade-offs and failure modes; recommendation conditional on the use case; remaining uncertainty; sources and reproducibility information |
| C. Research review | Research question and scope; why it matters; how sources were selected; concepts and terms; findings by theme, method or evidence; agreements, disagreements and methodological limits; evidence gaps; implications; references. Never called a systematic review unless its method justifies the name |
| D. Technology and science reporting | The development, claim or issue; why it matters to the reader; what is known and how it is established; people, institutions and primary sources; independent context or corroboration; competing perspectives or right of reply where warranted; reported facts kept apart from the reporter's interpretation; implications and open questions; sources, disclosures and method. Quotations are never invented or altered in meaning. Always high risk (Section 3) |
| E. Insight or short analysis | Section 6.4: a framing paragraph with the main observation, then Established (the evidence), Interpretation (why it matters; alternative explanations and limits) and Open questions (the implication or what is unresolved). Not a rewritten news item or a set of unsupported opinions |

### 6.8 Visual communication

Text is not the default for every kind of information (strategy 7). During drafting and editorial review the author and editor ask, for every substantial piece: would a diagram reduce the effort of understanding the main concept; would a table make a comparison easier to inspect; would a chart reveal a pattern prose hides; would an annotated example expose an assumption; would a worked calculation make the reasoning verifiable; would an interactive demonstration genuinely help, or is a static figure enough. The decision on each substantial opportunity is recorded in the review (developmental stage). Without the visual, the text must still be clear.

| Information | Preferred representation |
|---|---|
| Sequence of operations, system behavior | Flowchart or sequence diagram (Mermaid) |
| Components and relationships | Block or architecture diagram |
| Change over time; control-system response | Line chart or response plot with labeled variables, units and conditions |
| Comparison across categories or approaches | Bar chart, comparison table or decision matrix |
| Distribution; relationship of two measured variables | Histogram or box plot; scatter plot |
| Multi-step algorithm | Pseudocode, numbered procedure or flow diagram |
| Derivation | Equations with intermediate steps and annotations |
| Taxonomy | Hierarchical diagram or structured table |
| Key findings of a long piece | Summary table or findings list |

- **Chart integrity.** Title, axis labels, units, legend where needed, data provenance and method notes. No misleading scales, omitted comparison conditions or unsupported extrapolation. No chart when the data are unavailable or not comparable. ACRR plots are generated from the article's own formulas or from data the article states.
- **Diagram integrity.** A diagram shows a real relationship, process, structure or distinction, with the article's own terms. Conceptual illustrations are distinguished from measured results, and simplified models are labeled as simplified when it matters.
- **Captions** say what the reader should notice and, where relevant, what the figure does not establish; a caption does not repeat the title.
- **On the rendered site.** Figures, tables, equations and code must be readable on a 360-pixel screen and in dark mode; a correct figure in the source that is clipped or unreadable on the public page is a live-review finding.

## 7. Policy C: research integrity and technical accuracy

### 7.1 Source hierarchy

Prefer, in this order:

1. The primary source: the standard (IEC, ISO, IEEE, IETF RFC, W3C, NIST), the original paper, official specification or documentation.
2. Authoritative secondary sources: established textbooks and monographs from recognized publishers; survey articles in peer-reviewed venues.
3. Reputable technical documentation from vendors, clearly identified as vendor-specific.

Not acceptable as the sole support for a claim: blogs, forums, wikis, AI-generated text, marketing material, or a source that cannot be identified precisely.

### 7.2 Verification

- Every factual claim that is not common knowledge for the audience, and every number, date, name, version and standard number, is checked against a source of the kind above during the fact-check stage.
- Every reference is checked for existence and for its bibliographic details (authors, title, venue, volume, issue, pages, edition, publisher, year), and for the relationship between the source and the claim it supports.
- Worked examples are recomputed; code is run with the stated language version and its output compared with the text; equations are checked by derivation, dimensional analysis or a special case; diagrams generated from formulas are regenerated from the article's own formulas.
- What cannot be verified in the time and tools available is recorded as "not verified" in the review record, and the text is qualified ("according to ...", "reported as ...") or the claim is removed. An unverifiable claim is never left stated as fact.

### 7.3 Citation format

References use a simplified IEEE style, listed in alphabetical order of first author under a `### References` heading at the end of the Summary (or `## References` where the article has no Summary section):

- Journal article: `A. B. Author and C. Author, "Title in sentence or original case," *Journal Name*, vol. 9, no. 2, pp. 267–293, 1956.`
- Conference paper: `A. Author et al., "Title," in *Proceedings Name*, pp. 1–10, 2019.`
- Book: `A. Author, *Title of Book*, 3rd ed., Publisher, 2015.`
- Standard: `IEC 61131-3:2013, *Programmable controllers – Part 3: Programming languages*, International Electrotechnical Commission, 2013.`
- RFC: `M. Jones, J. Bradley and N. Sakimura, *The JSON Web Token (JWT)*, RFC 7519, IETF, 2015.`
- Specification or manual: `Organization, *Title*, version or revision, year.`

Every entry has authors or an organization, a title, and a year. Volume, issue and pages are given when they exist. URLs are added only after they have been fetched and found to contain the cited work; DOIs are preferred to URLs. Titles keep the spelling of the original.

### 7.4 Preserving meaning when rewriting

An editor who changes a technical sentence confirms that the new sentence is still true under the same conditions as the old one. If a correction is needed, it is made only when the error can be established with confidence (by derivation, recomputation or a primary source) and the evidence is recorded in the review finding.

### 7.5 Never fabricate

Never invent references, quotations, experiments, data, measurements, results, benchmarks, statistics, credentials, biographies, affiliations, collaborators, readership or citation figures, contact details, project counts, URLs or technical capabilities. Missing information stays missing; a placeholder that a reader can see ("Coming soon", "Planned") is labeled as such. Sample or demonstration content carries `example: true` and an Example label everywhere it appears. These rules restate and extend the content-integrity rules in `CLAUDE.md`, which remain in force.

## 8. Policy D: website-wide consistency and page requirements

### 8.1 Site-wide conventions

- **Titles**: headline style; specific (name the method or question, not "An Introduction to Everything"); at most 70 characters.
- **Descriptions** (front matter `description`, used as meta description, card summary and RSS summary): one complete sentence of 70-165 characters that says what the reader will learn; no "This article ..."; no list of every section.
- **Series vocabulary**: a series has *entries*; "the third entry", "the next entry"; link the first mention of another entry. Cross-references cite numbered sections ("Section 4.2 of the first entry").
- **Calls to action** use the existing interface labels ("Read article →", "View series", "Read insight") and are not rewritten per page.
- **Navigation labels**: Home, Blog, Series, Learning, Insights, About.
- **Dates**: `publishedAt` is the first publication date; `updatedAt` is set when the meaning, structure or technical content of a published item changes (not for typo fixes), and the change is summarized in its review record.

### 8.2 Page requirements by section

| Page | Purpose | Must | Must not |
|---|---|---|---|
| Home (`/`) | Tell a first-time visitor what ACRR is, what it covers and where to start | State the identity in one sentence; show the latest articles and the series with their real counts; describe the current state truthfully (what exists now, what is intended) | Overstate size, activity or achievements; describe published work as planned or planned work as published |
| About (`/about`) | Mission, scope, principles, editorial standards and direction | Link the editorial principles to this manual's commitments in reader language; say how corrections are handled | Contain biography, credentials or contact details that have not been supplied |
| Blog (`/blog`) | Chronological archive | Cards with date, category, title, description, "Read article →" | Duplicate descriptions |
| Series (`/series`, `/series/<id>`) | The series catalogue and each series' front door | Overview per Section 6.5; ordered entries with descriptions | Promise topics the entries do not cover |
| Learning (`/learning`) | Index of study resources | Status per entry; real links only; notices conditional on the data | Invented URLs; authoring instructions in visitor-facing copy |
| Insights (`/insights`, `/insights/<id>`) | Short structured judgments | The three-part structure; links to in-depth articles | Present interpretations as facts |
| Tags, categories | Navigation | Generated from content | Hand-written copy that drifts from the content |
| 404 | Recover a lost reader | Links to the main sections in the page's language | — |

### 8.3 Coherence checks across the site

The Content Auditor checks, site-wide: duplicated explanations that should be a cross-reference; conflicting explanations of the same concept; inconsistent terminology or notation; broken internal links and fragments; orphaned pages (published but not linked from any listing or series); series entries whose cross-references or promises are not fulfilled; and static pages whose description of the site has fallen behind the content.

## 9. Policy E: publication readiness

This policy decides whether an item may be published (Gate 6). It does not decide whether the published page is accepted: that is the chief editor's live review (Section 4.4 and Section 9.5).

### 9.1 Critical conditions (pass/fail)

An item fails, whatever its scores, if any of these holds:

| # | Critical condition | Detected by |
|---|---|---|
| C1 | A factual, mathematical, code or technical error that is known and not corrected | Subject-Matter Editor, Fact-Checker |
| C2 | Fabricated or unverifiable content stated as fact (Section 7.5) | Fact-Checker |
| C3 | A reference that does not exist or does not support the claim it is cited for | Fact-Checker |
| C4 | Sample content without its Example label, or planned content presented as published | QA Editor, build |
| C5 | Build, MDX, KaTeX or Mermaid failure; broken internal link or fragment | Build, `check:links`, `eos validate-site` |
| C6 | A false cross-reference (wrong entry, wrong section, unfulfilled promise) | `eos lint` (`series-crossref`, `section-reference`), Series Editor |
| C7 | Missing required front matter or required sections | `eos lint` |
| C8 | An unresolved blocking finding from any review stage | Review record |
| C9 | For a series entry: the series has no current, resolved series review | `series-pipeline gate` |

### 9.2 Scoring rubric

The QA Editor scores seven dimensions from 0 to 4 after all other stages are complete. The same rubric applies to every content type, read against that type's requirements in Section 6.

| Score | Meaning |
|---|---|
| 4 | Exemplary: nothing a careful expert editor would change |
| 3 | Publishable: minor optional improvements only |
| 2 | Needs revision: should-fix problems that a reader would notice |
| 1 | Seriously deficient: problems that mislead or block understanding |
| 0 | Absent or unusable |

| Dimension | 4 | 3 | 2 or below |
|---|---|---|---|
| **Purpose and audience** (`purpose`) | Purpose, reader and prerequisites explicit; every section serves them | Clear purpose; minor drift | Unclear who it is for or what it delivers |
| **Structure and argument** (`structure`) | Concepts before mechanics; each step follows; complete; ending that resolves | Sound with a weak transition or one section out of place | Fragmented, repetitive, or missing a step the argument needs |
| **Technical accuracy** (`accuracy`) | Every statement, equation, number and code sample verified; limits stated | Correct; a qualification could be sharper | Any unqualified error or misleading simplification |
| **Evidence and sourcing** (`evidence`) | Non-trivial claims derived or cited to primary/authoritative sources; references complete and consistent | Adequate; minor bibliographic gaps | Unsupported claims or weak sources |
| **Language and style** (`language`) | Precise, idiomatic, concise; house style throughout | Clear; a few awkward or wordy sentences | Awkward, generic, padded or ambiguous prose |
| **Consistency** (`consistency`) | Terms, notation and cross-references agree within the piece, the series and the site | Minor inconsistency | Conflicting terms, notation or explanations |
| **Publishing quality** (`publishing`) | Metadata, headings, links, math, diagrams, accessibility all correct; no lint warnings left without reason | Minor warnings with reasons | Rendering, metadata or accessibility defects |

### 9.3 Thresholds

| Type | Minimum total (of 28) | Minimum per dimension | Required stages |
|---|---|---|---|
| Article (including series entries) | 24 | 3 | developmental, copy, factCheck, technical, publishing, qa |
| Insight | 22 | 3 | developmental, copy, factCheck, technical, publishing, qa |
| Series overview | 22 | 3 | developmental, copy, series, publishing, qa |

The values are configured in `eos.config.json` (`review`) and enforced by `eos record` and `eos gate`. A stage may be recorded as `n/a` only with a note saying why (for example, a series overview has no code to run).

### 9.4 Acceptance checklists

**Article (series entry or standalone)**

- [ ] Opening states purpose, what it builds on, and assumed versions/conventions.
- [ ] Every concept introduced before its details; every term defined and abbreviation expanded at first use.
- [ ] Derivations checked; numbers recomputed; code run with real output; diagrams match formulas.
- [ ] Limits and assumptions stated.
- [ ] No unsupported claim; references complete in house format; sources support their claims.
- [ ] Section numbering and cross-references correct; promises to later entries fulfilled.
- [ ] Summary and References present (series entries); the closing paragraph leads to the next entry.
- [ ] Title ≤ 70 characters; description 70-165 characters, one sentence.
- [ ] `eos lint`: no errors; warnings resolved or justified in the record.
- [ ] Build, link check and `eos validate-site` clean for the page.
- [ ] For an item started or first published from 24 October 2026: an approved reader-value contract, a value category, a format and a risk level in its queue entry.
- [ ] The visual questions (Section 6.8) answered and the decisions recorded.
- [ ] Disclosures present where there is a sponsorship, partnership or conflict of interest; rights confirmed for third-party figures, code and data.

**Insight**: framing paragraph; the three sections in order; Established contains only verifiable claims, each sourced or common knowledge; Interpretation labeled as such; open questions are questions; links to the in-depth articles; metadata as above.

**Series overview**: sequence rationale; audience and prerequisites; shared conventions; 3-6 checkable objectives, each covered by an entry; description within limits; no promises the entries do not keep; series review current and stamped.

**Static page**: true to the current state of the site (counts and statuses computed from content, not written by hand); no fabricated personal or organizational details; no authoring instructions in visitor copy; both languages say the same thing.

### 9.5 Live-site acceptance

A published page is accepted (Gate 9) when its live-review report (Section 4.4) records the decision "accept" or "accept with minor follow-up", no critical or major finding is open, the page still delivers its reader-value contract, and the acceptance is by a permitted reviewer (Section 3: San for high-risk pages). Minor findings may stay open as documented follow-ups. Acceptance is recorded in the queue entry (`reviews.chiefEditor`, status `accepted`).

## 10. Review records, revisions and corrections

- Each published item has a review record, `editorial/records/<type>/<slug>.json`, written by `eos record` at the QA stage. It holds the content hash of the reviewed file, the stage outcomes, the scores, the finding counts, anything not verified, the reviewer roles, the commit, and the history of earlier records. `eos gate` fails if the file has changed since its record (the review is stale), if the record does not pass, or if the file has lint errors.
- Series additionally carry `reviews/<id>.md` with a content-hash stamp (`scripts/series-pipeline.mjs`), checked by the series gate.
- Each item has a queue entry (Section 4.3) with its workflow status, contract, live findings and the history of status changes. Live-review reports live in `editorial/live-reviews/<type>/<slug>.md`.
- Audit reports live in `editorial/audit/`. The Git history is the revision history; each commit has one editorial purpose.
- A merged or retired item keeps its queue entry (status `merged` with `mergedInto`, or `retired` with `redirect`), so the record of what was published, and why it was withdrawn, is preserved.
- A substantive revision of a published item sets `updatedAt` (Section 8.1). Corrections of fact are made openly: the item's review record names the correction, and, where a reader may have relied on the earlier statement, the article says what changed.

## 11. Vietnamese translations

English is the original; Vietnamese translations under `/vi` follow `docs/translation-vi.md`. A translation inherits the English item's technical content but is not reviewed by these stages. Vietnamese originals (`originalLang: "vi"`, see `docs/translation-vi.md`) are not translations: the strategy applies to them in full, but the engine does not yet review, record or queue them (adoption plan, gap G12); closing that gap is part of the adoption plan. When an English item is revised, its translation is marked for update in the audit report; copied front-matter fields (dates, category, tags, series, order, flags) are kept identical in the same commit, as the build requires.

## 12. Governance of these standards

- The chief editor (Editorial Director role) owns this manual; [`strategy.md`](strategy.md) governs it. A change is made by pull request that edits this file and, where needed, `eos.config.json` and `glossary.json` together, with a version and date at the top and a line in the change log below.
- A new house term is added to `glossary.json` with a note giving the reason; a new banned phrase needs an example of the problem it prevents.
- An exception for one item (for example, a long description that cannot be shortened without losing meaning) is recorded in that item's review record notes, not by weakening the rule.
- The standards are reviewed when a new content type is added, when an audit finds a class of problem the rules did not catch, or at least once a year.

### Change log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-13 | First edition: roles, workflow, policies A-E, rubric, records, governance. |
| 2.0 | 2026-10-24 | Adopts the editorial strategy (`strategy.md`): identity and audience; value before volume, reader-value contract, value categories and formats (2.4); strategy roles and the chief-editor decision of 23 October (3); nine gates, editorial queue and status model, live-site review, corrections and maintenance (4); assumptions and evidence proportional to the claim (5.7); answer first, explicit comparisons, specific limitations (6.1); templates by format (6.7); visual communication (6.8); live-site acceptance (9.5); queue and live reviews in the records (10). |
