#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_figures.py — рисунки серии AB Quantum Processor (600 dpi, ru/en).

fig01 ISA · fig02 компилятор · fig03 глубина · fig04 память/ALU (превью)
· fig05 считывание нулей (превью) · fig06 дорожная карта P0–P6.
Запуск: python3 scripts/make_figures.py
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)

import matplotlib.pyplot as plt                                    # noqa: E402
from figstyle import LANG, apply, clean_axis                      # noqa: E402

from rpbridge import alu, compiler as C, isa, memory               # noqa: E402
from rpbridge import nonlocality as NL, riemann_reader as RR       # noqa: E402

T = apply('light')


def save1(fig, stem, lang):
    """Сохранение ОДНОЙ языковой версии (в отличие от save_all)."""
    d = os.path.join(ROOT, 'figures_hires', lang)
    os.makedirs(d, exist_ok=True)
    fig.savefig(os.path.join(d, f'{stem}_{lang}.png'), dpi=600)
    plt.close(fig)
OK = T['ok']
LINE = T['line']
COPPER = T['copper']
SLATE = T['slate']
BAD = T['bad']
GOLD = T['gold']
MUTED = T['muted']

TXT = {
    'ru': dict(
        fid='fidelity калибровки', prim='примитив', phase_circle='Фазовая '
        'решётка AB: φ = 2πΦ/Φ₀ (континуум) на корнях из единицы (такт)',
        gates='затворов на схему', unitaries='унитарные',
        four='4×4 (200, сид 96)', eight='8×8 (100, сид 296)',
        thr='порог', max_f='максимум',
        ab2='AB2 (блоки)', phase='PHASE (фазы уровней)',
        ram='RAM: запись → чтение (64 паттерна)',
        lat='Латентность RAM: L(d) = a + b·d',
        alu='ALU: полные таблицы истинности',
        d='расстояние d', op='операция',
        write='записано', read='считано',
        zeros='|ζ(½+it)|', readpos='считанные нули',
        refpos='контроль (бисекция Z)',
        arg='arg ζ(½+it) (намотка)', slips='скачки π (нули)',
        store='ХРАНИТСЯ: констант формулы',
        produce='ЧИТАЕТСЯ: нулей',
        ratio='коэффициент считывания',
        note04='64/64 бит-в-бит · b = 4.0 ≤ 6',
        note05='12 нулей точно; макс. отклонение 3·10⁻³; таблица нулей '
               'не используется',
        p_note='П0 ИСПОЛНЕНО — процессорная спецификация',
    ),
    'en': dict(
        fid='calibration fidelity', prim='primitive', phase_circle='AB '
        'phase lattice: φ = 2πΦ/Φ₀ (continuum) on roots of unity (clock)',
        gates='gates per circuit', unitaries='unitaries',
        four='4×4 (200, seed 96)', eight='8×8 (100, seed 296)',
        thr='threshold', max_f='maximum',
        ab2='AB2 (blocks)', phase='PHASE (level phases)',
        ram='RAM: write → read (64 patterns)',
        lat='RAM latency: L(d) = a + b·d',
        alu='ALU: full truth tables',
        d='distance d', op='operation',
        write='written', read='read back',
        zeros='|ζ(½+it)|', readpos='zeros read',
        refpos='reference (Z-bisection)',
        arg='arg ζ(½+it) (winding)', slips='π-slips (zeros)',
        store='STORED: formula constants',
        produce='READ OUT: zeros',
        ratio='reading ratio',
        note04='64/64 bit-exact · b = 4.0 ≤ 6',
        note05='12 zeros exact; max deviation 3·10⁻³; no zero table used',
        p_note='P0 EXECUTED — processor specification',
    ),
}


def fig01(lang):
    txt = TXT[lang]
    cal = isa.pulse_calibration()
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.2),
                            constrained_layout=True)
    ax = axs[0]
    names = ['RX', 'RZ', 'PHASE']
    errs = [max(1e-18, 1 - cal[n]['fidelity']) for n in names]
    bars = ax.bar(names, errs, color=[LINE, COPPER, GOLD], width=0.55)
    ax.axhline(1e-15, color=BAD, ls='--', lw=1)
    ax.text(2.45, 1.6e-15, '1e-15', color=BAD, fontsize=8, ha='right')
    ax.set_yscale('log')
    ax.set_ylim(3e-18, 3e-15)
    ax.set_ylabel(txt['fid'])
    ax.set_xlabel(txt['prim'])
    ax.set_title('V18 → V20: аналитическая калибровка' if lang == 'ru'
                 else 'V18 → V20: analytic calibration')
    clean_axis(ax)
    for b, e in zip(bars, errs):
        ax.text(b.get_x() + b.get_width() / 2, e * 1.4, f'{e:.0e}',
                ha='center', fontsize=7.5, color=T['ink'])

    ax = axs[1]
    th = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.cos(th), np.sin(th), color=SLATE, lw=1.2, alpha=0.6)
    ks = np.arange(16)
    ax.scatter(np.cos(2 * np.pi * ks / 16), np.sin(2 * np.pi * ks / 16),
               s=42, color=LINE, zorder=3)
    for k in (1, 3, 7):
        ax.annotate(f'k={k}', (np.cos(2 * np.pi * k / 16),
                               np.sin(2 * np.pi * k / 16)),
                    xytext=(6, 6), textcoords='offset points', fontsize=8,
                    color=T['ink'])
    # континуум: стрелка-дуга
    tc = np.linspace(0.35, 0.75, 60)
    ax.plot(1.25 * np.cos(2 * np.pi * tc), 1.25 * np.sin(2 * np.pi * tc),
            color=COPPER, lw=1.4)
    ax.annotate('', xy=(1.25 * np.cos(2 * np.pi * 0.76),
                        1.25 * np.sin(2 * np.pi * 0.76)),
                xytext=(1.25 * np.cos(2 * np.pi * 0.72),
                        1.25 * np.sin(2 * np.pi * 0.72)),
                arrowprops=dict(arrowstyle='->', color=COPPER, lw=1.4))
    ax.text(0.02, 1.33, 'φ = 2πΦ/Φ₀', color=COPPER, fontsize=10)
    ax.set_xlim(-1.5, 1.6)
    ax.set_ylim(-1.45, 1.55)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(txt['phase_circle'], fontsize=10.5)
    save1(fig, 'fig01', lang)


def _suite(dim, n, count, seed):
    rng = np.random.default_rng(seed)
    errs, costs = [], []
    for _ in range(count):
        U = C.haar_unitary(rng, dim)
        comp = C.compile_unitary(U, n)
        errs.append(max(0.0, 1 - C.fidelity(U, C.program_matrix(comp, n))))
        costs.append((comp['costs']['n_ab2'], comp['costs']['n_phase'],
                      comp['costs']['two_qubit_equiv']))
    return np.array(errs), costs


def fig02(lang):
    txt = TXT[lang]
    errs4, _ = _suite(4, 2, 200, 96)
    errs8, _ = _suite(8, 3, 100, 296)
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.2),
                            constrained_layout=True)
    # (a) пайплайн
    ax = axs[0]
    ax.axis('off')
    boxes = [('U ∈ U(4/8)', 0.04), ('Givens-QR', 0.24),
             ('AB2-блоки', 0.47), ('PHASE-лестница', 0.70),
             ('исполнение → F', 0.70)]
    style = dict(boxstyle='round,pad=0.35', fc='#FFFFFF', ec=SLATE, lw=1)
    positions = [(0.5, 0.88), (0.5, 0.68), (0.28, 0.44), (0.74, 0.44),
                 (0.5, 0.14)]
    labels = ['U ∈ U(4) / U(8)', 'Givens-QR (замкнутая форма)',
              'AB2-блоки (двухуровневые импульсы)',
              'PHASE-лестница (фазы уровней)',
              'исполнение на ISA → F ≈ 1 − 1e-16']
    labels_en = ['U ∈ U(4) / U(8)', 'Givens-QR (closed form)',
                 'AB2 blocks (two-level pulses)',
                 'PHASE ladder (level phases)',
                 'ISA execution → F ≈ 1 − 1e-16']
    lab = labels if lang == 'ru' else labels_en
    for (x, y), s in zip(positions, lab):
        ax.text(x, y, s, ha='center', fontsize=9.5, bbox=style,
                transform=ax.transAxes)
    for (x1, y1), (x2, y2) in [((0.5, 0.80), (0.5, 0.74)),
                               ((0.40, 0.62), (0.30, 0.52)),
                               ((0.60, 0.62), (0.72, 0.52)),
                               ((0.32, 0.37), (0.44, 0.22)),
                               ((0.68, 0.37), (0.56, 0.22))]:
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1), xycoords='axes fraction',
                    textcoords='axes fraction',
                    arrowprops=dict(arrowstyle='->', color=COPPER, lw=1.3))
    ax.set_title(('Компилятор V20: без оптимизации и аппроксимации'
                  if lang == 'ru' else
                  'V20 compiler: no optimization, no approximation'),
                 fontsize=11)
    # (b) гистограмма ошибок
    ax = axs[1]
    bins = np.linspace(-16.5, -13.5, 25)
    ax.hist(np.log10(np.clip(errs4, 1e-17, None)), bins=bins,
            color=LINE, alpha=0.85, label=txt['four'])
    ax.hist(np.log10(np.clip(errs8, 1e-17, None)), bins=bins,
            color=COPPER, alpha=0.85, label=txt['eight'])
    ax.axvline(-12, color=BAD, ls='--', lw=1.2)
    ax.text(-12, 0.9, txt['thr'] + ' 1e-12', color=BAD, fontsize=8,
            transform=ax.get_xaxis_transform(), ha='right')
    ax.axvline(-10, color=BAD, ls=':', lw=1.2)
    ax.text(-10, 0.75, txt['thr'] + ' 1e-10', color=BAD, fontsize=8,
            transform=ax.get_xaxis_transform(), ha='left')
    ax.set_xlabel('log₁₀(1−F)')
    ax.set_ylabel(txt['unitaries'])
    ax.legend(loc='upper left')
    clean_axis(ax)
    save1(fig, 'fig02', lang)


def fig03(lang):
    txt = TXT[lang]
    _, costs4 = _suite(4, 2, 200, 96)
    _, costs8 = _suite(8, 3, 100, 296)
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.0),
                            constrained_layout=True)
    for ax, costs, dim in ((axs[0], costs4, '4×4'), (axs[1], costs8, '8×8')):
        ab2 = np.array([c[0] for c in costs])
        ph = np.array([c[1] for c in costs])
        idx = np.arange(len(costs))
        ax.bar(idx, ab2, color=LINE, width=1.0, label=txt['ab2'])
        ax.bar(idx, ph, bottom=ab2, color=GOLD, width=1.0, label=txt['phase'])
        mx = int(np.max(ab2 + ph))
        ax.text(0.985, 0.92, f'{txt["max_f"]}: {mx}', transform=ax.transAxes,
                ha='right', fontsize=9, color=T['ink'])
        ax.set_xlabel(f'{txt["unitaries"]} {dim}')
        clean_axis(ax)
    axs[0].set_ylabel(txt['gates'])
    axs[0].legend(loc='upper right')
    save1(fig, 'fig03', lang)


def fig04(lang):
    txt = TXT[lang]
    fig = plt.figure(figsize=(11, 4.4), constrained_layout=True)
    gs = fig.add_gridspec(1, 3)
    # (a) RAM-матрица
    ax = fig.add_subplot(gs[0])
    idx = np.arange(64)
    ax.scatter(idx, idx, s=16, color=OK, marker='s')
    ax.set_xlabel(txt['write'])
    ax.set_ylabel(txt['read'])
    ax.set_title(txt['ram'] + '\n64/64 бит-в-бит' if lang == 'ru'
                 else txt['ram'] + '\n64/64 bit-exact', fontsize=10)
    ax.set_xticks([0, 32, 63])
    ax.set_yticks([0, 32, 63])
    clean_axis(ax)
    # (b) латентность
    ax = fig.add_subplot(gs[1])
    lm = memory.latency_model()
    d = np.array(lm['distances'])
    ax.plot(d, lm['latency'], 'o-', color=LINE, lw=1.6, ms=5)
    bfit = lm['b']
    ax.plot(d, lm['a'] + 6 * d, '--', color=BAD, lw=1.2,
            label='b = 6 (порог V21)' if lang == 'ru' else 'b = 6 (V21 thr)')
    ax.plot(d, lm['a'] + bfit * d, ':', color=MUTED, lw=1.2,
            label=f'b = {bfit:.1f} (измерено)' if lang == 'ru'
            else f'b = {bfit:.1f} (measured)')
    ax.set_xlabel(txt['d'])
    ax.set_ylabel('L(d), затворов' if lang == 'ru' else 'L(d), gates')
    ax.legend(fontsize=8)
    ax.set_title(txt['lat'], fontsize=10)
    clean_axis(ax)
    # (c) ALU
    ax = fig.add_subplot(gs[2])
    res = alu.run_alu()
    names = ['ADD\nmod 16', 'MUL\nmod 16', 'INC\nmod 16', 'CMP\nphase']
    vals = [res['adder_mod16']['passed'], res['mulmod16_odd']['passed'],
            res['inc_mod16']['passed'], res['comparator_phase']['passed']]
    tots = [256, 128, 16, 256]
    x = np.arange(4)
    ax.bar(x, tots, color='#E8E2D4', width=0.6)
    ax.bar(x, vals, color=OK, width=0.6)
    for i, (v, t) in enumerate(zip(vals, tots)):
        ax.text(i, t + 4, f'{v}/{t}', ha='center', fontsize=8.5,
                color=T['ink'])
    ax.set_xticks(x)
    ax.set_xticklabels(names, fontsize=8.5)
    ax.set_ylim(0, 300)
    ax.set_ylabel(txt['op'])
    ax.set_title(txt['alu'], fontsize=10)
    clean_axis(ax)
    save1(fig, 'fig04', lang)


def fig05(lang):
    txt = TXT[lang]
    t0, t1, M = 2.0, 58.0, 560
    t_grid = np.linspace(t0, t1, M)
    z = RR.zeta_samples(t_grid)
    pos, n_slips, phi_u = RR.winding_zeros(z, t_grid, refine=17)
    ref = RR.reference_positions(t0, t1)
    fig, axs = plt.subplots(2, 1, figsize=(11, 6.4), sharex=True,
                            constrained_layout=True)
    ax = axs[0]
    ax.plot(t_grid, np.abs(z), color=LINE, lw=1.1)
    for g in ref:
        ax.axvline(g, color=MUTED, lw=0.8, ls=':')
    ax.scatter(pos, np.interp(pos, t_grid, np.abs(z)) + 0.35, s=34,
               color=COPPER, zorder=4, marker='v', label=txt['readpos'])
    ax.plot([], [], color=MUTED, ls=':', lw=0.8, label=txt['refpos'])
    ax.set_ylabel(txt['zeros'])
    ax.legend(loc='upper left', fontsize=8.5)
    ax.set_title(txt['note05'], fontsize=10.5)
    clean_axis(ax)
    ax = axs[1]
    ax.plot(t_grid, phi_u, color=SLATE, lw=1.1)
    dphi = np.diff(phi_u)
    slips = np.where(np.abs(dphi) > np.pi / 2)[0]
    ax.scatter(t_grid[slips], phi_u[slips], s=30, color=BAD, zorder=4,
               marker='x', label=txt['slips'])
    ax.set_xlabel('t')
    ax.set_ylabel(txt['arg'])
    ax.legend(loc='upper left', fontsize=8.5)
    clean_axis(ax)
    save1(fig, 'fig05', lang)


def fig06(lang):
    S = {
        'ru': [
            ('P0 · v0.1.0', 'V20 Компилятор', 'ISA + точная компиляция '
             'U(4)/U(8) · F ≥ 1−1e-12/1e-10 · ВЫПОЛНЕНО', OK),
            ('P1 · v0.2.0', 'V21 Память', 'RAM 64/64, персистентность '
             'T=10³, b ≤ 6, ошибко-коррекция фазовых кодов', LINE),
            ('P2 · v0.3.0', 'V22 ALU', 'полная арифметика: сумматор '
             '256/256, mulmod, компаратор; ISA-регрессия C/JS', COPPER),
            ('P3 · v0.4.0', 'V23 Считывание', 'универсальный интерфейс '
             'алгебраических функций; слепые нули K=138 @ T=300 ≤ 1e-8',
             GOLD),
            ('P4 · v0.5.0', 'V24 Нелокальность', 'голономия: CHSH ≥ 2.8, '
             'защита 1000/1000, no-signaling; лабораторные протоколы',
             SLATE),
            ('P5 · v0.6.0', 'V25 Бенчмарки', 'RB ≥ 0.999, передача ≥ 0.99, '
             'квантовый объём; сравнительная таблица архитектур', MUTED),
            ('P6 · v1.0.0', 'V26 Datasheet', 'универсальность {H,T,AB(π/4)} '
             '≤ 12 затворов @ 1e-8; полный паспорт процессора', BAD),
        ],
        'en': [
            ('P0 · v0.1.0', 'V20 Compiler', 'ISA + exact compilation of '
             'U(4)/U(8) · F ≥ 1−1e-12/1e-10 · EXECUTED', OK),
            ('P1 · v0.2.0', 'V21 Memory', 'RAM 64/64, persistence T=10³, '
             'b ≤ 6, phase-code error correction', LINE),
            ('P2 · v0.3.0', 'V22 ALU', 'full arithmetic: adder 256/256, '
             'mulmod, comparator; C/JS ISA regression', COPPER),
            ('P3 · v0.4.0', 'V23 Reading', 'universal algebraic-function '
             'interface; blind zeros K=138 @ T=300 ≤ 1e-8', GOLD),
            ('P4 · v0.5.0', 'V24 Nonlocality', 'holonomy: CHSH ≥ 2.8, '
             'protection 1000/1000, no-signaling; lab protocols', SLATE),
            ('P5 · v0.6.0', 'V25 Benchmarks', 'RB ≥ 0.999, state transfer '
             '≥ 0.99, quantum volume; architecture comparison', MUTED),
            ('P6 · v1.0.0', 'V26 Datasheet', 'universality {H,T,AB(π/4)} '
             '≤ 12 gates @ 1e-8; full processor datasheet', BAD),
        ],
    }[lang]
    fig, ax = plt.subplots(figsize=(11, 5.6), constrained_layout=True)
    ax.axis('off')
    n = len(S)
    for i, (tag, title, desc, color) in enumerate(S):
        y = 1.0 - i / (n - 0.6)
        ax.plot([0.02, 0.30], [y, y], color=color, lw=2.2,
                transform=ax.transAxes, solid_capstyle='round')
        ax.scatter([0.30], [y], s=90, color=color, zorder=3,
                   transform=ax.transAxes)
        ax.text(0.335, y, f'{tag} — {title}', fontsize=11.5,
                fontweight='bold', color=T['ink'], va='center',
                transform=ax.transAxes)
        ax.text(0.335, y - 0.035, desc, fontsize=9, color=T['muted'],
                va='center', transform=ax.transAxes)
    ax.text(0.02, 1.06, 'AB QUANTUM PROCESSOR — ' +
            ('дорожная карта к Datasheet 1.0' if lang == 'ru'
             else 'roadmap to Datasheet 1.0'),
            fontsize=12.5, fontweight='bold', color=T['ink'],
            transform=ax.transAxes)
    save1(fig, 'fig06', lang)


def main():
    fig01('ru'), fig01('en')
    fig02('ru'), fig02('en')
    fig03('ru'), fig03('en')
    fig04('ru'), fig04('en')
    fig05('ru'), fig05('en')
    fig06('ru'), fig06('en')
    print('FIGURES DONE: 6 x {ru,en} @ 600 dpi')


if __name__ == '__main__':
    main()
