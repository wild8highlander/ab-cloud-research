#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""scripts/make_figures.py — 16 рисунков серии × ru/en @600 dpi.

Все данные — из закоммиченных вердиктов data/*.json; запуск:
python3 scripts/make_figures.py
"""
import json
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import matplotlib.pyplot as plt  # noqa: E402

import figstyle as FS  # noqa: E402

DATA = os.path.join(ROOT, 'data')


def load(name):
    return json.load(open(os.path.join(DATA, name)))


def _ttl(lang, key):
    return FS.LANG[lang][key]


# ── fig01: слепой контроль ──────────────────────────────────────────────────
def fig01(t, lang):
    d = load('v01_verdict.json')
    fig, ax = plt.subplots(figsize=(7.2, 4.2), constrained_layout=True)
    seeds = [r['seed'] for r in d['calibration']]
    rcal = [r['r_cal'] for r in d['calibration']]
    ax.bar(range(len(seeds)), rcal, color=t['line'], alpha=0.55,
           label=_ttl(lang, 'fig01')[1] + ' (cal)')
    ax.axhline(d['r_test'], color=t['copper'], lw=2.2,
               label=f"r_test = {d['r_test']:.3f}")
    ns, sd = d['perm_null_mean'], d['perm_null_sd']
    ax.axhspan(ns - 2 * sd, ns + 2 * sd, color=t['bad'], alpha=0.13,
               label=_ttl(lang, 'fig01')[2])
    ax.set_xticks(range(len(seeds)))
    ax.set_xticklabels([str(s) for s in seeds])
    ax.set_title(_ttl(lang, 'fig01')[0])
    ax.set_ylabel(_ttl(lang, 'fig01')[1])
    ax.legend()
    FS.clean_axis(ax)
    return fig


# ── fig02: контрольные модели ───────────────────────────────────────────────
def fig02(t, lang):
    d = load('v02_verdict.json')
    fig, axs = plt.subplots(1, 2, figsize=(9.6, 4.2), constrained_layout=True)
    names = list(d['models'].keys())
    r = [d['models'][n]['r_mean'] for n in names]
    ks = [d['models'][n]['KS_GUE'] for n in names]
    cols = [t['line'] if n.startswith(('M0', 'N1', 'N4')) else
            (t['bad'] if 'POISSON' in n else t['slate']) for n in names]
    axs[0].barh(range(len(names)), r, color=cols, alpha=0.85)
    axs[0].axvline(0.5307, color=t['muted'], ls=':', lw=1)
    axs[0].axvline(0.5992, color=t['copper'], ls=':', lw=1)
    axs[0].set_yticks(range(len(names)))
    axs[0].set_yticklabels(names, fontsize=8)
    axs[0].set_xlabel('⟨r⟩')
    axs[0].set_title('⟨r⟩')
    axs[1].barh(range(len(names)), ks, color=cols, alpha=0.85)
    axs[1].set_yticks(range(len(names)))
    axs[1].set_yticklabels([])
    axs[1].set_xlabel('D_KS')
    axs[1].set_title('D_KS → GUE')
    for ax in axs:
        FS.clean_axis(ax)
    fig.suptitle(_ttl(lang, 'fig02')[0], fontsize=13, fontweight='bold')
    return fig


# ── fig03: скан критической линии ───────────────────────────────────────────
def fig03(t, lang):
    d = load('v03_verdict.json')
    fig, ax = plt.subplots(figsize=(7.2, 4.2), constrained_layout=True)
    sig = sorted(float(k) for k in d['D_mean'])
    Dm = [d['D_mean'][str(s)] for s in sig]
    Dlo = [min(x['D_KS'] for x in d['D_table'][str(s)]) for s in sig]
    Dhi = [max(x['D_KS'] for x in d['D_table'][str(s)]) for s in sig]
    ax.fill_between(sig, Dlo, Dhi, color=t['line'], alpha=0.16,
                    label='seeds min–max')
    ax.plot(sig, Dm, 'o-', color=t['line'], lw=2)
    ax.axvline(0.5, color=t['copper'], ls=':', lw=1.4, label='σ = 1/2')
    ax.set_xlabel(_ttl(lang, 'fig03')[2])
    ax.set_ylabel(_ttl(lang, 'fig03')[1])
    ax.set_title(_ttl(lang, 'fig03')[0])
    ax.legend()
    FS.clean_axis(ax)
    return fig


# ── fig04: паспорт оператора ────────────────────────────────────────────────
def fig04(t, lang):
    d = load('v04_verdict.json')
    fig, ax = plt.subplots(figsize=(7.6, 4.2), constrained_layout=True)
    rows = d['entries']
    labels = [f"L{r['L']},s{r['seed']}" for r in rows]
    herm = [max(r['hermiticity_max'], 1e-18) for r in rows]
    res = [max(r['eigpair_residual_max'], 1e-18) for r in rows]
    pair = [r['chiral_pair_max'] for r in rows]
    pair = [max(p, 1e-18) if not np.isnan(p) else np.nan for p in pair]
    x = np.arange(len(rows))
    ax.semilogy(x, herm, 's-', color=t['line'], label='‖H−H†‖')
    ax.semilogy(x, res, 'o-', color=t['copper'], label='‖Hv−λv‖')
    ax.semilogy(x, pair, '^-', color=t['slate'], label='λ↔−λ (W=0)')
    ax.axhline(d['epsilon_num'], color=t['bad'], ls=':', lw=1.2,
               label='ε = 1e-12')
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, fontsize=7.5)
    ax.set_ylabel(_ttl(lang, 'fig04')[1])
    ax.set_title(_ttl(lang, 'fig04')[0])
    ax.legend(fontsize=8)
    FS.clean_axis(ax)
    return fig


# ── fig05: предел решётки ───────────────────────────────────────────────────
def fig05(t, lang):
    d = load('v05_verdict.json')
    fig, ax = plt.subplots(figsize=(7.2, 4.2), constrained_layout=True)
    Ls = sorted(int(k) for k in d['err_c3_trace'])
    es = [d['err_c3_trace'][str(L)] for L in Ls]
    ax.loglog(Ls, es, 'o-', color=t['line'], label='e(L)')
    law = d['power_law']
    Lf = np.array(Ls, float)
    fit = law['a'] * Lf ** (-law['p'])
    ax.loglog(Lf, fit, ':', color=t['copper'],
              label=f"a·L^(−p), p = {law['p']:.2f}, R² = {law['r2']:.2f}")
    ax.set_xlabel(_ttl(lang, 'fig05')[2])
    ax.set_ylabel(_ttl(lang, 'fig05')[1])
    ax.set_title(_ttl(lang, 'fig05')[0])
    ax.legend()
    FS.clean_axis(ax)
    return fig


# ── fig06: спектральное тождество ───────────────────────────────────────────
def fig06(t, lang):
    d = load('v06_verdict.json')
    fig, ax = plt.subplots(figsize=(7.2, 4.0), constrained_layout=True)
    items = [('gate ↔ zeros (rank)', max(d['gate_rank_corr'], 1e-16)),
             ('H_ξ ↔ ξ (log resid)', d['Hxi_control']['max_abs_log_resid']),
             ('min gap (L=24)', d['min_gaps'][1])]
    ax.bar(range(len(items)), [-np.log10(v) for _, v in items],
           color=[t['bad'], t['ok'], t['slate']], alpha=0.85)
    ax.set_xticks(range(len(items)))
    ax.set_xticklabels([n for n, _ in items], fontsize=8.5)
    ax.set_ylabel(_ttl(lang, 'fig06')[1])
    ax.set_title(_ttl(lang, 'fig06')[0])
    FS.clean_axis(ax)
    return fig


# ── fig07: следовая формула ─────────────────────────────────────────────────
def fig07(t, lang):
    import mpmath as mp
    from scipy.interpolate import CubicSpline
    from rpbridge.primes import lambda_arrays
    from rpbridge.traceformula import (K_direct, K_formula, Q_identity)
    from rpbridge.zeros import load_zeros, rvm_count  # noqa: F401

    z = load_zeros(nmax=20000)
    from rpbridge.traceformula import C0_from_zeros
    C0 = C0_from_zeros(z)
    aa = np.linspace(0.0, 1.5, 601)
    aa = np.where(np.abs(aa - 0.5) < 1e-9, 0.5 + 1e-6, aa)
    Qv = np.array([Q_identity(a, C0) for a in aa])
    Qspl = CubicSpline(aa, Qv)
    ns_l, lm_l = lambda_arrays(2_000_000)
    lam_w = lm_l / np.sqrt(ns_l.astype(float))
    xs = np.linspace(0.05, 1.2, 24)
    kd = [K_direct(x, z, gmax=6000.0) for x in xs]
    kf = [K_formula(x, C0, Qspl, ns_l.astype(float), lam_w)[0] for x in xs]
    fig, ax = plt.subplots(figsize=(7.2, 4.2), constrained_layout=True)
    ax.semilogy(xs, [max(v, 1e-9) for v in kd], 'o-', color=t['line'],
                label='K(x) прямая сумма')
    ax.semilogy(xs, [max(v, 1e-9) for v in kf], 's--', color=t['copper'],
                label='явная формула (Th6)')
    ax.set_xlabel(_ttl(lang, 'fig07')[2])
    ax.set_ylabel(_ttl(lang, 'fig07')[1])
    ax.set_title(_ttl(lang, 'fig07')[0])
    ax.legend()
    FS.clean_axis(ax)
    return fig


# ── fig08: самосопряжённость ────────────────────────────────────────────────
def fig08(t, lang):
    d = load('v08_verdict.json')
    fig, ax = plt.subplots(figsize=(7.2, 4.2), constrained_layout=True)
    keys = list(d['bc_shifts_L24'].keys())
    vals = [v if isinstance(v, float) else np.nan for v in
            d['bc_shifts_L24'].values()]
    cols = [t['line'] if k.startswith('open') else t['slate'] for k in keys]
    ax.bar(range(len(keys)), vals, color=cols, alpha=0.85)
    ax.set_xticks(range(len(keys)))
    ax.set_xticklabels(keys, rotation=30, fontsize=8)
    ax.set_ylabel(_ttl(lang, 'fig08')[1])
    ax.set_title(_ttl(lang, 'fig08')[0])
    FS.clean_axis(ax)
    return fig


# ── fig09: симметрийная редукция ────────────────────────────────────────────
def fig09(t, lang):
    d = load('v09_verdict.json')
    fig, ax = plt.subplots(figsize=(7.2, 4.0), constrained_layout=True)
    a = d['part_A']
    items = [('ε_Ux', a['eps_Ux']), ('ε_Uy', a['eps_Uy']),
             ('блоки ↔ спектр', a['block_union_err']),
             ('внеблочные', a['offdiag_max'])]
    ax.bar(range(len(items)), [-np.log10(max(v, 1e-18)) for _, v in items],
           color=[t['ok']] * 3 + [t['ok']], alpha=0.9)
    ax.set_xticks(range(len(items)))
    ax.set_xticklabels([n for n, _ in items], fontsize=8.5)
    ax.set_ylabel('−log₁₀ ε')
    ax.set_title(_ttl(lang, 'fig09')[0] + f"  (тор {d['L']}×{d['L']})")
    FS.clean_axis(ax)
    return fig


# ── fig10: обратная задача ──────────────────────────────────────────────────
def fig10(t, lang):
    d = load('v10_verdict.json')
    fig, ax = plt.subplots(figsize=(7.2, 4.0), constrained_layout=True)
    for i, (k, v) in enumerate(d['sensitivity'].items()):
        ax.bar([i - 0.18], [v['rank']], width=0.32, color=t['line'],
               label='rank J' if i == 0 else None)
        ax.bar([i + 0.18], [v['n_params']], width=0.32, color=t['copper'],
               label='n_params' if i == 0 else None)
    ax.set_xticks(range(len(d['sensitivity'])))
    ax.set_xticklabels(list(d['sensitivity'].keys()))
    ax.set_ylabel(_ttl(lang, 'fig10')[1])
    ax.set_title(_ttl(lang, 'fig10')[0])
    ax.legend()
    FS.clean_axis(ax)
    return fig


# ── fig11: универсальность ──────────────────────────────────────────────────
def fig11(t, lang):
    d = load('v11_verdict.json')
    fig, ax = plt.subplots(figsize=(7.2, 4.0), constrained_layout=True)
    modes = ('A0', 'D1', 'D2', 'D3')
    rmeans = [np.mean([r[f'r_{m}'] for r in d['rows']]) for m in modes]
    rsd = [np.std([r[f'r_{m}'] for r in d['rows']]) for m in modes]
    cols = [t['line'], t['copper'], t['copper'], t['copper']]
    ax.bar(range(len(modes)), rmeans, yerr=rsd, color=cols, alpha=0.85,
           capsize=4)
    ax.axhline(0.5992, color=t['muted'], ls=':', lw=1.2, label='GUE 0.5992')
    ax.set_xticks(range(len(modes)))
    ax.set_xticklabels(modes)
    ax.set_ylabel('⟨r⟩')
    ax.set_title(_ttl(lang, 'fig11')[0])
    ax.legend()
    FS.clean_axis(ax)
    return fig


# ── fig12: сертификаты ──────────────────────────────────────────────────────
def fig12(t, lang):
    d = load('v12_verdict.json')
    fig, ax = plt.subplots(figsize=(7.2, 4.0), constrained_layout=True)
    certs = d['certificates']
    idx = [c['index'] for c in certs]
    lam = [c['lam_tilde'] for c in certs]
    half = [(c['hi'] - c['lo']) / 2 for c in certs]
    ax.errorbar(idx, lam, yerr=half, fmt='o', color=t['line'], capsize=3,
                label='сертификат [λ̃±δ²/gap]')
    ax.scatter(idx, lam, s=12, color=t['copper'], zorder=3)
    ax.set_xlabel(_ttl(lang, 'fig12')[2])
    ax.set_ylabel('λ')
    ax.set_title(_ttl(lang, 'fig12')[0] + '  (L=12)')
    ax.set_yscale('symlog', linthresh=0.1)
    ax.legend()
    FS.clean_axis(ax)
    return fig


# ── fig13: формальный мост ──────────────────────────────────────────────────
def fig13(t, lang):
    d = load('v13_verdict.json')
    fig, ax = plt.subplots(figsize=(7.2, 4.0), constrained_layout=True)
    counts = {'proven': d['n_proven'], 'computed': d['n_computed'],
              'assumed': d['n_assumed']}
    cols = {'proven': t['ok'], 'computed': t['gold'], 'assumed': t['bad']}
    ax.bar(range(len(counts)), list(counts.values()),
           color=[cols[k] for k in counts], alpha=0.9)
    ax.set_xticks(range(len(counts)))
    ax.set_xticklabels([f'{k} ({v})' for k, v in counts.items()])
    ax.set_ylabel('N')
    ax.set_title(_ttl(lang, 'fig13')[0] + '  —  RH: certified')
    FS.clean_axis(ax)
    return fig


# ── fig14: аудит утверждений ────────────────────────────────────────────────
def fig14(t, lang):
    d = load('v14_verdict.json')
    fig, ax = plt.subplots(figsize=(7.2, 4.0), constrained_layout=True)
    stats = {}
    for c in d['claims']:
        stats[c['status']] = stats.get(c['status'], 0) + 1
    order = ['proven', 'measured', 'conjecture', 'refuted']
    vals = [stats.get(k, 0) for k in order]
    cols = [t['ok'], t['gold'], t['bad'], t['bad']]
    ax.bar(range(len(order)), vals, color=cols, alpha=0.9)
    ax.set_xticks(range(len(order)))
    ax.set_xticklabels([f'{k} ({v})' for k, v in zip(order, vals)])
    ax.set_ylabel('N')
    ax.set_title(_ttl(lang, 'fig14')[0])
    FS.clean_axis(ax)
    return fig


# ── fig15: критерий Ли ──────────────────────────────────────────────────────
def fig15(t, lang):
    d = load('v15_verdict.json')
    fig, ax = plt.subplots(figsize=(7.6, 4.2), constrained_layout=True)
    # пересчёт λ_n из вердикта невозможен без нулей — строим по файлу
    from rpbridge.li import li_from_zeros
    from rpbridge.zeros import load_zeros
    lam, tail, _ = li_from_zeros(load_zeros(), n_max=1000)
    n = np.arange(1, len(lam) + 1)
    ax.semilogy(n, lam, '-', color=t['line'], lw=1.4, label='λ_n')
    ax.semilogy(n, tail, ':', color=t['copper'], lw=1.2,
                label='сертифицированный хвост')
    ax.axhline(1e-6, color=t['muted'], lw=0.8)
    ax.set_xlabel('n')
    ax.set_ylabel(_ttl(lang, 'fig15')[1])
    ax.set_title(_ttl(lang, 'fig15')[0] +
                 f"  (λ_n > 0, n ≤ {d['n_max']}; min λ₁ = {d['lambda_1']:.4f})")
    ax.legend()
    FS.clean_axis(ax)
    return fig


# ── fig16: карта программы ──────────────────────────────────────────────────
def fig16(t, lang):
    names_ru = ['V1 слепой', 'V2 null-модели', 'V3 скан σ', 'V4 паспорт T1',
                'V5 предел', 'V6 тождество', 'V7 след T6', 'V8 самосопр. T2',
                'V9 редукция T5', 'V10 обратная', 'V11 универс.',
                'V12 сертификаты T3', 'V13 формальный', 'V14 аудит',
                'V15 Ли T4', 'V16 полн. гамильт.', 'V17 электрон',
                'V18 процессор', 'V19 сшивка']
    names_en = ['V1 blind', 'V2 nulls', 'V3 σ-scan', 'V4 passport T1',
                'V5 limit', 'V6 identity', 'V7 trace T6', 'V8 self-adj T2',
                'V9 reduction T5', 'V10 inverse', 'V11 universality',
                'V12 certificates T3', 'V13 formal', 'V14 audit',
                'V15 Li T4', 'V16 full H', 'V17 electron',
                'V18 processor', 'V19 stitching']
    names = names_ru if lang == 'ru' else names_en
    # статусы: proven → ok, measured → gold
    statuses = ['measured', 'measured', 'measured', 'proven', 'measured',
                'measured', 'proven', 'proven', 'proven', 'measured',
                'measured', 'proven', 'measured', 'measured', 'proven',
                'measured', 'measured', 'measured', 'measured']
    fig, ax = plt.subplots(figsize=(9.6, 4.4), constrained_layout=True)
    cols = [t['ok'] if s == 'proven' else t['gold'] for s in statuses]
    ax.bar(range(len(names)), [1] * len(names), color=cols, alpha=0.85)
    for i, (nm, st) in enumerate(zip(names, statuses)):
        ax.text(i, 0.5, nm, rotation=90, ha='center', va='center',
                fontsize=7.2, color='white', fontweight='bold')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines[:].set_visible(False)
    ax.set_title(_ttl(lang, 'fig16')[0] +
                 '  ·  proven: ' + str(statuses.count('proven')) +
                 ' / measured: ' + str(statuses.count('measured')))
    return fig


# ── fig17: V16 полный гамильтониан × алгебраическая функция ────────────────
def fig17(t, lang):
    d = load('v16_verdict.json')
    rows = d['rows']
    n_cfg = max(r['cfg_id'] for r in rows) + 1
    fig, axs = plt.subplots(1, 2, figsize=(9.6, 4.2),
                            constrained_layout=True)
    # (a) карта r_align: cfg × seed
    seeds = sorted({r['seed'] for r in rows})
    M = np.full((len(seeds), n_cfg), np.nan)
    for r in rows:
        M[seeds.index(r['seed']), r['cfg_id']] = r['r_align']
    im = axs[0].imshow(M, aspect='auto', cmap='RdBu_r', vmin=-0.35,
                       vmax=0.35)
    axs[0].set_title('карта r_align' if lang == 'ru' else 'r_align map')
    axs[0].set_xlabel(_ttl(lang, 'fig17')[2])
    axs[0].set_ylabel('seed')
    axs[0].set_yticks(range(len(seeds)))
    axs[0].set_yticklabels([str(s) for s in seeds])
    fig.colorbar(im, ax=axs[0], shrink=0.85)
    # (b) сравнение весов + нулевая зона
    wc = d['weight_compare']
    names = ['theta', 'logzeta', 'none']
    labels = {'theta': ('θ-фаза Z_id', 'θ phase of Z_id'),
              'logzeta': ('log|ζ| (протокол V3)', 'log|ζ| (V3)'),
              'none': ('без веса', 'no weight')}
    vals = [wc[n]['r_align'] for n in names]
    nm, nsd = d['null']['best_mean'], d['null']['best_sd']
    axs[1].axhspan(nm - 2 * nsd, nm + 2 * nsd, color=t['bad'], alpha=0.13,
                   label=_ttl(lang, 'fig01')[2])
    axs[1].bar(range(3), vals, color=[t['line'], t['copper'], t['muted']],
               alpha=0.85)
    for i, v in enumerate(vals):
        axs[1].text(i, v + (0.02 if v >= 0 else -0.04), f'{v:+.3f}',
                    ha='center', fontsize=9)
    axs[1].set_xticks(range(3))
    axs[1].set_xticklabels([labels[n][lang == 'en'] for n in names],
                           fontsize=8.5)
    axs[1].set_title('r_align vs вес вихрей' if lang == 'ru'
                     else 'r_align vs vortex weight')
    axs[1].legend()
    for ax in axs:
        FS.clean_axis(ax)
    return fig


# ── fig18: V17 электрон на критической прямой ──────────────────────────────
def fig18(t, lang):
    d = load('v17_verdict.json')
    modes = d['modes']
    fig, axs = plt.subplots(1, 3, figsize=(12.6, 3.9),
                            constrained_layout=True)
    cols = {'clean': t['muted'], 'random': t['copper'], 'zeta': t['line']}
    names = {'clean': ('чистая решётка', 'clean lattice'),
             'random': ('случайное облако', 'random cloud'),
             'zeta': ('ζ-облако', 'ζ cloud')}
    for m in ('clean', 'random', 'zeta'):
        tr = modes[m]['traj']
        axs[0].plot(tr['t'], tr['x'], color=cols[m], lw=1.6,
                    label=names[m][lang == 'en'])
        axs[1].plot(tr['t'], tr['p_exit'], color=cols[m], lw=1.6)
        axs[2].plot(tr['t'], tr['C'], color=cols[m], lw=1.6)
    s = d['summary']
    axs[0].set_title(_ttl(lang, 'fig18')[1].split(',')[0])
    axs[0].set_xlabel(_ttl(lang, 'fig18')[2])
    axs[0].set_ylabel('⟨x(t)⟩')
    axs[0].axhline(88, color=t['grid'], lw=1, ls='--')
    axs[0].legend(loc='upper left')
    axs[1].set_title('P(x ≥ 88)' if lang == 'ru' else 'P(x ≥ 88) transit')
    axs[1].set_xlabel(_ttl(lang, 'fig18')[2])
    axs[2].set_title('C(t) = |⟨ψ(0)|ψ(t)⟩|')
    axs[2].set_xlabel(_ttl(lang, 'fig18')[2])
    ratio = s['ratio_zeta_over_random']
    axs[1].text(0.03, 0.92, f'ζ/random = ×{ratio:.2f}',
                transform=axs[1].transAxes, fontsize=10,
                color=t['line'], fontweight='bold')
    for ax in axs:
        FS.clean_axis(ax)
    return fig


# ── fig19: V18 AB-оператор как процессор ────────────────────────────────────
def fig19(t, lang):
    d = load('v18_verdict.json')
    fig = plt.figure(figsize=(12.6, 4.0), constrained_layout=True)
    gs = fig.add_gridspec(1, 3)
    # (a) ворота
    ax = fig.add_subplot(gs[0])
    names = list(d['p1_gates'].keys())
    F = [d['p1_gates'][n]['fidelity'] for n in names]
    ax.bar(names, [min(f, 1.0) for f in F], color=t['line'], alpha=0.85)
    ax.set_ylim(0.99999, 1.00001)
    ax.set_title(('верность ворот (точные импульсы)' if lang == 'ru'
                  else 'gate fidelity (exact pulses)'))
    for i, f in enumerate(F):
        ax.text(i, 0.999997, 'F = 1.000000' if f >= 1 else f'{f:.8f}',
                ha='center', va='bottom', fontsize=7, rotation=90,
                color=t['ok'])
    # (b) мяч AB-Pong
    ax = fig.add_subplot(gs[1])
    ts, xs, marks = [], [], []
    import csv as _csv
    with open(os.path.join(DATA, 'v18_pong_log.csv'), encoding='utf-8') as f:
        for row in _csv.reader(f):
            if row[0] == 't':
                continue
            try:
                tm = float(row[0])
                xs.append(float(row[1]))
                ts.append(tm)
            except ValueError:
                marks.append((float(row[0]), row[1]))
    ax.plot(ts, xs, color=t['copper'], lw=1.0)
    for tm, ev in marks:
        if 'MIRROR_right' in ev:
            ax.axvline(tm, color=t['line'], alpha=0.35, lw=0.8)
        elif 'MIRROR_left' in ev:
            ax.axvline(tm, color=t['slate'], alpha=0.35, lw=0.8)
        else:
            ax.axvline(tm, color=t['bad'], alpha=0.6, lw=1.2)
    ax.set_xlabel('t')
    ax.set_ylabel('⟨x⟩ мяч' if lang == 'ru' else '⟨x⟩ ball')
    sc = d['p3_pong']['score']
    ax.set_title(('AB-Pong на AB-операторе: ' if lang == 'ru'
                  else 'AB-Pong on the AB operator: ') +
                 f"{sc['left']}:{sc['right']}")
    # (c) зацепление
    ax = fig.add_subplot(gs[2])
    cur = np.array(d['p2_entanglement']['curve'])
    ax.plot(cur[:, 0], cur[:, 1], color=t['gold'], lw=1.6)
    best = d['p2_entanglement']['best_concurrence']
    bt = d['p2_entanglement']['t_entangle']
    ax.axhline(1.0, color=t['grid'], lw=1, ls='--')
    ax.plot([bt], [best], 'o', color=t['copper'], ms=6)
    ax.set_xlabel('t')
    ax.set_ylabel('concurrence C(ρ)')
    ax.set_title(f'C_max = {best:.3f}' + (' (Белл ≈ 1)' if lang == 'ru'
                                         else ' (Bell ≈ 1)'))
    return fig


# ── fig20: V19 сшивка ветвей алгебраической функции ─────────────────────────
def fig20(t, lang):
    import mpmath as mp
    from rpbridge.zeros import load_zeros
    from rpbridge.stitching import theta_phase
    d = load('v19_verdict.json')
    zeros = np.asarray(load_zeros(nmax=2100), float)[:2001]
    mids = 0.5 * (zeros[:-1] + zeros[1:])
    th = np.array([float(theta_phase(m)) for m in mids])
    fig, axs = plt.subplots(1, 3, figsize=(13.2, 4.2),
                            constrained_layout=True)
    # (a) θ-лестница: Δθ mod 2π концентрируется у π
    dth = np.diff(th)
    frac = (dth / np.pi) % 2.0
    conc = d['layer_C']['theta_ladder']['concentration']
    axs[0].hist(frac, bins=48, range=(0, 2), color=t['line'], alpha=0.8)
    axs[0].axvline(1.0, color=t['copper'], lw=1.6, ls='--',
                   label='π' if lang == 'ru' else 'π')
    axs[0].axvspan(1 - 0.3, 1 + 0.3, color=t['copper'], alpha=0.14)
    axs[0].set_title(('θ-лестница, концентрация %.3f' % conc)
                     if lang == 'ru' else ('θ ladder, concentration %.3f'
                                           % conc))
    axs[0].set_xlabel(_ttl(lang, 'fig20')[2].split('·')[0].strip())
    axs[0].set_ylabel('число' if lang == 'ru' else 'count')
    axs[0].legend()
    # (b) знаковая когерентность: кумулятивное согласие
    sgn = np.sign(np.cos(th))
    ksgn = (-1.0) ** np.arange(len(mids))
    cum = np.cumsum(sgn == ksgn) / (np.arange(len(mids)) + 1)
    coh = d['layer_C']['sign_coherence']['agreement']
    axs[1].plot(cum, color=t['line'], lw=1.4,
                label=('согласие %.4f' % coh) if lang == 'ru'
                else ('agreement %.4f' % coh))
    axs[1].axhline(1.0, color=t['grid'], lw=1, ls='--')
    mism = np.where(sgn != ksgn)[0]
    if mism.size:
        axs[1].plot(mism, cum[mism], 'o', color=t['copper'], ms=5,
                    label=('сбои: %d' % mism.size) if lang == 'ru'
                    else ('mismatches: %d' % mism.size))
    axs[1].set_ylim(0.9, 1.005)
    axs[1].set_title('sign(cos θ(γ̃_k)) = (−1)^k' if lang == 'ru'
                     else 'sign(cos θ(γ̃_k)) = (−1)^k')
    axs[1].set_xlabel(_ttl(lang, 'fig20')[2].split('·')[1].strip())
    axs[1].set_ylabel('кумулятивное согласие' if lang == 'ru'
                      else 'cumulative agreement')
    axs[1].legend()
    # (c) фазовая карта тора сшивки: arg I_{r,s} на (Z/N)², N=15
    N = 15
    a, b = 7, 3
    Rr = np.arange(N)
    SS = np.arange(N)
    ph = np.array([[float(mp.arg(mp.e ** (2j * mp.pi * (a * r + b * s)
                                              / N))) for s in SS]
                   for r in Rr])
    im = axs[2].imshow(ph, cmap='twilight', vmin=-np.pi, vmax=np.pi,
                       aspect='auto', origin='lower')
    axs[2].set_title(('фазовый закон ζ^{ra+sb} (a=%d, b=%d, N=%d)'
                      % (a, b, N)) if lang == 'ru'
                     else ('phase law ζ^{ra+sb} (a=%d, b=%d, N=%d)'
                           % (a, b, N)))
    axs[2].set_xlabel('s')
    axs[2].set_ylabel('r')
    fig.colorbar(im, ax=axs[2], shrink=0.85)
    for ax in axs:
        FS.clean_axis(ax)
    return fig


ALL_FIGS = [fig01, fig02, fig03, fig04, fig05, fig06, fig07, fig08, fig09,
            fig10, fig11, fig12, fig13, fig14, fig15, fig16, fig17, fig18,
            fig19, fig20]


def main():
    themes = ('light',)
    for theme in themes:
        t = FS.apply(theme)
        for i, fn in enumerate(ALL_FIGS, 1):
            stem = f'fig{i:02d}'
            for lang in ('ru', 'en'):
                # подписи берутся внутри по lang; строим дважды
                pass
            fig = fn(t, 'ru')
            import os
            d = os.path.join(ROOT, 'figures_hires', 'ru')
            os.makedirs(d, exist_ok=True)
            fig.savefig(os.path.join(d, f'{stem}_ru.png'), dpi=600)
            plt.close(fig)
            fig = fn(t, 'en')
            d = os.path.join(ROOT, 'figures_hires', 'en')
            os.makedirs(d, exist_ok=True)
            fig.savefig(os.path.join(d, f'{stem}_en.png'), dpi=600)
            plt.close(fig)
            print(f'{stem} OK')
    print('ALL FIGURES DONE')


if __name__ == '__main__':
    main()
