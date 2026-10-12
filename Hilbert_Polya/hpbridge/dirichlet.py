"""hpbridge.dirichlet — пайплайн C1–C4 + C6 для L-функций Дирихле
(C15, пункт 12 плана, теорема T17).

Вопрос: универсален ли измеренный разрыв Г2, или он — дефект конкретно дзеты?
Пайплайн v1 повторяется для двух квадратичных характеров:
  χ₅ — чётный вещественный характер mod 5 (1,−1,−1,1);
  χ₇ — нечётный вещественный характер mod 7 (1,1,−1,1,−1,−1).
Каждая ветвь:
  D1  Z_χ(t) = e^{iθ_χ(t)}L(½+it,χ) — вещественность на линии (K2-аналог);
  D2  нули Z_χ бисекцией до T = 120 (K3-аналог), согласие с гладким счётом;
  D3  следовая формула H_{ξ,χ}: K_χ(x) = Σe^{−xγ} = (1/π)∫Q_χ sin — T17:
      Q_χ(a) = Λ'/Λ(½+a,χ) − B_χ несёт СКРУЧЕННЫЙ вес χ(n)Λ(n)/√n;
  D4  ψ_χ-лестница: сито Σχ(n)Λ(n) против эталона по нулям (M2-аналог);
  D5  ранговая проекция: r_H7 решёточных затворов против окна нулей L —
      универсальность разрыва Г2 (ожидание: нулевая зона, как у дзеты).
"""
import numpy as np
import mpmath as mp

# ── характеры ────────────────────────────────────────────────────────────────
CHI5 = {1: 1, 2: -1, 3: -1, 4: 1}                       # чётный, a = 0
CHI7 = {1: 1, 2: 1, 3: -1, 4: 1, 5: -1, 6: -1}          # нечётный, a = 1


def character_values(q):
    if q == 5:
        return CHI5, 0
    if q == 7:
        return CHI7, 1
    raise ValueError("в v2 поддерживаются q = 5, 7")


def dirichlet_L(s, q, dps=25):
    """L(s,χ) через разложение Гурвица: L(s,χ) = q^{−s}Σ_r χ(r)ζ(s,r/q)."""
    chi, _ = character_values(q)
    keep = mp.mp.dps
    mp.mp.dps = dps
    try:
        s_ = mp.mpc(s)
        acc = mp.mpc(0)
        for r, c in chi.items():
            acc += c * mp.zeta(s_, mp.mpf(r) / q)
        return acc / mp.power(q, s_)
    finally:
        mp.mp.dps = keep


def L_prime(s, q, dps=25):
    """L'(s,χ) центральной разностью (mp.diff обнуляется из-за
    усечения точности внутри dirichlet_L)."""
    keep = mp.mp.dps
    mp.mp.dps = dps + 5
    try:
        s_ = mp.mpc(s)
        h = mp.mpf(10) ** (-(dps // 2))
        return (dirichlet_L(s_ + h, q, dps + 5)
                - dirichlet_L(s_ - h, q, dps + 5)) / (2 * h)
    finally:
        mp.mp.dps = keep


def theta_chi(t, q, dps=30):
    """θ_χ(t) = (t/2)ln(q/π) + Im ln Γ((½+a+it)/2) — фаза.completed."""
    chi, a = character_values(q)
    keep = mp.mp.dps
    mp.mp.dps = dps + 10
    try:
        tt = mp.mpf(t)
        val = (tt * mp.log(mp.mpf(q) / mp.pi) / 2
               + mp.im(mp.log(mp.gamma((mp.mpf('0.5') + a + 1j * tt) / 2))))
        return float(val)
    finally:
        mp.mp.dps = keep


def Z_chi(t, q, dps=25):
    """Z_χ(t) = e^{iθ_χ(t)}L(½+it,χ) — вещественная функция на линии."""
    keep = mp.mp.dps
    mp.mp.dps = dps + 10
    try:
        tt = mp.mpf(t)
        th = (tt * mp.log(mp.mpf(q) / mp.pi) / 2
              + mp.im(mp.log(mp.gamma((mp.mpf('0.5')
                                       + character_values(q)[1] + 1j * tt) / 2))))
        val = mp.e ** (1j * th) * dirichlet_L(0.5 + 1j * float(t), q, dps=dps + 10)
        return float(mp.re(val)), float(mp.im(val))
    finally:
        mp.mp.dps = keep


def chi_zeros_bisection(q, T=120.0, step=0.02, dps=25):
    """Нули Z_χ на (0,T] бисекцией по смене знака (K3-аналог)."""
    grid = np.arange(step, T + step, step)
    vals = np.array([Z_chi(float(g), q, dps)[0] for g in grid])
    signs = np.where(np.diff(np.sign(vals)) != 0)[0]
    zeros = []
    for i in signs:
        a, b = grid[i], grid[i + 1]
        fa = vals[i]
        for _ in range(70):
            m = 0.5 * (a + b)
            fm = Z_chi(float(m), q, dps)[0]
            if fm == 0:
                a = b = m
                break
            if np.sign(fm) == np.sign(fa):
                a, fa = m, fm
            else:
                b = m
        zeros.append(0.5 * (a + b))
    return np.array(zeros)


def smooth_count_chi(T, q):
    """Гладкий счёт N̄_χ(T) = (1/π)[(T/2)ln(q/π) + Im ln Γ((½+a+iT)/2)] + c."""
    chi, a = character_values(q)
    keep = mp.mp.dps
    mp.mp.dps = 30
    try:
        TT = mp.mpf(T)
        ph = (TT * mp.log(mp.mpf(q) / mp.pi) / 2
              + mp.im(mp.loggamma((mp.mpf('0.5') + a + 1j * TT) / 2)))
        return float(ph / mp.pi)
    finally:
        mp.mp.dps = keep


# ── следовая формула χ-стороны (T17) ────────────────────────────────────────
def completed_L(s, q, dps=25):
    """Λ_χ(s) = (q/π)^{(s+a)/2}Γ((s+a)/2)L(s,χ)."""
    chi, a = character_values(q)
    keep = mp.mp.dps
    mp.mp.dps = dps
    try:
        s_ = mp.mpc(s)
        return (mp.power(mp.mpf(q) / mp.pi, (s_ + a) / 2)
                * mp.gamma((s_ + a) / 2) * dirichlet_L(s, q, dps))
    finally:
        mp.mp.dps = keep


def B_chi(q, dps=30):
    """B_χ = Λ'_χ(0)/Λ_χ(0) — константа Адамара характера.

    Для чётного характера Γ(s/2) имеет полюс при s=0 (Λ целая за счёт
    L(0,χ)=0). B извлекается наклоном ln Λ(s) при s→0+ (устойчиво)."""
    keep = mp.mp.dps
    mp.mp.dps = dps
    try:
        ss = [mp.mpf('1e-5'), mp.mpf('2e-5'), mp.mpf('4e-5')]
        lns = [mp.log(completed_L(s, q, dps)) for s in ss]
        n = len(ss)
        sx = sum(ss); sy = sum(lns)
        sxx = sum(s * s for s in ss)
        sxy = sum(s * l for s, l in zip(ss, lns))
        return mp.re((n * sxy - sx * sy) / (n * sxx - sx * sx))
    finally:
        mp.mp.dps = keep


def C0_chi(zeros_chi, q, dps=25):
    """C₀^χ = Σ_{γ>0} 1/(¼+γ²) — точное тождество из Адамара:
    Λ'/Λ(½) = B_χ + C₀^χ  ⇒  C₀^χ = Λ'/Λ(½) − B_χ.
    Нулевая сумма (по закоммиченным нулям) — встроенный перекрёстный контроль.
    """
    z = np.asarray(zeros_chi, dtype=float)
    s_sum = float(np.sum(1.0 / (0.25 + z * z)))
    keep = mp.mp.dps
    mp.mp.dps = dps
    try:
        s0 = mp.mpf('0.5')
        h = mp.mpf('1e-6')
        lam1 = completed_L(s0 + h, q, dps)
        lam0 = completed_L(s0 - h, q, dps)
        lam = completed_L(s0, q, dps)
        ratio = mp.re((lam1 - lam0) / (2 * h) / lam)
        B = B_chi(q, dps)
        C0_exact = float(ratio - B)
        return C0_exact, s_sum
    finally:
        mp.mp.dps = keep


def Q_chi_direct(a, zeros_chi):
    z = np.asarray(zeros_chi, dtype=float)
    return float(np.sum(2.0 * a / (a * a + z * z)))


def Q_chi_identity(a, q, B, C0, dps=25):
    """Q_χ(a) = Λ'/Λ(½+a) − B_χ − C₀^χ (вывод Адамара для характера,
    полный аналог v1: пара нулей даёт 2a/(a²+γ²), плюс константа C₀)."""
    keep = mp.mp.dps
    mp.mp.dps = dps + 5
    try:
        s = mp.mpf('0.5') + mp.mpf(a)
        h = mp.mpf('1e-6') * max(1, float(a))
        lam1 = completed_L(s + h, q, dps + 5)
        lam0 = completed_L(s - h, q, dps + 5)
        lam = completed_L(s, q, dps + 5)
        dlam = (lam1 - lam0) / (2 * h)
        return float(mp.re(dlam / lam) - B - C0)
    finally:
        mp.mp.dps = keep


def K_chi_direct(x, zeros_chi, gmax=None):
    z = np.asarray(zeros_chi, dtype=float)
    if gmax:
        z = z[z <= gmax]
    return float(np.sum(np.exp(-x * z)))


def _chi_prime_weights(nmax, q):
    """(ln n, χ(n)Λ(n)/√n) — скрученные простые веса для T2χ."""
    from engine.solver import sieve_lambda
    lam, _ = sieve_lambda(nmax)
    chi, _ = character_values(q)
    ns = np.arange(2, lam.size)
    m = lam[2:] > 0
    ns = ns[m]
    lm = lam[2:][m]
    ch = np.array([chi.get(int(n % q), 0) for n in ns], dtype=float)
    w = ch * lm / np.sqrt(ns.astype(float))
    keep = w != 0.0
    return np.log(ns[keep].astype(float)), w[keep]


def _frac_neg(x, A, b):
    """∫_A^∞ sin(ax)/(a+b) da (v1-форма Si/Ci)."""
    from scipy.special import sici
    Si, Ci = sici((A + b) * x)
    return float(np.cos(b * x) * (np.pi / 2 - Si) + np.sin(b * x) * Ci)


def _J_ln(x, A, b=0.5):
    """∫_A^∞ ln((a+b)/2)·sin(ax) da (замкнутая форма, Si/Ci):
    = ln((A+b)/2)·cos(Ax)/x + (2/x)·[Ci((A+b)x)cos(bx)
                                     + (π/2 − Si((A+b)x))sin(bx)].
    Валидировано mp.quadosc (b = 0.5: до 6 значащих цифр)."""
    from scipy.special import sici
    lz = np.log((A + b) / 2.0)
    z = (A + b) * x
    Si, Ci = sici(z)
    return float(lz * np.cos(A * x) / x
                 + (-Ci * np.cos(b * x)
                    + (np.pi / 2 - Si) * np.sin(b * x)) / x)


def K_chi_formula(x, zeros_chi, q, B, C0, A_SPLIT=6.0, nmax=1_000_000):
    """(1/π)∫₀^∞ Q_χ(a)sin(ax)da — численно на [0.005, A] + ЗАКРЫТЫЙ хвост:
    лог-часть (J), константа, −½/(a+½) (хвост ψ), R2-остаток численно,
    χ-искажённая простая часть T2χ (точное преобразование ряда, v1-T2)."""
    x = float(x)
    _, a_char = character_values(q)
    b = 0.5 + a_char               # сдвиг Γ-аргумента: z = (a+b)/2
    a_grid = np.linspace(0.005, A_SPLIT, 500)
    qv = np.array([Q_chi_identity(a, q, B, C0, dps=18) for a in a_grid])
    t1 = float(np.trapezoid(qv * np.sin(a_grid * x), a_grid))
    # ── хвост a > A_SPLIT ──
    c0 = 0.5 * np.log(q / np.pi) - B - C0
    t_log = 0.5 * _J_ln(x, A_SPLIT, b)
    t_const = c0 * np.cos(A_SPLIT * x) / x
    t_half = -0.5 * _frac_neg(x, A_SPLIT, b)
    # R2χ = −1/(24z²), z = (a+b)/2 — численно до 150, хвост ничтожен
    aa = np.linspace(A_SPLIT, 150.0, 4000)
    zz = (aa + b) / 2.0
    t_r2 = float(np.trapezoid((-1.0 / (24.0 * zz ** 2)) * np.sin(aa * x), aa))
    # T2χ: −Σ χ(n)Λ(n)/√n · Im[e^{−A(ln n − ix)}/(ln n − ix)]
    lnn, w = _chi_prime_weights(nmax, q)
    ph = lnn - 1j * x
    t2chi = -float(np.sum(w * np.imag(np.exp(-A_SPLIT * ph) / ph)))
    tail = t_log + t_const + t_half + t_r2 + t2chi
    return (t1 + tail) / np.pi


# ── ψ_χ-лестница ─────────────────────────────────────────────────────────────
def psi_chi_sieve(xmax=200_000, q=5):
    """ψ_χ(x) = Σ_{n≤x} χ(n)Λ(n) — сито (M2-аналог, twisted)."""
    from engine.solver import sieve_lambda
    lam, _ = sieve_lambda(xmax)
    chi, _ = character_values(q)
    ns = np.arange(2, xmax + 1)
    w = np.array([chi.get(int(n % q), 0) for n in ns], dtype=float)
    cdf = np.cumsum(lam[2:] * w)
    return ns, cdf


def psi_chi_reference(x, zeros_chi, kmax=None):
    """ψ_χ^{ref}(x) = −Σ_ρ x^ρ/ρ (вещественная часть) — эталон по нулям.
    Непринципиальный характер: полюса нет, главный член отсутствует."""
    x = np.asarray(x, dtype=float)
    g = np.asarray(zeros_chi[:kmax] if kmax else zeros_chi, dtype=complex)
    out = np.zeros_like(x)
    for i, xi in enumerate(x):
        s = np.sum(np.exp(1j * g * np.log(xi)) / (0.5 + 1j * g))
        out[i] = -np.sqrt(xi) * s.real
    return out
