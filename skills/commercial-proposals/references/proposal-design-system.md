# Proposal CSS Class Catalog

All classes are defined in `proposal.css` (loaded automatically by the page component). Do NOT write inline CSS — use these classes exclusively.

## CSS Variables

```css
:root {
  --gold: #FDB71C;
  --gold-10: rgba(253,183,28,0.10);
  --gold-20: rgba(253,183,28,0.20);
  --gold-40: rgba(253,183,28,0.40);
  --black: #0A0A0A;
  --ink: #141414;
  --surface: #1A1A1E;
  --chalk: #FAFAF8;
  --cream: #F2F0EB;
  --stone: #888;
  --mist: #bbb;
  --display: 'Atyp Display', Georgia, serif;
  --text: 'Atyp Text', -apple-system, sans-serif;
}
```

## Reveal Animations

Add `reveal` class to any element that should animate on scroll. The page component's IntersectionObserver adds `.visible` when the element enters the viewport.

| Class | Effect |
|-------|--------|
| `reveal` | Fade + slide up (32px translateY, 0.7s cubic-bezier) |
| `reveal reveal-d1` | Same + 0.1s delay |
| `reveal reveal-d2` | Same + 0.2s delay |
| `reveal reveal-d3` | Same + 0.3s delay |
| `reveal reveal-d4` | Same + 0.4s delay |

## Cover (`<header class="cover">`)

Full-viewport dark cover with centered content, pulsing radial gradient behind, gold 3px bottom border.

| Class | Element | Notes |
|-------|---------|-------|
| `cover` | `<header>` | min-height: 100vh, centered flex column, dark bg |
| `cv-logo` | `<img>` | 64px square, fade-down animation |
| `cv-kicker` | `<div>` | 11px uppercase, letter-spacing 5px, gold color |
| `cover h1` | `<h1>` | Atyp Display, clamp(36px, 5vw, 56px), weight 300 |
| `cover h1 strong` | `<strong>` | Weight 700, gold color |
| `cv-lead` | `<p>` | 16px, weight 300, 50% white opacity, max-width 520px |
| `cv-meta` | `<div>` | Flex row, gap 40px, top border 1px white/6% |
| `cv-meta-item` | `<dl>` | Contains `<dt>` (9px gold uppercase) + `<dd>` (13px white/55%) |
| `cv-scroll` | `<div>` | Absolute bottom, bouncing scroll indicator |

## Sections (`<section>`)

Standard content container: 100px vertical padding, max-width 900px, auto margins.

| Class | Element | Notes |
|-------|---------|-------|
| `sec-full` | modifier | Removes max-width, zero side padding |
| `sec-n` | `<div>` | Section number: 10px, weight 600, letter-spacing 4px, uppercase, gold. Format: `01 &mdash; Title` |
| `sec-t` | `<div>` | Section title: Atyp Display, clamp(28px, 3.5vw, 38px), weight 300, chalk color |
| `sec-s` | `<p>` | Section subtitle: 15px, weight 300, stone color, max-width 580px, margin-bottom 48px |

## Stats (`.stats`)

4-column grid with 2px gold gap between cells.

| Class | Element | Notes |
|-------|---------|-------|
| `stats` | `<div>` | Grid, 4 columns, gold background (visible as gap lines) |
| `stat` | `<div>` | Surface bg, 32px padding, centered text, hover darkens |
| `stat-v` | `<div>` | Value: Atyp Display, 36px, weight 300, gold color |
| `stat-l` | `<div>` | Label: 10px, weight 500, letter-spacing 2px, uppercase, white/40% |

## Cards (`.cards`)

Grid layout with 2px gap. Cards have bottom gold border and hover-lift animation.

| Class | Element | Notes |
|-------|---------|-------|
| `cards` | `<div>` | Grid container, 2px gap, margin-bottom 40px |
| `cards-2` | modifier | 2-column grid |
| `cards-3` | modifier | 3-column grid |
| `card` | `<div>` | 28px padding, bottom 2px gold border, hover: lift 4px + shadow |
| `card-light` | modifier | Cream background (`var(--cream)`), ink text |
| `card-dark` | modifier | Surface background (`var(--surface)`), white headings, white/50% text |
| `card-num` | `<div>` | Atyp Display, 28px, weight 300, gold color, margin-bottom 8px |
| `card h3` | `<h3>` | 14px, weight 700, Atyp Text |
| `card p` | `<p>` | 13px, stone color, line-height 1.55 |

Span across columns with inline style: `style="grid-column: span 2"`

## Flow Diagram (`.flow`)

Horizontal step flow with arrows between steps.

| Class | Element | Notes |
|-------|---------|-------|
| `flow` | `<div>` | Flex row, centered, surface bg, 36px padding |
| `flow-step` | `<div>` | Flex 1, centered text, hover: scale 1.08 |
| `flow-icon` | `<div>` | 28px emoji/text, margin-bottom 8px |
| `flow-label` | `<div>` | 10px uppercase, weight 600, white/60% |
| `flow-arr` | `<div>` | Arrow `&rarr;`, Atyp Display, gold, 20px |

## Divider (`.divider`)

Full-width gold background section with giant "D D V B" watermark.

| Class | Element | Notes |
|-------|---------|-------|
| `divider` | `<div>` | Gold bg, 120px padding, centered, overflow hidden |
| `divider h2` | `<h2>` | Atyp Display, clamp(32px, 4vw, 48px), weight 300, black color |
| `divider p` | `<p>` | 14px, black/45% opacity, weight 500 |

## Callout (`.callout`)

Highlighted note/quote box with gold left border.

| Class | Element | Notes |
|-------|---------|-------|
| `callout` | `<div>` | Gold-10 bg, 3px gold left border, 20px/24px padding, hover: border widens to 6px |
| `callout p` | `<p>` | 13px, white/70%, line-height 1.65 |
| `callout strong` | `<strong>` | Chalk color |

Variant for emphasis: add `style="background:var(--gold-20);border-left-color:var(--gold)"` for stronger highlight.

## Table (`.tbl`)

Full-width table with dark headers and gold accents.

| Class | Element | Notes |
|-------|---------|-------|
| `tbl` | `<table>` | Full width, collapse borders, Atyp Text 13px |
| `tbl th` | `<th>` | Surface bg, gold text, 10px uppercase, 2px gold bottom border |
| `tbl td` | `<td>` | 12px/16px padding, white/70% text, 1px white/4% bottom border |
| `tbl td strong` | `<strong>` | Chalk color |
| `tbl em` | `<em>` | Stone color, 10px size |
| `tbl tr:hover td` | hover | Gold-04 background |

## Timeline (`.timeline`)

Vertical timeline with gold left border and dot markers.

| Class | Element | Notes |
|-------|---------|-------|
| `timeline` | `<div>` | Padding-left 28px, 2px gold-40 left border |
| `tl-item` | `<div>` | 28px bottom padding, left-padded 24px, hover: indents to 30px |
| `tl-item::before` | pseudo | 10px gold square at -33px left, hover: scale 1.3 + glow |
| `tl-step` | `<div>` | 10px, weight 600, letter-spacing 2px, uppercase, gold. E.g. "Неделя 01" |
| `tl-title` | `<div>` | Atyp Display, 17px, weight 500, chalk color |
| `tl-desc` | `<div>` | 13px, stone color, line-height 1.55 |

## Checklist (`.checks`)

Styled unordered list with gold bullet squares.

| Class | Element | Notes |
|-------|---------|-------|
| `checks` | `<ul>` | No list-style, margin-bottom 32px |
| `checks li` | `<li>` | 13px, white/65%, 10px padding, 24px left padding, 1px bottom border, hover: chalk + indent |
| `checks li::before` | pseudo | 8px gold square at left 0, hover: scale 1.3 |

## Schematics (`.sch`)

Container for images/diagrams.

| Class | Element | Notes |
|-------|---------|-------|
| `sch` | `<div>` | Surface bg, 20px padding, centered, hover: scale 1.01 |
| `sch-t` | `<p>` | Title: 14px, weight 600, chalk color |
| `sch-d` | `<p>` | Description: 12px, stone color, line-height 1.5 |
| `sch img` | `<img>` | max-width 100%, auto height, block centered |

## Responsive (768px breakpoint)

Automatically handled by proposal.css:
- Sections: 60px/24px padding
- Stats: 2-column grid
- Cards: single column
- Flow: flex-wrap with 8px gap
- Cover meta: vertical stack
- CTA grid: 2-column
- Nav links: hidden
