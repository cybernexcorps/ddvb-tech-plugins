#!/usr/bin/env python3
"""Regenerate ALL figures for DDVB presentation: transparent bg, dark-on-light colors."""

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fonts import font_props

FIG_DIR = Path(__file__).resolve().parent.parent / "figures"
FIG_DIR.mkdir(exist_ok=True)

# ── Light-mode palette (for white DDVB backgrounds) ────────────────────────
GOLD = "#FDB71C"
BLACK = "#0D0D0D"
DARK = "#1A1A1A"
GRAY = "#44546A"
LGRAY = "#9E9E9E"
VLGRAY = "#D9D9D9"
WHITE = "#FFFFFF"
BLUE = "#1565C0"
VIOLET = "#6A1B9A"
AMBER = "#E65100"
GREEN = "#2E7D32"
RED = "#C62828"

DPI = 250


def _save(fig, name, pad=0.2, dark=False):
    out = FIG_DIR / name
    if dark:
        fig.savefig(out, dpi=DPI, bbox_inches="tight", facecolor="#0D0D0D",
                    pad_inches=pad, transparent=False)
    else:
        fig.savefig(out, dpi=DPI, bbox_inches="tight", transparent=True, pad_inches=pad)
    plt.close(fig)
    print(f"  {name} ({out.stat().st_size // 1024} KB)")


# ════════════════════════════════════════════════════════════════════════════
# 1. SWOT QUADRANT
# ════════════════════════════════════════════════════════════════════════════
def gen_swot():
    fig, axes = plt.subplots(2, 2, figsize=(12, 7.5))
    fig.patch.set_alpha(0)

    quadrants = [
        {"title": "STRENGTHS", "sub": "Сильные стороны", "color": GREEN, "items": [
            "S1  Крупнейший частный брокер РФ",
            "S2  30 лет экспертизы, рейтинг ruА-",
            "S3  Топ-3 по знанию в сегменте 2М+",
            "S4  Монолайнер — только инвестиции",
            "S5  Лидер инноваций (крипта, 24/7)",
            "S6  Экосистема полного цикла",
            "S7  25,4% оборотов MOEX (рекорд)",
        ]},
        {"title": "WEAKNESSES", "sub": "Слабые стороны", "color": RED, "items": [
            "W1  5-е место по узнаваемости (21%)",
            "W2  Конфликт: fintech внутри \u2260 образ",
            "W3  Низкая эмоц. близость (Likeability)",
            "W4  Коммуникация массовая и корпорат.",
            "W5  Восприятие \u00ABсложно\u00BB и \u00ABдавят\u00BB",
            "W6  Доля в кошельке клиента \u21934,5 п.п.",
            "W7  Приток новых клиентов \u219323%",
        ]},
        {"title": "OPPORTUNITIES", "sub": "Возможности", "color": BLUE, "items": [
            "O1  Архетип Маг/Искатель — свободен!",
            "O2  Сегмент 2М+ растёт (+0,11 п.п.)",
            "O3  Запрос: Sales \u2192 Partner/Enabler",
            "O4  Спрос на пассивный доход (56\u201360%)",
            "O5  Горизонт 3+ года (47\u201351% ЦА)",
            "O6  Fintech = топ-сектор для инвесторов",
            "O7  Независимость от банка = уник. образ",
        ]},
        {"title": "THREATS", "sub": "Угрозы", "color": AMBER, "items": [
            "T1  Банки доминируют: 93,5% активных кл.",
            "T2  \u00ABСвязан с банком\u00BB = топ-фактор",
            "T3  Финам — прямой конкурент, двойные сч.",
            "T4  Недоверие к фин. советникам",
            "T5  Геополитическая неопределённость",
            "T6  АТОН усиливается в HNWI",
            "T7  Эмоц. барьеры: страх потерь, сложность",
        ]},
    ]

    for ax, q in zip(axes.flat, quadrants):
        ax.set_facecolor("none")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_xticks([])
        ax.set_yticks([])

        # Header bar
        header = FancyBboxPatch(
            (0.02, 0.88), 0.96, 0.10,
            boxstyle="round,pad=0.02", facecolor=q["color"],
            edgecolor=q["color"], linewidth=0, alpha=0.9, zorder=5)
        ax.add_patch(header)

        ax.text(0.5, 0.935, q["title"], ha="center", va="center",
                fontproperties=font_props("header", 13), color=WHITE, zorder=10)

        n = len(q["items"])
        for i, item in enumerate(q["items"]):
            y = 0.82 - i * (0.78 / max(n, 1))
            ax.text(0.06, y, item, ha="left", va="top",
                    fontproperties=font_props("body", 8.5), color=DARK)

        for spine in ax.spines.values():
            spine.set_color(q["color"])
            spine.set_linewidth(1.5)
            spine.set_alpha(0.4)

    plt.subplots_adjust(hspace=0.12, wspace=0.08)
    _save(fig, "swot_quadrant.png")


# ════════════════════════════════════════════════════════════════════════════
# 2. COMPETITIVE MAP
# ════════════════════════════════════════════════════════════════════════════
def gen_competitive_map():
    competitors = {
        "СберИнвестиции":    (-0.65, -0.35, "#21A038"),
        "Т-Инвестиции":      (-0.50,  0.30, "#DAA520"),
        "Альфа Инвестиции":  (-0.35, -0.20, "#EF3124"),
        "ВТБ Мои инвестиции":(-0.55, -0.55, "#003082"),
        "Финам":             ( 0.15, -0.45, "#1A73E8"),
        "АТОН":              ( 0.70,  0.20, "#8E24AA"),
        "Газпромбанк Инв.":  ( 0.10, -0.25, "#0097A7"),
        "БКС (текущее)":     ( 0.05, -0.10, "#78909C"),
        "БКС (целевое)":     ( 0.40,  0.55, GOLD),
    }

    fig, ax = plt.subplots(figsize=(11, 7.5))
    fig.patch.set_alpha(0)
    ax.set_facecolor("none")

    # Light grid
    for v in np.arange(-0.8, 1.0, 0.2):
        ax.axhline(v, color=VLGRAY, linewidth=0.3, zorder=0)
        ax.axvline(v, color=VLGRAY, linewidth=0.3, zorder=0)
    ax.axhline(0, color=LGRAY, linewidth=1, zorder=1)
    ax.axvline(0, color=LGRAY, linewidth=1, zorder=1)

    # Quadrant labels
    for txt, x, y in [
        ("Массовый +\nЭмоциональный", -0.5, 0.78),
        ("Эксклюзивный +\nЭмоциональный", 0.5, 0.78),
        ("Массовый +\nРациональный", -0.5, -0.78),
        ("Эксклюзивный +\nРациональный", 0.5, -0.78),
    ]:
        ax.text(x, y, txt, fontproperties=font_props("annotation", 8),
                color=LGRAY, ha="center", va="center")

    # Arrow
    ax.annotate("", xy=(0.40, 0.55), xytext=(0.05, -0.10),
                arrowprops=dict(arrowstyle="-|>", color=GOLD, lw=2.5,
                                connectionstyle="arc3,rad=0.15"), zorder=3)

    for name, (x, y, color) in competitors.items():
        is_target = name == "БКС (целевое)"
        is_current = name == "БКС (текущее)"
        size = 200 if is_target else (130 if is_current else 100)
        edge = GOLD if is_target else "#999"
        ew = 2.5 if is_target else 0.8

        ax.scatter(x, y, s=size, c=color, edgecolors=edge,
                   linewidths=ew, zorder=5, marker="o")

        role = "header" if "БКС" in name else "body_medium"
        fsize = 10 if "БКС" in name else 8
        lcolor = DARK if not is_target else GOLD

        ax.text(x, y + 0.07, name, ha="center", va="bottom",
                fontproperties=font_props(role, fsize), color=lcolor, zorder=6)

    # Axis labels
    for txt, pos, ha, va in [
        ("ЭКСКЛЮЗИВНОСТЬ \u2192", (0.97, 0.48), "right", "center"),
        ("\u2190 МАССОВОСТЬ", (0.03, 0.48), "left", "center"),
        ("ЭМОЦИОНАЛЬНОСТЬ \u2191", (0.5, 0.98), "center", "top"),
        ("\u2193 РАЦИОНАЛЬНОСТЬ", (0.5, 0.02), "center", "bottom"),
    ]:
        ax.text(*pos, txt, transform=ax.transAxes,
                fontproperties=font_props("header", 9), color=GRAY, ha=ha, va=va)

    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    _save(fig, "competitive_map.png")


# ════════════════════════════════════════════════════════════════════════════
# 3. BRAND WHEEL
# ════════════════════════════════════════════════════════════════════════════
def gen_brand_wheel():
    fig, ax = plt.subplots(figsize=(9, 9))
    fig.patch.set_alpha(0)
    ax.set_facecolor("none")

    rings = [
        {"r": 4.2, "color": VLGRAY, "alpha": 0.15},
        {"r": 3.2, "color": VLGRAY, "alpha": 0.25},
        {"r": 2.1, "color": "#E8E8E8", "alpha": 0.4},
        {"r": 1.0, "color": GOLD, "alpha": 0.95},
    ]
    for ring in rings:
        ax.add_patch(plt.Circle((0, 0), ring["r"], facecolor=ring["color"],
                                edgecolor=VLGRAY, linewidth=0.8, alpha=ring["alpha"], zorder=1))

    # Core
    ax.text(0, 0.25, "АКТИВИРУЙ", ha="center", va="center",
            fontproperties=font_props("title", 20), color=BLACK, zorder=10)
    ax.text(0, -0.2, "БЛАГОСОСТОЯНИЕ", ha="center", va="center",
            fontproperties=font_props("header", 11), color=BLACK, zorder=10)

    # Archetype
    ax.text(0, 1.65, "МАГ 65%", ha="center", va="center",
            fontproperties=font_props("header", 11), color=VIOLET, zorder=10)
    ax.text(0, 1.38, "трансформация реальности",
            fontproperties=font_props("body", 7.5), color=GRAY, ha="center", zorder=10)
    ax.text(0, -1.65, "ИСКАТЕЛЬ 35%", ha="center", va="center",
            fontproperties=font_props("header", 11), color=BLUE, zorder=10)
    ax.text(0, -1.38, "новые горизонты",
            fontproperties=font_props("body", 7.5), color=GRAY, ha="center", zorder=10)

    # Values
    for name, sub, angle, color in [
        ("ЯСНОСТЬ", "Сложность \u2192 ясность", 45, BLUE),
        ("ТРАНСФОРМАЦИЯ", "Потенциал \u2192 капитал", 135, VIOLET),
        ("МАСТЕРСТВО", "30 лет \u2192 точность", 225, GREEN),
        ("СВОБОДА", "Средство \u2192 цель", 315, AMBER),
    ]:
        r = 2.7
        rad = np.radians(angle)
        x, y = r * np.cos(rad), r * np.sin(rad)
        ax.text(x, y + 0.12, name, ha="center", va="center",
                fontproperties=font_props("header", 10), color=color, zorder=10)
        ax.text(x, y - 0.15, sub, ha="center", va="center",
                fontproperties=font_props("annotation", 6.5), color=GRAY, zorder=10)

    # Character traits
    for text, angle in [("Прагматичный", 15), ("Энергичный", 75),
                        ("Вдохновляющий", 105), ("Инновационный", 165),
                        ("Прямой", 195), ("Амбициозный", 255),
                        ("Современный", 285), ("Откровенный", 345)]:
        rad = np.radians(angle)
        x, y = 3.75 * np.cos(rad), 3.75 * np.sin(rad)
        ax.text(x, y, text, ha="center", va="center",
                fontproperties=font_props("body", 7), color=LGRAY, zorder=10)

    # Ring labels
    for txt, x, y in [("ХАРАКТЕР", 4.5, 4.5), ("ЦЕННОСТИ", 3.3, 3.3),
                       ("АРХЕТИП", 2.15, 2.15), ("BIG IDEA", 1.0, 1.0)]:
        ax.text(x, y, txt, ha="right", va="top",
                fontproperties=font_props("annotation", 7), color=LGRAY, zorder=10)

    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_aspect("equal")
    ax.axis("off")
    _save(fig, "brand_wheel.png")


# ════════════════════════════════════════════════════════════════════════════
# 4. COMMS ARCHITECTURE
# ════════════════════════════════════════════════════════════════════════════
def gen_comms():
    fig, ax = plt.subplots(figsize=(13, 8.5))
    fig.patch.set_alpha(0)
    ax.set_facecolor("none")

    # Big Idea box
    bi = FancyBboxPatch((3.5, 7.5), 6, 0.9, boxstyle="round,pad=0.12",
                         facecolor=GOLD, edgecolor="#DAA520", linewidth=1.5, zorder=5)
    ax.add_patch(bi)
    ax.text(6.5, 8.05, "АКТИВИРУЙ СВОЁ БЛАГОСОСТОЯНИЕ",
            fontproperties=font_props("title", 13), color=BLACK, ha="center", zorder=10)
    ax.text(6.5, 7.7, "Big Idea",
            fontproperties=font_props("annotation", 7), color=GRAY, ha="center", zorder=10)

    # Arrows
    for tx in [2.3, 6.5, 10.7]:
        ax.annotate("", xy=(tx, 6.7), xytext=(6.5, 7.5),
                    arrowprops=dict(arrowstyle="-|>", color=LGRAY, lw=1.2), zorder=3)

    messages = [
        {"x": 0.2, "title": "СООБЩЕНИЕ 1", "value": "ЯСНОСТЬ",
         "text": "Сложность рынков \u2192\nясность решений",
         "slogan": "Сложный рынок.\nЯсные решения.", "color": BLUE},
        {"x": 4.4, "title": "СООБЩЕНИЕ 2", "value": "ТРАНСФОРМАЦИЯ",
         "text": "Мы не храним капитал —\nмы активируем его",
         "slogan": "Капитал\nв действии.", "color": VIOLET},
        {"x": 8.6, "title": "СООБЩЕНИЕ 3", "value": "СВОБОДА + МАСТЕРСТВО",
         "text": "30 лет экспертизы —\nчтобы деньги работали\nна вашу жизнь",
         "slogan": "Инвестируй в жизнь,\nа не в тревогу.", "color": AMBER},
    ]

    for m in messages:
        w = 4.0
        # Card outline
        card = FancyBboxPatch((m["x"], 3.2), w, 3.4, boxstyle="round,pad=0.1",
                               facecolor=WHITE, edgecolor=m["color"],
                               linewidth=1.5, alpha=0.95, zorder=4)
        ax.add_patch(card)

        # Color bar
        bar = FancyBboxPatch((m["x"] + 0.05, 6.2), w - 0.1, 0.35,
                              boxstyle="round,pad=0.04", facecolor=m["color"],
                              linewidth=0, alpha=0.9, zorder=6)
        ax.add_patch(bar)

        cx = m["x"] + w / 2
        ax.text(cx, 6.37, m["title"], fontproperties=font_props("header", 8),
                color=WHITE, ha="center", va="center", zorder=10)
        ax.text(cx, 5.8, m["value"], fontproperties=font_props("header", 11),
                color=m["color"], ha="center", va="center", zorder=10)
        ax.text(cx, 5.0, m["text"], fontproperties=font_props("body", 8),
                color=GRAY, ha="center", va="center", linespacing=1.3, zorder=10)

        ax.plot([m["x"] + 0.4, m["x"] + w - 0.4], [4.3, 4.3],
                color=VLGRAY, linewidth=0.8, zorder=6)

        ax.text(cx, 4.0, "Слоган:", fontproperties=font_props("annotation", 6),
                color=LGRAY, ha="center", va="bottom", zorder=10)
        ax.text(cx, 3.9, m["slogan"], fontproperties=font_props("body_medium", 9),
                color=DARK, ha="center", va="top", linespacing=1.25, zorder=10)

    # Funnel
    funnel_y = 1.5
    funnel_bg = FancyBboxPatch((0.2, funnel_y - 0.2), 12.6, 1.5,
                                boxstyle="round,pad=0.08", facecolor="#F5F5F5",
                                edgecolor=VLGRAY, linewidth=0.8, alpha=0.8, zorder=3)
    ax.add_patch(funnel_bg)

    ax.text(6.5, funnel_y + 1.1, "ВОРОНКА КОММУНИКАЦИИ",
            fontproperties=font_props("annotation", 7), color=LGRAY, ha="center", zorder=10)

    for label, sub, color, x in [
        ("AWARENESS", "Наружка, видео,\ndigital brand", VIOLET, 0.5),
        ("CONSIDERATION", "Контент, аналитика,\nБКС Экспресс", BLUE, 4.7),
        ("CONVERSION", "CTA, приложение,\nретаргетинг, CRM", AMBER, 8.9),
    ]:
        sb = FancyBboxPatch((x, funnel_y - 0.05), 3.6, 0.95,
                             boxstyle="round,pad=0.06", facecolor=color,
                             linewidth=0, alpha=0.1, zorder=5)
        ax.add_patch(sb)
        ax.text(x + 1.8, funnel_y + 0.7, label,
                fontproperties=font_props("header", 9), color=color, ha="center", zorder=10)
        ax.text(x + 1.8, funnel_y + 0.25, sub,
                fontproperties=font_props("body", 7), color=GRAY, ha="center",
                linespacing=1.2, zorder=10)

    ax.set_xlim(-0.3, 13.3)
    ax.set_ylim(0.8, 9)
    ax.axis("off")
    _save(fig, "comms_architecture.png")


# ════════════════════════════════════════════════════════════════════════════
# 5. AD MOCKUPS (these stay dark — they ARE dark ads)
# ════════════════════════════════════════════════════════════════════════════
def gen_ad_mockups():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5),
                                    gridspec_kw={"width_ratios": [1.2, 1]})
    fig.patch.set_facecolor("#0D0D0D")

    for ax, title in [(ax1, "Digital banner"), (ax2, "Наружная реклама")]:
        ax.set_facecolor("#070707")
        for spine in ax.spines.values():
            spine.set_color(VLGRAY)
            spine.set_linewidth(1)

    # Banner
    ax1.set_xlim(0, 12); ax1.set_ylim(0, 6.28)
    for i in range(40):
        ax1.add_patch(plt.Circle((9, 3.5), 0.5 + i * 0.12, facecolor=GOLD,
                                  alpha=0.02 * (1 - i / 40), edgecolor="none"))
    ax1.text(0.8, 4.8, "КАПИТАЛ", fontproperties=font_props("title", 24), color=WHITE, ha="left", zorder=10)
    ax1.text(0.8, 3.6, "В ДЕЙСТВИИ", fontproperties=font_props("title", 24), color=GOLD, ha="left", zorder=10)
    ax1.text(0.8, 2.4, "25,4% оборотов Мосбиржи. 30 лет.",
             fontproperties=font_props("body", 8), color="#BDBDBD", ha="left", zorder=10)
    cta = FancyBboxPatch((0.8, 1.2), 3, 0.55, boxstyle="round,pad=0.08",
                          facecolor=GOLD, edgecolor="#DAA520", linewidth=1, zorder=8)
    ax1.add_patch(cta)
    ax1.text(2.3, 1.47, "АКТИВИРУЙ", fontproperties=font_props("header", 11),
             color=BLACK, ha="center", va="center", zorder=10)
    ax1.text(10, 0.4, "БКС", fontproperties=font_props("header", 12),
             color=GOLD, ha="center", zorder=10)
    ax1.axis("off")

    # Outdoor
    ax2.set_xlim(0, 6); ax2.set_ylim(0, 3)
    ax2.text(0.4, 2.3, "ИНВЕСТИРУЙ", fontproperties=font_props("title", 18), color=WHITE, ha="left", zorder=10)
    ax2.text(0.4, 1.75, "В ЖИЗНЬ,", fontproperties=font_props("title", 18), color=GOLD, ha="left", zorder=10)
    ax2.text(0.4, 1.2, "А НЕ В ТРЕВОГУ.", fontproperties=font_props("title", 18), color=WHITE, ha="left", zorder=10)
    ax2.text(5.5, 0.4, "БКС", fontproperties=font_props("header", 12), color=GOLD, ha="right", zorder=10)
    ax2.text(0.4, 0.3, "bcs.ru", fontproperties=font_props("body", 7), color="#555", ha="left", zorder=10)
    ax2.axis("off")

    plt.subplots_adjust(wspace=0.06)
    _save(fig, "ad_mockups.png", pad=0.1, dark=True)


# ════════════════════════════════════════════════════════════════════════════
# 6. COLOR SYSTEM
# ════════════════════════════════════════════════════════════════════════════
def gen_color_system():
    fig, ax = plt.subplots(figsize=(12, 7))
    fig.patch.set_alpha(0)
    ax.set_facecolor("none")

    primary = [
        {"name": "Activation\nGold", "hex": "#FDB71C", "tc": BLACK},
        {"name": "Deep\nSpace", "hex": "#0D0D0D", "tc": WHITE},
        {"name": "Pure\nWhite", "hex": "#FFFFFF", "tc": BLACK},
    ]
    ax.text(0.3, 7.5, "PRIMARY", fontproperties=font_props("header", 11), color=GOLD)
    for i, c in enumerate(primary):
        x = 0.3 + i * 3.6
        sw = FancyBboxPatch((x, 5.5), 3.0, 1.8, boxstyle="round,pad=0.1",
                             facecolor=c["hex"], edgecolor=VLGRAY, linewidth=1, zorder=5)
        ax.add_patch(sw)
        ax.text(x + 1.5, 6.6, c["name"], fontproperties=font_props("header", 12),
                color=c["tc"], ha="center", linespacing=1.2, zorder=10)
        ax.text(x + 1.5, 5.85, c["hex"], fontproperties=font_props("body", 9),
                color=c["tc"], ha="center", alpha=0.6, zorder=10)

    sec = [
        {"name": "Clarity Blue", "hex": BLUE, "msg": "Ясность"},
        {"name": "Transform Violet", "hex": VIOLET, "msg": "Трансформация"},
        {"name": "Freedom Amber", "hex": AMBER, "msg": "Свобода"},
    ]
    ax.text(0.3, 4.8, "SECONDARY", fontproperties=font_props("header", 10), color=GRAY)
    for i, c in enumerate(sec):
        x = 0.3 + i * 3.6
        sw = FancyBboxPatch((x, 3.6), 3.0, 0.9, boxstyle="round,pad=0.06",
                             facecolor=c["hex"], edgecolor=c["hex"], linewidth=1, alpha=0.85, zorder=5)
        ax.add_patch(sw)
        ax.text(x + 0.2, 4.15, c["name"], fontproperties=font_props("body_bold", 9),
                color=WHITE, ha="left", zorder=10)
        ax.text(x + 2.8, 4.15, c["msg"], fontproperties=font_props("annotation", 7),
                color=WHITE, ha="right", alpha=0.7, zorder=10)
        ax.text(x + 0.2, 3.85, c["hex"], fontproperties=font_props("body", 7),
                color=WHITE, ha="left", alpha=0.6, zorder=10)

    # Neutral scale
    neutrals = ["#F5F5F5", "#E0E0E0", "#BDBDBD", "#9E9E9E", "#616161", "#424242", "#2A2A2A", "#1A1A1A", "#0D0D0D"]
    ax.text(0.3, 2.9, "NEUTRAL", fontproperties=font_props("header", 10), color=GRAY)
    bw = 11.4 / len(neutrals)
    for i, h in enumerate(neutrals):
        x = 0.3 + i * bw
        sw = FancyBboxPatch((x + 0.03, 1.5), bw - 0.06, 1.1,
                             boxstyle="round,pad=0.03", facecolor=h,
                             edgecolor=VLGRAY, linewidth=0.3, zorder=5)
        ax.add_patch(sw)
        tc = BLACK if i < 4 else WHITE
        ax.text(x + bw / 2, 2.0, h, fontproperties=font_props("annotation", 5.5),
                color=tc, ha="center", zorder=10)

    ax.set_xlim(0, 12)
    ax.set_ylim(1, 8.2)
    ax.axis("off")
    _save(fig, "color_system.png")


# ════════════════════════════════════════════════════════════════════════════
# 7. TYPOGRAPHY SPECIMEN
# ════════════════════════════════════════════════════════════════════════════
def gen_typography():
    fig, ax = plt.subplots(figsize=(12, 7.5))
    fig.patch.set_alpha(0)
    ax.set_facecolor("none")

    specimens = [
        ("H1", "title", 28, "Активируй своё благосостояние", DARK),
        ("H2", "header", 20, "Капитал в действии", DARK),
        ("H3", "subtitle", 15, "Сложный рынок. Ясные решения.", DARK),
        ("Body", "body", 11, "Мы превращаем финансовые амбиции в работающий капитал — чтобы деньги создавали жизнь.", GRAY),
        ("Caption", "annotation", 8, "Рейтинг ruА-, ААА|ru.iv|. Данные на январь 2026.", LGRAY),
        ("Data", "header", 16, "856 млрд \u20BD  \u00B7  1 000+ экспертов  \u00B7  25,4%", GOLD),
    ]

    y = 7.0
    for label, font, size, text, color in specimens:
        ax.text(0.2, y, label, fontproperties=font_props("annotation", 7), color=LGRAY, ha="left", va="top")
        ax.text(2.0, y, text, fontproperties=font_props(font, size), color=color, ha="left", va="top")
        spacing = 1.0 if size > 18 else (0.85 if size > 12 else 0.65)
        y -= spacing
        ax.plot([0.2, 11.5], [y + 0.12, y + 0.12], color=VLGRAY, linewidth=0.3)

    ax.set_xlim(0, 12)
    ax.set_ylim(0.5, 7.5)
    ax.axis("off")
    _save(fig, "typography_specimen.png")


# ════════════════════════════════════════════════════════════════════════════
# 8. GRAPHIC DEVICE
# ════════════════════════════════════════════════════════════════════════════
def gen_graphic_device():
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))
    fig.patch.set_facecolor("#0D0D0D")

    # Glow
    ax = axes[0]
    ax.set_facecolor("#070707")
    ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    for i in range(60):
        ax.add_patch(plt.Circle((6.5, 5.5), 0.3 + i * 0.08, facecolor=GOLD,
                                 alpha=0.03 * (1 - i / 60) ** 1.5, edgecolor="none"))
    ax.text(1.5, 6.5, "КАПИТАЛ", fontproperties=font_props("title", 16), color=WHITE, zorder=10)
    ax.text(1.5, 5, "В ДЕЙСТВИИ", fontproperties=font_props("title", 16), color=GOLD, zorder=10)
    ax.text(5, 1, "Glow", fontproperties=font_props("annotation", 8), color="#777", ha="center")
    ax.axis("off")

    # Pulse Line
    ax = axes[1]
    ax.set_facecolor("#070707")
    ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    x_l = np.linspace(1, 9, 150)
    w_l = 0.4 + 3 * np.exp(-0.5 * ((x_l - 5) / 1.2) ** 2)
    for j in range(len(x_l) - 1):
        ax.plot(x_l[j:j+2], [5, 5], color=GOLD, linewidth=w_l[j], alpha=0.8,
                solid_capstyle="round", zorder=5)
    for k in range(20):
        ax.add_patch(plt.Circle((5, 5), 0.15 + k * 0.05, facecolor=GOLD,
                                 alpha=0.02 * (1 - k / 20), edgecolor="none"))
    ax.text(5, 1, "Pulse Line", fontproperties=font_props("annotation", 8), color="#777", ha="center")
    ax.axis("off")

    # Dots
    ax = axes[2]
    ax.set_facecolor("#070707")
    ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    for text, cy in [("Ясность решений", 7.5), ("Трансформация капитала", 5.5),
                      ("Мастерство 30 лет", 3.5)]:
        for k in range(12):
            ax.add_patch(plt.Circle((2, cy), 0.12 + k * 0.06, facecolor=GOLD,
                                     alpha=0.03 * (1 - k / 12), edgecolor="none"))
        ax.add_patch(plt.Circle((2, cy), 0.14, facecolor=GOLD, zorder=8))
        ax.text(2.6, cy, text, fontproperties=font_props("body_medium", 9), color="#E0E0E0",
                ha="left", va="center", zorder=10)
    ax.text(5, 1, "Activation Dot", fontproperties=font_props("annotation", 8), color="#777", ha="center")
    ax.axis("off")

    plt.subplots_adjust(wspace=0.04)
    _save(fig, "graphic_device.png", pad=0.1, dark=True)


# ════════════════════════════════════════════════════════════════════════════
# 9. APPLIED IDENTITY
# ════════════════════════════════════════════════════════════════════════════
def gen_applied():
    fig = plt.figure(figsize=(14, 8))
    fig.patch.set_facecolor("#0D0D0D")

    # Banner
    ax1 = fig.add_axes([0.02, 0.38, 0.55, 0.58])
    ax1.set_facecolor("#070707")
    ax1.set_xlim(0, 12); ax1.set_ylim(0, 6.28)
    for i in range(50):
        ax1.add_patch(plt.Circle((9, 3.5), 0.5 + i * 0.12, facecolor=GOLD,
                                  alpha=0.02 * (1 - i / 50), edgecolor="none"))
    ax1.text(0.8, 4.8, "КАПИТАЛ", fontproperties=font_props("title", 22), color=WHITE, zorder=10)
    ax1.text(0.8, 3.5, "В ДЕЙСТВИИ", fontproperties=font_props("title", 22), color=GOLD, zorder=10)
    cta = FancyBboxPatch((0.8, 1.2), 2.8, 0.5, boxstyle="round,pad=0.08",
                          facecolor=GOLD, linewidth=0, zorder=8)
    ax1.add_patch(cta)
    ax1.text(2.2, 1.45, "АКТИВИРУЙ", fontproperties=font_props("header", 10),
             color=BLACK, ha="center", va="center", zorder=10)
    ax1.text(10, 0.4, "БКС", fontproperties=font_props("header", 11), color=GOLD, ha="center", zorder=10)
    ax1.set_title("Digital banner", fontproperties=font_props("annotation", 7), color=GRAY, pad=3)
    ax1.axis("off")

    # Outdoor
    ax2 = fig.add_axes([0.60, 0.38, 0.38, 0.58])
    ax2.set_facecolor("#030303")
    ax2.set_xlim(0, 6); ax2.set_ylim(0, 3)
    ax2.text(0.3, 2.3, "ИНВЕСТИРУЙ", fontproperties=font_props("title", 16), color=WHITE, zorder=10)
    ax2.text(0.3, 1.7, "В ЖИЗНЬ,", fontproperties=font_props("title", 16), color=GOLD, zorder=10)
    ax2.text(0.3, 1.1, "А НЕ В ТРЕВОГУ.", fontproperties=font_props("title", 16), color=WHITE, zorder=10)
    ax2.text(5.5, 0.3, "БКС", fontproperties=font_props("header", 11), color=GOLD, ha="right", zorder=10)
    ax2.set_title("Наружная реклама", fontproperties=font_props("annotation", 7), color=GRAY, pad=3)
    ax2.axis("off")

    # App
    ax3 = fig.add_axes([0.18, 0.0, 0.25, 0.38])
    ax3.set_facecolor("#0A0A0A")
    ax3.set_xlim(0, 3.75); ax3.set_ylim(0, 5)
    frame = FancyBboxPatch((0, 0), 3.75, 5, boxstyle="round,pad=0.12",
                            facecolor="#0A0A0A", edgecolor="#333", linewidth=1.5)
    ax3.add_patch(frame)
    ax3.text(1.875, 4.5, "БКС", fontproperties=font_props("header", 10), color=GOLD, ha="center", zorder=10)
    ax3.text(0.4, 3.8, "Ваш портфель", fontproperties=font_props("annotation", 5), color="#777", zorder=10)
    ax3.text(0.4, 3.3, "2 847 320 \u20BD", fontproperties=font_props("header", 13), color=WHITE, zorder=10)
    ax3.text(0.4, 2.9, "+12,4%", fontproperties=font_props("body_medium", 7), color="#4CAF50", zorder=10)
    for text, y, col in [("Активируй стратегию", 2.2, VIOLET),
                          ("Активируй ясность", 1.5, BLUE),
                          ("Активируй свободу", 0.8, AMBER)]:
        ax3.plot([0.3, 0.3], [y - 0.15, y + 0.15], color=col, linewidth=2.5, solid_capstyle="round", zorder=5)
        ax3.text(0.55, y, text, fontproperties=font_props("body", 6), color=WHITE, va="center", zorder=10)
    ax3.set_title("Приложение", fontproperties=font_props("annotation", 7), color=GRAY, pad=3)
    ax3.axis("off")

    # Summary
    ax4 = fig.add_axes([0.55, 0.0, 0.42, 0.35])
    ax4.set_facecolor("none")
    ax4.set_xlim(0, 10); ax4.set_ylim(0, 6)

    # Color dots
    for i, col in enumerate([GOLD, BLACK, WHITE, BLUE, VIOLET, AMBER]):
        ax4.add_patch(plt.Circle((1 + i * 1.3, 5), 0.4, facecolor=col,
                                  edgecolor=VLGRAY, linewidth=0.5, zorder=5))

    ax4.text(0.3, 3.8, "Atyp Display Bold", fontproperties=font_props("title", 14), color=WHITE)
    ax4.text(0.3, 2.8, "Atyp Text Regular", fontproperties=font_props("body", 10), color="#BDBDBD")

    # Mini pulse
    x_p = np.linspace(0.3, 9.5, 100)
    w_p = 0.3 + 2 * np.exp(-0.5 * ((x_p - 5) / 1.5) ** 2)
    for j in range(len(x_p) - 1):
        ax4.plot(x_p[j:j+2], [1.5, 1.5], color=GOLD, linewidth=w_p[j], alpha=0.6,
                solid_capstyle="round", zorder=5)
    ax4.text(5, 0.7, "Activation Pulse", fontproperties=font_props("body_medium", 8),
             color=LGRAY, ha="center")
    ax4.axis("off")

    _save(fig, "applied_identity.png", dark=True)


# ════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("Generating all figures (transparent, light-mode)...")
    gen_swot()
    gen_competitive_map()
    gen_brand_wheel()
    gen_comms()
    gen_ad_mockups()
    gen_color_system()
    gen_typography()
    gen_graphic_device()
    gen_applied()
    print("Done.")
