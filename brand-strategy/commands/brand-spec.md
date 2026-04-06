---
name: brand-spec
description: "Phase 1: Intake brief, extract data from source PDFs, run parallel competitive research via Parallel AI (Ultra), map landscape."
---

# Phase 1: Specification

You are starting the **Spec** phase of a brand repositioning project.

## Step 1: Extract Source Materials

1. **Locate documents** — Find all PDFs, PPTX, and brief documents in the working directory
2. **Extract data** — Use `pdfplumber` for PDFs, `python-pptx` for PPTX. Use parallel agents for 3+ documents.
3. **Structure findings** — Client overview, metrics, target audience, competitors, hypotheses

## Step 2: Parallel Competitive Research (Parallel AI Ultra)

After extracting the brief and identifying competitors, run deep research via **Parallel AI**:

### Prepare the Research Prompt

1. Read the template: `references/competitive_research_template.md` (in the brand-strategy plugin)
2. Customize for this project:
   - Replace client name and market position
   - Update the competitor list (up to 10)
   - Set priority levels (HIGH for direct competitors, MEDIUM for peripheral)
   - Adjust the 30-dimension framework if needed

### Submit to Parallel AI

**Configuration:**
- **Processor: Ultra** (not Ultra8x — Ultra gives deeper research per competitor)
- **Tasks:** 1 per competitor, all running in parallel
- **Output:** Structured markdown, 30 dimensions per competitor

Submit via Parallel AI MCP or web platform (platform.parallel.ai):
- Create a task group with all competitors
- Each task gets the full prompt + competitor-specific instructions
- Wait for all tasks to complete (~10-15 min for Ultra)

### Process Results

1. Save reports to `research_reports/01_[name].md` through `10_[name].md`
2. Create `research_reports/README.md` with run IDs and platform URLs
3. Parse all reports into `competitive_analysis.csv` (30 columns × N competitors)
4. Generate `research_reports/00_competitive_intelligence_summary.md`:
   - Cross-competitor comparison tables
   - Archetype territory map
   - Affluent offering gaps
   - White space opportunities

## Step 3: Synthesize Spec

Create `analysis/spec_summary.md` combining:

**From source documents:**
- Client overview (name, market position, key metrics)
- Strategic problem (1-2 paragraphs)
- Target audience profile (demographics, goals, barriers)
- Available positioning hypotheses

**From Parallel AI research:**
- Competitive landscape (all identified competitors × 30 dimensions)
- Archetype map — who occupies which territory, what's free
- Affluent segment gaps — which competitors serve 2M+, which don't
- Communication territory analysis — who says what, where

## Step 4: Gate Check

Present to user:
1. Spec summary highlights
2. Competitor archetype map
3. Available hypotheses
4. **Ask:** "Which hypothesis do you want to develop? Or propose your own?"

Only proceed to `/brand-plan` after user confirms.

## Important

- Respond in the same language as source materials
- Use Parallel AI Ultra (not Ultra8x) for research depth
- The 30-dimension framework covers: identification, brand, communication, product, affluent deep-dive, digital, ecosystem, market position, sources
- Each competitor report should have 2-3 source citations per claim
