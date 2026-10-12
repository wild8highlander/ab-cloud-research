#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_banner.py — фирменные ассеты пакета AB Cloud Quantum Research:
1) assets/banner.gif — анимированный баннер: нули ζ «поднимаются» по
   критической прямой Re(s)=½ (детерминированные данные Одлыжко);
2) assets/logo_abcloud.svg + logo_abcloud_light.png + logo_abcloud_dark.png —
   логотип AB Cloud Quantum Research (спираль из нулей + критическая прямая)."""
import math
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.font_manager as fm

for _f in ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
           "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"):
    if os.path.exists(_f):
        fm.fontManager.addfont(_f)
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, "assets")
os.makedirs(ASSETS, exist_ok=True)

plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]

# Первые 40 ординат нулей ζ (встроены в веб-лабораторию core_rp —
# открытые данные Одлыжко); детерминированный список.
ZEROS = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178,
         40.918719, 43.327073, 48.005151, 49.773832, 52.970321, 56.446248,
         59.347044, 60.831779, 65.112544, 67.079811, 69.546402, 72.067158,
         75.704691, 77.144840, 79.337375, 82.910381, 84.735493, 87.425275,
         88.809111, 92.491899, 94.651344, 95.870634, 98.831194, 101.317851,
         103.725538, 105.446623, 107.168611, 111.029536, 111.874659,
         114.320222, 116.226680, 118.790783, 121.370125, 122.946829]

T = dict(bg="#FAF7F0", ink="#1A1A24", line="#0E7C86", copper="#C96F4A",
         muted="#6B6455", grid="#DDD6C8")


def zeta_curve(t):
    """Гладкая модель Z(t) для баннера: |ζ| интерполяция по нулям —
    ДЕКОРАТИВНАЯ кривая (для заголовка README, не для анализа):
    между нулями — синус-полудуги единичной амплитуды."""
    zs = np.asarray(ZEROS)
    y = np.zeros_like(t)
    for g in zs:
        y += np.exp(-((t - g) / 0.8) ** 2)
    return y


def banner_frame(k, n_frames, path_prefix=None):
    fig, ax = plt.subplots(figsize=(9.6, 3.2), dpi=100,
                           constrained_layout=True)
    fig.patch.set_facecolor(T["bg"])
    ax.set_facecolor(T["bg"])
    tmax = 126.0
    t = np.linspace(0, tmax, 900)
    # критическая прямая (вертикаль) — символ Re(s)=1/2
    ax.axvline(0.5, color=T["copper"], lw=2.2, alpha=0.9)
    # «подъём» нулей: показываем первые k+бегущий
    shown = max(1, int((k + 1) / n_frames * len(ZEROS)))
    zs = ZEROS[:shown]
    ax.scatter([0.5] * len(zs), zs, s=[(28 if i == len(zs) - 1 else 14)
               for i in range(len(zs))], color=T["copper"],
               edgecolors=T["ink"], linewidths=0.4, zorder=3)
    # волна Z(t) справа от прямой (декоративная)
    phase = 2 * np.pi * k / n_frames
    wave = 0.5 + 0.5 * zeta_curve(np.linspace(0, tmax, 900))
    wave = wave / wave.max()
    ax.plot(0.5 + 0.45 * wave * (0.85 + 0.15 * math.sin(phase)),
            t, color=T["line"], lw=1.4, alpha=0.95)
    ax.set_xlim(0.0, 1.05)
    ax.set_ylim(0, tmax)
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.text(0.015, 0.955, "AB CLOUD QUANTUM RESEARCH",
            transform=ax.transAxes, fontsize=14.5, fontweight="bold",
            color=T["ink"], va="top")
    ax.text(0.015, 0.86, "V01–V20 · E01–E18 — Th1–Th6 · RH blocked by V13",
            transform=ax.transAxes, fontsize=8.5, color=T["muted"], va="top")
    ax.text(0.5, tmax - 2, "Re(s) = 1/2", rotation=90, fontsize=7.5,
            color=T["copper"], ha="right", va="top")
    return fig


def make_banner():
    n_frames = 42
    frames = []
    for k in range(n_frames):
        fig = banner_frame(k, n_frames)
        tmp = os.path.join(ASSETS, f"_f{k:03d}.png")
        fig.savefig(tmp, dpi=100, facecolor=T["bg"])
        plt.close(fig)
        frames.append(Image.open(tmp).convert("P", palette=Image.ADAPTIVE))
    frames[0].save(os.path.join(ASSETS, "banner.gif"),
                   save_all=True, append_images=frames[1:], duration=140,
                   loop=0, optimize=True)
    for k in range(n_frames):
        os.remove(os.path.join(ASSETS, f"_f{k:03d}.png"))
    print("banner.gif:", os.path.getsize(os.path.join(ASSETS, "banner.gif")) // 1024, "KB")


def make_logo():
    # SVG: спираль из 12 нулей вокруг критической прямой
    pts = []
    for i in range(12):
        a = 2 * math.pi * i / 12
        r = 34 + 5 * math.sin(a * 2)
        x = 80 + r * math.cos(a)
        y = 80 + r * math.sin(a)
        pts.append((x, y))
    circles = "\n".join(
        f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{3.4 if i % 2 else 4.6}" '
        f'fill="{"#C96F4A" if i % 2 else "#0E7C86"}" stroke="#1A1A24" '
        f'stroke-width="0.6"/>'
        for i, (x, y) in enumerate(pts))
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="160" height="160" viewBox="0 0 160 160">
  <rect width="160" height="160" rx="24" fill="#2E3F49"/>
  <line x1="80" y1="18" x2="80" y2="142" stroke="#C96F4A" stroke-width="3"/>
  <circle cx="80" cy="80" r="56" fill="none" stroke="#4FB3BE" stroke-width="1.4" stroke-dasharray="4 3"/>
  {circles}
  <text x="80" y="152" font-family="DejaVu Sans, sans-serif" font-size="11"
        fill="#E8E4DA" text-anchor="middle" font-weight="bold">AB·CQ</text>
</svg>'''
    with open(os.path.join(ASSETS, "logo_abcloud.svg"), "w",
              encoding="utf-8") as f:
        f.write(svg)
    # PNG-версии через cairosvg может не быть — рисуем matplotlib-версию
    fig, ax = plt.subplots(figsize=(3.2, 3.2), dpi=100)
    fig.patch.set_alpha(0.0)
    ax.set_position([0, 0, 1, 1])
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.axis("off")
    import matplotlib.patches as mp
    bgc = "#2E3F49"
    ax.add_patch(mp.FancyBboxPatch((0.03, 0.03), 0.94, 0.94,
                boxstyle="round,pad=0.02,rounding_size=0.12",
                facecolor=bgc, edgecolor="#4FB3BE", lw=1.6))
    ax.plot([0.5, 0.5], [0.14, 0.86], color="#C96F4A", lw=3)
    th = np.linspace(0, 2 * np.pi, 200)
    ax.plot(0.5 + 0.33 * np.cos(th), 0.5 + 0.33 * np.sin(th),
            color="#4FB3BE", lw=1.2, ls=(0, (4, 3)))
    for i in range(12):
        a = 2 * np.pi * i / 12
        r = 0.21 + 0.03 * math.sin(2 * a)
        col = "#C96F4A" if i % 2 else "#0E7C86"
        ax.scatter([0.5 + r * math.cos(a)], [0.5 + r * math.sin(a)],
                   s=[110 if i % 2 == 0 else 70], color=col,
                   edgecolors="#1A1A24", linewidths=0.8, zorder=3)
    ax.text(0.5, 0.055, "AB·CQ", ha="center", va="center", fontsize=13,
            color="#E8E4DA", fontweight="bold")
    for name, transp in (("logo_abcloud_light.png", False),
                         ("logo_abcloud_dark.png", True)):
        fig.savefig(os.path.join(ASSETS, name), dpi=100,
                    facecolor="none" if transp else bgc,
                    transparent=transp)
    plt.close(fig)
    print("logo_abcloud.svg/.png ok")


if __name__ == "__main__":
    make_banner()
    make_logo()
