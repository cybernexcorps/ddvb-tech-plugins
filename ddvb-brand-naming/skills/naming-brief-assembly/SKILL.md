---
name: naming-brief-assembly
description: "Copywriter naming brief production. Use when assembling a naming brief from research data, positioning materials, and competitive analysis. Produces semantic field, strategy recommendations, selection criteria, taboo list, and inspiration facts."
metadata:
  priority: 7
  pathPatterns:
    - "*naming_brief*"
    - "*brief*"
    - "NAMING_BRIEF*"
---

# Naming Brief Assembly

## Purpose

Produce a structured copywriter-facing naming brief from research data and client materials. The brief is an INTERNAL working document — not client-facing.

## Brief Structure

The naming brief follows this mandatory section sequence:

### 1. Project Context (1 page)

- Client company name and current brand status
- Industry and market
- Why renaming (rebranding, merger, new product, expansion, legal)
- Target audience (1-2 sentences)
- Positioning direction chosen (reference from brand strategy if available)
- Key constraint: timeline, budget, market scope

### 2. Materials Assessment

Table rating each source document by its value for naming:

| Document | Content | Value for Naming |
|----------|---------|------------------|
| [doc name] | [what it contains] | HIGH / MEDIUM / LOW — [why] |

### 3. Strategic Recommendation

Based on research, recommend:
- Which positioning direction best supports naming (if multiple exist)
- Why this direction creates the strongest naming territory
- What brand archetype the name should embody
- 1-paragraph argument for the recommendation

### 4. Competitive Name Map

Visual representation of the competitive naming landscape:

```
DESCRIPTIVE ←——————————→ ABSTRACT
    |                        |
    |  [Competitor A]        |  [Competitor C]
    |  [Competitor B]        |
    |                        |  [Competitor D]
    |                        |
INSTITUTIONAL ←————————→ EMOTIONAL
```

Plus a table:

| Competitor | Name Type | Archetype | Semantic Territory | Threat to Us |
|------------|-----------|-----------|-------------------|--------------|

### 5. Semantic Field

7-10 core concepts the name should evoke. Organized by priority:

**Primary (must resonate):**
1. [Concept] — why it matters, connection to positioning
2. [Concept] — ...
3. [Concept] — ...

**Secondary (nice to have):**
4. [Concept] — ...
5. [Concept] — ...

**Aspirational (Phase II / future):**
6. [Concept] — ...
7. [Concept] — ...

### 6. Naming Strategy Recommendation

Based on competitive landscape and positioning, recommend 2-3 naming strategies from `references/naming-strategies.md`:

```
Primary: [Strategy] — [why it fits this project]
Secondary: [Strategy] — [why it's a backup]
Avoid: [Strategy] — [why it doesn't work here]
```

### 7. Selection Criteria

**Mandatory (all must pass):**
1. [Criterion] — [rationale]
2. [Criterion] — [rationale]
3. [Criterion] — [rationale]
4. [Criterion] — [rationale]
5. [Criterion] — [rationale]
6. [Criterion] — [rationale]

**Desired (strengthens the candidate):**
1. [Criterion] — [rationale]
2. [Criterion] — [rationale]
3. [Criterion] — [rationale]

Standard mandatory criteria to consider:
- Pronounceable in all target languages
- No negative connotations in target languages
- Domain availability (.com + local TLDs)
- Trademarkable in required classes
- Visually distinctive (can form a strong logo)
- Not confusable with direct competitors

Standard desired criteria to consider:
- Works as a verb or has verbal form potential
- Short (≤3 syllables)
- Has natural abbreviation
- Scales to sub-brands

### 8. Taboo List

What to AVOID — compiled from competitive research and linguistic audit:

**Names/patterns to avoid:**
- [Pattern] — [why, e.g., "occupied by competitor X"]

**Sounds/roots to avoid:**
- [Sound/root] — [why, e.g., "negative connotation in Kazakh"]

**Semantic territories to avoid:**
- [Territory] — [why, e.g., "saturated, 4 competitors already there"]

### 9. Inspiration Facts

Non-obvious facts about the company, market, or culture that could spark naming ideas:

- [Fact] — [naming potential]
- [Fact] — [naming potential]
- [Fact] — [naming potential]

Sources: client interviews, research findings, market context.

### 10. Expected Deliverables

```
From copywriter:
1. Long-list: 50-80 candidates (categorized by naming strategy)
2. Self-evaluation: top 15 with rationale
3. Short-list: final 8-10 (after DDVB team review)
→ DDVB selects final 3-5 for client presentation
```

## Output

Save as `NAMING_BRIEF_FOR_COPYWRITER.md` in the project directory.

## Language Rules

- Write in the same language as source materials (usually Russian)
- Technical branding terms can stay in English (archetype, positioning, etc.)
- Tone: professional, directive, clear — this is a working document
- Use «кавычки» for Russian quotes, "quotes" for English
