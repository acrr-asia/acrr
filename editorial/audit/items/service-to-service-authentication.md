<!-- audit: {"slug":"service-to-service-authentication","type":"article","series":"identity-and-access-control","priority":"P2","before":{"purpose":3,"structure":2,"accuracy":4,"evidence":2,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":6,"optional":2}} -->
# Audit: Service-to-Service Authentication

- Path: `src/content/blog/service-to-service-authentication.mdx` · Route: `/blog/service-to-service-authentication` · Type: article · Series `identity-and-access-control`, entry 7 of 7 · Words: 2606 (from `eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 3: clear; earlier entries not linked.
- structure 2: the entry ends with "## 7. Summary" (table only) followed by "## 8. The Series in One Picture", and the References sit under §8. Standards 6.2 item 6: the Summary ends with the closing paragraph, which for the last entry closes the series against its objectives; §8 recaps the entries but never refers to the objectives.
- accuracy 4: the Transaction Tokens work is still an Internet-Draft (draft-ietf-oauth-transaction-tokens-11, July 2026), so "IETF work in progress" stands; NIST SP 800-207 is August 2020 (csrc.nist.gov).
- evidence 2: references not in house format: "RFC 8693 (OAuth 2.0 token exchange), RFC 7523 (...), RFC 8705 (...)" lumped in one line; "SPIFFE specifications (...)" and "In progress at the IETF: OAuth Transaction Tokens" without authors or year; Hardy without volume or pages.
- language 3: "an organisation's" (85); sentences of 46–48 words (18, 46, 99).
- consistency 3: "the first entry", "the fifth entry", "the previous entry" unlinked.
- publishing 2: description 326 characters; six title-case H2 headings.

## Priority

P2.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| D1 | Should fix | §7–§8, lines 180–213 | structure | Summary does not close the series; §8 separates References from the Summary. |
| P1 | Should fix | `:3` | publishing | Description 326 characters. |
| P2 | Should fix | H2 headings | language | Title case. |
| P3 | Should fix | lines 207–213 | evidence | References not in house format. |
| D2 | Should fix | lines 16, 34, 85, 91, 99, 103 | consistency | Entries named but not linked. |
| C1 | Should fix | lines 26, 46, 80, 81 | language | VPN, URI, SVID, JWT not expanded. |
| A1 | Optional | line 210 | evidence | Hardy 1988: pages 36–38 confirmed from the article PDF; volume and issue (22(4)) not confirmed from a primary source. Flag for the fact-checker. |
| C2 | Optional | lines 18, 46, 99, 85 | language | Long sentences; "organisation". |

### D1. Ending
- **Correction:** Remove §8 as a section; end §7 Summary with the entry-by-entry recap (linked), a paragraph that names the series objectives and where they were met, and the closing lessons; keep `### References` under §7. No link in `src/` points to `#8-the-series-in-one-picture`.

## Revision log (wave 1)
- Structure (D1): "## 8. The Series in One Picture" removed as a section; its entry-by-entry recap (now linked) and closing lessons end §7 Summary, with a new paragraph that checks each of the six series objectives against the entries that meet it; `### References` now sits under §7. No link in `src/` targeted `#8-the-series-in-one-picture`.
- Prose: opening's 46-word sentence split; §2.1 SPIFFE ID sentence split; §3.2 first sentence restructured.
- Terminology/style: six H2 headings in sentence case; VPN, URI, JWT, NIST, PKCE expanded; SVID glossed ("SPIFFE Verifiable Identity Document"); "organisation" → "organization".
- Metadata: description 157 characters.
- References: house format, alphabetical, one entry per work: RFC 8705, 7523, 8693 (rfc-editor.org); NIST SP 800-207 (Rose, Borchert, Mitchell, Connelly, August 2020, csrc.nist.gov); Hardy with pages 36–38 (from the article PDF); the three SPIFFE standards by their document titles (github.com/spiffe/spiffe, fetched; the documents carry no date, so "consulted October 2026"); Transaction Tokens draft -11 (datatracker, 30 July 2026).
- Cross-references: links to the first entry (opening, §1.2, §3.2), the sixth entry (opening, §3.1 → its §2), the fifth entry §5, the fourth entry, the series page, and every entry in the closing recap.
- Remaining suggestions and why they stay: "SVID" is glossed in words rather than in the "Expansion (ABBR)" form; ACM, SIGOPS and SP occur only in reference entries; line 30 (46 words) is a definition that reads clearly.
- Flags for independent review: (fact-check) Hardy's volume and issue (22(4)) not confirmed from a primary source and therefore omitted (A1); (series) the new objectives paragraph in the Summary maps objectives to entries and should be checked against the revised overview.
- Vietnamese translation affected: yes. §8 merged into §7 (the Vietnamese file still has a separate section), a new paragraph on the objectives, and the References list.
