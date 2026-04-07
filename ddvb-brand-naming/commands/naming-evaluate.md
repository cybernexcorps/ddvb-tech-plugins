---
name: naming-evaluate
description: "Phase 3: Score candidates across 10 dimensions, produce ranked short-list."
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Agent, WebSearch, WebFetch
argument-hint: "[path-to-long-list]"
---

# Phase 3: Candidate Evaluation

Score and rank name candidates from the copywriter's long-list.

## Prerequisites

- `NAMING_BRIEF_FOR_COPYWRITER.md` must exist
- Copywriter has returned a long-list (50-80 candidates)

## Step 1: Import Long-List

Accept candidates from:
- `$ARGUMENTS` path to a file
- User pasting candidates directly
- File in the working directory

Parse each candidate into: name, strategy type, copywriter's rationale (if provided).

## Step 2: Review Evaluation Weights

Read `references/evaluation-matrix.md`. Present default weights:

```
Brand-Strategic:
1. Brand fit (20%)    2. Differentiation (15%)    3. Emotional resonance (10%)
4. Story potential (10%)    5. Scalability (5%)

Practical-Linguistic:
6. Memorability (15%)    7. Pronounceability (10%)    8. Domain availability (5%)
9. Visual/logo potential (5%)    10. Abbreviation quality (5%)
```

Propose weight adjustments based on project context:
- International → boost Pronounceability
- Digital-first → boost Domain
- Heritage rebrand → boost Brand Fit

**Get user confirmation** on weights before scoring.

## Step 3: Automated Pre-Screen

Run automated checks on ALL candidates:
1. Domain availability (.com + local TLDs)
2. Social handle availability
3. Trademark database search
4. Cross-language phonetic screen

Auto-disqualify:
- Exact trademark match in same ICGS class
- Negative meaning in primary target language
- Identical to direct competitor

Report disqualified candidates with reasons. Present count: "X of Y candidates pass pre-screen."

## Step 4: Score

Score each surviving candidate across all 10 dimensions. For each:
- AI assigns initial score with rationale
- Flag low-confidence scores for human review

Produce the full scoring matrix table (see evaluation-matrix.md for format).

Calculate weighted totals. Sort descending.

## Step 5: Produce Short-List

Select top 8-10 candidates. For each, provide:
- Weighted total score
- Score breakdown by dimension
- Top 3 strengths
- Top 2 risks
- Overall recommendation: PROCEED / CAUTION / DROP

Save to `evaluation/short_list.md`.

## Step 6: Gate Check

Present short-list to user:
1. Ranked table with scores
2. Per-candidate analysis (strengths + risks)
3. **Ask:** "Select 3-5 candidates for the final presentation. Or adjust the short-list?"

Save final selection to `evaluation/final_candidates.md`.

## After Selection

If user wants a client-facing deck → proceed to `/naming-present`.
Otherwise, the evaluation deliverables are the final output.
