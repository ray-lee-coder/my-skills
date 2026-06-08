# my-skills

> **This is a standalone curated collection, not a Hermes backup.**
> Before any change, read `~/.hermes/dev-logs/collections/methodology.md`.
> Adapts to: Hermes · OpenClaw · Cursor · Claude Code — design decisions must hold across all 4, not just Hermes.

A curated cross-source collection of 100 AI agent skills, organized into 5 categories:
`dev/` · `doc/` · `marketing/` · `biz/` · `meta/`

## Layout

```
my-skills/
├── CLAUDE.md                this file (agent entry point)
├── README.md                GitHub-facing overview
├── LICENSE                  MIT
├── banner.png
├── scripts/validate.py      quality gate — run before commit
└── <category>/
    ├── README.md            per-category overview
    └── <skill>/SKILL.md     one directory per skill
```

## Hard rules (non-negotiable)

1. **Standalone project.** This repo is a first-class deliverable, not a Hermes backup. Any change that only optimizes for Hermes is wrong.
2. **Curate, don't accumulate.** Default target 30-50 skills. Bulk stages are OK; final delivery must be tight.
3. **Skill = noun, command = verb.** This repo has no `commands/` directory — slash-command workflows don't exist in this ecosystem. End-to-end workflows are encoded as skills with a sequence of steps in the body.
4. **Frontmatter required on every `SKILL.md`:** `name` (must match directory name) + `description` (must contain a trigger phrase: `Use when` / `Use for` / `Triggers` / `Use this`).
5. **Run `python3 scripts/validate.py` before every commit.** CI gate, not a suggestion.
6. **No Claude-Code-specific structures:** no `.claude-plugin/marketplace.json`, no `plugin.json`, no `$ARGUMENTS` placeholders. These don't work in Hermes/OpenClaw/Cursor.

## Maintenance workflow

1. Read `~/.hermes/dev-logs/collections/methodology.md` (shared across all curated collections).
2. Pick the right SOP from `~/.hermes/dev-logs/collections/sops/`:
   - `SOP-new-collection.md` — first-time setup
   - `SOP-audit.md` — quality audit on existing items
   - `SOP-add-item.md` — adding a single item
   - `SOP-sync-upstream.md` — pulling changes from upstream sources
3. Run `python3 scripts/validate.py` to confirm zero errors before commit.
4. Update the per-category `README.md` count and total badge in root `README.md`.

## Sources tracked (for upstream sync)

- `phuryn/pm-skills` — primary PM/process source
- `nexscope-ai/eCommerce-Skills` — e-commerce
- `aitytech/agentkits-marketing` — marketing/CRO
- `yizhiyanhua-ai/agent-skills` — official Anthropic mirror + meta-tools
- `laolaoshiren/claude-code-skills-zh` — Chinese dev

Sync policy: quarterly review, not real-time. See `SOP-sync-upstream.md`.

## What this is NOT

- Not a fork of any single source — items are cherry-picked across sources.
- Not a Claude Code plugin marketplace — no `marketplace.json`, install via direct clone.
- Not sealed at 100 items — the number is current count, not a target ceiling.
