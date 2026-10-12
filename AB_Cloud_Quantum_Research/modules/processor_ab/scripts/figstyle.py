"""scripts/figstyle.py — единый стиль серии «Critical Line & Copper».

Палитра и правила унаследованы от эталона Hilbert Polya Bridge; все подписи
двуязычны (ru/en). Никаких сторонних тем — только matplotlib.
"""
import matplotlib
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np

for _f in ('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
           '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'):
    try:
        fm.fontManager.addfont(_f)
    except Exception:  # noqa: BLE001
        pass

TOKENS = {
    'light': dict(bg='#FAF7F0', panel='#FFFFFF', ink='#1A1A24',
                  line='#0E7C86', copper='#C96F4A', slate='#3E515B',
                  muted='#6B6455', grid='#DDD6C8', ok='#3A6B4F',
                  bad='#8C3A2F', gold='#8C6D1F'),
    'dark': dict(bg='#10101A', panel='#181826', ink='#E8E4DA',
                 line='#4FB3BE', copper='#E08B66', slate='#8FA8B5',
                 muted='#9A938A', grid='#2A2A3A', ok='#6FBF8A',
                 bad='#D97B66', gold='#C9A85C'),
}

LANG = {
    'ru': {
        'fig01': ('V20 ISA: затворы AB-облака',
                  'fidelity калибровки / фазовая решётка',
                  'примитив · φ'),
        'fig02': ('V20 Компилятор: формула → ISA → точное исполнение',
                  'log₁₀(1−F) компиляции', 'унитарные (сид 96 / 296)'),
        'fig03': ('V20 Глубина и стоимость схем',
                  'число затворов AB2 + PHASE', 'унитарные'),
        'fig04': ('Память и ALU (превью P1/V22)',
                  'RAM / латентность / таблицы истинности',
                  'паттерн · d · операция'),
        'fig05': ('Считывание нулей с критической прямой (превью V23)',
                  '|ζ(½+it)| и фаза arg ζ', 't'),
        'fig06': ('Дорожная карта программы P0–P6', '', ''),
    },
    'en': {
        'fig01': ('V20 ISA: AB-cloud gates',
                  'calibration fidelity / phase lattice',
                  'primitive · φ'),
        'fig02': ('V20 Compiler: formula → ISA → exact execution',
                  'log₁₀(1−F) of compilation', 'unitaries (seed 96 / 296)'),
        'fig03': ('V20 Circuit depth and cost',
                  'AB2 + PHASE gate count', 'unitaries'),
        'fig04': ('Memory and ALU (P1/V22 preview)',
                  'RAM / latency / truth tables',
                  'pattern · d · operation'),
        'fig05': ('Reading zeros off the critical line (V23 preview)',
                  '|ζ(½+it)| and phase arg ζ', 't'),
        'fig06': ('Program roadmap P0–P6', '', ''),
    },
}


def apply(theme='light'):
    t = TOKENS[theme]
    matplotlib.rcParams.update({
        'figure.facecolor': t['bg'], 'axes.facecolor': t['panel'],
        'savefig.facecolor': t['bg'],
        'text.color': t['ink'], 'axes.edgecolor': t['muted'],
        'axes.labelcolor': t['ink'], 'xtick.color': t['muted'],
        'ytick.color': t['muted'],
        'axes.titlesize': 13, 'axes.titleweight': 'bold',
        'axes.labelsize': 10.5, 'xtick.labelsize': 9,
        'ytick.labelsize': 9, 'legend.fontsize': 9, 'legend.frameon': False,
        'axes.spines.top': False, 'axes.spines.right': False,
        'axes.grid': False, 'font.family': 'DejaVu Sans',
        'axes.unicode_minus': False,
    })
    return t


def clean_axis(ax, grid=True):
    ax.grid(True, axis='y', alpha=0.12, color=TOKENS['light']['grid'])
    if not grid:
        ax.grid(False)


def save_all(fig, stem, out_root, langs=('ru', 'en'), hires_dpi=600):
    """Сохраняет figures_hires/{lang}/{stem}_{lang}.png @600 dpi."""
    import os
    for lang in langs:
        d = os.path.join(out_root, 'figures_hires', lang)
        os.makedirs(d, exist_ok=True)
        fig.savefig(os.path.join(d, f'{stem}_{lang}.png'), dpi=hires_dpi)
    plt.close(fig)
