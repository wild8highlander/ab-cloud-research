#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_tiled_figures.py — плиточные фигуры пакета AB Cloud Quantum Research.

Каждая фигура — сетка 2×2, ЧЕТЫРЕ разных измерения измерений одной теоремы
(Th1–Th6), построенные из ЗАКОММИЧЕННЫХ вердиктов кампаний
(modules/core_spectrum/data/v*_verdict.json). 600 dpi, стиль
«Critical Line & Copper», RU/EN. Фигуры кладутся в:
  figures_tiled/{ru,en}/thK_4dim_{lang}.png
  theorems_lemmas/T0K_*/figures/thK_4dim_{lang}.png
"""
import json
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.font_manager as fm

for _f in ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
           "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
           "/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf"):
    if os.path.exists(_f):
        fm.fontManager.addfont(_f)
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "modules", "core_spectrum", "data")
OUT_TILED = os.path.join(ROOT, "figures_tiled")
OUT_THM = os.path.join(ROOT, "theorems_lemmas")

T = dict(bg="#FAF7F0", panel="#FFFFFF", ink="#1A1A24", line="#0E7C86",
         copper="#C96F4A", slate="#3E515B", muted="#6B6455",
         grid="#DDD6C8", ok="#3A6B4F", bad="#8C3A2F", gold="#8C6D1F")

V = {n: json.load(open(os.path.join(DATA, f"v{n}_verdict.json")))
     for n in ("04", "07", "08", "09", "12", "15")}

LANG = {
    "ru": dict(
        th1=("Th1. Эрмитовость и вещественность спектра — 4 измерения",
             "a) ‖H−H†‖ по затворам (max, log)", "b) невязка вещественности спектра (log)",
             "c) спаривание λ ↔ −λ (max, log)", "d) остатки собственных пар (max, log)",
             "затвор L", "значение", "порог 1e−12",
             "Вердикт V4: Th1 доказана — эрмитовость по построению (пары сопряжённых связей), "
             "спектр вещественен, киральность α=½/W=0 — бипартидность."),
    th2=("Th2. Конечномерная самосопряжённость — 4 измерения",
         "a) дефектные индексы n+/n− по L", "b) min сингулярное число H−iI",
         "c) дрейф унитарности e^{−iHt} (log)", "d) сдвиги спектра при смене границ (L12/L24)",
         "затвор L", "значение", "порог: индексы = 0",
         "Вердикт V8: дефекты (0,0); ‖(H∓iI)ψ‖² = ‖Hψ‖²+‖ψ‖²; дрейф 2.2e−16; "
         "семейство границ устойчиво (сдвиги конечны, убывают с L)."),
    th3=("Th3. Сертификаты собственных значений — 4 измерения",
         "a) невязка δ по сертификатам (log)", "b) граница Каутского δ²/gap (log)",
         "c) ширина интервала hi−lo (log)", "d) покрытие Гершгорина спектра",
         "номер сертификата", "значение", "истинное λ внутри интервала",
         "Вердикт V12: 5/5 сертификатов валидны; интервалы гарантированные "
         "(рациональная арифметика), ширины ~1e−27 (mpmath dps 40)."),
    th4=("Th4. Спектральная формула коэффициентов Ли — 4 измерения",
         "a) λ_n при n = 1…3000 (log)", "b) согласование двух путей |Δ| (log)",
         "c) сертифицированный хвост (log)", "d) контроль: ранговая корреляция затворов",
         "n", "значение", "порог 1e−9",
         "Вердикт V15: λ_n = Tr g_n(H_ξ); два пути согласованы до 4.4e−11; "
         "λ_n > 0 для n ≤ 3000; контроль затворов −1.0 (вес живёт в H_ξ)."),
    th5=("Th5. Блочная редукция по симметрии — 4 измерения",
         "a) коммутаторы чистой решётки (log)", "b) ошибка объединения блоков (log)",
         "c) вихри: коммутаторы по твистам (симметрия сломана)", "d) вихри: среднее r по твистам",
         "твист (φx, φy)", "значение", "порог 1e−9",
         "Вердикт V9: тор без вихрей — спектр = объединение блоков характеров "
         "(7.1e−15); вихри ломают симметрию (ε ~ O(1)) — граница области действия."),
    th6=("Th6. Следовая формула Гуинанда–Вейля — 4 измерения",
         "a) арифметика констант B−C₀ и M0 (log)", "b) след H_ξ ↔ простые: r и невязка",
         "c) решёточные затворы: r_EF по затворам", "d) контраст: H_ξ против решётки",
         "затвор", "значение", "r = 1",
         "Вердикт V7: вес простых Λ(n)/√n доказательно живёт в тепловом следе H_ξ "
         "(r = 0.9996); в следах решёточных затворов гребёнка невидима (r̄ = 0.76)."),
    ylab_log="значение (log)",
    cls_zero="= 0 (точно)",
    thr="порог",
    hxi="след H_ξ",
    latt="решётка (контроль)",
    bmc0="B−C₀",
    m0="M0 (Q)",
    agree="согласование |Δ|",
    tail="хвост",
    rank="ранговая корр.",
    sigmap="σ_min(H−iI)",
    defects="дефектные индексы",
    nplus="n+",
    nminus="n−",
    openbc="открытые",
    torusbc="тор (3 твиста)",
),
    "en": dict(
        th1=("Th1. Hermiticity and the real spectrum — 4 dimensions",
             "a) ‖H−H†‖ by gates (max, log)", "b) spectrum-realness residual (log)",
             "c) pairing λ ↔ −λ (max, log)", "d) eigenpair residuals (max, log)",
             "gate L", "value", "threshold 1e−12",
             "V4 verdict: Th1 proven — hermiticity by construction (conjugate bond pairs), "
             "real spectrum, chirality α=½/W=0 via bipartiteness."),
    th2=("Th2. Finite-dimensional self-adjointness — 4 dimensions",
         "a) defect indices n+/n− by L", "b) smallest singular value of H−iI",
         "c) unitarity drift of e^{−iHt} (log)", "d) spectrum shifts under boundary change (L12/L24)",
         "gate L", "value", "threshold: indices = 0",
         "V8 verdict: defects (0,0); ‖(H∓iI)ψ‖² = ‖Hψ‖²+‖ψ‖²; drift 2.2e−16; "
         "the boundary family is stable (shifts finite, decay with L)."),
    th3=("Th3. Eigenvalue certificates — 4 dimensions",
         "a) residual δ per certificate (log)", "b) Kato bound δ²/gap (log)",
         "c) interval width hi−lo (log)", "d) Gershgorin coverage of the spectrum",
         "certificate no.", "value", "true λ inside the interval",
         "V12 verdict: 5/5 certificates valid; guaranteed (rational-arithmetic) "
         "intervals, widths ~1e−27 (mpmath dps 40)."),
    th4=("Th4. Spectral formula of the Li coefficients — 4 dimensions",
         "a) λ_n at n = 1…3000 (log)", "b) two-path agreement |Δ| (log)",
         "c) certified tail (log)", "d) control: gate rank correlation",
         "n", "value", "threshold 1e−9",
         "V15 verdict: λ_n = Tr g_n(H_ξ); two paths agree to 4.4e−11; "
         "λ_n > 0 for n ≤ 3000; gate control −1.0 (the weight lives in H_ξ)."),
    th5=("Th5. Block reduction by symmetry — 4 dimensions",
         "a) commutators of the clean lattice (log)", "b) block-union error (log)",
         "c) vortices: commutators by twist (symmetry broken)", "d) vortices: mean r by twist",
         "twist (φx, φy)", "value", "threshold 1e−9",
         "V9 verdict: vortex-free torus — spectrum = union of character blocks "
         "(7.1e−15); vortices break the symmetry (ε ~ O(1)) — scope boundary."),
    th6=("Th6. Guinand–Weil trace formula — 4 dimensions",
         "a) constants arithmetic B−C₀ and M0 (log)", "b) H_ξ trace ↔ primes: r and residual",
         "c) lattice gates: r_EF per gate", "d) contrast: H_ξ vs the lattice",
         "gate", "value", "r = 1",
         "V7 verdict: the prime weight Λ(n)/√n provably lives in the heat trace of H_ξ "
         "(r = 0.9996); the lattice-gate traces show no comb (r̄ = 0.76)."),
    ylab_log="value (log)",
    cls_zero="= 0 (exact)",
    thr="threshold",
    hxi="H_ξ trace",
    latt="lattice (control)",
    bmc0="B−C₀",
    m0="M0 (Q)",
    agree="agreement |Δ|",
    tail="tail",
    rank="rank corr.",
    sigmap="σ_min(H−iI)",
    defects="defect indices",
    nplus="n+",
    nminus="n−",
    openbc="open",
    torusbc="torus (3 twists)",
    ),
}


def _style_ax(ax, title, xlabel, ylabel, lang_pack):
    ax.set_title(title, fontsize=9.5, color=T["ink"], pad=6)
    ax.set_xlabel(xlabel, fontsize=8.5, color=T["muted"])
    ax.set_ylabel(ylabel, fontsize=8.5, color=T["muted"])
    ax.grid(True, alpha=0.35, color=T["grid"], lw=0.6)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.tick_params(labelsize=8, colors=T["slate"])


def _log_bar(ax, xs, ys, color, hatch=None):
    floor = 1e-18
    vals = [max(y, floor) if (y is not None and np.isfinite(y)) else floor
            for y in ys]
    ax.bar(xs, vals, color=color, width=0.6, edgecolor=T["ink"], lw=0.4,
           hatch=hatch)
    ax.set_yscale("log")
    for x, y, v in zip(xs, ys, vals):
        if y is not None and np.isfinite(y) and y < floor:
            ax.text(x, floor * 1.6, LANG_CUR["cls_zero"], ha="center",
                    fontsize=6.5, color=T["ok"], rotation=90)


def _save(fig, thm_no, lang):
    for out_root in (OUT_TILED, OUT_THM):
        d = (os.path.join(out_root, lang) if out_root == OUT_TILED else
             os.path.join(out_root, THM_DIRS[thm_no], "figures"))
        os.makedirs(d, exist_ok=True)
        fig.savefig(os.path.join(d, f"th{thm_no}_4dim_{lang}.png"), dpi=600)
    plt.close(fig)


def _frame(fig, suptitle, verdict_line, lang_pack):
    fig.patch.set_facecolor(T["bg"])
    fig.suptitle(suptitle, fontsize=12.5, color=T["ink"], fontweight="bold")
    fig.supxlabel(verdict_line, fontsize=7.8, color=T["slate"],
                  style="italic")


LANG_CUR = None


def fig_th1(lang):
    L = LANG_CUR
    e = V["04"]["entries"]
    xs = [f"L={r['L']}" for r in e]
    fig, axs = plt.subplots(2, 2, figsize=(11.0, 7.6),
                            constrained_layout=True)
    _frame(fig, L["th1"][0], L["th1"][8], L)
    t = V["04"]["epsilon_num"]
    a, b, c, d = axs[0][0], axs[0][1], axs[1][0], axs[1][1]
    _log_bar(a, xs, [r["hermiticity_max"] for r in e], T["copper"])
    a.axhline(t, color=T["bad"], ls="--", lw=1.0)
    _style_ax(a, L["th1"][1], L["th1"][5], L["th1"][6], L)
    _log_bar(b, xs, [r["imag_spectrum_max"] for r in e], T["line"])
    b.axhline(t, color=T["bad"], ls="--", lw=1.0)
    _style_ax(b, L["th1"][2], L["th1"][5], L["th1"][6], L)
    _log_bar(c, xs, [r["chiral_pair_max"] for r in e], T["gold"])
    c.axhline(t, color=T["bad"], ls="--", lw=1.0)
    _style_ax(c, L["th1"][3], L["th1"][5], L["th1"][6], L)
    _log_bar(d, xs, [r.get("eigpair_resid_max", None) for r in e], T["slate"])
    d.axhline(t, color=T["bad"], ls="--", lw=1.0)
    d.text(0.02, 0.86, f"{L['thr']}: {t:.0e}", transform=d.transAxes,
           fontsize=7.5, color=T["bad"])
    _style_ax(d, L["th1"][4], L["th1"][5], L["th1"][6], L)
    _save(fig, 1, lang)


def fig_th2(lang):
    L = LANG_CUR
    di = V["08"]["defect_indices"]
    xs = [f"L={r['L']}" for r in di]
    fig, axs = plt.subplots(2, 2, figsize=(11.0, 7.6),
                            constrained_layout=True)
    _frame(fig, L["th2"][0], L["th2"][8], L)
    a, b, c, d = axs[0][0], axs[0][1], axs[1][0], axs[1][1]
    w = 0.38
    a.bar(np.arange(len(di)) - w / 2, [r["n_plus"] for r in di], w,
          color=T["copper"], edgecolor=T["ink"], lw=0.4, label=L["nplus"])
    a.bar(np.arange(len(di)) + w / 2, [r["n_minus"] for r in di], w,
          color=T["line"], edgecolor=T["ink"], lw=0.4, label=L["nminus"])
    a.set_xticks(np.arange(len(di)))
    a.set_xticklabels(xs)
    a.legend(fontsize=7.5, frameon=False)
    _style_ax(a, L["th2"][1], L["th2"][5], L["th2"][6], L)
    sm = [0.5 * (r["sigma_min_plus"] + r["sigma_min_minus"]) for r in di]
    b.bar(xs, sm, color=T["gold"], width=0.6, edgecolor=T["ink"], lw=0.4)
    for x, y in zip(xs, sm):
        b.text(x, y + 0.015, f"{y:.3f}", ha="center", fontsize=7.5,
               color=T["slate"])
    _style_ax(b, L["th2"][2], L["th2"][5], L["sigmap"], L)
    u = V["08"]["unitarity"]
    c.bar(["e^{−iHt}"], [max(u["unitarity_drift_max"], 1e-18)], color=T["line"],
          width=0.35, edgecolor=T["ink"], lw=0.4)
    c.bar(["Im⟨ψ,Hψ⟩"], [max(u["imag_form"], 1e-18)], color=T["copper"],
          width=0.35, edgecolor=T["ink"], lw=0.4)
    c.set_yscale("log")
    c.axhline(1e-12, color=T["bad"], ls="--", lw=1.0)
    _style_ax(c, L["th2"][3], "", L["ylab_log"], L)
    s12 = V["08"]["bc_shifts_L12"]
    s24 = V["08"]["bc_shifts_L24"]
    keys = list(s12.keys())
    xpos = np.arange(len(keys))
    d.bar(xpos - w / 2, [s12[k] for k in keys], w, color=T["slate"],
          edgecolor=T["ink"], lw=0.4, label="L=12")
    d.bar(xpos + w / 2, [s24[k] for k in keys], w, color=T["copper"],
          edgecolor=T["ink"], lw=0.4, label="L=24")
    labels = [L["openbc"] if "open" in k else L["torusbc"] for k in keys]
    d.set_xticks(xpos)
    d.set_xticklabels([f"{labels[i]}\n{k.split('|')[1]}" for i, k in
                       enumerate(keys)], fontsize=6.5)
    d.legend(fontsize=7.5, frameon=False)
    _style_ax(d, L["th2"][4], "", "Δλ", L)
    _save(fig, 2, lang)


def fig_th3(lang):
    L = LANG_CUR
    certs = V["12"]["certificates"]
    xs = [str(r["index"]) for r in certs]
    fig, axs = plt.subplots(2, 2, figsize=(11.0, 7.6),
                            constrained_layout=True)
    _frame(fig, L["th3"][0], L["th3"][8], L)
    a, b, c, d = axs[0][0], axs[0][1], axs[1][0], axs[1][1]
    _log_bar(a, xs, [r["delta"] for r in certs], T["line"])
    _style_ax(a, L["th3"][1], L["th3"][5], L["ylab_log"], L)
    _log_bar(b, xs, [r["delta"] ** 2 / r["gap"] for r in certs], T["copper"])
    _style_ax(b, L["th3"][2], L["th3"][5], L["ylab_log"], L)
    widths = [r["hi"] - r["lo"] for r in certs]
    _log_bar(c, xs, widths, T["gold"])
    _style_ax(c, L["th3"][3], L["th3"][5], L["ylab_log"], L)
    g = V["12"]["gershgorin"]
    lam = [r["lam_tilde"] for r in certs]
    d.axhspan(g["lo"], g["hi"], color=T["line"], alpha=0.18)
    d.plot(range(len(lam)), lam, "o", color=T["copper"], ms=6,
           mec=T["ink"], mew=0.5)
    d.axhline(g["lo"], color=T["slate"], lw=1.0)
    d.axhline(g["hi"], color=T["slate"], lw=1.0)
    d.text(0.02, 0.06, f"Gershgorin: [{g['lo']:.3f}, {g['hi']:.3f}] · "
           f"{g['n_intervals']} int.", transform=d.transAxes, fontsize=7.5,
           color=T["slate"])
    _style_ax(d, L["th3"][4], L["th3"][5], "λ̃", L)
    _save(fig, 3, lang)


def fig_th4(lang):
    L = LANG_CUR
    v = V["15"]
    fig, axs = plt.subplots(2, 2, figsize=(11.0, 7.6),
                            constrained_layout=True)
    _frame(fig, L["th4"][0], L["th4"][8], L)
    a, b, c, d = axs[0][0], axs[0][1], axs[1][0], axs[1][1]
    ns = [1, 100, 1000, 3000]
    lams = [v[f"lambda_{n}"] for n in ns]
    a.bar([str(n) for n in ns], lams, color=T["copper"], width=0.6,
          edgecolor=T["ink"], lw=0.4)
    a.set_yscale("log")
    a.axhline(v["lambda_min"], color=T["ok"], ls=":", lw=1.2)
    a.text(0.02, 0.9, f"λ_min = {v['lambda_min']:.4f} > 0",
           transform=a.transAxes, fontsize=8, color=T["ok"])
    _style_ax(a, L["th4"][1], L["th4"][5], "λ_n", L)
    _log_bar(b, ["|Δ|"], [v["Th4_max_abs_diff"]], T["line"])
    b.axhline(1e-9, color=T["bad"], ls="--", lw=1.0)
    b.text(0.02, 0.86, f"{L['thr']}: 1e−9", transform=b.transAxes,
           fontsize=7.5, color=T["bad"])
    _style_ax(b, L["th4"][2], "", L["ylab_log"], L)
    _log_bar(c, [L["tail"]], [v["tail_bound_max"]], T["gold"])
    c.text(0.02, 0.86, f"n_zeros = {v['n_zeros_used']:,} · "
           f"T_eff = {v['T_eff']:.0f}", transform=c.transAxes, fontsize=7.5,
           color=T["slate"])
    _style_ax(c, L["th4"][3], "", L["ylab_log"], L)
    d.bar([L["hxi"], L["latt"]], [0.9996, -1.0], color=[T["copper"],
          T["muted"]], width=0.5, edgecolor=T["ink"], lw=0.4)
    d.axhline(0, color=T["ink"], lw=0.8)
    d.set_ylim(-1.35, 1.15)
    for x, y in zip([L["hxi"], L["latt"]], [0.9996, -1.0]):
        d.text(x, y + (0.06 if y > 0 else -0.14), f"{y:.4f}", ha="center",
               fontsize=7.5, color=T["slate"])
    _style_ax(d, L["th4"][4], "", L["rank"], L)
    _save(fig, 4, lang)


def fig_th5(lang):
    L = LANG_CUR
    pa = V["09"]["part_A"]
    pb = V["09"]["part_B"]["rows"]
    fig, axs = plt.subplots(2, 2, figsize=(11.0, 7.6),
                            constrained_layout=True)
    _frame(fig, L["th5"][0], L["th5"][8], L)
    a, b, c, d = axs[0][0], axs[0][1], axs[1][0], axs[1][1]
    keys = ["eps_Ux", "eps_Uy", "eps_AB", "offdiag_max", "block_union_err"]
    vals = [max(pa.get(k, 1e-18), 1e-18) for k in keys]
    a.bar(range(len(keys)), vals, color=T["line"], width=0.6,
          edgecolor=T["ink"], lw=0.4)
    a.set_yscale("log")
    a.axhline(1e-9, color=T["bad"], ls="--", lw=1.0)
    a.set_xticks(range(len(keys)))
    a.set_xticklabels([k.replace("eps_", "ε").replace("_", " ") for k in keys],
                      fontsize=7)
    _style_ax(a, L["th5"][1], "", L["ylab_log"], L)
    _log_bar(b, ["∪ blocks"], [max(pa["block_union_err"], 1e-18)], T["copper"])
    b.axhline(1e-9, color=T["bad"], ls="--", lw=1.0)
    b.text(0.02, 0.86, f"{L['thr']}: 1e−9", transform=b.transAxes,
           fontsize=7.5, color=T["bad"])
    _style_ax(b, L["th5"][2], "", L["ylab_log"], L)
    tw = [f"({r['twist'][0]:.0f},{r['twist'][1]:.0f})" for r in pb]
    w = 0.38
    c.bar(np.arange(len(pb)) - w / 2, [r["eps_Ux"] for r in pb], w,
          color=T["slate"], edgecolor=T["ink"], lw=0.4, label="ε_Ux")
    c.bar(np.arange(len(pb)) + w / 2, [r["eps_Uy"] for r in pb], w,
          color=T["gold"], edgecolor=T["ink"], lw=0.4, label="ε_Uy")
    c.set_xticks(np.arange(len(pb)))
    c.set_xticklabels(tw)
    c.legend(fontsize=7.5, frameon=False)
    _style_ax(c, L["th5"][3], L["th5"][5], "ε", L)
    d.bar(tw, [r["r_mean"] for r in pb], color=T["muted"], width=0.6,
          edgecolor=T["ink"], lw=0.4)
    _style_ax(d, L["th5"][4], L["th5"][5], "r_mean", L)
    _save(fig, 5, lang)


def fig_th6(lang):
    L = LANG_CUR
    v = V["07"]
    ver = v["verify"]
    fig, axs = plt.subplots(2, 2, figsize=(11.0, 7.6),
                            constrained_layout=True)
    _frame(fig, L["th6"][0], L["th6"][8], L)
    a, b, c, d = axs[0][0], axs[0][1], axs[1][0], axs[1][1]
    keys = [L["bmc0"], L["m0"]]
    vals = [max(abs(ver["B_minus_C0"]), 1e-18),
            max(ver["M0_max_abs_diff_Q"], 1e-18)]
    a.bar(keys, vals, color=[T["copper"], T["line"]], width=0.5,
          edgecolor=T["ink"], lw=0.4)
    a.set_yscale("log")
    for x, y in zip(keys, vals):
        a.text(x, y * 1.25, f"{y:.2e}", ha="center", fontsize=7.5,
               color=T["slate"])
    _style_ax(a, L["th6"][1], "", L["ylab_log"], L)
    b.bar([L["hxi"]], [v["PC0_Hxi_r"]], color=T["copper"], width=0.4,
          edgecolor=T["ink"], lw=0.4)
    b.set_ylim(0.9, 1.02)
    b.axhline(1.0, color=T["ok"], ls=":", lw=1.2)
    b.text(0.02, 0.06, f"r = {v['PC0_Hxi_r']:.4f} · resid = "
           f"{v['PC0_resid_rel']:.4f}", transform=b.transAxes, fontsize=7.5,
           color=T["slate"])
    _style_ax(b, L["th6"][2], "", "r", L)
    gates = v["gates"]
    gxs = [f"G{i+1}" for i in range(len(gates))]
    c.bar(gxs, [g["r_EF"] for g in gates], color=T["line"], width=0.6,
          edgecolor=T["ink"], lw=0.4)
    c.axhline(v["gates_rEF_mean"], color=T["bad"], ls="--", lw=1.0)
    c.text(0.02, 0.9, f"mean = {v['gates_rEF_mean']:.3f}",
           transform=c.transAxes, fontsize=7.5, color=T["bad"])
    _style_ax(c, L["th6"][3], L["th6"][5], "r_EF", L)
    d.bar([L["hxi"], L["latt"]], [v["PC0_Hxi_r"], v["gates_rEF_mean"]],
          color=[T["copper"], T["muted"]], width=0.5, edgecolor=T["ink"],
          lw=0.4)
    d.set_ylim(0.0, 1.1)
    for x, y in zip([L["hxi"], L["latt"]],
                    [v["PC0_Hxi_r"], v["gates_rEF_mean"]]):
        d.text(x, y + 0.02, f"{y:.4f}", ha="center", fontsize=7.5,
               color=T["slate"])
    _style_ax(d, L["th6"][4], "", "r", L)
    _save(fig, 6, lang)


FIGS = {"th1": fig_th1, "th2": fig_th2, "th3": fig_th3,
        "th4": fig_th4, "th5": fig_th5, "th6": fig_th6}

THM_DIRS = {
    1: "T01_hermiticity", 2: "T02_self_adjointness",
    3: "T03_certificates", 4: "T04_li_spectral",
    5: "T05_block_reduction", 6: "T06_trace_formula"}


def main():
    global LANG_CUR
    for lang in ("ru", "en"):
        print(f"[{lang}]")
        for name, fn in FIGS.items():
            LANG_CUR = dict(LANG["ru"], **LANG[lang]) if lang == "en" \
                else LANG["ru"]
            fn(lang)
            print("  ", name, "ok")
    n = 6 * 2
    print(f"Готово: {n} плиточных фигур @600 dpi → figures_tiled/ + "
          f"theorems_lemmas/T0K_*/figures/")


if __name__ == "__main__":
    main()
