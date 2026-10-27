"""engine.solver — спектральный конвейер затворов: конфигурация → спектр →
развёртка → окно; GUE-нуль; нули ζ и гладкий счёт Римана–фон Мангольдта;
решето функции фон Мангольдта."""
from engine.hamiltonian import (  # noqa: F401
    BASE_SEED, HARDCORE_OFFSET, T_HOP, CENTER_FRACTION, MIN_DIST,
    random_vortex_configuration, build_hamiltonian, central_band,
    unfold_poly, window_u, gate_spectrum)

import numpy as np
from scipy.linalg import eigvalsh


def load_zeros(path, nmax=None):
    """Высоты нулей ζ (γ>0), Odlyzko-формат: один столбец."""
    z = np.loadtxt(path, dtype=float)
    z = np.sort(z[z > 0])
    return z if nmax is None else z[:nmax]


def rvm_count(g):
    """Гладкий счёт Римана–фон Мангольдта N̄(γ) = γ/2π·ln(γ/2πe) + 5/8."""
    g = np.asarray(g, dtype=float)
    return g / (2 * np.pi) * np.log(g / (2 * np.pi * np.e)) + 0.625


def gue_spectrum(n=576, seed=0):
    """GUE-нуль: (X+X†)/2, X комплексный гауссовский."""
    rng = np.random.default_rng(9000 + seed)
    X = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    return np.sort(eigvalsh((X + X.conj().T) / 2, check_finite=False,
                            driver='evr'))


def sieve_lambda(nmax):
    """Λ(n) — решето наименьшего простого делителя. Возвращает (lam, primes)."""
    spf = np.zeros(nmax + 1, dtype=np.int64)
    primes = []
    for i in range(2, nmax + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
        for p in primes:
            if p > spf[i] or i * p > nmax:
                break
            spf[i * p] = p
    lam = np.zeros(nmax + 1)
    for p in primes:
        pk = p
        while pk <= nmax:
            lam[pk] = np.log(p)
            pk *= p
    return lam, np.array(primes, dtype=np.int64)
