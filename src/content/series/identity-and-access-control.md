---
# Authoring note: when a planned entry is written, publish it as an article in
# src/content/blog (with `series` and `seriesOrder`) and remove it from plannedEntries.
# Remove it from the Vietnamese translation (src/content/series/vi/identity-and-access-control.md) as well.
title: "Identity and Access Control"
description: "Learn how networked systems establish who is making a request and decide what it may do, from the access-control model to tokens and calls between services."
category: "Computing Systems"
status: "published"
objectives:
  - "Separate identification, authentication, authorization and audit, and say which mechanism answers which question."
  - "Evaluate authenticators by their resistance to online guessing, verifier compromise, replay and phishing, and explain why origin-bound public-key credentials resist phishing."
  - "Compare server-side sessions with self-contained tokens in terms of where state lives, how revocation works and what a verifier needs."
  - "Explain delegated authorization with OAuth 2.0 and federated authentication with OpenID Connect, including why public clients need PKCE."
  - "Validate an access token correctly and enforce object-level authorization at the resource server."
  - "Design authentication between services with workload identities, sender-constrained tokens and per-hop token exchange instead of network location, forwarded tokens or trusted headers."
---

This series is written for readers who build or review networked software, such as a web application, an HTTP API or a set of back-end services, and want a model of access control that does not depend on a particular framework or vendor. It assumes that the reader has written or read code that sends and handles web requests, and knows what a digital signature and a hash function guarantee, without their mathematics. Everything else the series needs, from HTTP and TLS to cookies and JSON Web Tokens, is introduced where it is first used.

The order follows a request through a system. The first entry gives the whole picture from the top down: the reference monitor that must see every request, the two questions every request raises (*who is asking?* and *may they do this?*), and the tokens that carry the answers between services. The next two entries answer the first question in depth. The second compares the authenticators with which a user proves an identity, from passwords to passkeys, and the third shows how a web session carries that proof from request to request and which attacks target it. The fourth entry turns to the second question and compares the models in which authorization policy is written. The fifth returns to OAuth 2.0 and examines how each kind of client obtains its tokens. The sixth binds those tokens to keys so that a stolen copy is useless, and the seventh applies the same principles inside the system, where services call services on a user's behalf.

All entries share a few conventions. HTTP messages are written in the text syntax of HTTP/1.1, and nothing in the series depends on the HTTP version. Tokens, keys, identifiers and timestamps in the examples are illustrative values, internally consistent where an entry says so. Pseudocode is language-neutral. Standards are cited by their RFC or specification number in the text and listed in full in each entry's references.
