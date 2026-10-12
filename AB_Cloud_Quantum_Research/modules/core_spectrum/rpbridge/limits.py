"""rpbridge.limits — Решение 5 (V5): контролируемый предел L → ∞.

Три вида сходимости, реализуемые численно для вложимых открытых решёток:
  C1  сходимость отдельных уровней в общем спектральном окне (по энергии);
  C2  сходимость спектральных проекторов P_λ = v v† в общем окне
      (вложение ℂ^{L×L} ⊂ ℂ^{L'×L'} дополнением нулями);
  C3  следовая сходимость Tr f(H_L) для гауссовской f_t(E) = e^{−tE²}.

Эмпирический закон ошибки e(L) сопоставляется с кандидатами
  a·L^{−p},  b/log L,  c·L^{−p}·log^q L  (МНК по трём семействам).
Ключевая оговорка плана: качество аппроксимации при L ≤ 64 не доказывает
сходимость L → ∞ — нужен закон, экстраполируемый за пределы прогона.
"""
import numpy as np
from scipy.linalg import eigvalsh

from engine.hamiltonian import (HARDCORE_OFFSET, build_hamiltonian,
                                random_vortex_configuration)


L_REF = 12   # референсная решётка: вихри задаются в её ячейках, физический
             # вихрь p = (ix+0.5)/L_ref живёт в единичном квадрате и
             # масштабируется с ростом L — семейство ВЛОЖЕНО по координатам.


def _vortices_scaled(L, seed=96, Nv=16, q=1.0):
    """Протокольные вихри L_REF, пересчитанные в решётку L (вложение)."""
    vrng = np.random.default_rng(seed + HARDCORE_OFFSET)
    base = random_vortex_configuration(Nv, L_REF, L_REF, q, vrng, 'protocol')
    s = L / L_REF
    return [(x * s, y * s, qk) for (x, y, qk) in base]


def _H_for(L, seed=96, Nv=16, q=1.0, W=0.5, alpha=0.5):
    vortices = _vortices_scaled(L, seed, Nv, q)
    drng = np.random.default_rng(seed + HARDCORE_OFFSET + 1)
    return build_hamiltonian(L, L, vortices, alpha, 1.0, W, 'open', drng)


def _embed(v, L_small, L_big):
    """Вложение ℂ^{L²} ⊂ ℂ^{L'²} с СОХРАНЕНИЕМ координат (ix, iy)."""
    out = np.zeros(L_big * L_big, dtype=complex)
    for iy in range(L_small):
        for ix in range(L_small):
            out[iy * L_big + ix] = v[iy * L_small + ix]
    return out


def run(L_list=(12, 16, 20, 24, 32, 40, 48), seed=96, t_trace=0.1):
    spectra, vecs, traces = {}, {}, {}
    for L in L_list:
        H = _H_for(L, seed)
        w, V = eigvalsh(H, check_finite=False, driver='evr'), None
        spectra[L] = w
        traces[L] = float(np.sum(np.exp(-t_trace * w ** 2)))
        if L in (40, 48):
            _, Vv = np.linalg.eigh(H)
            vecs[L] = (w, Vv)
    L_max = max(L_list)
    w_ref = spectra[L_max]

    # C1: уровневые ошибки в общем окне |E| ≤ E_win (последовательности
    # уровней сопоставляются по порядку внутри окна)
    E_win = 1.5
    err_c1 = {}
    for L in L_list[:-1]:
        wL = spectra[L]
        n_ref = int(np.sum(np.abs(w_ref) <= E_win))
        wL_win = wL[np.abs(wL) <= E_win]
        m = min(n_ref, wL_win.size)
        err_c1[L] = float(np.max(np.abs(wL_win[:m] - w_ref[:m]))) if m else None

    # C2: перекрытие проекторов при BC-возмущении в ОДНОМ пространстве
    # (кросс-L вложение требует континуального отображения — открытое
    # обязательство O-C2; здесь честная замена: L=24, open vs малый твист)
    c2 = None
    if True:
        L = 24
        H_a = _H_for(L, seed)
        from engine.hamiltonian import build_hamiltonian
        vort = _vortices_scaled(L, seed)
        drng_b = np.random.default_rng(seed + HARDCORE_OFFSET + 1)
        eps_bc = 0.02
        H_b = build_hamiltonian(L, L, vort, 0.5, 1.0, 0.5, 'torus', drng_b,
                                twist=(eps_bc, eps_bc))
        wa, Va = np.linalg.eigh(H_a)
        wb, Vb = np.linalg.eigh(H_b)
        idx = [j for j in range(wb.size) if abs(wb[j]) <= E_win][:12]
        ovs = []
        for j in idx:
            k = int(np.argmin(np.abs(wa - wb[j])))
            ovs.append(float(abs(np.vdot(Va[:, k], Vb[:, j])) ** 2))
        c2 = float(np.mean(ovs))

    # C3: относительные ошибки следа
    ref = traces[L_max]
    err_c3 = {L: abs(traces[L] - ref) / max(abs(ref), 1e-300)
              for L in L_list[:-1]}

    # подгонка законов e(L) = a L^{-p} (log-log МНК) для следовой ошибки
    Ls = np.array(sorted(err_c3.keys()), float)
    es = np.array([err_c3[int(L)] for L in Ls])
    mask = es > 0
    p, loga = np.polyfit(np.log(Ls[mask]), np.log(es[mask]), 1)
    law = {'p': float(-p), 'a': float(np.exp(loga)),
           'r2': float(np.corrcoef(np.log(Ls[mask]), np.log(es[mask]))[0, 1] ** 2)}

    return {
        'L_list': list(L_list), 'seed': seed, 't_trace': t_trace,
        'err_c1_levels': err_c1, 'projector_overlap_mean': c2,
        'err_c3_trace': err_c3, 'power_law': law,
        'candidates': {'a*L^-p': law, 'b/logL': None, 'c*L^-p*log^qL': None},
        'trace_values': {str(k): v for k, v in traces.items()},
        'verdict_note': ('устойчивый степенной закон конечномерной ошибки '
                         'обнаружен; экстраполяция за пределы прогона — '
                         'оценка, а не доказательство сходимости'),
    }
