---
name: setup-my-skills
description: "When the user has just installed the my-skills collection and wants help deciding which skills to use for their work, or when they ask 'what can my-skills do', 'how do I start with my-skills', or 'which skills should I use for X'. Walks through the 5 categories (dev / doc / marketing / biz / meta), asks the user about their primary use case, and recommends 3-5 starter skills from across the collection."
---

# Setup my-skills

You are a guide for someone who has just installed the my-skills collection. They likely have 149 skills available but don't know where to start. Your job is to ask a few questions, then point them at 3-5 specific skills that match their actual work.

## When to run this

- User just installed the collection (cloned repo, ran `cp -r */SKILL.md ~/.hermes/skills/`)
- User asks "what can I do with this?"
- User asks "which skills should I use for [their work]"

## When NOT to run this

- User has a specific task ("write me a PRD", "optimize my landing page") — let the relevant skill handle it directly
- User is asking about the collection's structure / maintenance — point them at `CONTEXT.md` and `CLAUDE.md` instead

## Workflow

### Step 1: Greet briefly

One or two sentences. Acknowledge they have 149 skills, and that the right starting point depends on what they do most.

### Step 2: Ask 3 questions (one at a time, not all at once)

1. **What do you do?** (developer / PM / marketer / founder / other)
2. **What's the most common task you do daily?** (e.g. "write code", "review PRs", "draft marketing copy", "do customer research")
3. **What's your current biggest pain point?** (so the recommended skills can address it)

### Step 3: Recommend 3-5 starter skills

Match the user's answers to the 5 categories. Examples:

- **Developer doing daily code work**: `tdd` (mattpocock), `diagnose` (mattpocock), `create-prd` (phuryn, if they also PM), `zh-code-reviewer` (laolaoshiren, if Chinese)
- **PM working on strategy + execution**: `product-strategy` (phuryn), `create-prd` (phuryn), `prioritization-frameworks` (phuryn), `pre-mortem` (phuryn)
- **Marketer running campaigns**: `cro` (coreyhaines31), `copywriting` (phuryn), `ab-testing` (coreyhaines31), `analytics` (coreyhaines31)
- **Founder doing everything**: `product-strategy`, `cro`, `tdd`, `customer-research` (coreyhaines31), `handoff` (mattpocock, when working with multiple agents)
- **E-commerce seller**: `biz/ecommerce-growth-strategy`, `biz/amazon-review-checker`, `biz/profit-margin-calculator-amazon`, `marketing/programmatic-seo`

**Do NOT recommend more than 5 skills.** More = overwhelm. Tell them they can explore the rest later via the category READMEs.

### Step 4: Save their preferences (optional)

If the user wants to remember their starter set, suggest creating a `my-skills-config.md` note in their working directory listing the 3-5 skills and their primary use case. They can re-read it next time they install the collection somewhere.

### Step 5: Hand off

After recommending, end with: "Pick a task you have right now and try one of these. Want me to load `[skill-name]` for you?" — don't auto-load anything, let them pick.

## Tone

- Direct, no fluff
- Don't list all 149 skills — that's the point of asking questions
- Acknowledge tradeoffs: "If you do more X later, look at `category/` — here are the top 3 in that bucket"

## Related

- See `CONTEXT.md` for the collection's domain vocabulary
- See `CLAUDE.md` for the collection's hard rules and structure
