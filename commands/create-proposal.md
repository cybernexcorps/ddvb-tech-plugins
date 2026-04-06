---
description: "Generate a commercial proposal in the ddvb.tech website format"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Agent, WebSearch, WebFetch
argument-hint: "[client-name-or-path-to-materials]"
---

# Commercial Proposal Generator — Website Format

Generate a commercial proposal that deploys directly to the DDVB TECH website at `ddvb.tech/{locale}/proposals/{slug}`. The output is two files: a TypeScript data entry and an HTML body file.

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
- **Company name** (required) — becomes the slug
- **Industry / vertical**
- **Key contacts** (names, roles)
- **Website URL** (for research)
- **Pain points** mentioned in calls/notes (use their exact words)
- **Budget range** (if known)
- **Timeline expectations**
- **Referral** (if someone introduced the client)

### Research
1. If a website URL is available, fetch and extract: company description, products/services, team, tech stack signals
2. Web search: `"[Company]" + industry context, recent news, competitors`
3. If transcripts provided: extract verbatim pain point quotes, decision criteria, objections, internal project names

### DDVB TECH Context
Know what we sell:
- AI-powered automation for creative and PR agencies
- Products: media comment writer, case study generator, SEO content agent, article rewriter, tender automation
- Platform: n8n workflows + LangChain/LangGraph agents + Next.js web apps
- Delivery model: discovery → prototype → production
- Analytics dashboards (RFM, ABC/XYZ, Text-to-SQL, BigQuery)

Map DDVB TECH capabilities to client's specific pain points.

### Reference Existing Proposals
Read existing proposals to match the established quality bar:
- `Dev/ddvb-tech-website/src/data/proposals.ts` — all proposal data entries
- `Dev/ddvb-tech-website/src/data/proposals/adapter-body.html` — Discovery/research format
- `Dev/ddvb-tech-website/src/data/proposals/resinstudiocz-body.html` — Product/analytics format

## Phase 1: Generate HTML Body

Create `src/data/proposals/{slug}-body.html` in the website repository at:
`Dev/ddvb-tech-website/src/data/proposals/{slug}-body.html`

### Structure

Follow this section sequence (adapt to the deal — not all sections are required):

1. **Cover** — `<header class="cover" id="top">` with logo, kicker, title, lead, meta, scroll indicator
2. **Business section** — `<section id="business">` with stats bar, pain point cards (card-light), callouts with verbatim quotes
3. **Divider** — `<div class="divider">` with headline summarizing the approach
4. **Solution sections** (1-3 sections) — each `<section>` with flow diagram, numbered dark cards, callouts
5. **Architecture/Stack** — `<section>` with `.tbl` table showing tech stack
6. **Pricing** — `<section id="pricing">` with `.tbl` table + pricing cards + highlighted total callout
7. **Plan** — `<section id="plan">` with `.timeline` and `.tl-item` phases
8. **Why Us** — `<section id="why">` with 4 competency cards + `.checks` list

**Do NOT include a CTA section** — it's rendered by the React component from the TypeScript data.

### HTML Rules

- No `<html>`, `<head>`, `<body>`, `<style>`, or `<script>` tags
- No inline CSS except minimal overrides (e.g., `style="grid-column: span 2"`, `style="text-align:center"`)
- Use CSS classes from `proposal.css` exclusively — see skill references
- All content elements get `class="reveal"` (with delay variants `reveal-d1` through `reveal-d4` for stagger)
- Use HTML entities: `&mdash;`, `&laquo;`, `&raquo;`, `&times;`, `&middot;`, `&rarr;`, `&#8381;`
- Logo always: `<img class="cv-logo" src="/logo.png" alt="DDVB TECH">`
- Images in `/proposals/` path (public directory)

## Phase 2: Generate TypeScript Data Entry

Create the `Proposal` object to add to the `proposals` array in:
`Dev/ddvb-tech-website/src/data/proposals.ts`

### Required Fields

```typescript
{
  slug: "{slug}",
  locale: "ru",
  client: "{Client Name}",
  date: "{Month} 2026",
  // referral: "Name" — if applicable
  bodyHtml: loadProposalHtml("{slug}-body.html"),
  hero: {
    kicker: "Commercial Proposal",
    title: "Headline for **{Client}**",
    subtitle: "One-sentence value proposition.",
    meta: [
      { label: "Подготовлено для", value: "{Client}" },
      { label: "Контакт", value: "{Contact Person}" },
      { label: "Дата", value: "{Month} 2026" },
      { label: "Формат", value: "{Type}" },
    ],
  },
  stats: [ /* exactly 4 items */ ],
  painPoints: { title: "...", items: [ /* from transcripts */ ] },
  solutions: { title: "...", subtitle: "...", items: [ /* mapped to pain points */ ] },
  pricing: { title: "Инвестиции", tiers: [ /* with highlighted totals */ ] },
  timeline: { title: "План работ", phases: [ /* with durations */ ] },
  cta: {
    title: "Давайте **начнём**",
    subtitle: "What happens after accepting.",
    acceptLabel: "Принять предложение",
    discussLabel: "Обсудить детали",
    contactGrid: [
      { label: "Telegram", value: "@slavickk" },
      { label: "Email", value: "info@ddvb.tech" },
      { label: "Web", value: "ddvb.tech" },
      { label: "Следующий шаг", value: "{Next step}" },
    ],
  },
}
```

## Phase 3: Integration

1. Add the new entry to the `proposals` array in `src/data/proposals.ts`
2. Verify the HTML body file exists at `src/data/proposals/{slug}-body.html`
3. Run `npm run build` from `Dev/ddvb-tech-website/` to verify static generation works
4. The proposal will be available at `ddvb.tech/ru/proposals/{slug}`

## Phase 4: Present to User

Summarize the proposal:
- **URL**: `ddvb.tech/ru/proposals/{slug}`
- **Sections created**: list each section with brief content summary
- **Key data used**: pain points quoted, solutions mapped, pricing structured
- **Assumptions made**: flag anything inferred vs. explicitly stated
- **Files created**:
  - `src/data/proposals/{slug}-body.html`
  - Entry added to `src/data/proposals.ts`

## Content Language

- **All proposal content in Russian** (target market)
- Technical terms can stay in English (API, AI, LLM, CRM, etc.)
- Use the client's own terminology from transcripts
- Tone: confident, direct, professional — not corporate-speak
- Short sentences, active voice
- Pain points: quote the client verbatim (in Russian)

## Important

- The HTML body must look identical in style to existing proposals (adapter, resinstudiocz)
- Pain points from transcripts are the most powerful content — use verbatim quotes generously
- Every solution section must map directly to a stated pain point
- The TypeScript data and HTML body must be consistent (same stats, same pricing, same timeline)
- Do NOT duplicate content that belongs in the CTA (the React component handles it)
- Test that the build works before delivering
