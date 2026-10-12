"""V16: полный гамильтониан × полная алгебраическая функция (живой пересчёт).

Проверяет:
  1. Спектр одной точки пространства ручек корректен (unfold, KS, r_mean).
  2. Метрика выравнивания r_align ∈ [−1, 1] и воспроизводима.
  3. Перестановочная null-модель даёт конечный z-счёт.
  4. Тождество в ПОЛНОМ пространстве ручек НЕ замыкается
     (главный результат V16: z_best < 6 — алгебраическая функция
      необходима, произвольная ручка её не воспроизводит).
"""
import numpy as np

from rpbridge.fullham import (gate_spectrum_full, align_metric,
                             permutation_null, handle_grid)
from rpbridge.zeros import load_zeros


def _zeros():
    return load_zeros(nmax=400)


def test_handle_grid_shape():
    g = handle_grid()
    assert len(g) == 96
    keys = set(g[0].keys())
    assert {'signs', 'profile', 'aniso', 'mass', 'twist', 'dalpha'} <= keys


def test_single_config_spectrum():
    z = _zeros()
    u, d_ks, r_mean = gate_spectrum_full(z, 96)
    assert len(u) >= 100
    assert np.isfinite(u).all()
    assert 0.0 <= d_ks <= 1.0
    assert 0.4 < r_mean < 0.6  # развёртка близка к равномерной


def test_align_metric_bounded_and_reproducible():
    z = _zeros()
    u, _, _ = gate_spectrum_full(z, 96)
    r1, rmse1 = align_metric(u, z)
    r2, rmse2 = align_metric(u, z)
    assert -1.0 <= r1 <= 1.0
    assert rmse1 >= 0.0
    assert r1 == r2 and rmse1 == rmse2  # детерминизм


def test_permutation_null_finite():
    z = _zeros()
    u, _, _ = gate_spectrum_full(z, 96)
    nm, nsd = permutation_null(u, z, n_perm=40)
    assert np.isfinite(nm) and nsd > 0


def test_identity_does_not_close_full_space():
    """Главный результат V16: z_best < 6 — тождество не замыкается.

    Это НЕ дефект, а карта честности: полная ручка гамильтониана без
    алгебраической функции не воспроизводит Z_id (позитивный контроль
    внутри run() при этом даёт r = 1.0).
    """
    from rpbridge.fullham import run as run_v16
    v = run_v16(_zeros(), full=False)
    assert v['summary']['identity_closed'] is False
    assert v['summary']['z_best'] < 6.0
    assert len(v['rows']) == 6
    # вес-сравнение присутствует для theta/logzeta/none
    assert set(v['weight_compare'].keys()) == {'theta', 'logzeta', 'none'}
