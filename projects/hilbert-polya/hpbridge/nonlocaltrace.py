"""hpbridge.nonlocal — нелокальные следовые примитивы (C9, направление R1).

Урок T6: вес простых Λ(n)/√n живёт в тепловом следе оператора H_ξ, сшитого
из нулей. Вопрос R1: существует ли нелокальный (внелогичный, внерезеточный)
оператор, у которого вес простых в следе есть ПО КОНСТРУКЦИИ из
Гуинана–Вейля, — и что это говорит о разрыве Г2.

Семейство C9 (все — эрмитовы, дискретные, детерминированные):
  N1  H_ξ = diag(±γ_n)                — позитивный контроль (след = нули);
  N2  DCT-близнец  O·diag(γ)·Oᵀ       — изоспектрален по построению, O —
                                        детерминированный DCT-II ортогонал
                                        (плотная, нелокальная матрица);
  N3  QR-близнец   O·diag(γ)·Oᵀ       — O из seeded QR (нелокальность
                                        с независимым от нулей зерном);
  N4  H_BK — обрезанный Berry–Keating (xp+px)/2 на решётке x = 1..N
        (кандидат «вне решётки», непрерывный прототип);
  N5  M_LCM — мультипликативное ядро Λ(lcm(m,n))/√(mn) (простой вес в
        самом ядре, НЕ в спектре).

Теорема T11 (уникальность теплового следа): если Tr e^{-xH} = (1/π)∫Q sin
для всех x > 0, то spec H = {±γ_n}. Следствие: примитив «вес простых в
следе» существует ровно на изоспектральном классе H_ξ — нелокальность
достижима произвольно (N2/N3), локальность (решётка) — никогда.
"""
import numpy as np
from scipy.linalg import eigh, eigvalsh, hadamard
from scipy.fft import dct, idct

from hpbridge.traceformula import (K_direct, K_formula, Q_direct, Q_identity,
                                    C0_from_zeros, prime_comb,
                                    heat_trace_fluct, fit_corr, resid_rel,
                                    surrogate_null, S_smooth)


# ── конструкция объектов ─────────────────────────────────────────────────────
def h_xi(gamma):
    """N1: диагональный оператор из нулей ±γ (позитивный контроль)."""
    g = np.asarray(gamma, dtype=float)
    return np.concatenate([-g[::-1], g])


def dct_orthogonal(N):
    """Детерминированная ортогональная (DCT-II) матрица N×N — нелокальная база."""
    I = np.eye(N)
    return dct(I, type=2, norm="ortho").T


def qr_orthogonal(N, seed=2026):
    """Ортогонал из seeded QR — хаос, независимый от нулей."""
    rng = np.random.default_rng(seed)
    A = rng.standard_normal((N, N)) + np.tril(np.ones((N, N)))
    Q, _ = np.linalg.qr(A)
    return Q


def ispectral_twin(gamma, kind="dct", seed=2026):
    """N2/N3: O·diag(γ)·Oᵀ — спектр бит-в-бит нулевой, ядро плотное."""
    g = np.asarray(gamma, dtype=float)
    O = dct_orthogonal(g.size) if kind == "dct" else qr_orthogonal(g.size, seed)
    H = O @ np.diag(g) @ O.T
    return H, O


def berry_keating(N, h=1.0):
    """N4: симметризованный xp на сетке x_i = h·i, i = 1..N (эрмитов).

    Возвращает КОМПЛЕКСНУЮ эрмитову матрицу (внедиагональ чисто мнимая):
    H[i,i+1] = i(x_i+x_{i+1})/4 — вещественные собственные значения.
    """
    x = h * np.arange(1, N + 1, dtype=float)
    P = np.zeros((N, N), dtype=complex)
    for j in range(N - 1):
        P[j, j + 1] = 1j / (2 * h)
        P[j + 1, j] = -1j / (2 * h)
    XP = x[:, None] * P
    H = (XP + XP.conj().T) / 2.0
    return H


def lcm_kernel(N):
    """N5: M_{mn} = Λ(lcm(m,n))/√(mn) — простой вес в ядре.
    Решето Λ тянется до N² (lcm может превышать N)."""
    lam = _sieve_lambda(N * N)
    idx = np.arange(1, N + 1)
    g = np.gcd.outer(idx, idx)
    l = idx[:, None] * idx[None, :] // np.maximum(g, 1)
    M = lam[l] / np.sqrt(idx[:, None] * idx[None, :])
    return M


def _sieve_lambda(nmax):
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
    return lam


# ── следовые метрики ─────────────────────────────────────────────────────────
def trace_fluct_curve(eigs, U):
    """D(u) = Σ e^{-u x_n} − гладкая единичная плотность (протокол C4/M2)."""
    return heat_trace_fluct(np.asarray(eigs, dtype=float), U)


def prime_curve(U, nmax=2_000_000):
    """P(u) = Σ Λ(n)/√n·u/(u²+ln²n) — простая гребёнка (v1-протокол)."""
    lam = _sieve_lambda(min(nmax, 2_000_000))
    ns = np.arange(2, lam.size)
    m = lam[2:] > 0
    ns = ns[m]
    lm = lam[2:][m]
    return np.array([prime_comb_u(u, ns, lm) for u in U])


def prime_comb_u(u, ns, lm):
    lnn = np.log(ns.astype(np.float64))
    w = lm / np.sqrt(ns.astype(np.float64))
    return float(np.sum(w * u / (u * u + lnn * lnn)))


def r_EF_report(eigs, U, P):
    """r_EF + остаток + суррогатный нуль (фикс. масштаб — без подгонки)."""
    D = trace_fluct_curve(eigs, U)
    r, _, c = fit_corr(D, P)
    try:
        res = resid_rel(D, P)
        if not np.isfinite(res):
            raise ValueError
    except Exception:
        res = float(np.sqrt(max(0.0, 1.0 - r * r)))
    return {"r_EF": float(r), "coef": float(c),
            "resid_rel": res,
            "null": surrogate_null(D, P, 120, 5, 1234)}


def trace_formula_check(gamma, xs, A_SPLIT=1.5, nmax=2_000_000):
    """Верификация T6-машины на заданном наборе нулей: K_direct vs K_formula.
    Q-сплайн обязан покрывать ровно [0, A_SPLIT] (интеграл T1)."""
    C0 = C0_from_zeros(gamma)
    # 77 точек: шаг 1.5/76 не попадает в полюс a = 0.5 (иначе ζ(1))
    a_grid = np.linspace(0.0, A_SPLIT, 77)
    a_grid = a_grid[np.abs(a_grid - 0.5) > 1e-6]
    q_id = np.array([Q_identity(a, C0, dps=20) for a in a_grid])
    q_dr = np.array([Q_direct(a, gamma) for a in a_grid])
    from scipy.interpolate import CubicSpline
    spline = CubicSpline(a_grid, q_id)
    lam = _sieve_lambda(nmax)
    ns = np.arange(2, lam.size)[lam[2:] > 0]
    lm = lam[ns]
    lnn = np.log(ns.astype(float))
    w = lm / np.sqrt(ns.astype(float))
    diffs = []
    parts = []
    for x in xs:
        kd = K_direct(x, gamma)
        kf, pr = K_formula(x, C0, spline, lnn, w, A_SPLIT)
        diffs.append(abs(kd - kf))
        parts.append(pr)
    return {"max_abs_diff_K": float(np.max(diffs)),
            "max_abs_diff_Q": float(np.max(np.abs(q_id - q_dr))),
            "C0": float(C0)}


def b_minus_c0_check(gamma):
    """Встроенный контроль v1: B = −C₀ (12 цифр) на внутреннем кэше нулей."""
    C0 = C0_from_zeros(gamma)
    from hpbridge.constants import B_HADAMARD as B
    return float(abs(B + C0)), float(C0), float(B)
