# AGENTS.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## What This Is

A Claude plugin (`brand-strategy`) for DDVB Analytics that delivers end-to-end brand repositioning workflows. It provides slash commands, sub-agents, and skills — not a standalone application. No build step or test runner exists; the plugin is used directly inside Claude.

## Slash Commands (the workflow entry points)

| Command | Phase | Purpose |
|---------|-------|---------|
| `/brand-spec` | 1 | Extract source PDFs/PPTX, run Parallel AI competitive research, synthesize spec |
| `/brand-plan` | 2 | SWOT, brand platform, comms platform, visual identity |
| `/brand-review` | 3 | Coherence matrix, cross-block alignment, brief compliance |
| `/brand-execute` | 4 | Generate matplotlib figures, build PPTX presentation |
| `/brand-full` | All | Full pipeline with user-approval gates between phases |

Phases must run in sequence. Each phase reads outputs from the previous one. `/brand-full` enforces gate stops for user confirmation at the end of each phase.

## Python Dependencies

Install before running any execute-phase scripts:

```bash
pip install pdfplumber python-pptx matplotlib numpy
```

- `pdfplumber` — PDF extraction (never use `pdftoppm`, `PyPDF2`, or shell tools)
- `python-pptx` — PPTX creation and extraction
- `matplotlib` with `numpy` — all figure generation

## Project Directory Conventions

When running a brand strategy project, files land in these directories relative to the project working directory:

```
analysis/
  spec_summary.md          # output of brand-spec
  swot_competitive.md      # output of brand-plan
  brand_platform.md        # output of brand-plan
  communication_platform.md
  visual_identity.md       # source of brand colors/fonts for figure scripts
  coherence_review.md      # output of brand-review
  review_report.md

research_reports/
  README.md                # Parallel AI run IDs and task URLs
  00_competitive_intelligence_summary.md
  01_[competitor].md ... 10_[competitor].md
competitive_analysis.csv   # 30-column CSV merged from all competitor reports

scripts/
  fonts.py                 # shared font module (created from references/fonts_template.py)
  generate_all_slides.py   # figure generation (from references/generate_figures_template.py)
  build_presentation.py    # PPTX builder (from references/build_pptx_template.py)

figures/
  swot_quadrant.png, competitive_map.png, brand_wheel.png,
  comms_architecture.png, color_system.png, typography_specimen.png,
  ad_mockups.png, graphic_device.png, applied_identity.png
```

The `references/` directory in this plugin holds the canonical templates for `scripts/fonts.py`, `scripts/generate_all_slides.py`, and `scripts/build_presentation.py`. When starting a new project, copy and adapt these templates.

## Architecture

### Four-Phase Pipeline

```
brand-spec ──[user picks hypothesis]──▶ brand-plan ──[user confirms Big Idea]──▶ brand-review ──[user approves]──▶ brand-execute
```

Each phase reads `analysis/*.md` files and writes new ones. The execute phase reads `analysis/visual_identity.md` to get project-specific brand colors (hex codes) for figures.

### Competitive Research via Parallel AI

The spec phase uses [platform.parallel.ai](https://platform.parallel.ai) to research up to 10 competitors in parallel, each across 30 structured dimensions (see `references/competitive_research_template.md`). Use **Ultra processor** (not Ultra8x) for up to ~10 competitors — Ultra gives deeper per-task research. Ultra8x optimizes throughput for 50+ tasks.

Results saved as `research_reports/01_[name].md` through `10_[name].md`, then merged into `competitive_analysis.csv`.

### Visual Generation (matplotlib)

All figures use one of two rendering modes depending on figure type:

**Transparent mode** — analytical/structural figures that sit on white DDVB slide backgrounds:
```python
fig.savefig(path, transparent=True, dpi=250, bbox_inches="tight")
```
Use for: SWOT, competitive map, brand wheel, comms architecture, color system, typography specimen.

**Dark mode** — creative mockups that are intentionally dark:
```python
fig.savefig(path, facecolor="#0D0D0D", transparent=False, dpi=250, bbox_inches="tight")
```
Use for: ad mockups, graphic device demos, applied identity.

All text in figures must use `font_props(role, size)` from `scripts/fonts.py` — never matplotlib default fonts. Gold (`#FDB71C`) text is only readable on dark backgrounds; never use it on white.

Font roles: `title`, `subtitle`, `header`, `body`, `body_medium`, `body_bold`, `label`, `annotation`.
Font files: `~/AppData/Local/Microsoft/Windows/Fonts/AtypDisplay-*.ttf` and `AtypText-*.ttf`.

### PPTX Assembly (python-pptx)

Slide content is either native PPTX shapes or PNG figures — choose based on content type:

| Use native PPTX shapes | Use PNG figures |
|------------------------|-----------------|
| SWOT, values, comms cards, typography specimen, brand architecture, key metrics | Competitive map, brand wheel, ad mockups, graphic device, applied identity, color swatches |

Native shapes render crisply at any zoom; PNGs are used for complex visuals that are hard to replicate in PPTX.

Every slide requires a header: `"0X  Title"` in Atyp Display 26pt at position `(0.8", 0.35")`.

DDVB background PNGs come from:
```python
Path.home() / ".claude/skills/ddvb-brand-guidelines/resources/backgrounds"
```
Backgrounds are inserted at z-order 2 (behind all other shapes). If a `.pptx` file is locked (open in PowerPoint), save with versioned suffix `_v2`, `_v3`, etc. Target file size: under 15 MB.

### Sub-agents

| Agent | Tools | When to use |
|-------|-------|-------------|
| `research-analyst` | Bash, Read, Write, Glob, Grep | Extracting data from source PDFs/PPTX |
| `visual-designer` | Bash, Read, Write, Glob | Generating matplotlib figures |
| `quality-reviewer` | Read, Glob, Grep | Reviewing strategy docs for coherence and completeness |

The quality reviewer scores four dimensions (0–100%): coherence, completeness, distinctiveness, presentation readiness. It recommends PASS, PASS WITH NOTES, or NEEDS REVISION.

### Skills (auto-activated by file patterns)

| Skill | Activates on |
|-------|-------------|
| `brand-research` | `*.pdf`, `*.pptx`, `analysis/spec_summary*` |
| `parallel-research` | `competitive_analysis*`, `research_reports/*`, `*competitor*` |
| `presentation-assembly` | `scripts/build_presentation.py`, `*.pptx` |
| `visual-generation` | `scripts/generate_*.py`, `scripts/fonts.py`, `figures/*.png` |

## Brand Colors (DDVB / project palette)

| Role | Hex |
|------|-----|
| Activation Gold | `#FDB71C` |
| Deep Space (black) | `#0D0D0D` |
| Clarity Blue (message 1) | `#1565C0` |
| Transform Violet (message 2) | `#6A1B9A` |
| Freedom Amber (message 3) | `#E65100` |

Secondary colors map to the message system. The project-specific palette is always defined in `analysis/visual_identity.md` and should be read from there rather than hardcoded, since each project has different brand colors.
