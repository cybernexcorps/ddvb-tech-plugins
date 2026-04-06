---
name: parallel-research
description: "Parallel AI deep research for competitive intelligence. Use when researching multiple competitors, market players, or data sources simultaneously. Generates structured research across 30 dimensions per competitor."
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

## Configuration

**Mode: Ultra** (not Ultra8x — Ultra gives better depth per task for 10 or fewer targets)

| Setting | Value |
|---------|-------|
| Processor | Ultra |
| Tasks | 1 per competitor (parallel, typically 5-10) |
| Output | Structured markdown per task |
| Search depth | Deep Research |
| Language | Match source materials (Russian for RU markets) |

## Workflow

### Step 1: Generate Research Prompt

Use the template at `references/competitive_research_template.md` as the base. Customize:

1. **Subject company** — Replace BCS references with the actual client
2. **Competitors list** — Update the 10-row competitor table with actual competitors
3. **Dimensions** — Keep all 30 dimensions unless the brief requires fewer
4. **Strategic context** — Update the target segment and repositioning goals
5. **Priority levels** — Set HIGH for direct competitors, MEDIUM for peripheral

### Step 2: Submit to Parallel AI

Via the Parallel AI MCP or web platform:

```
Task configuration:
- Type: Deep Research
- Processor: Ultra
- Parallel tasks: [number of competitors]
- Each task prompt: "Research [Competitor Name] across all 30 dimensions..."
- Attach the full prompt with dimension definitions
```

### Step 3: Collect Results

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

### Step 4: Parse into CSV

Merge all 10 reports into a single `competitive_analysis.csv` with:
- Rows = competitors (N)
- Columns = dimensions (30)
- Each cell = the research finding for that competitor × dimension

```python
import csv
import re
from pathlib import Path

reports_dir = Path("research_reports")
dimensions = [f"dimension_{i}" for i in range(1, 31)]

rows = []
for report_file in sorted(reports_dir.glob("[0-9][0-9]_*.md")):
    if report_file.name.startswith("00_"):
        continue  # skip summary
    text = report_file.read_text(encoding="utf-8")
    row = {"file": report_file.name}
    # Parse numbered dimensions from structured report
    for i in range(1, 31):
        pattern = rf'{i}\.\s*\*\*\w+\*\*\s*[—–-]\s*(.*?)(?=\n\d+\.\s*\*\*|\n##|\Z)'
        match = re.search(pattern, text, re.DOTALL)
        row[f"dim_{i}"] = match.group(1).strip() if match else ""
    rows.append(row)

with open("competitive_analysis.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["file"] + [f"dim_{i}" for i in range(1, 31)])
    writer.writeheader()
    writer.writerows(rows)
```

### Step 5: Synthesize into Summary

Create `research_reports/00_competitive_intelligence_summary.md` with:
- Cross-competitor comparison tables
- Archetype map (who occupies which territory)
- Affluent offering gap analysis
- White space identification for the client

## 30 Dimension Framework

### A. Identification (3)
1. competitor_name, 2. competitor_type, 3. parent_company

### B. Brand & Positioning (5)
4. brand_essence, 5. brand_positioning, 6. brand_archetype, 7. brand_image, 8. tone_of_voice

### C. Communication & Channels (4)
9. communication_channels, 10. social_media_presence, 11. content_and_education, 12. key_messages

### D. Product & Service (5)
13. product_range, 14. tariff_plans, 15. advisory_model, 16. affluent_offering, 17. unique_features

### E. Affluent Deep Dive (3)
18. affluent_entry_threshold, 19. affluent_service_model, 20. affluent_brand_communication

### F. Digital Experience (3)
21. app_name_and_rating, 22. platform_features, 23. digital_ux_reputation

### G. Ecosystem & Integration (2)
24. ecosystem_integration, 25. loyalty_program

### H. Market Position (4)
26. market_share_data, 27. target_audience, 28. competitive_advantages, 29. competitive_weaknesses

### I. Source Attribution (1)
30. sources

## Quality Rules

- **Ultra mode** gives deeper search per task than Ultra8x (which optimizes for throughput)
- Cross-reference: 2-3 sources per factual claim minimum
- Recency: current year data preferred, flag vintage explicitly
- Verbatim quotes: include actual slogans in «кавычки»
- Gap documentation: absence of data IS data — state "Информация не найдена"
- No hallucination: if uncertain, say so
