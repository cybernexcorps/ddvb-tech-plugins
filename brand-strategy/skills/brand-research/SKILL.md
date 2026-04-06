---
name: brand-research
description: "PDF/PPTX data extraction patterns for brand strategy projects. Use when reading briefs, market reports, brand health trackers, or survey data from PDF/PPTX files."
metadata:
  priority: 5
  pathPatterns:
    - "*.pdf"
    - "*.pptx"
    - "analysis/spec_summary*"
  bashPatterns:
    - "pdfplumber"
    - "python-pptx"
---

# Brand Research Extraction Patterns

## PDF Extraction

Always use `pdfplumber` — never `pdftoppm`, `PyPDF2`, or shell tools.

```python
import pdfplumber

with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages):
        text = page.extract_text()
        tables = page.extract_tables()
        if text:
            print(f"=== PAGE {i+1} ===")
            print(text)
        if tables:
            for table in tables:
                # Process table rows
                pass
```

## PPTX Extraction

Use `python-pptx` for PowerPoint files:

```python
from pptx import Presentation

prs = Presentation(pptx_path)
for i, slide in enumerate(prs.slides):
    for shape in slide.shapes:
        if shape.has_text_frame:
            print(shape.text_frame.text)
```

## Parallel Extraction

When 3+ source files exist, use the Agent tool to extract from multiple files simultaneously. Each agent processes one file and returns full text.

## Common Data Patterns in Brand Briefs

| Data Type | Where to Find | How to Extract |
|-----------|--------------|----------------|
| Brand awareness | Health tracker PPTX/PDF | Tables with % values |
| Market share | MOEX/exchange reports | Key metrics pages |
| Competitor factors | Qualitative research PDF | Factor ranking tables |
| Product preferences | Quantitative survey PDF | Crosstabs, segment breakdowns |
| Client demographics | Survey/tracker | Age, gender, asset distributions |
| Archetype mapping | Audit/strategy PDF | Visual archetype wheel (may be image-only) |

## Garbled Filenames

Russian PDF filenames often get corrupted on Windows. Use glob patterns to find files:
```python
from pathlib import Path
pdfs = list(Path(".").glob("*.pdf"))
```
