---
name: product-scoping
description: >
  This skill should be used when the user asks to "scope a product", "turn brainstorming into a spec",
  "create a blueprint from notes", "synthesize research into a product plan", "write a technical blueprint",
  or provides brainstorming transcripts, call recordings, or meeting notes that need to be turned into
  structured product documentation. Also triggers when the user mentions "one-pager" alongside product planning.
version: 0.1.0
---

# Product Scoping

Transform raw brainstorming materials into structured product documentation: research synthesis, 14-section technical blueprint, and executive one-pagers.

## Workflow

1. **Ingest** — accept audio (transcribe with faster_whisper), transcripts, notes, or verbal input
2. **Synthesize** — extract findings, separate products, identify opportunities
3. **Blueprint** — generate a 14-section technical blueprint per product (see `references/blueprint-template.md`)
4. **One-Pager** — generate DDVB TECH-branded HTML one-pagers (EN + RU)

## Synthesis Method

Follow thematic analysis:
- Extract key observations, verbatim quotes, behaviors, pain points, positive signals
- Group into themes, count frequency, assess impact
- Priority matrix: High freq + High impact = top priority
- Separate distinct products into comparison tables
- 5-8 findings max — quality over quantity

## Blueprint Format

Use the 14-section template from `references/blueprint-template.md`. Every section required:

1. Product Design Requirements (PDR)
2. Design Decisions (ADR format)
3. Tech Stack
4. App Flowchart (Mermaid)
5. Technical Design (interfaces, data models, file structure)
6. Project Rules
7. Frontend Guidelines
8. Backend Guidelines
9. Optimised Code Guidelines
10. Implementation Plan (phased)
11. Testing Strategy
12. Observability
13. Rollout Strategy
14. Security Checklist

Default tech constraints (override if user specifies):
- Supabase self-hosted
- LLMs API-based (Claude, OpenAI, Gemini)
- No n8n — LangGraph + FastAPI
- Hosted abroad (EU/US)

## One-Pager Format

Self-contained HTML with DDVB TECH branding:
- Black header, gold (#FDB71C) accents, sharp corners
- Logo from `Dev-Platform/web-apps/ddvb-marketing-app/public/logo.png`
- 5 key stats in gold bar
- Vision, architecture, tech + advantage columns, investment table, decision box
- EN and RU versions (product names stay in English)

## References

- `references/blueprint-template.md` — full 14-section blueprint prompt
- `references/one-pager-structure.md` — HTML one-pager component reference
