"""V17: электрон на критической прямой (живой пересчёт, редуцированный).

Проверяет:
  1. Оператор эрмитов во всех трёх режимах облака.
  2. Динамика честная: дрейф энергии < 1e-10.
  3. ζ-облако направляет пакет сильнее случайного (ratio > 1).
  4. Отклонение по y у ζ-облака больше случайного (эффект C7 эталона).
"""
import numpy as np

from rpbridge.electron import (build_operator, propagate, run as run_v17,
                               _gaussian_packet, LX, LY, SIGMA0, K0,
                               Y_CENTER)
from rpbridge.zeros import load_zeros


def _zeros():
    return load_zeros(nmax=400)


def test_operators_hermitian():
    z = _zeros()
    for mode in ('clean', 'random', 'zeta'):
        H = build_operator(mode, z)
        eps = float(np.max(np.abs(H - H.conj().T)))
        assert eps < 1e-13, (mode, eps)


def test_honest_dynamics_energy():
    z = _zeros()
    H = build_operator('zeta', z)
    psi0 = None
    psi0 = _gaussian_packet(LX, LY, 8.0, Y_CENTER, SIGMA0, K0)
    times = np.linspace(0.0, 4.0, 21)
    traj, E0, _ = propagate(H, psi0, times)
    dE = max(abs(e - E0) / abs(E0) for e in traj['E'])
    assert dE < 1e-10, dE
    assert len(traj['x']) == 21


def test_zeta_cloud_steers():
    v = run_v17(_zeros(), full=False)
    s = v['summary']
    assert s['ratio_zeta_over_random'] > 1.0
    assert s['energy_max_dev'] < 1e-10


def test_y_deflection_like_C7():
    v = run_v17(_zeros(), full=False)
    s = v['summary']
    assert s['Dy_zeta'] > s['Dy_random']


def test_phase_correlation_present():
    v = run_v17(_zeros(), full=False)
    s = v['summary']
    for k in ('r_phase_zeta', 'r_phase_random'):
        assert -1.0 <= s[k] <= 1.0
