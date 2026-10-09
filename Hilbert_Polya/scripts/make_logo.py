#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_logo.py — официальный логотип «Hilbert Polya Bridge».

Эмблема «Critical Line & Copper»: слева — критическая полоса с нулями ζ
(медь) на линии ½ (teal); арка — сам мост (отождествление график↔оператор);
справа — спектральная лестница затворов (сланец) с символом Tr e^{−uH}.
Варианты light/dark; PNG 600 dpi + SVG (текст путями — переносимо).
Детерминировано; внешних файлов нет. Запуск: python3 scripts/make_logo.py
"""
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.font_manager as fm

for _p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
           "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"):
    try:
        fm.fontManager.addfont(_p)
    except Exception:
        pass

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Circle, FancyArrowPatch  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

THEMES = {
    "light": {"bg": "#FAF7F0", "ink": "#1A1A24", "line": "#0E7C86",
              "copper": "#C96F4A", "slate": "#3E515B", "muted": "#6B6455"},
    "dark": {"bg": "#10101A", "ink": "#E8E2D0", "line": "#4FB3BE",
             "copper": "#E08B66", "slate": "#8FA8B5", "muted": "#8A8574"},
}
ZEROS = [14.13, 21.02, 25.01, 30.42, 32.94, 37.59, 40.92, 43.33, 48.01, 49.77]


def draw(theme):
    t = THEMES[theme]
    fig, ax = plt.subplots(figsize=(9.6, 3.6), constrained_layout=True)
    ax.set_facecolor(t["bg"])
    ax.set_xlim(0, 96)
    ax.set_ylim(0, 36)
    ax.axis("off")

    # ── левая половина: критическая полоса ──
    ax.add_patch(plt.Rectangle((3, 4), 10, 28, fill=True, facecolor=t["bg"],
                               edgecolor=t["muted"], lw=1.2, alpha=0.35))
    ax.plot([8, 8], [4, 32], color=t["line"], lw=3.2,
            solid_capstyle="round")
    for i, g in enumerate(ZEROS):
        y = 4 + (g / 50.0) * 28
        ax.plot([8], [y], "o", ms=6.5, color=t["copper"], zorder=6)
        ax.plot([8], [36 - y], "o", ms=6.5, color=t["copper"],
                alpha=0.35, zorder=5)
    ax.text(8, 1.6, "Re s = 1/2", ha="center", fontsize=11,
            color=t["line"], fontweight="bold")

    # ── арка моста ──
    arrow = FancyArrowPatch((15.0, 21), (57.0, 21),
                            connectionstyle="arc3,rad=-0.26",
                            arrowstyle="-|>,head_width=4,head_length=8",
                            color=t["ink"], lw=2.4, mutation_scale=1.4)
    ax.add_patch(arrow)
    ax.text(36, 33.2, "Tr e$^{-uH}$ = (1/π)∫ Q(a) sin(ua) da",
            ha="center", fontsize=15.5, color=t["ink"], fontweight="bold")
    ax.text(36, 29.2, "ξ(1/2+it)  ↔  spec H", ha="center", fontsize=12.5,
            color=t["muted"])

    # ── правая половина: спектральная лестница ──
    x0 = 62
    for row in range(6):
        y = 5.5 + row * 4.6
        w = 26 - row * 2.2
        ax.add_patch(plt.Rectangle((x0, y), w, 2.2, fill=True,
                                   facecolor=t["slate"],
                                   edgecolor="none", alpha=0.85 - row * 0.1))
    for i, g in enumerate(ZEROS[:6]):
        y = 5.5 + i * 4.6 + 1.1
        ax.plot([x0 - 2.4], [y], "o", ms=5.5, color=t["copper"])
    ax.text(x0 + 12, 1.6, "spec H (gates)", ha="center", fontsize=11,
            color=t["slate"], fontweight="bold")

    return fig, ax


def main():
    out = os.path.join(ROOT, "figures", "logo")
    os.makedirs(out, exist_ok=True)
    for theme in ("light", "dark"):
        fig, _ = draw(theme)
        fig.savefig(f"{out}/hpb_logo_{theme}.png", dpi=600)
        fig.savefig(f"{out}/hpb_logo_{theme}.svg")
        plt.close(fig)
        print(f"logo {theme} OK")


if __name__ == "__main__":
    main()
