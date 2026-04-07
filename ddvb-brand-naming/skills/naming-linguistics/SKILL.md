---
name: naming-linguistics
description: "Linguistic analysis for naming: phonetic patterns, cross-language connotation checks, morphological analysis, and automated domain/social/trademark availability checks. Use when analyzing name candidates or building the linguistic landscape for a naming brief."
metadata:
  priority: 6
  pathPatterns:
    - "*linguistic*"
    - "*phonetic*"
    - "*domain*"
    - "*trademark*"
---

# Naming Linguistics

## Purpose

Provide linguistic rigor for naming projects: phonetic analysis, cross-language connotation scanning, morphological analysis, and automated availability checks.

## Target Languages

**Default:** Russian + English (always checked).
**Additional:** Ask user based on:
- Client's target markets
- Languages detected in brief materials
- Competitor name languages from research

## Phonetic Analysis

For each target language, analyze:

### Sound Symbolism

| Sound Type | Association | Example |
|------------|-------------|---------|
| Hard plosives (K, T, P, B, D, G) | Strength, precision, impact | Kodak, Toyota |
| Soft liquids (L, M, N, R) | Warmth, flow, elegance | Lululemon, Muji |
| Sibilants (S, Sh, Z) | Speed, technology, sleekness | Cisco, Zoom |
| Vowel-dominant (A, O) | Openness, scale, approachability | Amazon, Ozon |

### Cross-Language Check Matrix

For each name candidate, check across all target languages:

```
| Candidate | Russian | English | [Lang 3] | Risk Level |
|-----------|---------|---------|----------|------------|
| [Name]    | [meaning/association] | [meaning/association] | ... | LOW/MED/HIGH |
```

Flags:
- **RED** — Negative meaning, profanity, or offensive association in any target language
- **YELLOW** — Ambiguous pronunciation, confusable with negative word, awkward phonetics
- **GREEN** — Clean across all languages

### Morphological Analysis

For coined/blended names:
- Component roots and their meanings
- Derivation potential (can it verb? can it adjective?)
- Diminutive/informal forms (what will people actually call it?)
- Abbreviation behavior (initials, first syllable, etc.)

## Automated Availability Checks

### Domain Availability

Check these TLDs for each candidate:

**Always:** `.com`
**If Russian market:** `.ru`, `.рф`
**If Kazakhstan:** `.kz`
**If Czech/EU:** `.cz`, `.eu`, `.de`
**If global:** `.io`, `.co`, `.app`

Method: DNS lookup via Bash:
```bash
for name in candidate1 candidate2 candidate3; do
  for tld in com ru kz; do
    domain="${name}.${tld}"
    if nslookup "$domain" > /dev/null 2>&1; then
      echo "TAKEN: $domain"
    else
      echo "AVAILABLE: $domain"
    fi
  done
done
```

Also check common variations: brand-name.com, getbrand.com, brand-group.com.

### Social Handle Availability

Check availability on:
- **Telegram:** @candidate (use web search: t.me/candidate)
- **Instagram:** @candidate (use web search: instagram.com/candidate)
- **VK:** vk.com/candidate (for Russian market)
- **LinkedIn:** company page (use web search)

Method: Web fetch or search for each platform + handle.

### Trademark Database Search

Check in relevant registries:

| Registry | Market | URL / Method |
|----------|--------|-------------|
| Rospatent (ФИПС) | Russia | fips.ru — search by name in relevant ICGS classes |
| NIIS Kazakhstan | Kazakhstan | niis.kz — trademark search |
| WIPO Global Brand Database | International | branddb.wipo.int — search across jurisdictions |
| EUIPO | EU | euipo.europa.eu — EU trademark search |

Method: Web search for each candidate + registry. Flag exact matches and confusingly similar marks in the same ICGS class.

**Key ICGS classes by industry:**
- Logistics: 35 (business management), 39 (transport/storage)
- Finance: 36 (insurance/financial), 35 (business services)
- FMCG/Food: 29 (food products), 30 (staple foods), 32 (beverages)
- Tech/SaaS: 9 (software), 42 (tech services), 35 (business services)
- Services/Agency: 35 (advertising), 41 (education), 42 (design)

## Output Format

### Per-Candidate Linguistic Report

```markdown
## [Candidate Name]

**Phonetics:** [syllable count] syllables, [stress pattern], [sound character: hard/soft/mixed]
**Russian:** [meaning/association or "no meaning"]
**English:** [meaning/association or "no meaning"]
**[Lang 3]:** [meaning/association or "no meaning"]
**Risk level:** GREEN / YELLOW / RED
**Morphology:** [root analysis, derivation potential]
**Domain:** .com [✓/✗], .ru [✓/✗], .kz [✓/✗]
**Social:** TG [✓/✗], IG [✓/✗], VK [✓/✗]
**Trademark:** [class] — [clear / conflict with X]
```

### Batch Summary Table

```markdown
| # | Candidate | Syllables | RU | EN | Domain .com | TG | TM Risk | Overall |
|---|-----------|-----------|----|----|-------------|-----|---------|---------|
| 1 | [Name]    | 2         | ✓  | ✓  | ✓           | ✓   | LOW     | GREEN   |
| 2 | [Name]    | 3         | ✓  | ⚠  | ✗           | ✓   | MED     | YELLOW  |
```
