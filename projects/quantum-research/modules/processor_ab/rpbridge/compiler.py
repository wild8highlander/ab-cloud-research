# -*- coding: utf-8 -*-
"""rpbridge.compiler — V20: компилятор AB-процессора.

Точная компиляция произвольной унитарной матрицы U ∈ U(d), d = 2^n,
в программу ISA {AB2, ABPH}:

  1. Givens-QR: U = G_1·…·G_k·D, где каждый G_i — двухуровневый
     блок (тождество вне пары строк (c_i, r_i)), D — диагональная
     фазовая матрица (для унитарной U R-фактор QR диагонален).
     Число Givens-вращений = число обнуляемых поддиагональных
     элементов ≤ d(d−1)/2 (для перестановочных матриц — единицы).
  2. Каждый 2×2 блок W → AB2(θ, λ, φ, χ) в замкнутой форме
     (ZXZ-Эйлер + глобальная фаза).
  3. Диагональ D → лестница фаз уровней: D = Π_x PHASE(x; φ_x)
     (в точности; элементы с |φ_x| < 1e-14 отбрасываются с оценкой
     ошибки, входящей в метрику fidelity).

Всё построение — замкнутая алгебра, без оптимизации и аппроксимации:
fidelity компиляции ограничена только машинным полом. Предрегистрированный
механизм спецификации («QR + блоки») исполнен дословно; KAK-оптимальность
глубины — обязательство P3 (V26).
"""
import numpy as np

SKIP_EPS = 1e-14


# ── AB2: 2×2 → параметры ISA ────────────────────────────────────────────────
def ab2_matrix(theta, lam, phi, chi):
    """e^{iχ}·RZ(φ)·RX(θ)·RZ(λ) — полный U(2)."""
    c, s = np.cos(theta / 2), np.sin(theta / 2)
    M = np.array([[c, -1j * s * np.exp(1j * lam)],
                  [-1j * s * np.exp(1j * phi),
                   np.exp(1j * (phi + lam)) * c]], dtype=np.complex128)
    return np.exp(1j * chi) * M


def ab2_params(W):
    """Замкнутое разложение W ∈ U(2) → (θ, λ, φ, χ).

    Структура ab2_matrix: α = e^{iχ}c, β = −is·e^{i(χ+λ)},
    γ = −is·e^{i(χ+φ)}, δ = e^{i(χ+φ+λ)}c. Ортонормированность строк
    гарантирует согласованность δ (проверяется assert-ом)."""
    alpha, beta = W[0, 0], W[0, 1]
    gamma, delta = W[1, 0], W[1, 1]
    c = float(np.clip(abs(alpha), 0.0, 1.0))
    s = np.sqrt(max(0.0, 1.0 - c * c))
    theta = 2.0 * np.arccos(c)
    if c < 1e-15:
        # θ = π: фазы несут β и γ (α = δ = 0)
        lam = float(np.angle(beta / (-1j)))
        phi = float(np.angle(gamma / (-1j)))
        W2 = ab2_matrix(theta, lam, phi, 0.0)
        assert abs(np.trace(W2.conj().T @ W)) > 2 - 1e-9
        return (theta, lam, phi, 0.0)
    chi = float(np.angle(alpha))
    if s < 1e-15:
        phi = float(np.angle(delta) - chi)
        return (theta, 0.0, phi, chi)
    lam = float(np.angle(beta / (-1j * s)) - chi)
    phi = float(np.angle(gamma / (-1j * s)) - chi)
    W2 = ab2_matrix(theta, lam, phi, chi)
    assert abs(np.trace(W2.conj().T @ W)) > 2 - 1e-9, 'AB2 param mismatch'
    return (theta, lam, phi, chi)


# ── Givens-QR: U → [двухуровневые блоки] · D ────────────────────────────────
def givens_decompose(U):
    """U = B_1·B_2·…·B_k·D, где каждый B_i = W_i† — двухуровневый
    блок (тождество вне пары строк (c_i, r_i)), D — диагональная
    фазовая матрица (для унитарной U R-фактор QR диагонален).
    Возвращает (blocks, diag), blocks = [(c, r, B2)] в порядке B_1…B_k."""
    R = np.array(U, dtype=np.complex128, copy=True)
    d = R.shape[0]
    blocks = []
    for c in range(d - 1):
        for r in range(d - 1, c, -1):
            a, b = R[c, c], R[r, c]
            if abs(b) < 1e-300:
                continue
            nrm = np.sqrt(abs(a) ** 2 + abs(b) ** 2)
            W = np.array([[np.conj(a), np.conj(b)],
                          [-b, a]], dtype=np.complex128) / nrm
            rows = np.array([a, b], dtype=np.complex128)
            new = W @ rows
            R[c, c], R[r, c] = new[0], new[1]
            # полная работа со столбцами c+1..d-1 и строками c,r:
            sub = W @ R[[c, r], c + 1:]
            R[c, c + 1:] = sub[0]
            R[r, c + 1:] = sub[1]
            blocks.append((c, r, W.conj().T))   # U = B_1…B_k·D
    diag = np.diag(R).copy()
    # строгая унитарность R-фактора: вне диагонали всё занулено
    off = R - np.diag(diag)
    assert np.max(np.abs(off)) < 1e-10, 'QR of unitary must be diagonal'
    return blocks, diag


# ── диагональ → фазы уровней PHASE ────────────────────────────────────
def diagonal_to_phases(diag, n):
    """D = Π_x PHASE(x; φ_x) — прямое разложение диагонали на фазы
    уровней (φ_x = arg D_xx, приведены в (−π, π]).

    Возвращает [(x, phi)] c |phi| ≥ SKIP_EPS; отброшенная масса фаз
    возвращается как max_skipped (входит в метрику fidelity)."""
    d = 1 << n
    ph = np.angle(np.asarray(diag, dtype=np.complex128))
    ph = (ph + np.pi) % (2 * np.pi) - np.pi
    out = []
    max_skipped = 0.0
    for x in range(d):
        if abs(ph[x]) >= SKIP_EPS:
            out.append((x, float(ph[x])))
        else:
            max_skipped = max(max_skipped, abs(ph[x]))
    return out, max_skipped


# ── сборка и исполнение программы ISA ───────────────────────────────────────
def compile_unitary(U, n):
    """Полная компиляция: программа (список ops в ПОРЯДКЕ ВРЕМЕНИ)
    + справочная диагональ.

    ops: ('PHASE', x, psi) — фаза уровня x (селективный детюнинг);
         ('AB2', c, r, theta, lam, phi, chi) — двухуровневый блок на
         строках/столбцах (c, r) с матрицей e^{iχ}RZ(φ)RX(θ)RZ(λ).

    Временнóй порядок: сначала фазы уровней (D), затем блоки в
    обратном порядке (B_k, …, B_1) — так что итоговый оператор
    программы равен B_1·…·B_k·D' = U (D' — диагональ из фаз программы;
    отброшенные микроскопические фазы входят в fidelity честно)."""
    d = 1 << n
    U = np.asarray(U, dtype=np.complex128)
    assert U.shape == (d, d)
    blocks, diag = givens_decompose(U)
    ph_list, max_skipped = diagonal_to_phases(diag, n)
    program = [('PHASE', int(x), float(psi)) for x, psi in ph_list]
    cost_2q = 0          # эквивалент двухкубитных блоков (маршрутизация)
    for (c, r, B) in reversed(blocks):
        theta, lam, phi, chi = ab2_params(B)
        program.append(('AB2', int(c), int(r), float(theta), float(lam),
                        float(phi), float(chi)))
        h = bin(c ^ r).count('1')
        cost_2q += 1 if h == 1 else 2 * h - 1   # CNOT-маршрутизация до dist 1
    costs = dict(n_gates=len(program),
                 n_ab2=sum(1 for op in program if op[0] == 'AB2'),
                 n_phase=sum(1 for op in program if op[0] == 'PHASE'),
                 two_qubit_equiv=cost_2q,
                 max_diag_skip=max_skipped)
    return dict(program=program, diag=np.asarray(diag), costs=costs)


def _block_matrix(d, c, r, theta, lam, phi, chi):
    M = np.eye(d, dtype=np.complex128)
    W = ab2_matrix(theta, lam, phi, chi)
    M[np.ix_([c, r], [c, r])] = W
    return M


def program_matrix(comp, n):
    """Матрица того, что исполняет процессор: произведение операций
    программы в порядке времени (фазы уровней применяются первыми,
    затем блоки в обратном порядке). Отброшенные микроскопические
    фазы не применяются — их вклад честно входит в fidelity."""
    d = 1 << n
    V = np.eye(d, dtype=np.complex128)
    for op in comp['program']:
        if op[0] == 'AB2':
            _, c, r, th, lm, ph, ch = op
            V = _block_matrix(d, c, r, th, lm, ph, ch) @ V
        else:
            _, x, psi = op
            V = _phase_matrix(n, x, psi) @ V
    return V


def _phase_matrix(n, x, psi):
    D = np.ones(1 << n, dtype=np.complex128)
    if x > 0:
        D[x] = np.exp(1j * psi)
    return np.diag(D)


def program_state(comp, n, psi0):
    """Исполнение программы на векторе состояния (память/ALU-слой).
    Применяются только операции программы (без внешней диагонали) —
    то, что реально исполняет процессор."""
    psi = np.array(psi0, dtype=np.complex128, copy=True)
    for op in comp['program']:
        if op[0] == 'AB2':
            _, c, r, th, lm, ph, ch = op
            i, j = psi[c].copy(), psi[r].copy()
            W = ab2_matrix(th, lm, ph, ch)
            psi[c] = W[0, 0] * i + W[0, 1] * j
            psi[r] = W[1, 0] * i + W[1, 1] * j
        else:
            _, x, psi_ph = op
            if x > 0:
                psi[x] *= np.exp(1j * psi_ph)
    return psi


def fidelity(U, V):
    """F = |Tr(V†U)|²/d² (глобальная фаза не влияет)."""
    d = U.shape[0]
    return float(abs(np.trace(np.conj(V.T) @ U)) ** 2 / (d * d))


def haar_unitary(rng, d):
    """Хаар-случайная унитарная (QR Ginibre с фазовой нормировкой)."""
    A = (rng.standard_normal((d, d)) +
         1j * rng.standard_normal((d, d))) / np.sqrt(2)
    Q, R = np.linalg.qr(A)
    ph = np.diag(R) / np.abs(np.diag(R))
    return Q * ph
