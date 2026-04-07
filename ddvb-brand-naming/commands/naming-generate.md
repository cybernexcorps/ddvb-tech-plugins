---
name: naming-generate
description: "Phase 2: AI-assisted seed generation. Recommend naming strategies, generate 30-50 categorized candidates, run automated availability checks."
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Agent, WebSearch, WebFetch
---

# Phase 2: Seed Generation

AI-assisted name candidate generation from the naming brief.

## Prerequisites

- `NAMING_BRIEF_FOR_COPYWRITER.md` must exist (from Phase 1)
- Read the brief to understand: semantic field, naming strategies, selection criteria, taboo list

## Step 1: Analyze Brief & Recommend Strategies

Read the naming brief and `references/naming-strategies.md`. Recommend 2-3 naming strategies:

```
Based on the competitive landscape and positioning:

Primary: [Strategy] — [why]
Secondary: [Strategy] — [why]
Avoid: [Strategy] — [why]
```

Present to user. Get confirmation on which strategies to focus generation on.

## Step 2: Generate Seed Candidates

Generate 30-50 name candidates, categorized by confirmed strategies:

For each candidate provide:
- **Name**
- **Strategy type** (descriptive, metaphorical, coined, etc.)
- **Etymology** (what roots, what it evokes)
- **Cross-language note** (how it sounds/means in target languages)
- **Phonetic character** (hard/soft, syllable count)

Group by strategy. Aim for:
- 12-18 in primary strategy
- 8-12 in secondary
- 5-8 exploratory (other strategies that might surprise)

## Step 3: Automated Availability Checks

Run the naming-linguistics skill's automated checks on ALL generated candidates:

1. **Domain availability** — .com + local TLDs
2. **Social handles** — Telegram, Instagram, VK
3. **Trademark search** — relevant registries and ICGS classes

Produce a batch summary table:

```
| # | Candidate | Strategy | .com | .ru | TG | IG | TM Risk | Notes |
|---|-----------|----------|------|-----|-----|-----|---------|-------|
```

## Step 4: Flag & Filter

- **GREEN** candidates: all checks pass
- **YELLOW**: partial availability (e.g., .com taken but .ru free)
- **RED**: trademark conflict or negative connotation — mark but don't auto-remove

## Step 5: Deliver Seed List

Save to `seeds/naming_seeds.md` with:
- Full candidate list (categorized, with all metadata)
- Availability summary table
- Flagged candidates with risk notes

Present to user:
1. Seed list highlights (top 10 by initial assessment)
2. Availability summary
3. **Ask:** "Review these seeds. The copywriter will use them alongside the brief to produce the full long-list. Ready to hand off to the copywriter?"

## After Handoff

The copywriter receives:
1. `NAMING_BRIEF_FOR_COPYWRITER.md` — the structured brief
2. `seeds/naming_seeds.md` — AI-generated seed candidates for inspiration

The copywriter returns: long-list of 50-80 candidates → feeds into Phase 3 (`/naming-evaluate`).
