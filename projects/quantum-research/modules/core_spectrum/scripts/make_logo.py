#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""scripts/make_logo.py — эмблема пакета (критическая полоса + нули + арка
+ спектральная лестница) в темах light/dark, PNG @600dpi + SVG."""
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyArrowPatch  # noqa: E402

import figstyle as FS  # noqa: E402

ZEROS = (14.1347251, 21.0220396, 25.0108576, 30.4248761, 32.9350616,
         37.5861782, 40.9187190, 43.3270733, 48.0051509, 49.7738325)


def build(theme):
    t = FS.apply(theme)
    fig = plt.figure(figsize=(9.6, 3.6), constrained_layout=True)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 96)
    ax.set_ylim(0, 36)
    ax.axis('off')
    # критическая полоса
    ax.add_patch(plt.Rectangle((3, 6), 26, 24, facecolor=t['panel'],
                               edgecolor=t['grid'], lw=1.2))
    ax.plot([16, 16], [7, 29], color=t['line'], lw=2.0)
    ax.text(16, 31.2, 'Re s = 1/2', ha='center', fontsize=9,
            color=t['line'], fontweight='bold')
    for k, g in enumerate(ZEROS):
        y = 7 + 22 * (k / (len(ZEROS) - 1))
        ax.plot([16], [y], 'o', ms=5, color=t['copper'])
        ax.plot([16], [36 - y], 'o', ms=5, color=t['copper'], alpha=0.35)
    ax.text(16, 3.8, 'ξ(1/2+it)', ha='center', fontsize=9, color=t['muted'])
    # арка
    arr = FancyArrowPatch((30.5, 22), (60.5, 22), connectionstyle='arc3,rad=-0.26',
                          arrowstyle='-|>', mutation_scale=16, lw=1.6,
                          color=t['copper'])
    ax.add_patch(arr)
    ax.text(45.5, 30.4, 'Tr e$^{-uH}$ = (1/π)∫ Q(a)·sin(ua) da',
            ha='center', fontsize=9.5, color=t['ink'])
    ax.text(45.5, 27.0, 'ξ(1/2+it)  ↔  spec H', ha='center', fontsize=9,
            color=t['muted'])
    # спектральная лестница
    ax.add_patch(plt.Rectangle((62, 6), 31, 24, facecolor=t['panel'],
                               edgecolor=t['grid'], lw=1.2))
    rng = np.random.default_rng(96)
    for k in range(6):
        x0 = 64 + 5 * k
        h = 3 + 3.4 * rng.random()
        ax.add_patch(plt.Rectangle((x0, 8), 3.6, h, facecolor=t['slate'],
                                   alpha=0.55))
        ax.plot([x0 + 1.8], [8 + h + 1.2], 'o', ms=4, color=t['copper'])
    ax.text(77.5, 3.8, 'spec H (gates V1–V15)', ha='center', fontsize=9,
            color=t['muted'])
    ax.text(2.5, 33.6, 'AB RESEARCH PROGRAM · v1.0.0', fontsize=10.5,
            color=t['ink'], fontweight='bold')
    return fig


def main():
    for theme in ('light', 'dark'):
        fig = build(theme)
        d = os.path.join(ROOT, 'figures', 'logo')
        os.makedirs(d, exist_ok=True)
        fig.savefig(os.path.join(d, f'arp_logo_{theme}.png'), dpi=600)
        fig.savefig(os.path.join(d, f'arp_logo_{theme}.svg'))
        plt.close(fig)
        print('logo', theme, 'OK')


if __name__ == '__main__':
    main()
