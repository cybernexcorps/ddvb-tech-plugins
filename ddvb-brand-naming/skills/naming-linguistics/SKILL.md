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

Three-tier approach, from most to least automated:

#### Tier 1: EUIPO API (EU marks — official, free, automated)

Official REST API. Register at https://dev.euipo.europa.eu/, get API key.

```bash
# Search for a name in Nice classes 35 and 42
curl -X GET \
  'https://api.euipo.europa.eu/trademark-search/trademarks?query=wordMarkSpecification.verbalElement==*CANDIDATE*%20and%20niceClasses%3Dall%3D(35,42)&page=0&size=10' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'X-IBM-Client-Id: YOUR_CLIENT_ID'
```

RSQL query syntax:
- `wordMarkSpecification.verbalElement==*NAME*` — fuzzy name match
- `niceClasses=all=(35,42)` — filter by Nice classes
- `status==REGISTERED` — only registered marks
- `applicationDate>=2020-01-01` — date filter

Covers ~3.1M EU trademarks (EUTM). Does NOT cover Russian or Kazakh national marks.

**Setup:** Environment variable `EUIPO_CLIENT_ID` required. Get it free at dev.euipo.europa.eu.

#### Tier 2: WIPO Global Brand Database (international marks — semi-automated)

Covers marks with international protection via Madrid System:
- Russia (RU): ~404K marks
- Kazakhstan (KZ): ~207K marks
- EU (EM): ~3.1M marks

**Limitation:** Only Madrid-system marks designated to RU/KZ, NOT purely national marks filed directly with Rospatent. Coverage is partial.

**Automation status:** The API at `api.branddb.wipo.int/search` exists but:
- Requires solving an Altcha proof-of-work CAPTCHA (SHA-256)
- Responses are AES-encrypted
- TOS prohibits automated querying

**Practical approach for WIPO:** Use web search to query WIPO Brand Database results:
```
Search: site:branddb.wipo.int "CANDIDATE NAME" OR "CANDIDATE"
```
Or instruct the user to check manually at https://branddb.wipo.int with filters: Designation=RU, Nice Class=[relevant].

#### Tier 3: Rospatent / FIPS (Russian national marks — manual + web search)

The complete Russian trademark database (including national-only marks not in WIPO) is at:
- **Open Register:** https://new.fips.ru/registers-web/ — free, limited search, granted marks only
- **Open API portal:** https://online.rospatent.gov.ru/open-data/open-api — may have API access (investigate per project)
- **Paid ISS:** https://new.fips.ru/iiss/ — comprehensive, ~15-30K RUB/year subscription

**Note:** The Rospatent Open API at `searchplatform.rospatent.gov.ru/patsearch/v0.2/` covers **patents only**, NOT trademarks.

**Practical approach for Rospatent:** Use web search as a proxy:
```bash
# Search for trademark conflicts via web
Web search: "товарный знак" "CANDIDATE" site:new.fips.ru OR site:fips.ru
Web search: "CANDIDATE" МКТУ [class number] товарный знак Россия
```

#### Tier 4: Kazakhstan NIIS (Kazakh marks — manual)

- **Registry:** https://niis.kz — trademark search interface
- No known public API
- Use web search: `"CANDIDATE" товарный знак site:niis.kz`

### Trademark Check Automation Summary

| Source | Method | Coverage | Completeness |
|--------|--------|----------|-------------|
| EUIPO API | REST API (automated) | EU marks | Full |
| WIPO Brand DB | Web search (semi-auto) | International marks in RU/KZ | Partial (~60-70% of RU marks) |
| Rospatent FIPS | Web search (semi-auto) | Russian national marks | Partial (granted only via free register) |
| NIIS KZ | Web search (manual) | Kazakh marks | Low |

**Always add disclaimer:** "Trademark search results are preliminary. A professional trademark attorney search through FIPS ISS (paid) is recommended before filing."

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
