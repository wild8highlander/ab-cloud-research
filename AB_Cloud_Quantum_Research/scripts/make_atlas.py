#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_atlas.py — атлас флагманских результатов AB Cloud Quantum Research.

Одна плитка 2×2 «четыре измерения» программы (600 dpi, RU/EN),
построенная ТОЛЬКО из закоммиченных вердиктов:
  a) слепое чтение нулей ζ до T=1000 (E17: 649/649 ЭМ + 639/639 РС);
  b) точный компилятор AB-облаков (V20: 1−F = 4.4e-16 / 6.7e-16);
  c) след ↔ простые (V7/Th6: r = 0.9996 против решётки 0.76);
  d) нелокальность без сигналинга (V24-превью: CHSH S = 2√2 − 4.4e-16).
Выход: atlas/atlas_flagships_{lang}.png."""
import json
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

plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MOD = os.path.join(ROOT, "modules")
OUT = os.path.join(ROOT, "atlas")
os.makedirs(OUT, exist_ok=True)

T = dict(bg="#FAF7F0", panel="#FFFFFF", ink="#1A1A24", line="#0E7C86",
         copper="#C96F4A", slate="#3E515B", muted="#6B6455",
         grid="#DDD6C8", ok="#3A6B4F", bad="#8C3A2F", gold="#8C6D1F")

v20 = json.load(open(os.path.join(MOD, "processor_ab", "data",
                                  "v20_verdict.json")))
v07 = json.load(open(os.path.join(MOD, "core_spectrum", "data",
                                  "v07_verdict.json")))
e17 = json.load(open(os.path.join(MOD, "verifier_multilang", "results",
                                  "e17_verdict.json")))
S = v20["previews"]["nonlocality_V24"]["chsh"]["S"]

L = {
    "ru": dict(
        t="AB Cloud Quantum Research — атлас флагманов (4 измерения)",
        a="a) слепое чтение нулей ζ, T ≤ 1000 (E17)",
        b="b) точный компилятор AB-облаков (V20)",
        c="c) след H_ξ ↔ простые (V7 · Th6)",
        d="d) нелокальность без сигналинга (V24-превью)",
        cap=("Числа — из закоммиченных вердиктов: 649+639 слепо, "
             "кросс-движок 0.0; 1−F ≤ 4.4e-16; r = 0.9996 против 0.76; "
             "S = 2√2 − 4.4e-16."),
    ),
    "en": dict(
        t="AB Cloud Quantum Research — flagship atlas (4 dimensions)",
        a="a) blind ζ-zero reading, T ≤ 1000 (E17)",
        b="b) exact AB-cloud compiler (V20)",
        c="c) trace H_ξ ↔ primes (V7 · Th6)",
        d="d) no-signaling nonlocality (V24 preview)",
        cap=("Numbers from committed verdicts: 649+639 blind, "
             "cross-engine 0.0; 1−F ≤ 4.4e-16; r = 0.9996 vs 0.76; "
             "S = 2√2 − 4.4e-16."),
    ),
}


def clean(ax):
    ax.set_facecolor(T["panel"])
    for s in ax.spines.values():
        s.set_color(T["grid"])
    ax.tick_params(colors=T["muted"], labelsize=8)
    ax.grid(True, color=T["grid"], lw=0.5, alpha=0.6)


def fig(lang):
    P = L[lang]
    fig, axs = plt.subplots(2, 2, figsize=(11, 8.2), dpi=100,
                            constrained_layout=True)
    a, b, c, d = axs.ravel()
    fig.patch.set_facecolor(T["bg"])

    # a) слепые нули
    vals = [e17["n_detected_em"], e17["n_detected_rs"], 649]
    labels = ["ЭМ" if lang == "ru" else "EM",
              "Риман–Зигель" if lang == "ru" else "Riemann–Siegel",
              "N(1000) эталон" if lang == "ru" else "N(1000) reference"]
    a.bar(range(3), vals, width=0.55,
          color=[T["copper"], T["line"], "none"],
          edgecolor=[T["ink"]] * 3, linewidth=[0.5, 0.5, 1.4])
    for i, v in enumerate(vals):
        a.text(i, v + 12, str(v), ha="center", fontsize=9, color=T["ink"])
    a.set_xticks(range(3))
    a.set_xticklabels(labels, fontsize=8.5)
    a.set_ylim(0, 730)
    a.set_ylabel("нулей" if lang == "ru" else "zeros", fontsize=9,
                 color=T["ink"])
    a.set_title(P["a"], fontsize=10, color=T["ink"])
    clean(a)

    # b) компилятор
    m4 = v20["compiler"]["m4"]["max_one_minus_F"]
    m8 = v20["compiler"]["m8"]["max_one_minus_F"]
    th4 = v20["compiler"]["m4"]["threshold"]
    th8 = v20["compiler"]["m8"]["threshold"]
    b.bar([0, 1], [max(m4, 1e-18), max(m8, 1e-18)], width=0.5,
          color=[T["line"], T["slate"]], edgecolor=T["ink"], linewidth=0.5)
    b.axhline(th4, color=T["bad"], ls="--", lw=1.3)
    b.axhline(th8, color=T["gold"], ls=":", lw=1.3)
    b.text(0.52, th4 * 2.2, f"порог 4×4: 1e-12", fontsize=7.5,
           color=T["bad"])
    b.text(0.52, th8 * 0.35, f"порог 8×8: 1e-10", fontsize=7.5,
           color=T["gold"])
    b.text(0, m4 * 1.4, f"{m4:.1e}", ha="center", fontsize=8.5,
           color=T["ink"])
    b.text(1, m8 * 1.4, f"{m8:.1e}", ha="center", fontsize=8.5,
           color=T["ink"])
    b.set_yscale("log")
    b.set_ylim(1e-18, 1e-9)
    b.set_xticks([0, 1])
    b.set_xticklabels(["4×4 (200 целей)" if lang == "ru" else
                       "4×4 (200 targets)",
                       "8×8 (100 целей)" if lang == "ru" else
                       "8×8 (100 targets)"], fontsize=8.5)
    b.set_ylabel("max (1−F), log", fontsize=9, color=T["ink"])
    b.set_title(P["b"], fontsize=10, color=T["ink"])
    clean(b)

    # c) след ↔ простые
    r_hxi = v07["PC0_Hxi_r"]
    r_lat = v07.get("gates_rEF_mean", 0.76)
    c.bar([0, 1], [r_hxi, r_lat], width=0.5,
          color=[T["copper"], T["muted"]], edgecolor=T["ink"], linewidth=0.5)
    c.axhline(1.0, color=T["ok"], ls="--", lw=1.3)
    c.text(0.5, 1.012, "r = 1 (идеал)" if lang == "ru" else "r = 1 (ideal)",
           ha="center", fontsize=7.5, color=T["ok"])
    c.text(0, r_hxi * 0.5, f"{r_hxi:.4f}", ha="center", fontsize=10,
           color="white", fontweight="bold")
    c.text(1, r_lat * 0.5, f"{r_lat:.2f}", ha="center", fontsize=10,
           color="white", fontweight="bold")
    c.set_xticks([0, 1])
    c.set_xticklabels(["след H_ξ" if lang == "ru" else "trace H_ξ",
                       "решётка (контроль)" if lang == "ru" else
                       "lattice (control)"], fontsize=8.5)
    c.set_ylim(0, 1.15)
    c.set_ylabel("ранговая корреляция" if lang == "ru" else
                 "rank correlation", fontsize=9, color=T["ink"])
    c.set_title(P["c"], fontsize=10, color=T["ink"])
    clean(c)

    # d) CHSH
    d.bar([0], [S], width=0.32, color=T["line"], edgecolor=T["ink"],
          linewidth=0.5)
    d.axhline(2.0, color=T["bad"], ls="--", lw=1.3)
    d.axhline(2 * np.sqrt(2), color=T["ok"], ls="-", lw=1.2)
    d.text(0.22, 2.02, "классический предел 2" if lang == "ru" else
           "classical bound 2", fontsize=7.5, color=T["bad"])
    d.text(0.22, 2 * np.sqrt(2) * 1.004, "2√2 (Цирельсон)", fontsize=7.5,
           color=T["ok"])
    d.text(0, S * 0.5, f"S = {S:.6f}", ha="center", fontsize=10,
           color="white", fontweight="bold")
    d.set_xlim(-0.5, 1.1)
    d.set_ylim(0, 3.1)
    d.set_xticks([0])
    d.set_xticklabels(["CHSH"], fontsize=9)
    d.set_ylabel("S", fontsize=9, color=T["ink"])
    d.set_title(P["d"], fontsize=10, color=T["ink"])
    clean(d)

    fig.suptitle(P["t"], fontsize=13.5, fontweight="bold", color=T["ink"])
    fig.supxlabel(P["cap"], fontsize=8.6, color=T["muted"], style="italic")
    out = os.path.join(OUT, f"atlas_flagships_{lang}.png")
    fig.savefig(out, dpi=600, facecolor=T["bg"])
    plt.close(fig)
    print("OK:", out, f"({os.path.getsize(out) // 1024} KB)")


if __name__ == "__main__":
    for lang in ("ru", "en"):
        fig(lang)
