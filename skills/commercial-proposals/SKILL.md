---
name: commercial-proposals
description: >
  This skill should be used when the user asks to "create a proposal", "write a commercial proposal",
  "generate a КП", "make a client proposal", "build a presale deck", or needs to produce a client-facing
  commercial document from call transcripts, meeting notes, or sales context. Also triggers when user
  mentions "Presales" alongside document creation, or references an existing proposal as a template.
version: 0.1.0
---

# Interactive Commercial Proposals

Generate polished, interactive HTML commercial proposals for DDVB TECH clients. Proposals are self-contained single-file HTML documents with scroll animations, interactive navigation, and DDVB branding.

## Proposal Structure

Every proposal follows this section sequence:

| # | Section | Content |
|---|---------|---------|
| Cover | Full-screen dark | Logo, "КОММЕРЧЕСКОЕ ПРЕДЛОЖЕНИЕ" badge, client-specific title, subtitle, meta (date, author) |
| 01 | О вашем бизнесе | Client profile cards, pain points as quoted cards from transcripts |
| 02-N | Solution sections | One per solution direction — how it works (step cards), key features (capability cards), expected result |
| N+1 | Архитектура | Tech stack visualization (CSS diagram, not image), integration points |
| N+2 | План работ | Timeline with phase cards, durations, milestones, decision points |
| N+3 | Стоимость | Pricing tiers or phases, ROI comparison table, savings highlight |
| N+4 | Почему мы | 4 competency cards (stack, multilingual, industry, partnership) |
| CTA | Full-screen dark | "Давайте обсудим" + contact details + next step |

## Interactive Requirements

These are non-negotiable — every proposal must include:

### Navigation
- Sticky sidebar or top nav with section numbers
- Active section highlight (IntersectionObserver)
- Smooth scroll on click
- Progress indicator (scroll percentage)

### Animations (IntersectionObserver-based)
- Cards fade + slide up on scroll entry (translateY(30px) + opacity: 0 → visible)
- Number counters animate from 0 to target value
- Staggered reveal: cards in a grid appear with 100ms delay between each
- Section titles slide in from left

### Interactive Elements
- Expandable cards (click to reveal details)
- Tab switchers for solution variants or pricing
- ROI calculator with sliders (if applicable)
- Hover: cards lift with shadow transition

### Technical
- Single self-contained HTML (inline CSS + JS)
- No external deps except Google Fonts (Inter)
- `@media print` for clean A4 output
- 60fps animations (transform + opacity only)
- IntersectionObserver for scroll triggers (threshold: 0.15)

## Visual Design

See `references/proposal-design-system.md` for the complete CSS variable system, component patterns, and layout rules.

Key rules:
- Sharp corners (border-radius: 0) on all structural elements
- Gold (#FDB71C) as accent only — never background for large text areas
- Section pages: white bg, 50px padding, gold section number, black title, 48px gold divider
- Cards: #F5F5F5 bg, 3px gold left border, 24px padding
- Cover + CTA: full dark (#0D0D0D)
- Logo: actual PNG from `Dev-Platform/web-apps/ddvb-marketing-app/public/logo.png`

## Content Rules

- All content in Russian
- Technical terms stay in English (API, AI, CRM, etc.)
- Use client's own terminology from transcripts
- Pain points: verbatim quotes from calls (most powerful content)
- Every solution maps to a stated pain point
- Tone: confident, direct, professional — not corporate
- Short sentences, active voice

## DDVB TECH Capabilities (for solution mapping)

Reference when mapping solutions to pain points:

| Capability | Description |
|------------|-------------|
| Media Comment Writer | AI generates CEO/expert comments for media requests in minutes |
| Case Study Generator | Automated case study creation from project data |
| SEO Content Agent | Claude + Perplexity + Yandex WordStat for SEO articles |
| Article Rewriter | Multi-model content adaptation |
| DocuFlow | Document automation for agencies (from custdev) |
| Custom AI Agents | LangChain/LangGraph agents for specific business workflows |
| Analytics Dashboards | Data visualization + AI insights (Text-to-SQL, RFM, etc.) |
| n8n Automation | Workflow automation for repetitive tasks |

## References

- `references/proposal-design-system.md` — CSS variables, component patterns, animation code
- `references/proposal-js-template.md` — JavaScript for IntersectionObserver, counters, navigation
