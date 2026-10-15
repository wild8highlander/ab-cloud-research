#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""scripts/make_infographics.py — 3 инфографики × ru/en × light/dark:
info_scorecard (вердикты 19 решений V1–V19), info_map (7 направлений A–G),
info_trace (теоремы Th1–Th6). Формат карточек — matplotlib (без браузера,
полная портируемость самосборки)."""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import matplotlib.pyplot as plt  # noqa: E402

import figstyle as FS  # noqa: E402

DATA = os.path.join(ROOT, 'data')


def _card(ax, x, y, w, h, title, body, verdict, ok, t):
    ax.add_patch(plt.Rectangle((x, y), w, h, facecolor=t['panel'],
                               edgecolor=t['grid'], lw=1.1))
    ax.add_patch(plt.Rectangle((x, y + h - 0.42), w, 0.42,
                               facecolor=t['slate'], alpha=0.9))
    ax.text(x + 0.14, y + h - 0.21, title, fontsize=8.6, color='white',
            va='center', fontweight='bold')
    ax.text(x + 0.14, y + h - 0.75, body, fontsize=7.4, color=t['ink'],
            va='top', wrap=True)
    ax.text(x + 0.14, y + 0.16, verdict, fontsize=8.6,
            color=t['ok'] if ok else t['bad'], fontweight='bold')


def info_scorecard(t, lang):
    L = {
     'ru': [('V1 Слепой спектр', 'r_test в нулевой зоне пермукаций (z = 0.09)',
             'ИЗМЕРЕНО'),
            ('V2 Null-модели', 'AB ∈ GUE-класс вместе с N1/N4; N3 вне класса',
             'ИЗМЕРЕНО'),
            ('V3 Скан σ', 'минимум D(σ) у ½ отсутствует/неустойчив',
             'ИЗМЕРЕНО'),
            ('V4 Паспорт T1', '‖H−H†‖ = 0; спектр вещественен', 'ДОКАЗАНО'),
            ('V5 Предел', 'e(L) ≈ L^{−0.86}, R² = 0.80', 'ИЗМЕРЕНО'),
            ('V6 Тождество', 'затворы: НЕТ; H_ξ: ДА (остаток 5.8e-10)',
             'ИЗМЕРЕНО'),
            ('V7 След T6', '|ΔK| ≤ 6.9e-6; PC0 r = +0.9996', 'ДОКАЗАНО'),
            ('V8 Самосопр. T2', 'дефекты (0,0); унитарность 1e-13', 'ДОКАЗАНО'),
            ('V9 Редукция T5', 'блоки ↔ спектр 7e-15; вихри ломают', 'ДОКАЗАНО'),
            ('V10 Обратная', 'восстановление зарядов ≤ 0.08; rank-limited',
             'ИЗМЕРЕНО'),
            ('V11 Универсальность', '⟨r⟩ выживает; r_EF — шум на окнах',
             'ИЗМЕРЕНО'),
            ('V12 Сертификаты T3', '5/5 интервалов содержат λ', 'ДОКАЗАНО'),
            ('V13 Формальный', 'RH: blocked (7 блокеров)', 'ИЗМЕРЕНО'),
            ('V14 Аудит', '19/19 claims по схеме', 'ИЗМЕРЕНО'),
            ('V15 Ли T4', 'λ_n = Tr g_n(H_ξ); λ_n > 0, n ≤ 3000', 'ДОКАЗАНО'),
            ('V16 Полный гамильтониан',
             'z_best = 2.49 < 6; тождество открыто; ПК r = 1.0', 'ИЗМЕРЕНО'),
            ('V17 Электрон', 'ζ-облако ×1.62; ΔE = 1.8e-15; r −0.96',
             'ИЗМЕРЕНО'),
            ('V18 AB-процессор',
             'ворота точны 1−2e-16; C = 0.984; Pong 0:1', 'ИЗМЕРЕНО'),
            ('V19 Сшивка ветвей', 'фазы 1e-40; монодромия 100%; z = 43.4',
             'ИЗМЕРЕНО'),
            ('Пакет · итог', 'V1–V19 · A–G · 6 доказано · 13 измерено',
             'АУДИТ 19/19')],
     'en': [('V1 Blind spectrum', 'r_test inside permutation null (z = 0.09)',
             'MEASURED'),
            ('V2 Null models', 'AB ∈ GUE class with N1/N4; N3 outside',
             'MEASURED'),
            ('V3 σ-scan', 'no stable minimum of D(σ) at ½', 'MEASURED'),
            ('V4 Passport T1', '‖H−H†‖ = 0; real spectrum', 'PROVEN'),
            ('V5 Limit', 'e(L) ≈ L^{−0.86}, R² = 0.80', 'MEASURED'),
            ('V6 Identity', 'gates: NO; H_ξ: YES (resid 5.8e-10)', 'MEASURED'),
            ('V7 Trace T6', '|ΔK| ≤ 6.9e-6; PC0 r = +0.9996', 'PROVEN'),
            ('V8 Self-adj T2', 'defects (0,0); unitarity 1e-13', 'PROVEN'),
            ('V9 Reduction T5', 'blocks ↔ spectrum 7e-15; vortices break',
             'PROVEN'),
            ('V10 Inverse', 'charge recovery ≤ 0.08; rank-limited',
             'MEASURED'),
            ('V11 Universality', '⟨r⟩ survives; r_EF noise-limited on windows',
             'MEASURED'),
            ('V12 Certificates T3', '5/5 intervals contain λ', 'PROVEN'),
            ('V13 Formal', 'RH: blocked (7 blockers)', 'MEASURED'),
            ('V14 Audit', '19/19 claims per schema', 'MEASURED'),
            ('V15 Li T4', 'λ_n = Tr g_n(H_ξ); λ_n > 0, n ≤ 3000', 'PROVEN'),
            ('V16 Full Hamiltonian',
             'z_best = 2.49 < 6; identity open; PC r = 1.0', 'MEASURED'),
            ('V17 Electron', 'ζ-cloud steers ×1.62; ΔE = 1.8e-15; r −0.96',
             'MEASURED'),
            ('V18 AB processor',
             'gates exact 1−2e-16; C = 0.984; Pong 0:1', 'MEASURED'),
            ('V19 Branch stitching', 'phases 1e-40; monodromy 100%; z = 43.4',
             'MEASURED'),
            ('Package · summary', 'V1–V19 · A–G · 6 proven · 13 measured',
             'AUDIT 19/19')],
    }[lang]
    fig, ax = plt.subplots(figsize=(17, 10.1), constrained_layout=True)
    ax.set_xlim(0, 17)
    ax.set_ylim(0, 10.1)
    ax.axis('off')
    ax.text(0.2, 9.62, 'AB RESEARCH PROGRAM · ' +
            ('Табель 19 решений' if lang == 'ru' else 'Scorecard of 19 solutions'),
            fontsize=15, fontweight='bold', color=t['ink'])
    for i, (title, body, verdict) in enumerate(L):
        col, row = i % 5, i // 5
        _card(ax, 0.2 + col * 3.36, 7.3 - row * 2.28, 3.16, 2.08,
              title, body, verdict,
              verdict in ('ДОКАЗАНО', 'PROVEN', 'АУДИТ 19/19', 'AUDIT 19/19'), t)
    return fig


def info_map(t, lang):
    ru = [('A Независимость', 'V1 слепой · V2 null · V3 скан σ'),
          ('B Спектральный объект', 'V4 паспорт · V5 предел · V6 тождество · V7 след · V8 самосопр.'),
          ('C Арифметика из спектра', 'V9 редукция · V10 обратная · V11 универсальность'),
          ('D Доказательства', 'V12 сертификаты · V13 формальный · V14 аудит'),
          ('E Критерии RH', 'V15 критерий Ли'),
          ('F Полный гамильтониан и вычислимость',
           'V16 карта ручек · V17 электрон · V18 процессор AB-Pong'),
          ('G Сшивка ветвей (R2)',
           'V19 монодромная склейка · Γ-фаза — сшитый объект')]
    en = [('A Independence', 'V1 blind · V2 nulls · V3 σ-scan'),
          ('B Spectral object', 'V4 passport · V5 limit · V6 identity · V7 trace · V8 self-adj'),
          ('C Arithmetic from spectrum', 'V9 reduction · V10 inverse · V11 universality'),
          ('D Proofs', 'V12 certificates · V13 formal · V14 audit'),
          ('E RH criteria', 'V15 Li criterion'),
          ('F Full Hamiltonian & computability',
           'V16 handle map · V17 electron · V18 AB-Pong processor'),
          ('G Branch stitching (R2)',
           'V19 monodromy stitching · the Γ-phase is the stitched object')]
    L = ru if lang == 'ru' else en
    fig, ax = plt.subplots(figsize=(17, 8.6), constrained_layout=True)
    ax.set_xlim(0, 17)
    ax.set_ylim(0, 8.6)
    ax.axis('off')
    ax.text(0.2, 8.15, 'AB RESEARCH PROGRAM · ' +
            ('Карта семи направлений' if lang == 'ru' else 'Map of seven directions'),
            fontsize=15, fontweight='bold', color=t['ink'])
    pos = [(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (1, 1), (2, 1)]
    W = 4.0
    for i, (title, body) in enumerate(L):
        col, row = pos[i]
        x = 0.2 + col * 4.2
        y = 4.4 - row * 3.9
        ax.add_patch(plt.Rectangle((x, y), W, 3.3, facecolor=t['panel'],
                                   edgecolor=t['grid'], lw=1.1))
        ax.add_patch(plt.Circle((x + 0.5, y + 2.7), 0.34, facecolor=t['copper']))
        ax.text(x + 0.5, y + 2.7, title.split()[0][0],
                ha='center', va='center', fontsize=11, color='white',
                fontweight='bold')
        ax.text(x + 0.16, y + 2.05, title, fontsize=9.6, color=t['ink'],
                fontweight='bold', va='top')
        ax.text(x + 0.16, y + 1.4, body, fontsize=7.6, color=t['muted'],
                va='top')
        if (row == 0 and col < 3) or (row == 1 and col < 2):
            ax.annotate('', xy=(x + W + 0.18, y + 1.6), xytext=(x + W, y + 1.6),
                        arrowprops=dict(arrowstyle='-|>', color=t['copper'],
                                        lw=1.6))
    return fig


def info_trace(t, lang):
    ru = [('Th1 Эрмитовость', 'spec H_L ⊂ ℝ; киральность W=0', 'V4'),
          ('Th2 Самосопряжённость', 'дефекты (0,0); BC-устойчивость', 'V8'),
          ('Th3 Сертификаты', 'Гершгорин + невязка ⊇ λ', 'V12'),
          ('Th4 Спектральная формула Ли', 'λ_n = Tr g_n(H_ξ)', 'V15'),
          ('Th5 Блочная редукция', 'spec H = ⊔ spec блоков', 'V9'),
          ('Th6 Следовая формула', 'K(x) = (1/π)∫Q(a)sin(ax)da', 'V7')]
    en = [('Th1 Hermiticity', 'spec H_L ⊂ ℝ; chirality W=0', 'V4'),
          ('Th2 Self-adjointness', 'defects (0,0); BC-stability', 'V8'),
          ('Th3 Certificates', 'Gershgorin + residual ⊇ λ', 'V12'),
          ('Th4 Li spectral formula', 'λ_n = Tr g_n(H_ξ)', 'V15'),
          ('Th5 Block reduction', 'spec H = ⊔ spec blocks', 'V9'),
          ('Th6 Trace formula', 'K(x) = (1/π)∫Q(a)sin(ax)da', 'V7')]
    L = ru if lang == 'ru' else en
    fig, ax = plt.subplots(figsize=(17, 3.8), constrained_layout=True)
    ax.set_xlim(0, 17)
    ax.set_ylim(0, 3.8)
    ax.axis('off')
    ax.text(0.2, 3.35, 'AB RESEARCH PROGRAM · ' +
            ('Теоремы пакета' if lang == 'ru' else 'Package theorems'),
            fontsize=15, fontweight='bold', color=t['ink'])
    for i, (title, body, src) in enumerate(L):
        x = 0.2 + i * 2.8
        _card(ax, x, 0.35, 2.6, 2.55, title, body,
              ('доказано · ' if lang == 'ru' else 'proven · ') + src, True, t)
    return fig


BUILDERS = {'info_scorecard': info_scorecard, 'info_map': info_map,
            'info_trace': info_trace}


def main():
    for theme in ('light', 'dark'):
        t = FS.apply(theme)
        for name, fn in BUILDERS.items():
            for lang in ('ru', 'en'):
                fig = fn(t, lang)
                d = os.path.join(ROOT, 'figures', lang, theme)
                os.makedirs(d, exist_ok=True)
                fig.savefig(os.path.join(d, f'{name}_{lang}.png'), dpi=300)
                plt.close(fig)
            print(name, theme, 'OK')
    print('INFOGRAPHICS DONE')


if __name__ == '__main__':
    main()
