---
# Authoring note: when a planned entry is written, publish it as an article in
# src/content/blog (with `series` and `seriesOrder`) and remove it from plannedEntries.
title: "Identity and Access Control"
description: "A series on how networked systems decide who is making a request and what that party may do, from the access-control model down to protocols and token formats."
category: "Computing Systems"
status: "published"
objectives:
  - "Separate identification, authentication, authorization and audit, and say which mechanism answers which question."
  - "Compare server-side sessions with self-contained tokens in terms of where state lives, how revocation works and what a verifier needs."
  - "Explain delegated authorization with OAuth 2.0 and federated authentication with OpenID Connect, including why public clients need PKCE."
  - "Validate an access token correctly and enforce object-level authorization at the resource server."
---

This series is intended for readers who build or review networked software and want a model of access control that does not depend on a particular framework or vendor. The first entry gives the whole picture from the top down; each later entry takes one layer of that picture and goes further into it.
