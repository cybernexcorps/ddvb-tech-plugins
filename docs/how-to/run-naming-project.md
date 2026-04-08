# How to Run a Naming Project

Produce a copywriter naming brief, generate seed candidates, and evaluate the final long-list.

## When to Use

A client needs a new name — rebranding, new product, or new company. You have positioning materials or a brief.

## What You Need

- Client source documents (positioning, brand manifesto, communication strategy — PDF/PPTX/DOCX)
- A Parallel AI account (for competitive name research)
- A copywriter to produce the long-list between Phase 2 and Phase 3

## The Full Pipeline

```
Phase 1: Brief → Phase 2: Seeds → [Copywriter works] → Phase 3: Evaluate → Phase 4: Present
```

Note the pause between Phase 2 and Phase 3 — the copywriter produces the long-list externally. This pipeline typically spans days, not a single session.

## Steps

### Phase 1: Naming Brief

```
/ddvb-brand-naming:naming-brief
```

**What happens:**

1. Claude extracts text from all source documents
2. Runs two-layer research:
   - **Layer 1:** Competitive name analysis — per-competitor via Parallel AI (names, archetypes, semantic territories, naming patterns)
   - **Layer 2:** Linguistic audit — phonetic patterns per language (default RU + EN), domain/social/trademark landscape
3. Asks which target languages to check (Russian + English are always included)
4. Produces `NAMING_BRIEF_FOR_COPYWRITER.md`

**The brief contains:**
- Materials assessment (what's useful for naming)
- Strategic recommendation (which positioning direction to name from)
- Competitive name map (what's occupied, what to avoid)
- Semantic field (7-10 core concepts, prioritized)
- Naming strategy recommendation (2-3 from: descriptive, metaphorical, coined, acronym, portmanteau, founder, geographic)
- Selection criteria (mandatory + desired)
- Taboo list (names, patterns, sounds to avoid)
- Inspiration facts

### Phase 2: Seed Generation

```
/ddvb-brand-naming:naming-generate
```

**What happens:**

1. Claude reads the brief and recommends 2-3 naming strategies
2. **You confirm** which strategies to focus on
3. Claude generates 30-50 seed candidates, categorized by strategy
4. Runs automated availability checks (domain, social handles, trademark search)
5. Produces `seeds/naming_seeds.md`

**Hand off to the copywriter:**
- Send them `NAMING_BRIEF_FOR_COPYWRITER.md` (the structured brief)
- Send them `seeds/naming_seeds.md` (AI seeds for inspiration)
- The copywriter returns a long-list of 50-80 candidates

### Phase 3: Evaluate

```
/ddvb-brand-naming:naming-evaluate [path-to-long-list]
```

**What happens:**

1. Claude imports the copywriter's long-list
2. Proposes evaluation weights (you can adjust for project context)
3. Runs automated pre-screen: domain, trademark, phonetic checks
4. Scores each surviving candidate across 10 dimensions
5. Produces a ranked short-list (top 8-10)
6. **You select** 3-5 finalists

### Phase 4: Client Presentation (Optional)

```
/ddvb-brand-naming:naming-present
```

Generates a DDVB-branded PPTX with the final candidates — one slide per name with strengths, availability, and recommendation.

## Output Files

```
project-dir/
├── extracted/                          # Source material text
├── research_reports/
│   ├── 01-10_*.md                      # Per-competitor name research
│   ├── naming_territory_map.md         # Occupied vs free territories
│   ├── linguistic_audit_ru.md          # Russian phonetic landscape
│   ├── linguistic_audit_en.md          # English phonetic landscape
│   └── availability_landscape.md       # Domain/social/trademark
├── NAMING_BRIEF_FOR_COPYWRITER.md      # → Send to copywriter
├── seeds/naming_seeds.md               # → Send to copywriter
├── evaluation/
│   ├── scoring_matrix.md               # Full scoring table
│   ├── short_list.md                   # Top 8-10
│   └── final_candidates.md             # Your selected 3-5
└── {CLIENT}_NAMING_PRESENTATION.pptx   # Client deck (optional)
```

## Tips

- **The brief is internal.** It goes to the copywriter, not the client. The client sees the final presentation (Phase 4).
- **Seed generation is inspiration, not the answer.** The AI generates 30-50 seeds to get the copywriter's creative engine running — the real long-list comes from human creativity.
- **Availability checks are preliminary.** Domain and trademark checks use free tools. Always recommend a professional attorney search before filing.
- **Language matters.** If the brand will operate in Kazakh, Czech, or German markets, add those languages in Phase 1 — phonetic and connotation checks are only as good as the languages you specify.
