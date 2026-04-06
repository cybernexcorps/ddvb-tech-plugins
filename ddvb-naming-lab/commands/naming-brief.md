---
name: naming-brief
description: "Phase 1: Extract materials, run two-layer naming research, produce copywriter brief."
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Agent, WebSearch, WebFetch
argument-hint: "[path-to-materials-or-client-name]"
---

# Phase 1: Naming Brief

Generate a structured copywriter naming brief from client materials and competitive research.

## Step 1: Extract Source Materials

1. **Locate documents** — Find all PDFs, PPTX, DOCX, and brief documents in the working directory or provided path
2. **Extract data** — Use `pdfplumber` for PDFs, `python-pptx` for PPTX, `python-docx` for DOCX. Use parallel agents for 3+ documents.
3. **Structure findings** — Client overview, current brand status, positioning (if exists), competitors, target audience, reason for renaming

If `$ARGUMENTS` is provided, treat it as client name or path to materials. Otherwise ask: "What's the client name? Where are the source materials?"

## Step 2: Identify Industry & Select Research Dimensions

1. **Auto-detect industry** from extracted materials
2. **Read** `references/research-dimensions-naming.md` for the dimension catalog
3. **Present** 17 fixed (Layer 1) + linguistic audit (Layer 2) + industry-specific variable dimensions
4. **Get confirmation** before proceeding

## Step 3: Layer 1 — Competitive Name Research (Parallel AI)

Run per-competitor research via Parallel AI Ultra:
- 1 task per competitor (up to 10)
- All confirmed dimensions per task
- Focus on NAME-SPECIFIC insights

Save to `research_reports/01_[name].md` through `research_reports/10_[name].md`.

Synthesize into:
- `research_reports/00_naming_landscape_summary.md` — cross-competitor synthesis
- `research_reports/naming_territory_map.md` — occupied vs free semantic territories

## Step 4: Layer 2 — Linguistic Audit

Run market-wide linguistic research:
- Phonetic landscape per target language (default: RU + EN, ask for more)
- Domain/social/trademark landscape
- Naming convention patterns for the industry

Save to:
- `research_reports/linguistic_audit_ru.md`
- `research_reports/linguistic_audit_en.md`
- `research_reports/availability_landscape.md`
- `research_reports/naming_constraints.md`

## Step 5: Assemble Naming Brief

Using the naming-brief-assembly skill, produce `NAMING_BRIEF_FOR_COPYWRITER.md` with all 10 mandatory sections:

1. Project context
2. Materials assessment
3. Strategic recommendation
4. Competitive name map
5. Semantic field (7-10 concepts)
6. Naming strategy recommendation (from `references/naming-strategies.md`)
7. Selection criteria (mandatory + desired)
8. Taboo list
9. Inspiration facts
10. Expected deliverables

## Step 6: Gate Check

Present to user:
1. Naming brief highlights
2. Recommended naming strategies
3. Semantic field summary
4. **Ask:** "Ready to proceed to seed generation (/naming-generate), or adjustments needed?"

Only proceed after user confirms.

## Important

- Respond in the same language as source materials
- The brief is an INTERNAL document for the copywriter — not client-facing
- Use Parallel AI Ultra for research depth
- Always confirm dimensions and target languages with the user before research
- Document which positioning direction was chosen (if from prior brand strategy work)
