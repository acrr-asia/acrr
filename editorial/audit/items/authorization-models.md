<!-- audit: {"slug":"authorization-models","type":"article","series":"identity-and-access-control","priority":"P2","before":{"purpose":3,"structure":3,"accuracy":4,"evidence":2,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":6,"optional":2}} -->
# Audit: Authorization Models: RBAC, ABAC and Relationship-Based Access

- Path: `src/content/blog/authorization-models.mdx` · Route: `/blog/authorization-models` · Type: article · Series `identity-and-access-control`, entry 4 of 7 · Words: 2575 (from `eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 3: clear; the second opening paragraph ends in a prose table of contents ("The entry starts from ..., then examines ..., and ends with ...").
- structure 3: sound; three H3 headings are all "The structure" (2.1, 3.1, 4.1).
- accuracy 4.
- evidence 2: reference list not in house format: titles in quotes with the comma outside, no volume or pages, Lampson listed first out of alphabetical order, "OASIS, *eXtensible Access Control Markup Language (XACML)*." with no version or year, "ANSI INCITS 359, *Role Based Access Control* (2004; revised 2012)" combining two editions in one entry, "*IEEE Computer*" and "*Communications of the ACM*" without volume, issue or pages.
- language 3: "actually" (54), "simply" (116); British "organisation" (50; `organisation_id` in an SQL fragment, 206).
- consistency 3: "the first entry" (lines 18, 41, 126, 130, 210, 216) never linked.
- publishing 2: description 264 characters; six title-case H2 headings; three duplicate H3 headings.

## Accuracy check

Bibliographic details checked: Lampson 1971, *Proc. Fifth Princeton Symposium on Information Sciences and Systems*, pp. 437–443; Harrison, Ruzzo and Ullman, *Commun. ACM* 19(8):461–471, August 1976; Ferraiolo and Kuhn, 15th National Computer Security Conference, pp. 554–563, 13 October 1992 (csrc.nist.gov); Sandhu et al., *IEEE Computer* 29(2):38–47, February 1996 (profsandhu.com); INCITS 359-2012 revises INCITS 359-2004 (webstore.ansi.org); NIST SP 800-162, Hu et al., January 2014 with updates of 2 August 2019 (csrc.nist.gov); XACML Version 3.0, OASIS Standard, 22 January 2013 (oasis-open.org); Pang et al., USENIX ATC 2019, pp. 33–46 (usenix.org).

## Priority

P2.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 264 characters. |
| P2 | Should fix | H2 headings | language | Title case. |
| P3 | Should fix | lines 58, 91, 144 | publishing | Three headings "The structure". |
| P4 | Should fix | lines 243–252 | evidence | References not in house format (see above). |
| D1 | Should fix | lines 16, 18, 41 | consistency | Entries named but not linked. |
| C1 | Should fix | lines 60, 120, 130 | language | ANSI, INCITS, XACML, OASIS, HR not expanded. |
| A1 | Optional | line 48 | evidence | Bell–LaPadula (1973) and Biba (1977) are dated in the text but not referenced; dates match the usual citations (MITRE reports) but were not checked against a primary source here. Flag for the fact-checker. |
| C2 | Optional | lines 54, 116, 50 | language | "actually", "simply"; "organisation". |

### P3. Duplicate headings
- **Correction:** "2.1 Users, roles and permissions", "3.1 Rules over attributes", "4.1 Relationships as data". No link in `src/` targets these anchors.

### P1. Description
- **Correction:** "Learn how ACLs, capabilities, RBAC, ABAC and ReBAC represent policy, and how the choice shapes auditing, list filtering and change over time." (one sentence, within limits)

## Revision log (wave 1)
- Structure: duplicate headings renamed: "2.1 Users, roles and permissions", "3.1 Rules over attributes", "4.1 Relationships as data" (P3). §2.1's 52-word opening sentence split into three (formalization; standardization; what RBAC does).
- Prose: "actually", "simply" removed; policy information points sentence rewritten without a parenthesized list.
- Terminology/style: six H2 headings in sentence case; INCITS, ANSI, XACML, OASIS, HR expanded; "organisation" → "organization" (prose and the SQL fragment).
- Metadata: description 153 characters.
- References: rewritten in house format, alphabetical, with volume, issue and pages where checked (sources in the accuracy check above); the 2004 and 2012 editions of INCITS 359 listed as separate entries; XACML now Version 3.0, OASIS Standard, 2013.
- Cross-references: links to the second and third entries (opening), the first entry §4.2 and §5.2 (twice), and the next entry.
- Remaining suggestions and why they stay: "ACL" flagged in the heading of §1.2 (expanded in the first bullet below it); ACM, SP and USENIX occur only in reference entries; the 52-word sentence at line 146 is a list of three parallel examples.
- Flags for independent review: (fact-check) the title of the 2004 edition of INCITS 359 is assumed identical to the 2012 title checked on webstore.ansi.org; Bell–LaPadula (1973) and Biba (1977) dates unreferenced (A1).
- Vietnamese translation affected: yes, in headings 2.1, 3.1 and 4.1 and the References list; no technical change.

## Independent review (wave 2)

- Report: `reviews/identity-and-access-control.md`
- Fact-check: pass
- Technical: pass
- Findings: F3 (optional), S2 (optional), S1 (should fix, Vietnamese translation)
- Not verified: none.
