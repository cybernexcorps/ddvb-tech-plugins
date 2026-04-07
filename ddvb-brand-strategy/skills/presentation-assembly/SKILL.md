---
name: presentation-assembly
description: "PPTX presentation assembly for brand strategy deliverables. Use when building PowerPoint slides with python-pptx, inserting backgrounds, creating native shapes, or combining PNG figures with text."
metadata:
  priority: 5
  pathPatterns:
    - "scripts/build_presentation.py"
    - "*.pptx"
  bashPatterns:
    - "python-pptx"
    - "build_presentation"
---

# Presentation Assembly

## Slide Architecture

### When to Use Native PPTX vs PNG

| Content Type | Approach | Why |
|-------------|----------|-----|
| SWOT analysis | **Native PPTX** | Colored rectangles + text = crisp at any zoom |
| Values list | **Native PPTX** | Simple text + color bars |
| Communication cards | **Native PPTX** | Structured cards with borders |
| Typography specimen | **Native PPTX** | Shows actual fonts, not a picture of fonts |
| Brand architecture | **Native PPTX** | Boxes + arrows |
| Key metrics | **Native PPTX** | Large numbers + labels |
| Competitive map | **PNG** | Complex scatter plot hard to replicate in PPTX |
| Brand wheel | **PNG** | Concentric circles with many labels |
| Ad mockups | **PNG (dark)** | Creative mockups intentionally dark |
| Graphic device | **PNG (dark)** | Visual effects need matplotlib rendering |
| Applied identity | **PNG (dark)** | Composite mockup layout |
| Color swatches | **PNG** | Many small colored rectangles + hex codes |

### Slide Layout Rules

1. **Every slide has a header** — `"0X  Title"` in Atyp Display 26pt, at (0.8", 0.35")
2. **Orange slides** for title + closing (DDVB `background_2.png` or `background_4.png`)
3. **White slides** for content (DDVB `background_7.png` with markers)
4. **Grid slides** for data-heavy content (`background_8.png`)
5. **PNG images get constrained dimensions** — never exceed slide height (5.625")

### DDVB Background Integration

If the `ddvb-brand-guidelines` skill is available, use its pre-made 4K backgrounds:
```python
BG_DIR = Path.home() / ".claude/skills/ddvb-brand-guidelines/resources/backgrounds"
```

Insert as full-slide image sent to back:
```python
pic = slide.shapes.add_picture(str(bg_path), 0, 0,
                                width=prs.slide_width, height=prs.slide_height)
sp = pic._element
slide.shapes._spTree.remove(sp)
slide.shapes._spTree.insert(2, sp)
```

### Helper Functions Pattern

```python
def txt(slide, l, t, w, h, text, font="Atyp Text", sz=18, color=BLACK,
        bold=False, align=PP_ALIGN.LEFT):
    """Add formatted text box."""

def header(slide, num, title, color=BLACK):
    """Standard slide header."""
    txt(slide, 0.8, 0.35, 8.4, 0.5, f"{num}  {title}", "Atyp Display", 26, color, bold=True)

def rect(slide, l, t, w, h, fill_color):
    """Add rounded rectangle."""

def img(slide, path, l, t, w=None, h=None):
    """Add image with optional sizing."""
```

### File Locking

If the PPTX file is open in PowerPoint, `prs.save()` will throw `PermissionError`. Handle by saving with a version suffix:
```python
for v in range(1, 10):
    try:
        prs.save(f"Presentation_v{v}.pptx")
        break
    except PermissionError:
        continue
```

### Size Budget

Target: under 15MB for the final PPTX.
- DDVB backgrounds: ~0.5MB total (4K PNGs)
- Generated figures: ~1-2MB (9 PNGs at 250 DPI)
- Native PPTX shapes: negligible
- Typical total: 1-3MB
