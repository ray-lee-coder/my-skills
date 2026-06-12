# Skill Auto-Triggers Hint (Experimental)

> **Status:** Draft v0.1 — 2026-06-12
> **Purpose:** Manual trigger hints for the 5 highest-value skills in this collection. No automatic routing. No agent layer. You tell the AI which skill to use; this document tells you when to.
>
> **Why this exists:** `my-skills` has 153 skills. Most will never be triggered automatically because the description-based matching is too loose. This file is the human-side override — when your task fits one of these patterns, you explicitly invoke the skill.
>
> **What this is NOT:** Not an agent layer. Not a workflow engine. Not a registry. Just a 1-page cheat sheet.

## The 5 Core Skills (most likely to actually be useful)

| When you want to... | Tell the AI | Skill that runs |
|---|---|---|
| Design a B2B go-to-market plan, audit your current motion, or pick channels/budget | "Use gtm-strategy to plan our Q3 launch" | `biz/gtm-strategy` |
| Define or refine your ICP with scored tiers (firmographic + psychographic + behavioral) | "Use ideal-customer-profile to score our target accounts" | `biz/ideal-customer-profile` |
| Write a cold email sequence with the SPARK framework + follow-up engine | "Use outbound-copywriter for our 4-step campaign" | `biz/outbound-copywriter` |
| Generate a 13-section AARRR marketing plan with budget allocation | "Use marketing-plan for our 12-month roadmap" | `marketing/marketing-plan` |
| Get a primer on cold email basics (subject lines, openers, CTAs) | "Use cold-email to write 3 subject line variants" | `marketing/cold-email` |

## Routing Rules (avoid double-trigger)

These 5 overlap with each other and with other skills. Pick by scope:

- **GTM strategy vs marketing plan** — both produce plans. Use `gtm-strategy` for B2B with explicit channel/motion/budget decisions. Use `marketing-plan` for AARRR-structured 13-section deliverable with current-state audit. They reference each other but the output format differs.
- **Outbound copywriter vs cold-email** — `outbound-copywriter` is the full SPARK + 7 archetypes + 4-step follow-up engine. `cold-email` is the shorter primer (subject lines, openers, basic CTAs). Use the long one for serious campaigns; the short one for quick drafts.
- **ICP vs user-personas** — `ideal-customer-profile` (biz) gives you a scored, tiered matrix for outbound prioritization. `user-personas` (marketing) is qualitative narrative personas. Quantitative scoring → biz. Qualitative persona docs → marketing.

## Invocation Patterns

The my-skills frontmatter is built to be cross-agent. In Claude Code:

```
> Use gtm-strategy to design a SaaS launch motion for US SMB
> Use ideal-customer-profile to tier our 200 target accounts
> Use outbound-copywriter for a 4-step cold email sequence
```

In OpenClaw / Cursor / other agents, the invocation syntax differs but the skill file is the same. See `../CONTEXT.md` for cross-agent notes.

## How to Validate This Document Works

This file is **experimental** and **self-rescinding** if unused. Validation criteria:

- **Use it 5+ times over 2 weeks** → keep it, expand to top 10 skills
- **Use it 0 times in 2 weeks** → delete it, the 153 skills remain format-only and the user is fine with that
- **You find a 6th skill more useful than 1 of the 5** → swap it in, log the swap in `~/.hermes/dev-logs/my-skills/`

## Why Not Build the Real Thing?

The "real thing" would be:
- An `agents/` directory (Claude Code plugin pattern) that auto-loads skills by user intent
- A workflow engine that chains skills like `mkt-strategist` (Vietnamese: `00-ke-hoach-mkt` → `08-nghien-cuu-doi-thu` → `09-insight-khach-hang` → `10-tinh-kpi-nguoc`)
- A region-variant system (US/EU/SEA/LATAM benchmarks)
- An MCP server registry (`.mcp.json`)

**Why we're not building any of that**:
1. `my-skills` CLAUDE.md hard rule 6 forbids Claude-Code-only structures (no `.claude-plugin/marketplace.json`, no `plugin.json`, no `$ARGUMENTS`). Plugin-style agents would violate this.
2. No real usage data yet — building routing infrastructure before proving any skill is actually used is the classic over-engineering trap. See `~/.hermes/dev-logs/my-skills/my-skills-dev-log.md` for context.
3. The user prefers "small, useful, with evidence" over "big, comprehensive, untested." 153 skills + validator PASS already ships value. Adding layers risks breaking what's not broken.

## Related

- `../CLAUDE.md` — hard rules (especially rule 6 on cross-agent constraints)
- `../CONTEXT.md` — domain vocabulary
- `../scripts/validate.py` — quality gate
- `skill-adoption-planner` — how to actually adopt skills in your workflow
- `skill-roi-calculator` — measure which skills are worth keeping
