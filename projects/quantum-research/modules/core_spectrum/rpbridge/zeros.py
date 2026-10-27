"""rpbridge.zeros — нули дзета: загрузка, гладкий счёт, слепые разбиения.

Единственный внешний файл данных — стандартная таблица Одлыжко
(data/zeta_zeros_50000_embedded.txt, 50 000 высот, SHA-256 в data/README.md).
Никакой сторонний исследовательский код не используется.
"""
import hashlib
import os

import numpy as np

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZFILE = os.path.join(REPO, 'data', 'zeta_zeros_50000_embedded.txt')


def load_zeros(path=None, nmax=None):
    """Высоты нулей ζ (γ>0), формат Одлыжко: один столбец, # — комментарии."""
    z = np.loadtxt(path or ZFILE, dtype=float)
    z = np.sort(z[z > 0])
    return z if nmax is None else z[:nmax]


def rvm_count(g):
    """Гладкий счёт Римана–фон Мангольдта N̄(γ) = γ/2π·ln(γ/2πe) + 5/8."""
    g = np.asarray(g, dtype=float)
    return g / (2 * np.pi) * np.log(g / (2 * np.pi * np.e)) + 0.625


def blind_split(zeros, n_cal, n_test, salt='ARP-v1'):
    """Слепое разбиение V1: G = G_cal ⊔ G_test, без общих ординат.

    Разбиение детерминировано (чётные/нечётные индексы после перемешивания
    с фиксированным salt) и фиксируется SHA-256 дайджестом обеих частей —
    параметризация не может «подглядывать» в контрольную часть.
    """
    z = np.asarray(zeros[:n_cal + n_test], dtype=float)
    h = hashlib.sha256((salt + str(len(z))).encode()).digest()
    perm = np.random.default_rng(int.from_bytes(h[:8], 'little'))
    idx = perm.permutation(z.size)
    cal = np.sort(z[idx[:n_cal]])
    test = np.sort(z[idx[n_cal:n_cal + n_test]])
    dig = (hashlib.sha256(cal.tobytes()).hexdigest()[:16],
           hashlib.sha256(test.tobytes()).hexdigest()[:16])
    return cal, test, dig


def gram_points_ref(n_points=220):
    """Эталонные точки Грама через mpmath (используется как позитив-контроль)."""
    import mpmath as mp
    out, n = [], 0
    while len(out) < n_points:
        g = mp.findroot(lambda t: mp.im(mp.log(
            mp.gamma(mp.mpf('0.25') + 1j * t / 2)))
            - t * mp.log(mp.pi) / 2 - mp.pi * n,
            (n * mp.pi / mp.log(mp.mpf(n + 10)) * 8,))
        out.append(float(g))
        n += 1
    return np.array(out)
