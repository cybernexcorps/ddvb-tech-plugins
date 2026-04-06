---
name: naming-research
description: "Two-layer competitive research for naming projects. Use when researching competitor names, brand archetypes, semantic territories, and linguistic landscape. Runs stripped brand dimensions via Parallel AI + linguistic audit with automated checks."
metadata:
  priority: 8
  pathPatterns:
    - "*naming*"
    - "*competitor*"
    - "research_reports/*"
---

# Naming Research — Two-Layer Framework

## Overview

Naming research runs in two layers:
- **Layer 1: Brand dimensions** — per-competitor research via Parallel AI (names, archetypes, semantic territories, tone, market position)
- **Layer 2: Linguistic audit** — market-wide analysis (phonetic patterns, connotation landscape, domain/social/trademark availability)

See `references/research-dimensions-naming.md` for the complete dimension catalog.

## Layer 1: Competitive Name Research

### Dimension Selection

1. Auto-detect industry from brief
2. Present 17 fixed dimensions + 2 industry-specific variable dimensions
3. Confirm with user

### Execution via Parallel AI

**Mode: Ultra** (depth over throughput for naming)

- 1 task per competitor, all parallel
- Each task covers all confirmed dimensions (typically 19)
- Focus the prompt on NAME-SPECIFIC insights — not full business analysis

### Key Differences from Brand-Strategy Research

- **Name origin analysis** (dim 4) — etymological, not just descriptive
- **Cross-language name meaning** (dim 5) — critical for multilingual markets
- **Semantic field mapping** (dim 10) — what associations are occupied
- **Occupied territories** (dim 13) — explicitly maps what's taken
- **No product/service deep dive** — we need names, not business models

### Output

```
research_reports/
├── 00_naming_landscape_summary.md    # Cross-competitor synthesis
├── 01_[competitor].md                # Per-competitor (17-19 dimensions)
├── ...
└── naming_territory_map.md           # Semantic territories: occupied vs free
```

## Layer 2: Linguistic Audit

Runs AFTER Layer 1 is complete. Uses findings from Layer 1 to focus the linguistic analysis.

### Target Languages

Default: **Russian + English**. Ask user for additional languages based on:
- Client's target markets
- Languages mentioned in the brief
- Competitor name languages detected in Layer 1

### Research Tasks

**Task A: Phonetic Landscape** (per language)
- Common phonetic patterns in the industry
- Sounds that carry positive associations (strength, trust, speed, innovation)
- Sounds to avoid (negative connotations, profanity, confusion with competitors)
- Syllable count norms for the industry

**Task B: Naming Availability Landscape** (market-wide)
- Domain patterns (.com, local TLDs)
- Social handle patterns (Telegram, Instagram, VK, LinkedIn)
- Trademark classes relevant to this industry
- Which registries to check

### Automated Checks (run after research)

Where possible, automate:
1. **Domain availability** — Check .com, .ru, .kz (and other relevant TLDs) via DNS lookup or WHOIS
2. **Social handle availability** — Check Telegram, Instagram, VK handle availability
3. **Trademark database search** — Query Rospatent, NIIS Kazakhstan, WIPO (where APIs exist)

Use Bash for DNS checks:
```bash
# Domain check
for domain in example.com example.ru example.kz; do
  if host "$domain" > /dev/null 2>&1; then
    echo "TAKEN: $domain"
  else
    echo "AVAILABLE: $domain"
  fi
done
```

Use web search for trademark checks where APIs aren't available.

### Output

```
research_reports/
├── linguistic_audit_ru.md           # Russian phonetic landscape
├── linguistic_audit_en.md           # English phonetic landscape
├── linguistic_audit_[lang].md       # Additional languages
├── availability_landscape.md        # Domain, social, trademark landscape
└── naming_constraints.md            # Compiled taboo list + positive signals
```

## Synthesizing Both Layers

After both layers complete, produce:

### `naming_landscape_complete.md`

1. **Competitor name map** — visual grid of all competitor names × naming strategy × archetype
2. **Occupied semantic territories** — what's taken, what's free
3. **Naming whitespace** — where the opportunity is
4. **Phonetic guidelines** — sounds to lean into, sounds to avoid
5. **Availability constraints** — TLD patterns, handle patterns, trademark classes
6. **Taboo list** — names, patterns, sounds, associations to avoid (compiled from both layers)
7. **Opportunity brief** — 3-5 recommended semantic territories with rationale

This synthesis feeds directly into the naming brief.
