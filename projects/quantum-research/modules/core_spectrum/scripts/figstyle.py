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
        'fig01': ('V1 Слепой контроль', 'ранговая корреляция', 'нулевая зона (пермукации)'),
        'fig02': ('V2 Контрольные модели', '⟨r⟩ по моделям', 'D_KS к GUE'),
        'fig03': ('V3 Скан критической линии', 'D_KS(σ) к GUE', 'σ'),
        'fig04': ('V4 Паспорт оператора', 'невязки паспорта', 'конфигурация'),
        'fig05': ('V5 Предел решётки', 'ошибка следа e(L)', 'L'),
        'fig06': ('V6 Спектральное тождество', 'log₁₀ остатка', 'объект'),
        'fig07': ('V7 Следовая формула', 'K(x) = Tr e^{−xH}', 'x'),
        'fig08': ('V8 Самосопряжённость', 'сдвиг спектра при смене BC', 'BC-семейство'),
        'fig09': ('V9 Симметрийная редукция', '‖[U_g,H]‖ и блоки', 'проверка'),
        'fig10': ('V10 Обратная задача', 'сингулярные числа J', 'индекс'),
        'fig11': ('V11 Универсальность', '⟨r⟩ по режимам', 'режим'),
        'fig12': ('V12 Сертификаты', 'ширина интервала', 'уровень'),
        'fig13': ('V13 Формальный мост', 'статусы обязательств', 'статус'),
        'fig14': ('V14 Аудит утверждений', 'статусы claims', 'статус'),
        'fig15': ('V15 Критерий Ли', 'λ_n', 'n'),
        'fig16': ('Карта программы', '19 решений', ''),
        'fig17': ('V16 Полный гамильтониан × алгебраическая функция',
                  'r_align (выравнивание с нулями ζ)', 'конфигурация ручек'),
        'fig18': ('V17 Электрон на критической прямой',
                  '⟨x(t)⟩, транзит, когерентность', 't'),
        'fig19': ('V18 AB-оператор как процессор',
                  'верность ворот / мяч AB-Pong / concurrence',
                  'ворота · t · t'),
        'fig20': ('V19 Сшивка ветвей алгебраической функции',
                  'концентрация Δθ / знаковая когерентность / фазы тора',
                  'k · k · (r, s)'),
    },
    'en': {
        'fig01': ('V1 Blind protocol', 'rank correlation', 'null zone (permutations)'),
        'fig02': ('V2 Null models', '⟨r⟩ by model', 'D_KS to GUE'),
        'fig03': ('V3 Critical line scan', 'D_KS(σ) to GUE', 'σ'),
        'fig04': ('V4 Operator passport', 'passport residuals', 'configuration'),
        'fig05': ('V5 Lattice limit', 'trace error e(L)', 'L'),
        'fig06': ('V6 Spectral identity', 'log₁₀ residual', 'object'),
        'fig07': ('V7 Trace formula', 'K(x) = Tr e^{−xH}', 'x'),
        'fig08': ('V8 Self-adjointness', 'spectrum shift under BC change', 'BC family'),
        'fig09': ('V9 Symmetry reduction', '‖[U_g,H]‖ and blocks', 'check'),
        'fig10': ('V10 Inverse problem', 'singular values of J', 'index'),
        'fig11': ('V11 Universality', '⟨r⟩ by mode', 'mode'),
        'fig12': ('V12 Certificates', 'interval width', 'level'),
        'fig13': ('V13 Formal bridge', 'obligation statuses', 'status'),
        'fig14': ('V14 Claim audit', 'claim statuses', 'status'),
        'fig15': ('V15 Li criterion', 'λ_n', 'n'),
        'fig16': ('Program map', '19 solutions', ''),
        'fig17': ('V16 Full Hamiltonian x algebraic function',
                  'r_align (alignment with ζ zeros)', 'handle configuration'),
        'fig18': ('V17 Electron on the critical line',
                  '⟨x(t)⟩, transit, coherence', 't'),
        'fig19': ('V18 AB operator as processor',
                  'gate fidelity / AB-Pong ball / concurrence',
                  'gates · t · t'),
        'fig20': ('V19 Branch stitching of the algebraic function',
                  'Δθ concentration / sign coherence / torus phases',
                  'k · k · (r, s)'),
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
