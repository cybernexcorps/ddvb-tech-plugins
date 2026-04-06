"""Shared Atyp font configuration for all BCS visualization scripts."""

from pathlib import Path
from matplotlib import font_manager as fm

FONT_DIR = Path.home() / "AppData/Local/Microsoft/Windows/Fonts"

# ── Font paths ───────────────────────────────────────────────────────────────
_ATYP_FONTS = {
    "display_regular": FONT_DIR / "AtypDisplay-Regular.ttf",
    "display_medium":  FONT_DIR / "AtypDisplay-Medium.ttf",
    "display_semibold": FONT_DIR / "AtypDisplay-Semibold.ttf",
    "display_bold":    FONT_DIR / "AtypDisplay-Bold.ttf",
    "display_light":   FONT_DIR / "AtypDisplay-Light.ttf",
    "display_italic":  FONT_DIR / "AtypDisplay-Italic.ttf",
    "text_regular":    FONT_DIR / "AtypText-Regular.ttf",
    "text_medium":     FONT_DIR / "AtypText-Medium.ttf",
    "text_semibold":   FONT_DIR / "AtypText-Semibold.ttf",
    "text_bold":       FONT_DIR / "AtypText-Bold.ttf",
    "text_light":      FONT_DIR / "AtypText-Light.ttf",
}

# ── Register all fonts with matplotlib ───────────────────────────────────────
for _name, _path in _ATYP_FONTS.items():
    if _path.exists():
        fm.fontManager.addfont(str(_path))

# ── FontProperties objects for direct use ────────────────────────────────────
# Titles, headers (AtypDisplay)
FONT_TITLE = fm.FontProperties(fname=str(_ATYP_FONTS["display_bold"]))
FONT_SUBTITLE = fm.FontProperties(fname=str(_ATYP_FONTS["display_medium"]))
FONT_HEADER = fm.FontProperties(fname=str(_ATYP_FONTS["display_semibold"]))

# Body text, labels (AtypText)
FONT_BODY = fm.FontProperties(fname=str(_ATYP_FONTS["text_regular"]))
FONT_BODY_MEDIUM = fm.FontProperties(fname=str(_ATYP_FONTS["text_medium"]))
FONT_BODY_BOLD = fm.FontProperties(fname=str(_ATYP_FONTS["text_bold"]))
FONT_BODY_LIGHT = fm.FontProperties(fname=str(_ATYP_FONTS["text_light"]))
FONT_LABEL = fm.FontProperties(fname=str(_ATYP_FONTS["text_medium"]))
FONT_ANNOTATION = fm.FontProperties(fname=str(_ATYP_FONTS["text_light"]))


def font_props(role: str = "body", size: float = 10) -> fm.FontProperties:
    """Get a sized FontProperties by role name.

    Roles: title, subtitle, header, body, body_medium, body_bold, label, annotation
    """
    mapping = {
        "title": FONT_TITLE,
        "subtitle": FONT_SUBTITLE,
        "header": FONT_HEADER,
        "body": FONT_BODY,
        "body_medium": FONT_BODY_MEDIUM,
        "body_bold": FONT_BODY_BOLD,
        "body_light": FONT_BODY_LIGHT,
        "label": FONT_LABEL,
        "annotation": FONT_ANNOTATION,
    }
    fp = mapping.get(role, FONT_BODY).copy()
    fp.set_size(size)
    return fp
