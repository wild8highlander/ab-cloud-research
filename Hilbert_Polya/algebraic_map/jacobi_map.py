# -*- coding: utf-8 -*-
"""jacobi_map.py — алгебраическая функция якобиевой кодировки Hilbert_Polya.

Кодировка из video/pixel_decoding.py (Appendix H.8):
    нули γ_1..γ_N и веса w_n ∝ 1/|ζ'(ρ_n)|
    -> Ланцош на diag(γ), стартовый вектор v = w/||w||, полное реортогонализация
    -> трёхдиагональная J = tridiag(β, α, β)
    -> 87 гейтов -> канва 25×25 RGBA (Q22, 30-битный мантисс + знак).

Этот модуль поднимает ту же карту до АЛГЕБРАИЧЕСКОЙ функции Φ:

    Φ: (t_1..t_N; ν_1..ν_N)  ↦  (α_0..α_{N-1}; β_1..β_{N-1})

    μ_k = Σ_i ν_i t_i^k                          (моменты меры)
    D_n  = det(μ_{i+j})_{i,j=0}^{n-1},  D_0 = 1   (определители Ханкеля)
    Dˆ_n = det(μ_{i+j+1})_{i,j=0}^{n-1}, Dˆ_0 = 1  (сдвинутые определители)

    α_0  = Dˆ_1 / D_1 = μ_1/μ_0
    α_n  = Dˆ_{n+1}/D_{n+1} − Dˆ_n/D_n             (n ≥ 1)
    β_n² = D_{n+1}·D_{n-1} / D_n²                  (n ≥ 1)

Φ рациональна по моментам (значит, рациональна по (t, ν)); β_n = √(β_n²) —
единственный радикал. Ланцош — лишь численный алгоритм вычисления Φ;
декодирование (рекуррентность трёхчлена + бисекция) — обратная ветвь Φ⁻¹.

Здесь реализованы две независимые вычислительные ветви Φ:
  1) последовательное ортогонализационное построение (стиль Стилтьеса) —
     только скалярные произведения явно выписанных многочленов;
  2) формулы через определители Ханкеля (классика: Стилтьес/Грам,
     см. Szegő 1939; Golub–Meurant 2010; Deift 1999).
Совпадение (1) и (2) в точной арифметике = доказательство формул (2).

Обратная задача: p_{n+1}(λ) = (λ−α_n)p_n(λ) − β_n² p_{n-1}(λ), p_N —
характеристический многочлен J, его корни — исходные узлы t_i; коэффициенты
p_N суть элементарные симметрические многочлены узлов (тождества Ньютона).

Все конструкции существуют в float- и в ТОЧНОЙ рациональной версии
(fractions.Fraction); точная ветвь позволяет доказывать тождества на реальных
данных без округлений (см. run_verification.py).
"""
from fractions import Fraction
from math import lcm
import numpy as np

# --- параметры квантования канвы (как в pixel_decoding.py) -------------------
Q_EXP = 22
SCALE = 1 << Q_EXP          # v = X * 2^-22
LIMIT = (1 << 30) - 1       # 30-битный мантисс + знаковый бит


def frac(x):
    """Точная двоичная рационализация float (Fraction(float) точен)."""
    return x if isinstance(x, Fraction) else Fraction(x)


# =============================================================================
# 1. Моменты
# =============================================================================
def moments(t, nu, kmax, exact=False):
    """μ_k = Σ_i ν_i t_i^k, k = 0..kmax.

    exact=False -> np.ndarray (float); exact=True -> list[Fraction].
    ν_i — МЕРЫ атомов (в кодировке это ν_i = w_i²/Σw_j², квадрат
    нормированного вектора весов, т.к. стартовый вектор Ланцоша = w/||w||).
    """
    if exact:
        t = [frac(x) for x in t]
        nu = [frac(x) for x in nu]
        pw = [Fraction(1)] * len(t)
        out = []
        for _ in range(kmax + 1):
            s = Fraction(0)
            for i in range(len(t)):
                s += nu[i] * pw[i]
            out.append(s)
            pw = [pw[i] * t[i] for i in range(len(t))]
        return out
    t = np.asarray(t, dtype=float)
    nu = np.asarray(nu, dtype=float)
    out = np.empty(kmax + 1)
    pw = np.ones_like(t)
    for k in range(kmax + 1):
        out[k] = float(nu @ pw)
        pw = pw * t
    return out


def masses_from_weights(w, exact=False):
    """Меры атомов ν_i = w_i²/Σ w_j² (стартовый вектор Ланцоша v = w/||w||)."""
    if exact:
        w = [frac(x) for x in w]
        s = sum((x * x for x in w), Fraction(0))
        return [x * x / s for x in w]
    w = np.asarray(w, dtype=float)
    return (w * w) / np.sum(w * w)


# =============================================================================
# 2. Точный линейный базис: определители рациональных матриц
# =============================================================================
def _bareiss_int(A):
    """Точный определитель целочисленной матрицы (Bareiss, дробь-свободно)."""
    n = len(A)
    A = [row[:] for row in A]
    sign = 1
    prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            for r in range(k + 1, n):
                if A[r][k] != 0:
                    A[k], A[r] = A[r], A[k]
                    sign = -sign
                    break
            else:
                return 0
        pivot = A[k][k]
        for i in range(k + 1, n):
            aik = A[i][k]
            row_i = A[i]
            row_k = A[k]
            for j in range(k + 1, n):
                row_i[j] = (row_i[j] * pivot - aik * row_k[j]) // prev
            row_i[k] = 0
        prev = pivot
    return sign * A[-1][-1]


def det_frac(M):
    """Точный определитель матрицы из Fraction: масштаб к целым + Bareiss."""
    n = len(M)
    if n == 0:
        return Fraction(1)
    dens = [x.denominator for row in M for x in row]
    L = lcm(*dens) if len(dens) > 1 else dens[0]
    A = []
    for row in M:
        r = []
        for x in row:
            y = x * L
            if y.denominator != 1:
                raise ArithmeticError("scale failed")
            r.append(y.numerator)
        A.append(r)
    d = _bareiss_int(A)
    return Fraction(d, L ** n)


# =============================================================================
# 3. Ветвь (1): последовательное построение Φ (точная и float)
# =============================================================================
def _poly_inner(p, q, mus, exact):
    """⟨p, q⟩ = Σ_{i,j} p_i q_j μ_{i+j} для многочленов со списками коэфф."""
    total = Fraction(0) if exact else 0.0
    for i, ci in enumerate(p):
        if ci == 0:
            continue
        for j, cj in enumerate(q):
            if cj == 0:
                continue
            total += ci * cj * mus[i + j]
    return total


def alpha_beta_sequential(t, nu, exact=False):
    """Φ через ортогонализацию моментов (стиль Стилтьеса).

    P_0 = 1; P_{n+1} = xP_n − α_n P_n − β_n² P_{n−1}, где
    α_n = ⟨xP_n, P_n⟩/h_n,  β_n² = h_n/h_{n−1},  h_n = ⟨P_n, P_n⟩.

    Возвращает (alphas[N], beta2[N-1], h[N]) — (α_n, β_n², h_n = ||P_n||²).
    Работает и в Fraction (exact=True), и во float.
    """
    N = len(t)
    F = frac if exact else float
    mus = moments(t, nu, 2 * N, exact=exact)
    if not exact:
        mus = list(mus)

    def ip(p, q):
        return _poly_inner(p, q, mus, exact)

    P_prev = None                # P_{n-1}
    P = [F(1)]                   # P_0 = 1
    h_prev = None
    h = ip(P, P)                 # h_0
    alphas, beta2, hs = [], [], [h]
    for n in range(N):
        if n > 0:
            beta2.append(h / h_prev)      # β_n² = h_n / h_{n−1}
        xP = [F(0)] + P
        alphas.append(ip(xP, P) / h)      # α_n = ⟨xP_n, P_n⟩/h_n
        if n == N - 1:
            break                          # P_N не нужен
        b2 = h / h_prev if n > 0 else None
        P_next = []
        for i in range(len(xP)):
            v = xP[i] - alphas[n] * (P[i] if i < len(P) else F(0))
            if n > 0:
                v = v - b2 * (P_prev[i] if i < len(P_prev) else F(0))
            P_next.append(v)
        P_prev, P = P, P_next
        h_prev, h = h, ip(P, P)            # h_{n+1}
        hs.append(h)
    return alphas, beta2, hs


# =============================================================================
# 4. Ветвь (2): определители Ханкеля
# =============================================================================
def hankel_matrix(mus, n, shift=0, exact=False):
    if exact:
        return [[mus[i + j + shift] for j in range(n)] for i in range(n)]
    return [[float(mus[i + j + shift]) for j in range(n)] for i in range(n)]


def semishifted_matrix(mus, m, exact=False):
    """Матрица S_m: ганкелева μ_{i+j} для j ≤ m−2, ПОСЛЕДНИЙ столбец сдвинут:
    entry(i, m−1) = μ_{i+m}. S_0 := 0 по соглашению (пустой определитель).

    Зачем: коэффициент при λ^{n−1} моника P_n равен −S_n/D_n (разложение
    бордельного определителя по последней строке), откуда
        α_n = S_{n+1}/D_{n+1} − S_n/D_n.
    (Полностью сдвинутые определители Dˆ_n = det(μ_{i+j+1}) дают ДРУГУЮ
    величину и для α не годятся — проверено численно.)
    """
    if m == 0:
        return []
    if exact:
        return [[mus[i + j] if j < m - 1 else mus[i + m] for j in range(m)]
                for i in range(m)]
    return [[float(mus[i + j]) if j < m - 1 else float(mus[i + m])
             for j in range(m)] for i in range(m)]


def hankel_dets_exact(mus, nmax):
    """D_n и полусдвинутые S_n для n = 0..nmax (точные Fraction).
    D_0 = 1, S_0 = 0 по соглашению."""
    D = [Fraction(1)]
    S = [Fraction(0)]
    for n in range(1, nmax + 1):
        D.append(det_frac(hankel_matrix(mus, n, 0, exact=True)))
        S.append(det_frac(semishifted_matrix(mus, n, exact=True)))
    return D, S


def alpha_beta_from_hankel(D, S):
    """Φ из определителей: α_n = S_{n+1}/D_{n+1} − S_n/D_n; β_n² = D_{n+1}D_{n−1}/D_n².

    D[0..N] — ганкелевы D_0 = 1; S[0..N] — полусдвинутые S_0 = 0, S_1 = μ_1.
    """
    N = len(D) - 1
    al = [S[n + 1] / D[n + 1] - S[n] / D[n] for n in range(N)]
    b2 = [D[n + 1] * D[n - 1] / (D[n] * D[n]) for n in range(1, N)]
    return al, b2


# =============================================================================
# 3bis. Ветвь (2) в высокой точности: определители Ханкеля через mpmath.
# Моменты ζ-меры растут как γ^k ~ 10^91, det H_24 ~ 10^2000 — обычный float
# переполняется, поэтому считаем (sign, log|det|) и собираем α, β² из логов.
# =============================================================================
from mpmath import mp, mpf, log as mp_log, exp as mp_exp


def _det_logdet(A):
    """(sign, log|det|) методом LU с выбором главного элемента и строковым
    масштабированием. A — квадратная матрица (список списков чисел mpf/float)."""
    n = len(A)
    A = [[mpf(x) for x in row] for row in A]
    s = [max((abs(x) for x in row), default=mpf(1)) for row in A]
    for i in range(n):
        if s[i] == 0:
            s[i] = mpf(1)
        A[i] = [x / s[i] for x in A[i]]
    sign = 1
    logdet = sum(mp_log(s[i]) for i in range(n))
    for k in range(n):
        p = max(range(k, n), key=lambda r: abs(A[r][k]))
        if p != k:
            A[k], A[p] = A[p], A[k]
            sign = -sign
        piv = A[k][k]
        if piv == 0:
            return 0, mpf('-inf')
        logdet += mp_log(abs(piv))
        if piv < 0:
            sign = -sign
        for i in range(k + 1, n):
            f = A[i][k] / piv
            if f:
                for j in range(k, n):
                    A[i][j] -= f * A[k][j]
    return sign, logdet


def hankel_logdets_mp(mus, nmax, shift=0):
    """Список (sign, log|det|) для D_n^(shift), n = 1..nmax (mpmath)."""
    out = []
    for n in range(1, nmax + 1):
        M = [[mpf(mus[i + j + shift]) for j in range(n)] for i in range(n)]
        out.append(_det_logdet(M))
    return out


def alpha_beta_hankel_mp(t, nu, dps=400):
    """Φ через определители Ханкеля в mpmath-арифметике высокой точности.

    Моменты считаются ТОЧНО (Fraction) и переводятся в mpf без потерь,
    так что точность ограничена только dps.
    Возвращает (alphas[N] (mpf), beta2[N-1] (mpf), logD[n], logS[n]).
    Для положительной меры все D_n, S_n > 0 (n ≥ 1).
    """
    old = mp.dps
    mp.dps = dps
    try:
        N = len(t)
        mus_ex = moments(t, nu, 2 * N, exact=True)
        mus = [mpf(m.numerator) / mpf(m.denominator) for m in mus_ex]
        logD = [mpf(0)] + [hankel_logdets_mp(mus, N, 0)[i][1] for i in range(N)]
        logS = [mpf('-inf')]           # S_0 = 0 → log = −inf
        for m in range(1, N + 1):
            M = [[mus[i + j] if j < m - 1 else mus[i + m] for j in range(m)]
                 for i in range(m)]
            logS.append(_det_logdet(M)[1])
        al = [mp_exp(logS[1] - logD[1])]
        for n in range(1, N):
            al.append(mp_exp(logS[n + 1] - logD[n + 1])
                      - mp_exp(logS[n] - logD[n]))
        b2 = [mp_exp(logD[n + 1] + logD[n - 1] - 2 * logD[n])
              for n in range(1, N)]
        return al, b2, logD, logS
    finally:
        mp.dps = old


# =============================================================================
# 5. Обратная задача Φ⁻¹ и тождества Ньютона
# =============================================================================
def charpoly_coeffs(alpha, beta2, exact=False):
    """Коэффициенты p_N(λ) = det(λI − J) по рекуррентности трёхчлена.

    p_0 = 1; p_1 = λ − α_0; p_{n+1} = (λ − α_n) p_n − β_n² p_{n-1}.
    Возвращает список коэффициентов [c_0..c_N] (c_N = 1) — старший последний.
    """
    F = frac if exact else float
    N = len(alpha)
    p_prev = [F(1)]                    # p_0
    p = [-alpha[0], F(1)]              # p_1
    for n in range(1, N):
        c = beta2[n - 1]
        new = [F(0)] * (n + 2)
        # (λ − α_n) p
        for i, ci in enumerate(p):
            new[i + 1] += ci
            new[i] -= alpha[n] * ci
        # − β_n² p_prev
        for i, ci in enumerate(p_prev):
            new[i] -= c * ci
        p_prev, p = p, new
    return p


def charpoly_of_roots(values, exact=False):
    """Коэффициенты Π(λ − t_i) по возрастанию степеней: [c_0..c_N], c_N = 1.

    Возвращает также элементарные симметрические e_k: c_{N-k} = (−1)^k e_k.
    Входные значения приводятся к Fraction/float — иначе Fraction × np.float64
    тихо возвращает float и точность гибнет.
    """
    F = frac if exact else float
    vals = [F(x) for x in values]
    c = [F(1)]                       # многочлен «1», возрастающий порядок
    for x in vals:
        new = [F(0)] * (len(c) + 1)
        for k, ck in enumerate(c):
            new[k] += ck * (-x)
            new[k + 1] += ck
        c = new
    N = len(vals)
    e = [(((-1) ** k) * c[N - k]) for k in range(N + 1)]
    return c, e


def elementary_symmetric(values, exact=False):
    """e_k(values), k = 0..N (e_0 = 1) — точные Fraction или float."""
    return charpoly_of_roots(values, exact=exact)[1]


def poly_eval(p, x, exact=False):
    """Значение многочлена (коэффициенты по возрастанию) в точке x."""
    if exact:
        acc = Fraction(0)
        for c in reversed(p):
            acc = acc * frac(x) + c
        return acc
    acc = 0.0
    for c in reversed(p):
        acc = acc * x + c
    return acc


# =============================================================================
# 5bis. Точная проверка ранга матрицы моментов (аннигиляция)
# =============================================================================
def annihilation_residuals(t, nu, kmax, exact=True):
    """Остатки Σ_i c_i μ_{i+j} для j = 0..kmax, где c — коэффициенты
    Π(x − t_i) (по возрастанию). Для меры с N атомами ВСЕ остатки равны 0
    точно (многочлен N-й степени аннигилирует меру) — ранг матрицы моментов
    равен N, поэтому D_{N+1} = 0. Проверяется в точной арифметике."""
    c, _ = charpoly_of_roots(t, exact=exact)
    mus = moments(t, nu, kmax + len(t), exact=exact)
    res = []
    for j in range(kmax + 1):
        s = Fraction(0) if exact else 0.0
        for i, ci in enumerate(c):
            s += ci * mus[i + j]
        res.append(s)
    return res


def h_squares_certificate(t, nu, P):
    """«Позитивный сертификат»: h_n = ⟨P_n,P_n⟩ = Σ ν_i P_n(t_i)² — точная
    сумма квадратов; используется для проверки положительности и как
    независимый пересчёт h_n. P — список коэффициентов (по возрастанию)."""
    mus = None
    total = Fraction(0)
    for i in range(len(t)):
        v = poly_eval(P, t[i], exact=True)
        total += frac(nu[i]) * v * v
    return total


# =============================================================================
# 6. Резольвента: три согласованных представления
# =============================================================================
def resolvent_cf(z, alpha, beta2):
    """S(z) через продолженную дробь якобиева оператора (вниз-вверх)."""
    n = len(alpha)
    zs = complex(z)
    # S_n = 1/(z − α_{n-1}),  S_k = 1/(z − α_k − β_{k+1}² S_{k+1})
    S = 1.0 / (zs - alpha[n - 1])
    for k in range(n - 2, -1, -1):
        S = 1.0 / (zs - alpha[k] - beta2[k] * S)
    return S


def resolvent_direct(z, t, nu):
    """S(z) = Σ ν_i/(z − t_i)."""
    zs = complex(z)
    return sum(nu[i] / (zs - t[i]) for i in range(len(t)))


def resolvent_qp(z, t, nu):
    """S(z) = Q(z)/P(z), P(λ) = Π(λ − t_i), Q(λ) = Σ ν_i Π_{j≠i}(λ − t_j)."""
    zs = complex(z)
    P = 1.0 + 0.0j
    Q = 0.0 + 0.0j
    for i in range(len(t)):
        # вычисляем P(z) и Π_{j≠i}(z − t_j) за один проход невозможно —
        # поэтому честно: два прохода.
        pass
    P = 1.0 + 0.0j
    for x in t:
        P *= (zs - x)
    for i in range(len(t)):
        term = 1.0 + 0.0j
        for j in range(len(t)):
            if j != i:
                term *= (zs - t[j])
        Q += nu[i] * term
    return Q / P


# =============================================================================
# 7. Квантование канвы Q22 (точно как в pixel_decoding.py)
# =============================================================================
def encode(v):
    x = int(round(abs(v) * SCALE))
    if not (0 <= x <= LIMIT):
        raise ValueError("value out of Q22 range")
    return ((x & 255, (x >> 8) & 255, (x >> 16) & 255,
             ((x >> 23) & 127) | (0x80 if v < 0 else 0)))


def decode(px):
    x = int(px[0]) | (int(px[1]) << 8) | (int(px[2]) << 16) | \
        ((int(px[3]) & 127) << 23)
    v = x / SCALE
    return -v if (int(px[3]) >> 7) else v


# =============================================================================
# 8. Эталонный Ланцош (как в pixel_decoding.py) — численная ссылка
# =============================================================================
def lanczos_jacobi(gams, w):
    """Трёхдиагональ J из Ланцоша на diag(γ), полное реортогонализация."""
    V = np.zeros((len(gams), len(gams)))
    al = np.zeros(len(gams))
    be = np.zeros(len(gams) - 1)
    V[:, 0] = w / np.linalg.norm(w)
    for k in range(len(gams)):
        z = gams * V[:, k]
        al[k] = V[:, k] @ z
        z = z - al[k] * V[:, k]
        if k > 0:
            z = z - be[k - 1] * V[:, k - 1]
        for j in range(k + 1):
            z -= (V[:, j] @ z) * V[:, j]
        if k < len(gams) - 1:
            be[k] = np.linalg.norm(z)
            V[:, k + 1] = z / be[k]
    return al, be


def tridiag(al, be):
    n = len(al)
    H = np.zeros((n, n))
    np.fill_diagonal(H, al)
    for i in range(1, n):
        H[i, i - 1] = H[i - 1, i] = be[i - 1]
    return H


def trace_powers(H, kmax):
    """tr H^k, k = 1..kmax (через собственные значения — симметричная H)."""
    lam = np.linalg.eigvalsh(H)
    return np.array([np.sum(lam ** k) for k in range(1, kmax + 1)])
