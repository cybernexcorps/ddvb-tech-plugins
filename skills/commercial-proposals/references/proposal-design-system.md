# Proposal Design System

## CSS Variables

```css
:root {
  --ddvb-gold: #FDB71C;
  --ddvb-black: #0D0D0D;
  --ddvb-sidebar: #111111;
  --ddvb-white: #FFFFFF;
  --ddvb-gray-100: #F5F5F5;
  --ddvb-gray-200: #E8E8E8;
  --ddvb-gray-400: #AAAAAA;
  --ddvb-body-text: #2A2A2A;
  --ddvb-muted: #666666;
}
```

## Page Structure

```css
/* Each section = one "page" (min-height matches A4 proportions) */
.section-page {
  padding: 50px;
  min-height: 1123px;
  display: flex;
  flex-direction: column;
  position: relative;
}

/* Subtle bottom separator between sections */
.section-page::after {
  content: '';
  position: absolute;
  bottom: 0; left: 50px; right: 50px;
  height: 1px;
  background: var(--ddvb-gray-200);
}
```

## Section Headers

```css
.section-number {
  font-size: 11px;
  letter-spacing: 3px;
  text-transform: uppercase;
  color: var(--ddvb-gold);
  font-weight: 700;
  margin-bottom: 8px;
}

.section-title {
  font-size: 30px;
  font-weight: 700;
  color: var(--ddvb-black);
  margin-bottom: 4px;
  letter-spacing: -0.3px;
}

.section-divider {
  width: 48px;
  height: 3px;
  background: var(--ddvb-gold);
  margin: 16px 0 32px;
}

.section-subtitle {
  font-size: 15px;
  color: var(--ddvb-muted);
  margin-bottom: 32px;
  line-height: 1.6;
  max-width: 580px;
}
```

## Cards

```css
.card-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin-bottom: 32px;
}
.card-grid.three { grid-template-columns: 1fr 1fr 1fr; }
.card-grid.single { grid-template-columns: 1fr; }

.card {
  background: var(--ddvb-gray-100);
  padding: 24px;
  border-left: 3px solid var(--ddvb-gold);
  transition: transform 0.2s, box-shadow 0.2s;
}
.card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

.card-number {
  display: inline-flex;
  width: 28px; height: 28px;
  background: var(--ddvb-black);
  color: var(--ddvb-gold);
  font-size: 12px;
  font-weight: 800;
  align-items: center;
  justify-content: center;
  margin-bottom: 12px;
}

.card h3 {
  font-size: 15px;
  font-weight: 700;
  color: var(--ddvb-black);
  margin-bottom: 8px;
}

.card p {
  font-size: 13px;
  line-height: 1.6;
  color: var(--ddvb-muted);
}
```

## Cover Page

```css
.cover {
  min-height: 1123px;
  background: var(--ddvb-black);
  color: var(--ddvb-white);
  padding: 50px;
  display: flex;
  flex-direction: column;
}

.cover-tag {
  display: inline-block;
  background: var(--ddvb-gold);
  color: var(--ddvb-black);
  padding: 6px 16px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  width: fit-content;
}

.cover h1 {
  font-size: 44px;
  font-weight: 300;
  line-height: 1.15;
  letter-spacing: -0.5px;
}
.cover h1 strong {
  font-weight: 700;
  color: var(--ddvb-gold);
}

.cover-subtitle {
  font-size: 18px;
  font-weight: 300;
  color: rgba(255,255,255,0.7);
  line-height: 1.6;
  max-width: 520px;
}

.cover-meta {
  display: flex;
  gap: 40px;
  margin-top: 20px;
  padding-top: 24px;
  border-top: 1px solid rgba(255,255,255,0.1);
}
```

## Pain Point Quote Cards

```css
.pain-card {
  background: var(--ddvb-gray-100);
  padding: 24px;
  border-left: 3px solid var(--ddvb-gold);
}

.pain-card .quote {
  font-size: 14px;
  font-style: italic;
  color: var(--ddvb-body-text);
  line-height: 1.6;
  margin-bottom: 12px;
}

.pain-card .quote::before { content: '\201C'; color: var(--ddvb-gold); font-size: 24px; margin-right: 4px; }

.pain-card .impact {
  font-size: 12px;
  font-weight: 600;
  color: var(--ddvb-black);
}

.pain-card .impact span {
  color: var(--ddvb-gold);
}
```

## Timeline

```css
.timeline {
  display: flex;
  gap: 2px;
  margin: 32px 0;
}

.timeline-phase {
  flex: 1;
  background: var(--ddvb-black);
  padding: 20px 16px;
  color: var(--ddvb-white);
}
.timeline-phase:first-child { border-left: 3px solid var(--ddvb-gold); }

.phase-number {
  font-size: 20px;
  font-weight: 800;
  color: var(--ddvb-gold);
}
.phase-label {
  font-size: 11px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-top: 4px;
}
.phase-duration {
  font-size: 10px;
  color: var(--ddvb-gray-400);
  margin-top: 6px;
}
```

## Pricing Table

```css
.pricing-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 16px;
}

.price-card {
  background: var(--ddvb-gray-100);
  padding: 24px;
  border-top: 3px solid var(--ddvb-gold);
  text-align: center;
}
.price-card.featured {
  background: var(--ddvb-black);
  color: var(--ddvb-white);
}

.price-value {
  font-size: 32px;
  font-weight: 800;
  color: var(--ddvb-black);
}
.price-card.featured .price-value { color: var(--ddvb-gold); }

.price-unit {
  font-size: 12px;
  color: var(--ddvb-muted);
}
```

## ROI Comparison

```css
.roi-table {
  width: 100%;
  border-collapse: collapse;
}
.roi-table th {
  text-align: left;
  padding: 10px 16px;
  background: var(--ddvb-gray-100);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 1px;
  text-transform: uppercase;
  border-bottom: 2px solid var(--ddvb-black);
}
.roi-table td {
  padding: 10px 16px;
  border-bottom: 1px solid var(--ddvb-gray-200);
  font-size: 13px;
}
.roi-table .savings {
  color: var(--ddvb-gold);
  font-weight: 700;
}
```

## Print Styles

```css
@media print {
  body { background: white; }
  .section-page { break-inside: avoid; page-break-after: always; }
  .cover { break-after: page; }
  .nav, .progress-bar { display: none; }
  .card:hover { transform: none; box-shadow: none; }
  [data-animate] { opacity: 1 !important; transform: none !important; }
}
```
