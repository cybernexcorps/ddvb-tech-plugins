---
name: parallel-research
description: "Parallel AI deep research for competitive intelligence. Use when researching multiple competitors, market players, or data sources simultaneously. Generates structured research with adaptive industry-specific dimensions."
metadata:
  priority: 8
  pathPatterns:
    - "competitive_analysis*"
    - "research_reports/*"
    - "*competitor*"
  bashPatterns:
    - "parallel"
---

# Parallel Competitive Research via Parallel AI

## Overview

Use **Parallel AI** (platform.parallel.ai) to run deep research on multiple competitors simultaneously. Each competitor gets its own research task, all running in parallel with web search and source verification.

## Adaptive Dimension Framework

Research dimensions are split into two layers:

- **Fixed (17)** — universal dimensions always included: Identification (3), Brand & Positioning (5), Communication (4), Market Position (4), Sources (1)
- **Variable (8-15)** — industry-specific dimensions selected based on the client's sector

See `references/research-dimensions.md` for the full dimension catalog with industry presets.

### Dimension Selection Workflow

**Step 1: Auto-detect industry.** Read the client brief and identify the closest industry from:
- Finance / Investment / Banking
- FMCG / Food & Beverage / Consumer Goods
- Tech / SaaS / Software
- Professional Services / Agency / Consulting
- E-commerce / Marketplace / Retail
- Manufacturing / Industrial / B2B

**Step 2: Propose dimensions.** Present the matched preset to the user:

```
Based on the brief, I've identified this as a **[Industry]** project.

Fixed dimensions (always included): 17
Suggested variable dimensions from [Industry] preset: [N]
- V1. dimension_name — one-line description
- V2. ...

Total: [17 + N] dimensions per competitor

Would you like to add, remove, or customize any dimensions?
```

**Step 3: Suggest additional dimensions.** Based on strategic context, proactively suggest dimensions the user might not have considered:
- Cross-industry dimensions (e.g., FMCG company with e-commerce arm → suggest e-commerce dimensions)
- Strategic context dimensions (premium repositioning → affluent-specific dimensions)
- Competitive asymmetry dimensions (mix of traditional + digital-native → digital_transformation)

**Step 4: Get confirmation.** Only proceed after user confirms the final dimension set.

**Step 5: Number and compose.** Fixed dimensions 1-17, variable dimensions numbered 18+. Insert into the research template.

## Configuration

**Mode: Ultra** (not Ultra8x — Ultra gives better depth per task for 10 or fewer targets)

| Setting | Value |
|---------|-------|
| Processor | Ultra |
| Tasks | 1 per competitor (parallel, typically 5-10) |
| Output | Structured markdown per task |
| Search depth | Deep Research |
| Language | Match source materials |

## Workflow

### Step 1: Select Dimensions (see above)

Run the dimension selection workflow. Get user confirmation.

### Step 2: Generate Research Prompt

Use the adaptive template at `references/competitive_research_template.md`. Customize:

1. **Client info** — Replace all `{{PLACEHOLDERS}}`
2. **Competitors list** — Fill `{{COMPETITOR_TABLE}}` (up to 10)
3. **Variable dimensions** — Replace `{{VARIABLE_DIMENSIONS}}` with the confirmed set, numbered 18+
4. **Industry label** — Replace `{{INDUSTRY_LABEL}}` and `{{VARIABLE_SECTION_LABEL}}`
5. **Total count** — Replace `{{TOTAL_DIMENSIONS}}` with actual count (17 + variable)
6. **Client reference** — Replace `{{CLIENT_REFERENCE_POINT}}` with known client data for calibration
7. **Priority levels** — Set HIGH for direct competitors, MEDIUM for peripheral

### Step 3: Submit to Parallel AI

Via the Parallel AI MCP or web platform:

```
Task configuration:
- Type: Deep Research
- Processor: Ultra
- Parallel tasks: [number of competitors]
- Each task prompt: "Research [Competitor Name] across all [N] dimensions..."
- Attach the full prompt with dimension definitions
```

### Step 4: Collect Results

Each task returns a structured markdown report. Save to `research_reports/`:

```
research_reports/
├── README.md                              # Run metadata + task IDs
├── 00_competitive_intelligence_summary.md # Cross-competitor synthesis
├── 01_[competitor_1].md                   # Individual reports
├── 02_[competitor_2].md
├── ...
└── 10_[competitor_10].md
```

### Step 5: Parse into CSV

Merge all reports into a single `competitive_analysis.csv` with:
- Rows = competitors (N)
- Columns = all dimensions (17 fixed + variable)
- Each cell = the research finding for that competitor × dimension

```python
import csv
import re
from pathlib import Path

reports_dir = Path("research_reports")
total_dims = {{TOTAL_DIMENSIONS}}  # replace with actual count

rows = []
for report_file in sorted(reports_dir.glob("[0-9][0-9]_*.md")):
    if report_file.name.startswith("00_"):
        continue  # skip summary
    text = report_file.read_text(encoding="utf-8")
    row = {"file": report_file.name}
    for i in range(1, total_dims + 1):
        pattern = rf'{i}\.\s*\*\*\w+\*\*\s*[—–-]\s*(.*?)(?=\n\d+\.\s*\*\*|\n##|\Z)'
        match = re.search(pattern, text, re.DOTALL)
        row[f"dim_{i}"] = match.group(1).strip() if match else ""
    rows.append(row)

with open("competitive_analysis.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["file"] + [f"dim_{i}" for i in range(1, total_dims + 1)])
    writer.writeheader()
    writer.writerows(rows)
```

### Step 6: Synthesize into Summary

Create `research_reports/00_competitive_intelligence_summary.md` with:
- Cross-competitor comparison tables
- Archetype map (who occupies which territory)
- Industry-specific gap analysis (based on variable dimensions)
- White space identification for the client

## Quality Rules

- **Ultra mode** gives deeper search per task than Ultra8x (which optimizes for throughput)
- Cross-reference: 2-3 sources per factual claim minimum
- Recency: current year data preferred, flag vintage explicitly
- Verbatim quotes: include actual slogans in «кавычки»
- Gap documentation: absence of data IS data — state "Информация не найдена"
- No hallucination: if uncertain, say so
