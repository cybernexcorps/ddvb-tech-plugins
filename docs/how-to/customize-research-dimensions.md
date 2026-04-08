# How to Customize Research Dimensions

Adapt the competitive research framework when the default industry preset doesn't fit your project.

## When to Use

- The client's business spans multiple industries (e.g., a food company with an e-commerce arm)
- The default preset is missing dimensions you need
- You want to add project-specific dimensions not in any preset

## How Dimensions Work

Every research project uses:
- **17 fixed dimensions** — always included (identification, brand, communication, market position, sources)
- **8-15 variable dimensions** — selected from an industry preset

Claude auto-detects the industry and proposes a preset. You always confirm before research runs.

## Steps

### 1. Let Claude propose

When you run `/brand-spec` or `/naming-brief`, Claude presents:

```
Based on the brief, I've identified this as a FMCG project.

Fixed dimensions (always included): 17
Suggested variable dimensions from FMCG preset: 12
- V1. product_portfolio — Product categories, SKU count, flagship products
- V2. price_positioning — Price segment: economy, mid-market, premium
- ...

Total: 29 dimensions per competitor
```

### 2. Add from other presets

If the client has an e-commerce channel, add e-commerce dimensions:

> "Add `ux_and_conversion` and `logistics_and_delivery` from the E-commerce preset"

Claude adds them to the variable set and renumbers.

### 3. Remove irrelevant dimensions

If the client is a local producer with no export plans:

> "Remove `export_markets` — they only sell domestically"

### 4. Add custom dimensions

For project-specific needs not in any preset:

> "Add a custom dimension: `halal_certification` — whether the competitor has halal certification and which markets it covers"

Claude creates a new dimension following the standard format:
```
V[N]. **halal_certification** — Halal certification status, certifying body, 
markets covered, prominence in marketing materials.
```

### 5. Confirm and proceed

Claude shows the final dimension set with total count. Confirm, and research launches with your customized set.

## Available Presets

| Preset | Dims | Use when |
|--------|------|----------|
| Finance | 13 | Banks, brokers, insurance, fintech |
| FMCG | 12 | Food, beverages, personal care, household |
| Tech/SaaS | 12 | Software, platforms, dev tools |
| Services | 10 | Agencies, consultancies, law firms |
| E-commerce | 12 | Online stores, marketplaces, D2C |
| Manufacturing | 11 | Industrial producers, B2B suppliers |

Full dimension lists are in the [reference](../reference.md#industry-presets-variable-dimensions).

## Common Customizations

| Scenario | What to add |
|----------|------------|
| Client has both B2B and B2C | Dimensions from both relevant presets |
| Premium repositioning | `affluent_offering`, `affluent_communication` from Finance |
| International expansion | `export_markets`, `regional_coverage`, add target languages |
| Digital-native competitors | `ai_capabilities`, `developer_experience` from Tech |
| Sustainability is key differentiator | `sustainability_and_esg` from FMCG or Manufacturing |

## For Naming Projects

The naming plugin (`ddvb-brand-naming`) has its own lighter dimension set focused on names, not business analysis. Naming-specific variable dimensions are shorter (2 per industry) — see the [reference](../reference.md#naming-specific-dimensions-layer-1--17).
