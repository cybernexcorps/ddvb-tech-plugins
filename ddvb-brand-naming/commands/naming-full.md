---
name: naming-full
description: "Run all naming phases end-to-end: brief (with research), seed generation, evaluation, and optional client presentation."
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Agent, WebSearch, WebFetch
argument-hint: "[path-to-materials-or-client-name]"
---

# Full Naming Pipeline

Run all 4 phases of the naming workflow with gate checks between each.

## Phase 1: Naming Brief (`/naming-brief`)

1. Extract source materials (PDFs, PPTX, DOCX)
2. Identify industry, select research dimensions, confirm with user
3. Layer 1: Competitive name research (Parallel AI Ultra)
4. Layer 2: Linguistic audit (phonetics, availability landscape)
5. Assemble copywriter naming brief

**Gate:** User confirms brief before proceeding.

## Phase 2: Seed Generation (`/naming-generate`)

1. Analyze brief, recommend 2-3 naming strategies
2. User confirms strategy focus
3. AI generates 30-50 categorized seed candidates
4. Automated availability checks (domain, social, trademark)
5. Deliver seed list to copywriter alongside brief

**Gate:** User confirms seeds are ready for copywriter handoff.

**⏸ PAUSE:** Wait for copywriter to return long-list (50-80 candidates). This is an external dependency — the copywriter works independently. Resume when user provides the long-list.

## Phase 3: Evaluation (`/naming-evaluate`)

1. Import copywriter's long-list
2. Review and confirm evaluation weights
3. Automated pre-screen (domain, trademark, phonetic)
4. Score all candidates across 10 weighted dimensions
5. Produce ranked short-list (top 8-10)

**Gate:** User selects final 3-5 candidates.

## Phase 4: Client Presentation (`/naming-present`) — Optional

1. Prepare candidate presentation content
2. Generate DDVB-branded PPTX (12 slides)
3. Deliver for client meeting

**Gate:** User confirms deck is ready.

## Important

- Each phase has a gate check — never proceed without user confirmation
- Phase 2→3 has an EXTERNAL dependency (copywriter turnaround)
- The full pipeline typically spans days/weeks, not a single session
- If source materials include existing positioning/brand strategy, reference it — don't redo it
- All outputs in the same language as source materials (usually Russian)
