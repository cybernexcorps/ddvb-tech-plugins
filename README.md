# DDVB TECH Product Lab

A Claude plugin for end-to-end product scoping and interactive commercial proposal generation.

## Commands

| Command | Purpose |
|---------|---------|
| `/scope-product [path]` | Transform brainstorming materials into research synthesis, 14-section blueprint, and branded one-pagers (EN + RU) |
| `/create-proposal [client]` | Generate an interactive HTML commercial proposal from client call transcripts, meeting notes, and sales context |

## Skills

| Skill | Triggers on |
|-------|-------------|
| `product-scoping` | "scope a product", "create a blueprint", "synthesize research", brainstorming transcripts |
| `commercial-proposals` | "create a proposal", "write a КП", "build a presale deck", client proposal work |

## What It Does

### Product Scoping (`/scope-product`)

**Input:** Audio recordings, transcripts, meeting notes, or verbal descriptions

**Output:**
1. Transcription (if audio) via faster_whisper
2. Research synthesis with findings, evidence, and opportunity areas
3. 14-section technical blueprint per product identified
4. DDVB TECH-branded HTML one-pagers (EN + RU versions)

### Commercial Proposals (`/create-proposal`)

**Input:** Client call transcripts, meeting notes, website URLs, sales context

**Output:** A single self-contained interactive HTML file with:
- Scroll-triggered animations (IntersectionObserver)
- Sticky navigation with active section highlighting
- Animated number counters
- Expandable cards, tab switchers
- ROI calculator (when applicable)
- Print-friendly A4 layout
- Full DDVB TECH branding (dark covers, gold accents, sharp corners)

## Brand Guidelines

Both commands apply DDVB TECH visual identity:
- Colors: Gold (#FDB71C), Black (#0D0D0D), White
- Typography: Inter (web), Atyp (print/PPTX)
- Style: Sharp corners, high contrast, gold as accent only
- Logo: from `Dev-Platform/web-apps/ddvb-marketing-app/public/logo.png`

## Version

0.1.0
