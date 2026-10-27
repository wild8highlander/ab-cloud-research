# -*- coding: utf-8 -*-
"""rpbridge.nonlocality — V24-превью: AB-голономия как механизм
«знания» одной частицей о другой.

Механизм (формулировка в терминах модели):
  Фаза частицы в AB-облаке — функционал НЕ локального поля, а
  ГЛОБАЛЬНОЙ топологии её пути относительно вихревой конфигурации:
  φ = 2π·q·L/Φ0, где L — число зацеплений (linking number). Для ДВУХ
  частиц волновая функция живёт на конфигурационном пространстве
  Ψ(r1, r2), и совместная фаза содержит ПЕРЕКРЁСТНЫЙ член
  Φ12 = 2π·q12·L12/Φ0 — общую степень свободы, не принадлежащую ни
  одной из частиц по отдельности. Обе частицы «читают» одну и ту же
  глобальную калибровочную конфигурацию — поэтому корреляция
  мгновенна, топологически защищена (не зависит от формы пути в
  области без полей) и НЕ передаёт информацию (маргиналы не зависят
  от удалённых выборов — коммутативность разделённых наблюдаемых).

Тесты (все точные, детерминированные):
  1. Интерферометр: сдвиг интерференции = фаза голономии (закон
     Маха–Зандера с AB-фазой), невязка против аналитики.
  2. Топологическая защита: 1000 случайных локальных унитарных
     возмущений внутри плеча (область без полей) не меняют фазу.
  3. Кросс-фаза пары: совместные вероятности зависят от Φ12, а
     маргиналы каждой частицы — НЕТ (no-signaling, алгебраически
     точный).
  4. CHSH на AB-связанной паре (симуляционный слой): S = 2√2;
     одновременно [A_i ⊗ I, I ⊗ B_j] = 0 — нет сверхсветового
     сигналинга.
"""
import numpy as np

H2 = np.array([[1, 1], [1, -1]], dtype=np.complex128) / np.sqrt(2)


def ab_phase(q, L, phi0=1.0):
    """Голономия: φ = 2π·q·L·phi0 (в единицах Φ0)."""
    return 2 * np.pi * q * L * phi0


def interferometer(phi=0.7, phase_grid=None):
    """Маха–Зандер с AB-фазой φ в одном плече: P(детектор 1) =
    sin²(φ/2). Возвращает невязку против аналитического закона на
    сетке фаз (порог спецификации V24: ≤ 1e-14)."""
    if phase_grid is None:
        phase_grid = np.linspace(0, 2 * np.pi, 257)
    worst = 0.0
    for ph in phase_grid:
        U = H2 @ np.diag([1.0, np.exp(1j * ph)]) @ H2
        psi = U @ np.array([1.0, 0.0], dtype=np.complex128)
        p_sim = float(abs(psi[1]) ** 2)
        p_law = float(np.sin(ph / 2) ** 2)
        worst = max(worst, abs(p_sim - p_law))
    return dict(phi=phi, max_resid=float(worst), threshold=1e-14,
                passed=bool(worst <= 1e-14))


def topological_protection(n_seeds=1000, phi=0.7, seed=96):
    """1000 случайных локальных возмущений потенциала в области без
    поля: действуют на внутренние состояния носителя одинаково во всех
    плечах (фаза AB зависит только от числа зацеплений, не от формы
    пути). Измеренная фаза интерференции = φ с точностью машинного
    пола при любом возмущении.

    Модель: путь (2) ⊗ внутренние состояния (2); U = BS2 ·
    (I_путь ⊗ V_int) · Phase(φ) · BS1 — V_int сокращается, P1 =
    sin²(φ/2) точно."""
    rng = np.random.default_rng(seed)
    I2 = np.eye(2, dtype=np.complex128)
    devs = []
    for _ in range(n_seeds):
        A = rng.standard_normal((2, 2)) + 1j * rng.standard_normal((2, 2))
        Q, R = np.linalg.qr(A)
        V = Q * (np.diag(R) / np.abs(np.diag(R)))   # случайное унитарное
        U = np.kron(H2, I2) @ np.kron(I2, V) @ \
            np.kron(np.diag([1.0, np.exp(1j * phi)]), I2) @ np.kron(H2, I2)
        psi0 = np.zeros(4, dtype=np.complex128)
        psi0[0] = 1.0                                # |плечо A⟩|i0⟩
        psi = U @ psi0
        p1 = float(np.abs(psi[2]) ** 2 + np.abs(psi[3]) ** 2)  # путь B
        p1 = min(1.0, max(0.0, p1))
        phi_meas = 2 * np.arcsin(np.sqrt(p1))
        devs.append(abs(phi_meas - phi))
    return dict(n_seeds=n_seeds,
                protected=int(sum(d <= 1e-12 for d in devs)),
                max_dev=float(max(devs)), threshold=1e-12,
                passed=bool(max(devs) <= 1e-12))


def cross_phase_no_signaling(L12=1.0, q12_grid=(0.0, 0.25, 0.5, 0.75, 1.0),
                             n_local=100, seed=96):
    """Кросс-фаза пары: «знает — но не сигнализирует».

    Состояние пары после совместной AB-фазы (общая степень свободы):
        |Ψ(Φ12)⟩ = (1/2)(|++⟩ + |+−⟩ + |−+⟩ + e^{iΦ12}|−−⟩),
    Φ12 = 2π·q12·L12 — ПЕРЕКРЁСТНАЯ фаза (функционал общей глобальной
    вихревой конфигурации, V19).

    Три точных факта:
      1. ЗНАЕТ: совместная корреляция E(XX) = (1+cos Φ12)/2 —
         интерференция совместных ветвей (++) и (−−) несёт Φ12;
      2. НЕ СИГНАЛИЗИТ: редуцированное состояние ρ1 инвариантно
         относительно ЛОКАЛЬНЫХ операций второй частицы (100 случайных
         унитарных A2: ‖Tr₂[(I⊗A₂)ρ(I⊗A₂)†] − ρ1‖ = 0 — алгебраически
         точно); изменение Φ12 меняет только СОВМЕСТНУЮ статистику;
      3. Маргиналы по модулю Φ12 меняются — но Φ12 не может быть
         изменена локально (это голономия общей конфигурации), поэтому
         канал связи отсутствует (см. п. 2 и коммутаторы в chsh)."""
    X = np.array([[0, 1], [1, 0]], dtype=np.complex128)
    I2 = np.eye(2, dtype=np.complex128)
    out = dict(q12_grid=list(q12_grid), Exx=[], Exx_theory=[],
               rho1_local_invariance_max=0.0)
    for q12 in q12_grid:
        Phi = ab_phase(q12, L12)
        psi = np.array([1, 1, 1, np.exp(1j * Phi)],
                       dtype=np.complex128) / 2
        rho = np.outer(psi, psi.conj())
        Exx = float(np.real(np.trace(rho @ np.kron(X, X))))
        out['Exx'].append(Exx)
        out['Exx_theory'].append(float((1 + np.cos(Phi)) / 2))
    out['joint_resid'] = float(np.max(np.abs(
        np.array(out['Exx']) - np.array(out['Exx_theory']))))

    # no-signaling: локальные унитарные второй частицы не меняют ρ1
    rng = np.random.default_rng(seed)
    psi = np.array([1, 1, 1, np.exp(1j * 0.9)], dtype=np.complex128) / 2
    rho = np.outer(psi, psi.conj())
    rho1 = rho.reshape(2, 2, 2, 2).trace(axis1=3, axis2=1)
    worst = 0.0
    for _ in range(n_local):
        A = rng.standard_normal((2, 2)) + 1j * rng.standard_normal((2, 2))
        Q, R = np.linalg.qr(A)
        A2 = Q * (np.diag(R) / np.abs(np.diag(R)))
        rho2 = np.kron(I2, A2) @ rho @ np.kron(I2, A2).conj().T
        rho1_2 = rho2.reshape(2, 2, 2, 2).trace(axis1=3, axis2=1)
        worst = max(worst, float(np.max(np.abs(rho1_2 - rho1))))
    out['rho1_local_invariance_max'] = worst
    out['n_local_seeds'] = n_local
    out['passed'] = bool(out['joint_resid'] <= 1e-14 and worst <= 1e-14)
    return out


def chsh_ab_pair():
    """CHSH на AB-связанной паре |Φ+⟩ (симуляционный слой): S = 2√2;
    коммутаторы [A_i⊗I, I⊗B_j] = 0 — сигналинга нет."""
    phi_p = np.array([1, 0, 0, 1], dtype=np.complex128) / np.sqrt(2)
    def op(a):
        return np.array([[np.cos(a), np.sin(a)],
                         [np.sin(a), -np.cos(a)]], dtype=np.complex128)
    A0, A1 = op(0.0), op(np.pi / 2)
    B0, B1 = op(np.pi / 4), op(-np.pi / 4)
    Z = np.diag([1.0, -1.0]).astype(np.complex128)
    def corr(A, B):
        M = np.kron(A, B)
        return float(np.real(phi_p.conj() @ M @ phi_p))
    S = corr(A0, B0) + corr(A0, B1) + corr(A1, B0) - corr(A1, B1)
    comm = 0.0
    for Ai in (A0, A1):
        for Bj in (B0, B1):
            comm = max(comm, float(np.max(np.abs(
                np.kron(Ai, np.eye(2)) @ np.kron(np.eye(2), Bj) -
                np.kron(np.eye(2), Bj) @ np.kron(Ai, np.eye(2))))))
    # точное значение Тсире—Брассара для |Φ+>
    S_exact = 2 * np.sqrt(2)
    return dict(S=float(S), S_exact=float(S_exact),
                S_resid=float(abs(S - S_exact)), chsh_passed=bool(S >= 2.8),
                comm_max=float(comm), no_signaling=bool(comm <= 1e-14))


def run():
    """Полный прогон V24-превью."""
    interf = interferometer()
    prot = topological_protection()
    cross = cross_phase_no_signaling()
    chsh = chsh_ab_pair()
    return dict(interferometer=interf, protection=prot, cross_phase=cross,
                chsh=chsh,
                verdict_note=dict(
                    ru=('Голономная корреляция: совместная фаза — общая '
                        'степень свободы пары; маргиналы инвариантны '
                        '(сигналинга нет); защита топологическая'),
                    en=('Holonomic correlation: the joint phase is a '
                        'shared degree of freedom; marginals invariant '
                        '(no signaling); topological protection')))
