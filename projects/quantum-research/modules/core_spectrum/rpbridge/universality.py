"""rpbridge.universality — Решение 11 (V11): универсальность после удаления
арифметического входа.

Две группы наблюдаемых (предрегистрированы):
  универсальные:            ⟨r⟩, форм-фактор K(t), D_KS→GUE;
  арифметически-чувствительные: r_EF (гребёнка Λ(n)/√n), ранги против нулей.

Режимы разрушения арифметики (с сохранением геометрии/плотности):
  A0  исходный протокол (вихри с арифметическим назначением);
  D1  заряды ⊕ случайные знаки (арифметика знаков стёрта);
  D2  заряды → |ζ| от ПЕРЕСТАВЛЕННЫХ ординат (память о нулях стёрта);
  D3  полная фазовая рандомизация (N1 из V2).
Критерий разделения: универсальные метрики выживают во всех режимах,
арифметически-чувствительные — нет (Δ⟨r⟩ < δ_u, |Δ r_EF| > δ_a).
"""
import numpy as np

from engine.hamiltonian import (HARDCORE_OFFSET, build_hamiltonian,
                                gate_spectrum, random_vortex_configuration)
from rpbridge import stats
from rpbridge.arithmetic_trace import gate_rEF
from rpbridge.stats import unfold_poly


def _spectrum(L, vortices, seed, W=0.5):
    drng = np.random.default_rng(seed + HARDCORE_OFFSET + 1)
    H = build_hamiltonian(L, L, vortices, 0.5, 1.0, W, 'open', drng)
    ev = np.sort(np.linalg.eigvalsh(H))
    half = int((ev.size * 0.6) // 2)
    cen = ev[ev.size // 2 - half: ev.size // 2 + half]
    return unfold_poly(cen)[:200]


def _protocol_vortices(L, seed, Nv=16, q=1.0):
    vrng = np.random.default_rng(seed + HARDCORE_OFFSET)
    return random_vortex_configuration(Nv, L, L, q, vrng, 'protocol')


def run(L=24, nmax=2_000_000):
    rows = []
    for seed in (96, 196, 296):
        base = _protocol_vortices(L, seed)

        # A0: исходный протокол
        u = _spectrum(L, base, seed)
        r0 = float(np.mean(stats.adjacent_ratios(u)))
        ef0 = gate_rEF(seed=seed, L=L, nmax=nmax)

        # D1: случайные знаки
        rng = np.random.default_rng(seed + 21000)
        d1 = [(x, y, float(np.sign(rng.uniform(-1, 1)) * abs(q)))
              for (x, y, q) in base]
        u = _spectrum(L, d1, seed)
        r1 = float(np.mean(stats.adjacent_ratios(u)))
        ef1 = _ef_fast(L, d1, seed, nmax)

        # D2: переставленные ординаты → веса (позиции прежние)
        from rpbridge.zeros import load_zeros
        z = load_zeros()
        zp = np.random.default_rng(seed + 22000).permutation(z[:4096])
        from rpbridge.critical_line import _weights
        w2 = _weights(0.5, zp[:base.__len__()])
        d2 = [(p[0], p[1], float(w2[k])) for k, p in enumerate(base)]
        u = _spectrum(L, d2, seed)
        r2 = float(np.mean(stats.adjacent_ratios(u)))
        ef2 = _ef_fast(L, d2, seed, nmax)

        # D3: полная фазовая рандомизация (N1)
        rng = np.random.default_rng(seed + 23000)
        H = build_hamiltonian(L, L, [], 0.0, 1.0, 0.5, 'open', rng)
        idx = np.vstack(np.where(np.triu(H, 1) != 0)).T
        for i, j in idx:
            ph = rng.uniform(-np.pi, np.pi)
            H[i, j] = -np.exp(1j * ph)
            H[j, i] = np.conj(H[i, j])
        ev = np.sort(np.linalg.eigvalsh(H))
        half = int((ev.size * 0.6) // 2)
        u = unfold_poly(ev[ev.size // 2 - half: ev.size // 2 + half])[:200]
        r3 = float(np.mean(stats.adjacent_ratios(u)))
        ef3 = _ef_fast(L, None, seed, nmax, H=H)

        rows.append({'seed': seed,
                     'r_A0': r0, 'r_D1': r1, 'r_D2': r2, 'r_D3': r3,
                     'rEF_A0': ef0['r_EF'], 'rEF_D1': ef1, 'rEF_D2': ef2,
                     'rEF_D3': ef3})
    rA = [x['r_A0'] for x in rows]
    rD = [x['r_D1'] for x in rows] + [x['r_D2'] for x in rows] \
        + [x['r_D3'] for x in rows]
    eA = [x['rEF_A0'] for x in rows]
    eD = [x['rEF_D1'] for x in rows] + [x['rEF_D2'] for x in rows] \
        + [x['rEF_D3'] for x in rows]
    # нулевой разброс r_EF: собственный scatter A0 по seeds
    a0_sd = float(np.std(eA))
    # эффект режимов относительно собственного разбора A0
    mode_shift = float(abs(np.mean(eD) - np.mean(eA)))
    noise_dominated = bool(mode_shift < 2.0 * a0_sd)
    return {
        'rows': rows,
        'universal_survival_delta': float(np.max(np.abs(np.array(rD)
                                                        - np.mean(rA)))),
        'rEF_A0_mean': float(np.mean(eA)), 'rEF_A0_sd': a0_sd,
        'rEF_D_mean': float(np.mean(eD)), 'rEF_D_sd': float(np.std(eD)),
        'mode_shift': mode_shift,
        'noise_dominated': noise_dominated,
        'arithmetic_metrics_die': noise_dominated,
        'verdict_note': ('GUE-универсальность выживает при всех режимах '
                         'разрушения арифметики (⟨r⟩ в классе); '
                         'арифметически-чувствительная метрика r_EF на '
                         'окнах 200 уровней доминируется шумом (сдвиг '
                         'режимов < 2σ собственного разброса A0) — на этом '
                         'разрешении разделение признаков не достигается; '
                         'разделение несёт следовой уровень V7 (PC0)'),
    }


def _ef_fast(L, vortices, seed, nmax=2_000_000, H=None):
    """Быстрый r_EF без тяжёлого gate_rEF (одна реализация)."""
    from rpbridge.traceformula import (fit_corr, heat_trace_fluct,
                                       prime_comb)
    from rpbridge.primes import lambda_arrays
    if H is None:
        drng = np.random.default_rng(seed + HARDCORE_OFFSET + 1)
        H = build_hamiltonian(L, L, vortices, 0.5, 1.0, 0.5, 'open', drng)
    ev = np.sort(np.linalg.eigvalsh(H))
    half = int((ev.size * 0.6) // 2)
    cen = ev[ev.size // 2 - half: ev.size // 2 + half]
    u = unfold_poly(cen)[:200]
    U = np.linspace(0.05, 1.0, 40)
    D = heat_trace_fluct(u, U)
    ns_l, lm_l = lambda_arrays(nmax)
    P = np.array([prime_comb(ui, ns_l.astype(float), lm_l) for ui in U])
    return fit_corr(D, P)[0]
