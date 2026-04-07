---
name: brand-spec
description: "Phase 1: Intake brief, extract data from source PDFs, select research dimensions, run parallel competitive research via Parallel AI (Ultra), map landscape."
---

# Phase 1: Specification

You are starting the **Spec** phase of a brand repositioning project.

## Step 1: Extract Source Materials

1. **Locate documents** — Find all PDFs, PPTX, and brief documents in the working directory
2. **Extract data** — Use `pdfplumber` for PDFs, `python-pptx` for PPTX. Use parallel agents for 3+ documents.
3. **Structure findings** — Client overview, metrics, target audience, competitors, hypotheses

## Step 2: Identify Industry & Select Research Dimensions

After extracting the brief, before running competitive research:

### 2a. Auto-detect industry

Read the extracted brief and identify the client's industry sector. Look for:
- Products/services described
- Competitors mentioned and their type
- Market terminology (trading, retail, SaaS, production, etc.)
- Regulatory context

Match to one of: **Finance**, **FMCG**, **Tech/SaaS**, **Services/Agency**, **E-commerce**, **Manufacturing**

### 2b. Propose dimensions to the user

Read `references/research-dimensions.md` for the full dimension catalog. Present:

```
Based on the brief, I've identified this as a **[Industry]** project.

**Fixed dimensions (always included):** 17
A. Identification (3) · B. Brand & Positioning (5) · C. Communication (4) · H. Market Position (4) · I. Sources (1)

**Suggested variable dimensions from [Industry] preset:** [N]
- V1. dimension_name — one-line description
- V2. dimension_name — one-line description
...

**Total: [17 + N] dimensions per competitor**
```

### 2c. Suggest additional dimensions

Based on the strategic context, proactively suggest dimensions the user might not have considered:
- Cross-industry dimensions if the business spans sectors
- Premium/affluent-specific dimensions if repositioning upmarket
- Digital/tech dimensions if competitors include digital-native players
- Export/international dimensions if cross-border expansion is relevant

Frame as: "Based on the strategic context, you might also want to add: ..."

### 2d. Get confirmation

Ask the user to confirm, add, remove, or customize dimensions. **Do not proceed to research until dimensions are confirmed.**

## Step 3: Parallel Competitive Research (Parallel AI Ultra)

After confirming dimensions, run deep research via **Parallel AI**:

### Prepare the Research Prompt

1. Read the adaptive template: `references/competitive_research_template.md` (in the brand-strategy plugin)
2. Customize for this project:
   - Replace all `{{PLACEHOLDERS}}` with actual client data
   - Fill `{{COMPETITOR_TABLE}}` with identified competitors (up to 10)
   - Replace `{{VARIABLE_DIMENSIONS}}` with the confirmed variable dimensions, numbered 18+
   - Set `{{TOTAL_DIMENSIONS}}` to actual count
   - Set priority levels (HIGH for direct competitors, MEDIUM for peripheral)
   - Fill `{{CLIENT_REFERENCE_POINT}}` with known client data for calibration

### Submit to Parallel AI

**Configuration:**
- **Processor: Ultra** (not Ultra8x — Ultra gives deeper research per competitor)
- **Tasks:** 1 per competitor, all running in parallel
- **Output:** Structured markdown, all dimensions per competitor

Submit via Parallel AI MCP or web platform (platform.parallel.ai):
- Create a task group with all competitors
- Each task gets the full prompt + competitor-specific instructions
- Wait for all tasks to complete (~10-15 min for Ultra)

### Process Results

1. Save reports to `research_reports/01_[name].md` through `10_[name].md`
2. Create `research_reports/README.md` with run IDs and platform URLs
3. Parse all reports into `competitive_analysis.csv` (all dimensions × N competitors)
4. Generate `research_reports/00_competitive_intelligence_summary.md`:
   - Cross-competitor comparison tables
   - Archetype territory map
   - Industry-specific gap analysis (based on variable dimensions selected)
   - White space opportunities

## Step 4: Synthesize Spec

Create `analysis/spec_summary.md` combining:

**From source documents:**
- Client overview (name, market position, key metrics)
- Strategic problem (1-2 paragraphs)
- Target audience profile (demographics, goals, barriers)
- Available positioning hypotheses

**From Parallel AI research:**
- Competitive landscape (all identified competitors × confirmed dimensions)
- Archetype map — who occupies which territory, what's free
- Industry-specific gaps identified from variable dimensions
- Communication territory analysis — who says what, where

**Research dimensions used:**
- Document which dimensions were included (fixed + variable)
- Note any dimensions that were added/removed vs the default preset
- This metadata helps the Plan phase reference specific findings

## Step 5: Gate Check

Present to user:
1. Spec summary highlights
2. Competitor archetype map
3. Available hypotheses
4. **Ask:** "Which hypothesis do you want to develop? Or propose your own?"

Only proceed to `/brand-plan` after user confirms.

## Important

- Respond in the same language as source materials
- Use Parallel AI Ultra (not Ultra8x) for research depth
- The dimension framework is adaptive — fixed 17 + variable from industry preset
- **Always confirm dimensions with the user before running research**
- Each competitor report should have 2-3 source citations per claim
- Document which dimensions were used in spec_summary.md for downstream phases
