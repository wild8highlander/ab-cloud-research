"""hpbridge.primes — простая сторона: решето Λ(n), гребёнка P(u),
ψ-лестница фон Мангольдта (кампания C6)."""
import numpy as np

from engine.solver import sieve_lambda


def lambda_arrays(nmax=2_000_000):
    """(n, Λ(n)) только для носителей."""
    lam, _ = sieve_lambda(nmax)
    ns = np.arange(2, nmax + 1)
    lm = lam[2:]
    m = lm > 0
    return ns[m], lm[m]


def prime_comb(u, ns_l, lm_l):
    """P(u) = Σ Λ(n)/√n · u/(u²+ln²n) — «вес простых» в следовой формуле."""
    lnn = np.log(ns_l.astype(np.float64))
    w = lm_l / np.sqrt(ns_l.astype(np.float64))
    return float(np.sum(w * u / (u * u + lnn * lnn)))


def psi_sieve(xmax=10 ** 6):
    """ψ(x) = Σ_{p^k ≤ x} ln p — ситовая лестница (для C6/M2)."""
    lam, _ = sieve_lambda(xmax)
    cdf = np.cumsum(lam)
    return cdf  # cdf[n] = ψ(n)


def psi_zeros_reference(x, zeros, k_max=200):
    """ψ_ζ(x) = x − √x·Σ_{k≤K} e^{iγ_k ln x}/(½+iγ_k) − ln 2π − ½ln(1−x⁻²) —
    эталонная лестница по первым K нулям (протокол C6/M2)."""
    x = np.asarray(x, dtype=float)
    g = np.asarray(zeros[:k_max], dtype=complex)
    psi = x.astype(np.float64).copy()
    for xi in np.atleast_1d(x):
        s = np.sum(np.exp(1j * g * np.log(xi)) / (0.5 + 1j * g))
        psi_val = xi - np.sqrt(xi) * s.real - np.log(2 * np.pi) \
            - 0.5 * np.log(1 - xi ** -2)
        psi[np.atleast_1d(x) == xi] = psi_val
    return psi


def flow_phi(p):
    """Поток простого Φ_p = ½·ln p (кампания C6/M1: ко-локация
    (Φ_p, Φ_q) ≡ Φ_pq с max|ΔE| = 1.35e-14)."""
    return 0.5 * np.log(np.asarray(p, dtype=float))
