---
name: naming-evaluation
description: "Score and rank name candidates using a weighted evaluation matrix. Use when evaluating a long-list of name candidates from a copywriter, filtering to short-list, or producing a scored comparison for stakeholder review."
metadata:
  priority: 7
  pathPatterns:
    - "*candidates*"
    - "*long_list*"
    - "*short_list*"
    - "*evaluation*"
---

# Naming Evaluation

## Purpose

Score name candidates across 10 weighted dimensions (5 brand-strategic + 5 practical-linguistic), produce a ranked short-list, and support final candidate selection.

## Workflow

See `references/evaluation-matrix.md` for the full scoring framework, dimension definitions, weights, and scale.

### 1. Import

Accept the long-list from the copywriter (50-80 candidates). Sources:
- Markdown file with candidates
- User pasting candidates directly
- AI-generated seed list from `/naming-generate`

Parse each candidate into: name, strategy type, rationale.

### 2. Pre-Screen (Automated)

Run automated checks before manual scoring:
- Domain availability (.com + local TLDs)
- Social handle availability (Telegram, Instagram, VK)
- Trademark database search
- Cross-language phonetic screen

Auto-disqualify hard failures. Flag borderline cases.

### 3. Score

Score each surviving candidate across 10 dimensions (see evaluation-matrix.md). Present as a sortable matrix table.

### 4. Rank & Short-List

Top 8-10 by weighted score. For each:
- Score breakdown
- Key strengths (top 3 dims)
- Key risks (bottom 2 dims)
- Recommendation: proceed / caution / drop

### 5. Gate

User selects final 3-5 for client presentation (if `/naming-present` will be used).

## Weight Adjustment

Default weights suit most projects. Propose adjustments based on brief context:
- International → boost Pronounceability
- Digital-first → boost Domain, add SEO
- Heritage → boost Brand Fit, add Continuity
- Startup → boost Memorability

Always confirm weights with user before scoring.
