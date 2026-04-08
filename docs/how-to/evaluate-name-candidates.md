# How to Evaluate Name Candidates

Score the copywriter's long-list and produce a ranked short-list.

## When to Use

The copywriter has returned 50-80 name candidates. You need to systematically evaluate them and select 3-5 finalists.

## What You Need

- The copywriter's long-list (as a markdown file, text file, or pasted directly)
- `NAMING_BRIEF_FOR_COPYWRITER.md` from Phase 1 (for context)
- 30-60 minutes for the evaluation process

## Steps

### 1. Import the long-list

```
/ddvb-brand-naming:naming-evaluate path/to/long-list.md
```

Or paste the candidates directly into the chat. Claude parses each candidate into: name, strategy type, and copywriter's rationale (if provided).

### 2. Review the evaluation weights

Claude proposes default weights:

| Dimension | Default Weight |
|-----------|---------------|
| Brand fit | 20% |
| Differentiation | 15% |
| Memorability | 15% |
| Emotional resonance | 10% |
| Pronounceability | 10% |
| Story potential | 10% |
| Domain availability | 5% |
| Scalability | 5% |
| Visual/logo potential | 5% |
| Abbreviation quality | 5% |

Claude may suggest adjustments based on your project:
- **International launch?** Pronounceability goes up
- **Digital-first?** Domain availability goes up
- **Heritage rebrand?** Brand fit goes up

**Confirm the weights** before scoring begins.

### 3. Automated pre-screen

Claude runs automated checks on ALL candidates:

- **Domain availability** — .com + local TLDs (.ru, .kz, etc.)
- **Social handles** — Telegram, Instagram, VK
- **Trademark search** — EUIPO API (EU), WIPO (international), Rospatent (web search)
- **Phonetic screen** — Cross-language connotation check in target languages

Candidates with hard failures are auto-disqualified:
- Exact trademark match in the same Nice class
- Negative meaning in a target language
- Identical to a direct competitor

Claude reports: *"47 of 62 candidates pass pre-screen. 15 disqualified."* — with reasons for each.

### 4. Scoring

Claude scores each surviving candidate across all 10 dimensions, producing a table:

```
| # | Candidate | Brand | Diff | Memory | Emotion | Pronoun | Story | Domain | Scale | Visual | Abbrev | Total |
|---|-----------|-------|------|--------|---------|---------|-------|--------|-------|--------|--------|-------|
| 1 | MERIDIAN  |  5    |  5   |   4    |   4     |   4     |  5    |   4    |  4    |   5    |   3    |  87   |
| 2 | VECTOR    |  4    |  3   |   5    |   3     |   5     |  3    |   3    |  4    |   4    |   4    |  75   |
```

Low-confidence scores are flagged for your review.

### 5. Short-list

Claude presents the top 8-10 candidates with:
- Score breakdown
- Top 3 strengths
- Top 2 risks
- Recommendation: **PROCEED** / **CAUTION** / **DROP**

### 6. Select finalists

Pick your final 3-5 candidates. Claude saves them to `evaluation/final_candidates.md`.

If you want a client-facing presentation, run `/ddvb-brand-naming:naming-present`.

## Understanding the Scores

### What makes a high score (80+)

- Strong brand fit — the name embodies the positioning and archetype
- Clear differentiation — no competitor has anything similar
- Memorable — sticks after one hearing
- Clean availability — domain, social handles, and trademark all clear
- Works in all target languages without negative associations

### What makes a low score (below 60)

- Fails one critical dimension (brand fit < 3 or pronounceability < 2)
- Domain and trademark conflicts
- Confusable with a competitor
- Doesn't scale (too narrow, too specific to one product)

### When to override the score

The scoring matrix is a tool, not a judge. Override when:
- A name scores low on domain but you know a creative workaround exists
- A name scores high overall but feels wrong — trust your gut and investigate why
- The client has a strong preference that the scoring doesn't capture

## Tips

- **Pre-screen saves time.** The automated checks eliminate obviously unavailable names before you spend time scoring.
- **Adjust weights for the project.** Don't use defaults blindly — a local Kazakhstan brand and a global SaaS startup need different weight distributions.
- **The copywriter's rationale matters.** If the copywriter flagged a name as their top pick, read their reasoning — it may reveal strengths the scoring matrix misses.
- **Keep 8-10, not 3.** The short-list should be 8-10 for internal discussion before narrowing to 3-5 for the client.
