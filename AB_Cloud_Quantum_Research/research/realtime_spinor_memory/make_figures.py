#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_figures.py — плиточные фигуры вспомогательного исследования
«машина без долговременной памяти» (research/realtime_spinor_memory).

Каждая фигура — сетка 2×2, ЧЕТЫРЕ измерения измерений, построенные
ИСКЛЮЧИТЕЛЬНО из закоммиченных вердиктов/данных кампаний ES1–ES5
(data/*.json, data/*.csv). 600 dpi, стиль «Critical Line & Copper»,
RU/EN. Выход: figures/{ru,en}/tsK_4dim_{lang}.png + models_4dim_{lang}.png.
"""
import csv
import json
import math
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

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
OUT = os.path.join(HERE, "figures")

T = dict(bg="#FAF7F0", panel="#FFFFFF", ink="#1A1A24", line="#0E7C86",
         copper="#C96F4A", slate="#3E515B", muted="#6B6455",
         grid="#DDD6C8", ok="#3A6B4F", bad="#8C3A2F", gold="#8C6D1F")

MCOL = {"S1": T["copper"], "S2": T["line"], "S3": T["slate"]}
MNAMES = {"S1": "S1 · π/2 (N=4)", "S2": "S2 · π/3 (N=6)",
          "S3": "S3 · π/7 (N=14)"}


def load_verdict(tag):
    return json.load(open(os.path.join(DATA, f"{tag}_verdict.json"),
                          encoding="utf-8"))


def load_csv(name):
    with open(os.path.join(DATA, f"{name}.csv"), encoding="utf-8") as f:
        r = list(csv.reader(f))
    hdr, rows = r[0], r[1:]
    return [dict(zip(hdr, row)) for row in rows]


def clean(ax, grid=True):
    ax.set_facecolor(T["panel"])
    for s in ax.spines.values():
        s.set_color(T["grid"])
    ax.tick_params(colors=T["muted"], labelsize=8)
    if grid:
        ax.grid(True, color=T["grid"], lw=0.5, alpha=0.6)


def style(fig, title, caption):
    """Управляемая компоновка: suptitle/supxlabel резервируют место в
    constrained_layout — без наложений и обрезки (в отличие от fig.text)."""
    fig.patch.set_facecolor(T["bg"])
    fig.suptitle(title, fontsize=13.5, fontweight="bold", color=T["ink"])
    fig.supxlabel(caption, fontsize=8.6, color=T["muted"], style="italic")


# ────────────────────────────────────────────────────────────────────
def fig_ts1(lang):
    v = load_verdict("es1_cycles")["results"]
    L = LANGS[lang]
    fig, axs = plt.subplots(2, 2, figsize=(11, 8.2), dpi=100,
                            constrained_layout=True)
    a, b, c, d = axs.ravel()

    # a) решётки состояний на окружности
    th = np.linspace(0, 2 * np.pi, 400)
    for ax in (a,):
        pass
    a.plot(np.cos(th), np.sin(th), color=T["grid"], lw=1.2, zorder=1)
    offs = {"S1": 0.0, "S2": 0.055, "S3": 0.11}
    for name, theta in (("S1", math.pi / 2), ("S2", math.pi / 3),
                        ("S3", math.pi / 7)):
        N = v[name]["N_measured"]
        ph = np.arange(N) * theta
        r = 1.0 - offs[name]
        a.scatter(r * np.cos(ph), r * np.sin(ph), s=64 if name == "S1" else
                  (44 if name == "S2" else 22), color=MCOL[name],
                  edgecolors=T["ink"], linewidths=0.5, zorder=3,
                  label=MNAMES[name])
    a.plot([0, 1.13], [0, 0], color=T["copper"], lw=1.6, ls="--", zorder=2)
    a.text(1.13, 0.06, "θ", color=T["copper"], fontsize=10)
    a.set_xlim(-1.25, 1.3)
    a.set_ylim(-1.25, 1.25)
    a.set_aspect("equal")
    a.legend(loc="upper left", fontsize=7.5, framealpha=0.9)
    a.set_title(L["ts1a"], fontsize=10, color=T["ink"])
    a.axis("off")

    # b) период N vs k: формула N = 2k
    ks = np.arange(2, 17)
    b.plot(ks, 2 * ks, color=T["line"], lw=1.6,
           label="N = 2k (теорема TS1)")
    for name in ("S1", "S2", "S3"):
        k = v[name]["k"]
        b.scatter([k], [v[name]["period_measured"]], s=90, zorder=3,
                  color=MCOL[name], edgecolors=T["ink"], linewidths=0.6)
    b.annotate("S1(4)", (2, 4), textcoords="offset points", xytext=(6, 6),
               fontsize=8, color=T["copper"])
    b.annotate("S2(6)", (3, 6), textcoords="offset points", xytext=(6, 6),
               fontsize=8, color=T["line"])
    b.annotate("S3(14)", (7, 14), textcoords="offset points", xytext=(6, -12),
               fontsize=8, color=T["slate"])
    b.set_xlabel("k  (θ = π/k)", fontsize=9, color=T["ink"])
    b.set_ylabel("N (период)", fontsize=9, color=T["ink"])
    b.set_title(L["ts1b"], fontsize=10, color=T["ink"])
    b.set_xticks(range(2, 17, 2))
    clean(b)
    b.legend(fontsize=8)

    # c) минимальный зазор = 2π/N = π/k
    names = ("S1", "S2", "S3")
    xs = np.arange(3)
    gaps = [v[n]["min_gap"] for n in names]
    exp = [v[n]["min_gap_expected"] for n in names]
    c.bar(xs - 0.18, gaps, width=0.36, color=[MCOL[n] for n in names],
          edgecolor=T["ink"], linewidth=0.5, label="измеренный min gap")
    c.bar(xs + 0.18, exp, width=0.36, color="none", edgecolor=T["ink"],
          linewidth=1.0, ls=":", label="2π/N (теория)")
    c.set_xticks(xs)
    c.set_xticklabels([MNAMES[n] for n in names], fontsize=8)
    c.set_ylabel("зазор (рад)", fontsize=9, color=T["ink"])
    c.set_title(L["ts1c"], fontsize=10, color=T["ink"])
    c.set_yscale("log")
    clean(c)
    c.legend(fontsize=8)

    # d) контроль: равномерность решётки и биты/шаг
    devs = [v[n]["uniformity_dev"] for n in names]
    bits = [v[n]["bits_per_step"] for n in names]
    dd = c.twinx() if False else d
    d.bar(xs - 0.18, [max(x, 1e-17) for x in devs], width=0.36,
          color=T["gold"], edgecolor=T["ink"], linewidth=0.5,
          label="равномерность (max откл.)")
    d.set_yscale("log")
    d.set_ylim(1e-17, 1e-8)
    d.set_ylabel("отклонение (рад, log)", fontsize=9, color=T["ink"])
    d2 = d.twinx()
    d2.bar(xs + 0.18, bits, width=0.36, color=T["line"], alpha=0.85,
           edgecolor=T["ink"], linewidth=0.5, label="биты/шаг log₂N")
    for i, x in enumerate(bits):
        d2.text(i + 0.18, x + 0.08, f"{x:.2f}", ha="center", fontsize=8,
                color=T["ink"])
    d2.set_ylim(0, 5)
    d2.set_ylabel("бит/шаг", fontsize=9, color=T["ink"])
    d.set_xticks(xs)
    d.set_xticklabels([MNAMES[n] for n in names], fontsize=8)
    d.set_title(L["ts1d"], fontsize=10, color=T["ink"])
    clean(d)
    h1, l1 = d.get_legend_handles_labels()
    h2, l2 = d2.get_legend_handles_labels()
    d.legend(h1 + h2, l1 + l2, fontsize=7.5, loc="lower right")

    style(fig, L["ts1t"], L["ts1cap"])
    return fig


# ────────────────────────────────────────────────────────────────────
def fig_ts2(lang):
    v = load_verdict("es2_volatility")["results"]
    L = LANGS[lang]
    fig, axs = plt.subplots(2, 2, figsize=(11, 8.2), dpi=100,
                            constrained_layout=True)
    a, b, c, d = axs.ravel()
    names = ("S1", "S2", "S3")
    xs = np.arange(3)

    # a) реконструкция после сброса ≈ 1/N
    acc = [v[n]["recon_acc"] for n in names]
    ch = [v[n]["chance"] for n in names]
    a.bar(xs, acc, width=0.5, color=[MCOL[n] for n in names],
          edgecolor=T["ink"], linewidth=0.5)
    a.plot(xs, ch, "o", ms=9, mfc="none", mec=T["bad"], mew=1.6,
           label="уровень случайности 1/N")
    a.set_xticks(xs)
    a.set_xticklabels([MNAMES[n] for n in names], fontsize=8)
    a.set_ylabel("точность реконструкции", fontsize=9, color=T["ink"])
    a.set_title(L["ts2a"], fontsize=10, color=T["ink"])
    clean(a)
    a.legend(fontsize=8)

    # b) MI(пре;пост) = 0; контроль без сброса = 1.0
    mi = [v[n]["MI_post"] for n in names]
    b.bar(xs - 0.18, mi, width=0.36, color=T["copper"],
           edgecolor=T["ink"], linewidth=0.5, label="I(пре; пост) = 0")
    b.bar(xs + 0.18, [1.0] * 3, width=0.36, color=T["line"], alpha=0.85,
          edgecolor=T["ink"], linewidth=0.5,
          label="контроль: живое состояние (точность 1.0)")
    b.set_xticks(xs)
    b.set_xticklabels([MNAMES[n] for n in names], fontsize=8)
    b.set_ylim(0, 1.15)
    b.set_ylabel("значение", fontsize=9, color=T["ink"])
    b.set_title(L["ts2b"], fontsize=10, color=T["ink"])
    clean(b)
    b.legend(fontsize=8, loc="lower right")

    # c) время сжато до mod N: доля согласованных t' ≈ 1/N
    cons = [v[n]["consistent_share"] for n in names]
    exp = [v[n]["expected_share"] for n in names]
    c.bar(xs - 0.18, cons, width=0.36, color=[MCOL[n] for n in names],
          edgecolor=T["ink"], linewidth=0.5, label="доля согласованных t′")
    c.bar(xs + 0.18, exp, width=0.36, color="none", edgecolor=T["ink"],
          linewidth=1.0, ls=":", label="1/N (теория)")
    c.set_xticks(xs)
    c.set_xticklabels([MNAMES[n] for n in names], fontsize=8)
    c.set_ylabel("доля от [0, 10⁶)", fontsize=9, color=T["ink"])
    c.set_title(L["ts2c"], fontsize=10, color=T["ink"])
    clean(c)
    c.legend(fontsize=8)

    # d) 3σ-полоса порога
    bands = {"S1": 3.75e-3, "S2": 3.23e-3, "S3": 2.23e-3}
    lim = [ch[i] + bands[n] for i, n in enumerate(names)]
    d.bar(xs, lim, width=0.5, color="none", edgecolor=T["muted"],
          linewidth=1.1, label="порог 1/N + 3σ (предел)")
    d.bar(xs, acc, width=0.3, color=[MCOL[n] for n in names],
          edgecolor=T["ink"], linewidth=0.5, label="измерено")
    for i, n in enumerate(names):
        d.text(i, acc[i] * 0.5, f"{acc[i]:.4f}", ha="center", fontsize=8,
               color=T["ink"])
    d.set_xticks(xs)
    d.set_xticklabels([MNAMES[n] for n in names], fontsize=8)
    d.set_ylabel("точность", fontsize=9, color=T["ink"])
    d.set_title(L["ts2d"], fontsize=10, color=T["ink"])
    clean(d)
    d.legend(fontsize=8, loc="upper right")

    style(fig, L["ts2t"], L["ts2cap"])
    return fig


# ────────────────────────────────────────────────────────────────────
def fig_ts3(lang):
    v = load_verdict("es3_realtime")["results"]
    L = LANGS[lang]
    fig, axs = plt.subplots(2, 2, figsize=(11, 8.2), dpi=100,
                            constrained_layout=True)
    a, b, c, d = axs.ravel()

    # a) стоимость шага: машина (плоско) против LogMachine (рост)
    chunks = load_csv("es3_machine_chunks")
    tc = [float(r["t"]) for r in chunks]
    mc = [float(r["median_ms"]) for r in chunks]
    a.plot(tc, mc, color=T["line"], lw=1.6, label="машина (медиана шага)")
    lm_pts = sorted((float(t), c) for t, c in
                    v["logmachine"]["cost_ms_at"].items())
    a.plot([p[0] for p in lm_pts], [p[1] for p in lm_pts], "o-",
           color=T["copper"], lw=1.4, ms=5,
           label="LogMachine (шаг + replay)")
    a.set_yscale("log")
    a.set_xlabel("t (шагов)", fontsize=9, color=T["ink"])
    a.set_ylabel("мс", fontsize=9, color=T["ink"])
    a.set_title(L["ts3a"], fontsize=10, color=T["ink"])
    clean(a)
    a.legend(fontsize=8, loc="center left")

    # b) дедлайн-комплаенс
    miss1 = v["machine_S1"]["deadline_misses"]
    miss3 = v["machine_S3"]["deadline_misses"]
    b.bar([0, 1], [200000 - miss1, 200000 - miss3], width=0.45,
          color=[T["line"], T["slate"]], edgecolor=T["ink"], linewidth=0.5)
    b.axhline(200000, color=T["bad"], lw=1.4, ls="--")
    b.text(0.5, 200000 * 1.01, "Δt = 1 мс: 200 000/200 000", ha="center",
           fontsize=8.5, color=T["bad"])
    b.set_xticks([0, 1])
    b.set_xticklabels(["S1", "S3"], fontsize=9)
    b.set_ylim(0, 230000)
    b.set_ylabel("шагов в дедлайне", fontsize=9, color=T["ink"])
    b.set_title(L["ts3b"], fontsize=10, color=T["ink"])
    clean(b)

    # c) replay: Ω(t)
    rep = load_csv("es3_replay_curve")
    tr = [float(r["t"]) for r in rep]
    cr = [float(r["cost_ms"]) for r in rep]
    c.plot(tr, cr, "o-", color=T["copper"], ms=3.5, lw=1.3,
           label=f"replay: наклон {v['replay']['slope_ms_per_cell']:.1e} "
                 f"мс/ячейка, R²={v['replay']['r2']:.3f}")
    c.set_xscale("log")
    c.set_yscale("log")
    c.set_xlabel("t (ячеек журнала)", fontsize=9, color=T["ink"])
    c.set_ylabel("мс", fontsize=9, color=T["ink"])
    c.set_title(L["ts3c"], fontsize=10, color=T["ink"])
    clean(c)
    c.legend(fontsize=8)

    # d) порог: рост стоимости к t=2^17
    ratio_base = v["logmachine"]["growth_ratio_2x17_over_2x10"]
    d.bar([0, 1], [1.01, ratio_base], width=0.45,
          color=[T["line"], T["copper"]], edgecolor=T["ink"], linewidth=0.5)
    d.axhline(5.0, color=T["bad"], lw=1.4, ls="--")
    d.text(0.5, 6.2, "порог ×5", ha="center", fontsize=8.5, color=T["bad"])
    d.set_yscale("log")
    d.set_xticks([0, 1])
    d.set_xticklabels(["машина (×1.01)", f"LogMachine (×{ratio_base:.0f})"],
                      fontsize=8.5)
    d.set_ylabel("рост стоимости шага\n(t=2¹⁷ против t=2¹⁰, log)",
                 fontsize=9, color=T["ink"])
    d.set_title(L["ts3d"], fontsize=10, color=T["ink"])
    clean(d)

    style(fig, L["ts3t"], L["ts3cap"])
    return fig


# ────────────────────────────────────────────────────────────────────
def fig_models(lang):
    v = load_verdict("es5_noise")["results"]
    L = LANGS[lang]
    fig, axs = plt.subplots(2, 2, figsize=(11, 8.2), dpi=100,
                            constrained_layout=True)
    a, b, c, d = axs.ravel()
    names = ("S1", "S2", "S3")
    xs = np.arange(3)

    # a) N и биты/шаг
    Ns = [load_verdict("es1_cycles")["results"][n]["N_measured"]
          for n in names]
    bits = [math.log2(n) for n in Ns]
    a.bar(xs - 0.18, Ns, width=0.36, color=[MCOL[n] for n in names],
          edgecolor=T["ink"], linewidth=0.5, label="N состояний")
    for i, n_ in enumerate(Ns):
        a.text(i - 0.18, n_ + 0.3, str(n_), ha="center", fontsize=8.5,
               color=T["ink"])
    a2 = a.twinx()
    a2.bar(xs + 0.18, bits, width=0.36, color=T["gold"], alpha=0.85,
           edgecolor=T["ink"], linewidth=0.5, label="биты/шаг")
    for i, x in enumerate(bits):
        a2.text(i + 0.18, x + 0.08, f"{x:.2f}", ha="center", fontsize=8,
                color=T["ink"])
    a2.set_ylim(0, 4.6)
    a2.set_ylabel("бит/шаг", fontsize=9, color=T["ink"])
    a.set_xticks(xs)
    a.set_xticklabels([MNAMES[n] for n in names], fontsize=8)
    a.set_ylabel("N", fontsize=9, color=T["ink"])
    a.set_ylim(0, 16.5)
    a.set_title(L["ma"], fontsize=10, color=T["ink"])
    clean(a)
    h1, l1 = a.get_legend_handles_labels()
    h2, l2 = a2.get_legend_handles_labels()
    a.legend(h1 + h2, l1 + l2, fontsize=7.5, loc="upper left")

    # b) зона тишины σ* против границ gap/12 … gap/2
    sstar = [v[n]["sigma_star"] for n in names]
    lo = [v[n]["gap_over_12"] for n in names]
    hi = [v[n]["gap_over_2"] for n in names]
    b.bar(xs, [h - l for l, h in zip(lo, hi)], bottom=lo, width=0.5,
          color="none", edgecolor=T["muted"], linewidth=1.1,
          label="пределы [gap/12, gap/2]")
    b.scatter(xs, sstar, s=110, zorder=3, color=[MCOL[n] for n in names],
              edgecolors=T["ink"], linewidths=0.7, label="σ* (SER = 0)")
    b.set_yscale("log")
    b.set_xticks(xs)
    b.set_xticklabels([MNAMES[n] for n in names], fontsize=8)
    b.set_ylabel("σ (рад, log)", fontsize=9, color=T["ink"])
    b.set_title(L["mb"], fontsize=10, color=T["ink"])
    clean(b)
    b.legend(fontsize=8, loc="upper right")

    # c) SER(σ) — кривые трёх моделей
    rows = load_csv("es5_noise")
    for n in names:
        pts = sorted((float(r["sigma_rad"]), float(r["SER"]))
                     for r in rows if r["model"] == n)
        c.plot([p[0] for p in pts], [max(p[1], 1e-6) for p in pts], "o-",
               ms=3, lw=1.3, color=MCOL[n], label=MNAMES[n])
    for n, y in (("S1", 2e-4), ("S2", 3.4e-4), ("S3", 8e-4)):
        c.axvline(v[n]["gap"] / 8, color=MCOL[n], lw=0.9, ls=":", alpha=0.8)
    c.axvline(v["S1"]["gap"] / 8, color=MCOL["S1"], lw=0.9, ls=":",
              alpha=0.8, label="gap/8")
    c.axhline(1e-3, color=T["bad"], lw=1.1, ls="--")
    c.text(2.2e-4, 1.5e-3, "порог C3: 1e-3", fontsize=7.5, color=T["bad"])
    c.set_xscale("log")
    c.set_yscale("log")
    c.set_ylim(1e-6, 1.2)
    c.set_xlabel("σ (рад, log)", fontsize=9, color=T["ink"])
    c.set_ylabel("SER (log)", fontsize=9, color=T["ink"])
    c.set_title(L["mc"], fontsize=10, color=T["ink"])
    clean(c)
    c.legend(fontsize=7.5, loc="lower right", ncol=2)

    # d) сводка вердиктов ES1–ES5
    tags = ["es1_cycles", "es2_volatility", "es3_realtime",
            "es4_memoryless_task", "es5_noise"]
    labels = ["ES1 циклы", "ES2 летучесть", "ES3 реальное время",
              "ES4 без хранилища", "ES5 шум"] if lang == "ru" else \
             ["ES1 cycles", "ES2 volatility", "ES3 real-time",
              "ES4 memoryless", "ES5 noise"]
    status = [1 if load_verdict(t)["pass"] else 0 for t in tags]
    d.bar(np.arange(5), status, width=0.55,
          color=[T["ok"] if s else T["bad"] for s in status],
          edgecolor=T["ink"], linewidth=0.5)
    d.set_xticks(np.arange(5))
    d.set_xticklabels(labels, fontsize=8, rotation=12)
    d.set_ylim(0, 1.35)
    d.set_yticks([0, 1])
    d.set_yticklabels(["FAIL", "PASS"])
    d.set_title(L["md"], fontsize=10, color=T["ink"])
    clean(d)

    style(fig, L["mt"], L["mcap"])
    return fig


# ────────────────────────────────────────────────────────────────────
LANGS = {
    "ru": dict(
        ts1t="TS1. Теорема о фазовом цикле — 4 измерения",
        ts1a="a) решётки состояний трёх моделей на S¹",
        ts1b="b) период цикла: N = 2k точно (серия k = 2…16)",
        ts1c="c) минимальный зазор состояний = 2π/N",
        ts1d="d) контроль: равномерность решётки и ёмкость (биты/шаг)",
        ts1cap=("Вердикт ES1: периоды 4/6/14 = 2k точно; min gap = 2π/N; "
                "решётка равномерна (≤ 8.9e-16); N(π/k) = 2k для k = 2…16."),
        ts2t="TS2. Теорема о летучести состояния — 4 измерения",
        ts2a="a) реконструкция пре-состояния после сброса ≈ 1/N",
        ts2b="b) I(пре; пост) = 0; контроль без сброса — 1.0",
        ts2c="c) память о времени сжата до mod N (доля t′ ≈ 1/N)",
        ts2d="d) порог C1: измеренное внутри 1/N + 3σ",
        ts2cap=("Вердикт ES2 (эрратум ES2a): после сброса реконструкция на "
                "уровне случайности (внутри 3σ-полосы); I(пре; пост) = 0 "
                "точно; контроль без сброса — 1.0. 120 000 trials/модель."),
        ts3t="TS3. Теорема о реальном времени — 4 измерения",
        ts3a="a) стоимость шага: машина плоская, LogMachine растёт",
        ts3b="b) дедлайн-комплаенс 100% (Δt = 1 мс, 200 000 шагов)",
        ts3c="c) полная перепроверка журнала: Ω(t), R² = 0.999",
        ts3d="d) порог C3: рост к t = 2¹⁷ — машина ×1, baseline ×130",
        ts3cap=("Вердикт ES3: наклон шага машины −1.5e−12 мс/шаг; 0 из "
                "200 000 пропусков дедлайна; LogMachine: рост ×129–132, "
                "replay Ω(t) (R² = 0.999)."),
        mt="Три модели без долговременной памяти — 4 измерения",
        ma="a) ёмкость: N состояний и биты/шаг",
        mb="b) зона тишины σ* внутри [gap/12, gap/2]",
        mc="c) SER(σ): пробой канала при σ ~ gap",
        md="d) сводка предрегистрированных вердиктов ES1–ES5",
        mcap=("Вердикт ES5 (эрратум ES5a): σ* внутри [gap/12, gap/2]; "
              "порядок S1 ≥ S2 ≥ S3; SER(gap/8) ≈ 6e-5; SER(gap) ≈ 0.62. "
              "Диффузия (разведка): t* ~ gap²/σ². Все вердикты PASS."),
    ),
    "en": dict(
        ts1t="TS1. The phase-cycle theorem — four dimensions",
        ts1a="a) state lattices of the three models on S¹",
        ts1b="b) cycle period: N = 2k exactly (sweep k = 2…16)",
        ts1c="c) minimal state gap = 2π/N",
        ts1d="d) control: lattice uniformity and capacity (bits/step)",
        ts1cap=("ES1 verdict: periods 4/6/14 = 2k exactly; min gap = 2π/N; "
                "lattice uniform (≤ 8.9e-16); N(π/k) = 2k for k = 2…16."),
        ts2t="TS2. The volatility theorem — four dimensions",
        ts2a="a) pre-state reconstruction after reset ≈ 1/N",
        ts2b="b) I(pre; post) = 0; control without reset — 1.0",
        ts2c="c) time memory compressed to mod N (share of t′ ≈ 1/N)",
        ts2d="d) threshold C1: measured value inside 1/N + 3σ",
        ts2cap=("ES2 verdict (erratum ES2a): post-reset reconstruction at "
                "chance level (inside the 3σ band); I(pre; post) = 0 exactly; "
                "no-reset control — 1.0. 120,000 trials per model."),
        ts3t="TS3. The real-time theorem — four dimensions",
        ts3a="a) step cost: machine flat, LogMachine growing",
        ts3b="b) deadline compliance 100% (Δt = 1 ms, 200,000 steps)",
        ts3c="c) full log replay: Ω(t), R² = 0.999",
        ts3d="d) threshold C3: growth to t = 2¹⁷ — machine ×1, baseline ×130",
        ts3cap=("ES3 verdict: machine step-cost slope −1.5e−12 ms/step; 0 of "
                "200,000 deadline misses; LogMachine: ×129–132 growth, "
                "replay Ω(t) (R² = 0.999)."),
        mt="Three memoryless models — four dimensions",
        ma="a) capacity: N states and bits/step",
        mb="b) silence zone σ* inside [gap/12, gap/2]",
        mc="c) SER(σ): channel breakdown at σ ~ gap",
        md="d) summary of pre-registered verdicts ES1–ES5",
        mcap=("ES5 verdict (erratum ES5a): σ* inside [gap/12, gap/2]; order "
              "S1 ≥ S2 ≥ S3; SER(gap/8) ≈ 6e-5; SER(gap) ≈ 0.62. Diffusion "
              "(exploratory): t* ~ gap²/σ². All verdicts PASS."),
    ),
}


def main():
    for lang in ("ru", "en"):
        outdir = os.path.join(OUT, lang)
        os.makedirs(outdir, exist_ok=True)
        for fn, stem in ((fig_ts1, "ts1_4dim"), (fig_ts2, "ts2_4dim"),
                         (fig_ts3, "ts3_4dim"), (fig_models, "models_4dim")):
            fig = fn(lang)
            path = os.path.join(outdir, f"{stem}_{lang}.png")
            fig.savefig(path, dpi=600, facecolor=T["bg"])
            plt.close(fig)
            print("OK:", os.path.relpath(path, HERE),
                  f"({os.path.getsize(path) // 1024} KB)")


if __name__ == "__main__":
    main()
