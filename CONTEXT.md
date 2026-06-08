# my-skills Context

> Domain language table for my-skills. All SKILL.md files reference these terms.
> Pattern: mattpocock/skills/CONTEXT.md — shared vocabulary, not duplicated per skill.
> 2026-06-08: first version, modeled after mattpocock.

## Core terms

**Item**:
A single curated unit in the collection — one directory with a SKILL.md.
_Avoid_: skill (overloaded; "skill" is a runtime concept in some agents, "item" is the collection concept), entry, record.

**Category**:
A first-level directory under repo root (`dev/`, `doc/`, `marketing/`, `biz/`, `meta/`) grouping items by domain, NOT by source.
_Avoid_: section, bucket, type.

**Upstream**:
A external GitHub repository from which items were cherry-picked. We do not fork — items are copied and adapted.
_Avoid_: source (overloaded with "data source", "source of truth"), origin, vendor.

**Trigger phrase**:
A phrase in the `description` frontmatter field that signals when an agent should load this item. Examples: "Use when...", "Use for...", "Triggers...", or Chinese "用于", "使用场景".
_Avoid_: keyword (too SEO-flavored), tag (too generic), prompt (overloaded).

**Scope boundary**:
An explicit "for X, see Y" sentence in the `description` that disambiguates overlapping items. Prevents two items from being triggered for the same input.
_Avoid_: cross-reference (too generic), link (overloaded).

## Cross-cutting

**Validator**:
`scripts/validate.py` — quality gate. Errors fail; warnings don't. Run before every commit.

**Frontmatter**:
The YAML block at the top of each SKILL.md, between `---` markers. Contains at least `name` and `description`. May contain a nested `metadata:` block.

**Body**:
Everything after the frontmatter in a SKILL.md. The actual instructions an agent reads when the item is triggered.

## Item lifecycle states

- **Active**: listed in README, validator passes, may be installed
- **Deprecated**: kept in `meta/` or `deprecated/`, README marks it, validator may warn
- **Pending**: being evaluated, not yet committed

## What this file is NOT

- Not a glossary for end users — only for collection maintainers and agents
- Not versioned per item — that's `VERSIONS.md` (TBD; not yet created)
- Not the source of truth for "what counts as a valid item" — that's `scripts/validate.py`
