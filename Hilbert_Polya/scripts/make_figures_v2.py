#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_figures_v2.py — билингвальные рисунки 600 dpi для кампаний C9–C16.

Палитра и правила — scripts/figstyle.py (Critical Line & Copper).
Рисунки: fig17_nonlocal, fig18_coloc, fig19_alphathird, fig20_band5000,
fig21_blind, fig22_anomaly, fig23_dirichlet, fig24_qinfo, fig25_map.
Сохранение: figures_hires/{lang}/ (600 dpi) + копии в computations/C*/figures/.
"""
import json, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)

import figstyle  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

V2 = {
    "en": {
        "nonloc_title": "C9 · Nonlocal trace primitive: rank and heat metrics",
        "nonloc_y": "metric value", "rH7": "r_H7 (rank)", "rEF": "r_EF fluct (heat)",
        "pc": "positive control r = 1", "null": "GUE null 0.04±0.05",
        "coloc_title": "C10 · Hard co-location (T12): residual and spectra",
        "coloc_res": "co-location max residual", "beta_x": "phase handle β",
        "rH7_beta": "r_H7(β)", "machine_zero": "machine zero",
        "alpha_title": "C11 · α=1/3 zero modes: arithmetic law (T13)",
        "n0_y": "zero modes N₀", "L_x": "lattice L",
        "law": "law 2L−6·[L≡0 mod 12]", "idx": "index −2 subfamily",
        "band_title": "C12 · Argument principle to T=5000 (T14)",
        "S_y": "S(T) = N − N̄", "N_y": "N(T)", "anchors": "v1 anchors",
        "blind_title": "C13 · Blind families: |r_H7| by gate",
        "anom_title": "C14 · Anomaly hunt: ⟨r⟩ taxonomy",
        "r_y": "⟨r⟩ (spacing ratio)", "gue_line": "GUE 0.5996",
        "poi_line": "Poisson 0.386", "classes": "gue / intermediate / integrable",
        "diri_title": "C15 · Dirichlet χ₅, χ₇: Z_χ and K_χ (T17)",
        "kchi": "K_χ direct", "kchif": "K_χ formula (1/π)∫Q_χ sin",
        "qinfo_title": "C16 · Fermionic entanglement: locality echo (T18)",
        "S_y2": "S_vN half (nats)", "fill_x": "filling",
        "gate": "gate Nv=16", "haar": "GUE Haar baseline",
        "map_title": "v2.0 · Bridge map: eight new campaigns",
    },
    "ru": {
        "nonloc_title": "C9 · Нелокальный примитив: ранговая и тепловая метрики",
        "nonloc_y": "значение метрики", "rH7": "r_H7 (ранговая)",
        "rEF": "r_EF fluct (тепловая)",
        "pc": "позитивный контроль r = 1", "null": "GUE-нуль 0.04±0.05",
        "coloc_title": "C10 · Жёсткая ко-локация (T12): невязка и спектры",
        "coloc_res": "макс. невязка ко-локации", "beta_x": "фазовая ручка β",
        "rH7_beta": "r_H7(β)", "machine_zero": "машинный нуль",
        "alpha_title": "C11 · Нулевые моды α=1/3: арифметический закон (T13)",
        "n0_y": "нулевые моды N₀", "L_x": "решётка L",
        "law": "закон 2L−6·[L≡0 mod 12]", "idx": "подсемейство индекса −2",
        "band_title": "C12 · Аргументный принцип до T=5000 (T14)",
        "S_y": "S(T) = N − N̄", "N_y": "N(T)", "anchors": "якоря v1",
        "blind_title": "C13 · Слепые семейства: |r_H7| по затворам",
        "anom_title": "C14 · Поиск аномалий: таксономия ⟨r⟩",
        "r_y": "⟨r⟩ (отношение зазоров)", "gue_line": "GUE 0.5996",
        "poi_line": "Пуассон 0.386", "classes": "gue / промежуточные / интегрируемые",
        "diri_title": "C15 · Дирихле χ₅, χ₇: Z_χ и K_χ (T17)",
        "kchi": "K_χ прямая сумма", "kchif": "K_χ формула (1/π)∫Q_χ sin",
        "qinfo_title": "C16 · Фермионная запутанность: эхо локальности (T18)",
        "S_y2": "S_vN половины (нат)", "fill_x": "заполнение",
        "gate": "затвор Nv=16", "haar": "GUE Haar-база",
        "map_title": "v2.0 · Карта моста: восемь новых кампаний",
    },
}


def save_all(fig, stem, langs=("ru", "en"), dpi=600):
    paths = []
    for lang in langs:
        d = os.path.join(ROOT, "figures_hires", lang)
        os.makedirs(d, exist_ok=True)
        p = os.path.join(d, f"{stem}_{lang}.png")
        fig.savefig(p, dpi=dpi)
        paths.append(p)
    plt.close(fig)
    return paths


def copy_to_campaign(stem, camps):
    import shutil
    for lang in ("ru", "en"):
        src = os.path.join(ROOT, "figures_hires", lang, f"{stem}_{lang}.png")
        for c in camps:
            dst = os.path.join(ROOT, "computations", c, "figures", lang)
            os.makedirs(dst, exist_ok=True)
            shutil.copy(src, dst)


def fig_nonlocal(t):
    d = json.load(open(f"{ROOT}/computations/C9_nonlocal_trace/data/results.json"))
    U = np.load(f"{ROOT}/computations/C9_nonlocal_trace/data/curves.npz")
    names = ["N1_Hxi", "N2_DCT_twin", "N3_QR_twin", "N4_BerryKeating",
             "N5_LCM_kernel"]
    r7 = [d["results"][n].get("r_H7_matched", d["results"][n].get("r_H7")) or 0
          for n in names]
    ref = [d["results"][n]["r_EF"]["r_fluct"] for n in names]
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), constrained_layout=True)
    x = np.arange(len(names))
    axes[0].bar(x - 0.2, r7, 0.4, color=t["line"], label=t["rH7"])
    axes[0].bar(x + 0.2, ref, 0.4, color=t["copper"], label=t["rEF"])
    axes[0].axhline(1.0, color=t["ok"], ls="--", lw=1, label=t["pc"])
    axes[0].axhspan(-0.10, 0.18, color=t["grid"], alpha=0.3, label=t["null"])
    axes[0].set_xticks(x)
    axes[0].set_xticklabels(["H_ξ", "DCT", "QR", "xp", "LCM"], fontsize=9)
    axes[0].set_title(t["nonloc_title"], fontsize=11)
    axes[0].set_ylabel(t["nonloc_y"])
    axes[0].legend(fontsize=8)
    figstyle.clean_axis(axes[0])
    axes[1].plot(U["U"], U["D_xi"], color=t["line"], lw=1.5,
                 label="D(u), H_ξ")
    axes[1].plot(U["U"], U["P"] * (U["D_xi"].max() / U["P"].max()),
                 color=t["copper"], lw=1.2, ls="--", label="P(u) (scaled)")
    axes[1].set_xlabel("u")
    axes[1].legend(fontsize=8)
    figstyle.clean_axis(axes[1])
    return fig


def fig_coloc(t):
    d = json.load(open(f"{ROOT}/computations/C10_phase_coded/data/results.json"))
    betas = [g["beta"] for g in d["gates"] if g["mode"] == "beta"]
    r7 = [g["r_H7"] for g in d["gates"] if g["mode"] == "beta"]
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), constrained_layout=True)
    resids = [v["pairwise_max_resid"] for v in d["colocation_T12"].values()]
    axes[0].semilogy(range(len(resids)), resids, "o", color=t["line"], ms=6)
    axes[0].axhline(1e-15, color=t["ok"], ls="--", lw=1, label=t["machine_zero"])
    axes[0].set_xticks(range(len(d["colocation_T12"])))
    axes[0].set_xticklabels(list(d["colocation_T12"].keys()), fontsize=8,
                            rotation=30)
    axes[0].set_title(t["coloc_title"], fontsize=11)
    axes[0].set_ylabel(t["coloc_res"])
    axes[0].legend(fontsize=8)
    figstyle.clean_axis(axes[0])
    axes[1].plot(betas, r7, "o-", color=t["copper"], ms=5)
    axes[1].axhspan(-0.10, 0.18, color=t["grid"], alpha=0.3)
    axes[1].set_xlabel(t["beta_x"])
    axes[1].set_ylabel(t["rH7_beta"])
    figstyle.clean_axis(axes[1])
    return fig


def fig_alphathird(t):
    d = json.load(open(f"{ROOT}/computations/C11_alpha_third/data/results.json"))
    rows = [r for r in d["scan"] if r["torus_exists"]]
    Ls = [r["L"] for r in rows]
    n0 = [r["n_zero_torus"] for r in rows]
    fig, ax = plt.subplots(figsize=(7.5, 4.6), constrained_layout=True)
    ax.plot(Ls, n0, "o", color=t["copper"], ms=7, label="N₀ measured")
    Lfine = np.arange(6, 49)
    law = [2 * L - 6 * (1 if L % 12 == 0 else 0) if L % 6 == 0 else 0
           for L in Lfine]
    ax.plot(Lfine, law, "-", color=t["line"], lw=1.5, label=t["law"])
    ax.plot([L for L, r in zip(Ls, rows) if r["index_torus"] == -2],
            [n for n, r in zip(n0, rows) if r["index_torus"] == -2],
            "s", color=t["gold"], ms=10, mfc="none", mew=2, label=t["idx"])
    ax.set_xlabel(t["L_x"])
    ax.set_ylabel(t["n0_y"])
    ax.set_title(t["alpha_title"], fontsize=11)
    ax.legend(fontsize=9)
    figstyle.clean_axis(ax)
    return fig


def fig_band(t):
    d = np.load(f"{ROOT}/computations/C12_band_5000/data/curve.npz")
    j = json.load(open(f"{ROOT}/computations/C12_band_5000/data/results.json"))
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), constrained_layout=True)
    z = d["zeros"]
    Ts = np.linspace(10, 5000, 200)
    from engine.hamiltonian import rvm_count
    axes[0].plot(z, np.arange(1, z.size + 1), color=t["line"], lw=1,
                 label="N(T) on line")
    axes[0].plot(Ts, rvm_count(Ts), "--", color=t["copper"], lw=1.2,
                 label="N̄(T) smooth")
    anch = [(float(k.split("=")[1]), v["N_int"]) for k, v in j["anchors"].items()
            if v.get("expected") is not None]
    axes[0].plot([a[0] for a in anch], [a[1] for a in anch], "o",
                 color=t["gold"], ms=6, label=t["anchors"])
    axes[0].set_xlabel("T")
    axes[0].set_ylabel(t["N_y"])
    axes[0].set_title(t["band_title"], fontsize=11)
    axes[0].legend(fontsize=8)
    figstyle.clean_axis(axes[0])
    axes[1].plot(d["Ts"], d["S_vals"], color=t["line"], lw=1.2)
    axes[1].axhspan(-2, 2, color=t["ok"], alpha=0.15)
    axes[1].set_xlabel("T")
    axes[1].set_ylabel(t["S_y"])
    figstyle.clean_axis(axes[1])
    return fig


def fig_blind(t):
    d = json.load(open(f"{ROOT}/computations/C13_blind_families/data/results.json"))
    names = [g["gate"] for g in d["gates"]]
    r7 = [abs(g["r_H7"]) for g in d["gates"]]
    fams = [g["family"] for g in d["gates"]]
    colors = {f: c for f, c in zip(sorted(set(fams)),
              [t["line"], t["copper"], t["slate"], t["gold"], t["ok"]])}
    fig, ax = plt.subplots(figsize=(9.5, 4.2), constrained_layout=True)
    ax.bar(range(len(names)), r7, color=[colors[f] for f in fams])
    ax.axhspan(0, 0.10, color=t["grid"], alpha=0.35)
    ax.set_xticks(range(len(names)))
    ax.set_xticklabels(names, rotation=60, fontsize=6.5, ha="right")
    ax.set_ylabel("|r_H7|")
    ax.set_title(t["blind_title"], fontsize=11)
    figstyle.clean_axis(ax)
    return fig


def fig_anomaly(t):
    d = json.load(open(f"{ROOT}/computations/C14_anomaly_hunt/data/results.json"))
    rows = d["gates"]
    cmap = {"gue": t["line"], "intermediate": t["gold"],
            "integrable": t["copper"]}
    fig, ax = plt.subplots(figsize=(8.5, 4.6), constrained_layout=True)
    for cls in ("gue", "intermediate", "integrable"):
        xs = [i for i, r in enumerate(rows) if r.get("class") == cls]
        ys = [rows[i]["r_mean"] for i in xs]
        ax.plot(xs, ys, "o", ms=4, color=cmap[cls], label=cls)
    ax.axhline(0.5996, color=t["line"], ls="--", lw=1, label=t["gue_line"])
    ax.axhline(0.386, color=t["copper"], ls=":", lw=1, label=t["poi_line"])
    ax.set_xlabel("config #")
    ax.set_ylabel(t["r_y"])
    ax.set_title(t["anom_title"], fontsize=11)
    ax.legend(fontsize=8)
    figstyle.clean_axis(ax)
    return fig


def fig_dirichlet(t):
    d = np.load(f"{ROOT}/computations/C15_dirichlet/data/zeros_chi.npz")
    j = json.load(open(f"{ROOT}/computations/C15_dirichlet/data/results.json"))
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), constrained_layout=True)
    for q, c in ((5, t["line"]), (7, t["copper"])):
        z = d[f"z{q}"]
        axes[0].plot(z, np.arange(1, z.size + 1), color=c, lw=1.2,
                     label=f"χ_{q} zeros (n={z.size})")
        nbar = [r for r in [j["results"][f"q{q}"]]][0]["n_bar_120"]
        axes[0].axhline(nbar, color=c, ls=":", lw=1)
    axes[0].set_xlabel("γ")
    axes[0].set_ylabel("n(γ)")
    axes[0].set_title(t["diri_title"], fontsize=11)
    axes[0].legend(fontsize=8)
    figstyle.clean_axis(axes[0])
    xs = [r["x"] for r in j["results"]["q5"]["trace_formula"]]
    kd = [r["K_direct"] for r in j["results"]["q5"]["trace_formula"]]
    kf = [r["K_formula"] for r in j["results"]["q5"]["trace_formula"]]
    axes[1].plot(xs, kd, "o-", color=t["line"], ms=5, label=t["kchi"])
    axes[1].plot(xs, kf, "s--", color=t["copper"], ms=5, label=t["kchif"])
    axes[1].set_xlabel("x")
    axes[1].set_yscale("symlog", linthresh=1e-3)
    axes[1].legend(fontsize=8)
    figstyle.clean_axis(axes[1])
    return fig


def fig_qinfo(t):
    d = json.load(open(f"{ROOT}/computations/C16_qinfo/data/results.json"))
    fig, ax = plt.subplots(figsize=(7.5, 4.6), constrained_layout=True)
    fills = [p["filling"] for p in d["Q1_gate_profile"]]
    mi_gate = [p["MI"] for p in d["Q1_gate_profile"]]
    mi_clean = [p["MI"] for p in d["Q1_clean_profile"]]
    bm = d["Q1_page_baseline"]["mean"]
    bs = d["Q1_page_baseline"]["std"]
    ax.plot(fills, mi_gate, "o-", color=t["line"], label=t["gate"])
    ax.plot(fills, mi_clean, "s--", color=t["copper"], label="clean")
    ax.errorbar(fills, bm, yerr=bs, fmt="D", color=t["slate"], ms=5,
                capsize=3, label=t["haar"])
    ax.set_xlabel(t["fill_x"])
    ax.set_ylabel("MI (nats)")
    ax.set_title(t["qinfo_title"], fontsize=11)
    ax.legend(fontsize=9)
    figstyle.clean_axis(ax)
    return fig


def fig_map(t):
    fig, ax = plt.subplots(figsize=(9.5, 5.4), constrained_layout=True)
    ax.axis("off")
    items = [
        ("C9 nonlocal trace", "T11 · r_H7=1.000, r_EF=0.999 — primitive exists",
         "H2 = wall of LOCALITY"),
        ("C10 phase coding", "T12 · co-location 4.4e-16, spectrum blind",
         "universality erases hard codings"),
        ("C11 α=1/3", "T13 · N₀=2L−6·[L≡0 mod 12], index −2",
         "first arithmetic→spectrum bridge"),
        ("C12 band T=5000", "T14 · N=4520=4520, S_max=0.91",
         "RH verified in wider band"),
        ("C13 blind families", "T15 · 16 gates, all null, GUE",
         "gap robust to new designs"),
        ("C14 anomaly hunt", "T16 · 97 GUE / 18 integrable / 6 intermediate",
         "attractor global, basin structured"),
        ("C15 Dirichlet L", "T17 · |ΔK|≤9.6e-6 twisted weights",
         "H2 gap is UNIVERSAL"),
        ("C16 qinfo", "T18 · locality suppresses entanglement",
         "complexity erases arithmetic"),
    ]
    for k, (name, res, meaning) in enumerate(items):
        y = 0.93 - k * 0.115
        ax.add_patch(plt.Rectangle((0.01, y - 0.04), 0.30, 0.075,
                     color=t["panel"], ec=t["grid"]))
        ax.text(0.025, y, name, fontsize=10, weight="bold", color=t["line"])
        ax.text(0.33, y + 0.012, res, fontsize=9, color=t["ink"])
        ax.text(0.33, y - 0.028, "→ " + meaning, fontsize=8.5,
                color=t["muted"])
    ax.set_title(t["map_title"], fontsize=12)
    return fig


def main():
    stems = {
        "fig17_nonlocal": (fig_nonlocal, ["C9_nonlocal_trace"]),
        "fig18_coloc": (fig_coloc, ["C10_phase_coded"]),
        "fig19_alphathird": (fig_alphathird, ["C11_alpha_third"]),
        "fig20_band5000": (fig_band, ["C12_band_5000"]),
        "fig21_blind": (fig_blind, ["C13_blind_families"]),
        "fig22_anomaly": (fig_anomaly, ["C14_anomaly_hunt"]),
        "fig23_dirichlet": (fig_dirichlet, ["C15_dirichlet"]),
        "fig24_qinfo": (fig_qinfo, ["C16_qinfo"]),
        "fig25_map": (fig_map, ["C9_nonlocal_trace"]),
    }
    for theme in ("light",):
        t0 = figstyle.apply(theme)
        for lang in ("ru", "en"):
            T = {**t0, **V2[lang]}
            for stem, (fn, camps) in stems.items():
                fig = fn(T)
                save_all(fig, stem, langs=(lang,))
        copy_map = stems
        for stem, (fn, camps) in copy_map.items():
            copy_to_campaign(stem, camps)
    print("figures v2 done:", len(stems), "stems × 2 langs @ 600dpi")


if __name__ == "__main__":
    main()
