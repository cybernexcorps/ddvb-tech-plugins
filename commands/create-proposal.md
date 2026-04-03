---
description: "Generate an interactive commercial proposal from client data"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Agent, WebSearch, WebFetch
argument-hint: "[client-name-or-path-to-materials]"
---

# Interactive Commercial Proposal Generator

Generate a polished, interactive HTML commercial proposal for a prospective client, using DDVB TECH branding and data gathered from call transcripts, meeting notes, sales decks, and web research.

## Inputs

Accept any combination of:
- Call transcripts (.txt, .md)
- Audio recordings (.m4a, .mp3) — transcribe first
- Meeting notes or summaries
- Client's website URL (for research)
- Sales deck or brief (.md, .pptx)
- CRM notes or email threads
- User's verbal context about the deal

If `$ARGUMENTS` is provided, treat it as the client name or path to materials. Otherwise, ask: "Which client is this proposal for? What materials do you have?"

## Phase 0: Context Gathering

### Client Context
Extract or ask for:
- **Company name** (required)
- **Industry / vertical**
- **Key contacts** (names, roles)
- **Website URL** (for research)
- **Pain points** mentioned in calls/notes (use their exact words)
- **Budget range** (if known)
- **Timeline expectations**
- **Deal stage** (intro / discovery / evaluation / negotiation)

### Research
1. If a website URL is available, fetch and extract: company description, products/services, team, tech stack signals
2. Web search: `"[Company]" + industry context, recent news, competitors`
3. If transcripts provided: extract verbatim pain point quotes, decision criteria, objections, internal project names

### DDVB TECH Context
Know what we sell:
- AI-powered automation for creative and PR agencies
- Products: media comment writer, case study generator, SEO content agent, article rewriter
- Platform: n8n workflows + LangChain/LangGraph agents + Next.js web apps
- Delivery model: discovery → prototype → production (6-step implementation)
- Pricing: project-based or subscription ($499-$1,499/mo+ for platform access)

Map DDVB TECH capabilities to client's specific pain points.

## Phase 1: Proposal Structure

Generate an interactive multi-page HTML proposal with these sections:

### Cover Page (dark, full-screen)
- DDVB TECH logo (from `Dev-Platform/web-apps/ddvb-marketing-app/public/logo.png`)
- Tag: "КОММЕРЧЕСКОЕ ПРЕДЛОЖЕНИЕ" (gold badge)
- Title: "AI-автоматизация для **{Client Name}**"
- Subtitle: one sentence addressing their core need
- Meta: date, prepared by, version
- Footer: DDVB TECH brand

### 01 — О вашем бизнесе (About Your Business)
- Show we understand their world
- Client profile cards (industry, size, products, market)
- Pain points extracted from transcripts — use THEIR words in quotes
- Each pain point as a card with icon, quote, and time/cost impact

### 02-N — Solution Sections (one per solution direction)
For each proposed solution:
- Section title + subtitle explaining the approach
- "How it works" — 3-5 step flow (numbered cards)
- Key capabilities as feature cards (icon + title + 2-line description)
- Expected result / outcome card (highlighted)

### Architecture Section
- Visual tech stack diagram (HTML/CSS, not image)
- Integration points with client's existing systems
- Data flow description

### Timeline & Roadmap
- Phase cards with duration, deliverables, and milestones
- Visual timeline bar
- Key decision points marked

### Pricing
- Tier cards or phase-based pricing
- What's included in each tier
- ROI comparison table (current cost vs. with automation)
- "Экономия" (savings) highlight

### Почему мы (Why DDVB TECH)
- 4 competency cards (proven stack, multilingual, industry expertise, partnership approach)
- Client logos / social proof if available

### Call to Action (dark, full-screen)
- "Давайте обсудим" with contact details
- Clear next step
- QR code or meeting link (if provided)

## Phase 2: Interactive Features

The proposal MUST be interactive — not a static document:

### Navigation
- **Sticky sidebar or top nav** with section numbers — clicking scrolls to section
- **Progress indicator** showing how far the reader has scrolled
- **Smooth scroll** between sections

### Animations
- **Scroll-triggered reveals** — cards and sections fade/slide in as they enter viewport (use IntersectionObserver)
- **Number counters** — key metrics animate from 0 to target value on scroll
- **Hover effects** — cards lift with subtle shadow on hover
- **Active section highlight** in navigation

### Interactive Elements
- **Expandable cards** — click to reveal detailed description
- **ROI calculator** (if applicable) — sliders for input variables, live calculation of savings
- **Tab switchers** — for solution variants or pricing tiers
- **Timeline slider** — interactive phase exploration

### Technical Requirements
- **Single self-contained HTML file** — all CSS and JS inline
- **No external dependencies** except Google Fonts (Inter)
- **Print-friendly** — `@media print` styles that flatten to clean A4 pages
- **Responsive** — works on desktop and tablet (mobile not required but nice)
- **Smooth 60fps animations** — use `transform` and `opacity` only, no layout-triggering properties

## Phase 3: Visual Design

### DDVB TECH Brand System
```css
:root {
  --ddvb-gold: #FDB71C;
  --ddvb-black: #0D0D0D;
  --ddvb-white: #FFFFFF;
  --ddvb-gray-100: #F5F5F5;
  --ddvb-gray-200: #E8E8E8;
  --ddvb-gray-400: #AAAAAA;
  --ddvb-body-text: #2A2A2A;
  --ddvb-muted: #666666;
  --ddvb-sidebar: #111111;
}
```

### Design Rules
- **Sharp corners** (border-radius: 0) on structural elements — agency aesthetic
- **High contrast**: black on white, white on black, black on gold
- **Gold (#FDB71C) as accent only** — badges, borders, highlights, dividers. Never as large background for text
- **Section pages**: white background, 50px padding, section number in gold, title in black, gold divider bar (48px wide, 3px tall)
- **Cards**: #F5F5F5 background, 3px left border in gold, 24px padding
- **Cover page**: full dark (#0D0D0D), gold accents, large typography
- **CTA page**: full dark, centered, gold heading

### Typography
- **Headings**: Inter 700/800, tight letter-spacing
- **Body**: Inter 400, 1.6 line-height
- **Section numbers**: 11px, letter-spacing 3px, uppercase, gold, 700 weight
- **Section titles**: 30px, 700 weight, black

### Logo
- Use the actual DDVB TECH logo PNG from `Dev-Platform/web-apps/ddvb-marketing-app/public/logo.png`
- Copy to the output directory and reference as `ddvb-logo.png`
- Display at 56px in header, 80px on cover

## Phase 4: Content Language

- **All proposal content in Russian** (target market)
- Technical terms can stay in English (API, AI, LLM, CRM, etc.)
- Use the client's own terminology from transcripts
- Tone: confident, direct, professional — not corporate-speak
- Short sentences, active voice
- Pain points: quote the client verbatim (in Russian)

## Phase 5: Delivery

1. Save proposal as `{ClientName}_Commercial_Proposal.html` in the `Presales/` directory
2. Copy logo to `Presales/ddvb-logo.png` if not already there
3. Present to user with:
   - File path
   - Section summary (what's in each section)
   - Key assumptions made (flag for review)
   - Suggested follow-up actions

## Important

- The proposal must feel bespoke, not templated — reference specific client data throughout
- Pain points from transcripts are the most powerful content — use verbatim quotes generously
- Every solution section must map directly to a stated pain point
- Interactive features are non-negotiable — this is what differentiates from a PDF
- The HTML must be a single self-contained file (no external assets except the logo PNG and Google Fonts)
- Test that IntersectionObserver animations work correctly before delivering
