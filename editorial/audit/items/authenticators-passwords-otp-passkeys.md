<!-- audit: {"slug":"authenticators-passwords-otp-passkeys","type":"article","series":"identity-and-access-control","priority":"P2","before":{"purpose":3,"structure":3,"accuracy":3,"evidence":2,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":7,"optional":2}} -->
# Audit: Authenticators: Passwords, One-Time Codes and Passkeys

- Path: `src/content/blog/authenticators-passwords-otp-passkeys.mdx` · Route: `/blog/authenticators-passwords-otp-passkeys` · Type: article · Series `identity-and-access-control`, entry 2 of 7 · Words: 3139 (from `eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 3: the opening states the three questions; it does not link the first entry or say which standards versions it describes.
- structure 3: §2.1 opens with a detached definition of a hash function before saying what problem the section addresses (concept before mechanics, standards 6.1).
- accuracy 3: the NIST guidance is cited as SP 800-63B revision 3, which NIST withdrew on 1 August 2025 and replaced with SP 800-63B-4; the statements remain true under revision 4 (checked, below), but the citation points the reader to a withdrawn document.
- evidence 2: no References list; "### The specifications" gives RFC numbers and two titles without authors or years.
- language 3: a 91-word sentence (line 139) and a 58-word sentence (145); "simply" (124).
- consistency 3: the first entry and the third entry are named but not linked.
- publishing 2: description 204 characters; five title-case H2 headings.

## Accuracy check

Recomputed with python3: HOTP truncation as described reproduces the RFC 4226 test vector (key "12345678901234567890", counter 0 → 755224; counter 1 → 287082). The online-guessing figure "about $15/10^6$ per step" (line 124): exact probability for five guesses against three valid codes is $1-(1-3\cdot10^{-6})^5 = 1.49999\times10^{-5}$, so "about" is right. NIST SP 800-63B-4 (pages.nist.gov/800-63-4, fetched): "Verifiers and CSPs SHALL NOT impose other composition rules", "SHALL NOT require subscribers to change passwords periodically", blocklist comparison required, and "Use of the PSTN for out-of-band verification is *restricted*"; so §2.3 and §3.4 hold for the current revision. WebAuthn Level 3 is a W3C Recommendation (25 August 2026) and defines the backup eligibility and backup state flags (w3.org/TR/webauthn-3, fetched). CTAP: latest Proposed Standard 2.3 (26 February 2026, fidoalliance.org).

## Priority

P2: should-fix metadata, references and a stale citation; no technical error.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 204 characters. |
| P2 | Should fix | H2 headings | language | Title case ("A Framework for Comparing Authenticators", "One-Time Codes", "Out-of-Band Approval", "Comparing the Authenticators", "Recovery Is Part of Authentication"). |
| P3 | Should fix | lines 256–261 | evidence | No References list in house format. |
| A1 | Should fix | lines 88, 133, 261 | accuracy | SP 800-63B revision 3 is withdrawn; cite the current revision 4 as well. |
| D1 | Should fix | line 56 | structure | §2.1 begins with a definition before the problem. |
| D2 | Should fix | lines 17, 148, 254 | consistency | Other entries named but not linked; versions not stated in the opening. |
| C1 | Should fix | lines 27, 56, 60, 102, 110, 112, 120, 131, 133, 145 | language | Abbreviations not expanded at first use: PIN, SHA, KDF, HOTP, HMAC (expanded after use), TOTP, QR, SMS, SIM, FIDO. |
| C2 | Should fix | lines 139, 145 | language | Sentences of 91 and 58 words. |
| C3 | Optional | line 124 | language | "simply keep trying". |

### A1. Withdrawn NIST revision
- **Text:** "NIST SP 800-63B, from its 2017 revision onwards" (88); "in the 2017 revision of SP 800-63B" (133); "(revision 3, 2017, and later revisions)" (261)
- **Problem:** csrc.nist.gov marks SP 800-63B (revision 3) "Withdrawn on August 01, 2025", superseded by SP 800-63B-4, *Digital Identity Guidelines: Authentication and Authenticator Management* (July 2025; note the changed title).
- **Correction:** Name both revisions in the text ("introduced in its 2017 revision 3 and kept in the current revision 4 of 2025") and list both in References.

### D1. §2.1 order
- **Text:** "A **cryptographic hash function** such as SHA-256 maps any input to a short, fixed-size digest; ..." (first paragraph of §2.1)
- **Correction:** Start with the problem (a stored password table), then define the hash where the text first needs it.

### C2. Long sentences
- **Text (139):** "**Number matching**, in which the browser shows a short number that the user must enter or select in the app, ties the approval ... genuine site." (91 words across one sentence and its clauses)
- **Correction:** Split into what number matching is, what it stops, and what it does not prove.

## Revision log (wave 1)
- Structure: §2.1 now opens with the problem (a stored password table) and defines the cryptographic hash where it is needed (D1). HMAC is defined at its first use in §3.1 (before HOTP) instead of inside a later sentence. Opening links the first entry and a new paragraph states the versions the entry describes (RFCs, NIST SP 800-63B revisions 3 and 4, WebAuthn Level 3).
- Technical/factual update (A1): §2.3 now says the guidance was introduced in the 2017 revision and kept in revision 4 (2025); §3.4 says the PSTN "restricted" classification holds in both. Evidence: csrc.nist.gov marks SP 800-63B rev. 3 "Withdrawn on August 01, 2025", superseded by SP 800-63B-4 (July 2025); pages.nist.gov/800-63-4/sp800-63b.html: "SHALL NOT impose other composition rules", "SHALL NOT require subscribers to change passwords periodically", blocklist comparison required, "Use of the PSTN for out-of-band verification is *restricted*". "The guidelines recommend" → "call for".
- Prose: §4 number-matching passage split into three sentences; §5.1 WebAuthn/CTAP sentence split; Argon2 sentence split; "simply" removed.
- Terminology/style: five H2 headings in sentence case; expanded PIN, KDF (as "key derivation function (KDF)"), HMAC, HOTP, TOTP, QR, SMS, SIM, FIDO, NIST, SP; "US" → "United States".
- Metadata: description 152 characters.
- References: `### References` (9 entries, house format, alphabetical): RFC 9106, 7914, 8018, 4226, 6238 checked at rfc-editor.org; WebAuthn Level 3 (W3C Recommendation, 25 August 2026, w3.org/TR/webauthn-3); CTAP 2.3 Proposed Standard (26 February 2026, fidoalliance.org); NIST SP 800-63B rev. 3 (Grassi et al., June 2017, withdrawn 2025) and SP 800-63B-4 (Temoshok et al., July 2025), both from csrc.nist.gov.
- Cross-references: links to the first entry (opening), the third entry §3.1 (origins) and the next entry.
- Remaining suggestions and why they stay: HOTP, TOTP and SMS flagged at their headings (102, 112, 131); each is expanded in the first sentence below its heading. SHA-256 and FIDO2 are names (FIDO is expanded). PKCS is in a reference title. Sentences of 46–48 words at 19, 104, 203 read clearly and were left.
- Flags for independent review: (fact-check) "FIDO (Fast IDentity Online)" expansion from general knowledge, not from a fetched page; middle initial of Grassi omitted because the NIST page gives "Paul Grassi". (technical) none.
- Vietnamese translation affected: yes. New versions paragraph in the opening; §2.3 and §3.4 now name revision 4 of SP 800-63B; §2.1 and §3.1 reordered (hash and HMAC definitions moved); References list replaces "The specifications".

## Independent review (wave 2)

- Report: `reviews/identity-and-access-control.md`
- Fact-check: fail
- Technical: fail
- Findings: F2 (should fix), T1 (should fix), S1 (should fix, Vietnamese translation)
- Not verified: graphics-processor hash rate and phishing-kit availability (qualitative, unsourced); FIDO expansion confirmed only in press coverage.

## Revision log (wave 2 resolution)

- F2: revision 4 forbids email for out-of-band authentication, line 133; table row relabeled, line 225.
- T1: related-origins exception of WebAuthn Level 3, line 192.
- Meaning changes mirrored in Vietnamese: F2, T1, versions paragraph, SP 800-63B-4 wording in §2.3 and §3.4, References, description.
- Lint: `eos lint identity-and-access-control` 0 errors, 0 warnings (suggestions only, none on the changed lines). Syntax: `eos syntax` "All files compile"; Vietnamese MDX compiled with @mdx-js/mdx.
- Vietnamese translation: updated in this resolution (scope S1); copied front-matter fields unchanged.
