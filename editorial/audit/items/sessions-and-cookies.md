<!-- audit: {"slug":"sessions-and-cookies","type":"article","series":"identity-and-access-control","priority":"P2","before":{"purpose":3,"structure":3,"accuracy":4,"evidence":2,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":6,"optional":2}} -->
# Audit: Sessions and Cookies in Depth

- Path: `src/content/blog/sessions-and-cookies.mdx` · Route: `/blog/sessions-and-cookies` · Type: article · Series `identity-and-access-control`, entry 3 of 7 · Words: 2915 (from `eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 3: clear purpose; the opening links neither the previous nor the first entry.
- structure 3: sound order; two sections share the heading "The attack" (4.1 and 5.1), so their anchors are ambiguous.
- accuracy 4: browser behavior stated is consistent with the Fetch Metadata Request Headers draft (W3C, September 2026: `Sec-Fetch-Site` values `cross-site`, `same-origin`, `same-site`, `none`) and the cookie revision draft (draft-ietf-httpbis-rfc6265bis-22, in the RFC Editor queue, so "revision in progress at the IETF" is still true).
- evidence 2: no References list; "### The specifications" names documents without authors or years.
- language 3: "very low cost" (182), "actually safe" (262); a 56-word sentence (114).
- consistency 3: CORS is used (182) one bullet before it is expanded (183); "the first entry" and "the previous entry" unlinked.
- publishing 2: description 260 characters; seven title-case H2 headings; duplicate H3.

## Accuracy check

Recomputed with python3: the cookie value `Vb9xQm4tR2kz8YpLw7nJcA` decodes to 16 bytes = 128 bits, consistent with the "128 random bits ... encoded in base64url" of §9.

## Priority

P2.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 260 characters. |
| P2 | Should fix | H2 headings | language | Title case (e.g. "Cookies: How the Identifier Travels", "Sites, Origins and When Cookies Are Sent", "Theft After Authentication"). |
| P3 | Should fix | lines 120, 147 | publishing | Duplicate heading "The attack". |
| P4 | Should fix | lines 268–273 | evidence | No References list in house format. |
| D1 | Should fix | lines 17, 28, 45, 227, 231 | consistency | References to the first and second entries unlinked. |
| C1 | Should fix | lines 181–183 | language | HMAC unexpanded; CORS used before its expansion in the next bullet. |
| C2 | Optional | lines 182, 262 | language | "very", "actually". |
| C3 | Optional | line 114 | language | 56-word sentence. |

### P1. Description
- **Correction:** "Learn how a web session keeps a user signed in: identifiers, cookie attributes and prefixes, sites and origins, fixation, CSRF, timeouts and logout." (one sentence, under 165 characters)

### P3. Duplicate heading
- **Correction:** "4.1 How fixation works" and "5.1 How the forgery works". No link in `src/` points to either anchor (grep).

### C1. CORS
- **Text (182):** "and on cross-origin requests made with CORS."
- **Correction:** Expand CORS here ("Cross-Origin Resource Sharing (CORS), defined in the next item") and keep the explanation in the next bullet.

## Revision log (wave 1)
- Structure: duplicate headings renamed: "4.1 How fixation works", "5.1 How the forgery works" (P3). Opening links the previous entry and states which cookie specification and browsers the behavior is described against.
- Prose: §1.3 trade-off sentence split; §3.2 "`Strict` ... `Lax` ..." sentences now name "the `Strict` mode"; "very low cost" → "little cost"; "safe methods that are actually safe" → "safe methods that change no state".
- Terminology/style: nine H2 headings in sentence case; HMAC expanded in §5.3; CORS expanded at its first use in §5.3 (third bullet) with a pointer to the next bullet, where it is defined.
- Metadata: description 151 characters.
- References: `### References` (8 entries): RFC 6265, RFC 9110, RFC 6797 (rfc-editor.org); draft-ietf-httpbis-rfc6265bis-22 (datatracker); Fetch Metadata Request Headers (W3C WD, 21 September 2026) and Clear Site Data (W3C WD, 30 November 2017), both edited by M. West (w3.org/TR); WHATWG Fetch Standard (living standard, last updated 6 October 2026); Public Suffix List (publicsuffix.org: "an initiative of Mozilla ... maintained as a community resource").
- Cross-references: links to the previous entry, the first entry §3.5 and §7.3, the sixth entry, and the next entry.
- Remaining warnings: none.
- Flags for independent review: none beyond the usual check of the browser-behavior statements in §3.2 and §5.3 against current browsers.
- Vietnamese translation affected: yes, in wording of headings 4.1 and 5.1, one added sentence in the opening, and the References list; no technical change.
