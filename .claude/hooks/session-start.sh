#!/bin/bash
# SessionStart hook for Claude Code cloud sessions: makes `npm run build`,
# `npm run check` and `npm run check:links` work as soon as the session starts.
# Local sessions are left alone (contributors install once, see README.md).
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "$CLAUDE_PROJECT_DIR"

# `npm install` (not `npm ci`) so the cached container state is reused.
npm install --no-audit --no-fund --loglevel=error

# Mermaid diagrams are rendered at build time in headless Chromium. The cloud
# image usually ships the revision the pinned playwright wants; download only
# when it is missing (the deploy workflow does the same with --with-deps).
if ! npx --no-install playwright install --dry-run chromium 2>/dev/null \
  | awk '/Install location:/ {print $3}' \
  | while read -r dir; do [ -d "$dir" ] || exit 1; done; then
  npx --no-install playwright install chromium
fi

# The short-term memory file is the first thing to read in a new session.
if [ -f .claude/memory/working-notes.md ]; then
  echo "ACRR: dependencies ready. Read .claude/memory/working-notes.md for in-progress work."
fi
