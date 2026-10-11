# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Current state

The repository currently contains only [idea-plan.md](idea-plan.md), the website specification for ACRR (Advanced Computing & Robotics Research). There is no source code, `package.json`, git history, or build tooling yet, so there are no build/lint/test commands to document. Do not invent them; once the project is scaffolded, add the real commands here (including how to run a single test, if tests are added).

`idea-plan.md` is the source of truth for scope and requirements. Read it before starting any implementation. Its own scope note says it is a specification, not confirmation that a build exists or has been tested.

## Planned architecture (from the spec)

- Static site, no backend or database, deployable immediately. Suggested stack: **Astro with Markdown/MDX content collections** (the spec calls this "a suitable implementation", not a hard requirement).
- Entire site is written in English.
- Six primary sections: Home, Blog, Series, Learning, Insights, About. The Blog archive and article pages must be generated from structured content files, not hand-maintained HTML per article.
- Content is kept separate from layout code, with validated frontmatter. Article schema: `title`, `description`, `publishedAt`, `category`, `tags[]`, `draft`. The `draft` flag must exclude unfinished content from published listings.
- Series are ordered collections of articles (series page plus ordered entries linking to articles).
- Learning is a resource index (title, description, topic, type, external URL, optional status such as planned / in progress / published), driven by config or content files so real Notion URLs can be added later without redesign.
- Planned implementation order: design system/layout/header/footer → Home, About, Learning → content collections + Blog → Series and Insights → SEO, sitemap, RSS, 404 → route/link/responsive/build testing → deployment and content docs.
- MVP also requires: basic SEO metadata, a 404 page, responsive layouts, and a README (install, local dev, content authoring, build). RSS, sitemap, search/filtering, reading time, dark mode are optional enhancements and must not delay the first release.

## Content-integrity rules (easy to violate, strictly required)

- Never fabricate: founder biography, credentials, affiliations, publications, collaborators, contact details, statistics, readership/citation figures, research results, or external URLs. Missing data stays missing.
- No Notion URLs exist yet. Learning entries without a real link should be shown as "Coming soon" or omitted, never given a made-up URL.
- Sample/demo articles and illustrative series must be clearly labelled as examples, drafts, or planned, not presented as completed original research.
- Research areas on the Home and About pages are proposed interests, not claims of active projects or a staffed lab. Do not overstate ACRR's size or achievements.
- Insights entries should separate established facts, interpretations, and open questions.

## Design direction

Editorial, restrained "independent technical publication" style (reference: tieukhoimai.me for information architecture and presentation only, not to copy its content or identity). Long-form readability, comfortable line lengths, distinct styling for code, equations, quotes and diagrams, accessible contrast and keyboard navigation, minimal decorative animation.
