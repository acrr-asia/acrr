<!-- audit: {"slug":"series-identity-and-access-control","type":"series","series":"identity-and-access-control","priority":"P1","before":{"purpose":2,"structure":2,"accuracy":4,"evidence":3,"language":3,"consistency":3,"publishing":3},"findings":{"blocking":0,"shouldFix":4,"optional":1}} -->
# Audit: Identity and Access Control (series overview)

- Path: `src/content/series/identity-and-access-control.md` · Route: `/series/identity-and-access-control` · Type: series overview · 7 entries, status published, no planned entries · Words: 54 (from `eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 2: the body names the reader ("readers who build or review networked software") but states no prerequisites, although the entries assume familiarity with HTTP-based software, public-key signatures and basic web development.
- structure 2: no sequence rationale beyond "the first entry gives the whole picture from the top down; each later entry takes one layer"; it does not say how the seven entries connect or why they come in this order (standards 6.5).
- accuracy 4.
- evidence 3: no sources needed on an overview; conventions (citation by RFC number, HTTP/1.1 syntax, illustrative values) are stated only inside entries.
- language 3: the description is a fragment ("A series on how ..."), not a sentence.
- consistency 3: the four objectives cover entries 1, 3, 4 and 5 and part of 6, but nothing names what entries 2 (authenticators), 6 (sender-constrained tokens) and 7 (service-to-service authentication) let the reader do, so three entries teach outcomes the overview never promises.
- publishing 3: metadata within limits (description 157 characters).

## Priority

P1: the front door of the series; the missing prerequisites and sequence rationale are problems every entry depends on.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| D1 | Should fix | body, line 16 | structure | No sequence rationale; does not say how the entries connect. |
| D2 | Should fix | body, line 16 | purpose | No prerequisites. |
| D3 | Should fix | `objectives`, lines 9–13 | consistency | Objectives do not cover entries 2, 6 and 7. |
| D4 | Should fix | body | consistency | Shared conventions (HTTP/1.1 syntax, illustrative values, standards cited by RFC number, language-neutral pseudocode) are not stated on the overview. |
| C1 | Optional | `:6` | language | Description is a fragment. |

### D1. Sequence rationale
- **Where:** line 16
- **Text:** "The first entry gives the whole picture from the top down; each later entry takes one layer of that picture and goes further into it."
- **Problem:** Standards 6.5 requires the sequence rationale and what each entry contributes. The order (model, authenticators, sessions, authorization, OAuth grants, binding, services) follows the path of a request and the two questions of entry 1, but the overview does not say so.
- **Correction:** A paragraph that follows a request: authentication (entries 2 and 3), authorization (entry 4), delegation (entry 5), binding (entry 6), internal calls (entry 7).

### D2. Prerequisites
- **Text:** "intended for readers who build or review networked software"
- **Correction:** State the assumed background: writing or reading code for a web application or HTTP API; the idea of public-key signatures and hash functions at the level of what they guarantee (entry 1 and entry 2 introduce what the series needs). No cryptography mathematics is required.

### D3. Objectives
- **Problem:** Standards 6.5: 3–6 checkable outcomes, each covered by an entry. Entries 2, 6 and 7 are the main subject of no objective.
- **Correction:** Add two objectives (total 6): "Evaluate authenticators by their resistance to online guessing, verifier compromise, replay and phishing, and explain why origin-bound public-key credentials resist phishing." and "Design authentication between services with workload identities, sender-constrained tokens and per-hop token exchange instead of network location, forwarded tokens or trusted headers."

### D4. Conventions
- **Correction:** One paragraph: HTTP messages in HTTP/1.1 text syntax; tokens, keys and timestamps are illustrative; standards cited by RFC number and listed in each entry's References; pseudocode is language-neutral.

### C1. Description
- **Text:** "A series on how networked systems decide who is making a request and what that party may do, from the access-control model down to protocols and token formats."
- **Correction:** "Learn how networked systems establish who is making a request and decide what it may do, from the access-control model to tokens and calls between services." (one sentence; within 70–165 characters).

## Revision log (wave 1)
- Structure: body rewritten as three paragraphs: reader and prerequisites (D2); sequence rationale following a request through the system, with what each entry contributes (D1); shared conventions (D4).
- Objectives: two added (now six), so that entries 2 and 6–7 are covered: "Evaluate authenticators ..." (placed second, after the separation objective) and "Design authentication between services ..." (last). The four existing objectives are unchanged in wording.
- Metadata: description rewritten as one sentence (156 characters). `status`, `category`, `example`, `plannedEntries` unchanged; authoring comment kept.
- Remaining warnings: none.
- Flags for independent review (series): confirm that the two new objectives are fully delivered (objective 2 by entry 2 §1–§6; objective 6 by entry 6 and entry 7 §2–§5); the series review stamp is now stale because the series file and all English entries changed.
- Vietnamese translation affected: yes. New description, two new objectives (pairing check compares only status, category, example and the planned-entry count, so the build does not fail, but the translation now lists four objectives against six), and the body is replaced by three new paragraphs.
