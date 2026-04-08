# How to Run a Brand Strategy Project

Run the full 4-phase brand repositioning pipeline: Spec → Plan → Review → Execute.

## When to Use

A client needs brand repositioning, and you have their source materials (brand health tracker, research reports, competitor briefs, strategy decks).

## What You Need

- Client source documents (PDF, PPTX) in a working directory
- A Parallel AI account (for competitive research)
- 2-4 hours across all phases (research takes ~15 minutes, the rest is interactive)

## Steps

### Phase 1: Spec

```
/ddvb-brand-strategy:brand-spec
```

**What happens:**

1. Claude extracts text from all PDFs and PPTX files
2. Identifies the client's industry and proposes research dimensions:
   - 17 fixed universal dimensions (identification, brand, communication, market position)
   - Variable dimensions from the matched industry preset
3. **You confirm** the dimension set — add, remove, or customize
4. Claude launches Parallel AI Ultra (one task per competitor, up to 10)
5. Waits ~10-15 minutes for research to complete
6. Produces `analysis/spec_summary.md`

**Gate check:** Claude shows the spec summary, archetype map, and positioning hypotheses. You choose which direction to develop.

### Phase 2: Plan

```
/ddvb-brand-strategy:brand-plan
```

**What happens:**

Claude develops the chosen hypothesis into:
- **SWOT analysis** with 7-9 factors per quadrant
- **Competitive landscape** — positioning map, competitor matrix
- **Brand platform** — mission, values, archetype formula, Big Idea (3-5 alternatives)
- **Communication platform** — key messages, slogans, channel matrix, content pillars
- **Visual identity concept** — colors, typography, graphic device, photo style

**Gate check:** Claude presents the Big Idea alternatives. You pick one.

### Phase 3: Review

```
/ddvb-brand-strategy:brand-review
```

Claude validates coherence across all deliverables — mission, values, archetype, Big Idea, communication, and visual identity must form a consistent system.

### Phase 4: Execute

```
/ddvb-brand-strategy:brand-execute
```

Claude generates:
- Matplotlib figures (SWOT diagrams, positioning maps, archetype charts)
- DDVB-branded PPTX presentation with all deliverables

### Or run everything at once

```
/ddvb-brand-strategy:brand-full
```

This runs all 4 phases sequentially with gate checks between each. You can stop at any phase.

## Output Files

```
project-dir/
├── extracted/                          # Source material text
│   ├── 01_brand_health.md
│   └── 02_competitor_brief.md
├── research_reports/                   # Parallel AI results
│   ├── 00_competitive_intelligence_summary.md
│   ├── 01_competitor_name.md
│   └── ...
├── competitive_analysis.csv            # All dimensions x competitors
├── analysis/
│   ├── spec_summary.md                 # Phase 1 output
│   ├── swot_competitive.md             # Phase 2
│   ├── brand_platform.md               # Phase 2
│   ├── communication_platform.md       # Phase 2
│   └── visual_identity.md              # Phase 2
├── figures/                            # Phase 4
│   └── *.png
└── {CLIENT}_Brand_Strategy_DDVB.pptx   # Final presentation
```

## Tips

- **Dimension confirmation matters.** Don't skip the dimension selection step. If the default preset doesn't fit, add dimensions from other presets or create custom ones.
- **Research takes 10-15 minutes.** Parallel AI Ultra runs one task per competitor. Wait for all tasks to complete before synthesis.
- **Big Idea is the key gate.** Phase 2 produces 3-5 Big Idea alternatives. The one you choose shapes everything downstream — take your time here.
- **You can re-run individual phases.** If Phase 2 doesn't hit the mark, run `/brand-plan` again with different direction — it reads the same spec.
