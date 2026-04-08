# Reference

Complete reference for all plugins, commands, skills, research dimensions, and output files.

---

## Plugin Catalog

| Plugin | Version | Skills | Commands | Agents | References |
|--------|---------|--------|----------|--------|------------|
| `ddvb-product-scoping` | 0.2.0 | 2 | 2 | — | 4 |
| `ddvb-brand-strategy` | 1.1.0 | 4 | 5 | 3 | 5 |
| `ddvb-brand-naming` | 0.1.0 | 4 | 5 | — | 4 |

---

## Commands

### ddvb-product-scoping

| Command | Description | Arguments | Prerequisites |
|---------|-------------|-----------|---------------|
| `/ddvb-product-scoping:create-proposal` | Generate a commercial proposal in ddvb.tech format | `[client-name-or-path]` | Source materials (transcripts, notes, briefs) |
| `/ddvb-product-scoping:scope-product` | Scope a product from brainstorming materials | `[path-to-materials]` | Audio recordings, transcripts, or notes |

**create-proposal outputs:**
- `src/data/proposals/{slug}-body.html` — HTML body with `proposal.css` classes
- Entry in `src/data/proposals.ts` — TypeScript `Proposal` object

**scope-product outputs:**
- `{input-name}-synthesis.md` — Research synthesis
- `{product-name}-blueprint.md` — 14-section technical blueprint
- `DDVB-TECH-{ProductName}-OnePager.html` — EN + RU one-pagers

### ddvb-brand-strategy

| Command | Phase | Description | Prerequisites |
|---------|-------|-------------|---------------|
| `/ddvb-brand-strategy:brand-full` | All | Run all 4 phases end-to-end | Source materials |
| `/ddvb-brand-strategy:brand-spec` | 1 | Extract, research, synthesize spec | Source materials (PDF/PPTX) |
| `/ddvb-brand-strategy:brand-plan` | 2 | SWOT, brand platform, communication strategy | `analysis/spec_summary.md` |
| `/ddvb-brand-strategy:brand-review` | 3 | Validate coherence across deliverables | All Phase 2 analysis files |
| `/ddvb-brand-strategy:brand-execute` | 4 | Generate figures and PPTX | All analysis files |

**Phase 1 outputs:**
- `extracted/*.md` — Extracted text from source documents
- `research_reports/01-10_*.md` — Per-competitor research
- `research_reports/00_competitive_intelligence_summary.md`
- `competitive_analysis.csv` — All dimensions x competitors
- `analysis/spec_summary.md` — Synthesized specification

**Phase 2 outputs:**
- `analysis/swot_competitive.md` — SWOT + competitive landscape
- `analysis/brand_platform.md` — Mission, values, archetype, Big Idea
- `analysis/communication_platform.md` — Messages, slogans, channel matrix
- `analysis/visual_identity.md` — Colors, typography, graphic device

**Phase 4 outputs:**
- `figures/*.png` — Matplotlib charts and diagrams
- `{CLIENT}_Brand_Strategy_DDVB.pptx` — Branded presentation

### ddvb-brand-naming

| Command | Phase | Description | Prerequisites |
|---------|-------|-------------|---------------|
| `/ddvb-brand-naming:naming-full` | All | Run all phases with gate checks | Source materials |
| `/ddvb-brand-naming:naming-brief` | 1 | Research + copywriter brief | Source materials (PDF/PPTX/DOCX) |
| `/ddvb-brand-naming:naming-generate` | 2 | AI seed generation + availability checks | `NAMING_BRIEF_FOR_COPYWRITER.md` |
| `/ddvb-brand-naming:naming-evaluate` | 3 | Score candidates, produce short-list | Copywriter's long-list (50-80 names) |
| `/ddvb-brand-naming:naming-present` | 4 | Client-facing PPTX (optional) | `evaluation/final_candidates.md` |

**Phase 1 outputs:**
- `extracted/*.md` — Source material text
- `research_reports/01-10_*.md` — Per-competitor name research
- `research_reports/naming_territory_map.md` — Occupied vs free semantic territories
- `research_reports/linguistic_audit_*.md` — Per-language phonetic landscape
- `research_reports/availability_landscape.md` — Domain/social/trademark landscape
- `NAMING_BRIEF_FOR_COPYWRITER.md` — The copywriter brief

**Phase 2 outputs:**
- `seeds/naming_seeds.md` — 30-50 AI-generated candidates with availability data

**Phase 3 outputs:**
- `evaluation/long_list_import.md` — Imported candidates
- `evaluation/automated_screening.md` — Domain/trademark/phonetic pre-screen
- `evaluation/scoring_matrix.md` — Full 10-dimension scoring table
- `evaluation/short_list.md` — Top 8-10 with analysis
- `evaluation/final_candidates.md` — User-selected 3-5

**Phase 4 outputs:**
- `{CLIENT}_NAMING_PRESENTATION_DDVB.pptx` — Client-facing deck

---

## Skills

### ddvb-product-scoping

| Skill | Triggers on |
|-------|------------|
| `commercial-proposals` | "create a proposal", "generate a КП", "make a client proposal" |
| `product-scoping` | "scope a product", "turn brainstorming into a spec", "create a blueprint" |

### ddvb-brand-strategy

| Skill | Triggers on |
|-------|------------|
| `brand-research` | Reading PDFs/PPTX for brand strategy projects |
| `parallel-research` | Running competitive research via Parallel AI |
| `visual-generation` | Creating matplotlib figures for strategy deliverables |
| `presentation-assembly` | Building PPTX presentations |

### ddvb-brand-naming

| Skill | Triggers on |
|-------|------------|
| `naming-research` | Researching competitor names, archetypes, semantic territories |
| `naming-brief-assembly` | Assembling the copywriter naming brief |
| `naming-evaluation` | Scoring and ranking name candidates |
| `naming-linguistics` | Phonetic analysis, cross-language checks, domain/trademark availability |

---

## Research Dimensions

### Fixed Dimensions (always included — 17)

| Group | # | Dimensions |
|-------|---|-----------|
| A. Identification | 3 | competitor_name, competitor_type, parent_company |
| B. Brand & Positioning | 5 | brand_essence, brand_positioning, brand_archetype, brand_image, tone_of_voice |
| C. Communication | 4 | communication_channels, social_media_presence, content_and_education, key_messages |
| H. Market Position | 4 | market_share_data, target_audience, competitive_advantages, competitive_weaknesses |
| I. Sources | 1 | sources |

### Industry Presets (variable dimensions)

| Industry | Dimensions | Key focus areas |
|----------|-----------|----------------|
| **Finance** | 13 | product_range, tariff_plans, advisory_model, affluent_offering, affluent_threshold, affluent_service, affluent_communication, app_rating, platform_features, digital_ux, ecosystem_integration, loyalty_program, regulatory_status |
| **FMCG** | 12 | product_portfolio, price_positioning, distribution_channels, retail_presence, production_origin, quality_certifications, sustainability_esg, packaging_design, innovation_pipeline, digital_presence, trade_marketing, export_markets |
| **Tech/SaaS** | 12 | product_suite, pricing_model, enterprise_offering, developer_experience, integration_ecosystem, platform_metrics, onboarding_support, ai_capabilities, security_compliance, partner_program, funding_trajectory, technology_stack |
| **Services** | 10 | service_portfolio, pricing_model, key_clients, team_expertise, awards_recognition, methodology, case_studies_quality, digital_maturity, geographic_reach, partnership_network |
| **E-commerce** | 12 | product_catalog, price_positioning, marketplace_model, logistics_delivery, payment_financing, ux_conversion, customer_service, loyalty_retention, seller_ecosystem, technology_platform, regional_coverage, sustainability |
| **Manufacturing** | 11 | product_portfolio, production_capacity, pricing_contracts, distribution_network, technical_support, quality_certifications, r_and_d, key_accounts, sustainability_esg, digital_transformation, export_localization |

### Naming-Specific Dimensions (Layer 1 — 17)

| Group | # | Dimensions |
|-------|---|-----------|
| A. Identification | 3 | competitor_name, competitor_type, parent_company |
| B. Name & Brand | 6 | name_origin, name_languages, brand_archetype, brand_positioning, tagline_slogan, tone_of_voice |
| C. Semantic Territory | 4 | semantic_field, visual_identity_of_name, naming_pattern_industry, occupied_territories |
| D. Market Position | 3 | market_share_data, competitive_advantages, competitive_weaknesses |
| E. Sources | 1 | sources |

### Naming Linguistic Dimensions (Layer 2)

| # | Dimension | Scope |
|---|-----------|-------|
| L1-L3 | phonetic_patterns, negative_connotations, positive_associations | Per target language |
| L4-L6 | domain_landscape, social_handle_landscape, trademark_landscape | Market-wide |

---

## Naming Strategies

| Strategy | Best for | Risk |
|----------|----------|------|
| **Descriptive** | Established categories, B2B clarity | Hard to trademark, limits pivots |
| **Metaphorical** | Strong archetype, emotional positioning | Needs marketing to build association |
| **Coined** | Global ambitions, 3+ languages | Zero inherent meaning, expensive to build |
| **Acronym** | Transitioning established long names | Forgettable for new brands |
| **Portmanteau** | Two strong concepts that blend | Can sound forced |
| **Founder** | Heritage, trust, craft businesses | Tied to one person's reputation |
| **Geographic** | Origin story matters, regional expertise | May limit expansion |

---

## Evaluation Matrix

### Dimensions and Weights

| # | Dimension | Weight | Type |
|---|-----------|--------|------|
| 1 | Brand fit | 20% | Strategic |
| 2 | Differentiation | 15% | Strategic |
| 3 | Emotional resonance | 10% | Strategic |
| 4 | Story potential | 10% | Strategic |
| 5 | Scalability | 5% | Strategic |
| 6 | Memorability | 15% | Practical |
| 7 | Pronounceability | 10% | Practical |
| 8 | Domain availability | 5% | Practical |
| 9 | Visual/logo potential | 5% | Practical |
| 10 | Abbreviation quality | 5% | Practical |

### Scoring Scale

| Score | Meaning |
|-------|---------|
| 5 | Excellent |
| 4 | Strong |
| 3 | Adequate |
| 2 | Weak |
| 1 | Fail — disqualifying |

**Minimum passing: 60 points** (out of 100).

### Weight Adjustments

| Context | Adjustment |
|---------|-----------|
| International launch | Pronounceability → 15%, Story → 5% |
| Startup / VC-backed | Memorability → 20%, Scalability → 0% |
| Heritage rebrand | Brand fit → 25%, add Heritage Continuity |
| Digital-first | Domain → 10%, add SEO/Searchability |

---

## Trademark Sources

| Tier | Source | Method | Coverage |
|------|--------|--------|----------|
| 1 | EUIPO API | REST API (automated) | EU marks (~3.1M) |
| 2 | WIPO Brand DB | Web search (semi-auto) | International marks in RU/KZ (~400K RU) |
| 3 | Rospatent FIPS | Web search (semi-auto) | Russian national marks (granted only) |
| 4 | NIIS Kazakhstan | Manual | Kazakh marks |

EUIPO API requires `EUIPO_CLIENT_ID` (free registration at dev.euipo.europa.eu).

All other tiers use web search as a proxy. Plugin always adds a disclaimer recommending professional attorney search.

---

## ICGS Classes by Industry

| Industry | Key Nice Classes |
|----------|-----------------|
| Logistics | 35 (business management), 39 (transport/storage) |
| Finance | 35 (business services), 36 (insurance/financial) |
| FMCG/Food | 29 (food products), 30 (staple foods), 32 (beverages) |
| Tech/SaaS | 9 (software), 35 (business services), 42 (tech services) |
| Services/Agency | 35 (advertising), 41 (education), 42 (design) |
