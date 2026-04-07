---
name: brand-full
description: "Run all 4 phases end-to-end: spec (with Parallel AI Ultra research) → plan → review → execute. Pause for user input between phases."
---

# Full Brand Strategy Workflow

Run the complete brand repositioning pipeline with parallel competitive research.

## Pipeline

```
/brand-spec                          /brand-plan                    /brand-review              /brand-execute
┌──────────────────────┐     ┌──────────────────────┐     ┌─────────────────┐     ┌──────────────────┐
│ 1. Extract PDFs      │     │ 1. SWOT analysis     │     │ 1. Coherence    │     │ 1. Font module   │
│ 2. Parallel AI Ultra │────▶│ 2. Brand platform    │────▶│    matrix       │────▶│ 2. Generate figs │
│    (N competitors)   │     │ 3. Comms platform    │     │ 2. Cross-block  │     │ 3. Build PPTX    │
│ 3. Synthesize spec   │     │ 4. Visual identity   │     │ 3. Brief check  │     │ 4. Verify        │
└──────────┬───────────┘     └──────────┬───────────┘     └────────┬────────┘     └──────────────────┘
           │                            │                          │
     [User picks                  [User confirms              [User approves
      hypothesis]                  Big Idea]                   or fixes]
```

## Execution

### Gate 0: Prerequisites Check
Before starting, verify:
- Source materials exist (PDFs, PPTX in working directory)
- Python packages available: `pdfplumber`, `python-pptx`, `matplotlib`, `numpy`
- Parallel AI access (MCP or web platform)

### Gate 1: Spec → Plan
1. Execute `/brand-spec` (includes Parallel AI Ultra research on all competitors)
2. Present: spec summary, archetype map, competitor gaps
3. **STOP:** "Which hypothesis? Or propose your own."
4. Proceed only after user confirms

### Gate 2: Plan → Review
1. Execute `/brand-plan` (SWOT, platform, comms, visual)
2. Present: Big Idea + alternatives, brand wheel, values
3. **STOP:** "Does the Big Idea work? Adjustments?"
4. Proceed only after user confirms

### Gate 3: Review → Execute
1. Execute `/brand-review` (coherence, completeness, distinctiveness)
2. Present: review report with scores
3. **STOP:** "Ready to generate? Any fixes?"
4. Proceed only after user approves

### Final Delivery
1. Execute `/brand-execute` (figures + PPTX)
2. Present: file path, size, slide count
3. Remind: "Export to PDF via PowerPoint for final delivery"

## Parallel AI Configuration

| Parameter | Value |
|-----------|-------|
| Processor | **Ultra** |
| Mode | Deep Research |
| Tasks | 1 per competitor (parallel, typically 5-10) |
| Dimensions | 30 per competitor |
| Language | Match source materials |

**Why Ultra, not Ultra8x:** Ultra provides deeper per-task research with more source verification. Ultra8x optimizes for throughput (50+ tasks) but sacrifices depth. For up to ~10 competitors × 30 dimensions, Ultra hits the sweet spot.

## Important

- Never skip a gate — user input shapes the strategy
- If user says "skip to [phase]", check prerequisites exist
- Track progress: show active phase and completed work
- Total timeline: ~2-4 hours for full pipeline (most time in Spec research)
