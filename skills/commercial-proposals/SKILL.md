---
name: commercial-proposals
description: >
  This skill should be used when the user asks to "create a proposal", "write a commercial proposal",
  "generate a КП", "make a client proposal", "build a presale deck", or needs to produce a client-facing
  commercial document from call transcripts, meeting notes, or sales context. Also triggers when user
  mentions "Presales" alongside document creation, or references an existing proposal as a template.
version: 0.2.0
---

# Commercial Proposals — Website Format

Generate commercial proposals that deploy directly to the DDVB TECH website at `ddvb.tech/{locale}/proposals/{slug}`. Proposals use a **dual-layer architecture**: structured TypeScript data (for CTA, metadata, SEO) + raw HTML body (for full creative control over the main content).

## Output Format — Two Files

Every proposal produces exactly two deliverables:

### 1. TypeScript Data Entry (for `src/data/proposals.ts`)

A `Proposal` object added to the `proposals` array. Contains structured fields: hero, stats, painPoints, solutions, pricing, timeline, cta. See `references/proposal-typescript-schema.md` for full interface definitions and examples.

### 2. HTML Body File (`src/data/proposals/{slug}-body.html`)

Raw HTML rendered via `dangerouslySetInnerHTML`. Uses CSS classes from `proposal.css` — dark theme, `var(--gold)` accents, centered cover, `.reveal` animations, `.card-dark`/`.card-light` cards, `.tbl` tables, `.timeline` with `.tl-item` steps, `.callout` boxes, `.divider` sections with gold background. See `references/proposal-html-patterns.md` for the full pattern catalog.

**This is NOT a standalone HTML file.** No `<html>`, `<head>`, `<style>`, or `<script>` tags. No inline CSS. No inline JavaScript. The page component (`page.tsx`) loads `proposal.css` and injects the IntersectionObserver reveal script automatically.

## Architecture — How It Works on the Website

```
proposals.ts (data)          {slug}-body.html (content)
       │                            │
       ▼                            ▼
  page.tsx ─── dangerouslySetInnerHTML ───▶ .proposal-page div
       │
       ▼
  ProposalCtaSection (React component) ── renders CTA from data
       │
       ▼
  <script> IntersectionObserver ── animates .reveal elements
```

- `page.tsx` loads proposal data via `getProposalBySlug(slug)`
- The HTML body is rendered inside a `<div class="proposal-page">`
- The CTA section is rendered by a separate React component (NOT in the HTML body)
- The reveal animation script is injected by the page component
- `proposal.css` is imported by the page — all CSS classes are available

## HTML Body Structure

The HTML body follows this section sequence. Do NOT include a CTA section in the HTML — it's handled by the React component.

| # | Section | HTML Pattern |
|---|---------|-------------|
| Cover | `<header class="cover" id="top">` | Logo, kicker, `<h1>` with `<strong>` for gold, lead, meta, scroll indicator |
| 01 | О вашем бизнесе | `<section id="business">` with `.sec-n`, `.sec-t`, `.sec-s`, `.stats`, `.cards .card-light`, `.callout` |
| Divider | Gold separator | `<div class="divider">` with `<h2>` and `<p>` |
| 02-N | Solution sections | `<section>` with `.flow`, `.cards .card-dark`, `.card-num`, `.callout` |
| N+1 | Архитектура | `<section>` with `.tbl` table, `.callout` |
| N+2 | Стоимость | `<section id="pricing">` with `.tbl`, pricing `.cards`, highlighted `.callout` |
| N+3 | План работ | `<section id="plan">` with `.timeline`, `.tl-item` |
| N+4 | Почему мы | `<section id="why">` with `.cards .card-dark`, `.checks` |

## Visual Design System

**Dark cinematic theme.** NOT the white-on-gold one-pager format.

### CSS Variables (defined by proposal.css)

```
--gold: #FDB71C          --gold-10: rgba(253,183,28,0.10)
--gold-20: rgba(253,183,28,0.20)   --gold-40: rgba(253,183,28,0.40)
--black: #0A0A0A          --ink: #141414
--surface: #1A1A1E        --chalk: #FAFAF8
--cream: #F2F0EB          --stone: #888
--mist: #bbb
--display: 'Atyp Display', Georgia, serif
--text: 'Atyp Text', -apple-system, sans-serif
```

### Key Design Rules

- **Dark background** throughout — `var(--black)` body, `var(--surface)` card backgrounds
- **Atyp fonts** — Display for headings (light 300, bold 700), Text for body
- **Gold accents** — section labels, stat values, card numbers, table headers, timeline dots, callout borders
- **Sharp corners** — no border-radius on structural elements
- **Reveal animations** — `.reveal` class on all content blocks, `.reveal-d1` through `.reveal-d4` for staggered delays
- **Cover** — centered layout, pulsing radial gradient, scroll indicator mouse
- **Cards** — bottom gold 2px border, hover lift 4px, `.card-dark` (surface bg) or `.card-light` (cream bg)
- **Tables** — dark headers with gold text, hover row highlight
- **Dividers** — gold background, giant "D D V B" watermark behind, contrasting black text
- **No images in cover** — logo via `<img src="/logo.png">`, no background images

### Typography

- Section numbers: 10px, weight 600, letter-spacing 4px, uppercase, gold
- Section titles: clamp(28px, 3.5vw, 38px), weight 300, chalk color, Atyp Display
- Section subtitles: 15px, weight 300, stone color, max-width 580px
- Card titles: 14px, weight 700, Atyp Text
- Card body: 13px, stone color, line-height 1.55
- Cover h1: clamp(36px, 5vw, 56px), weight 300, Atyp Display — `<strong>` for gold emphasis

## Content Rules

- All content in Russian
- Technical terms stay in English (API, AI, CRM, LLM, etc.)
- Use client's own terminology from transcripts
- Pain points: verbatim quotes from calls (most powerful content)
- Every solution maps to a stated pain point
- Tone: confident, direct, professional — not corporate
- Short sentences, active voice
- HTML entities for special characters: `&mdash;`, `&laquo;`, `&raquo;`, `&times;`, `&middot;`, `&#8381;` (ruble sign)

## Structured Data Fields

The TypeScript `Proposal` object provides structured data for programmatic use. Key fields:

- **slug** — URL slug (kebab-case, e.g., `"adapter"`)
- **locale** — `"ru"` or `"en"` (usually `"ru"`)
- **hero** — kicker, title (with `**bold**` for gold text in Markdown), subtitle, meta items
- **stats** — 4 key metrics (value + label)
- **painPoints** — title + items with icon, heading, quote, detail, hours
- **solutions** — title, subtitle + items with number, name, description, painSolved, features
- **pricing** — title + tiers with name, price, period, features, highlighted flag
- **timeline** — title + phases with name, duration, items
- **cta** — title (with `**bold**`), subtitle, acceptLabel, discussLabel, contactGrid

## DDVB TECH Capabilities (for solution mapping)

Reference when mapping solutions to pain points:

| Capability | Description |
|------------|-------------|
| Media Comment Writer | AI generates CEO/expert comments for media requests in minutes |
| Case Study Generator | Automated case study creation from project data |
| SEO Content Agent | Claude + Perplexity + Yandex WordStat for SEO articles |
| Article Rewriter | Multi-model content adaptation and translation |
| DocuFlow | Document automation for agencies |
| Custom AI Agents | LangChain/LangGraph agents for specific business workflows |
| Analytics Dashboards | Data visualization + AI insights (Text-to-SQL, RFM, etc.) |
| n8n Automation | Workflow automation for repetitive tasks |
| Tender Automation | AI-powered tender document preparation |

## References

- `references/proposal-typescript-schema.md` — Full TypeScript interfaces and complete data example
- `references/proposal-design-system.md` — CSS class catalog with usage patterns
- `references/proposal-html-patterns.md` — Copy-paste HTML patterns for every component
