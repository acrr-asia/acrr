# ACRR — Editorial Strategy and Operating System

Status: supplied by San on 23 October 2026 and proposed for adoption as the governing editorial strategy. How it relates to the existing standards manual and tooling, and the order in which it is implemented, is set out in [`strategy-adoption-plan.md`](strategy-adoption-plan.md). Until that plan's first phase is merged, [`standards.md`](standards.md) v1.0 remains the operative manual.

## 1. Strategic direction

**Positioning:** ACRR is an independent technical publication focused on advanced computing, AI, robotics, control systems, and scientific methods. It combines technical publishing with a clearly differentiated technology journalism and science reporting stream.

**Primary audience:** Engineers, researchers, graduate students, and advanced technical learners.

**Commercial priorities:** Sponsorships, technical events, and enterprise content partnerships.

**Operating principle:** Optimize for reader value, technical credibility, and lasting usefulness—not publication volume.

ACRR should help readers accomplish at least one meaningful outcome:

- Understand a difficult concept accurately.
- Evaluate a technical claim or competing approaches.
- Reproduce a method, experiment, calculation, or implementation.
- Make a better engineering or research decision.
- Understand what a research result means in practice.
- Discover evidence, limitations, risks, or open questions they would otherwise miss.

A piece that is technically correct but merely repeats familiar information without improving the reader's understanding is not automatically worth publishing.

### Strategic pillars

**Technical publishing**

Tutorials, engineering guides, mathematical explanations, reproducible demonstrations, literature reviews, and technical comparisons.

**Technology and science reporting**

Original interviews, research profiles, institutional and industry reporting, field observations, and investigations into the gap between technical claims and actual results.

**Insights and analysis**

Evidence-based assessments of technical developments, competing approaches, industry changes, and unresolved questions.

**Learning paths and reference resources**

Structured collections that help readers progress from foundational concepts to advanced methods and practical applications.

These pillars must be distinguishable on the website. Readers should be able to tell whether a page is a tutorial, a research review, an opinion, a reported article, or sponsored material.

## 2. The editorial quality principle: value before volume

Every article must pass two separate tests.

**Test A — Is the content worth the reader's time?**

The article should deliver a specific intellectual or practical benefit that is not adequately available from existing ACRR content or from a more authoritative source.

**Test B — Is ACRR the right publisher for it?**

ACRR must have a reason to publish this particular version: better explanation, stronger evidence, useful synthesis, original reporting, reproducibility, a Vietnam-specific perspective, or a meaningful connection between research and engineering practice.

An article can be accurate and still fail both tests.

### The reader-value contract

Before drafting, the author must complete these statements:

- **Reader:** Who specifically needs this article?
- **Reader's problem:** What question, decision, misconception, or task does the reader have?
- **Expected outcome:** What will the reader understand or be able to do after reading?
- **Distinctive contribution:** What does this article add beyond existing ACRR pages and readily available sources?
- **Evidence:** What sources, data, derivations, experiments, or interviews support the contribution?
- **Limitations:** What will the article not establish or solve?

If these questions cannot be answered clearly, the idea should not enter production.

### Reader-value categories

Every article must have a primary value category.

| Category | Required reader benefit |
|---|---|
| Conceptual understanding | Explains a difficult concept or resolves a common misconception |
| Practical implementation | Enables the reader to implement, test, or troubleshoot something |
| Technical decision | Helps compare alternatives using explicit criteria |
| Research synthesis | Organizes and critically evaluates evidence from multiple sources |
| Original reporting | Provides verified information, access, observations, or perspectives unavailable from routine summaries |
| Reference value | Provides a reliable resource that readers can revisit |
| Critical analysis | Examines a claim, method, system, or trend and reaches a reasoned conclusion |

A topic label is not a value proposition. “Introduction to robotics” describes a subject; it does not explain why a particular article deserves to exist.

### Reject, merge, rewrite, or retire

The editorial team must be willing to reject content before publication and reconsider existing content afterward.

- **Reject:** No clear reader problem, weak evidence, redundant scope, or no defensible contribution.
- **Merge:** Multiple articles cover substantially the same concepts without providing distinct value.
- **Rewrite:** The subject is valuable, but the explanation, evidence, structure, or technical depth is inadequate.
- **Reclassify:** The content is useful but belongs in a different format, such as an Insight, reference page, or learning-path entry.
- **Retire:** The content is obsolete, misleading, irreparably weak, or no longer worth maintaining.
- **Keep and maintain:** The article provides distinctive value and remains accurate.

Retiring an article requires a redirect or other appropriate handling when readers or external links may depend on it. Preserve useful information before consolidating pages, and avoid deleting pages solely because their traffic is low.

## 3. The ACRR editorial governance model

The workflow must have distinct responsibilities, even if one person temporarily performs several roles.

### Author

Responsible for the article's central question, research, argument, references, technical work, visual assets, and revisions.

### Technical reviewer

Responsible for technical correctness, assumptions, equations, code, reproducibility, source quality, and limitations. The reviewer must disclose relevant conflicts of interest.

### Managing editor

Responsible for commissioning, editorial structure, reader value, clarity, sourcing, article classification, production status, and coordination of reviews.

### Chief editor

Responsible for the final editorial decision and the quality of the published website.

The chief editor must be able to inspect the live article at `https://acrr.asia/`, not merely the Markdown, MDX, or CMS draft. The review must include the rendered page, its navigation and metadata, and the presentation of diagrams, code, equations, tables, references, and mobile content where relevant.

### Publisher or commercial owner

Responsible for commercial relationships, budgets, contracts, events, and operations. Commercial ownership must not override editorial decisions.

### Independence rule

If ACRR is operated by one person, these roles can be combined operationally, but the checks must not disappear. For high-risk articles, the author should obtain a separate technical or editorial review rather than treating self-review as independent verification.

## 4. Standard publication workflow

The workflow is a sequence of approval gates, not a calendar. Work advances when the relevant acceptance criteria are met.

**Idea → Commissioning → Research → Draft → Technical review → Editorial review → Revision → Pre-publication checks → Publication → Chief editor's live-site review → Revision if required → Final acceptance → Monitoring and correction**

### Gate 1 — Idea approval

The author submits a short proposal containing:

- Working title and central question.
- Intended reader.
- Reader problem and expected outcome.
- Primary value category.
- Distinctive contribution.
- Proposed evidence and source access.
- Relationship to existing ACRR content.
- Proposed diagrams, tables, code, or other explanatory assets.
- Conflicts of interest or commercial relationships.

**Acceptance criterion:** The editor can explain why this article is worth the intended reader's time in one or two sentences.

### Gate 2 — Research readiness

Before substantial drafting, the author establishes the evidence base.

For technical content, this may include primary research, official technical documentation, standards, mathematical derivations, source code, datasets, benchmarks, or reproducible experiments.

For reporting, it may include interviews, public records, direct observations, research papers, institutional statements, and independent corroboration appropriate to the claims.

The author records:

- Claim or proposition.
- Supporting source or evidence.
- Source quality and limitations.
- Verification status.
- Unresolved uncertainty.

**Acceptance criterion:** The central argument is supportable. The author is not relying on a collection of loosely related links or on unsupported summaries of other people's work.

### Gate 3 — Draft completion

A draft must contain the actual explanation, evidence, reasoning, and proposed visuals. It must not be a collection of headings awaiting substance.

The draft should identify:

- The question being answered.
- The answer or main conclusion.
- The reasoning and supporting evidence.
- Important assumptions.
- Counterarguments or alternative explanations where relevant.
- Limitations and practical implications.
- References and supporting materials.

**Acceptance criterion:** A qualified reader can understand the article's central argument without needing the author to explain what the draft is trying to say.

### Gate 4 — Technical review

The technical reviewer checks correctness and completeness.

For mathematical and engineering content, review:

- Definitions and notation.
- Units, dimensions, signs, and boundary conditions.
- Derivations and intermediate reasoning.
- Assumptions and applicability.
- Code correctness, dependencies, versions, and execution instructions.
- Experimental design and reproducibility.
- Comparability of benchmark results.
- Whether conclusions follow from the evidence.
- Limitations and failure conditions.

For research reviews, check whether the selected sources fairly represent the evidence and whether the article distinguishes established findings from contested interpretations.

**Acceptance criterion:** No unresolved critical technical error remains. Any limitations that materially affect the conclusion are stated.

### Gate 5 — Editorial review

The managing editor evaluates the article from the reader's perspective.

The review covers:

- Relevance to the intended audience.
- Clarity of the main answer.
- Originality and differentiation.
- Logical structure.
- Evidence quality and attribution.
- Unnecessary repetition.
- Terminology and definitions.
- Balance and fairness.
- Usefulness of examples.
- Appropriate visual presentation.
- Headline accuracy.
- Whether the conclusion provides a real takeaway.

The editor must explicitly identify content that is technically correct but does not contribute to the reader's understanding.

**Acceptance criterion:** The article delivers a clear, defensible benefit and can be read without unnecessary effort.

### Gate 6 — Pre-publication checks

Before publication, verify:

- Correct title, summary, author, content type, and publication date.
- Accurate references and working links.
- Proper attribution and usage rights for images, diagrams, code, and datasets.
- Correct mathematical notation and code formatting.
- Appropriate disclosures of funding, sponsorship, and conflicts.
- Accessibility and responsive presentation.
- Appropriate treatment of uncertainty and limitations.
- Privacy, confidentiality, and legal concerns.
- Relevant AI-use disclosures where required.

**Acceptance criterion:** The page is ready for public access, and all mandatory checks have been completed.

### Gate 7 — Publication and live-site inspection

Publishing the page does not complete the workflow.

After publication, the chief editor opens the actual public URL and evaluates the rendered result.

The review must include:

1. The title and opening screen.
2. The article's main answer and argument.
3. The structure and flow of sections.
4. Equations, code blocks, tables, diagrams, images, and captions.
5. References and internal links.
6. Related content and navigation.
7. Desktop and mobile readability.
8. Missing content, rendering defects, and visual inconsistencies.
9. Whether the published version still satisfies the reader-value contract.

The chief editor records the URL, review result, findings, and required actions.

**Acceptance criterion:** The published page meets ACRR's editorial and presentation standards, not merely its build or deployment requirements.

### Gate 8 — Chief editor's feedback and revision

If the live-site review finds problems, the chief editor creates a structured revision request.

Each finding must specify:

- **Location:** Section, paragraph, figure, table, or URL.
- **Problem:** What is incorrect, unclear, redundant, missing, or visually ineffective?
- **Why it matters:** How does it harm accuracy, understanding, usability, or reader value?
- **Required action:** What change is expected?
- **Priority:** Critical, major, or minor.
- **Acceptance condition:** What evidence will show that the issue has been resolved?

The author revises the source content and republishes the page. The chief editor then inspects the updated live page.

This cycle repeats until the acceptance conditions are met or the article is rejected, retired, or explicitly accepted with documented non-critical limitations.

The chief editor should not merely say “improve clarity” or “make this more professional.” Feedback must be specific enough that the author can act on it.

### Gate 9 — Final acceptance and post-publication maintenance

After approval, record the final status and preserve the review history.

Readers must have a way to report errors. Material corrections should be made promptly and documented. Technical articles should be reassessed when relevant standards, software versions, evidence, or assumptions change.

An article can be editorially accepted and still require future maintenance.

## 5. The chief editor's live-site review system

ACRR should maintain a central editorial queue, separate from the website's visual design and from any particular publishing tool.

Each content item should have:

- Stable article identifier.
- Current public URL, if published.
- Source file or CMS reference.
- Author and reviewers.
- Content classification.
- Primary reader-value category.
- Workflow status.
- Technical-review status.
- Editorial-review status.
- Chief-editor review status.
- Outstanding findings.
- Revision history.
- Publication and update records.
- Known conflicts or disclosures.

### Recommended status model

`Proposed → Approved for research → Drafting → Technical review → Editorial review → Revision required → Ready to publish → Published, awaiting live review → Revision required after publication → Accepted → Maintenance`

Additional terminal or exceptional states should include `Rejected`, `Merged`, `Retired`, and `Blocked`.

Do not treat a successful website build, deployment, or automated test as editorial approval. Technical quality assurance and editorial acceptance are different controls.

### Live-review report template

For every reviewed page, the chief editor should produce a report with these sections:

**A. Decision**

Accept, accept with minor follow-up, request revision, block publication, or recommend retirement.

**B. Reader-value assessment**

- What will the intended reader learn or accomplish?
- Is that benefit delivered?
- What remains missing?
- Is the article worth its reading effort?

**C. Substantive findings**

List issues with location, severity, evidence, required action, and acceptance condition.

**D. Visual and structural findings**

Identify content that should be represented more effectively as a diagram, chart, table, comparison matrix, numbered procedure, summary, or interactive demonstration.

**E. Technical and source findings**

Identify incorrect claims, weak evidence, missing definitions, unverifiable references, unsupported conclusions, or reproducibility problems.

**F. Required changes**

Provide an actionable checklist. Separate mandatory changes from optional improvements.

**G. Re-review**

After changes are deployed, inspect the updated URL and close each finding only after confirming that the acceptance condition has been met.

### Chief editor's authority

The chief editor may reject an article even if it is technically correct when it lacks sufficient reader value, repeats existing content, or imposes unnecessary reading effort.

The chief editor may also require an existing article to be rewritten, consolidated, reclassified, or retired.

## 6. Scientific communication and professional problem-solving standards

ACRR should adopt a consistent set of public, transferable principles associated with rigorous scientific communication, professional consulting, and high-quality technical publishing.

The aim is not to imitate the branding or proprietary internal methods of any particular firm. The aim is to make reasoning explicit, evidence traceable, and communication efficient.

### Principle 1 — Answer first, then explain

For decision-oriented articles, state the principal answer or conclusion near the beginning.

A useful opening usually establishes:

- The question.
- The answer or main finding.
- Why it matters.
- The conditions or limitations under which the answer holds.

Do not make readers traverse a long history of a topic before revealing what the article is actually arguing.

Exceptions are appropriate for narrative reporting, investigative features, and tutorials in which a sequence of discovery is essential to understanding.

### Principle 2 — Use a logical argument structure

Apply the Pyramid Principle as a writing technique: lead with the central answer, then organize supporting reasons into clear groups, then provide the evidence.

Use MECE—mutually exclusive and collectively exhaustive—as a diagnostic when categorizing problems or alternatives. It is not a requirement to force every subject into artificial categories.

For analytical articles, a useful structure is:

1. Main conclusion.
2. Supporting arguments.
3. Evidence for each argument.
4. Assumptions and limitations.
5. Implications or recommended next steps.

Every major section should support the central question. Sections that do not support it should be removed, relocated, or justified.

### Principle 3 — Separate facts, interpretations, and recommendations

Readers must be able to distinguish:

- **Fact:** What the source, measurement, experiment, or observation establishes.
- **Interpretation:** What the evidence may mean.
- **Assumption:** What is being taken as given but has not been established.
- **Recommendation:** What action follows under specified goals and constraints.
- **Uncertainty:** What remains unknown or contested.

Do not turn an author's interpretation into an established scientific result through confident wording.

### Principle 4 — Use evidence proportional to the claim

The stronger or more consequential the claim, the stronger the supporting evidence should be.

Prefer primary papers, official documentation, standards, original datasets, reproducible code, and direct reporting when appropriate. Secondary sources are useful for orientation and synthesis but should not silently replace primary evidence for important technical claims.

For quantitative claims, state the relevant measurement, comparison basis, sample or experimental conditions where material, and limitations.

A citation is not proof by itself. The article must accurately represent what the cited source supports.

### Principle 5 — Make comparisons explicit

When comparing algorithms, architectures, models, products, or methods, define the decision criteria before declaring a winner.

Possible criteria include:

- Accuracy or error.
- Latency and throughput.
- Compute and memory requirements.
- Cost.
- Robustness and failure modes.
- Reproducibility.
- Maintainability.
- Security and privacy.
- Deployment constraints.
- Suitability for the intended task.

Use a comparison table when readers need to compare multiple dimensions. Do not collapse a multi-dimensional trade-off into an unsupported ranking.

### Principle 6 — Prefer explanatory structure over rhetorical volume

Long articles are justified when the subject requires depth, not simply because the author has accumulated information.

Use definitions, examples, equations, diagrams, tables, and short summaries to reduce the cognitive effort needed to follow the argument.

Remove paragraphs that repeat a previous conclusion, restate a diagram without adding interpretation, or introduce background unrelated to the central question.

### Principle 7 — Make limitations visible

Every substantial technical analysis should address the relevant limitations.

Examples include assumptions, data quality, external validity, computational cost, hardware constraints, software-version dependence, benchmark bias, incomplete evidence, and unresolved research questions.

Limitations should be specific. “Further research is needed” is not sufficient if the actual uncertainty can be identified.

### Principle 8 — Make the output actionable when the subject permits

A practical guide should leave the reader with something usable: a tested procedure, a decision framework, a worked example, a reproducible implementation, a checklist, or an explicit next step.

A conceptual or research article does not need to invent an implementation merely to appear practical. Its value may instead be a clearer mental model or a better understanding of evidence.

## 7. Visual communication standard

Text should not be the default representation for every kind of information.

During drafting and editorial review, authors must identify material that could be communicated more effectively through a visual structure. The goal is to improve understanding, not to decorate the page.

### Visual selection rules

| Information or reasoning | Preferred representation |
|---|---|
| Sequence of operations or system behavior | Flowchart or sequence diagram |
| System components and relationships | Architecture or block diagram |
| Change over time | Line chart |
| Comparison across categories | Bar chart or comparison table |
| Distribution or spread | Histogram, box plot, or distribution plot |
| Relationship between two measured variables | Scatter plot |
| Multi-step algorithm | Pseudocode, numbered procedure, or flow diagram |
| Mathematical derivation | Equations with intermediate steps and explanatory annotations |
| Competing approaches and trade-offs | Decision matrix |
| Classification or taxonomy | Hierarchical diagram or structured table |
| Research workflow | Methodology diagram |
| Experimental setup | Labelled schematic or photograph with a caption |
| Control-system response | Plot with clearly labelled variables, units, and conditions |
| Complex spatial or mechanical relationships | Appropriate schematic, CAD rendering, or annotated illustration |
| Key findings from a long article | Concise summary table or findings list |

Do not use a chart when the underlying data are unavailable or incomparable. Do not convert every paragraph into a visual. Use prose when nuance, qualifications, or narrative explanation are essential.

### Required visual review questions

For every substantial article, the author and editor must ask:

- Would a diagram reduce the effort needed to understand the main concept?
- Would a table make the comparison easier to inspect?
- Would a chart reveal a pattern that prose would obscure?
- Would an annotated example expose an important assumption?
- Would a worked calculation make the reasoning verifiable?
- Would an interactive demonstration genuinely improve understanding, or would a static figure be sufficient?

Record the decision for substantial visual opportunities. If a visual is not used, the explanation should remain clear without it.

### Chart integrity

Charts must include appropriate titles, axis labels, units, legends where necessary, data provenance, and relevant methodological notes.

The presentation must not distort the evidence through misleading scales, omitted comparison conditions, unsupported extrapolation, or visual emphasis that exaggerates a result.

Captions should explain what the reader should notice and, where relevant, what the chart does not establish. A caption should not merely repeat the title.

### Diagram integrity

Diagrams should communicate a real relationship, process, structure, or distinction.

Use consistent terminology and distinguish conceptual illustrations from measured or experimentally validated results. Label simplified models as simplified when that distinction matters.

### Technical implementation on ACRR

The publishing system should support, as appropriate:

- Responsive figures and tables.
- Accessible captions and alternative text.
- High-resolution images where detail matters.
- Code and equations that remain readable on mobile devices.
- Mermaid or equivalent diagrams where suitable.
- Interactive demonstrations with a static explanatory fallback.
- Source data or code links where available and permitted.
- Consistent styling without sacrificing scientific precision.

Visual assets must be checked on the rendered website. A correct diagram in a source file is not useful if it is clipped, unreadable, or broken on the public page.

## 8. Article structure templates

Templates should standardize quality without forcing every article into the same shape.

### A. Technical explainer

1. **The question:** What problem or concept is being explained?
2. **Short answer:** The core explanation.
3. **Prerequisites:** Definitions the reader needs.
4. **Conceptual model:** A diagram or intuitive explanation where appropriate.
5. **Technical explanation:** The method, mechanism, mathematics, or architecture.
6. **Worked example:** An example that demonstrates the reasoning.
7. **Practical application:** When and how the method is useful.
8. **Limitations and failure modes:** Conditions under which the explanation or method does not apply.
9. **Summary:** The essential takeaways.
10. **References and further study:** Sources and genuinely useful follow-up material.

### B. Technical comparison or decision analysis

1. Decision to be made.
2. Intended use case and constraints.
3. Evaluation criteria.
4. Evidence and comparison methodology.
5. Comparison table or visualization.
6. Trade-offs and failure modes.
7. Recommendation conditional on the use case.
8. Remaining uncertainty.
9. Sources and reproducibility information.

### C. Research review

1. Research question and scope.
2. Why the question matters.
3. Search or source-selection approach where appropriate.
4. Relevant concepts and terminology.
5. Findings organized by theme, method, or evidence.
6. Agreements, disagreements, and methodological limitations.
7. Evidence gaps and unresolved questions.
8. Implications for research or engineering.
9. References.

Do not call an article a systematic review unless the methods justify that designation.

### D. Technology and science reporting

1. The development, claim, or issue being reported.
2. Why it matters to the intended audience.
3. What is known and how it is established.
4. Relevant people, institutions, and primary sources.
5. Independent context or corroboration appropriate to the claims.
6. Competing perspectives or right of reply where warranted.
7. Distinction between reported facts and the reporter's interpretation.
8. Practical implications and unresolved questions.
9. Sources, disclosures, and relevant methodology.

Interview-based content should preserve the meaning of the interviewee's statements. Quotations must not be invented or altered to imply a different meaning.

### E. Insight or short analysis

1. The main observation.
2. Evidence supporting it.
3. Why it matters.
4. What alternative explanation or limitation should be considered.
5. The implication or open question.

An Insight should not be a lightly rewritten news item or a collection of unsupported opinions.

## 9. Existing content audit and remediation

The existing ACRR library must be evaluated against the new standards. The goal is not to preserve every URL; it is to preserve and improve the value of the publication as a whole.

### Audit dimensions

For each published article, assess:

- Reader and intended outcome.
- Distinctive contribution.
- Technical correctness.
- Evidence quality and reference integrity.
- Clarity and structure.
- Completeness of definitions and assumptions.
- Visual communication.
- Reproducibility where relevant.
- Currency and version dependence.
- Overlap with other ACRR articles.
- Search and navigation usefulness.
- Public presentation quality.
- Maintenance burden.

### Remediation decision

Assign each article a decision:

- Retain.
- Retain and update.
- Rewrite substantially.
- Merge with another article.
- Reclassify.
- Archive or retire.

The decision must include a rationale and an owner. High-risk technical errors, misleading claims, broken core explanations, and materially defective reporting should take precedence over cosmetic improvements.

### Value-density test

Reviewers should identify the amount of useful understanding delivered relative to the effort required to read the article.

Ask:

- Does each major section advance the central question?
- Are prerequisites explained at the point they become necessary?
- Are important concepts defined before use?
- Are examples doing explanatory work?
- Is the same information repeated in several sections?
- Can a table, figure, or structured list replace a long and difficult passage?
- Does the conclusion tell the reader something not already established?
- Could the article be shorter without losing useful reasoning?

The goal is not minimal word count. It is high explanatory value per unit of reader effort.

## 10. Website backlog and acceptance criteria

Work should be prioritized by dependency, risk, reader value, and operational capacity. There are no fixed calendar deadlines in this operating plan; the executor determines sequencing and duration.

### Priority A — Editorial control and trust

- Establish author, editor, and publisher information appropriate to the operating model.
- Publish editorial, correction, AI-use, and sponsorship policies.
- Establish content classifications and disclosures.
- Create a central editorial queue and revision history.
- Implement the chief editor's live-site review and feedback workflow.
- Audit the existing article library.
- Verify references and address critical technical errors.
- Establish privacy, copyright, and legal review procedures.

**Acceptance condition:** ACRR can trace an article from proposal through review and publication, identify who approved it, and verify the actual public page against recorded findings.

### Priority B — Article quality and discovery

- Standardize article metadata and author pages.
- Improve internal links between related concepts.
- Review series ordering and completeness.
- Improve navigation between technical articles, reporting, Insights, and learning resources.
- Establish accessible diagrams, tables, equations, and code presentation.
- Improve search and related-content recommendations where justified.
- Establish maintenance and retirement procedures.

**Acceptance condition:** Readers can identify the type and purpose of an article, navigate to relevant material, and use the content without avoidable presentation defects.

### Priority C — Audience relationship

- Establish the newsletter and its privacy workflow.
- Create an audience feedback mechanism.
- Identify which topics and formats provide the greatest reader value.
- Develop learning paths around demonstrated demand.
- Track meaningful engagement rather than relying solely on page views.

**Acceptance condition:** ACRR can explain which reader needs it serves, which content produces repeat engagement, and what evidence supports its editorial priorities.

### Priority D — Commercial readiness

- Prepare a fact-based media kit.
- Define sponsorship and enterprise content offers.
- Establish event planning and evaluation procedures.
- Prepare written commercial terms and disclosure rules.
- Maintain a conflict-of-interest register.
- Track project revenue, direct costs, time, and reusable assets.

**Acceptance condition:** Commercial offers are clearly scoped, transparent, operationally feasible, and compatible with editorial independence.

### Priority E — Selective expansion

Consider resource directories, downloadable engineering references, additional learning paths, public event archives, and community contributions only when audience evidence and maintenance capacity justify them.

Do not introduce complex community, membership, or monetization features simply because they are common on other publishing platforms.

## 11. Sponsorship, events, and enterprise partnerships

ACRR's commercial model should reinforce its technical credibility without allowing clients to purchase editorial conclusions.

### Potential offers

**Technical event sponsorship**

Seminars, expert discussions, technical workshops, and research-to-industry roundtables.

**Sponsored educational content**

Clearly labelled technical explainers, educational series, or demonstrations with transparent limitations and product relationships.

**Enterprise research communication**

Technical reports, educational resources, research summaries, and events commissioned by companies or institutions.

**Independent editorial reporting**

Reporting and analysis governed by ACRR's editorial standards. It must not be sold as independent reporting if a client controls the conclusion or the content is fundamentally promotional.

### Commercial acceptance criteria

Before accepting an assignment, document:

- Scope and intended audience.
- Deliverables and acceptance conditions.
- Source material and verification responsibilities.
- Ownership and reuse rights.
- Confidentiality and publication restrictions.
- Disclosure requirements.
- Payment and cancellation terms.
- Responsibility for claims, data, images, and product demonstrations.
- Editorial independence and the right to report material limitations.
- Handling of corrections and disputed claims.

A sponsor may fund a topic or event. It must not be allowed to suppress a material finding or dictate an unsupported conclusion.

## 12. KPI framework

KPIs must measure quality, reader outcomes, operational reliability, and commercial sustainability together. Baselines should be established from actual data before setting numerical growth targets.

### Editorial quality

- Percentage of new articles with an approved reader-value proposition.
- Percentage completing the required technical and editorial checks.
- Percentage of published pages reviewed by the chief editor.
- Number and severity of unresolved review findings.
- Rework rate and recurring defect categories.
- Material correction frequency and resolution time.
- Percentage of priority articles with verified references and appropriate visual review.

### Reader value

- Returning readers and meaningful engagement.
- Reader feedback about usefulness and clarity.
- Engagement with learning paths and related articles.
- Completion or use of practical examples, code, or resources where measurable.
- Evidence that readers use ACRR content to solve a problem, evaluate an approach, or deepen understanding.

Time on page must be interpreted carefully: a long visit may indicate deep engagement or a confusing article.

### Content portfolio

- Distribution across technical publishing, reporting, and Insights.
- Number of high-priority articles improved or consolidated.
- Coverage gaps and redundant content.
- Performance and maintenance burden of each series.
- Contribution of original reporting and reproducible technical work.

### Audience development

- Newsletter subscriptions and unsubscribes.
- Returning readers from direct channels.
- Relevant referrals and qualified professional engagement.
- Feedback from engineers, researchers, and advanced learners.

### Commercial sustainability

- Qualified partner conversations.
- Conversion of proposals into paid work.
- Revenue by commercial offer.
- Direct costs and effective hourly return.
- Repeat partnership rate.
- Sponsor concentration and conflict exposure.
- Event registration, attendance, feedback, and financial outcome.

### Operating rules

Do not increase output merely because traffic is growing. Do not keep a content format solely because it produces page views. Do not judge a research reference article by the same criteria as a reported feature or a newsletter.

Use evidence to determine which activities should continue, change, expand, or stop.

## 13. Legal and ethical controls in Vietnam

This checklist is for operational planning and is not a legal opinion. The actual obligations depend on ACRR's legal operator, publishing model, distribution methods, and commercial activities.

### Website and publishing classification

Review the applicability of:

- Press Law No. 126/2025/QH15.
- Decree No. 237/2026/ND-CP.
- Decree No. 147/2024/ND-CP.

Obtain qualified legal advice on whether ACRR's current and planned activities require particular licensing, registration, or notification. Do not assume that a technical website is automatically subject to every rule governing a licensed press agency, or that calling a site a technical publication exempts it from applicable rules.

### Advertising and sponsorship

Review the Advertising Law amendment, Law No. 75/2025/QH15, and applicable implementing rules.

Distinguish sponsored content from independent editorial work. Disclose commercial relationships clearly, substantiate claims, and assess sector-specific restrictions where relevant.

### Personal data

Review Personal Data Protection Law No. 91/2025/QH15 and applicable implementing rules.

Document data collected through newsletters, analytics, interviews, contact forms, and events. Review purpose, lawful basis, consent where required, retention, access, deletion, service providers, cross-border transfers, and the use of recordings or identifiable information.

### Copyright and research integrity

Verify permissions and licences for third-party images, diagrams, code, datasets, and text. Define author attribution, contributor agreements, publication rights, and reuse terms.

Do not claim peer review, experimental validation, or independent replication unless those processes actually occurred.

### AI-assisted production

Require human verification of substantive claims. Do not fabricate interviews, sources, experiments, datasets, or media presented as authentic. Apply relevant disclosure requirements and maintain sufficient records for consequential claims.

### Commercial and employment obligations

Review legal and tax treatment, contracts, invoicing, intellectual-property rights, confidentiality, liability, and potential conflicts with the founder's primary employment.

**Legal go/no-go condition:** Before introducing a materially new publishing or revenue activity, establish the applicable regulatory classification, required permissions, disclosure obligations, data and copyright controls, contract terms, and tax treatment.

## 14. Operating review and continuous improvement

The operating review should be triggered by work status and available evidence, not by fixed calendar dates.

At each review, ask:

- Which articles are blocked, and why?
- Which chief-editor findings remain unresolved?
- Which defects recur across multiple articles?
- Which published articles fail the reader-value test?
- Which technical claims or references need reassessment?
- Which visual improvements would most improve understanding?
- Which series or learning paths remain incomplete or incoherent?
- Which audience needs are not being met?
- Which commercial activities justify their costs and effort?
- Which processes should be simplified, automated, or stopped?

Record decisions, owners, and acceptance conditions. Update the backlog according to dependencies and impact.

## 15. Definition of success

ACRR succeeds when it becomes a trusted specialist publication with:

- A technical library whose articles deliver clear and defensible reader value.
- A repeatable publication process with technical review, editorial review, and chief-editor inspection of live pages.
- A documented mechanism for revision, correction, consolidation, and retirement.
- Scientific and analytical communication that makes reasoning, evidence, and uncertainty explicit.
- Effective use of diagrams, charts, tables, worked examples, and other appropriate explanatory formats.
- An original reporting stream that distinguishes verified facts from interpretation.
- A direct relationship with a relevant specialist audience.
- Commercial partnerships and events that are financially useful without compromising editorial independence.
- An operating model that can be maintained with the available people, time, and resources.

The central objective is not to publish more. It is to make every published page earn the reader's attention—and to improve or remove pages that do not.
