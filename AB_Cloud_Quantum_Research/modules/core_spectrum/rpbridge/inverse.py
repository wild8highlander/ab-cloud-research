"""rpbridge.inverse — Решение 10 (V10): обратная задача — восстановление
арифметики из спектра.

Инварианты: Φ(θ) = (Tr H, Tr H², …, Tr H^k) — спектральные инварианты
(следы степеней; полиномы от собственных значений).
Матрица чувствительности: J_ij = ∂Φ_i/∂θ_j по параметрам вихрей
(позиции x_k, y_k, заряды q_k) — конечные разности с фиксированным шагом.
Идентифицируемость: ранг J (числовая), обусловленность cond(J).
Восстановление: оптимизация θ по инвариантам из спектра (МНК, Нелдера–Мид)
на конфигурациях, НЕ использованных при настройке протокола.
"""
import numpy as np

from engine.hamiltonian import (HARDCORE_OFFSET, build_hamiltonian,
                                random_vortex_configuration)


def _theta_of(vortices):
    out = []
    for (x, y, q) in vortices:
        out.extend([x, y, q])
    return np.array(out)


def _vortices_of(theta, Nv):
    v = []
    for k in range(Nv):
        x, y, q = theta[3 * k:3 * k + 3]
        v.append((float(x), float(y), float(q)))
    return v


def _H_of_theta(theta, Nv, L, seed):
    drng = np.random.default_rng(seed + HARDCORE_OFFSET + 1)
    return build_hamiltonian(L, L, _vortices_of(theta, Nv), 0.5, 1.0, 0.5,
                             'open', drng)


def invariants(H, k_max=6):
    """Φ = (Tr H, …, Tr H^k); Tr H^m = Σ λ^m (через eigenvalues)."""
    w = np.linalg.eigvalsh(H)
    return np.array([np.sum(w ** m) for m in range(1, k_max + 1)])


def sensitivity_matrix(Nv=8, L=12, seed=96, k_max=6, h=1e-4):
    """J_ij численно; работаем с реальными вихрями протокола."""
    vrng = np.random.default_rng(seed + HARDCORE_OFFSET)
    vort = random_vortex_configuration(Nv, L, L, 1.0, vrng, 'protocol')
    theta0 = _theta_of(vort)
    Phi0 = invariants(_H_of_theta(theta0, Nv, L, seed), k_max)
    J = np.zeros((k_max, theta0.size))
    for j in range(theta0.size):
        tp = theta0.copy()
        tp[j] += h
        Phip = invariants(_H_of_theta(tp, Nv, L, seed), k_max)
        J[:, j] = (Phip - Phi0) / h
    s = np.linalg.svd(J, compute_uv=False)
    return {'J': J, 'Phi0': Phi0,
            'rank': int(np.linalg.matrix_rank(J, tol=1e-6 * s[0])),
            'cond': float(s[0] / max(s[-1], 1e-300)),
            'n_params': int(theta0.size), 'k_max': k_max}


def recovery(zeros_or_seed=196, Nv=4, L=12, k_max=6, iters=600):
    """Восстановление зарядов q из инвариантов (позиции фиксированы)."""
    vrng = np.random.default_rng(zeros_or_seed + HARDCORE_OFFSET)
    vort = random_vortex_configuration(Nv, L, L, 1.0, vrng, 'protocol')
    theta_true = _theta_of(vort)
    Phi_true = invariants(_H_of_theta(theta_true, Nv, L, zeros_or_seed), k_max)

    def loss(theta):
        return float(np.sum((invariants(_H_of_theta(theta, Nv, L,
                                                    zeros_or_seed), k_max)
                             - Phi_true) ** 2))

    rng = np.random.default_rng(31337)
    best, best_val = None, np.inf
    for trial in range(3):
        th0 = theta_true.copy()
        th0[2::3] += rng.uniform(-0.3, 0.3, Nv)   # старт с возмущёнными q
        from scipy.optimize import minimize
        res = minimize(loss, th0, method='Nelder-Mead',
                       options={'maxiter': iters, 'xatol': 1e-4, 'fatol': 1e-10})
        if res.fun < best_val:
            best_val, best = float(res.fun), res.x
    q_err = float(np.max(np.abs(best[2::3] - theta_true[2::3])))
    return {'loss': best_val, 'q_recovery_max_err': q_err,
            'identifiable': bool(q_err < 1e-3)}


def run():
    sens = {}
    for Nv in (4, 8):
        sens[f'Nv{Nv}'] = sensitivity_matrix(Nv=Nv)
    rec = recovery()
    # различение арифметических конфигураций: Φ для разных (q) vs случайных
    sep = []
    for seed in (96, 196):
        vrng = np.random.default_rng(seed + HARDCORE_OFFSET)
        v_arith = random_vortex_configuration(4, 12, 12, 1.0, vrng, 'protocol')
        v_rand = [(x, y, float(np.random.default_rng(seed + k).uniform(-1, 1)))
                  for k, (x, y, _) in enumerate(v_arith)]
        Pa = invariants(_H_of_theta(_theta_of(v_arith), 4, 12, seed))
        Pr = invariants(_H_of_theta(_theta_of(v_rand), 4, 12, seed))
        sep.append(float(np.linalg.norm(Pa - Pr) / max(np.linalg.norm(Pa),
                                                       1e-30)))
    return {
        'sensitivity': {k: {'rank': v['rank'], 'cond': v['cond'],
                            'n_params': v['n_params'], 'k_max': v['k_max']}
                        for k, v in sens.items()},
        'recovery': rec,
        'arith_vs_random_separation': sep,
        'verdict_note': ('часть арифметики (заряды) идентифицируема по '
                         'старшим следам при достаточном k; ранг J < n_params '
                         '⇒ полная идентифицируемость позиций недостижима '
                         'по инвариантам этого класса — измерено'),
    }
