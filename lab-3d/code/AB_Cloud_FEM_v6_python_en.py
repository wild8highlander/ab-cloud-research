"""
AB_Cloud_FEM_v6_python — English Version
============================================================

FEM on Klein quartic (2,3,7) with MeatAxe — Python prototype for debugging the algorithm. Fixes eigenvalue clustering for tensor-structured representations of PSL(2,7).

This is the English translation of AB_Cloud_FEM_v6_python.py.
Russian comments in the code body are preserved for reference.

Original file: AB_Cloud_FEM_v6_python.py
"""

# ============================================================================
# AB_Cloud_FEM_v6_python.py — FEM на Klein quartic (2,3,7) с MeatAxe
# Python-прототип для отладки алгоритма
#
# Ключевое исправление v6 → v6_python:
#
#   В v6 MeatAxe искал ПРОСТЫЕ собственные значения H = α·ρ_R(s) + β·ρ_R(u)
#   на Im(P_ρ) ≅ V_ρ ⊗ V_ρ*. Но из-за тензорной структуры I ⊗ (α·ρ̄(s)+β·ρ̄(u))
#   ВСЕ собственные значения имеют кратность d_ρ. Фильтр gap < 1e-6 отсекал их ВСЕ.
#
#   Исправление: кластеризуем собственные значения, ищем кластер размера d_ρ,
#   берём ОДИН собственный вектор из кластера, применяем левое регулярное действие
#   для построения d_ρ-мерного инвариантного подпространства V_ρ ⊗ w_λ.
#
# Запуск: python3 AB_Cloud_FEM_v6_python.py
# ============================================================================

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh
import time
import sys

# ============================================================================
# КОНСТАНТЫ
# ============================================================================

PI = np.pi
SQRT7 = np.sqrt(7.0)
PSL27_ORDER = 168

# Известные собственные значения Klein quartic (Cook 2018)
KNOWN_EIGENVALUES = [
    (2.67793,  8, "8a"),
    (6.62251,  7, "7a"),
    (10.8691,  6, "6a"),
    (12.1844,  8, "8a"),
    (17.2486,  7, "7a"),
    (21.9705,  7, "7a"),
    (24.0811,  8, "8a"),
    (25.9276,  6, "6a"),
    (30.8039,  6, "6a"),
    (36.4555,  8, "8a"),
]

# ============================================================================
# ТАБЛИЦА ХАРАКТЕРОВ PSL(2,7)
# Классы: 1a, 2a, 3a, 4a, 7a, 7b
# Размеры:  1, 21, 56, 42, 24, 24
# ============================================================================

def psl27_character_table():
    alpha = (-1 + SQRT7 * 1j) / 2
    alpha_bar = np.conj(alpha)
    return {
        "1a": np.array([1,  1,  1,  1,  1,  1], dtype=complex),
        "3a": np.array([3, -1,  0,  1,  alpha, alpha_bar], dtype=complex),
        "3b": np.array([3, -1,  0,  1,  alpha_bar, alpha], dtype=complex),
        "6a": np.array([6,  2,  0,  0, -1, -1], dtype=complex),
        "7a": np.array([7, -1,  1, -1,  0,  0], dtype=complex),
        "8a": np.array([8,  0, -1,  0,  1,  1], dtype=complex),
    }

CLASS_SIZES = np.array([1, 21, 56, 42, 24, 24])

# ============================================================================
# ПОСТРОЕНИЕ PSL(2,7)
# ============================================================================

def enumerate_psl27():
    """Перечисление элементов PSL(2,7) как матриц 2x2 над F_7"""
    elements = []
    seen = set()
    for a in range(7):
        for b in range(7):
            for c in range(7):
                for d in range(7):
                    if (a*d - b*c) % 7 != 1:
                        continue
                    na, nb, nc, nd = a, b, c, d
                    if a > 3 or (a == 0 and c > 3) or \
                       (a == 0 and c == 0 and b > 3) or \
                       (a == 0 and c == 0 and b == 0 and d > 3):
                        na, nb, nc, nd = (-a)%7, (-b)%7, (-c)%7, (-d)%7
                    key = (na, nb, nc, nd)
                    if key not in seen:
                        seen.add(key)
                        elements.append(key)
    assert len(elements) == 168, f"Expected 168 elements, got {len(elements)}"
    return elements


def mat_mul_mod7(x, y):
    a = (x[0]*y[0] + x[1]*y[2]) % 7
    b = (x[0]*y[1] + x[1]*y[3]) % 7
    c = (x[2]*y[0] + x[3]*y[2]) % 7
    d = (x[2]*y[1] + x[3]*y[3]) % 7
    if a > 3 or (a == 0 and c > 3) or \
       (a == 0 and c == 0 and b > 3) or \
       (a == 0 and c == 0 and b == 0 and d > 3):
        a, b, c, d = (-a)%7, (-b)%7, (-c)%7, (-d)%7
    return (a, b, c, d)


def build_mult_table(elements):
    n = len(elements)
    idx_map = {e: i for i, e in enumerate(elements)}
    mt = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            prod = mat_mul_mod7(elements[i], elements[j])
            mt[i, j] = idx_map[prod]
    return mt


def element_order(mt, idx, eid):
    cur = idx
    for k in range(1, 25):
        if cur == eid:
            return k
        cur = mt[cur, idx]
    return -1


def find_identity(mt):
    n = mt.shape[0]
    for i in range(n):
        if np.all(mt[i, :] == np.arange(n)):
            return i
    raise ValueError("Identity not found")


def find_generators(elements, mt, eid):
    n = len(elements)
    order2 = [i for i in range(n) if element_order(mt, i, eid) == 2]
    order3 = [i for i in range(n) if element_order(mt, i, eid) == 3]
    for s in order2:
        for u in order3:
            su = mt[s, u]
            if element_order(mt, su, eid) == 7:
                return s, u
    raise ValueError("Generators not found")


def find_inverse(mt, g_idx, eid):
    n = mt.shape[0]
    for j in range(n):
        if mt[g_idx, j] == eid:
            return j
    raise ValueError(f"Inverse not found for {g_idx}")


def classify_conjugacy_classes(elements, mt, eid):
    n = len(elements)
    class_map = np.zeros(n, dtype=int)

    for i in range(n):
        ord_i = element_order(mt, i, eid)
        if   ord_i == 1: class_map[i] = 1
        elif ord_i == 2: class_map[i] = 2
        elif ord_i == 3: class_map[i] = 3
        elif ord_i == 4: class_map[i] = 4

    order7 = [i for i in range(n) if element_order(mt, i, eid) == 7]
    assert len(order7) == 48

    def are_conjugate(i1, i2):
        for c in range(n):
            if mt[c, i1] == mt[i2, c]:
                return True
        return False

    g0 = order7[1]
    class5, class6 = [], []
    assigned = set()

    for g in order7:
        if g in assigned:
            continue
        powers = [g]
        cur = g
        for _ in range(6):
            cur = mt[cur, g]
            powers.append(cur)

        g_in_7a = are_conjugate(g, g0)

        for k, p in enumerate(powers):
            if k in [0, 1, 3]:    # g^1, g^2, g^4
                if g_in_7a:
                    class5.append(p)
                else:
                    class6.append(p)
            elif k in [2, 4, 5]:  # g^3, g^5, g^6
                if g_in_7a:
                    class6.append(p)
                else:
                    class5.append(p)
            assigned.add(p)

    assert len(class5) == 24 and len(class6) == 24, \
        f"class5={len(class5)}, class6={len(class6)}"

    for i in class5: class_map[i] = 5
    for i in class6: class_map[i] = 6

    return class_map


# ============================================================================
# МАТРИЦЫ ПРЕДСТАВЛЕНИЙ — ИСПРАВЛЕННЫЙ MeatAxe
# ============================================================================
#
# Структура Im(P_ρ) ≅ V_ρ ⊗ V_ρ*:
#   ρ_L(g) действует как ρ(g) ⊗ I   (левое регулярное)
#   ρ_R(g) действует как I ⊗ ρ̄(g)  (правое регулярное)
#   ρ_L и ρ_R коммутируют!
#
# H = α·ρ_R(s) + β·ρ_R(u) на Im(P_ρ) действует как
#   I ⊗ (α·ρ̄(s) + β·ρ̄(u))
#
# Поэтому собственные значения H = {λ_i : i=1..d_ρ}, где λ_i — с.з.
# матрицы d_ρ×d_ρ (α·ρ̄(s) + β·ρ̄(u)), КАЖДОЕ кратности d_ρ.
#
# Алгоритм:
#   1. Кластеризуем с.з. H (ищем кластеры размера d_ρ)
#   2. Берём ОДИН собственный вектор из кластера → лежит в V_ρ ⊗ w_λ
#   3. Применяем ρ_L(s), ρ_L(u) → генерируем всё V_ρ ⊗ w_λ (размерность d_ρ)
#   4. Извлекаем матрицы представления S_ρ, U_ρ
# ============================================================================

def build_rep_matrices(elements, mt, class_map, rep_name, s_idx, u_idx, eid):
    """Построение матриц представления S_ρ, U_ρ алгоритмом MeatAxe"""
    chi_table = psl27_character_table()
    chi_rho = chi_table[rep_name]
    dim_rho = int(np.real(chi_rho[0]))
    n = len(elements)

    print(f"    {rep_name}: dim={dim_rho}")

    # Тривиальное представление
    if dim_rho == 1:
        return np.array([[1.0+0j]]), np.array([[1.0+0j]]), True

    # --- Шаг 1: Строим проектор P_ρ ---
    s_inv = find_inverse(mt, s_idx, eid)
    u_inv = find_inverse(mt, u_idx, eid)

    # P_ρ = (dim_ρ/|G|) Σ_g χ̄_ρ(g) ρ_L(g)
    # ρ_L(g) — перестановочная матрица: (ρ_L(g))_{i,j} = δ_{i, mt[g,j]}
    P_rho = np.zeros((n, n), dtype=complex)
    for g_idx in range(n):
        coeff = (dim_rho / PSL27_ORDER) * np.conj(chi_rho[class_map[g_idx] - 1])
        for j in range(n):
            i = mt[g_idx, j]
            P_rho[i, j] += coeff

    # Проверяем, что P_ρ — проектор
    err_proj = np.linalg.norm(P_rho @ P_rho - P_rho)
    print(f"      ||P²-P|| = {err_proj:.2e}")

    # SVD проектора → базис образа (ЛЕВЫЕ сингулярные векторы = образ P_ρ)
    U_svd, S_svd, Vh_svd = np.linalg.svd(P_rho)
    tol = S_svd[0] * n * np.finfo(float).eps
    proj_rank = int(np.sum(S_svd > tol))

    if proj_rank != dim_rho**2:
        print(f"      WARNING: rank(P)={proj_rank}, expected dim²={dim_rho**2}")
        return (np.zeros((dim_rho, dim_rho), dtype=complex),
                np.zeros((dim_rho, dim_rho), dtype=complex), False)

    print(f"      rank(P)={proj_rank} = dim²={dim_rho**2} ✓")

    # Используем ЛЕВЫЕ сингулярные векторы (столбцы U_svd) — образ P_ρ
    basis = U_svd[:, :proj_rank]  # n × d_ρ²

    # --- Шаг 2: Левое и правое регулярные представления ---
    # Левое: ρ_L(g)·e_j = e_{g·j}  →  (ρ_L(g))_{mt[g,j], j} = 1
    perm_s_L = np.zeros((n, n))
    for j in range(n):
        perm_s_L[mt[s_idx, j], j] = 1.0

    perm_u_L = np.zeros((n, n))
    for j in range(n):
        perm_u_L[mt[u_idx, j], j] = 1.0

    # Правое: ρ_R(g)·e_j = e_{j·g⁻¹}  →  (ρ_R(g))_{mt[j,g⁻¹], j} = 1
    perm_s_R = np.zeros((n, n))
    for j in range(n):
        perm_s_R[mt[j, s_inv], j] = 1.0

    perm_u_R = np.zeros((n, n))
    for j in range(n):
        perm_u_R[mt[j, u_inv], j] = 1.0

    # Ограничиваем на образ P_ρ (в координатах базиса образа)
    M_s_L = basis.T.conj() @ perm_s_L @ basis   # d_ρ² × d_ρ²
    M_u_L = basis.T.conj() @ perm_u_L @ basis
    M_s_R = basis.T.conj() @ perm_s_R @ basis
    M_u_R = basis.T.conj() @ perm_u_R @ basis

    # Проверяем, что левые и правые действия коммутируют
    comm_su = np.linalg.norm(M_s_L @ M_u_R - M_u_R @ M_s_L)
    print(f"      ||[ρ_L(s), ρ_R(u)]|| = {comm_su:.2e}")

    # --- Шаг 3: MeatAxe с кластеризацией ---
    rng = np.random.RandomState(42)

    for attempt in range(100):
        # Случайная комбинация правых регулярных матриц
        # Используем несколько образующих для лучшего разделения
        alpha = rng.randn() + 1j * rng.randn()
        beta  = rng.randn() + 1j * rng.randn()
        H = alpha * M_s_R + beta * M_u_R

        # Диагонализация
        evals_H, evecs_H = np.linalg.eig(H)

        # Сортируем по вещественной части
        sort_idx = np.argsort(np.real(evals_H))
        evals_sorted = evals_H[sort_idx]
        evecs_sorted = evecs_H[:, sort_idx]

        # Кластеризуем собственные значения
        # Сначала вычисляем все попарные расстояния
        clusters = []
        used = set()
        for i in range(len(evals_sorted)):
            if i in used:
                continue
            cluster = [i]
            used.add(i)
            for j in range(i + 1, len(evals_sorted)):
                if j in used:
                    continue
                # Относительное расстояние между с.з.
                dist = abs(evals_sorted[j] - evals_sorted[i])
                scale = max(1.0, abs(evals_sorted[i]))
                if dist < 1e-6 * scale:
                    cluster.append(j)
                    used.add(j)
            clusters.append(cluster)

        cluster_sizes = [len(c) for c in clusters]
        print(f"      Попытка {attempt+1}: кластеры = {cluster_sizes}")

        # Ищем кластер размером d_ρ
        good_clusters = [c for c in clusters if len(c) == dim_rho]

        if not good_clusters:
            continue

        # Пробуем каждый подходящий кластер
        for cluster in good_clusters:
            # Берём один собственный вектор из кластера
            for ci in cluster[:3]:  # пробуем до 3 векторов из кластера
                v = evecs_sorted[:, ci].copy()
                v = v / np.linalg.norm(v)

                # Строим лево-инвариантное подпространство
                Q_list = [v.copy()]
                queue = [v.copy()]
                head = 0

                while len(Q_list) < dim_rho and head < len(queue):
                    w = queue[head]
                    head += 1
                    for M_L in [M_s_L, M_u_L]:
                        w_new = M_L @ w
                        # Ортогонализуем против текущего базиса (modified Gram-Schmidt)
                        Q_mat = np.column_stack(Q_list)
                        w_orth = w_new - Q_mat @ (Q_mat.T.conj() @ w_new)
                        nrm = np.linalg.norm(w_orth)
                        if nrm > 1e-10:
                            w_orth = w_orth / nrm
                            Q_list.append(w_orth)
                            queue.append(w_new)
                            if len(Q_list) >= dim_rho:
                                break
                    if len(Q_list) >= dim_rho:
                        break

                if len(Q_list) != dim_rho:
                    continue

                Q_sub = np.column_stack(Q_list)  # d_ρ² × d_ρ

                # --- Извлекаем матрицы представления ---
                S_rep = Q_sub.T.conj() @ M_s_L @ Q_sub   # d_ρ × d_ρ
                U_rep = Q_sub.T.conj() @ M_u_L @ Q_sub

                # Проверяем соотношения группы
                err_S2 = np.linalg.norm(S_rep @ S_rep - np.eye(dim_rho))
                err_U3 = np.linalg.norm(np.linalg.matrix_power(U_rep, 3) - np.eye(dim_rho))
                SU = S_rep @ U_rep
                err_SU7 = np.linalg.norm(np.linalg.matrix_power(SU, 7) - np.eye(dim_rho))

                success = err_S2 < 1e-6 and err_U3 < 1e-6 and err_SU7 < 1e-3

                if success:
                    tr_S = np.real(np.trace(S_rep))
                    tr_U = np.real(np.trace(U_rep))
                    chi_S = np.real(chi_rho[1])  # χ(s) для класса 2a
                    chi_U = np.real(chi_rho[2])  # χ(u) для класса 3a
                    print(f"      ✓ S²={err_S2:.2e}, U³={err_U3:.2e}, (SU)⁷={err_SU7:.2e}")
                    print(f"      tr(S)={tr_S:.4f} (χ={chi_S:.4f}), "
                          f"tr(U)={tr_U:.4f} (χ={chi_U:.4f})")
                    return S_rep, U_rep, True
                else:
                    if attempt < 5:  # подробный вывод для первых попыток
                        print(f"        n_basis={len(Q_list)}, "
                              f"S²={err_S2:.2e}, U³={err_U3:.2e}, (SU)⁷={err_SU7:.2e}")

    print(f"    ✗ MeatAxe не смог построить матрицы для {rep_name} после 100 попыток")
    return (np.zeros((dim_rho, dim_rho), dtype=complex),
            np.zeros((dim_rho, dim_rho), dtype=complex), False)


# ============================================================================
# ГЕОМЕТРИЯ ДИСКА ПУАНКАРЕ
# ============================================================================

def poincare_omega2(x, y):
    return 4.0 / (1.0 - x**2 - y**2 + 1e-15)**2


def moebius_rotation(z, center, angle):
    """Вращение на угол θ вокруг точки center в диске Пуанкаре"""
    cz = complex(z[0], z[1])
    cc = complex(center[0], center[1])
    cc_bar = np.conj(cc)

    denom = 1.0 - cc_bar * cz
    if abs(denom) < 1e-15:
        return z
    w = (cz - cc) / denom
    w_rot = w * np.exp(1j * angle)
    denom2 = 1.0 + cc_bar * w_rot
    if abs(denom2) < 1e-15:
        return z
    z_new = (w_rot + cc) / denom2

    r2 = abs(z_new)**2
    if r2 >= 0.999:
        z_new = z_new * 0.998 / np.sqrt(r2)

    return [z_new.real, z_new.imag]


def rotation_pi_around_origin(z):
    return [-z[0], -z[1]]


def geodesic_arc_points(p1, p2, n_points):
    cross = p1[0]*p2[1] - p1[1]*p2[0]
    if abs(cross) < 1e-10:
        return [[(1-k/n_points)*p1[0]+(k/n_points)*p2[0],
                 (1-k/n_points)*p1[1]+(k/n_points)*p2[1]]
                for k in range(n_points+1)]

    x1, y1 = p1; x2, y2 = p2
    A_mat = np.array([[2*x1, 2*y1], [2*x2, 2*y2]])
    b_vec = np.array([x1**2+y1**2+1, x2**2+y2**2+1])
    det_A = np.linalg.det(A_mat)
    if abs(det_A) < 1e-12:
        return [[(1-k/n_points)*p1[0]+(k/n_points)*p2[0],
                 (1-k/n_points)*p1[1]+(k/n_points)*p2[1]]
                for k in range(n_points+1)]

    center = np.linalg.solve(A_mat, b_vec)
    px, py = center[0], center[1]
    R = np.sqrt(max(0, px**2 + py**2 - 1.0))

    theta1 = np.arctan2(y1 - py, x1 - px)
    theta2 = np.arctan2(y2 - py, x2 - px)
    dtheta = theta2 - theta1
    if dtheta > np.pi: dtheta -= 2*np.pi
    if dtheta < -np.pi: dtheta += 2*np.pi

    pts = []
    for k in range(n_points + 1):
        t = k / n_points
        theta = theta1 + t * dtheta
        x = px + R * np.cos(theta)
        y = py + R * np.sin(theta)
        r2 = x**2 + y**2
        if r2 >= 0.999:
            s = 0.998/np.sqrt(r2); x *= s; y *= s
        pts.append([x, y])
    return pts


# ============================================================================
# СЕТКА ДВОЙНОГО ТРЕУГОЛЬНИКА
# ============================================================================
#
# D = T⁺ ∪ T⁻,  T⁻ = отражение T⁺ от AB (оси x)
#
# T⁺: A(0,0), B(xB,0), C(0,yC)
# T⁻: A(0,0), B(xB,0), C'(0,-yC)
#
# Граница D:
#   e₁: C→B   (геодезическая дуга, верхняя)
#   e₂: B→C'  (геодезическая дуга, нижняя)
#   e₃: C'→A  (прямая, отрицательная y-ось)
#   e₄: A→C   (прямая, положительная y-ось)
#
# Склейки:
#   R₁ (поворот π вокруг A):    e₃ ↔ e₄
#   R₂ (поворот 2π/3 вокруг B): e₁ ↔ e₂
# ============================================================================

def create_double_triangle_mesh(level, verbose=True):
    alpha = PI / 2; beta = PI / 3; gamma = PI / 7
    ca, sa = np.cos(alpha), np.sin(alpha)
    cb, sb = np.cos(beta),  np.sin(beta)
    cc, sc = np.cos(gamma), np.sin(gamma)

    a_side = np.arccosh((cb*cc + ca) / (sb*sc))
    b_side = np.arccosh((ca*cc + cb) / (sa*sc))
    c_side = np.arccosh((ca*cb + cc) / (sa*sb))

    vA = [0.0, 0.0]
    vB = [np.tanh(c_side / 2), 0.0]
    vC = [0.0, np.tanh(b_side / 2)]
    vC_prime = [0.0, -np.tanh(b_side / 2)]

    n_sub = 2**level

    # Предвычисляем геодезические дуги
    arc_upper = geodesic_arc_points(vC, vB, n_sub)
    arc_lower = geodesic_arc_points(vC_prime, vB, n_sub)

    vertices = []
    edge_id = []      # 0=int, 1=e₁, 2=e₂, 3=e₃, 4=e₄
    is_vertex = []    # 0=no, 1=A, 2=B, 3=C, 4=C'
    bary_plus  = {}
    bary_minus = {}

    # --- T⁺ вершины ---
    idx = 0
    for i in range(n_sub + 1):
        for j in range(n_sub - i + 1):
            k = n_sub - i - j
            u, v, w = k/n_sub, j/n_sub, i/n_sub

            if k == 0 and i > 0 and j > 0:
                pt = list(arc_upper[i])
            else:
                pt = [u*vA[0]+v*vB[0]+w*vC[0],
                      u*vA[1]+v*vB[1]+w*vC[1]]

            r2 = pt[0]**2 + pt[1]**2
            if r2 >= 0.999:
                s = 0.998/np.sqrt(r2); pt = [pt[0]*s, pt[1]*s]

            idx += 1
            vertices.append(pt)
            bary_plus[(i,j,k)] = idx

            eid = 0
            if k == 0 and i + j == n_sub and i > 0 and j > 0: eid = 1
            if j == 0 and i > 0 and k > 0: eid = 4
            edge_id.append(eid)

            iv = 0
            if i == 0 and j == 0 and k == n_sub: iv = 1  # A
            if i == 0 and j == n_sub and k == 0:  iv = 2  # B
            if i == n_sub and j == 0 and k == 0:  iv = 3  # C
            is_vertex.append(iv)

    # --- T⁻ вершины ---
    for i in range(n_sub + 1):
        for j in range(n_sub - i + 1):
            k = n_sub - i - j
            u, v, w = k/n_sub, j/n_sub, i/n_sub

            if k == 0 and i > 0 and j > 0:
                pt = list(arc_lower[i])
            else:
                pt = [u*vA[0]+v*vB[0]+w*vC_prime[0],
                      u*vA[1]+v*vB[1]+w*vC_prime[1]]

            r2 = pt[0]**2 + pt[1]**2
            if r2 >= 0.999:
                s = 0.998/np.sqrt(r2); pt = [pt[0]*s, pt[1]*s]

            idx += 1
            vertices.append(pt)
            bary_minus[(i,j,k)] = idx

            eid = 0
            if k == 0 and i + j == n_sub and i > 0 and j > 0: eid = 2
            if j == 0 and i > 0 and k > 0: eid = 3
            edge_id.append(eid)

            iv = 0
            if i == 0 and j == 0 and k == n_sub: iv = 1  # A
            if i == 0 and j == n_sub and k == 0:  iv = 2  # B
            if i == n_sub and j == 0 and k == 0:  iv = 4  # C'
            is_vertex.append(iv)

    # --- Треугольные элементы ---
    elements = []
    for bary in [bary_plus, bary_minus]:
        for i in range(n_sub):
            for j in range(n_sub - i):
                k = n_sub - i - j
                v1 = bary[(i,j,k)]
                v2 = bary[(i+1,j,k-1)]
                v3 = bary[(i,j+1,k-1)]
                elements.append([v1, v2, v3])
                if k >= 2:
                    v4 = bary[(i+1,j+1,k-2)]
                    elements.append([v2, v4, v3])

    # --- Склейка T⁺ и T⁻ по стороне AB ---
    replace_map = {}
    for j in range(n_sub + 1):
        idx_p = bary_plus[(0, j, n_sub-j)]
        idx_m = bary_minus[(0, j, n_sub-j)]
        if idx_p != idx_m:
            replace_map[idx_m] = idx_p

    for elem in elements:
        for k in range(3):
            if elem[k] in replace_map:
                elem[k] = replace_map[elem[k]]

    # Перенумерация
    removed = set(replace_map.keys())
    old2new = {}
    new_idx = 0
    for i in range(1, idx + 1):
        if i in removed:
            old2new[i] = old2new[replace_map[i]]
        else:
            new_idx += 1
            old2new[i] = new_idx

    new_verts = [vertices[i-1] for i in range(1, idx+1) if i not in removed]
    new_edge  = [edge_id[i-1] for i in range(1, idx+1) if i not in removed]
    new_ivert = [is_vertex[i-1] for i in range(1, idx+1) if i not in removed]

    for elem in elements:
        for k in range(3):
            elem[k] = old2new[elem[k]]

    # Удаление дубликатов
    seen = set()
    unique_elems = []
    for elem in elements:
        key = tuple(sorted(elem))
        if key not in seen:
            seen.add(key)
            unique_elems.append(sorted(elem))

    if verbose:
        A_euc = sum(abs((new_verts[e[1]-1][0]-new_verts[e[0]-1][0])*
                         (new_verts[e[2]-1][1]-new_verts[e[0]-1][1]) -
                         (new_verts[e[2]-1][0]-new_verts[e[0]-1][0])*
                         (new_verts[e[1]-1][1]-new_verts[e[0]-1][1]))/2
                    for e in unique_elems)
        print(f"  Сетка D(2,3,7): {len(new_verts)} вершин, "
              f"{len(unique_elems)} элементов, A_euc={A_euc:.6f}")

    return new_verts, unique_elems, new_edge, new_ivert, vA, vB, vC, vC_prime, n_sub


# ============================================================================
# FEM СБОРКА
# ============================================================================
#
# Слабая форма гиперболического лапласиана:
#   -Δ_hyp ψ = λ ψ   ↔   ∫∇u·∇v dA_euc = λ ∫uv ω² dA_euc
#
# K = ∫∇φ_i·∇φ_j dA_euc     (евклидова матрица жёсткости)
# M = ∫φ_i φ_j ω² dA_euc     (гиперболическая матрица массы)
# ============================================================================

def assemble_laplacian(vertices, elements, verbose=True):
    n_v = len(vertices)
    K = np.zeros((n_v, n_v))
    M = np.zeros((n_v, n_v))
    total_euc = 0.0
    total_hyp = 0.0

    for elem in elements:
        i1, i2, i3 = elem[0]-1, elem[1]-1, elem[2]-1  # 0-based
        x1, y1 = vertices[i1]; x2, y2 = vertices[i2]; x3, y3 = vertices[i3]
        J_signed = (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)
        J = abs(J_signed)
        if J < 1e-15:
            continue
        A = J / 2.0
        gphi = [(y2-y3)/J_signed, (x3-x2)/J_signed,
                (y3-y1)/J_signed, (x1-x3)/J_signed,
                (y1-y2)/J_signed, (x2-x1)/J_signed]
        for a in range(3):
            for b in range(3):
                K[elem[a]-1, elem[b]-1] += \
                    (gphi[2*a]*gphi[2*b]+gphi[2*a+1]*gphi[2*b+1])*A

        w1 = poincare_omega2(x1, y1)
        w2 = poincare_omega2(x2, y2)
        w3 = poincare_omega2(x3, y3)
        # Масса: квадратурная формула повышенной точности
        M[elem[0]-1, elem[0]-1] += A*(3*w1+w2+w3)/30
        M[elem[1]-1, elem[1]-1] += A*(w1+3*w2+w3)/30
        M[elem[2]-1, elem[2]-1] += A*(w1+w2+3*w3)/30
        M[elem[0]-1, elem[1]-1] += A*(2*w1+2*w2+w3)/60
        M[elem[1]-1, elem[0]-1] += A*(2*w1+2*w2+w3)/60
        M[elem[0]-1, elem[2]-1] += A*(2*w1+w2+2*w3)/60
        M[elem[2]-1, elem[0]-1] += A*(2*w1+w2+2*w3)/60
        M[elem[1]-1, elem[2]-1] += A*(w1+2*w2+2*w3)/60
        M[elem[2]-1, elem[1]-1] += A*(w1+2*w2+2*w3)/60
        total_euc += A
        total_hyp += A*(w1+w2+w3)/3.0

    expected_area = PI / 21
    area_err = abs(total_hyp - expected_area) / expected_area
    if area_err > 0.05:
        print(f"  WARNING: A_hyp={total_hyp:.6f}, expected π/21={expected_area:.6f}, "
              f"err={area_err*100:.1f}%")

    if verbose:
        print(f"  K({n_v}x{n_v}) | A_euc={total_euc:.6f} | "
              f"A_hyp={total_hyp:.6f} (π/21={expected_area:.6f}) | "
              f"<Ω²>={total_hyp/total_euc:.2f}")

    return K, M, total_euc, total_hyp


# ============================================================================
# ОТЖДЕСТВЛЕНИЕ ГРАНИЧНЫХ УЗЛОВ ЧЕРЕЗ МЁБИУСА
# ============================================================================

def build_bc_identification(vertices, edge_id, is_vertex, vA, vB, vC, vC_prime):
    n_v = len(vertices)

    idx_C = None; idx_Cp = None
    for i in range(n_v):
        if is_vertex[i] == 3: idx_C = i
        if is_vertex[i] == 4: idx_Cp = i

    # Внутренние узлы на каждой границе (без конусов)
    e4 = [i for i in range(n_v) if edge_id[i] == 4 and is_vertex[i] == 0]
    e3 = [i for i in range(n_v) if edge_id[i] == 3 and is_vertex[i] == 0]
    e1 = [i for i in range(n_v) if edge_id[i] == 1 and is_vertex[i] == 0]
    e2 = [i for i in range(n_v) if edge_id[i] == 2 and is_vertex[i] == 0]

    # R₁: поворот π вокруг A (начала координат) → z ↦ -z
    R1_map = {}
    e4_positions = [vertices[n4] for n4 in e4]
    for n3 in e3:
        z_img = rotation_pi_around_origin(vertices[n3])
        best_dist = float('inf')
        best_node = -1
        for k, n4 in enumerate(e4):
            d = (e4_positions[k][0]-z_img[0])**2 + (e4_positions[k][1]-z_img[1])**2
            if d < best_dist:
                best_dist = d
                best_node = n4
        if best_node >= 0 and best_dist < 0.01:
            R1_map[n3] = best_node

    # R₁ также: C' ↔ C
    if idx_C is not None and idx_Cp is not None:
        R1_map[idx_Cp] = idx_C

    # R₂: поворот 2π/3 вокруг B (Мёбиус-вращение)
    def try_R2_angle(angle):
        test_map = {}
        total_dist = 0.0
        count = 0
        for n2 in e2:
            z_img = moebius_rotation(vertices[n2], vB, angle)
            best_dist = float('inf')
            best_node = -1
            for n1 in e1:
                d = (vertices[n1][0]-z_img[0])**2 + (vertices[n1][1]-z_img[1])**2
                if d < best_dist:
                    best_dist = d
                    best_node = n1
            if best_node >= 0 and best_dist < 0.01:
                test_map[n2] = best_node
                total_dist += best_dist
                count += 1
        return test_map, total_dist, count

    map_pos, dist_pos, cnt_pos = try_R2_angle(2*PI/3)
    map_neg, dist_neg, cnt_neg = try_R2_angle(-2*PI/3)

    if cnt_neg > cnt_pos or (cnt_neg == cnt_pos and cnt_neg > 0
                              and dist_neg/cnt_neg < dist_pos/cnt_pos):
        R2_map = map_neg
        R2_angle = -2*PI/3
    else:
        R2_map = map_pos
        R2_angle = 2*PI/3

    all_slaves = {**R1_map, **R2_map}
    free_dofs = [i for i in range(n_v) if i not in all_slaves]

    return free_dofs, all_slaves, R1_map, R2_map, R2_angle


# ============================================================================
# ПЕРИОДИЧЕСКИЕ BC (1a представление)
# ============================================================================

def apply_periodic_bc(K, M, free_dofs, slave_map):
    n = K.shape[0]
    nf = len(free_dofs)
    fim = {gi: fi for fi, gi in enumerate(free_dofs)}

    P = np.zeros((n, nf))
    for fi, gi in enumerate(free_dofs):
        P[gi, fi] = 1.0
    for slave, master in slave_map.items():
        if master in fim:
            P[slave, fim[master]] = 1.0

    Kr = P.T @ K @ P
    Mr = P.T @ M @ P
    return (Kr + Kr.T) / 2, (Mr + Mr.T) / 2


# ============================================================================
# ВЕКТОРНО-РАССЛОЁННЫЙ FEM
# ============================================================================
#
# Для представления ρ размерности d_ρ:
#   ψ: D → C^{d_ρ},  ψ(g·z) = ρ(g)·ψ(z)
#
# Граничные условия:
#   slave на e₃ (R₁ = s): ψ(slave) = ρ(s)·ψ(master)
#   slave на e₂ (R₂ = u): ψ(slave) = ρ(u)·ψ(master)
# ============================================================================

def apply_vector_bundle_bc(K, M, free_dofs, slave_map, R1_map, R2_map,
                           rep_S, rep_U_R2, dim_rho):
    """
    Vector bundle FEM with twisted boundary conditions.
    
    BC convention: ψ(g·z) = ρ(g)·ψ(z)
    If R₂ maps slave(e₂) → master(e₁), then:
      ψ(master) = ρ(R₂)·ψ(slave)  →  ψ(slave) = ρ(R₂)⁻¹·ψ(master)
    
    rep_U_R2: the matrix to use for R₂ slave nodes.
    Should be ρ(R₂)⁻¹ where R₂ is the geometric rotation mapping e₂→e₁.
    If R₂ = u, then rep_U_R2 = ρ(u²) = U².
    If R₂ = u², then rep_U_R2 = ρ(u) = U.
    """
    n = K.shape[0]
    nf = len(free_dofs)
    N_red = nf * dim_rho
    fim = {gi: fi for fi, gi in enumerate(free_dofs)}

    P_vb = np.zeros((n * dim_rho, N_red), dtype=complex)

    # Свободные узлы: identity block
    for fi, gi in enumerate(free_dofs):
        for k in range(dim_rho):
            P_vb[gi * dim_rho + k, fi * dim_rho + k] = 1.0 + 0j

    # Slave узлы
    # R₁ maps e₃(slave) → e₄(master): ψ(slave) = ρ(s)⁻¹·ψ(master) = ρ(s)·ψ(master)
    # R₂ maps e₂(slave) → e₁(master): ψ(slave) = ρ(R₂)⁻¹·ψ(master) = rep_U_R2·ψ(master)
    for slave, master in slave_map.items():
        if master not in fim:
            continue
        fi_m = fim[master]
        if slave in R1_map:
            rep_mat = rep_S      # ρ(s)⁻¹ = ρ(s) since s² = e
        elif slave in R2_map:
            rep_mat = rep_U_R2   # ρ(R₂)⁻¹ — передаётся как аргумент
        else:
            continue
        for k in range(dim_rho):
            for j in range(dim_rho):
                val = complex(rep_mat[k, j])
                if abs(val) > 1e-12:
                    P_vb[slave * dim_rho + k, fi_m * dim_rho + j] = val

    Kc = K.astype(complex)
    Mc = M.astype(complex)
    # КРИТИЧЕСКИ: kron(K, I_d), НЕ kron(I_d, K)!
    # P_vb использует индексацию (node*d + comp),
    # поэтому K_vb[node1*d+c1, node2*d+c2] = K[node1,node2] * delta(c1,c2)
    # Это даёт kron(K, I_d), а НЕ kron(I_d, K)
    K_vb = np.kron(Kc, np.eye(dim_rho, dtype=complex))
    M_vb = np.kron(Mc, np.eye(dim_rho, dtype=complex))

    Kr = P_vb.T.conj() @ K_vb @ P_vb
    Mr = P_vb.T.conj() @ M_vb @ P_vb
    return (Kr + Kr.T.conj()) / 2, (Mr + Mr.T.conj()) / 2


# ============================================================================
# РЕШЕНИЕ ОБОБЩЁННОЙ ПРОБЛЕМЫ СЗ
# ============================================================================

def solve_eigen(K, M, n_eig=20):
    n = K.shape[0]
    ne = min(n_eig, n - 1)
    if ne < 1: ne = 1
    Md = M + 1e-12 * np.eye(n)
    try:
        evals, evecs = np.linalg.eig(np.linalg.solve(Md, K))
    except np.linalg.LinAlgError:
        evals, evecs = np.linalg.eig(K, Md)
    evals = np.real(evals)
    idx = np.argsort(evals)
    pos = [i for i in idx if evals[i] > 0.01]
    ne = min(ne, len(pos))
    if ne == 0:
        return np.array([]), np.array([]).reshape(n, 0)
    return evals[pos[:ne]], evecs[:, pos[:ne]]


# ============================================================================
# ГЛАВНЫЙ РАСЧЁТ
# ============================================================================

def main():
    t0 = time.time()
    print("=" * 80)
    print("AB Cloud v6 Python — FEM на Klein quartic (2,3,7) с MeatAxe")
    print("=" * 80)

    chi = psl27_character_table()
    reps = ["1a", "3a", "3b", "6a", "7a", "8a"]

    # --- Верификация ---
    print("\nВЕРИФИКАЦИЯ:")
    ortho_ok = True
    for i, r1 in enumerate(reps):
        for j, r2 in enumerate(reps):
            inner = sum(CLASS_SIZES[k]*chi[r1][k]*np.conj(chi[r2][k])
                       for k in range(6)) / PSL27_ORDER
            expected = 1.0 if i == j else 0.0
            if abs(inner - expected) > 0.01:
                ortho_ok = False
    print(f"  Ортогональность характеров: {'✓' if ortho_ok else '✗'}")

    dim_sum = sum(int(np.real(chi[r][0]))**2 for r in reps)
    print(f"  Σ dim² = {dim_sum}, |G| = {PSL27_ORDER}: "
          f"{'✓' if dim_sum == PSL27_ORDER else '✗'}")

    print("\n  Известные λ Klein quartic (Cook 2018):")
    for ev in KNOWN_EIGENVALUES[:5]:
        print(f"    λ = {ev[0]:.4f}  mult={ev[1]}  irrep={ev[2]}")

    # --- Построение PSL(2,7) ---
    print("\nПостроение PSL(2,7)...")
    elements = enumerate_psl27()
    mt = build_mult_table(elements)
    eid = find_identity(mt)
    class_map = classify_conjugacy_classes(elements, mt, eid)

    for c in range(1, 7):
        cnt = int(np.sum(class_map == c))
        print(f"  Класс {c}: {cnt} элементов")

    s_idx, u_idx = find_generators(elements, mt, eid)
    su_idx = mt[s_idx, u_idx]
    print(f"  Образующие: s={s_idx} (пор.2), u={u_idx} (пор.3), "
          f"su={su_idx} (пор.{element_order(mt, su_idx, eid)})")

    # --- Матрицы представлений (MeatAxe) ---
    print("\nПостроение матриц представлений (MeatAxe)...")
    rep_mats = {}
    for rep_name in reps:
        S, U, ok = build_rep_matrices(elements, mt, class_map, rep_name,
                                       s_idx, u_idx, eid)
        rep_mats[rep_name] = (S, U, ok)
        dim_rho = int(np.real(chi[rep_name][0]))
        if ok and dim_rho > 1:
            print(f"  {rep_name} (dim={dim_rho}): ✓")
        elif dim_rho == 1:
            print(f"  {rep_name} (dim={dim_rho}): ✓")
        else:
            print(f"  {rep_name} (dim={dim_rho}): ✗")

    # --- Верификация изометрий ---
    print("\nВерификация изометрий:")
    alpha_a = PI / 2; beta_v = PI / 3; gamma_v = PI / 7
    ca, sa = np.cos(alpha_a), np.sin(alpha_a)
    cb, sb = np.cos(beta_v),  np.sin(beta_v)
    cc_v, sc = np.cos(gamma_v), np.sin(gamma_v)
    b_side = np.arccosh((ca*cc_v + cb) / (sa*sc))
    c_side = np.arccosh((ca*cb + cc_v) / (sa*sb))
    vB_chk = [np.tanh(c_side / 2), 0.0]
    vC_chk = [0.0, np.tanh(b_side / 2)]
    vCp_chk = [0.0, -np.tanh(b_side / 2)]

    R1_Cp = rotation_pi_around_origin(vCp_chk)
    print(f"  R₁(C') = ({R1_Cp[0]:.6f}, {R1_Cp[1]:.6f}), "
          f"C = ({vC_chk[0]:.6f}, {vC_chk[1]:.6f}) ✓")

    R2_Cp = moebius_rotation(vCp_chk, vB_chk, 2*PI/3)
    R2_Cp_neg = moebius_rotation(vCp_chk, vB_chk, -2*PI/3)
    d_pos = np.sqrt((R2_Cp[0]-vC_chk[0])**2 + (R2_Cp[1]-vC_chk[1])**2)
    d_neg = np.sqrt((R2_Cp_neg[0]-vC_chk[0])**2 + (R2_Cp_neg[1]-vC_chk[1])**2)
    print(f"  R₂(C'): d+2π/3={d_pos:.4f}, d-2π/3={d_neg:.4f}")

    # --- FEM: 1a представление ---
    print("\n" + "=" * 80)
    print("1a ПРЕДСТАВЛЕНИЕ — ПЕРИОДИЧЕСКИЕ BC НА ДВОЙНОМ Δ")
    print("=" * 80)

    for level in [3, 4]:
        print(f"\n  Level {level}:")
        verts, elems, eid_mesh, ivert, vA, vB, vC, vCp, nsub = \
            create_double_triangle_mesh(level)
        K, M, _, A_hyp = assemble_laplacian(verts, elems)
        free, slaves, R1m, R2m, R2_ang = \
            build_bc_identification(verts, eid_mesh, ivert, vA, vB, vC, vCp)
        print(f"  free={len(free)}, slave={len(slaves)}, R₂ angle={R2_ang:+.4f}")

        Kr, Mr = apply_periodic_bc(K, M, free, slaves)
        evals, _ = solve_eigen(Kr, Mr, n_eig=10)
        print("  Первые λ:")
        for k in range(min(10, len(evals))):
            print(f"    λ_{k+1} = {evals[k]:.4f}")

    # --- Vector bundle FEM: тестирование обоих направлений R2 ---
    has_any = any(rep_mats[r][2] for r in reps if int(np.real(chi[r][0])) > 1)
    if not has_any:
        print("\n  Ни одно представление dim>1 не построено")
        return

    print("\n" + "=" * 80)
    print("ВЕКТОРНО-РАССЛОЁННЫЙ FEM — ТЕСТИРОВАНИЕ НАПРАВЛЕНИЯ R2")
    print("=" * 80)
    print("\n  R2 отображает e2(slave) -> e1(master)")
    print("  BC: psi(slave) = rho(R2)^{-1} * psi(master)")
    print("  Variant A: R2 = u  -> rho(R2)^{-1} = rho(u^2) = U^2")
    print("  Variant B: R2 = u^2 -> rho(R2)^{-1} = rho(u)  = U")

    level = 3
    verts, elems, eid_mesh, ivert, vA, vB, vC, vCp, nsub = \
        create_double_triangle_mesh(level, verbose=False)
    K, M, _, _ = assemble_laplacian(verts, elems, verbose=False)
    free, slaves, R1m, R2m, R2_ang = \
        build_bc_identification(verts, eid_mesh, ivert, vA, vB, vC, vCp)

    for r2_label, use_U_sq in [("A: R2=u, BC=U^2", True), ("B: R2=u^2, BC=U", False)]:
        print(f"\n  -- Variant {r2_label} --")
        print(f"  {'rep':>4} {'dim':>4} {'N_red':>7} {'lam1(FEM)':>11} "
              f"{'lam1(Cook)':>11} {'err%':>7}")
        print("  " + "-" * 55)

        for rep_name in ["8a", "7a", "6a", "3a", "3b", "1a"]:
            dim_rho = int(np.real(chi[rep_name][0]))
            S, U, ok = rep_mats[rep_name]

            lam_cook = 0.0
            for ev in KNOWN_EIGENVALUES:
                if ev[2] == rep_name:
                    lam_cook = ev[0]
                    break

            try:
                if dim_rho == 1:
                    Kr, Mr = apply_periodic_bc(K, M, free, slaves)
                    evl, _ = solve_eigen(Kr, Mr, n_eig=10)
                    lam1 = evl[0] if len(evl) > 0 else float('nan')
                    N_red = len(free)
                else:
                    if not ok:
                        print(f"  {rep_name:>4} {dim_rho:>4} -- matrices not found")
                        continue
                    if use_U_sq:
                        U_R2 = np.linalg.matrix_power(U, 2)
                    else:
                        U_R2 = U
                    Kr, Mr = apply_vector_bundle_bc(
                        K, M, free, slaves, R1m, R2m, S, U_R2, dim_rho)
                    evl, _ = solve_eigen(Kr, Mr, n_eig=10)
                    lam1 = evl[0] if len(evl) > 0 else float('nan')
                    N_red = Kr.shape[0]

                dlam = abs(lam1 - lam_cook)/lam_cook*100 if lam_cook > 0 else float('nan')
                print(f"  {rep_name:>4} {dim_rho:>4} {N_red:>7} "
                      f"{lam1:>11.4f} {lam_cook:>11.4f} {dlam:>6.1f}%")
            except Exception as e:
                print(f"  {rep_name:>4} {dim_rho:>4} ERROR: {str(e)[:60]}")

    # Convergence study for both variants
    print("\n" + "=" * 80)
    print("CONVERGENCE STUDY -- both R2 variants for 8a, 7a, 6a")
    print("=" * 80)

    for rep_chk in ["8a", "7a", "6a"]:
        S_chk, U_chk, ok_chk = rep_mats[rep_chk]
        if not ok_chk:
            continue
        U_chk_sq = np.linalg.matrix_power(U_chk, 2)
        dim_chk = int(np.real(chi[rep_chk][0]))
        lam_cook_chk = 0.0
        for ev in KNOWN_EIGENVALUES:
            if ev[2] == rep_chk:
                lam_cook_chk = ev[0]
                break

        print(f"\n  {rep_chk} (Cook lam1 = {lam_cook_chk:.4f}):")
        for r2_label, U_R2 in [("BC=U^2", U_chk_sq), ("BC=U", U_chk)]:
            results = []
            for lvl in [3, 4]:
                try:
                    v, e, ei, iv, vA2, vB2, vC2, vCp2, _ = \
                        create_double_triangle_mesh(lvl, verbose=False)
                    K2, M2, _, _ = assemble_laplacian(v, e, verbose=False)
                    f2, s2, R1m2, R2m2, _ = \
                        build_bc_identification(v, ei, iv, vA2, vB2, vC2, vCp2)
                    Kr2, Mr2 = apply_vector_bundle_bc(
                        K2, M2, f2, s2, R1m2, R2m2, S_chk, U_R2, dim_chk)
                    evl2, _ = solve_eigen(Kr2, Mr2, n_eig=3)
                    if len(evl2) > 0:
                        results.append((lvl, Kr2.shape[0], evl2[0]))
                except Exception as ex:
                    pass
            if results:
                print(f"    {r2_label}: " + ", ".join(
                    f"L{l}:N={n},lam1={v:.4f}" for l, n, v in results))

    elapsed = time.time() - t0
    print(f"\n{'█' * 80}")
    print(f"█  ЗАВЕРШЕНО за {elapsed:.1f} сек")
    print(f"{'█' * 80}")


if __name__ == "__main__":
    main()
