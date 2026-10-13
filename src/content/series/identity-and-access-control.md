---
# Authoring note: when a planned entry is written, publish it as an article in
# src/content/blog (with `series` and `seriesOrder`) and remove it from plannedEntries.
title: "Identity and Access Control"
description: "A series on how networked systems decide who is making a request and what that party may do, from the access-control model down to protocols and token formats."
category: "Computing Systems"
status: "in-progress"
objectives:
  - "Separate identification, authentication, authorization and audit, and say which mechanism answers which question."
  - "Compare server-side sessions with self-contained tokens in terms of where state lives, how revocation works and what a verifier needs."
  - "Explain delegated authorization with OAuth 2.0 and federated authentication with OpenID Connect, including why public clients need PKCE."
  - "Validate an access token correctly and enforce object-level authorization at the resource server."
plannedEntries:
  - title: "Authenticators: Passwords, One-Time Codes and Passkeys"
    description: "What each kind of authenticator proves, how it fails, and why origin-bound public-key credentials resist phishing where passwords and one-time codes do not."
  - title: "Sessions and Cookies in Depth"
    description: "Session identifiers, cookie attributes, fixation, CSRF and the browser's same-site rules, treated as one design problem."
  - title: "Authorization Models: RBAC, ABAC and Relationship-Based Access"
    description: "How each model represents policy, how decisions are evaluated, and how the choice affects auditing and change over time."
  - title: "OAuth 2.0 Grants and Client Types"
    description: "Authorization code with PKCE, client credentials, device authorization and token exchange, and the client properties that decide which grant applies."
  - title: "Sender-Constrained Tokens: DPoP and Mutual TLS"
    description: "Binding an access token to a key the client holds, so that a stolen token cannot be replayed by another party."
  - title: "Service-to-Service Authentication"
    description: "Workload identity, mutual TLS inside a service mesh, and propagating the end user's identity across internal calls."
---

This series is intended for readers who build or review networked software and want a model of access control that does not depend on a particular framework or vendor. The first entry gives the whole picture from the top down; each later entry takes one layer of that picture and goes further into it.
