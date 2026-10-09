"""hpbridge.traceformula — следовая формула Tr e^{-uH} против явной формулы
Гуинана–Вейля (кампания C4, теорема T6).

Точное тождество (произведение Адамара для ξ, вывод — docs/trace_formula.md):
  Q(a) := Σ_{γ>0} 2a/(a²+γ²)
       = ζ'/ζ(½+a) + 1/(½+a) + 1/(a−½) − ½lnπ + ½ψ(¼+a/2) − B − C₀,
  B = ½ln(4π) − 1 − γ/2 = ξ'(0)/ξ(0),  C₀ = Σ_{γ>0} 1/(¼+γ²) = −B.

Следовая формула для оператора H_ξ = diag(±γ_n):
  K(x) := Tr e^{-xH_ξ} = Σ_{γ>0} e^{-xγ} = (1/π)∫₀^∞ Q(a)·sin(ax) da,
причём при a > ½ ряд ζ'/ζ(½+a) = −ΣΛ(n)/n^{½+a} вносит ПРИНЯТЫЙ вес
Λ(n)/√n: «вес простых» в тепловом следе нулей. Для произвольного затвора
метрика r_EF — корреляция флуктуации развёрнутого теплового следа с простой
гребёнкой P(u) = ΣΛ(n)/√n·u/(u²+ln²n) при фиксированном масштабе.
"""
import numpy as np
from scipy.special import sici, psi as digamma

from hpbridge.constants import B_HADAMARD as B, GAMMA_E


def C0_from_zeros(zeros):
    """C₀ = Σ 1/(¼+γ²) по файлу + аналитический хвост по гладкой плотности."""
    z = np.asarray(zeros, dtype=float)
    tail = (np.log(z[-1] / (2 * np.pi)) + 1.0) / (2 * np.pi * z[-1])
    return float(np.sum(1.0 / (0.25 + z * z)) + tail)


def Q_direct(a, zeros):
    """Прямая сумма Σ 2a/(a²+γ²) + хвост (a/π)(ln(Γ/2π)+1)/Γ."""
    z = np.asarray(zeros, dtype=float)
    s = float(np.sum(2.0 * a / (a * a + z * z)))
    return s + (a / np.pi) * (np.log(z[-1] / (2 * np.pi)) + 1.0) / z[-1]


def Q_identity(a, C0, dps=25):
    """Замкнутая форма Q(a) (mpmath)."""
    import mpmath as mp
    mp.mp.dps = dps
    s = mp.mpf('0.5') + mp.mpf(a)
    zl = mp.diff(mp.zeta, s) / mp.zeta(s)
    val = (zl + 1 / s + 1 / (s - 1) - mp.log(mp.pi) / 2
           + mp.digamma(s / 2) / 2 - mp.mpf(B) - mp.mpf(C0))
    return float(val)


def S_smooth(a, C0):
    """Гладкая часть замкнутой формы (без ζ-ряда), векторизованная."""
    a = np.asarray(a, dtype=float)
    return (1.0 / (0.5 + a) + 1.0 / (a - 0.5) - 0.5 * np.log(np.pi)
            + 0.5 * digamma(0.25 + a / 2.0) - B - C0)


def tail_S(x, A, C0):
    """∫_A^∞ S_smooth(a)·sin(ax)da — точные замкнутые формы (Si/Ci):
    1/(a∓b), ln-часть ½·J (вывод — docs/trace_formula.md §4), R₂ численно."""
    x, A = float(x), float(A)

    def frac_pos(b):                     # ∫ sin(ax)/(a−b) da
        Si, Ci = sici((A - b) * x)
        return float(np.cos(b * x) * (np.pi / 2 - Si) - np.sin(b * x) * Ci)

    def frac_neg(b):                     # ∫ sin(ax)/(a+b) da
        Si, Ci = sici((A + b) * x)
        return float(np.cos(b * x) * (np.pi / 2 - Si) + np.sin(b * x) * Ci)

    t_pole = frac_pos(0.5)
    t_half = frac_neg(0.5) - 0.5 * frac_neg(0.5)   # 1/(a+½) и −1/(4z) = −½/(a+½)
    zA = 0.25 + A / 2.0
    bz = x * (A + 0.5)
    Sbz, Cbz = sici(bz)
    lz = np.log(zA)
    J = (np.cos(0.5 * x) * (lz * np.cos(bz) - Cbz)
         + np.sin(0.5 * x) * (lz * np.sin(bz) + np.pi / 2 - Sbz)) / x
    aa = np.linspace(A, 600.0, 8000)
    zz = 0.25 + aa / 2.0
    R2 = 0.5 * digamma(zz) - 0.5 * np.log(zz) + 0.25 / zz
    t_R2 = float(np.trapezoid(R2 * np.sin(aa * x), aa))
    t_const = (-0.5 * np.log(np.pi) - B - C0) * np.cos(A * x) / x
    return t_pole + t_half + 0.5 * J + t_R2 + t_const


def K_formula(x, C0, Q_spline, lam_n=None, lam_w=None, A_SPLIT=1.5):
    """Явная сторона следовой формулы: (1/π)(T1 + T2 + T3).
    T1 — интеграл замкнутой формы на [0, A_SPLIT] (сплайн Q);
    T2 — простая часть при a > A_SPLIT: −ΣΛ(n)/√n·Im[e^{−A(ln n−ix)}/(ln n−ix)];
    T3 — гладкая часть (tail_S)."""
    x = float(x)
    aa1 = np.linspace(0.0, A_SPLIT, 3001)
    t1 = float(np.trapezoid(Q_spline(aa1) * np.sin(aa1 * x), aa1))
    ph = lam_n - 1j * x
    t2 = -float(np.sum(lam_w * np.imag(np.exp(-A_SPLIT * ph) / ph)))
    t3 = tail_S(x, A_SPLIT, C0)
    return (t1 + t2 + t3) / np.pi, {'T1': t1 / np.pi, 'T2': t2 / np.pi,
                                    'T3': t3 / np.pi}


def K_direct(x, zeros, gmax=6000.0):
    """Прямая сумма Tr e^{-xH_ξ} = Σ e^{-xγ}."""
    g = np.asarray(zeros, dtype=float)
    g = g[g <= gmax]
    return float(np.sum(np.exp(-x * g)))


# ── метрика затворов (M2) ───────────────────────────────────────────────────
def heat_trace_fluct(xn, U):
    """D(u) = Σ e^{-u x_n} − гладкая часть единичной плотности."""
    xn = np.asarray(xn, dtype=float)
    S = np.array([np.sum(np.exp(-u * xn)) for u in U])
    return S - (1.0 - np.exp(-U * xn[-1])) / U


def prime_comb(u, lam_n, lam_w):
    """P(u) = Σ Λ(n)/√n·u/(u²+ln²n) + хвост."""
    lnn = np.log(lam_n.astype(np.float64))
    w = lam_w / np.sqrt(lam_n.astype(np.float64))
    s = float(np.sum(w * u / (u * u + lnn * lnn)))
    return s + (1.0 / u) * (lam_n[-1] ** -0.5) / 1e3


def fit_corr(D, P):
    """r_EF при фиксированном масштабе s=1 (ранговое соответствие окон)."""
    c = float(np.dot(D, P) / max(np.dot(P, P), 1e-30))
    return float(np.corrcoef(D, c * P)[0, 1]), 1.0, c


def resid_rel(D, P):
    """Относительный остаток после МНК (центрированные кривые) = √(1−r²)."""
    Dc, Pc = D - D.mean(), P - P.mean()
    c = float(np.dot(Dc, Pc) / max(np.dot(Pc, Pc), 1e-30))
    res = Dc - c * Pc
    return float(np.sqrt(np.mean(res ** 2)) / max(np.sqrt(np.mean(Dc ** 2)),
                                                  1e-30))


def surrogate_null(D, P, ndraw=120, block=5, seed0=1234):
    """Блочный суррогатный нуль: перемешивание блоков P."""
    rs, n = [], P.size
    for k in range(ndraw):
        rng = np.random.default_rng(seed0 + k)
        blocks = [np.arange(i, min(i + block, n)) for i in range(0, n, block)]
        order = rng.permutation(len(blocks))
        rs.append(fit_corr(D, np.concatenate([P[blocks[j]] for j in order]))[0])
    rs = np.array(rs)
    return float(np.mean(rs)), float(np.std(rs))
