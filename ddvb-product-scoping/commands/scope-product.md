---
description: "Scope a product from brainstorming materials to blueprint + one-pager"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Agent, WebSearch, WebFetch
argument-hint: "[path-to-transcript-or-notes]"
---

# Product Scoping Pipeline

Take brainstorming transcripts, call recordings, meeting notes, or raw ideas and produce a complete product scope: research synthesis, technical blueprint, and executive one-pager.

## Inputs

Accept any combination of:
- Audio files (.m4a, .mp3, .wav) — transcribe first using faster_whisper (large-v3, CPU, int8)
- Text transcripts (.txt)
- Meeting notes or brainstorming docs (.md)
- Existing specs or PRDs
- User's verbal description

If `$ARGUMENTS` is provided, read the file at that path. Otherwise, ask what materials the user has.

## Pipeline

### Phase 1: Transcription (if audio)

If the input is an audio file:
1. Transcribe using faster_whisper large-v3 (CPU, int8, beam_size=5, vad_filter=True)
2. Save transcript as `{filename}.transcript.txt` next to the audio file
3. Proceed with the transcript text

### Phase 2: Research Synthesis

Read the transcript/notes and produce a structured synthesis following this template:

1. **Research Overview** — methodology, participants, timeframe
2. **Key Findings** (5-8 max) — each with:
   - Finding statement (one sentence)
   - Evidence (verbatim quotes with timestamps/attribution)
   - Frequency, Impact, Confidence level
3. **Product Scoping Summary** — if multiple products emerge, create a comparison table separating them clearly by: type, market, user, deliverable, revenue model, tech stack, status, priority, legal entity, investment
4. **Opportunity Areas** — unmet needs, gaps, new capabilities
5. **Recommendations** — specific, actionable, prioritized
6. **Open Questions** — gaps needing further investigation

Save to the same directory as the input: `{input-name}-synthesis.md`

Ask the user: "The synthesis identifies [N] products/opportunities. Which should I blueprint?" Wait for confirmation.

### Phase 3: Technical Blueprint

For each approved product, generate a 14-section blueprint using the template in `${CLAUDE_PLUGIN_ROOT}/skills/product-scoping/references/blueprint-template.md`.

Key rules:
- Supabase self-hosted (Docker Compose) unless user says otherwise
- LLMs: API-based by default (Anthropic Claude, OpenAI, Gemini)
- No n8n — use LangGraph + FastAPI for agent orchestration
- Check if the brand-strategy plugin (`~/.claude/plugins/brand-strategy/`) exists and can be leveraged
- Hosted abroad (EU/US) unless user specifies otherwise
- Include Mermaid diagrams for architecture and flowcharts
- All 14 sections must be present — no shortcuts

Save as `{product-name}-blueprint.md` in `Product/Specifications/` or the user's preferred location.

### Phase 4: Executive One-Pager

For each blueprinted product, generate a branded HTML one-pager.

Apply DDVB TECH brand guidelines:
- Use the `/ddvb-brand-guidelines` skill if available
- Black header (#0D0D0D), gold accents (#FDB71C), sharp corners (0 border-radius)
- Inter font (web-safe fallback for Atyp)
- Include the DDVB TECH logo: look for it at `Dev-Platform/web-apps/ddvb-marketing-app/public/logo.png` and reference relatively (copy to output directory if needed)
- Product names stay in English even in Russian versions

One-pager structure:
1. **Header** — product badge, product name, subtitle, logo
2. **Stat bar** (gold) — 5 key metrics
3. **Vision** — 3-4 sentences explaining the product
4. **Architecture/Pipeline visualization** — stages or product model cards
5. **Two columns** — tech stack + key advantage (or business model)
6. **Investment table** — effort, infrastructure, costs, ROI
7. **Decision box** (black) — 4 numbered next steps
8. **Footer** — DDVB TECH, date, confidentiality notice

Generate both EN and RU versions. Russian version: translate all content EXCEPT product names.

Save as `DDVB-TECH-{ProductName}-OnePager.html` and `DDVB-TECH-{ProductName}-OnePager-RU.html`.

### Phase 5: Summary

Present to user:
- Links to all generated files
- Key decisions that need their input
- Suggested next steps

## Important

- Never skip the synthesis phase — it grounds everything in evidence
- Always separate distinct products into distinct blueprints
- Quote original speakers verbatim in the synthesis (with attribution)
- The blueprint must be self-contained: a developer reading only this document should be able to build the product
- One-pagers are for leadership — concise, visual, decision-oriented
