"""hpbridge.alphathird — нулевые моды при α = 1/3 и арифметический мост
(C11, направление R3, теорема T13).

Наблюдение T9 (v1): на торах L ≡ 0 (mod 4) при α = 1/3 есть нулевые моды
(18 при L = 12, 42 при L = 24). Вопрос R3: арифметика ли это? Мост
«L ≡ 0 (mod 3) → дираковский индекс»: флакс-квантование на торе требует
α·L ∈ ℤ, при α = 1/3 это ровно L ≡ 0 (mod 3) — геометрическая причина.
Дираковский индекс (Кэлер–Дирак на торе) = суммарный флакс = α·L² (кратность
с учётом двойников решётки — измеряется). Кампанья сканирует L и проверяет:

  A1  торус существует ⇔ L ≡ 0 (mod 3)  — flux quantization;
  A2  число нулевых мод N₀(L) при α=1/3 — измерение, скотт-протокол;
  A3  N₀(L) против индексных кандидатов: α·L²·κ, κ — решёточный фактор;
  A4  L ≢ 0 (mod 3): торус невозможен, открытая граница — мод нет/другие.

Гамильтониан — кэлер-дираковский (стаггерд) оператор на торе с Ландау-флаксом
α: H = D_x + D_y + стаггерд-масса m(−1)^{x+y}; нулевые моды — собственные
значения |λ| ≤ tol при m = 0 (хиральный сектор).
"""
import numpy as np
from scipy.linalg import eigvalsh


def kdir_hamiltonian(L, alpha, bc="torus", m=0.0):
    """Кэлер–Дирак (стаггерд фермион) на L×L с Ландау-флаксом α.

    D — анти-эрмитов разностный оператор: D_x = ½e^{2πiα·iy}(T_x⁺),
    D_y = ½(T_y⁺) (Ландау-калибровка v1-движка: фазы на x-связях);
    торус требует α·L ∈ ℤ.
    Эрмитов гамильтониан — γ₅-эрмитова форма: H = ε·D + m,
    ε(iy,ix) = (−1)^{iy+ix} (стаггерд-структура = двухкомпонентный Дирак).
    Эрмитовость: (εD)† = D†ε = −Dε = εD (D анти-эрмитово, {ε,D} = 0).
    Нулевые моды при m = 0 — хиральные; индекс = Σ sign(ε) по нулям.
    """
    N = L * L
    idx = np.arange(N).reshape(L, L)          # idx[iy, ix]
    D = np.zeros((N, N), dtype=np.complex128)
    ph = 2.0 * np.pi * alpha * np.arange(L)
    ex = np.exp(1j * ph)
    for iy in range(L):
        for ix in range(L):
            s = idx[iy, ix]
            if ix + 1 < L:
                D[s, idx[iy, ix + 1]] = 0.5 * ex[iy]
            elif bc == "torus":
                D[s, idx[iy, 0]] = 0.5 * ex[iy]
            if iy + 1 < L:
                D[s, idx[iy + 1, ix]] = 0.5
            elif bc == "torus":
                D[s, idx[0, ix]] = 0.5
    eps = ((np.add.outer(np.arange(L), np.arange(L)) % 2) * 2.0 - 1.0)
    H = eps.ravel()[:, None] * D + m * np.eye(N)
    H = 0.5 * (H + H.conj().T)   # симметризация машинного уровня (контроль)
    return H


def zero_mode_count(L, alpha, bc="torus", tol=1e-8, m=0.0):
    """Число |λ| ≤ tol и дираковский индекс Σ sign(ε) по нулевым состояниям.

    Возвращает dict(count, index) или None, если торус не существует
    (флакс α·L ∉ ℤ — квантование не выполняется).
    """
    if bc == "torus" and abs(alpha * L - round(alpha * L)) > 1e-10:
        return None  # флакс не квантуется: торус не существует
    H = kdir_hamiltonian(L, alpha, bc, m)
    ev, vec = np.linalg.eigh(H)
    zmask = np.abs(ev) <= tol
    count = int(np.sum(zmask))
    eps = ((np.add.outer(np.arange(L), np.arange(L)) % 2) * 2.0 - 1.0)
    eps_flat = eps.ravel()
    idx = int(np.sum(eps_flat[zmask])) if count else 0
    return {"count": count, "index": idx}


def index_candidates(L, alpha=1.0 / 3.0):
    """Теоретические кандидаты на N₀: индекс Кэлера–Дирака и решёточные
    факторы. Возвращает dict с α·L², α·L²/2 (дубль-отмена), α·L²/4."""
    a2 = alpha * L * L
    return {"chiral_index_alphaL2": a2, "half": a2 / 2.0, "quarter": a2 / 4.0}


def scan_L(L_list, alpha=1.0 / 3.0, tol=1e-8):
    """Скан A1–A4 по списку L. Возвращает строки вердикта."""
    rows = []
    for L in L_list:
        t = zero_mode_count(L, alpha, "torus", tol)
        o = zero_mode_count(L, alpha, "open", tol)
        rows.append({
            "L": L, "L_mod_3": L % 3, "L_mod_4": L % 4,
            "torus_exists": t is not None,
            "n_zero_torus": None if t is None else t["count"],
            "index_torus": None if t is None else t["index"],
            "n_zero_open": None if o is None else o["count"],
            "index_open": None if o is None else o["index"],
            **{k: round(v, 3) for k, v in index_candidates(L, alpha).items()},
        })
    return rows
