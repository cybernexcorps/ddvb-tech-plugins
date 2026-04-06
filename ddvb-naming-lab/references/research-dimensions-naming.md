# Naming Research Dimensions

Research dimensions for naming projects. Two layers: stripped brand dimensions + linguistic audit.

## Layer 1: Brand Dimensions (Fixed — always included)

Stripped from the full brand-strategy framework. Focus on what matters for naming: competitor names, archetypes, semantic territories, tone.

### A. Identification (3)

| # | Dimension | Description |
|---|-----------|-------------|
| 1 | **competitor_name** | Full name (in market language). Note: transliteration variants, abbreviations, informal names used by clients. |
| 2 | **competitor_type** | Category within the industry |
| 3 | **parent_company** | Parent group/holding, or "Independent" |

### B. Name & Brand Analysis (6)

| # | Dimension | Description |
|---|-----------|-------------|
| 4 | **name_origin** | Etymology and naming strategy: descriptive, metaphorical, coined, acronym, founder name, geographic, portmanteau. Why this name? |
| 5 | **name_languages** | Languages the name works in. Does it have meaning in other languages? Positive/negative connotations? |
| 6 | **brand_archetype** | Dominant archetype with 1-sentence justification. |
| 7 | **brand_positioning** | Market positioning: mass-market, premium, niche, tech-forward, expert, accessible. |
| 8 | **tagline_slogan** | Current tagline/slogan in original language. Quote in «кавычках». If none visible, state explicitly. |
| 9 | **tone_of_voice** | Communication tone: formal/informal, expert/accessible. Include 1-2 verbatim examples. |

### C. Semantic Territory (4)

| # | Dimension | Description |
|---|-----------|-------------|
| 10 | **semantic_field** | What concepts/associations does the brand name evoke? List 5-7 associated words/ideas. |
| 11 | **visual_identity_of_name** | How is the name rendered visually? Uppercase, lowercase, mixed? Logotype style? Does the visual treatment reinforce meaning? |
| 12 | **naming_pattern_industry** | Common naming patterns in this industry. What types of names dominate? (Acronyms? Descriptive? Founder names?) |
| 13 | **occupied_territories** | Which semantic territories are already claimed by competitors? What concepts are saturated? |

### D. Market Position (3)

| # | Dimension | Description |
|---|-----------|-------------|
| 14 | **market_share_data** | Revenue, client count, rankings — use most recent data. |
| 15 | **competitive_advantages** | 3-5 key advantages. |
| 16 | **competitive_weaknesses** | 3-5 known weaknesses. |

### E. Sources (1)

| # | Dimension | Description |
|---|-----------|-------------|
| 17 | **sources** | Semicolon-separated URLs. Minimum 3 per competitor. |

---

## Layer 2: Linguistic Audit Dimensions

Run AFTER Layer 1 is complete. Applied to the subject company's naming context (not per-competitor).

### F. Phonetic Landscape (run per target language)

| # | Dimension | Description |
|---|-----------|-------------|
| L1 | **phonetic_patterns_{lang}** | Common phonetic patterns in the industry for this language. Hard/soft sounds, syllable counts, stress patterns. |
| L2 | **negative_connotations_{lang}** | Words/sounds to avoid in this language due to negative associations, profanity, or unfortunate meanings. |
| L3 | **positive_associations_{lang}** | Sounds and word roots that carry positive connotations in this language for this industry. |

Default languages: Russian (ru), English (en). Ask user for additional languages.

### G. Name Availability Landscape

| # | Dimension | Description |
|---|-----------|-------------|
| L4 | **domain_landscape** | Which .com, .ru, .kz (etc.) domains are taken by competitors? What patterns are used (brand.com, brand-group.com, etc.)? |
| L5 | **social_handle_landscape** | Which social handles are taken? Telegram, Instagram, VK, LinkedIn patterns. |
| L6 | **trademark_landscape** | Key trademark classes for this industry. Which names are registered? Which registries to check (Rospatent, NIIS KZ, WIPO)? |

---

## Industry-Specific Variable Dimensions

Like brand-strategy, naming research can include industry-specific dimensions. These are lighter — focused on naming context, not full business analysis.

### Finance / Investment

| # | Dimension | Description |
|---|-----------|-------------|
| V1 | **naming_convention_finance** | Do competitors use "Инвестиции", "Капитал", "Брокер" in names? What suffixes/prefixes dominate? |
| V2 | **trust_signals_in_name** | Do names signal trust, stability, heritage? (Years in name, geographic anchors, institutional words) |

### FMCG / Food & Beverage

| # | Dimension | Description |
|---|-----------|-------------|
| V1 | **naming_convention_fmcg** | Descriptive (product-in-name) vs evocative (emotion/lifestyle) vs coined? What dominates? |
| V2 | **shelf_distinctiveness** | How do names stand out on shelf? Short vs long? Native language vs foreign? |

### Tech / SaaS

| # | Dimension | Description |
|---|-----------|-------------|
| V1 | **naming_convention_tech** | Coined names (Spotify, Asana) vs descriptive (Salesforce, Shopify) vs acronyms? |
| V2 | **developer_friendliness** | Is name easy to type, google, reference in code/docs? Case sensitivity? |

### Logistics / Industrial

| # | Dimension | Description |
|---|-----------|-------------|
| V1 | **naming_convention_logistics** | Geographic anchors, movement metaphors, reliability signals, acronyms? |
| V2 | **b2b_naming_trust** | Do names signal scale, infrastructure, precision? Or agility, innovation? |

### Services / Agency

| # | Dimension | Description |
|---|-----------|-------------|
| V1 | **naming_convention_services** | Founder names, methodology names, abstract concepts, descriptive? |
| V2 | **expertise_signals** | Do names claim specialization or breadth? |

---

## Dimension Selection Workflow

Same as brand-strategy: auto-detect → propose → confirm.

**Total per project:** 17 fixed (Layer 1) + 6 linguistic (Layer 2) + 2 industry-specific = ~25 dimensions.

Layer 1 runs as Parallel AI tasks (one per competitor).
Layer 2 runs as a separate research task (market-wide, not per-competitor).
