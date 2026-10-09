#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_figures.py — полный билингвальный набор рисунков проекта.

16 рисунков × 2 языка (ru/en) × 600 dpi → figures_hires/{ru,en}/,
экранные копии (160 dpi) → computations/C*/figures/.
Только закоммиченные данные data/ и computations/*/data/ — никаких
пересчётов кампаний. Детерминировано; запуск: python3 scripts/make_figures.py
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import matplotlib.pyplot as plt  # noqa: E402
from figstyle import LANG, apply, clean_axis, save_all, TOKENS  # noqa: E402

HIRES = os.path.join(ROOT, "figures_hires")
THEMES = ("light",)


def D(rel):
    return os.path.join(ROOT, rel)


def load(rel):
    return json.load(open(D(rel)))


def npz(rel, allow_pickle=False):
    return np.load(D(rel), allow_pickle=allow_pickle)


# ─────────────────────────────── C1 ─────────────────────────────────────────
def fig01_zid(t):
    z = npz("computations/C1_identity_function/data/curve_Zid.npz",
            allow_pickle=True)
    ts, vals = z["ts"], z["vals"]
    zeros, grams = z["zeros"], z["grams"]
    m = ts <= 200
    for lang in LANG:
        L = LANG[lang]
        for theme in THEMES:
            tok = apply(theme)
            fig, ax = plt.subplots(figsize=(7.6, 4.0),
                                   constrained_layout=True)
            ax.plot(ts[m], vals[m], color=tok["slate"], lw=1.1,
                    label=L["zid_title"].split(" on")[0].split(" на")[0])
            ax.scatter(zeros, np.zeros_like(zeros), s=14, zorder=5,
                       color=tok["copper"], label=L["zeros"])
            gv = [vals[np.argmin(np.abs(ts - g))] for g in grams if g <= 200]
            ax.scatter([g for g in grams if g <= 200], gv, s=10,
                       facecolor="none", edgecolor=tok["line"], lw=1.0,
                       label=L["grams"])
            ax.axhline(0, color=tok["muted"], lw=0.6, alpha=0.6)
            ax.axvline(0, color=tok["line"], lw=1.6, alpha=0.85)
            ax.set_xlabel(L["zid_x"])
            ax.set_ylabel(L["zid_y"])
            ax.set_title(L["zid_title"])
            ax.legend(loc="upper right")
            clean_axis(ax)
            save_all(fig, "fig01_zid", ROOT)
            plt.close(fig)


def fig02_ladder(t):
    u = np.linspace(0.05, 3.0, 200)
    import mpmath as mp
    mp.mp.dps = 30
    r1 = [abs(abs(mp.gamma(mp.mpf('0.5') + 1j * mp.mpf(x))) ** 2
              * mp.cosh(mp.pi * x) / mp.pi - 1) for x in u]
    r2 = [abs(abs(mp.gamma(1j * mp.mpf(x))) ** 2
              * x * mp.sinh(mp.pi * x) / mp.pi - 1) for x in u]
    r3 = [abs(abs(mp.gamma(mp.mpf('0.25') + 1j * mp.mpf(x)))
              * abs(mp.gamma(mp.mpf('0.75') + 1j * mp.mpf(x)))
              * mp.sqrt(mp.cosh(2 * mp.pi * x)) / (mp.pi * mp.sqrt(2)) - 1)
          for x in u]
    r1, r2, r3 = map(np.array, (r1, r2, r3))
    for lang in LANG:
        L = LANG[lang]
        for theme in THEMES:
            tok = apply(theme)
            fig, ax = plt.subplots(figsize=(7.0, 3.8),
                                   constrained_layout=True)
            ax.semilogy(u, r1 + 1e-40, color=tok["line"], label=L["ladder1"])
            ax.semilogy(u, r2 + 1e-40, color=tok["copper"], label=L["ladder2"])
            ax.semilogy(u, r3 + 1e-40, color=tok["slate"], label=L["ladder3"])
            ax.set_xlabel(L["u"])
            ax.set_ylabel(L["residual"])
            ax.set_title(L["ladder_title"])
            ax.legend(loc="center right")
            clean_axis(ax)
            save_all(fig, "fig02_gamma_ladder", ROOT)
            plt.close(fig)


# ─────────────────────────────── C2 ─────────────────────────────────────────
def fig03_argument(t):
    d = load("data/c2_argument_verdict.json")
    sc = d["S_curve"]
    T, S = np.array(sc["T"]), np.array(sc["S"])
    anchors = [(float(k.split("=")[1]), v["N_int"])
               for k, v in d["anchors"].items()]
    bT = [float(k.split("=")[1]) for k in d["blocks"]]
    bN = [v["N_int"] for v in d["blocks"].values()]
    for lang in LANG:
        L = LANG[lang]
        for theme in THEMES:
            tok = apply(theme)
            fig, ax = plt.subplots(figsize=(7.4, 4.0),
                                   constrained_layout=True)
            ax.scatter(bT, bN, s=26, color=tok["copper"], zorder=5,
                       label=L["anchors"])
            ax.plot(T, T / (2 * np.pi) * np.log(T / (2 * np.pi * np.e))
                    + 0.625, color=tok["line"], lw=1.2, alpha=0.9,
                    label="N̄(T)")
            ax2 = ax.twinx()
            ax2.plot(T, S, color=tok["muted"], lw=1.0, ls="--")
            ax2.set_ylabel(L["S_y"], color=tok["muted"])
            ax2.spines["top"].set_visible(False)
            ax.set_xlabel(L["T_x"])
            ax.set_ylabel(L["N_y"])
            ax.set_title(L["arg_title"])
            ax.legend(loc="upper left")
            clean_axis(ax)
            save_all(fig, "fig03_argument", ROOT)
            plt.close(fig)


def fig04_gaps(t):
    z = npz("computations/C2_argument_principle/data/curve.npz",
            allow_pickle=True)
    h = z["heights"]
    gaps = np.diff(h)
    for lang in LANG:
        L = LANG[lang]
        for theme in THEMES:
            tok = apply(theme)
            fig, ax = plt.subplots(figsize=(7.0, 3.6),
                                   constrained_layout=True)
            ax.plot(h[:-1], gaps, ".", ms=2.4, color=tok["copper"],
                    alpha=0.75)
            ax.axhline(1.521, color=tok["line"], lw=1.4, label=L["gap_mean"])
            ax.set_xlabel(L["T_x"])
            ax.set_ylabel(L["gap_y"])
            ax.set_title(L["gap_title"])
            ax.legend(loc="upper right")
            clean_axis(ax)
            save_all(fig, "fig04_gaps", ROOT)
            plt.close(fig)


# ─────────────────────────────── C3 ─────────────────────────────────────────
def fig05_gates(t):
    rows = list(np.genfromtxt(D("data/c3_gates_table.csv"), delimiter=",",
                              names=True, dtype=None, encoding="utf-8"))
    r7 = np.array([r["r_H7"] for r in rows])
    for lang in LANG:
        L = LANG[lang]
        for theme in THEMES:
            tok = apply(theme)
            fig, ax = plt.subplots(figsize=(7.6, 3.8),
                                   constrained_layout=True)
            ax.axhspan(-0.14, 0.14, color=tok["grid"], alpha=0.5,
                       label=L["null_band"].replace("0.00", "0.14"))
            ax.plot(r7, "o", ms=4, color=tok["slate"], lw=0)
            ax.axhline(0.226, color=tok["gold"], lw=1.3, ls="--",
                       label=L["c3_best"])
            ax.axhline(1.0, color=tok["copper"], lw=1.3,
                       label=L["pc_line"])
            ax.axhline(-1.0, color=tok["copper"], lw=1.3)
            ax.set_xlabel("gate #")
            ax.set_ylabel("r_H7")
            ax.set_title(L["rEF_title"].replace("r_EF", "r_H7"))
            ax.legend(loc="upper right")
            clean_axis(ax)
            save_all(fig, "fig05_gates", ROOT)
            plt.close(fig)


# ─────────────────────────────── C4 ─────────────────────────────────────────
def fig06_trace(t):
    d = load("data/c4_trace_verdict.json")
    xs = [r["x"] for r in d["M1_trace_formula"]]
    kd = [r["K_direct"] for r in d["M1_trace_formula"]]
    kf = [r["K_formula"] for r in d["M1_trace_formula"]]
    for lang in LANG:
        L = LANG[lang]
        for theme in THEMES:
            tok = apply(theme)
            fig, ax = plt.subplots(figsize=(7.0, 3.9),
                                   constrained_layout=True)
            ax.semilogy(xs, np.abs(kd), "o-", ms=4, color=tok["copper"],
                        label=L["K_direct"])
            ax.semilogy(xs, np.abs(kf), "s--", ms=4, color=tok["line"],
                        label=L["K_formula"])
            ax.set_xlabel(L["x_ax"])
            ax.set_ylabel("|K(x)|")
            ax.set_title(L["trace_title"])
            ax.legend(loc="lower left")
            clean_axis(ax)
            save_all(fig, "fig06_trace", ROOT)
            plt.close(fig)


def fig07_parts(t):
    d = load("data/c4_trace_verdict.json")
    sh = d["prime_share"]
    xs = [r["x"] for r in sh]
    T1 = [r["T1"] for r in sh]
    T2 = [r["T2"] for r in sh]
    T3 = [r["T3"] for r in sh]
    K = [a + b + c for a, b, c in zip(T1, T2, T3)]
    for lang in LANG:
        L = LANG[lang]
        for theme in THEMES:
            tok = apply(theme)
            fig, ax = plt.subplots(figsize=(7.0, 3.9),
                                   constrained_layout=True)
            ax.semilogy(xs, np.abs(K), "o-", ms=4, color=tok["ink"],
                        label="K(x)")
            ax.semilogy(xs, np.abs(T2), "s--", ms=4, color=tok["copper"],
                        label=L["part_T2"])
            ax.semilogy(xs, np.abs(T1), "^-.", ms=3.5, color=tok["line"],
                        label=L["part_T1"])
            ax.semilogy(xs, np.abs(T3), "v:", ms=3.5, color=tok["slate"],
                        label=L["part_T3"])
            ax.set_xlabel(L["x_ax"])
            ax.set_ylabel("|part|")
            ax.set_title(L["parts_title"])
            ax.legend(loc="lower left")
            clean_axis(ax)
            save_all(fig, "fig07_parts", ROOT)
            plt.close(fig)


def fig08_rEF(t):
    d = load("data/c4_trace_verdict.json")
    g = d["gates"]
    r = np.array([x["r_EF"] for x in g])
    z = npz("computations/C4_trace_formula/data/curves.npz")
    U, P, Dx = z["U"], z["P_ref"], z["D_xi"]
    c = float(np.dot(Dx, P) / np.dot(P, P))
    r_pc = float(np.corrcoef(Dx, c * P)[0, 1])
    for lang in LANG:
        L = LANG[lang]
        for theme in THEMES:
            tok = apply(theme)
            fig, ax = plt.subplots(figsize=(7.6, 3.8),
                                   constrained_layout=True)
            ax.axhspan(-0.39, 0.39, color=tok["grid"], alpha=0.5,
                       label=L["null_band"])
            ax.plot(r, "o", ms=4, color=tok["slate"], lw=0)
            ax.axhline(r_pc, color=tok["copper"], lw=1.4, label=L["PC0"])
            ax.set_xlabel("gate #")
            ax.set_ylabel(L["rEF_y"])
            ax.set_title(L["rEF_title"])
            ax.legend(loc="upper right")
            clean_axis(ax)
            save_all(fig, "fig08_rEF", ROOT)
            plt.close(fig)


# ─────────────────────────────── C5 ─────────────────────────────────────────
def fig09_handles(t):
    rows = list(np.genfromtxt(D("data/c5_gates_ext_table.csv"), delimiter=",",
                              names=True, dtype=None, encoding="utf-8"))
    names = [str(r["name"]) for r in rows]
    r7 = np.abs(np.array([r["r_H7"] for r in rows]))
    for lang in LANG:
        L = LANG[lang]
        for theme in THEMES:
            tok = apply(theme)
            fig, ax = plt.subplots(figsize=(8.6, 3.9),
                                   constrained_layout=True)
            cols = [tok["bad"] if n.startswith("D_") else tok["slate"]
                    for n in names]
            ax.bar(range(len(names)), r7, color=cols)
            ax.axhline(0.226, color=tok["gold"], ls="--", lw=1.3,
                       label=L["c3_best"])
            ax.axhline(1.0, color=tok["copper"], lw=1.3, label=L["pc_line"])
            ax.set_xticks(range(len(names)))
            ax.set_xticklabels([n[2:] for n in names], rotation=90,
                               fontsize=6.2)
            ax.set_ylabel(L["ext_y"])
            ax.set_title(L["ext_title"])
            ax.legend(loc="upper right")
            clean_axis(ax)
            save_all(fig, "fig09_handles", ROOT)
            plt.close(fig)


def fig10_gue_ext(t):
    rows = list(np.genfromtxt(D("data/c5_gates_ext_table.csv"), delimiter=",",
                              names=True, dtype=None, encoding="utf-8"))
    rm = np.array([r["r_mean"] for r in rows])
    for lang in LANG:
        L = LANG[lang]
        for theme in THEMES:
            tok = apply(theme)
            fig, ax = plt.subplots(figsize=(7.0, 3.4),
                                   constrained_layout=True)
            ax.axhspan(0.47, 0.53, color=tok["grid"], alpha=0.5)
            ax.plot(rm, "o", ms=4, color=tok["line"], lw=0)
            ax.axhline(0.5, color=tok["muted"], lw=1.0, ls="--")
            ax.set_xlabel("gate #")
            ax.set_ylabel(L["ladder_y"])
            ax.set_title(L["ladder_title2"] + " — C5")
            clean_axis(ax)
            save_all(fig, "fig10_gue_ext", ROOT)
            plt.close(fig)


# ─────────────────────────────── C6 ─────────────────────────────────────────
def fig11_coloc(t):
    d = load("data/c6_primes_verdict.json")
    ker = d["M1_factorization_kernel"]["kernel"]
    arr = [(r["d"], r["delta_composite"]) for r in ker]
    dd = np.array([a for a, _ in arr])
    kk = np.array([b for _, b in arr])
    for lang in LANG:
        L = LANG[lang]
        for theme in THEMES:
            tok = apply(theme)
            fig, ax = plt.subplots(figsize=(6.6, 3.5),
                                   constrained_layout=True)
            ax.plot(dd, kk, "o-", ms=4.5, color=tok["copper"])
            ax.set_xlabel(L["d_ax"])
            ax.set_ylabel(L["coloc_y"])
            ax.set_title(L["coloc_title"])
            clean_axis(ax)
            save_all(fig, "fig11_coloc", ROOT)
            plt.close(fig)


def fig12_psi(t):
    d = load("data/c6_primes_verdict.json")
    m2 = d["M2_prime_staircase"]
    x = np.array(m2["x_grid"])
    for lang in LANG:
        L = LANG[lang]
        for theme in THEMES:
            tok = apply(theme)
            fig, ax = plt.subplots(figsize=(7.2, 3.9),
                                   constrained_layout=True)
            ax.plot(x, m2["psi_true"], lw=2.2, color=tok["line"],
                    label=L["sieve"])
            ax.plot(x, m2["psi_Z200"], lw=1.2, ls="--", color=tok["copper"],
                    label=L["zeta"])
            ax.set_xlabel(L["x_psi"])
            ax.set_ylabel(L["psi_y"])
            ax.set_title(L["psi_title"])
            ax.legend(loc="upper left")
            clean_axis(ax)
            save_all(fig, "fig12_psi", ROOT)
            plt.close(fig)


# ─────────────────────────────── C7 ─────────────────────────────────────────
def fig13_dynamics(t):
    d = load("data/c7_dynamics_verdict.json")
    keys = [("clean", "clean"), ("z16", "z16"), ("z64", "z64"),
            ("z256", "z256"), ("r256", "r256")]
    for lang in LANG:
        L = LANG[lang]
        for theme in THEMES:
            tok = apply(theme)
            fig, ax = plt.subplots(figsize=(7.4, 3.9),
                                   constrained_layout=True)
            colors = [tok["line"], tok["copper"], tok["gold"],
                      tok["slate"], tok["muted"]]
            for (k, lab), col in zip(keys, colors):
                if k in d:
                    ax.plot(d[k]["t"], d[k]["mx"], lw=1.4, color=col,
                            label=L[lab])
            ax.set_xlabel(L["t_ax"])
            ax.set_ylabel(L["mx_y"])
            ax.set_title(L["dyn_title"])
            ax.legend(loc="upper right", ncols=2)
            clean_axis(ax)
            save_all(fig, "fig13_dynamics", ROOT)
            plt.close(fig)


# ─────────────────────────────── C8 ─────────────────────────────────────────
def fig14_ladder(t):
    d = load("computations/C8_stats_ladder/data/ladder/stats_ladder.json")
    rows = d["results"]
    labels, vals = [], []
    for r in rows:
        lab = f"Nv{r['Nv']},W{r['extra_disorder_w']}" \
            if r.get("extra_disorder_w") else f"Nv{r['Nv']}"
        labels.append(lab)
        vals.append(r["r_mean"])
    for lang in LANG:
        L = LANG[lang]
        for theme in THEMES:
            tok = apply(theme)
            fig, ax = plt.subplots(figsize=(7.6, 3.7),
                                   constrained_layout=True)
            cols = [tok["copper"] if v > 0.56 else
                    (tok["slate"] if v > 0.45 else tok["muted"])
                    for v in vals]
            ax.bar(range(len(vals)), vals, color=cols)
            ax.axhline(0.386, color=tok["muted"], ls=":", lw=1.2,
                       label=L["poi"])
            ax.axhline(0.531, color=tok["slate"], ls="--", lw=1.2,
                       label=L["goe"])
            ax.axhline(0.602, color=tok["copper"], ls="-.", lw=1.2,
                       label=L["gue"])
            ax.set_xticks(range(len(vals)))
            ax.set_xticklabels(labels, rotation=60, fontsize=6.6)
            ax.set_ylabel(L["ladder_y"])
            ax.set_title(L["ladder_title2"])
            ax.legend(loc="upper right")
            clean_axis(ax)
            save_all(fig, "fig14_ladder", ROOT)
            plt.close(fig)


def fig15_spinor(t):
    sp = load("computations/C8_stats_ladder/data/spinor64/spinor64_check.json")
    e2 = sp["E2_reduction"]
    vals = e2["unique_r_mean_values_in_their_table"]
    for lang in LANG:
        L = LANG[lang]
        for theme in THEMES:
            tok = apply(theme)
            fig, ax = plt.subplots(figsize=(5.8, 3.3),
                                   constrained_layout=True)
            ax.bar(range(len(vals)), vals, color=tok["line"], width=0.55)
            ax.set_ylim(0.58, 0.61)
            ax.set_xticks(range(len(vals)))
            ax.set_xticklabels(["φx0 φy0", "φx0 φy1", "φx1 φy0",
                                "φx1 φy1"], fontsize=8)
            ax.set_ylabel(L["ladder_y"])
            ttl = {"ru": "spinor64: 64 спин-структуры → 4 гамильтониана",
                   "en": "spinor64: 64 spin structures → 4 Hamiltonians"}[lang]
            ax.set_title(ttl)
            clean_axis(ax)
            save_all(fig, "fig15_spinor", ROOT)
            plt.close(fig)


# ────────────────────────── flagship map figures ────────────────────────────
def fig16_map(t):
    """Карта моста: расстояние (в порядках) между графиком и оператором
    в трёх проекциях: r_H7 (C3), ψ (C6), r_EF (C4)."""
    data = {
        "ru": {
            "title": "Карта моста «график ↔ оператор» в трёх проекциях",
            "ylabel": "корреляция с эталоном; * r_EF — консервативная метрика "
                  "(невязки: затвор 6.7% против PC0 2.1%)",
            "series": ["r_H7 (C3)", "ψ-лестница (C6)", "r_EF* (C4)"],
            "labels": ["лучший затвор", "нулевой максимум",
                       "позитивный контроль"],
            "gate_vals": [0.226, 0.239, 0.998],
            "pc_vals": [1.0, 0.972, 0.9998],
        },
        "en": {
            "title": "Bridge map graph ↔ operator in three projections",
            "ylabel": "correlation with reference; * r_EF is a conservative metric "
                  "(residuals: gate 6.7% vs PC0 2.1%)",
            "series": ["r_H7 (C3)", "ψ-ladder (C6)", "r_EF* (C4)"],
            "labels": ["best gate", "null maximum", "positive control"],
            "gate_vals": [0.226, 0.239, 0.998],
            "pc_vals": [1.0, 0.972, 0.9998],
        },
    }
    for lang in ("ru", "en"):
        dd = data[lang]
        for theme in THEMES:
            tok = apply(theme)
            x = np.arange(3)
            fig, ax = plt.subplots(figsize=(7.0, 3.8),
                                   constrained_layout=True)
            ax.bar(x - 0.18, dd["gate_vals"], width=0.34,
                   color=tok["slate"], label=dd["labels"][0])
            ax.bar(x + 0.18, dd["pc_vals"], width=0.34,
                   color=tok["copper"], label=dd["labels"][2])
            for xi in x:
                ax.axhline(0, color=tok["muted"], lw=0.6)
            ax.set_xticks(x)
            ax.set_xticklabels(dd["series"], fontsize=9)
            ax.set_ylim(0, 1.12)
            ax.set_ylabel(dd["ylabel"])
            ax.set_title(dd["title"])
            ax.legend(loc="upper left")
            clean_axis(ax)
            save_all(fig, "fig16_map", ROOT)
            plt.close(fig)


ALL_FIGS = [fig01_zid, fig02_ladder, fig03_argument, fig04_gaps,
            fig05_gates, fig06_trace, fig07_parts, fig08_rEF,
            fig09_handles, fig10_gue_ext, fig11_coloc, fig12_psi,
            fig13_dynamics, fig14_ladder, fig15_spinor, fig16_map]

if __name__ == "__main__":
    import time
    t0 = time.time()
    for i, f in enumerate(ALL_FIGS, 1):
        f(i)
        print(f"[{time.time()-t0:6.1f}s] fig{i:02d} {f.__name__} OK")
    print("ALL FIGURES DONE")
