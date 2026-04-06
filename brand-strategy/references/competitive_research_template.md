# Deep Research: {{CLIENT_NAME}} Competitive Analysis

<!-- 
  ADAPTIVE TEMPLATE
  
  This template has two sections:
  1. Fixed dimensions (1-17) — always included, universal across industries
  2. Variable dimensions (18+) — populated from industry preset after user confirmation
  
  Before using this template:
  1. Read references/research-dimensions.md for the dimension catalog
  2. Auto-detect industry from the brief
  3. Propose variable dimensions to the user
  4. Get confirmation, then populate {{VARIABLE_DIMENSIONS}} below
-->

## Agent Configuration

- **Execution model**: Parallel AI / Ultra — research all competitors simultaneously
- **Output**: Structured research report per competitor, covering all {{TOTAL_DIMENSIONS}} dimensions below
- **Language**: {{LANGUAGE}} for content. English terms acceptable for technical fields

---

## Objective

Research each competitor of **{{CLIENT_NAME}}** — {{CLIENT_DESCRIPTION}} — across {{TOTAL_DIMENSIONS}} defined dimensions. For each competitor, produce a structured research report organized by the dimension groups below.

## Strategic Context

{{CLIENT_NAME}} is repositioning toward **{{TARGET_SEGMENT}}**. The competitive analysis must reveal:
- How each competitor positions itself toward this target segment
- Where the whitespace opportunities exist for {{CLIENT_NAME}}
- What brand, product, and communication patterns dominate the market

---

## Competitors (parallel research tasks)

| # | Competitor | Type | Research Priority | Notes |
|---|-----------|------|-------------------|-------|
{{COMPETITOR_TABLE}}

---

## Fixed Dimensions (1-17) — Universal

For each dimension, provide a clear, concise answer. If information is not publicly available, write "Информация не найдена". Do NOT skip any dimension.

### A. Identification (3 dimensions)
1. **competitor_name** — Full name (in the market language)
2. **competitor_type** — Category within the industry
3. **parent_company** — Parent group/holding, or "Independent"

### B. Brand & Positioning (5 dimensions)
4. **brand_essence** — Core brand promise in 1-2 sentences. Quote actual tagline/slogan if available (in «кавычках»).
5. **brand_positioning** — Market positioning: mass-market, premium, niche, tech-forward, expert, accessible, etc.
6. **brand_archetype** — Dominant archetype (Hero, Sage, Creator, Magician, Explorer, Ruler, Caregiver, Regular Guy, Rebel, etc.) with 1-sentence justification.
7. **brand_image** — Visual identity: logo, primary colors (hex if possible), design language, aesthetic.
8. **tone_of_voice** — Communication tone: formal/informal, expert/accessible, aggressive/soft. Include 1-2 verbatim examples from ads or social media.

### C. Communication & Channels (4 dimensions)
9. **communication_channels** — All known channels: TV, digital, social, outdoor, content, events, sponsorships, influencer.
10. **social_media_presence** — Key accounts with follower counts. Cover: Telegram, VK, YouTube, Instagram, TikTok, Дзен (RU) or LinkedIn, X, Facebook (int'l).
11. **content_and_education** — Owned media: blogs, podcasts, newsletters, webinars, courses, media brands. Name specific products.
12. **key_messages** — 3-5 recurring themes in recent marketing. What do they repeatedly communicate?

### H. Market Position (4 dimensions)
13. **market_share_data** — Revenue, client count, industry rankings, volumes. Use most recent data. Flag data vintage.
14. **target_audience** — Primary target: segments, demographics, firmographics. Describe their ideal client/customer.
15. **competitive_advantages** — 3-5 key advantages vs. other players in the market.
16. **competitive_weaknesses** — 3-5 known weaknesses from public reviews, research, market perception.

### I. Source Attribution (1 dimension)
17. **sources** — Semicolon-separated list of key URLs/sources used. Minimum 3 per competitor.

---

## Variable Dimensions (18+) — {{INDUSTRY_LABEL}}

<!-- 
  Replace this entire section with the confirmed variable dimensions.
  Number sequentially starting from 18.
  Group into logical sections (D, E, F, G, etc.).
-->

{{VARIABLE_DIMENSIONS}}

---

## Output Format

For each competitor, structure the report as follows:

```
# [Competitor Name]

## A. Identification
1. competitor_name: ...
2. competitor_type: ...
3. parent_company: ...

## B. Brand & Positioning
4. brand_essence: ...
5. brand_positioning: ...
6. brand_archetype: ...
7. brand_image: ...
8. tone_of_voice: ...

## C. Communication & Channels
9. communication_channels: ...
10. social_media_presence: ...
11. content_and_education: ...
12. key_messages: ...

## H. Market Position
13. market_share_data: ...
14. target_audience: ...
15. competitive_advantages: ...
16. competitive_weaknesses: ...

## I. Sources
17. sources: ...

## {{VARIABLE_SECTION_LABEL}}
18. [first variable dimension]: ...
19. [second variable dimension]: ...
... (continue through all variable dimensions)
```

**Requirements:**
- Use the exact dimension numbering and field names as shown above
- Keep each answer concise but specific (1-3 sentences, more for critical dimensions)
- {{LANGUAGE}} content, English technical terms acceptable
- No skipped dimensions — use "Информация не найдена" for missing data

---

## Research Guidelines

### Source Priority
1. **Official websites** of each competitor (highest priority)
2. **Industry regulators and rankings** (e.g., MOEX, CBR, Euromonitor, Gartner, G2 — whatever applies)
3. **App stores** — ratings and reviews (if digital products exist)
4. **Industry media** — trade publications, analyst reports
5. **Social media accounts** — direct observation of tone, content, followers
6. **Company press releases and annual reports**

### Quality Requirements
1. **Cross-reference**: 2-3 sources per factual claim minimum
2. **Recency**: current year data preferred. Flag explicitly if older
3. **Specificity**: Not "has a mobile app" → specific name, rating, features
4. **Verbatim quotes**: include actual slogans, taglines in «кавычках»
5. **Gap documentation**: absence of data IS data — state explicitly
6. **No hallucination**: if uncertain, write "Информация не найдена"

---

## {{CLIENT_NAME}} Reference Point (DO NOT include in CSV — for calibration only)

{{CLIENT_REFERENCE_POINT}}

---

## Execution Notes for Parallel AI / Ultra

- Run all competitors as **parallel research tasks**
- Each task should be self-contained: one competitor, all {{TOTAL_DIMENSIONS}} dimensions
- HIGH priority competitors may require deeper research depth
- MEDIUM priority competitors can use standard depth but must still cover all dimensions
- Each parallel task outputs one structured competitor report following the format above
- The reports will be merged into a CSV separately after research is complete
