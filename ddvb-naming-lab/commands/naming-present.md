---
name: naming-present
description: "Phase 4 (optional): Generate client-facing PPTX with final candidates, rationale, and recommendation."
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Agent, WebSearch, WebFetch
---

# Phase 4: Client Presentation (Optional)

Generate a client-facing PPTX presenting the final 3-5 name candidates.

## Prerequisites

- `evaluation/final_candidates.md` must exist (from Phase 3)
- `NAMING_BRIEF_FOR_COPYWRITER.md` for context
- `research_reports/naming_territory_map.md` for competitive context

## Step 1: Prepare Presentation Content

For each final candidate, prepare:
- Name displayed prominently
- Strategy type and etymology (simplified for client)
- Why it fits the positioning (1-2 sentences)
- Scoring highlights (top 3 strengths, visualized)
- Availability status (domain, social, trademark — green/yellow/red)
- Competitive differentiation (how it stands apart on the territory map)

## Step 2: Slide Structure

Generate a PPTX with DDVB branding:

| Slide | Content |
|-------|---------|
| 1 | Title: "[Client] — Naming Presentation", DDVB logo, date |
| 2 | Process overview: how we arrived at these candidates (brief → research → generation → evaluation) |
| 3 | Competitive naming landscape (territory map visualization) |
| 4 | Evaluation criteria summary (10 dimensions, simplified for client) |
| 5-9 | One slide per candidate (name, strategy, fit, strengths, availability) |
| 10 | Comparison matrix (all candidates side-by-side, scored) |
| 11 | Recommendation (which name and why) |
| 12 | Next steps (trademark registration, domain acquisition, brand identity development) |

## Step 3: Generate PPTX

Use the DDVB presentation template:
- Dark backgrounds with DDVB corner markers (D/D/V/B)
- Atyp Display / Atyp Text typography
- Orange #FFC000 accent system
- Clean, minimal slide design

Generate via Python script using `python-pptx`. See `references/build_naming_pptx_template.py` for the base template.

## Step 4: Deliver

Save PPTX to: `[CLIENT]_NAMING_PRESENTATION_DDVB.pptx`

Present to user:
1. File path
2. Slide count and structure summary
3. **Ask:** "Review the deck. Any adjustments before the client meeting?"

## Important

- This is a CLIENT-FACING document — professional, polished, confident
- Do NOT include the full scoring matrix — show simplified strengths
- Do NOT include the taboo list or internal naming brief content
- Each candidate slide should feel like a reveal — build excitement
- The recommendation slide should have a clear, single recommendation with backup reasoning
