# Naming Evaluation Matrix

## Scoring Dimensions (10)

### Brand-Strategic (5)

| # | Dimension | Weight | Description | Score 1 | Score 5 |
|---|-----------|--------|-------------|---------|---------|
| 1 | **Brand fit** | 20% | How well the name aligns with the chosen positioning and archetype | Contradicts positioning | Perfect embodiment |
| 2 | **Differentiation** | 15% | Distance from competitor names in sound, meaning, and associations | Confusable with competitor | Completely unique territory |
| 3 | **Emotional resonance** | 10% | Emotional response the name evokes in the target audience | Neutral/flat | Strong positive emotion |
| 4 | **Story potential** | 10% | Can the name anchor a brand narrative? Does it invite questions? | No story, just a label | Rich narrative potential |
| 5 | **Scalability** | 5% | Can the name support sub-brands, product lines, geographic expansion? | Limits growth | Infinite extension |

### Practical-Linguistic (5)

| # | Dimension | Weight | Description | Score 1 | Score 5 |
|---|-----------|--------|-------------|---------|---------|
| 6 | **Memorability** | 15% | Easy to remember after one hearing | Forgettable | Sticks instantly |
| 7 | **Pronounceability** | 10% | Easy to say correctly in all target languages | Tongue-twister / ambiguous | Intuitive in all languages |
| 8 | **Domain availability** | 5% | .com and local TLD availability | Nothing available | Exact .com available |
| 9 | **Visual/logo potential** | 5% | Letterforms, symmetry, icon potential, distinctiveness when rendered | Generic / visually flat | Strong visual identity inherent |
| 10 | **Abbreviation quality** | 5% | Natural short form, initials, hashtag potential | Bad abbreviation / clash | Clean abbreviation |

**Total: 100%**

## Scoring Scale

| Score | Meaning |
|-------|---------|
| 5 | Excellent — among the best possible outcomes |
| 4 | Strong — clearly above average, minor issues at most |
| 3 | Adequate — meets requirements, nothing special |
| 2 | Weak — notable problems, needs justification to proceed |
| 1 | Fail — disqualifying issue or major misalignment |

## Weighted Score Calculation

```
Final Score = Σ (dimension_score × weight) / 5 × 100
```

Maximum: 100 points. Minimum passing: 60 points.

## Evaluation Process

### Step 1: Import Long-List

Accept the copywriter's long-list (50-80 candidates). Parse into structured format:
- Name
- Strategy type (descriptive, metaphorical, coined, etc.)
- Copywriter's rationale (if provided)

### Step 2: Automated Pre-Screen

Run automated checks on ALL candidates before scoring:

1. **Domain check** — .com, .ru, .kz (and other relevant TLDs)
2. **Social handle check** — Telegram, Instagram, VK
3. **Trademark search** — Rospatent, NIIS KZ, WIPO
4. **Phonetic screen** — flag names with negative connotations in target languages

Auto-disqualify candidates that fail hard requirements:
- Exact match with existing trademark in the same class
- Negative meaning in primary target language
- Identical to a direct competitor's name

### Step 3: Score Remaining Candidates

For each surviving candidate, score across all 10 dimensions. Use AI-assisted scoring with human override:

```markdown
| Candidate | Brand Fit (20%) | Diff (15%) | Emotion (10%) | Story (10%) | Scale (5%) | Memory (15%) | Pronounce (10%) | Domain (5%) | Visual (5%) | Abbrev (5%) | **Total** |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [Name 1]  | 4 | 5 | 3 | 4 | 3 | 5 | 4 | 2 | 4 | 3 | **76** |
| [Name 2]  | 5 | 4 | 4 | 3 | 4 | 4 | 5 | 4 | 3 | 4 | **82** |
```

### Step 4: Produce Short-List

Rank by total score. Present top 8-10 with:
- Score breakdown per dimension
- Key strengths (top 3 dimensions)
- Key risks (bottom 2 dimensions)
- Recommendation: proceed / caution / drop

### Step 5: Gate Check

Present short-list to user. User selects final 3-5 for client presentation.

## Output Files

```
evaluation/
├── long_list_import.md          # Raw imported candidates
├── automated_screening.md       # Pre-screen results (domain, trademark, phonetic)
├── scoring_matrix.md            # Full scoring table
├── short_list.md                # Top 8-10 with analysis
└── final_candidates.md          # User-selected 3-5 for presentation
```

## Adapting Weights

Default weights work for most projects. Adjust when:

- **International launch** → increase Pronounceability to 15%, decrease Story to 5%
- **Startup / VC-backed** → increase Memorability to 20%, decrease Scalability to 0%
- **Heritage rebrand** → increase Brand Fit to 25%, add Heritage Continuity dimension
- **Digital-first** → increase Domain to 10%, add SEO/Searchability dimension

Present weight adjustments to user for confirmation before scoring.
