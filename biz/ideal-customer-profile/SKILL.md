---
name: ideal-customer-profile
description: "Build a tiered ICP matrix with firmographic, psychographic, and behavioral scoring. Use when defining ICP, refining targeting after 3+ months of data, expanding into a new segment, or scoring accounts for outbound prioritization. For GTM motion and channel design, see gtm-strategy. For cold outreach copy, see outbound-copywriter."
metadata:
  version: 1.1.0
  category: strategy
  source: workflowsio-fused
license: MIT
triggers:
  - "ideal customer profile"
  - "ICP"
  - "target market"
  - "account scoring"
  - "firmographic"
  - "psychographic"
related:
  - gtm-strategy
  - outbound-copywriter
  - market-segments
  - user-personas
---

# Ideal Customer Profile

## Overview
Define a tiered ICP matrix that separates "could buy someday" from "should be in a sales sequence this week." This item merges the Jobs to Be Done ICP framework (Christensen-style: demographics, behaviors, JTBD, needs) with the workflows.io three-dimension scoring model (firmographic + psychographic + behavioral with explicit weights and tier cutoffs). Use Part 1 if you are early-stage and need a narrative ICP. Use Part 2 once you have data and need a scoring model your reps can run in 15 minutes.

## When to Use
- Defining ICP for the first time (pre-revenue or first 10 customers)
- Refining targeting after 3+ months of campaign data
- Expanding into a new market segment or vertical
- Quarterly ICP review (recommended every 90 days)
- Pre-revenue validation when no customers yet
- Scoring inbound accounts for routing or outbound prioritization

## Before You Start
Gather before building the matrix:
1. What you sell (product, key value prop, ACV range, sales cycle)
2. Your best 5-10 customers today (what makes them great)
3. Your worst customers (churned, low NPS, bad fit — equally important)
4. Available data: CRM closed-won, win/loss notes, campaign performance, intent data
5. Existing ICP work, personas, or targeting criteria
6. Channels used to reach them (outbound email, LinkedIn, ads, inbound, events)
7. Expanding into a new segment, or refining existing one?

Do not build from assumptions. If no data exists, use the Pre-Revenue Workflow below.

## Pre-Revenue Workflow
If you have no customers yet, work backward from competitors and your network:

1. **Competitor customer analysis.** Identify 3-5 direct competitors. Find their customers through case studies, G2 reviews, LinkedIn testimonials, job postings mentioning the competitor. Those companies share your likely ICP.
2. **Founder network analysis.** Your first 10 customers almost always come from your network. Build the ICP around companies you can actually reach.
3. **Problem-first definition.** Who feels this pain most acutely? Who has budget? Who has tried and failed with alternatives? Those answers define initial ICP.
4. **Hypothesis matrix.** Build the matrix below, but label every attribute as hypothesis or validated. Run 2-4 weeks of outbound. Track reply rates, meeting rates, objections by segment. Promote high-performers to validated.
5. **Rapid iteration.** After 50 outbound touches per segment, deprioritize anything under 2% reply rate, double down on anything above 5%.

## Part 1 — The Narrative ICP (Jobs to Be Done)

### ICP Framework Components

**Demographics — Who they are, firmographically and personally:**
- Company size (employees, revenue)
- Industry or vertical (specific sub-vertical, not broad category)
- Geographic location
- Job title and department
- Years of experience in the role
- Education and background
- Organizational structure and reporting line

**Behaviors — How they work and decide:**
- How they discover and evaluate solutions
- Buying process and decision-making timeline
- Technical literacy and product adoption speed
- Decision style (solo founder vs committee, consensus vs dictatorial)
- Change management and adoption style
- Tool switching frequency
- Community involvement and peer influence

**Jobs to Be Done — What they are trying to accomplish:**
- Primary job or goal (functional)
- Secondary jobs that support the primary
- Emotional jobs (how they want to feel)
- Social jobs (status, perception, team impact)
- Jobs they want to avoid or eliminate
- Frequency and importance of each job
- Success metrics for completing the job

**Needs and Pain Points — What problems you solve:**
- Specific pain points they experience
- Current workarounds and their limitations
- Impact on productivity or outcomes
- Cost or time burden of the problem
- Emotional frustration level
- Barriers to solving the problem
- Available budget
- Competing priorities

### How to Build the Narrative ICP
1. **Gather customer data.** PMF survey responses, customer interviews, trial behavior, support tickets, churn analysis, win/loss notes, competitor customer analysis.
2. **Segment by value.** Highest LTV, fastest time-to-value, lowest churn, highest expansion, most enthusiastic, best reference, most aligned with product vision.
3. **Profile demographics.** Common sizes, verticals, geographies, departments, budget holders, company stages, culture indicators.
4. **Identify behaviors.** Discovery channel, evaluation timeline, key stakeholders, obstacles, adoption speed, team involvement, feature usage, support needs.
5. **Define JTBD.** Primary job, emotional dimensions, social dimensions, success metrics, context, competing jobs, importance ranking.
6. **Document pain points.** Before state, after state, gap size, emotional dimensions, resource constraints, skepticism, success criteria.

## Part 2 — The Scored ICP Matrix (workflows.io lens)

An ICP is not a single profile. It is a scored, tiered matrix across three independent dimensions. Each contributes to the total. Scoring all three separates "could buy someday" from "should be in a sequence this week."

### Dimension 1: Firmographic (WHO they are)
Observable, quantifiable characteristics. Easiest to score at scale because data is public.

| Attribute | How to Define | Default Data Sources |
|---|---|---|
| Industry and vertical | Specific sub-vertical, not broad category | CRM, Apollo, Clay, LinkedIn, ZoomInfo |
| Company size (headcount) | Range; include department-specific headcount when relevant | LinkedIn, Apollo, BuiltWith |
| Revenue range | ARR or annual revenue; use ranges | PitchBook, Crunchbase, ZoomInfo |
| Geography | Country, region, city; note timezone implications | CRM, Apollo, LinkedIn, company website |
| Funding stage | Bootstrapped, Seed, A-C, Public | Crunchbase, PitchBook, TechCrunch |
| Business model | B2B, B2C, B2B2C, SaaS, marketplace | Website, G2, LinkedIn |
| Tech stack | Tools that indicate fit (HubSpot CRM, AWS, etc.) | BuiltWith, Wappalyzer, Clay |
| Company age | Years since founding; startup vs established | Crunchbase, LinkedIn |

**Firmographic scoring (default weights):**
- Industry match: 0 / 5 / 10 — weight HIGH
- Headcount range: 0 / 5 / 10 — weight HIGH
- Revenue range: 0 / 5 / 10 — weight MEDIUM
- Geography: 0 / 5 / 10 — weight MEDIUM
- Funding stage: 0 / 5 / 10 — weight LOW-MEDIUM
- Tech stack: 0 / 3 / 5 / 8 — weight MEDIUM
- Business model: 0 / 10 — weight HIGH

Max firmographic score: 63. If geography does not matter for your product, drop it to 0/0/5. If tech stack is a hard requirement, make it 0/0/10 binary.

**Good firmographic definition (specific, testable):** Industry = B2B SaaS in HR Tech (talent acquisition). Headcount = 50-500 with 5+ in sales. Revenue = $5M-75M ARR. Geography = US and UK. Funding = Series A-C raised in last 24 months. Tech stack = Salesforce or HubSpot CRM.

**Bad firmographic definition (vague, untestable):** Industry = "Technology companies." Headcount = "Mid-market." Revenue = "Growing." Geography = "Global." You cannot build a campaign list from this.

### Dimension 2: Psychographic (WHY they buy)
Internal motivations, pain points, decision patterns. Most predictive dimension but hardest to score at scale.

| Attribute | Data Sources |
|---|---|
| Primary pain points (in buyer language) | Customer interviews, sales calls, G2 reviews, support tickets |
| Buying triggers (events that make pain urgent) | LinkedIn job posts, news, funding events, interview patterns |
| Decision-making structure (who decides, influences, blocks) | Sales call notes, CRM deal data, org chart analysis |
| Budget availability (allocated for this solution type) | Funding, job postings mentioning category, tech stack spend |
| Urgency level (how fast do they need to solve) | Trigger recency, board pressure, regulatory deadlines |
| Sophistication (DIY attempts vs first-time buyers) | Tech stack history, G2 reviews, job postings |

**Psychographic scoring:**
- Pain point alignment: 0 / 5 / 10
- Active buying trigger: 0 / 5 / 10
- Budget indicators: 0 / 5 / 10
- Urgency signals: 0 / 5 / 10
- Sophistication match: 0 / 5 / 10

Max psychographic score: 50.

For each pain point, map: who feels it most, when it becomes urgent, the current workaround, the cost of inaction, how you solve it differently.

### Dimension 3: Behavioral (HOW they signal readiness)
Active signals that the company or its people are doing things that predict a purchase.

**Tier A signals (10 points each, high intent):** Visited pricing page, downloaded resource or attended webinar, currently evaluating competitors, leadership change in buying role under 90 days.

**Tier B signals (5 points each, moderate intent):** Hiring for roles your product supports, recent funding under 6 months, engaged with your LinkedIn content (commented not just liked), attended relevant industry event.

**Tier C signals (3 points each, weak but relevant):** Adopted adjacent technology, headcount growing above 20% YoY, published content on topics you address, opened/clicked previous outbound.

**Behavioral scoring with recency multiplier:**
- Under 7 days: 1.5x
- 7-30 days: 1.0x
- 30-90 days: 0.5x
- Over 90 days: 0.25x (consider dropping)

Max behavioral score: uncapped (more signals = higher score).

### Combine into Tiered Matrix

| Total Score | Tier |
|---|---|
| Firmographic ≥ 40 AND Psychographic ≥ 30 AND Total ≥ 80 | Tier 1 (Bullseye) |
| Firmographic ≥ 25 AND Psychographic ≥ 20 AND Total ≥ 50 | Tier 2 (Strong Fit) |
| Firmographic ≥ 15 AND Total ≥ 30 | Tier 3 (Good Fit) |
| Firmographic < 15 OR Total < 30 OR hard disqualifier | Disqualified |

**Hard disqualifiers (override score, instant DQ):** Direct competitor, existing customer (route to expansion not outbound), excluded industry, excluded geography, below minimum size, known bad-fit pattern (churned within 90 days before).

### Tier Treatment

| Treatment | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|
| Volume | 50-200 accounts | 200-500 accounts | 500-2,000 accounts |
| Research depth | Individual account | Segment-level | Minimal |
| Personalization | Hyper-personalized | Signal-based | Bucket/template |
| Channels | Email + LinkedIn + Phone + Direct mail (top 50) | Email + LinkedIn | Email only |
| Contacts per account | 3-5 (multi-thread) | 2-3 | 1-2 |
| Sequence | 4-step + manual touches | 4-step automated | 3-step automated |
| Expected reply rate | 8-15% | 4-8% | 1-4% |
| Sales involvement | AE-led, SDR supports | SDR-led, AE at meeting | Automated, SDR reviews replies |

### Validation and Calibration
- **Backtest:** Score existing customers. 80%+ should land Tier 1 or 2. If under 60%, your scoring is miscalibrated.
- **A/B test:** Run same message to Tier 1 vs Tier 3. Tier 1 should reply at 2-3x Tier 3 rate.
- **Sales feedback:** After 10 meetings, ask AE "did this feel real?" 70%+ of Tier 1 meetings should be qualified opportunities.
- **Conversion funnel:** Track lead-to-meeting and meeting-to-deal by tier. Tier 1 should convert at 2x Tier 2.

**Minimum sample:** 50 outbound touches per tier before drawing conclusions. 20+ replies per tier before changing weights. Log every change with the data that prompted it.

**Common calibration problems:**
- All accounts score Tier 1: criteria too broad. Tighten industry, headcount, or revenue.
- Almost no Tier 1: too narrow. Lower thresholds or relax 1-2 attributes.
- Tier 3 outperforms Tier 1: wrong attributes weighted high. Re-analyze closed-won, swap priorities.
- High reply, low close: firmographic right, psychographic wrong. Add pain/budget validation.
- High meetings, "not a fit" feedback: behavioral signals inflating scores for poor-fit. Require minimum firmographic regardless.

## ICP Matrix Output Template

```
# ICP Matrix: [Company] - [Product/Segment]
- Created / Last Updated / Status (Hypothesis or Validated)
- Review cadence: every 90 days

## 1. Product Context
- What we sell (1-2 sentences)
- Key value prop in buyer language
- ACV range
- Sales cycle

## 2. Tier 1 (Bullseye)
- Firmographic profile (industry, headcount, revenue, geography, funding, tech stack)
- Psychographic profile (pain, trigger, decision maker, budget signal, sophistication)
- Behavioral signals to monitor
- Campaign treatment (channels, personalization, contacts, sequence)

## 3. Tier 2 / Tier 3
- Same structure as Tier 1

## 4. Disqualified Segments
## 5. Hard Disqualifiers
## 6. Scoring Model (full tables with your customized weights)
## 7. Validation Plan
## 8. Changelog (date, change, data that prompted it)
```

## Tips
- Start from your best 10 customers. The pattern across them IS the Tier 1 definition. Work backward from proven buyers, not forward from assumptions.
- If you only have time to get one dimension right, make it psychographic. A perfect firmographic match with no pain alignment never converts.
- Behavioral signals decay fast. A funding round from 6 months ago is not the same signal as one from 2 weeks ago. Always apply recency multipliers.
- If Tier 1 is more than 15% of your total addressable market, the definition is too broad. If less than 3%, too narrow for sustainable campaign volume.
- Tech stack signals are underrated. A company using a direct competitor has proven budget, proven need, and proven buying behavior — Tier A even without other data.
- This matrix feeds directly into persona-building and outreach copy. Build the matrix first, then personas, then copy. For motion and channel design, see gtm-strategy. For outreach copy, see outbound-copywriter.
- For pre-revenue: supplement CRM data with competitor customer analysis. Find who buys from competing products. Those companies share your ICP.
- The ICP is not a marketing document. It is an operational tool. If your SDR team cannot use it to build a list in 15 minutes, it is too abstract. If your AE cannot use it to qualify a deal in the first 5 minutes of a call, it is missing psychographic detail.
- Update when you lose a deal you expected to win. Those losses contain more ICP signal than your wins.
