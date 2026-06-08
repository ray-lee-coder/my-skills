# my-skills

> **This is a standalone curated collection, not a Hermes backup.** Before any change, read `CONTEXT.md` and `scripts/validate.py`.

## Layout

```
my-skills/
├── CLAUDE.md            this file
├── CONTEXT.md           shared domain vocabulary
├── README.md            GitHub-facing
├── scripts/validate.py  quality gate — must PASS before commit
└── <category>/          dev | doc | marketing | biz | meta
    ├── README.md
    └── <item>/SKILL.md
```

## Hard rules (non-negotiable)

1. **Standalone project.** First-class deliverable, not a tool backup. Decisions must hold across Hermes / OpenClaw / Cursor / Claude Code.
2. **Curate, don't accumulate.** Default target 30-50. Bulk stages OK; final delivery tight.
3. **Every `SKILL.md` has frontmatter:** `name` (1-64 chars, kebab-case, matches dir) + `description` (trigger phrase, 30-1024 chars en / 15-200 zh).
4. **No Claude-Code-only syntax in SKILL.md body.** No `` !`command` `` shell injection. Skills must be cross-agent.
5. **Run `python3 scripts/validate.py` before commit.** Zero errors required; warnings accepted.
6. **No Claude-Code-specific repo structures:** no `.claude-plugin/marketplace.json`, no `plugin.json`, no `$ARGUMENTS` placeholders.

## Naming

- Noun or verb, both fine — match upstream convention when porting.
- Lowercase, hyphens, no `--`, no leading/trailing hyphen.
- Disambiguate via "for X, see Y" in description (see CONTEXT.md "Scope boundary").

## Workflow

1. Read `CONTEXT.md` (terms) + this file (rules).
2. New item → cherry-pick from upstream, copy to `<category>/<item>/SKILL.md`, add to category README.
3. Modify item → keep frontmatter, update body, re-run validator.
4. Sync upstream → diff, judge per-item, update only what fixes bugs or improves clarity.

## Sources tracked

phuryn/pm-skills · nexscope-ai/eCommerce-Skills · aitytech/agentkits-marketing · yizhiyanhua-ai/agent-skills · laolaoshiren/claude-code-skills-zh · coreyhaines31/marketingskills · mattpocock/skills
