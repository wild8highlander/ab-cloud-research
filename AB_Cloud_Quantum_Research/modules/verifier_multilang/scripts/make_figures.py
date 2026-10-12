#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_figures.py — рисунки серии ABQP Julia Research Program v0.3.0.
Стиль «Critical Line & Copper», 12 фигур × {ru,en} @ 600 dpi.
"""
import csv
import json
import os

import matplotlib
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np

for _f in ('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
           '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'):
    try:
        fm.fontManager.addfont(_f)
    except Exception:
        pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(ROOT, "results")

TOKENS = dict(bg='#FAF7F0', panel='#FFFFFF', ink='#1A1A24', line='#0E7C86',
              copper='#C96F4A', slate='#3E515B', muted='#6B6455',
              grid='#DDD6C8', ok='#3A6B4F', bad='#8C3A2F', gold='#8C6D1F')

LANG = {
    'ru': dict(
        f1=('E02: компиляция Haar-унитарий (Givens + фазы)',
            'log$_{10}$(1−F) по выборке', 'число матриц'),
        f2=('E03: масштабирование стоимости компиляции',
            'время компиляции, с (log)', 'размерность d (log)'),
        f3=('E05: чувствительность к фазовому шуму',
            'p95(1−F)', 'σ$_φ$, рад'),
        f4=('E07: код повторения против контролей',
            'частота ошибок', 'p (бит-флип на такт)'),
        f5=('E11: слепое чтение нулей ζ с критической прямой',
            '|ζ(½+it)| и развёрнутый arg ζ', 't'),
        f6=('E12: интерферометр Маха–Зендера',
            'P(выход 1)', 'φ, рад'),
        f7=('E14: CHSH — квантовая модель против LHV',
            'величина S', 'вариант расчёта'),
        f8=('E15: три механизма устойчивости — различающая сигнатура',
            'эффект (log)', 'механизм'),
        legend_1mF='1−F', legend_p95='p95', legend_median='медиана',
        legend_uncoded='без кода', legend_logical='код (3 повторения)',
        legend_corr='контроль: коррелированные ошибки',
        legend_abszeta='|ζ(½+it)|', legend_arg='arg ζ (развёрнутый)',
        legend_det='найденные нули (слепо)',
        legend_S_an='S аналит. (2√2)', legend_S_sm='S Монте-Карло (10⁶)',
        legend_lhv='max LHV (=2)', legend_local='локальный предел (=2)',
        legend_M1='M1: общая локальная унитарная',
        legend_M2='M2: асимметричная фаза',
        legend_M3f='M3: AB-поток, полный квант',
        legend_M3h='M3: AB-поток, полуквант',
        legend_abl='абляция (φ≡0)', legend_lin='контроль: линейная фаза',
        x_S_var=['аналит.', 'МК 10⁶', 'LHV max'],
        f9=('E17: слепое чтение 649 нулей ζ до высоты T = 1000',
            '|ζ(½+it)| и развёрнутый arg ζ', 't'),
        f10=('E16: стоимость ζ(½+it) при равной точности: ЭМ против Римана–Зигеля',
            'медиана времени оценки, мс (log)', 'высота t (log)'),
        f11=('E17: точность 649 нулей против эталона mpmath.zetazero',
            '|Δγ|, рад (log)', 'номер нуля n'),
        f12=('E17: полнота — накопленное число нулей и N(T) по стандартному пути',
            'число нулей ниже γ', 'высота γ'),
        legend_em='движок A: Эйлер–Маклорен (слепо)',
        legend_rs='движок B: Риман–Зигель (слепо)',
        legend_thr='порог 1e−9',
        legend_cum_em='найдено движком A',
        legend_cum_rs='найдено движком B',
        legend_N_ref='mpmath.zetazero (эталон)',
        legend_EM='Эйлер–Маклорен',
        legend_RS='Риман–Зигель',
        annot_N='N(1000) = 649 (принцип аргумента)',
        f13=('E18 (O-J2): медианное время компиляции по методам при равных ограничениях ISA',
             'медиана времени компиляции, мс (log)', 'метод'),
        f14=('E18 (O-J2): точность против стоимости — 69 независимых целей',
             '1−F (log)', 'время компиляции, мс (log)'),
        legend_abqp='ABQP (замкнутая форма, Givens-QR)',
        legend_bl1='BL1: наивный Givens',
        legend_bl2='BL2: Эйлер ZYZ (учебная)',
        legend_bl4='BL4: Хаусхолдер',
        legend_bl3='BL3: покоординатный спуск',
        legend_bl5='BL5: случайный поиск',
        legend_thr12='порог 1e−12',
        annot_x59='×59 000 по времени',
        annot_sr='успех 1e−12:',
    ),
    'en': dict(
        f1=('E02: Haar unitary compilation (Givens + phases)',
            'log$_{10}$(1−F) over the sample', 'matrix index'),
        f2=('E03: compilation cost scaling',
            'compile time, s (log)', 'dimension d (log)'),
        f3=('E05: phase-noise sensitivity',
            'p95(1−F)', 'σ$_φ$, rad'),
        f4=('E07: repetition code vs controls',
            'error rate', 'p (bit flip per step)'),
        f5=('E11: blind reading of ζ zeros off the critical line',
            '|ζ(½+it)| and unwrapped arg ζ', 't'),
        f6=('E12: Mach–Zehnder interferometer',
            'P(output 1)', 'φ, rad'),
        f7=('E14: CHSH — quantum model vs LHV',
            'quantity S', 'computation variant'),
        f8=('E15: three robustness mechanisms — discriminating signature',
            'effect (log)', 'mechanism'),
        legend_1mF='1−F', legend_p95='p95', legend_median='median',
        legend_uncoded='uncoded', legend_logical='code (3 repeats)',
        legend_corr='control: correlated errors',
        legend_abszeta='|ζ(½+it)|', legend_arg='arg ζ (unwrapped)',
        legend_det='detected zeros (blind)',
        legend_S_an='S analytic (2√2)', legend_S_sm='S Monte Carlo (10⁶)',
        legend_lhv='max LHV (=2)', legend_local='local bound (=2)',
        legend_M1='M1: common local unitary',
        legend_M2='M2: asymmetric phase',
        legend_M3f='M3: AB flux, full quantum',
        legend_M3h='M3: AB flux, half quantum',
        legend_abl='ablation (φ≡0)', legend_lin='control: linear phase',
        x_S_var=['analytic', 'MC 10⁶', 'LHV max'],
        f9=('E17: blind reading of 649 ζ zeros up to height T = 1000',
            '|ζ(½+it)| and unwrapped arg ζ', 't'),
        f10=('E16: cost of ζ(½+it) at equal accuracy: Euler–Maclaurin vs Riemann–Siegel',
            'median evaluation time, ms (log)', 'height t (log)'),
        f11=('E17: accuracy of 649 zeros against the mpmath.zetazero reference',
            '|Δγ|, rad (log)', 'zero index n'),
        f12=('E17: completeness — cumulative zero count and N(T) via the standard path',
            'number of zeros below γ', 'height γ'),
        legend_em='engine A: Euler–Maclaurin (blind)',
        legend_rs='engine B: Riemann–Siegel (blind)',
        legend_thr='threshold 1e−9',
        legend_cum_em='found by engine A',
        legend_cum_rs='found by engine B',
        legend_N_ref='mpmath.zetazero (reference)',
        legend_EM='Euler–Maclaurin',
        legend_RS='Riemann–Siegel',
        annot_N='N(1000) = 649 (argument principle)',
        f13=('E18 (O-J2): median compile time by method under equal ISA constraints',
             'median compile time, ms (log)', 'method'),
        f14=('E18 (O-J2): accuracy vs cost — 69 independent targets',
             '1−F (log)', 'compile time, ms (log)'),
        legend_abqp='ABQP (closed form, Givens-QR)',
        legend_bl1='BL1: naive Givens',
        legend_bl2='BL2: Euler ZYZ (textbook)',
        legend_bl4='BL4: Householder',
        legend_bl3='BL3: coordinate descent',
        legend_bl5='BL5: random search',
        legend_thr12='threshold 1e−12',
        annot_x59='×59,000 in time',
        annot_sr='1e−12 success:',
    ),
}


def apply():
    t = TOKENS
    matplotlib.rcParams.update({
        'figure.facecolor': t['bg'], 'axes.facecolor': t['panel'],
        'savefig.facecolor': t['bg'], 'text.color': t['ink'],
        'axes.edgecolor': t['muted'], 'axes.labelcolor': t['ink'],
        'xtick.color': t['muted'], 'ytick.color': t['muted'],
        'axes.titlesize': 12.5, 'axes.titleweight': 'bold',
        'axes.labelsize': 10.5, 'xtick.labelsize': 9, 'ytick.labelsize': 9,
        'legend.fontsize': 8.5, 'legend.frameon': False,
        'axes.spines.top': False, 'axes.spines.right': False,
        'font.family': 'DejaVu Sans', 'axes.unicode_minus': False,
    })


def read_csv(name):
    path = os.path.join(RES, name + ".csv")
    with open(path, newline='', encoding='utf-8') as f:
        r = csv.DictReader(f)
        return list(r)


def f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return np.nan


def save(fig, stem, lang):
    d = os.path.join(ROOT, 'figures_hires', lang)
    os.makedirs(d, exist_ok=True)
    fig.savefig(os.path.join(d, f'{stem}_{lang}.png'), dpi=600)
    plt.close(fig)


def fig01(L):
    rows = read_csv("experiment_02_haar")
    fig, axes = plt.subplots(1, 2, figsize=(9.5, 4.1), constrained_layout=True)
    for ax, (d, seed) in zip(axes, [(4, 96), (8, 296)]):
        rr = [r for r in rows if int(float(r["dimension"])) == d]
        for r, col, lbl in ((rr[0], TOKENS['line'], 'replication'),
                            (rr[1], TOKENS['copper'], 'new seeds')):
            errs = f(r["max_one_minus_F"]), f(r["p95_one_minus_F"]), f(r["median_one_minus_F"])
            ax.bar([0, 1, 2], [max(v, 1e-18) for v in errs], width=0.55,
                   color=['none', 'none', 'none'])
        # per-run scatter isn't stored; plot max/p95/median bars per series
        xs = np.arange(3)
        w = 0.36
        for k, (r, col, lbl) in enumerate(((rr[0], TOKENS['line'], 'replication_v20'),
                                           (rr[1], TOKENS['copper'], 'new_predeclared'))):
            vals = [max(f(r["max_one_minus_F"]), 1e-18),
                    max(f(r["p95_one_minus_F"]), 1e-18),
                    max(f(r["median_one_minus_F"]), 1e-18)]
            ax.bar(xs + (k - 0.5) * w, np.log10(vals), width=w, color=col,
                   alpha=0.85, label=lbl)
        thr = -12 if d == 4 else -10
        ax.axhline(thr, color=TOKENS['bad'], lw=1.1, ls='--')
        ax.text(2.35, thr - 0.25, f'порог 1e{{{thr}}}' if L is LANG['ru']
                else f'threshold 1e{{{thr}}}', color=TOKENS['bad'], fontsize=8)
        ax.set_xticks(xs)
        ax.set_xticklabels(['max', 'p95', 'median' if L is LANG['en'] else 'медиана'])
        ax.set_title(f'd={d}×{d} (seed ' + rr[0]["seed"] + ' / ' + rr[1]["seed"] + ')')
        ax.set_ylabel(L['f1'][1])
        ax.legend(loc='lower right')
    fig.suptitle(L['f1'][0], fontsize=13, fontweight='bold')
    return fig


def fig02(L):
    rows = read_csv("experiment_03_scaling")
    fit = read_csv("experiment_03_fit")[0]
    d = np.array([f(r["dimension"]) for r in rows])
    t = np.array([f(r["sec_compile"]) for r in rows])
    b = f(fit["slope_b_log2"])
    lo, hi = f(fit["ci_lo"]), f(fit["ci_hi"])
    fig, ax = plt.subplots(figsize=(6.8, 4.4), constrained_layout=True)
    ax.loglog(d, t, 'o-', color=TOKENS['line'], lw=1.6, ms=5,
              label=L['legend_1mF'] if False else 'compile time')
    dd = np.linspace(d.min(), d.max(), 50)
    a = f(fit["intercept_a_log2"])
    ax.loglog(dd, 2 ** (a + b * np.log2(dd)), '--', color=TOKENS['copper'],
              label=f'fit: t ∝ d^{b:.2f}  [{lo:.2f}, {hi:.2f}] (95%)')
    ax.set_xlabel(L['f2'][2])
    ax.set_ylabel(L['f2'][1])
    ax.set_title(L['f2'][0])
    ax.grid(True, which='both', alpha=0.15, color=TOKENS['grid'])
    ax.legend(loc='upper left')
    return fig


def fig03(L):
    rows = read_csv("experiment_05_phase_noise")
    rr = [r for r in rows if r["mode"] == "random_sigma"]
    sig = np.array([f(r["sigma_rad"]) for r in rr])
    p95 = np.array([f(r["p95_one_minus_F"]) for r in rr])
    med = np.array([f(r["median_one_minus_F"]) for r in rr])
    fig, ax = plt.subplots(figsize=(6.8, 4.4), constrained_layout=True)
    ax.loglog(sig[sig > 0], np.maximum(p95[sig > 0], 1e-18), 'o-',
              color=TOKENS['line'], label=L['legend_p95'])
    ax.loglog(sig[sig > 0], np.maximum(med[sig > 0], 1e-18), 's--',
              color=TOKENS['slate'], label=L['legend_median'])
    ax.axhline(1e-8, color=TOKENS['bad'], ls='--', lw=1.1)
    ax.axvline(1e-5, color=TOKENS['gold'], ls=':', lw=1.2)
    ax.text(1.3e-5, 3e-13, 'σ* = 1e−5', color=TOKENS['gold'], fontsize=9)
    ax.set_xlabel(L['f3'][2])
    ax.set_ylabel(L['f3'][1])
    ax.set_title(L['f3'][0])
    ax.grid(True, which='both', alpha=0.15, color=TOKENS['grid'])
    ax.legend(loc='upper left')
    return fig


def fig04(L):
    rows = read_csv("experiment_07_repetition_code")
    ind = [r for r in rows if r["mode"] == "independent"]
    cor = [r for r in rows if r["mode"] == "correlated"]
    p = np.array([f(r["p"]) for r in ind])
    unc = np.array([f(r["uncoded_error_rate"]) for r in ind])
    log = np.array([f(r["logical_error_rate"]) for r in ind])
    corl = np.array([f(r["logical_error_rate"]) for r in cor])
    fig, ax = plt.subplots(figsize=(6.8, 4.4), constrained_layout=True)
    ax.plot(p, unc, '-', color=TOKENS['muted'], lw=2.2, label=L['legend_uncoded'])
    ax.plot(p, log, '-', color=TOKENS['ok'], lw=2.2, label=L['legend_logical'])
    ax.plot(p, corl, '--', color=TOKENS['bad'], lw=1.8, label=L['legend_corr'])
    ax.axvline(0.5, color=TOKENS['grid'], lw=1)
    ax.set_xlabel(L['f4'][2])
    ax.set_ylabel(L['f4'][1])
    ax.set_title(L['f4'][0])
    ax.grid(True, alpha=0.15, color=TOKENS['grid'])
    ax.legend(loc='upper left')
    return fig


def fig05(L):
    curve = read_csv("experiment_11_winding_curve")
    with open(os.path.join(RES, "e11_detector_output.csv"),
              newline='', encoding='utf-8') as f_:
        det = list(csv.DictReader(f_))
    ts = np.array([f(r["t"]) for r in curve])
    args = np.array([f(r["arg_unwrapped"]) for r in curve])
    mags = np.array([f(r["abs_zeta"]) for r in curve])
    pos = [float(r["key2"]) for r in det if r["kind"] == "position"]
    fig, ax1 = plt.subplots(figsize=(8.6, 4.6), constrained_layout=True)
    ax1.plot(ts, mags, color=TOKENS['line'], lw=0.9, label=L['legend_abszeta'])
    ax1.set_yscale('log')
    ax1.set_xlabel(L['f5'][2])
    ax1.set_ylabel(L['f5'][1])
    ax1.grid(True, alpha=0.12, color=TOKENS['grid'])
    for p in pos:
        ax1.axvline(p, color=TOKENS['copper'], lw=0.7, alpha=0.55)
    ax2 = ax1.twinx()
    ax2.plot(ts, args / np.pi, color=TOKENS['slate'], lw=1.3, alpha=0.85,
             label=L['legend_arg'])
    ax2.set_ylabel('arg ζ / π', color=TOKENS['slate'])
    ax2.tick_params(axis='y', colors=TOKENS['slate'])
    ax2.spines['right'].set_visible(True)
    ax1.set_title(L['f5'][0])
    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax1.legend(h1 + h2, l1 + l2, loc='upper left')
    return fig


def fig06(L):
    rows = read_csv("experiment_12_interferometer")
    rr = [r for r in rows if r["grid"] == "dense_257"]
    phi = np.array([f(r["phi"]) for r in rr])
    pn = np.array([f(r["p_numeric"]) for r in rr])
    pa = np.array([f(r["p_analytic"]) for r in rr])
    fig, ax = plt.subplots(figsize=(6.8, 4.2), constrained_layout=True)
    ax.plot(phi, pa, '-', color=TOKENS['muted'], lw=2.4, label='sin²(φ/2)')
    ax.plot(phi, pn, '--', color=TOKENS['copper'], lw=1.2,
            label='численно (max |Δ| = 6.7e−16)' if L is LANG['ru']
            else 'numeric (max |Δ| = 6.7e−16)')
    ax.set_xlabel(L['f6'][2])
    ax.set_ylabel(L['f6'][1])
    ax.set_title(L['f6'][0])
    ax.grid(True, alpha=0.15, color=TOKENS['grid'])
    ax.legend(loc='upper right')
    return fig


def fig07(L):
    rows = read_csv("experiment_14_chsh")
    g = {r["quantity"]: f(r["value"]) for r in rows}
    vals = [g["S_analytic"], g["S_sampled_1e6"], g["LHV_max_S"]]
    fig, ax = plt.subplots(figsize=(6.4, 4.2), constrained_layout=True)
    colors = [TOKENS['line'], TOKENS['copper'], TOKENS['bad']]
    bars = ax.bar(L['x_S_var'], vals, width=0.55, color=colors, alpha=0.9)
    ax.errorbar(1, g["S_sampled_1e6"], yerr=3 * g["S_sampled_sigma"],
                fmt='none', ecolor=TOKENS['ink'], capsize=4, lw=1.2)
    ax.axhline(2.0, color=TOKENS['muted'], ls=':', lw=1.4)
    ax.text(2.28, 2.03, 'S = 2', color=TOKENS['muted'], fontsize=9)
    ax.axhline(2 * np.sqrt(2), color=TOKENS['gold'], ls='--', lw=1.0, alpha=0.7)
    for b_, v in zip(bars, vals):
        ax.text(b_.get_x() + b_.get_width() / 2, v + 0.03, f'{v:.4f}',
                ha='center', fontsize=8.5)
    ax.set_ylim(0, 3.2)
    ax.set_ylabel(L['f7'][1])
    ax.set_title(L['f7'][0])
    ax.grid(True, axis='y', alpha=0.15, color=TOKENS['grid'])
    return fig


def fig08(L):
    rows = read_csv("experiment_15_topology_ablation")
    g = {}
    for r in rows:
        g.setdefault(r["mechanism"], []).append(f(r["effect"]))
    names = ["M1", "M2", "M3q", "M3h", "ABL", "LIN"]
    vals = [max(g["M1_common_local_unitary"]),
            max(g["M2_asymmetric_phase"]),
            max(g["M3_AB_flux_full_quantum"]),
            max(g["M3_AB_flux_half_quantum"]),
            max(g["ABLATION_phi0_full_shift"]),
            max(g["CONTROL_linear_phase_model"])]
    labels = {'ru': ['M1: общая\nунитарная', 'M2: асимм.\nфаза δ=0.5',
                     'M3: AB\nполный квант', 'M3: AB\nполуквант',
                     'абляция\n(φ≡0)', 'линейная\nфаза (контроль)'],
              'en': ['M1: common\nunitary', 'M2: asym.\nphase δ=0.5',
                     'M3: AB\nfull quantum', 'M3: AB\nhalf quantum',
                     'ablation\n(φ≡0)', 'linear\nphase (control)']}[
                  'ru' if L is LANG['ru'] else 'en']
    cols = [TOKENS['ok'], TOKENS['line'], TOKENS['gold'], TOKENS['copper'],
            TOKENS['muted'], TOKENS['bad']]
    fig, ax = plt.subplots(figsize=(7.6, 4.4), constrained_layout=True)
    bars = ax.bar(labels, np.maximum(vals, 1e-17), width=0.6, color=cols,
                  alpha=0.9)
    ax.set_yscale('log')
    ax.axhline(1e-12, color=TOKENS['muted'], ls=':', lw=1.1)
    ax.text(4.6, 4e-13, '1e−12', color=TOKENS['muted'], fontsize=8)
    for b_, v in zip(bars, vals):
        ax.text(b_.get_x() + b_.get_width() / 2, max(v, 1e-17) * 1.6,
                f'{v:.1e}' if v < 0.01 else f'{v:.2f}', ha='center', fontsize=8)
    ax.set_ylabel(L['f8'][1])
    ax.set_title(L['f8'][0])
    ax.grid(True, axis='y', which='both', alpha=0.12, color=TOKENS['grid'])
    ax.tick_params(axis='x', labelsize=7.6)
    return fig


def fig09(L):
    curve = read_csv("experiment_17_winding_curve")
    pos = _read_positions(os.path.join(RES, "e17_detector_em.csv"))
    pos_rs = _read_positions(os.path.join(RES, "e17_detector_rs.csv"))
    ts = np.array([f(r["t"]) for r in curve])
    args = np.array([f(r["arg_unwrapped"]) for r in curve])
    mags = np.array([f(r["abs_zeta"]) for r in curve])
    fig, ax1 = plt.subplots(figsize=(9.0, 4.6), constrained_layout=True)
    ax1.plot(ts, np.maximum(mags, 1e-16), color=TOKENS['line'], lw=0.7,
             label=L['legend_abszeta'])
    ax1.set_yscale('log')
    ax1.set_xlabel(L['f9'][2])
    ax1.set_ylabel(L['f9'][1])
    ax1.grid(True, alpha=0.12, color=TOKENS['grid'])
    for p in pos:
        ax1.axvline(p, color=TOKENS['copper'], lw=0.5, alpha=0.5)
    ax2 = ax1.twinx()
    ax2.plot(ts, args / np.pi, color=TOKENS['slate'], lw=1.2, alpha=0.85,
             label=L['legend_arg'])
    ax2.set_ylabel('arg ζ / π', color=TOKENS['slate'])
    ax2.tick_params(axis='y', colors=TOKENS['slate'])
    ax2.spines['right'].set_visible(True)
    ax1.set_title(L['f9'][0])
    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax1.legend(h1 + h2, l1 + l2, loc='upper left')
    return fig


def fig10(L):
    rows = read_csv("experiment_16_benchmark")
    t = np.array([f(r["height"]) for r in rows])
    em = np.array([f(r["em_ms_median"]) for r in rows])
    rs = np.array([f(r["rs_ms_median"]) for r in rows])
    fig, ax = plt.subplots(figsize=(6.8, 4.4), constrained_layout=True)
    ax.loglog(t, em, 'o-', color=TOKENS['line'], lw=1.7, ms=5,
              label=L['legend_EM'])
    ax.loglog(t, rs, 's--', color=TOKENS['copper'], lw=1.7, ms=5,
              label=L['legend_RS'])
    ax.set_xlabel(L['f10'][2])
    ax.set_ylabel(L['f10'][1])
    ax.set_title(L['f10'][0])
    ax.grid(True, which='both', alpha=0.15, color=TOKENS['grid'])
    ax.legend(loc='upper left')
    return fig


def _read_positions(path):
    pos = []
    for ln in open(path).read().splitlines()[1:]:
        parts = ln.split(",")
        if parts[0] == "position":
            pos.append(float(parts[2]))
    return pos


def fig11(L):
    em = _read_positions(os.path.join(RES, "e17_detector_em.csv"))
    rs = _read_positions(os.path.join(RES, "e17_detector_rs.csv"))
    ref = {}
    for ln in open(os.path.join(RES, "e17_zetazero_reference.csv")).read().splitlines()[1:]:
        parts = ln.split(",")
        if len(parts) == 2:
            ref[int(parts[0])] = float(parts[1])
    ref_g = [g for n, g in sorted(ref.items()) if 0.3 <= g < 1000.0]
    n_em = np.arange(1, len(em) + 1)
    d_em = np.array([abs(p - g) for p, g in zip(em, ref_g)])
    ref_rs = [g for n, g in sorted(ref.items()) if 50.0 <= g < 1000.0]
    n_rs = np.arange(1, len(rs) + 1)
    d_rs = np.array([abs(p - g) for p, g in zip(rs, ref_rs)])
    fig, ax = plt.subplots(figsize=(6.8, 4.4), constrained_layout=True)
    ax.semilogy(n_em, np.maximum(d_em, 1e-17), '.', color=TOKENS['line'],
                ms=3.5, alpha=0.8, label=L['legend_em'])
    ax.semilogy(n_rs, np.maximum(d_rs, 1e-17), '.', color=TOKENS['copper'],
                ms=3.5, alpha=0.8, label=L['legend_rs'])
    ax.axhline(1e-9, color=TOKENS['bad'], ls='--', lw=1.1)
    ax.text(560, 2.2e-9, L['legend_thr'], color=TOKENS['bad'], fontsize=8.5)
    ax.set_xlabel(L['f11'][2])
    ax.set_ylabel(L['f11'][1])
    ax.set_title(L['f11'][0])
    ax.grid(True, which='both', alpha=0.15, color=TOKENS['grid'])
    ax.legend(loc='upper right')
    return fig


def fig12(L):
    em = _read_positions(os.path.join(RES, "e17_detector_em.csv"))
    rs = _read_positions(os.path.join(RES, "e17_detector_rs.csv"))
    ref = {}
    for ln in open(os.path.join(RES, "e17_zetazero_reference.csv")).read().splitlines()[1:]:
        parts = ln.split(",")
        if len(parts) == 2:
            ref[int(parts[0])] = float(parts[1])
    ref_g = [g for n, g in sorted(ref.items()) if 0.3 <= g < 1000.0]
    fig, ax = plt.subplots(figsize=(6.8, 4.4), constrained_layout=True)
    ax.plot(ref_g, np.arange(1, len(ref_g) + 1), '-', color=TOKENS['muted'],
            lw=2.0, label=L['legend_N_ref'])
    ax.step(em, np.arange(1, len(em) + 1), where='post', color=TOKENS['line'],
            lw=1.2, alpha=0.9, label=L['legend_cum_em'])
    ax.step(rs, np.arange(1, len(rs) + 1), where='post', color=TOKENS['copper'],
            lw=1.0, alpha=0.9, label=L['legend_cum_rs'])
    ax.annotate(L['annot_N'], xy=(1000, 649), xytext=(620, 560),
                fontsize=9, color=TOKENS['ink'],
                arrowprops=dict(arrowstyle='->', color=TOKENS['muted'], lw=1.0))
    ax.set_xlabel(L['f12'][2])
    ax.set_ylabel(L['f12'][1])
    ax.set_title(L['f12'][0])
    ax.grid(True, alpha=0.15, color=TOKENS['grid'])
    ax.legend(loc='upper left')
    return fig


def _read18_baselines():
    """Строки experiment_18_baselines.csv (без испорченного контроля)."""
    rows = []
    with open(os.path.join(RES, 'experiment_18_baselines.csv')) as f:
        import csv as _csv
        for r in _csv.DictReader(f):
            if r.get('family') == 'control':
                continue
            rows.append(r)
    return rows


def fig13(L):
    import csv as _csv
    summary = []
    with open(os.path.join(RES, 'experiment_18_summary.csv')) as f:
        for r in _csv.DictReader(f):
            summary.append(r)
    order = ['ABQP', 'BL1_naive_givens', 'BL2_euler_zyz', 'BL4_householder',
             'BL3_coord_descent', 'BL5_random_search']
    names = {'ABQP': 'ABQP', 'BL1_naive_givens': 'BL1',
             'BL2_euler_zyz': 'BL2', 'BL4_householder': 'BL4',
             'BL3_coord_descent': 'BL3', 'BL5_random_search': 'BL5'}
    colors = {'ABQP': TOKENS['copper'], 'BL1_naive_givens': TOKENS['line'],
              'BL2_euler_zyz': TOKENS['slate'], 'BL4_householder': TOKENS['gold'],
              'BL3_coord_descent': TOKENS['bad'], 'BL5_random_search': TOKENS['muted']}
    med, sr = [], []
    for m in order:
        row = [r for r in summary if r['method'] == m][0]
        med.append(float(row['median_compile_ms']))
        sr.append(float(row['success_rate_1e12']))
    fig, ax = plt.subplots(figsize=(6.8, 4.4), constrained_layout=True)
    xs = np.arange(len(order))
    ax.bar(xs, med, color=[colors[m] for m in order], width=0.62,
           edgecolor=TOKENS['ink'], linewidth=0.5)
    ax.set_yscale('log')
    for x, (m, v, s) in enumerate(zip(order, med, sr)):
        ax.text(x, v * 1.35, f'{s:.2f}', ha='center', fontsize=8.5,
                color=TOKENS['ink'])
    ax.text(len(order) - 1.2, med[0] * 40,
            L['annot_sr'] + f' {sr[0]:.2f}', fontsize=9, color=TOKENS['copper'])
    ax.set_xticks(xs)
    ax.set_xticklabels([names[m] for m in order])
    ax.set_ylabel(L['f13'][1])
    ax.set_title(L['f13'][0], fontsize=10.5)
    ax.grid(True, axis='y', alpha=0.15, color=TOKENS['grid'])
    return fig


def fig14(L):
    rows = _read18_baselines()
    groups = {
        'ABQP': ('copper', L['legend_abqp'], 22),
        'BL1_naive_givens': ('line', L['legend_bl1'], 8),
        'BL2_euler_zyz': ('slate', L['legend_bl2'], 8),
        'BL4_householder': ('gold', L['legend_bl4'], 8),
        'BL3_coord_descent': ('bad', L['legend_bl3'], 8),
        'BL5_random_search': ('muted', L['legend_bl5'], 8),
    }
    fig, ax = plt.subplots(figsize=(6.8, 4.4), constrained_layout=True)
    for m, (ck, lb, ms) in groups.items():
        pts = [(float(r['compile_ms']), float(r['one_minus_F']))
               for r in rows if r['method'] == m]
        pts = [(x, max(y, 1e-18)) for x, y in pts if y > 0 or m == 'ABQP']
        pts = [(x, max(y, 1e-18)) for x, y in pts]
        ax.scatter([p[0] for p in pts], [p[1] for p in pts], s=ms,
                   color=TOKENS[ck], alpha=0.75, label=lb,
                   edgecolors=TOKENS['ink'], linewidths=0.3)
    ax.axhline(1e-12, color=TOKENS['ok'], ls='--', lw=1.1)
    ax.text(60, 1.6e-12, L['legend_thr12'], color=TOKENS['ok'], fontsize=8.5)
    ax.annotate(L['annot_x59'], xy=(0.004, 4.5e-16), xytext=(0.05, 3e-14),
                fontsize=9, color=TOKENS['copper'],
                arrowprops=dict(arrowstyle='->', color=TOKENS['copper'], lw=1.0))
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel(L['f14'][2])
    ax.set_ylabel(L['f14'][1])
    ax.set_title(L['f14'][0], fontsize=10.5)
    ax.grid(True, which='both', alpha=0.15, color=TOKENS['grid'])
    ax.legend(loc='upper left', fontsize=7.8, framealpha=0.9)
    return fig


def main():
    apply()
    for lang, L in (('ru', LANG['ru']), ('en', LANG['en'])):
        print(f'[{lang}]')
        for stem, fn in (('fig01', fig01), ('fig02', fig02), ('fig03', fig03),
                         ('fig04', fig04), ('fig05', fig05), ('fig06', fig06),
                         ('fig07', fig07), ('fig08', fig08), ('fig09', fig09),
                         ('fig10', fig10), ('fig11', fig11), ('fig12', fig12),
                         ('fig13', fig13), ('fig14', fig14)):
            fig = fn(L)
            save(fig, stem, lang)
            print('  ', stem, 'ok')
    print('Фигуры: figures_hires/{ru,en}/fig01..fig14 @600dpi')


if __name__ == '__main__':
    main()
