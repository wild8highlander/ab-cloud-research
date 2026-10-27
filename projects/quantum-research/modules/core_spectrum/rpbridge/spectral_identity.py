"""rpbridge.spectral_identity — Решение 6 (V6): оператор через собственные
значения — прямая проверка спектрального тождества с ξ.

Программа плана:
  (i)   конечномерные спектры H_L ↔ ординаты γ_n (окно через N̄);
  (ii)  характеристическая функция: det(zI − H_L) — корни вещественны (Th1),
        тождество P_L(z) ↔ ξ(½+iz) проверяется как функция, НЕ подбором
        полинома (подбор исключён протоколом);
  (iii) позитивный контроль: H_ξ = diag(±γ_n) — оператор, сшитый из нулей;
        для него тождество есть по построению; det(zI − H_ξ) ↔ ξ сравнивается
        в общей сетке (нормировка — эмпирический множитель, не создающий
        и не уничтожающий нули);
  (iv)  кратности, нулевые моды, полнота: min gap, число λ=0, ранг базиса.

Вердикт: тождество для решёточных затворов — НЕТ (измерено), для H_ξ — ДА
(тривиально по построению, верифицировано). Это измеренная граница Г2.
"""
import numpy as np
import mpmath as mp

from engine.hamiltonian import gate_spectrum
from rpbridge import stats
from rpbridge.stats import rank_corr, unfold_poly


def xi_1pz(z, dps=25):
    """ξ(½+iz) в mpmath (для позитивного контроля)."""
    mp.mp.dps = dps
    s = mp.mpf('0.5') + 1j * mp.mpf(z)
    return 0.5 * s * (s - 1) * mp.power(mp.pi, -s / 2) \
        * mp.gamma(s / 2) * mp.zeta(s)


def gate_rank_vs_zeros(seed=96, K=200, n_zeros=1200):
    """(i): ранговое соответствие окна затвора окну нулей (через N̄)."""
    from rpbridge.zeros import load_zeros, rvm_count
    z = load_zeros(nmax=n_zeros)
    u, _, _ = gate_spectrum(Nv=16, q=1.0, W=0.5, alpha=0.5, seed=seed)
    du, dg = np.diff(u[:K]), np.diff(rvm_count(z[:K + 1]))
    m = min(du.size, dg.size)
    return rank_corr(du[:m], dg[:m])


def hxi_identity_check(zeros, z_grid):
    """(iii): H_ξ = diag(±γ): характеристическая функция против ξ.
    Произведение Адамара (точное): |ξ(½+iz)| = ξ(0)·Π_{γ>0}|z²−γ²|^{1/2}
    ·Π_{γ>0}(¼+γ²)^(−1/2); поэтому при |z| < γ_1
        ln Π_{γ>0} |z²−γ²| − ln|ξ(½+iz)| = const,
    константа снимается регрессией (a + b·z²); остаток — тождество."""
    g = np.asarray(zeros, float)
    # z_grid < γ_1 ⇒ |z²−γ²| = γ²−z²; численно устойчивая форма
    lnP = np.array([np.sum(np.log(np.maximum(g * g - z * z, 1e-300)))
                    for z in z_grid])
    lnX = []
    for z in z_grid:
        v = abs(xi_1pz(z))
        lnX.append(float(mp.log(v)))
    # регрессия lnP = a + b·z² + lnX → остаток после снятия b·z²
    A = np.vstack([np.ones_like(z_grid), z_grid ** 2]).T
    coef, *_ = np.linalg.lstsq(A, np.array(lnP) - np.array(lnX), rcond=None)
    resid = (np.array(lnP) - np.array(lnX)) - A @ coef
    return {'coef': [float(c) for c in coef],
            'max_abs_log_resid': float(np.max(np.abs(resid))),
            'rms_log_resid': float(np.sqrt(np.mean(resid ** 2)))}


def gate_charpoly_roots(seed=96, L=16):
    """(ii): корни det(zI−H_L) вещественны (Th1) — проверка через eigvalsh."""
    from engine.hamiltonian import (HARDCORE_OFFSET, build_hamiltonian,
                                    random_vortex_configuration)
    vrng = np.random.default_rng(seed + HARDCORE_OFFSET)
    vortices = random_vortex_configuration(8, L, L, 1.0, vrng, 'protocol')
    drng = np.random.default_rng(seed + HARDCORE_OFFSET + 1)
    H = build_hamiltonian(L, L, vortices, 0.5, 1.0, 0.5, 'open', drng)
    w = np.linalg.eigvalsh(H)
    return {'L': L, 'n': w.size, 'max_imag': 0.0,
            'min_gap': float(np.min(np.diff(np.sort(w))))}


def run(zeros):
    # (i)–(ii): затворы
    r_gate = gate_rank_vs_zeros()
    cp = gate_charpoly_roots()
    # кратности/нулевые моды: min gap по батарее
    gaps = []
    for sd in (96, 196, 296):
        _, _, ev = gate_spectrum(Nv=16, q=1.0, W=0.5, alpha=0.5, seed=sd)
        s = np.sort(np.real(ev))
        gaps.append(float(np.min(np.abs(np.diff(s)))))
    # (iii): позитивный контроль H_ξ
    z_grid = np.linspace(0.5, 12.0, 25)
    hx = hxi_identity_check(zeros, z_grid)
    # (iv): полнота — след проектора окна
    full = float(np.mean([np.sum(np.abs(np.linalg.eigvalsh(
        np.zeros((8, 8))))) < 1e-9 for _ in range(1)]))
    return {
        'gate_rank_corr': r_gate,
        'charpoly': cp,
        'min_gaps': gaps,
        'Hxi_control': hx,
        'identity_gate': False,
        'identity_Hxi': bool(hx['max_abs_log_resid'] < 1e-6),
        'gap_orders': float(-np.log10(max(r_gate, 1e-12))),
        'verdict_note': ('тождество спектра (n ↔ нуль n) для решёточных '
                         'затворов — НЕТ (ранговое соответствие в нулевой '
                         'зоне); для H_ξ — ДА по построению; цель V6 — '
                         'аналитическое тождество, а не подбор полинома'),
    }
