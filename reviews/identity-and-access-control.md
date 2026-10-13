# Series review: Identity and Access Control

- Series: `identity-and-access-control` (7 articles, status published, 0 planned entries)
- Reviewed commit: 6e6f2ee
- Date: 2026-10-13
- Review: second pass, with the "Concept introduction" and "Stated versions and defaults" dimensions added to the review procedure after the first pass. The first pass (commit 841f4e6) found 11 findings, all of which were applied in commit 17cc179.

## Summary

The corrections from the first pass hold: the technical content is accurate, cross-references resolve, every objective is met, and every recomputed value is consistent. The stricter procedure, however, shows that the series does not fully keep its promise to work "from the top down". The first entry never says what HTTP is, although every entry's examples are HTTP messages and its §3.1 begins with HTTP's mechanics. That is the one blocking finding.

The same pattern recurs at smaller scale:
- TLS, X.509 certificates, cookies, XSS, CSRF, origins, CORS, cryptographic hashes, HMAC, JSON and base64url are used before, or without, being introduced.
- The standards bodies and document series the series cites throughout (RFC, IETF, W3C, NIST, OWASP, XACML) are never explained.
- Eighteen HTTP messages across four entries use HTTP/1.1 text syntax without saying so.
- Four citations omit a version or revision that matters: RFC 6265 for `SameSite`, the NIST SP 800-63B revision, the WebAuthn level, and the RBAC standard revision.

None of these makes a statement wrong, and all are fixable with short additions. The series should be considered final once F1 is fixed, and ideally the should-fix items too.

Findings: 1 blocking, 12 should fix, 1 optional.

## Objectives coverage

| Objective (from the series file) | Covered by | Assessment |
|---|---|---|
| Separate identification, authentication, authorization and audit, and say which mechanism answers which question. | Entry 1 §1.2 (four stages, "Accountability (audit)"), §11; entry 7 §8 | Met. |
| Compare server-side sessions with self-contained tokens in terms of where state lives, how revocation works and what a verifier needs. | Entry 1 §3.3–3.5, §7.1; entry 3 §1.1–1.3, §7.3 | Met. The comparison rests on HTTP's statelessness, which is not explained (F1). |
| Explain delegated authorization with OAuth 2.0 and federated authentication with OpenID Connect, including why public clients need PKCE. | Entry 1 §5; entry 5 (including §3.4 on ID token validation) | Met. |
| Validate an access token correctly and enforce object-level authorization at the resource server. | Entry 1 §6.5, §9; entry 4 §6.1–6.2; entry 6 §3.4 | Met. |

## Findings

| ID | Severity | Article | Location | Dimension | Finding |
|---|---|---|---|---|---|
| F1 | Blocking | `src/content/blog/token-based-authentication.mdx` | §3.1 (lines 110–112) | Concept introduction | HTTP, the protocol underneath every entry, is never introduced; §3.1 opens with its mechanics |
| F2 | Should fix | Entries 1, 3, 5, 6 | 18 HTTP examples (first at entry 1 line 115) | Stated versions and defaults | All HTTP examples use HTTP/1.1 text syntax without saying so or noting that HTTP/2 and HTTP/3 carry the same semantics |
| F3 | Should fix | `src/content/blog/token-based-authentication.mdx` | §2.2 (line 100), §3.2 (line 124), §3.3 (line 138) | Concept introduction | TLS, HTTPS and X.509 certificates are used (first in §2.2) but never introduced |
| F4 | Should fix | `src/content/blog/token-based-authentication.mdx` | §3.3 (lines 128, 138) | Concept introduction | Cookie, cross-site scripting and cross-site request forgery are used in entry 1; they are introduced only in entry 3 |
| F5 | Should fix | Entries 1 and 2 | Entry 1 lines 279, 370; entry 2 lines 56, 62, 105 | Concept introduction | Cryptographic hash, HMAC and KDF are relied on but never introduced; "KDF" is never expanded |
| F6 | Should fix | Entries 1 and 2 | Entry 1 line 92; entry 2 lines 146, 190 | Concept introduction | "Origin", central to the phishing-resistance argument, is defined only in entry 3 |
| F7 | Should fix | Entries 1 and 2 | Entry 1 lines 124, 197, 199; entry 2 lines 86, 143 | Concept introduction / Terminology | RFC, IETF, W3C, NIST, OWASP and XACML are used without being expanded or explained |
| F8 | Should fix | `src/content/blog/sessions-and-cookies.mdx` | §5.3 (lines 182–183) | Concept introduction | CORS and "preflight" are used without being introduced (entry 1 line 531 also uses CORS unexpanded) |
| F9 | Should fix | `src/content/blog/token-based-authentication.mdx` | §6.3 (line 323) | Concept introduction | JSON and base64url, the building blocks of a JWT, are not introduced |
| F10 | Should fix | `src/content/blog/token-based-authentication.mdx` | Specifications (line 555) | Stated versions and defaults | RFC 6265 is cited for cookies, but the `SameSite` attribute the entry relies on is defined only in its revision |
| F11 | Should fix | `src/content/blog/authenticators-passwords-otp-passkeys.mdx` | §2.3 (line 86), §3.4 (line 131), specifications (line 259) | Stated versions and defaults | NIST SP 800-63B is cited without its revision, although its guidance has changed between revisions |
| F12 | Should fix | `src/content/blog/authenticators-passwords-otp-passkeys.mdx` | §5.6 (line 206), specifications (line 258) | Stated versions and defaults | WebAuthn is cited without a level, while the backup flags it describes come from WebAuthn Level 3 |
| F13 | Should fix | `src/content/blog/authorization-models.mdx` | §2.1 (line 60), references (line 249) | Stated versions and defaults | The RBAC standard is cited as ANSI INCITS 359-2004 without its 2012 revision |
| F14 | Optional | `src/content/blog/oauth-grants-and-client-types.mdx` | §3.3 (line 121) | Concept introduction | Percent-encoded parameter values (`https%3A%2F%2F…`) appear without explanation |

### F1. HTTP is never introduced
- **Where:** `src/content/blog/token-based-authentication.mdx:110-112`, section "3.1 HTTP is stateless"
- **Text:** "### 3.1 HTTP is stateless" / "HTTP treats each request independently: nothing in the protocol links a request to the one before it. A request consists of a method, a target, header fields and an optional body:"
- **Problem:** Every entry in the series shows HTTP messages, and the session/token comparison (objective 2) rests on HTTP being stateless. The entry promises to work "from the general to the specific" (line 21), and the series introduction promises "the whole picture from the top down". Yet HTTP is first named in passing (line 73, "An HTTP API") and §3.1 starts with a property and the message structure of a protocol the reader has not been told about. What HTTP is (an application-level request–response protocol between a client and a server), what its messages are for, and where its meaning is defined are all missing. Under the procedure this is blocking: a foundational concept missing in a series that promises a top-down treatment.
- **Recommended correction:** Replace the heading and the first paragraph of §3.1 (lines 110–112) with:

  ```markdown
  ### 3.1 HTTP, the protocol underneath

  Almost every exchange in this series travels over **HTTP**, the Hypertext Transfer Protocol. HTTP is an application-level request–response protocol: a **client** (a browser, an app, another service) sends a **request** to a **server**, and the server returns one **response**. A request names a **method**, which says what to do (`GET` to read, `POST` to submit, `DELETE` to remove, and others); a **target**, which says what to do it to (such as `/orders/123`); **header fields**, which carry metadata such as `Host`, `Accept` or `Authorization`; and an optional **body**. A response carries a three-digit **status code** (`200` for success, or `401` and `403` for the failures discussed in Section 4.4), header fields and usually a body. The meaning of all these parts is defined once, independently of how they are transmitted, in *HTTP Semantics* (RFC 9110).

  HTTP is **stateless**: each request is complete in itself, and nothing in the protocol links a request to the one before it. A server that has just answered a request from a user does not, from HTTP alone, know that the next request comes from the same user. A request looks like this:
  ```

  The example and the paragraph that follows ("Any notion of …") stay as they are. Update the summary table's "Transport" row only if F3 is applied.

### F2. HTTP/1.1 syntax is assumed but never stated
- **Where:** `src/content/blog/token-based-authentication.mdx:115` (first of 18 messages). The others are at entry 1 lines 131, 145, 209; `sessions-and-cookies.mdx` lines 54, 60, 217; `oauth-grants-and-client-types.mdx` lines 117, 124, 131, 145, 188, 238; `sender-constrained-tokens.mdx` lines 157, 169, 188, 207, 220.
- **Text:** "GET /orders/123 HTTP/1.1"
- **Problem:** Every HTTP example uses the HTTP/1.1 text format, and no entry says so or mentions HTTP/2 or HTTP/3 (a search of the seven articles finds none). A reader could conclude that the series describes HTTP/1.1 specifically, or that header-based mechanisms such as `Authorization`, cookies and `DPoP` work differently in later versions. They do not: HTTP/2 and HTTP/3 carry the same semantics (RFC 9110) in a binary framing, over TCP and QUIC respectively.
- **Recommended correction:** In entry 1, after the example in §3.1 (after line 118, before "Any notion of …"), add:

  > This example, like the other HTTP messages in this series, is written in the text format of HTTP/1.1, which is the easiest to read. HTTP/2 and HTTP/3 carry exactly the same methods, header fields, status codes and bodies in a binary framing (over TCP and over QUIC respectively), so nothing in this series depends on which version is in use.

  In entries 3, 5 and 6, add "(in HTTP/1.1 syntax, as throughout the series)" to the sentence that introduces each article's first HTTP example: entry 3 line 51, entry 5 line 108, entry 6 line 154.

### F3. TLS, HTTPS and X.509 certificates are never introduced
- **Where:** `src/content/blog/token-based-authentication.mdx:100` (first use), `:124`, `:138`, section "2.2 Users and workloads" and "3.2–3.3"
- **Text:** "**mutual TLS**, in which the workload presents an X.509 certificate during the TLS handshake."; "the password is effectively sent in clear text inside the TLS connection"; "`Secure` restricts the cookie to HTTPS"
- **Problem:** TLS is the series' transport layer (the summary table, line 539, lists it as the first layer). Entry 6 builds on client certificates in TLS, and entry 7 on mutual TLS between services. Yet no entry says what TLS does, what HTTPS is, or what a certificate is. §2.2 also uses "mutual TLS" before TLS has been mentioned at all.
- **Recommended correction:** After the HTTP/1.1 paragraph added by F2 (or after line 118 if F2 is not applied), add:

  > In practice HTTP runs inside **TLS** (Transport Layer Security), which encrypts the connection and lets the client verify the server's identity using an **X.509 certificate**: a statement, signed by a certificate authority that the client trusts, binding the server's name to its public key. HTTP over TLS is **HTTPS**. TLS protects messages in transit; it says nothing about who the user is, which is the problem the rest of this section addresses.

  In §2.2, line 100, replace the bullet with: "**mutual TLS**, in which the workload also presents an X.509 certificate during the TLS handshake (TLS and certificates are introduced in Section 3.1)."

### F4. Cookie, XSS and CSRF are used before they are introduced
- **Where:** `src/content/blog/token-based-authentication.mdx:128` and `:138`, section "3.3 Strategy two: a reference to server-side state"
- **Text:** "The client receives only a long, unpredictable **session identifier**, usually in a cookie:"; "so a cross-site scripting bug cannot read it directly; `SameSite` … reduces (but does not on its own eliminate) cross-site request forgery."
- **Problem:** Entry 3 introduces cookies (§2.1), CSRF (§5.1) and XSS (§6) properly. Entry 1 uses all three earlier, with no gloss or forward reference, at the point where it argues about their security.
- **Recommended correction:**
  - Line 128: "…**session identifier**, usually in a cookie (a small named value that the server asks the browser to store and to send back with later requests to the same site):"
  - Line 138: "`HttpOnly` hides it from page scripts, so a cross-site scripting (XSS) bug, in which an attacker's script runs inside the application's pages, cannot read it directly; `SameSite` limits when the browser attaches it to requests initiated by other sites, which reduces (but does not on its own eliminate) cross-site request forgery (CSRF), in which another site makes the browser send a request that carries the user's cookie. The third entry treats both attacks in detail."

### F5. Cryptographic hash, HMAC and KDF are not introduced
- **Where:** `src/content/blog/token-based-authentication.mdx:279` ("`code_challenge` is a hash") and `:370` ("HS256 (HMAC with SHA-256)"); `src/content/blog/authenticators-passwords-otp-passkeys.mdx:56`, `:62`, `:105`
- **Text:** "Storing a fast hash such as SHA-256 is barely better"; "record = (salt, parameters, KDF(password, salt, parameters))"; "Because HMAC is a pseudorandom function"
- **Problem:** Hash functions underpin password storage, PKCE, DPoP's `ath` and `jkt`, and certificate thumbprints. HMAC underpins HOTP/TOTP and HS256. Neither is ever said to be what it is. "KDF" appears in pseudocode and is never expanded, while the prose calls the same thing a "password hashing function".
- **Recommended correction:**
  - Entry 2, before line 56 (start of §2.1), add: "A **cryptographic hash function** such as SHA-256 maps any input to a short, fixed-size digest; computing it is fast, but recovering the input from the digest, or finding two inputs with the same digest, is infeasible."
  - Entry 2, line 58: "A verifier should instead store the output of a **password hashing function** (also called a key derivation function, KDF), designed to be slow and, ideally, memory-hard:".
  - Entry 2, line 108: "Because HMAC (a hash computed over the message together with the secret key, so that only holders of the key can produce it) is a pseudorandom function, …".
  - Entry 1, line 370: "With a **symmetric** algorithm such as HS256 (HMAC with SHA-256: a hash keyed with the shared secret), the same secret both signs and verifies."

### F6. "Origin" is used two entries before it is defined
- **Where:** `src/content/blog/token-based-authentication.mdx:92`; `src/content/blog/authenticators-passwords-otp-passkeys.mdx:146` and `:190`
- **Text:** "An authenticator based on public-key cryptography and bound to the website's origin"; "the browser includes the origin of the page that made the request in the data that is signed"; "a page may only use a relying party ID equal to, or a registrable suffix of, its own domain"
- **Problem:** Origin binding is the core of entry 2's phishing-resistance argument (§5.1, §5.4), but "origin" and "registrable domain" are defined only in entry 3 §3.1.
- **Recommended correction:**
  - Entry 2, line 146: "When signing, the browser includes the **origin** of the page that made the request (its scheme, host and port, such as `https://example.com`; the third entry defines origins and sites precisely) in the data that is signed."
  - Entry 1, line 92: "…bound to the website's origin (its scheme, host and port)…".

### F7. Standards bodies and document series are never explained
- **Where:** `src/content/blog/token-based-authentication.mdx:124` (first "RFC"), `:197` (XACML), `:199` (OWASP); `src/content/blog/authenticators-passwords-otp-passkeys.mdx:86` (NIST), `:143` (W3C); "IETF" first at `oauth-grants-and-client-types.mdx:79`
- **Text:** "HTTP Basic authentication (RFC 7617)"; "Standards such as XACML"; "the OWASP API Security Top 10 (2023 edition)"; "NIST's digital identity guidelines"; "a W3C standard"
- **Problem:** The series cites about forty RFCs and leans on documents from NIST, W3C, OWASP and OASIS. It never says what an RFC is, or who these organisations are. A reader new to the field cannot tell a binding Internet standard from an advisory list.
- **Recommended correction:**
  - Entry 1, at the end of the introduction (line 21), add: "Most of these mechanisms are Internet standards, published by the Internet Engineering Task Force (IETF) as numbered *Requests for Comments* (RFCs); browser behaviour is standardised by the World Wide Web Consortium (W3C) and the WHATWG. Each standard is cited by number where it first matters."
  - Line 197: "Standards such as XACML (the eXtensible Access Control Markup Language, from the OASIS standards consortium) separate…".
  - Line 199: "…in the API Security Top 10 (2023 edition) of OWASP, the Open Worldwide Application Security Project:".
  - Entry 2, line 86: "The digital identity guidelines of the US National Institute of Standards and Technology (NIST SP 800-63B) reversed…" (combine with F11).

### F8. CORS and "preflight" are not introduced
- **Where:** `src/content/blog/sessions-and-cookies.mdx:182-183`, section "5.3 Request-level defences"; also `src/content/blog/token-based-authentication.mdx:531`
- **Text:** "on cross-origin requests made with CORS"; "cannot add a custom header such as `X-Requested-With` to a cross-origin request without a CORS preflight that the server refuses"
- **Problem:** The custom-header defence depends entirely on how CORS preflight works, but neither the acronym nor the mechanism is explained anywhere in the series. Entry 1 only says what CORS is not.
- **Recommended correction:** In entry 3, replace the first sentence of the "Custom request headers for APIs" bullet (line 183) with: "Browsers enforce **Cross-Origin Resource Sharing** (CORS): before sending a cross-origin request that a plain HTML form could not produce, such as one with a custom header or a JSON body, the browser first asks the server for permission with a *preflight* `OPTIONS` request, and sends the real request only if the server allows that origin. A cross-site page can therefore send a simple form `POST`, but cannot add a custom header such as `X-Requested-With` unless the server's CORS policy admits it." In entry 1, line 531, write "**CORS (Cross-Origin Resource Sharing) is not access control**".

### F9. JSON and base64url are not introduced
- **Where:** `src/content/blog/token-based-authentication.mdx:323`, section "6.3 The structure of a JSON Web Token"
- **Text:** "A JSON Web Token (RFC 7519) is a set of claims encoded as JSON. In its common signed form (JSON Web Signature, RFC 7515) it has three base64url-encoded parts separated by dots:"
- **Problem:** The section defines a JWT in terms of two formats the reader is not told about. Base64 is mentioned once (line 124) only as "an encoding", and base64url's difference from it is never stated.
- **Recommended correction:** "A JSON Web Token (RFC 7519) is a set of claims written in JSON (JavaScript Object Notation, a text format of named values, arrays and nested objects). In its common signed form (JSON Web Signature, RFC 7515) it has three parts separated by dots, each encoded in base64url (base64 with the URL-safe characters `-` and `_` and no padding, so that a token can travel in URLs and headers unchanged):".

### F10. RFC 6265 is cited for an attribute it does not define
- **Where:** `src/content/blog/token-based-authentication.mdx:555`, section "The specifications"
- **Text:** "Cookies: RFC 6265."
- **Problem:** Entry 1 relies on `SameSite` (lines 133, 138, 470, 526), which is not in RFC 6265; it is specified in the revision in progress at the IETF. Entry 3 (line 270) states this correctly, so the two entries disagree on the source of the same feature.
- **Recommended correction:** "Cookies: RFC 6265 and its revision in progress at the IETF, which specifies `SameSite`."

### F11. NIST SP 800-63B is cited without its revision
- **Where:** `src/content/blog/authenticators-passwords-otp-passkeys.mdx:86`, `:131`, `:259`
- **Text:** "NIST's digital identity guidelines (SP 800-63B) reversed much traditional advice"; "NIST's guidelines classify authentication over the public telephone network as *restricted*"; "Guidance: NIST Special Publication 800-63B, *Digital Identity Guidelines: Authentication and Lifecycle Management*."
- **Problem:** SP 800-63B has been revised. The reversal of composition rules and forced changes, and the "restricted" category for telephone-network authenticators, were introduced in revision 3 (2017). The text cites no revision, so a reader cannot tell which version's requirements are being described.
- **Recommended correction:** Line 86: "The digital identity guidelines of the US National Institute of Standards and Technology (NIST SP 800-63B, from its 2017 revision onwards) reversed…". Line 131: "NIST's guidelines (in the 2017 revision of SP 800-63B) classify…". Line 259: "…*Digital Identity Guidelines: Authentication and Lifecycle Management* (revision 3, 2017, and later revisions)."

### F12. WebAuthn is cited without a level
- **Where:** `src/content/blog/authenticators-passwords-otp-passkeys.mdx:206` and `:258`
- **Text:** "The authenticator data carries *backup eligible* and *backed up* flags so that the server can tell which kind it has."; "W3C Web Authentication (WebAuthn)"
- **Problem:** WebAuthn has several published levels. The backup-eligibility and backup-state flags that §5.6 relies on were added in Level 3, so a reader implementing against an earlier level will not find them.
- **Recommended correction:** Line 206: "WebAuthn Level 3 adds *backup eligible* and *backed up* flags to the authenticator data, so that the server can tell which kind it has." Line 258: "W3C Web Authentication (WebAuthn), Level 3 for the backup flags; FIDO Alliance Client to Authenticator Protocol (CTAP)."

### F13. The RBAC standard is cited without its revision
- **Where:** `src/content/blog/authorization-models.mdx:60` and `:249`
- **Text:** "and standardised as ANSI INCITS 359-2004"; "ANSI INCITS 359-2004, *Role Based Access Control*."
- **Problem:** The standard was revised in 2012 (INCITS 359-2012). Citing only the 2004 edition presents a superseded version as the current one.
- **Recommended correction:** Line 60: "and standardised as ANSI INCITS 359 (first published in 2004, revised in 2012)". Line 249: "ANSI INCITS 359, *Role Based Access Control* (2004; revised 2012)."

### F14. Percent-encoding is not explained
- **Where:** `src/content/blog/oauth-grants-and-client-types.mdx:121`, section "3.3 The messages"
- **Text:** "The line breaks are for readability; the request is a single URL."
- **Problem:** The examples contain values such as `https%3A%2F%2Fprint.example%2Fcallback` with no explanation, which may puzzle readers who have not met URL encoding.
- **Recommended correction:** "The line breaks are for readability; the request is a single URL. Parameter values are percent-encoded, so that characters with a special meaning in URLs survive: `https://` appears as `https%3A%2F%2F`."

## Concept introduction map

| Concept | First used (path:line) | Introduced where | Assessment |
|---|---|---|---|
| HTTP (request–response protocol) | `token-based-authentication.mdx:73` | Not introduced | F1 (blocking) |
| HTTP status codes 401/403/404 | `token-based-authentication.mdx:203` | Same place, §4.4 | Introduced |
| TLS / HTTPS | `token-based-authentication.mdx:100` | Not introduced | F3 |
| X.509 certificate | `token-based-authentication.mdx:100` | Not introduced (entry 6 §2.1 explains client certificates in TLS) | F3 |
| Cookie | `token-based-authentication.mdx:128` | `sessions-and-cookies.mdx:51` (entry 3 §2.1) | Used two entries early; F4 |
| Cross-site scripting (XSS) | `token-based-authentication.mdx:138` | `sessions-and-cookies.mdx:193` | Used early; F4 |
| Cross-site request forgery (CSRF) | `token-based-authentication.mdx:138` | `sessions-and-cookies.mdx:149` | Used early; F4 |
| Origin, site, registrable domain | `token-based-authentication.mdx:92` | `sessions-and-cookies.mdx:99-100` | Used early; F6 |
| Same-origin policy | `sessions-and-cookies.mdx:89` | `sessions-and-cookies.mdx:99` | Introduced (ten lines later, acceptable) |
| CORS, preflight | `token-based-authentication.mdx:531` | Not introduced | F8 |
| Cryptographic hash | `token-based-authentication.mdx:279` | Not introduced | F5 |
| HMAC | `token-based-authentication.mdx:370` | Not introduced | F5 |
| KDF / password hashing function | `authenticators-passwords-otp-passkeys.mdx:58` | Partly (the property is described, the abbreviation is never expanded) | F5 |
| Public-key cryptography, signature | `token-based-authentication.mdx:92` | `authenticators-passwords-otp-passkeys.mdx:28`; entry 1 §6.4 | Introduced (briefly, adequately) |
| JSON | `token-based-authentication.mdx:142` | Not introduced | F9 |
| Base64 / base64url | `token-based-authentication.mdx:124` | Base64 named as an encoding; base64url not introduced | F9 |
| JWT, JWS, JWE, JWK | `token-based-authentication.mdx:142` | `token-based-authentication.mdx:323-372` | Introduced |
| OAuth 2.0, OpenID Connect, PKCE | `token-based-authentication.mdx:21` | Entry 1 §5 | Introduced |
| RFC, IETF | `token-based-authentication.mdx:124` | Not introduced | F7 |
| W3C, WHATWG, NIST, OWASP, OASIS/XACML | `token-based-authentication.mdx:197` onwards | Not introduced | F7 |
| URL percent-encoding | `oauth-grants-and-client-types.mdx:113` | Not introduced | F14 (optional) |
| Reference monitor, complete mediation | `token-based-authentication.mdx:29` | Same place | Introduced |
| SPIFFE, service mesh, attestation | `service-to-service-authentication.mdx:43` | Same places, §2.1–3.1 | Introduced |
| DNS, URL, IP address, container | Various | Not introduced | Acceptable: general computing background outside the series' subject |

## Versions, defaults and conventions

| Assumption | Where it appears | Stated in the text? | Assessment |
|---|---|---|---|
| HTTP version of the examples (HTTP/1.1 text syntax) | 18 messages in entries 1, 3, 5, 6 | No | F2 |
| HTTP semantics source (RFC 9110) | Entry 1 §4.4, specifications | Yes | Correct, current |
| TLS version | Entries 1, 6, 7 | No | Not material: nothing described depends on TLS 1.2 vs 1.3 |
| OAuth version | Throughout | Yes (OAuth 2.0; OAuth 2.1 noted as in progress in entry 5 §6) | Good |
| OpenID Connect version | Entry 5 specifications | Yes (Core 1.0) | Good |
| Cookie specification | Entry 1 line 555; entry 3 line 270 | Entry 3 yes; entry 1 cites only RFC 6265 | F10 |
| `SameSite` default when absent | Entry 3 line 116 | Yes (stated to vary by browser) | Good |
| NIST SP 800-63B revision | Entry 2 lines 86, 131, 259 | No | F11 |
| WebAuthn level / CTAP version | Entry 2 §5 | No level; FIDO2 named | F12 |
| OWASP API Security Top 10 edition | Entry 1 line 199 | Yes (2023) | Good |
| RBAC standard edition | Entry 4 lines 60, 249 | 2004 only | F13 |
| NIST SP 800-162, SP 800-207 | Entries 4, 7 | Yes (2014, 2020) | Good |
| XACML version | Entries 1, 4 | No | Not material: the combining algorithms cited exist in both 2.0 and 3.0 |
| TOTP defaults (HMAC-SHA-1, 6 digits, 30 s) | Entry 2 §3.1–3.2 | Yes | Good |
| Time units for `iat`/`exp` | Entry 1 line 350 | Yes (Unix timestamps, seconds) | Good |
| Example values (keys, tokens, hashes) | Entries 1, 5, 6 | Yes (illustrative, or RFC 9449 samples) | Good |

## Series-level notes

**Previous findings.** All 11 findings from the first pass were applied and remain fixed:
- the staleness wording, OTP odds, `Origin`/`Sec-Fetch-Site` conditions, question order and "checkout";
- entry 5 §3.4 (ID token validation);
- the "authorize" spelling, "entry" wording, `at+jwt` example headers, the session-ID logging rule and "Accountability (audit)".

**Cross-references.** Unchanged from the first pass and all valid, including the new link from entry 5 §3.4 to "Section 5.5 of the first entry".

**Pattern behind this pass's findings.** The series introduces the concepts that are its subject (access control, tokens, OAuth, OIDC) carefully. It does not introduce the web and cryptographic infrastructure they run on: HTTP, TLS, cookies, origins, hashes, JSON. Entry 1 is the natural home for brief introductions of all of these, because it is read first and every later entry builds on it. F1, F3, F4, F5, F6 and F9 together add roughly a page to entry 1 and a few sentences to entry 2.

**Structure and tone.** These are unchanged and consistent: numbered sections, a summary table and a specifications/references list in every entry.

## Verification log

- `npm run build:local`: passed. `astro check` reported 0 errors and 0 warnings, the build completed, and Pagefind indexed 26 pages. The expected localhost warning appeared because `SITE_URL` was not set.
- `npm run check:links`: passed. It checked 76 pages and 1772 internal references; all resolve.
- Mermaid widths in `dist/blog/*.html`, all under 600px: entry 1: 357, 426, 340, 431px; entry 2: 344px; entry 3: 331, 336px; entry 4: 441, 350px; entry 5: 344, 469px; entry 6: 331px; entry 7: 428, 126px.
- Text glued to inline elements: none found in the seven pages.
- Recomputed:
  - PKCE S256 challenge (entry 5): matches.
  - Basic credentials (entry 5): match.
  - DPoP `ath` and `jkt` (entry 6): match.
  - Example token headers in entry 1 line 147 and entry 5 line 243 both decode to `{"alg":"RS256","typ":"at+jwt"}`.
  - HOTP truncation reproduces RFC 4226 Appendix D (755224, 287082, 359152).
  - TOTP reproduces the RFC 6238 SHA-1 vector for T = 59 (94287082).
  - OTP guessing odds with a ±1 step window: 3 valid codes × 5 guesses = 15 in 10⁶ per step, matching entry 2 line 122.
- Searches:
  - `HTTP/1.1` appears 18 times across entries 1, 3, 5 and 6;
  - `HTTP/2`, `HTTP/3` or "version of HTTP" appear nowhere (basis of F2);
  - first uses of TLS, RFC, IETF, W3C, NIST, OWASP and XACML as listed in the concept map.
- Not verified:
  - The revision history behind F11 (that the cited NIST guidance dates from the 2017 revision) and F13 (the 2012 revision of INCITS 359), and that the WebAuthn backup flags (F12) were added in Level 3. These were checked against the reviewer's knowledge of those documents, not re-read from the sources in this run.
  - Whether later NIST revisions keep the "restricted" classification of telephone-network authenticators. The recommended wording for F11 therefore attributes it to the 2017 revision only.
