# editorial-os

An Editorial Operating System for technical and research publications, packaged as a Claude Code plugin. It turns an editorial standards manual into a repeatable workflow: audit, developmental edit, copy edit, fact-check, technical review, series review, publishing validation and a final publication gate, with deterministic checks and a review record for every published item.

It was built for [ACRR](https://acrr.asia) (Astro 7, MDX, KaTeX, Mermaid, GitHub Pages) and is configured for other sites through one JSON file.

## What is in it

| Part | Path | Role |
|---|---|---|
| Orchestrator skill | `skills/editorial` | Managing Editor: runs the 12-step lifecycle (inventory, classify, plan, sources, revise, review, resolve, series review, validate, gate, publish, record) |
| Audit skill | `skills/content-audit` | Inventory every page and item, score it, prioritize, write the audit report and remediation plan |
| Review skill | `skills/editorial-review` | Multi-stage review of one item into one report and one record |
| Series review skill | `skills/series-editorial-review` | Integrated review of a whole series (used when the project has no series-review skill of its own) |
| Style guide manager | `skills/style-guide` | Set up or change the config, standards, glossary and rule severities; adapt to a new site |
| Role agents | `agents/` | `developmental-editor`, `copy-editor`, `fact-checker`, `technical-reviewer`, `qa-editor` |
| Engine | `scripts/eos.mjs` | Dependency-free Node CLI: lint, fix, inventory, status, record, gate, validate-site, refs, check-external, vale-style, syntax, hook |
| Hook | `hooks/hooks.json` | After Claude edits a content file, adds that file's lint findings to Claude's context (never blocks) |
| Review protocol | `references/review-protocol.md` | Severity scale, finding format, evidence rules, record format |
| Schemas | `schema/` | JSON Schemas for `eos.config.json` and review records |
| Templates | `templates/` | Starting config, glossary, standards manual and review input for a new site |

Each role in the standards maps to a part: Editorial Director (the person who owns the standards), Managing Editor (`editorial` skill), Subject-Matter Editor and Technical Publishing Editor (`technical-reviewer`, `eos validate-site`), Developmental, Copy and Research/Fact-Checking Editors (their agents), Series Editor (`series-editorial-review` or the project's series skill), QA Editor (`qa-editor` with `eos record` and `eos gate`).

## Requirements

- Node.js for `eos` (it uses only Node's standard library). Verified with Node 22.22 on Linux; earlier versions have not been tested.
- Claude Code with plugin support for the skills, agents and hook. Verified with Claude Code 2.1.296 on Linux (`claude plugin validate`, project-scope install, hook output). Other platforms and other agent hosts have not been tested; the skills are plain Markdown and the engine is a plain Node script, so they can be used by hand elsewhere.
- `eos syntax` needs the project's own `@mdx-js/mdx` (and `remark-math` if the project uses math); it reports clearly when they are missing.
- Optional: Vale 3 for in-editor feedback (`eos vale-style` generates the style), a Python interpreter for the technical reviewer's recomputation, WebSearch/WebFetch for the fact-checker.

## Installation

### In this repository (ACRR)

Nothing to do: `.claude/settings.json` declares the repository as the `acrr` marketplace and enables `editorial-os@acrr`. Claude Code asks once to trust the project's plugins. `npm run eos -- <command>` runs the engine.

### In another project

1. Add the marketplace and install the plugin, in Claude Code:

   ```
   /plugin marketplace add acrr-asia/acrr
   /plugin install editorial-os@acrr
   ```

   Or vendor it: copy `plugins/editorial-os/` into your repository and declare a local marketplace (see `.claude-plugin/marketplace.json` and `.claude/settings.json` in this repository for the two small files that do it).

2. Create the editorial files:

   ```sh
   node <plugin-root>/scripts/eos.mjs init
   ```

   This writes `editorial/eos.config.json`, `editorial/glossary.json` and `editorial/standards.md` from the templates and never overwrites existing files. Then ask Claude to run the `style-guide` skill, or edit the config yourself (next section).

3. Optional shortcut in `package.json`: `"eos": "node <path-to>/editorial-os/scripts/eos.mjs"`.

4. Check: `eos inventory` should list your content; `eos lint` should run without configuration errors.

## Configuring for a site

Everything site-specific lives in `editorial/eos.config.json` (schema: `schema/eos.config.schema.json`; worked examples: `templates/eos.config.example.json` for a Hugo-style site, `editorial/eos.config.json` in this repository for Astro).

| Key | What to set |
|---|---|
| `publication` | Name, URL, identity and audience; path of the standards manual |
| `language` | `variant` (`en-US` or `en-GB`), serial comma, contractions, heading and title case |
| `content.types` | One entry per content type: globs, public route pattern, required front-matter fields, required sections, whether it is a series index |
| `content.exclude`, `content.translations` | Files to skip (for example translations), and where translations live, so inventory can pair them |
| `content.fields` | Front-matter field names for title, description, dates, series, order, draft and example flags |
| `content.pages` | Built-site directory, static routes and route prefixes, for the inventory and validation |
| `thresholds` | Title and description length, sentence, paragraph and heading length |
| `glossary` | Path of the house terms and phrases file |
| `rules` | Severity per rule: `error` (blocks the gate), `warning`, `suggestion`, `off` |
| `acronyms`, `properNouns`, `references` | Known acronyms, words exempt from heading-case checks, reference section names |
| `review` | Records and audit directories, required stages per type, rubric minimums |
| `validation` | Commands the gate expects to pass (build, links, project checks) and built-site check options |

Domains outside engineering need only a different glossary, standards manual and rule severities; the engine has no domain knowledge. A site in another language than English can use the structural, link, record and gate features; the spelling-variant data and the prose phrase rules are English-only.

## Usage

In Claude Code:

| Ask | What runs |
|---|---|
| "What is the editorial status?" | `editorial` skill, `status` mode |
| "Audit the site" | `content-audit` skill |
| "Review and edit article X for publication" | `editorial` skill, `review` then `revise` |
| "Review series Y" | the project's series-review skill, or `series-editorial-review` |
| "Add a house term" / "We now use British spelling" | `style-guide` skill |
| "Publish these" | `editorial` skill, `publish` mode (stops at a ready pull request unless autonomous publishing is authorized) |

From a shell or CI:

```sh
eos status                    # stage of every item
eos lint --quiet              # errors only; exit 1 if any
eos fix --rules spelling-variant,terminology   # mechanical fixes in prose only
eos validate-site dist        # built HTML checks; exit 1 on any issue
eos record <file> --from review.json           # write a review record (see templates/review-input.example.json)
eos gate                      # exit 1 unless every published item has a current, passing record
eos queue                     # editorial queue: workflow status per item, contracts, open live findings
eos queue init                # add a queue entry for every item without one (never overwrites)
eos queue set <id> <status> --by <who> --note <why>   # change a workflow status; appended to the history
eos queue validate            # exit 1 on queue problems (the gate runs it when queue.enforce is warn or error)
```

A record is current only while the file's content hash matches the hash it was written for, so any edit after review sends the item back to `review-stale` and the gate fails until it is reviewed again. That is the mechanism that keeps the gate honest.

## Continuous integration

Add after the build in the workflow that guards publication:

```yaml
- run: node plugins/editorial-os/scripts/eos.mjs lint --quiet
- run: node plugins/editorial-os/scripts/eos.mjs validate-site dist
- run: node plugins/editorial-os/scripts/eos.mjs gate
```

ACRR runs these in `.github/workflows/publication-gate.yml` (pull requests) and `deploy.yml` (before deploying). External links are best checked on a schedule rather than in the gate, because a remote outage should not block publication: `eos check-external` reports unreachable hosts as "not verified".

## What it does not do

- It does not verify facts by itself. The fact-checker agent does, with web access, and records what it could not verify. No claim is marked verified without a source that was actually read.
- It does not replace the people who own the standards. Scope changes (a new article, dropping a planned entry) are findings for the Editorial Director.
- It has not been tested outside Linux, outside Claude Code, or with site generators other than Astro (the Hugo example config is untested against a real Hugo site).

## More

- [docs/workflow.md](docs/workflow.md): the publishing workflow, stage by stage, with the commands and the records it leaves
- [docs/maintenance.md](docs/maintenance.md): changing rules, adding terms, upgrading, troubleshooting
- [CHANGELOG.md](CHANGELOG.md)

License: MIT ([LICENSE](LICENSE)).
