# Getting Started

This guide walks you through installing the DDVB plugins and running your first command. By the end, you'll know how to launch a proposal, a brand strategy spec, or a naming brief.

## Prerequisites

- **Claude Code** installed (CLI, desktop app, or IDE extension)
- Access to the `ddvb-tech-plugins` marketplace (GitHub: `cybernexcorps/ddvb-tech-plugins`)
- For brand research: a [Parallel AI](https://platform.parallel.ai) account (Ultra processor)

## Installation

Open Claude Code and run these commands:

```bash
claude plugin install ddvb-product-scoping@ddvb-tech-plugins
claude plugin install ddvb-brand-strategy@ddvb-tech-plugins
claude plugin install ddvb-brand-naming@ddvb-tech-plugins
```

After installing, reload plugins:

```
/reload-plugins
```

Verify by checking the skill list — you should see commands like `/ddvb-product-scoping:create-proposal`, `/ddvb-brand-strategy:brand-full`, and `/ddvb-brand-naming:naming-full`.

## Your First Proposal

Let's create a commercial proposal for a client. You'll need:
- Client name
- Meeting notes, call transcripts, or a brief (`.md`, `.txt`, `.pdf`)
- Optionally: the client's website URL

### Run the command

```
/ddvb-product-scoping:create-proposal Adapter
```

Or just type in the chat: *"Create a commercial proposal for Adapter based on the materials in the Presales/Adapter/ folder"*

### What happens

1. Claude reads your source materials (transcripts, notes, PDFs)
2. Researches the client's website if a URL is available
3. Extracts pain points (verbatim quotes from transcripts are the most powerful content)
4. Maps DDVB capabilities to the client's problems
5. Generates two files:
   - **TypeScript data entry** — structured metadata for `proposals.ts`
   - **HTML body file** — the visual proposal using `proposal.css` classes

The proposal deploys directly to `ddvb.tech/ru/proposals/{slug}` — dark cinematic theme, gold accents, scroll animations.

### Output

```
Dev/ddvb-tech-website/src/data/proposals/
├── proposals.ts          ← your new entry added here
└── adapter-body.html     ← the visual HTML body
```

## Your First Brand Strategy Spec

For a repositioning project with client materials (PDFs, PPTX briefs):

### Prepare materials

Place all client documents in a working directory. Common inputs:
- Brand health tracker (PDF/PPTX)
- Qualitative research reports
- Competitor briefs
- Internal strategy decks

### Run the command

```
/ddvb-brand-strategy:brand-spec
```

### What happens

1. **Material extraction** — Claude reads all PDFs and PPTX files using `pdfplumber` and `python-pptx`
2. **Industry detection** — Identifies the client's industry from the materials
3. **Dimension selection** — Proposes research dimensions (17 fixed + industry-specific). You review and confirm.
4. **Parallel research** — Launches Parallel AI Ultra with one task per competitor (up to 10). Takes ~10-15 minutes.
5. **Synthesis** — Produces `spec_summary.md` with competitive landscape, archetype map, and positioning analysis

### Gate check

Before moving to Phase 2 (Strategy), Claude presents the spec summary and asks: *"Which hypothesis do you want to develop?"* You choose the direction, then run `/ddvb-brand-strategy:brand-plan`.

## Your First Naming Brief

For a naming project (new brand, rebrand, or product naming):

### Run the command

```
/ddvb-brand-naming:naming-brief
```

### What happens

1. **Material extraction** — Same as brand strategy
2. **Two-layer research:**
   - Layer 1: Competitive name analysis (per-competitor via Parallel AI)
   - Layer 2: Linguistic audit (phonetics, cross-language connotations, availability landscape)
3. **Brief assembly** — Produces `NAMING_BRIEF_FOR_COPYWRITER.md` with:
   - Semantic field (7-10 core concepts)
   - Recommended naming strategies
   - Selection criteria (mandatory + desired)
   - Taboo list
   - Inspiration facts

The brief goes to the copywriter. They return a long-list (50-80 candidates) which you then evaluate with `/ddvb-brand-naming:naming-evaluate`.

## Understanding the Pipeline

All three plugins follow the same pattern:

```
Source materials → Research → Synthesis → Deliverable → Gate check → Next phase
```

### Gate checks

Every phase ends with a gate check — Claude summarizes what was produced and asks for your confirmation before moving on. You can:
- **Approve** and proceed to the next phase
- **Adjust** — ask Claude to modify something
- **Stop** — the deliverables from completed phases are saved

### Parallel AI

Brand strategy and naming use [Parallel AI](https://platform.parallel.ai) for deep competitive research. When Claude launches research:
- It submits tasks to Parallel AI Ultra (one per competitor)
- Tasks run in parallel (~10-15 minutes)
- Results are saved to `research_reports/` as individual markdown files
- Claude synthesizes them into a summary

### Adaptive dimensions

Research dimensions adapt to the client's industry. Claude auto-detects the industry from your materials and proposes a dimension set. You always confirm before research runs. See the [reference](reference.md) for all available presets.

## What's Next

- [How to create a website proposal](how-to/create-website-proposal.md)
- [How to run a brand strategy project](how-to/run-brand-strategy.md)
- [How to run a naming project](how-to/run-naming-project.md)
- [Full command and skill reference](reference.md)
