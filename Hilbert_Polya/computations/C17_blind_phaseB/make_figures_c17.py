#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_figures_c17.py — рисунки fig29–32 (ru/en) для отчёта C17.
Данные: computations/C17_blind_phaseB/data/results.json (+ нули mpmath)."""
import json
import os
import sys

import numpy as np

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(R, "scripts"))
import figstyle  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "figures")
os.makedirs(OUT, exist_ok=True)
res = json.load(open(os.path.join(HERE, "data", "results.json")))

import mpmath as _mp  # noqa: E402
_mp.mp.dps = 30
gam = np.array([float(_mp.im(_mp.zetazero(n))) for n in range(1, 60)])

LANG = {
    "ru": dict(
        t1="C17b: узлы арифметической меры против нулей ζ (окно W1)",
        t1b="окно W2",
        zeros="нули ζ (mpmath)", nodes="узлы C17b (только простые и θ)",
        null="узлы null-модели без простых", x="высота t",
        t2="Декомпозиция ошибки: расстояние до квадратуры истинной гребёнки",
        y2="RMS расстояние до узлов истинной гребёнки",
        c17b="C17b (простые + θ)", n0="null без простых", flip="контроль фаза-минус",
        gap="инструментальный зазор квадратауры",
        t3="Плотность явной формулы против сглаженной гребёнки нулей (W1)",
        rho="ρ̃(t): только простые и θ", comb="истинная гребёнка (диагностика фазы C)",
        t4="Профили якобиевой матрицы: фильм против C17b (W1)",
        a_y="α_n", b_y="β_n", film="фильм (мера из нулей и весов)",
        c17="C17b W1 (мера из арифметики)"),
    "en": dict(
        t1="C17b: nodes of the arithmetic measure vs zeta zeros (window W1)",
        t1b="window W2",
        zeros="zeta zeros (mpmath)", nodes="C17b nodes (primes and theta only)",
        null="no-prime null nodes", x="height t",
        t2="Error decomposition: distance to the true-comb quadrature",
        y2="RMS distance to true-comb quadrature nodes",
        c17b="C17b (primes + theta)", n0="no-prime null", flip="phase-flip control",
        gap="quadrature instrument gap",
        t3="Explicit-formula density vs the smoothed zero comb (W1)",
        rho="rho(t): primes and theta only", comb="true comb (phase-C diagnostics)",
        t4="Jacobi profiles: the film vs C17b (W1)",
        a_y="alpha_n", b_y="beta_n", film="film (measure from zeros, weights)",
        c17="C17b W1 (measure from arithmetic)"),
}

tok = figstyle.apply("light")
import matplotlib.pyplot as plt  # noqa: E402

b = res["stage2_c17b"]["verify"]
for lang in ("ru", "en"):
    L = LANG[lang]
    ddir = os.path.join(OUT, lang)
    os.makedirs(ddir, exist_ok=True)

    # ── fig29: узлы vs нули, оба окна ───────────────────────────────────────
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.2), constrained_layout=True)
    for ax, tag in zip(axs, ("W1", "W2")):
        v = b[tag]
        z = np.array(v["zeros"]); nd = np.array(v["nodes"])
        n0 = np.array(v["nodes_N0"])
        ax.scatter(z, z, s=26, color=tok["copper"], zorder=3, label=L["zeros"])
        ax.scatter(z, nd, s=15, color=tok["line"], zorder=4, label=L["nodes"])
        ax.scatter(z, n0, s=15, facecolors="none", edgecolors=tok["slate"],
                   zorder=2, label=L["null"])
        d = np.abs(v["deltas"])
        ax.set_title(f"{tag}: RMS = {v['err_rms']:.3f}, z = {v['z_gue']:.1f}",
                     fontsize=11)
        ax.set_xlabel(L["x"]); ax.set_ylabel(L["x"])
        ax.set_xlim(z[0] - 4, z[-1] + 4); ax.set_ylim(z[0] - 4, z[-1] + 4)
        figstyle.clean_axis(ax)
    fig.suptitle(L["t1"], fontsize=12, fontweight="bold")
    axs[0].legend(loc="upper left")
    fig.savefig(os.path.join(ddir, "fig29_c17b_nodes.png"), dpi=220)
    plt.close(fig)

    # ── fig30: декомпозиция ─────────────────────────────────────────────────
    dec = res["decomposition_c17b"]
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.0), constrained_layout=True)
    fig.suptitle(L["t2"], fontsize=12, fontweight="bold")
    for ax, tag in zip(axs, ("W1", "W2")):
        d = dec[tag]
        names = [L["c17b"], L["n0"], L["flip"]]
        vals = [d["rms_c17b_vs_truequad"], d["rms_N0_vs_truequad"],
                d["rms_phaseflip_vs_truequad"]]
        cols = [tok["line"], tok["slate"], tok["bad"]]
        bars = ax.bar(names, vals, color=cols, width=0.55)
        ax.axhline(d["rms_truequad_vs_zeros"], color=tok["gold"], ls="--", lw=1.4)
        ax.text(0.02, d["rms_truequad_vs_zeros"] * 1.05 + 0.02,
                f"{L['gap']} = {d['rms_truequad_vs_zeros']:.3f}",
                color=tok["gold"], fontsize=9, transform=ax.get_yaxis_transform())
        for bb, vv in zip(bars, vals):
            ax.text(bb.get_x() + bb.get_width() / 2, vv + 0.04, f"{vv:.3f}",
                    ha="center", fontsize=9, color=tok["ink"])
        ax.set_title(f"{tag}", fontsize=11)
        ax.set_ylabel(L["y2"])
        figstyle.clean_axis(ax)
    fig.savefig(os.path.join(ddir, "fig30_c17_decomposition.png"), dpi=220)
    plt.close(fig)

    # ── fig31: плотность против гребёнки (W1) ───────────────────────────────
    sys.path.insert(0, os.path.join(R, "campaigns"))
    from run_c17_blind_phaseB import (sieve_primes, rho_grid, dbar_np,
                                      SIGMA, KMAX, PMAX)
    pr, lnp = sieve_primes(PMAX)
    pf = pr.astype(np.float64)
    T1, T2 = res["stage2_c17b"]["verify"]["W1"]["zeros"][0], None
    # окно C17b W1 берём из результатов слепого прогона
    T1 = res["stage2_c17b"]["verify"]["W1"]["_w1"] if "_w1" in res["stage2_c17b"]["verify"]["W1"] else 23.21
    T2 = 80.99
    ts = np.linspace(T1, T2, 2400)
    rho = rho_grid(ts, lnp, pf, SIGMA, KMAX)
    truth = np.zeros_like(ts)
    zin = gam[(gam > T1) & (gam < T2)]
    for g in zin:
        truth += np.exp(-0.5 * ((ts - g) / SIGMA) ** 2) / (SIGMA * np.sqrt(2 * np.pi))
    fig, ax = plt.subplots(figsize=(11, 4.0), constrained_layout=True)
    ax.plot(ts, rho, color=tok["line"], lw=1.3, label=L["rho"])
    ax.fill_between(ts, truth, color=tok["copper"], alpha=0.25, label=L["comb"])
    ax.set_title(L["t3"], fontsize=12)
    ax.set_xlabel(L["x"]); ax.set_ylabel("density")
    ax.legend(loc="upper right")
    figstyle.clean_axis(ax)
    fig.savefig(os.path.join(ddir, "fig31_c17_density.png"), dpi=220)
    plt.close(fig)

    # ── fig32: профили альфа/бета: фильм vs C17b W1 ─────────────────────
    film = json.load(open(os.path.join(R, "video", "pixel_decoding_data.json")))
    af = np.array(film["alphas"]); bf = np.array(film["betas"])
    vw = res["stage2_c17b"]["verify"]["W1"]
    al_c = np.array(vw["alphas_c17b"]); be_c = np.array(vw["betas_c17b"])
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.0), constrained_layout=True)
    fig.suptitle(L["t4"], fontsize=12, fontweight="bold")
    n1 = np.arange(1, af.size + 1); n2 = np.arange(1, al_c.size + 1)
    axs[0].plot(n1, af, "o-", color=tok["copper"], ms=4, lw=1.2, label=L["film"])
    axs[0].plot(n2, al_c, "s-", color=tok["line"], ms=4, lw=1.2, label=L["c17"])
    axs[0].set_title(L["a_y"], fontsize=11)
    axs[0].set_xlabel("n"); axs[0].set_ylabel(L["a_y"]); axs[0].legend()
    figstyle.clean_axis(axs[0])
    m1 = np.arange(1, bf.size + 1); m2 = np.arange(1, be_c.size + 1)
    axs[1].plot(m1, bf, "o-", color=tok["copper"], ms=4, lw=1.2, label=L["film"])
    axs[1].plot(m2, be_c, "s-", color=tok["line"], ms=4, lw=1.2, label=L["c17"])
    axs[1].set_title(L["b_y"] + " (W1)", fontsize=11)
    axs[1].set_xlabel("n"); axs[1].set_ylabel(L["b_y"]); axs[1].legend()
    figstyle.clean_axis(axs[1])
    fig.savefig(os.path.join(ddir, "fig32_c17_profiles.png"), dpi=220)
    plt.close(fig)
    print(lang, "figures done")
print("all figures written to", OUT)
