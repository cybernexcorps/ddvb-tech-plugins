---
name: brand-execute
description: "Phase 4: Generate all figures, build PPTX presentation with DDVB branding, produce final deliverable."
---

# Phase 4: Execute

You are starting the **Execute** phase. The Review phase should be completed first.

## Prerequisites

- All `analysis/*.md` files exist and are finalized
- Review passed (or gaps have been addressed)
- User has confirmed Big Idea and visual direction
- Required Python packages: `matplotlib`, `numpy`, `python-pptx`

## Execution Steps

### Step 1: Set Up Font Module

Create `scripts/fonts.py` — a shared module that registers the project's typography (e.g., Atyp) with matplotlib:
- Scan common font directories for the specified font family
- Provide `font_props(role, size)` function for consistent usage
- Roles: title, subtitle, header, body, body_medium, body_bold, label, annotation

### Step 2: Generate Figures

Create `scripts/generate_all_slides.py` that produces ALL figures in `figures/`:

**Transparent-background figures** (for white slide backgrounds):
- `swot_quadrant.png` — 4-quadrant SWOT with colored headers
- `competitive_map.png` — 2D scatter with labeled competitors and movement arrow
- `brand_wheel.png` — Concentric rings: core → archetype → values → character
- `comms_architecture.png` — Big Idea → 3 messages → funnel
- `color_system.png` — Palette swatches with hex codes
- `typography_specimen.png` — Type hierarchy from H1 to Caption

**Dark-background figures** (creative mockups that MUST stay dark):
- `ad_mockups.png` — Digital banner + outdoor ad concepts
- `graphic_device.png` — Graphic device demonstrations
- `applied_identity.png` — Applied mockups (banner + outdoor + app)

**Rules:**
- Use `transparent=True` for analytical/structural figures
- Use dark background (`#0D0D0D`) for creative/mockup figures
- All text uses the project font (via fonts.py)
- All colors use the brand palette from visual_identity.md
- DPI: 250 for sharp rendering

### Step 3: Build Presentation

Create `scripts/build_presentation.py` that assembles a PPTX:

**Slide structure** (adapt to project, typically 12-15 slides):
1. Title slide (orange DDVB background)
2. Contents
3-5. Analytical block (metrics, SWOT as native PPTX shapes, competitive map as PNG)
6-9. Strategic block (hypothesis, brand wheel PNG, values as native PPTX, architecture as native PPTX)
10-11. Communication block (platform as native PPTX, slogans + mockup PNG)
12-14. Visual block (color PNG, typography as native PPTX + graphic device PNG, applied identity PNG)
15. Closing slide (orange DDVB background)

**Key rules:**
- Use DDVB background PNGs from the ddvb-brand-guidelines skill (if available)
- Build SWOT, values, communication cards, and typography as **native PPTX shapes** (not PNGs)
- Use PNGs only for complex visuals (charts, wheels, mockups)
- Every slide with a PNG gets a text header above it
- Transparent PNGs for white backgrounds, dark PNGs for creative mockups
- Font: Atyp Display for headers, Atyp Text for body
- Keep under 15MB

### Step 4: Verify

Run the presentation build and verify:
- Correct number of slides
- File size under limit
- All images load correctly
- No permission errors (use versioned filenames if needed)

## Output

- `figures/*.png` — All generated figures
- `scripts/fonts.py` — Font module
- `scripts/generate_all_slides.py` — Figure generation
- `scripts/build_presentation.py` — PPTX builder
- `[ProjectName].pptx` — Final presentation

## Important

- If the PPTX file is locked (open in PowerPoint), save with `_v2`, `_v3` suffix
- Remind the user to export to PDF via PowerPoint for final delivery
- The user can iterate on specific slides after initial generation
