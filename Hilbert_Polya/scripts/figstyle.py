# -*- coding: utf-8 -*-
"""figstyle.py — визуальная идентичность «Hilbert Polya Bridge».

Палитра «Critical Line & Copper»: одна линия критической полосы (teal) как
единственный акцент, медь для нулей, сланец для затворов; две темы (light —
для печати, dark — для экранов), два языка (ru/en). Все рисунки проекта
проходят через этот модуль — набор остаётся визуально когерентным.

Правила:
  * constrained_layout всегда; никакого tight_layout/subplots_adjust;
  * сетка не громче alpha 0.12; без мусора на осях;
  * акцент отмечает ГЛАВНОЕ место рисунка (критическая линия, нуль,
    положительный контроль), никогда — украшение.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.font_manager as fm  # noqa: E402

for _p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
           "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"):
    try:
        fm.fontManager.addfont(_p)
    except Exception:
        pass

import matplotlib.pyplot as plt  # noqa: E402

plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

TOKENS = {
    "light": {
        "bg": "#FAF7F0", "panel": "#FFFFFF", "ink": "#1A1A24",
        "line": "#0E7C86",     # критическая линия (teal)
        "copper": "#C96F4A",   # нули ζ
        "slate": "#3E515B",    # затворы/оператор
        "muted": "#6B6455", "grid": "#DDD6C8",
        "ok": "#3A6B4F", "bad": "#8C3A2F", "gold": "#8C6D1F",
    },
    "dark": {
        "bg": "#10101A", "panel": "#171724", "ink": "#E8E2D0",
        "line": "#4FB3BE", "copper": "#E08B66", "slate": "#8FA8B5",
        "muted": "#8A8574", "grid": "#2A2A3A",
        "ok": "#7FBF9A", "bad": "#D97B6C", "gold": "#C9A84C",
    },
}

LANG = {
    "en": {
        "zid_title": "Identity function Z(t) = e^{iθ(t)}ζ(½+it) on the line",
        "zid_y": "Z(t)", "zid_x": "height t",
        "zeros": "zeros of Z_id (bisection)", "grams": "Gram points",
        "ladder_title": "Γ-ladder: three elementary closures",
        "ladder1": "|Γ(½+iu)|² = π/cosh πu",
        "ladder2": "|Γ(iu)|² = π/(u·sinh πu)",
        "ladder3": "|Γ(¼+iu)|·|Γ(¾+iu)| = π√2/√cosh 2πu",
        "residual": "relative residual",
        "u": "u",
        "arg_title": "Argument principle: N(T) and S(T) up to T = 1000",
        "N_y": "N(T) (strip count)", "S_y": "S(T) residual",
        "T_x": "height T",
        "anchors": "anchors N = n_line",
        "gap_title": "Nearest-neighbour zero gaps below T = 1000",
        "gap_y": "gap γ_{n+1} − γ_n", "gap_mean": "mean gap 1.521",
        "trace_title": "Trace formula: Tr e^{−xH_ξ} vs explicit formula",
        "K_direct": "direct sum Σ e^{−xγ}",
        "K_formula": "explicit formula (1/π)∫Q sin",
        "x_ax": "x (heat-kernel time)",
        "parts_title": "Decomposition: the weight of primes in K(x)",
        "part_T1": "T1 Γ-part", "part_T2": "T2 prime part Λ(n)/√n",
        "part_T3": "T3 smooth part",
        "rEF_title": "Heat-trace projection r_EF: gates vs nulls",
        "rEF_y": "r_EF (fixed scale)",
        "PC0": "PC0 zeros window (+0.9998)",
        "null_band": "surrogate null 0.00±0.39",
        "coloc_title": "Prime flow kernel: response vs distance d",
        "coloc_y": "kernel δ(d)", "d_ax": "distance d (flow cells)",
        "psi_title": "ψ(x): sieve vs first 200 zeros (corr = 0.972)",
        "psi_y": "ψ(x)", "x_psi": "x",
        "sieve": "von Mangoldt sieve", "zeta": "ψ via 200 zeros",
        "dyn_title": "Wave-packet dynamics on L = 96",
        "mx_y": "⟨x⟩(t)", "t_ax": "time t",
        "clean": "clean lattice", "z16": "ζ-cloud Nv=16",
        "z64": "Nv=64", "z256": "Nv=256", "r256": "random Nv=256",
        "ladder_title2": "Statistics ladder ⟨r⟩ by channel",
        "ladder_y": "⟨r⟩", "channel": "channel",
        "poi": "Poisson 0.386", "goe": "GOE 0.531", "gue": "GUE 0.602",
        "ext_title": "Extended gate family: |r_H7| by handle",
        "ext_y": "|r_H7|", "c3_best": "C3 best 0.226",
        "pc_line": "positive controls 1.000",
        "theme": "theme",
    },
    "ru": {
        "zid_title": "Функция тождеств Z(t) = e^{iθ(t)}ζ(½+it) на линии",
        "zid_y": "Z(t)", "zid_x": "высота t",
        "zeros": "нули Z_id (бисекция)", "grams": "точки Грама",
        "ladder_title": "Γ-лестница: три элементарных замыкания",
        "ladder1": "|Γ(½+iu)|² = π/cosh πu",
        "ladder2": "|Γ(iu)|² = π/(u·sinh πu)",
        "ladder3": "|Γ(¼+iu)|·|Γ(¾+iu)| = π√2/√cosh 2πu",
        "residual": "относительная невязка",
        "u": "u",
        "arg_title": "Аргументный принцип: N(T) и S(T) до T = 1000",
        "N_y": "N(T) (счёт по полосе)", "S_y": "остаток S(T)",
        "T_x": "высота T",
        "anchors": "якоря N = n_линия",
        "gap_title": "Соседние зазоры нулей ниже T = 1000",
        "gap_y": "зазор γ_{n+1} − γ_n", "gap_mean": "средний зазор 1.521",
        "trace_title": "Следовая формула: Tr e^{−xH_ξ} против явной формулы",
        "K_direct": "прямая сумма Σ e^{−xγ}",
        "K_formula": "явная формула (1/π)∫Q sin",
        "x_ax": "x (время теплового ядра)",
        "parts_title": "Раскладка: вес простых в K(x)",
        "part_T1": "T1 Γ-часть", "part_T2": "T2 простая часть Λ(n)/√n",
        "part_T3": "T3 гладкая часть",
        "rEF_title": "Тепловая проекция r_EF: затворы против нулей",
        "rEF_y": "r_EF (фикс. масштаб)",
        "PC0": "PC0 окно нулей (+0.9998)",
        "null_band": "суррогатный нуль 0.00±0.39",
        "coloc_title": "Ядро потока простых: отклик против расстояния d",
        "coloc_y": "ядро δ(d)", "d_ax": "расстояние d (ячейки потока)",
        "psi_title": "ψ(x): сито против первых 200 нулей (corr = 0.972)",
        "psi_y": "ψ(x)", "x_psi": "x",
        "sieve": "сито фон Мангольдта", "zeta": "ψ по 200 нулям",
        "dyn_title": "Динамика волнового пакета на L = 96",
        "mx_y": "⟨x⟩(t)", "t_ax": "время t",
        "clean": "чистая решётка", "z16": "ζ-облако Nv=16",
        "z64": "Nv=64", "z256": "Nv=256", "r256": "случайные Nv=256",
        "ladder_title2": "Лестница статистик ⟨r⟩ по каналам",
        "ladder_y": "⟨r⟩", "channel": "канал",
        "poi": "Пуассон 0.386", "goe": "GOE 0.531", "gue": "GUE 0.602",
        "ext_title": "Расширенное семейство: |r_H7| по ручкам",
        "ext_y": "|r_H7|", "c3_best": "лучший C3 0.226",
        "pc_line": "позитивные контроли 1.000",
        "theme": "тема",
    },
}


def apply(theme="light"):
    t = TOKENS[theme]
    plt.rcParams.update({
        "figure.facecolor": t["bg"], "axes.facecolor": t["panel"],
        "savefig.facecolor": t["bg"],
        "axes.edgecolor": t["grid"], "axes.labelcolor": t["ink"],
        "xtick.color": t["muted"], "ytick.color": t["muted"],
        "text.color": t["ink"], "axes.titlecolor": t["ink"],
        "axes.titlesize": 13, "axes.titleweight": "bold",
        "axes.labelsize": 10.5, "xtick.labelsize": 9, "ytick.labelsize": 9,
        "legend.frameon": False, "legend.fontsize": 9,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.grid": False,
    })
    return t


def clean_axis(ax, grid=True):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    if grid:
        ax.yaxis.grid(True, alpha=0.12, color=TOKENS["light"]["grid"])
        ax.set_axisbelow(True)


def save_all(fig, stem, out_root, langs=("ru", "en"),
             hires_dpi=600, screen_dpi=160):
    """Сохраняет рисунок во все целевые директории проекта.

    figures_hires/{lang}/{stem}.png        — 600 dpi (публикация);
    computations/… не трогает (копирует вызывающий скрипт при нужде).
    Возвращает список путей.
    """
    import os
    paths = []
    for lang in langs:
        d = os.path.join(out_root, "figures_hires", lang)
        os.makedirs(d, exist_ok=True)
        p = os.path.join(d, f"{stem}_{lang}.png")
        fig.savefig(p, dpi=hires_dpi)
        paths.append(p)
    return paths
