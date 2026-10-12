# Decisions and lessons (long-term memory)

Newest first. Read the entries that touch an area before changing it. Stable rules live in CLAUDE.md; this file keeps the reasons. Format: see `.claude/skills/handoff/SKILL.md`.

## 2026-10-12 — Claude Code project setup
Project skills (`write-article`, `write-insight`, `plan-series`, `editorial-review`, `verify-site`, `handoff`), a SessionStart hook for cloud sessions, and committed memory files. **Why:** cloud sessions start from a fresh clone, so setup and memory must live in the repo. **Applies to:** `.claude/`.

## 2026-10 — Mermaid rendered at build time
Mermaid blocks become inline SVG via `rehype-mermaid` in headless Chromium, recoloured with tokens; a broken diagram fails the build. **Why:** no client-side scripts or CDNs, and diagrams must follow dark mode. **Applies to:** `astro.config.mjs`, `src/plugins/rehype-mermaid-figure.mjs`, `prose.css`, the pinned `playwright` version and the deploy workflow.

## 2026-10 — Deploy to GitHub Pages at acrr.asia
`.github/workflows/deploy.yml` on push to `master` with `SITE_URL=https://acrr.asia`; `public/CNAME`. **Why:** static site, no backend. **Applies to:** deployment, `scripts/check-site-url.mjs`.

## Before 2026-10 — Foundational choices (recorded in CLAUDE.md)
Astro 7 with `build.format: 'file'` and `trailingSlash: 'never'`; drafts filtered only in `src/lib/content.ts`; listing pages not indexed by Pagefind; Shiki `github-dark-default` for contrast. **Why:** see the matching CLAUDE.md sections.
