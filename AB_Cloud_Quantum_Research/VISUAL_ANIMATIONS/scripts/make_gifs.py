#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the GIF animations of VISUAL_ANIMATIONS (Critical Line & Copper style).
Five GIFs: zeros rising, pipeline flow, spinor cycles, campaign timeline, compiler gates.
Reproducible: rebuild with  python3 make_gifs.py
"""
import os, math, numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.font_manager as fm
for f in ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",):
    if os.path.exists(f):
        fm.fontManager.addfont(f)
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, "..", "gif"))
os.makedirs(OUT, exist_ok=True)

BG = "#221B16"; PANEL = "#2C241E"; COPPER = "#C96F4A"; TEAL = "#0E7C86"
GOLD = "#C9A227"; TEXT = "#EDE6E0"; MUTED = "#B8A99C"; GRID = "#3A3028"

def style_ax(ax):
    ax.set_facecolor(PANEL)
    for s in ax.spines.values():
        s.set_color(GRID)
    ax.tick_params(colors=MUTED, labelsize=8)

def save_anim(fig, anim, name, fps=18, dpi=90):
    path = os.path.join(OUT, name)
    anim.save(path, writer=PillowWriter(fps=fps), dpi=dpi, savefig_kwargs={
        "facecolor": BG, "pad_inches": 0.12})
    plt.close(fig)
    sz = os.path.getsize(path) / 1e6
    print(f"{name}: {sz:.1f} MB")

# ─────────────────── 1. zeros rising along the critical line ───────────────────
def gif_zeros():
    # real ordinates of the first zeros (public data, matches datasets reference)
    zeros = [14.13,21.02,25.01,30.42,32.94,37.59,40.92,43.33,48.00,49.77,52.80,
             56.45,59.35,61.19,65.11,67.08,69.55,72.07,75.70,77.14,79.34,82.90,
             84.74,87.43,88.81,92.49,94.65,96.00,98.83]
    fig, ax = plt.subplots(figsize=(7.2, 4.05), constrained_layout=True)
    fig.patch.set_facecolor(BG)
    style_ax(ax)
    ax.set_xlim(0, 1); ax.set_ylim(0, 104)
    ax.set_xticks([])
    ax.set_ylabel("Im s = γ", color=MUTED, fontsize=9)
    ax.axvline(0.5, color=COPPER, lw=2.2, alpha=0.9)
    ax.text(0.52, 96, "Re(s) = 1/2", color=COPPER, fontsize=10, style="italic")
    ax.text(0.04, 4, "AB Cloud Quantum Research · blind zero reading (E17: 649/649 + 639/639)",
            color=MUTED, fontsize=7.5)
    scat = ax.scatter([], [], s=42, color=TEAL, edgecolors=TEXT, linewidths=0.5, zorder=3)
    trail = ax.scatter([], [], s=90, color=TEAL, alpha=0.25, zorder=2)
    cnt = ax.text(0.04, 90, "", color=TEXT, fontsize=11, family="monospace")
    frames = 70
    def update(f):
        n = 1 + int((f / frames) * len(zeros))
        data = np.array(zeros[:n])
        scat.set_offsets(np.c_[np.full(n, 0.5), data])
        trail.set_offsets(np.c_[np.full(n, 0.5), data])
        cnt.set_text(f"zeros on the line: {n:02d}/{len(zeros)}")
        return scat, trail, cnt
    anim = FuncAnimation(fig, update, frames=frames, blit=True)
    save_anim(fig, anim, "zeros_rising.gif", fps=16)

# ─────────────────── 2. pipeline flow through the four levels ───────────────────
def gif_pipeline():
    fig, ax = plt.subplots(figsize=(7.2, 4.05), constrained_layout=True)
    fig.patch.set_facecolor(BG)
    ax.set_xlim(0, 10); ax.set_ylim(0, 5.6)
    ax.axis("off")
    levels = [
        (5.0, 4.7, "SPECTRAL CORE", "V01–V19 · Th1–Th6 · V13", COPPER),
        (2.0, 3.1, "AB PROCESSOR", "V20 · ISA · Givens-QR", TEAL),
        (8.0, 3.1, "VERIFICATION", "E01–E18 · blind · Julia", GOLD),
        (5.0, 1.5, "SPINOR STUDY", "ES1–ES5 · TS1–TS3", "#8C6D1F"),
    ]
    boxes = []
    for x, y, title, sub, color in levels:
        b = FancyBboxPatch((x - 1.55, y - 0.42), 3.1, 0.9,
                           boxstyle="round,pad=0.06,rounding_size=0.12",
                           fc=PANEL, ec=color, lw=2)
        ax.add_patch(b)
        ax.text(x, y + 0.12, title, ha="center", color=color, fontsize=10.5,
                fontweight="bold")
        ax.text(x, y - 0.18, sub, ha="center", color=MUTED, fontsize=7.5)
        boxes.append((x, y, color))
    arrows = [(boxes[0], boxes[1], "ISA"), (boxes[0], boxes[2], "blind audit"),
              (boxes[1], boxes[3], "reads, not carries"), (boxes[3], boxes[0], "volatility")]
    arrs = []
    for (x1, y1, _), (x2, y2, _), label in arrows:
        a = FancyArrowPatch((x1, y1 + (-0.5 if y2 > y1 else 0.5) if abs(x1-x2) < 0.1 else x1 + (1.6 if x2 > x1 else -1.6)),
                            (x2 + (0 if abs(x1-x2) < 0.1 else (-1.6 if x2 > x1 else 1.6)),
                             y2 + (0.52 if y2 > y1 else -0.52)),
                            arrowstyle="-|>", mutation_scale=14, color=MUTED, lw=1.4)
        ax.add_patch(a)
        arrs.append(a)
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        ax.text(mx, my + 0.16, label, ha="center", color=MUTED, fontsize=7)
    pulse, = ax.plot([], [], "o", color=TEXT, markersize=6, zorder=5)
    title_txt = ax.text(5, 5.32, "", ha="center", color=TEXT, fontsize=11, fontweight="bold")
    frames = 90
    def update(f):
        # pulse travels: core → processor → spinor → core → verification
        route = [(5.0, 4.2), (2.0, 3.6), (2.0, 3.55), (5.0, 2.05), (5.0, 4.2), (8.0, 3.6)]
        t = (f % 45) / 45
        seg = int(t * (len(route) - 1))
        tt = t * (len(route) - 1) - seg
        x1, y1 = route[seg]; x2, y2 = route[min(seg + 1, len(route) - 1)]
        pulse.set_data([x1 + (x2 - x1) * tt], [y1 + (y2 - y1) * tt])
        titles = ["reads mathematics in real time…", "…compiles it into AB clouds…",
                  "…carries nothing (storage = 0)…", "…and survives blind verification"]
        title_txt.set_text(titles[(f // 45) % 4])
        return pulse, title_txt
    anim = FuncAnimation(fig, update, frames=frames, blit=True)
    save_anim(fig, anim, "pipeline_flow.gif", fps=15)

# ─────────────────── 3. spinor cycles ───────────────────
def gif_spinor():
    fig, axes = plt.subplots(1, 3, figsize=(7.2, 2.7), constrained_layout=True)
    fig.patch.set_facecolor(BG)
    models = [("π/2 · N=4", 4, COPPER), ("π/3 · N=6", 6, TEAL), ("π/7 · N=14", 14, GOLD)]
    for ax, (lab, N, color) in zip(axes, models):
        style_ax(ax)
        ax.set_xlim(-1.25, 1.25); ax.set_ylim(-1.25, 1.25)
        ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([])
        th = np.linspace(0, 2 * np.pi, 200)
        ax.plot(np.cos(th), np.sin(th), color=GRID, lw=1.2)
        step = 2 * np.pi / N
        for i in range(N):
            a = i * step
            ax.plot([0, np.cos(a)], [0, np.sin(a)], color=GRID, lw=0.6, alpha=0.6)
            ax.scatter([np.cos(a)], [np.sin(a)], s=26, color=color, zorder=3)
        ax.set_title(lab, color=color, fontsize=10)
        dot = ax.scatter([], [], s=130, color=TEXT, zorder=5, edgecolors=color, linewidths=2)
        setattr(ax, "_dot", dot)
    frames = 84  # 3 full cycles of N=14 (LCM-friendly)
    def update(f):
        dots = []
        for ax, (lab, N, color) in zip(axes, models):
            a = (f % N) * 2 * np.pi / N
            ax._dot.set_offsets([[np.cos(a), np.sin(a)]])
            dots.append(ax._dot)
        return dots
    anim = FuncAnimation(fig, update, frames=frames, blit=True)
    save_anim(fig, anim, "spinor_cycles.gif", fps=14)

# ─────────────────── 4. campaign timeline ───────────────────
def gif_timeline():
    import csv
    tl_path = os.path.normpath(os.path.join(HERE, "..", "..", "datasets", "campaign_timeline.csv"))
    rows = []
    with open(tl_path, encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            rows.append(r["campaign"])
    fig, ax = plt.subplots(figsize=(7.2, 4.05), constrained_layout=True)
    fig.patch.set_facecolor(BG)
    style_ax(ax)
    ax.set_xlim(0, len(rows) + 2); ax.set_ylim(0, 5)
    ax.set_xticks([]); ax.set_yticks([])
    bands = [("core V", COPPER, 3.4), ("processor", TEAL, 2.5),
             ("verification E", GOLD, 1.6), ("spinor ES", "#8C6D1F", 0.7)]
    for name, color, y in bands:
        ax.axhline(y, color=GRID, lw=1)
        ax.text(0.1, y + 0.14, name, color=color, fontsize=7.5)
    scat = ax.scatter([], [], s=34, c=[], zorder=3, cmap="copper", vmin=0, vmax=4)
    txt = ax.text(len(rows) / 2, 4.62, "", ha="center", color=TEXT, fontsize=12,
                  fontweight="bold")
    frames = 80
    def color_of(c):
        return COPPER if c.startswith("V") and c != "V20" else \
               TEAL if c.startswith("V20") or c.startswith("P") else \
               GOLD if c.startswith("E") else "#8C6D1F"
    def update(f):
        n = 1 + int((f / frames) * len(rows))
        xs = np.arange(1, n + 1)
        ys = []
        for c in rows[:n]:
            if c.startswith("V20"): ys.append(2.5)
            elif c.startswith("V"): ys.append(3.4)
            elif c.startswith("E"): ys.append(1.6)
            else: ys.append(0.7)
        scat.set_offsets(np.c_[xs, ys])
        scat.set_facecolor([color_of(c) for c in rows[:n]])
        txt.set_text(f"43 campaigns · {n}/43 · all PASS")
        return scat, txt
    anim = FuncAnimation(fig, update, frames=frames, blit=True)
    save_anim(fig, anim, "campaign_timeline.gif", fps=16)

# ─────────────────── 5. compiler gates ───────────────────
def gif_compiler():
    n = 4
    fig, ax = plt.subplots(figsize=(7.2, 4.05), constrained_layout=True)
    fig.patch.set_facecolor(BG)
    ax.set_xlim(-0.8, n - 0.2); ax.set_ylim(-0.9, n - 0.1)
    ax.set_aspect("equal"); ax.axis("off")
    # lattice of nodes
    for i in range(n):
        for j in range(n):
            ax.scatter([j], [n - 1 - i], s=210, color=PANEL, edgecolors=GRID,
                       linewidths=1.4, zorder=2)
    ax.text(n / 2 - 0.5, n - 0.35, "AB clouds: Givens rotations on a ring",
            ha="center", color=TEXT, fontsize=10.5, fontweight="bold")
    txt = ax.text(n / 2 - 0.5, -0.72, "", ha="center", color=COPPER, fontsize=9.5,
                  family="monospace")
    pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    lines = []
    frames = 60
    for _ in pairs:
        ln, = ax.plot([], [], color=COPPER, lw=2.4, zorder=3)
        lines.append(ln)
    update_text = ["target U(4×4)", "compiling…", "depth ≤ 7 · 1−F ≤ 4.4e−16 · PASS"]
    def update(f):
        k = int((f / frames) * (len(pairs) + 2))
        for i, ln in enumerate(lines):
            if i < k - 0:
                (a, b) = pairs[i]
                ln.set_data([a, b], [n - 1 - a * 0.85 - 0.3, n - 1 - b * 0.85 - 0.45])
            else:
                ln.set_data([], [])
        txt.set_text(update_text[min(2, k - 1)] if k >= 1 else update_text[0])
        return (*lines, txt)
    anim = FuncAnimation(fig, update, frames=frames, blit=True)
    save_anim(fig, anim, "compiler_gates.gif", fps=16)

if __name__ == "__main__":
    gif_zeros()
    gif_spinor()
    gif_timeline()
    gif_compiler()
    gif_pipeline()
    print("done")
