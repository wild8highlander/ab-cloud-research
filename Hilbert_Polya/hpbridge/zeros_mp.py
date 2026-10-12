"""hpbridge.zeros_mp — внутренний источник нулей дзеты (v2.0).

Дисциплина честности v2: пакет не зависит НИ ОТ ОДНОГО внешнего файла данных.
Нули вычисляются mpmath.zetazero внутри пакета и кэшируются в data/zeros/.
Файл нулей Одлыжко в v2 не используется ни одной кампанией; закоммиченный
кэш воспроизводим побитово (версия mpmath фиксируется в вердиктах).
"""
import os
import mpmath as mp
import numpy as np

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZDIR = os.path.join(REPO, "data", "zeros")
ZETA_DPS = 25          # точность вычисления нулей
MPMATH_VERSION = mp.__version__


def compute_zeros(nmax, dps=ZETA_DPS):
    """Первые nmax положительных ординат нулей ζ, mpmath.zetazero."""
    mp.mp.dps = dps
    out = np.empty(nmax, dtype=float)
    for n in range(1, nmax + 1):
        z = mp.zetazero(n)
        out[n - 1] = float(mp.im(z))
    return out


def cache_path(nmax):
    return os.path.join(ZDIR, f"zeros_mpmath_n{nmax}.npz")


def ensure_zeros(nmax=800, dps=ZETA_DPS, force=False):
    """Загрузить кэш или вычислить и закоммитить (идемпотентно)."""
    os.makedirs(ZDIR, exist_ok=True)
    p = cache_path(nmax)
    if os.path.exists(p) and not force:
        d = np.load(p)
        if int(d["nmax"]) >= nmax and d["dps"] == dps:
            return d["gamma"][:nmax]
    gamma = compute_zeros(nmax, dps)
    np.savez(p, gamma=gamma, nmax=nmax, dps=dps,
             mpmath=MPMATH_VERSION)
    return gamma


def zero_index_above(gamma, height):
    """Индекс первого нуля выше height."""
    return int(np.searchsorted(gamma, height))


def zid_zeros_reference(gamma, k0, k):
    """Окно k нулей, приведённое к началу отсчёта (γ_{k0+1} → 0)."""
    w = np.asarray(gamma[k0:k0 + k], dtype=float)
    return w - w[0]
