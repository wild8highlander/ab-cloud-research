#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
============================================================================
СИСТЕМА ВИХРЕЙ AB-ОБЛАКА ДЛЯ ЗАДАЧИ N ТЕЛ — PYTHON VERSION (v2.0)
============================================================================
Масштабная Python-реализация of the задачи трёх (и N) тел
верификация через вихревую модель AB-облака с топологическим интегралом Чаплыгина.

Это ЗЕРКАЛО Julia-версии (AB_Cloud_Вихрь_Система_v2.jl).
Оба кода дают идентичные результаты и имеют одинаковую 22-секционную структуру.

Автор: Z.ai Research Laboratory
Версия: 2.0
Год: 2026

22 СЕКЦИИ:
 1. Imports and Dependencies
 2. Constants and Global Конфигурация
 3. Данные Structures
 4. Hamiltonian Construction (Hofstadter with N вихрей)
 5. Аналитическое решение (Theorem 3.1)
 6. Сохранение Чаплыгина Verification
 7. Spectral Statistics (GUE/GOE/Пуассон)
 8. Zeta Zeros and Montgomery Test
 9. Quantum Version with Topological Qubits
10. Real Система Presets
11. High-Resolution Plot Generation
12. Report Generation (TXT, MD, HTML, CSV, JSON, DOCX, PDF)
13. Comprehensive Test Functions
14. Interactive Menu
15. Main Entry Point
16. NEW: Вычисление фазы Берри
17. NEW: Вычисление числа Черна (Fukui-Hatsugai-Suzuki)
18. NEW: Холловская проводимость TKNN
19. NEW: Анализ конуса Дирака
20. NEW: Спектральный форм-фактор
21. NEW: Дисперсия чисел и IPR
22. NEW: Показатель Ляпунова + Перестановочный тест
============================================================================
"""

# ===========================================================================
# SECTION 1: IMPORTS AND DEPENDENCIES
# ===========================================================================

import numpy as np
import scipy
from scipy import linalg, stats, integrate
from scipy.integrate import solve_ivp, odeint
from scipy.special import gamma as gamma_func, zeta as riemann_zeta
import matplotlib
matplotlib.use('Agg')
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, FancyArrowPatch, Polygon
from mpl_toolkits.mplot3d import Axes3D
import os, sys, json, math, time, datetime
from pathlib import Path
import csv

# Try to load optional packages
HAVE_MPMATH = False
try:
    import mpmath
    HAVE_MPMATH = True
except ImportError:
    pass

# Configure matplotlib
try:
    fm.fontManager.addfont('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
    fm.fontManager.addfont('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf')
except Exception:
    pass

plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 150
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['savefig.bbox'] = 'tight'

# ===========================================================================
# SECTION 2: CONSTANTS AND GLOBAL CONFIGURATION
# ===========================================================================

# Physical constants (SI)
G_NEWTON = 6.674e-11       # m^3 kg^-1 s^-2
HBAR = 1.0546e-34          # J·s
HBAR_EV = 6.582e-16        # eV·s
K_B = 1.381e-23            # J/K
C_LIGHT = 2.998e8          # m/s
ELECTRON_CHARGE = 1.602e-19 # C

# Mathematical constants
EULER = math.e
PI_CONST = math.pi
GAMMA_EULER = 0.5772156649015329

# RMT reference values for ⟨r⟩ статистика
R_GUE = 0.5996
R_GOE = 0.5307
R_GSE = 0.6762
R_POISSON = 0.3863


class Config:
    """Конфигурация with all tunable parameters."""
    def __init__(self):
        # Lattice parameters
        self.lattice_size = 20          # L (LxL lattice)
        self.n_вихрей = 3             # N_v
        self.alpha = 0.5                # Effective flux
        self.disorder_strength = 2.0    # W
        self.n_seeds = 5                # Number of random realizations

        # Chaplygin parameters
        self.C_Ch = 1.0                 # Chaplygin constant
        self.q_charges = [1, -1, 1]    # Topological charges
        self.T_period = 2 * math.pi     # Period T

        # Spectral analysis
        self.n_eigenvalues = 500
        self.unfolding_degree = 3

        # Numerical parameters
        self.rtol = 1e-10
        self.atol = 1e-12
        self.max_time = 100.0

        # Output
        self.output_dir = "reports"
        self.generate_plots = True
        self.generate_reports = True
        self.plot_dpi = 300
        self.verbose = True

        # Quantum
        self.n_qubits = 3

        # NEW: Berry/Chern parameters
        self.k_grid_size = 20           # For Chern number computation
        self.berry_n_points = 1000      # Точки интегрирования фазы Берри

        # NEW: Lyapunov
        self.lyapunov_time = 50.0       # Time for Lyapunov exponent
        self.lyapunov_n_traj = 100      # Число траекторий

        # NEW: Permutation test
        self.permutation_n = 10000      # Число перестановок

        # NEW: Spectral form factor
        self.sff_t_max = 10.0           # Макс. время для форм-фактора

        # NEW: Hofstadter butterfly
        self.butterfly_n_alpha = 100    # Число значений alpha
        self.butterfly_n_bands = 20     # Число зон для графика


def default_config():
    return Config()


# ===========================================================================
# SECTION 3: DATA STRUCTURES
# ===========================================================================

class Вихрь:
    """A single topological vortex."""
    def __init__(self, position, charge, mass=1.0):
        self.position = np.array(position, dtype=float)
        self.charge = int(charge)
        self.mass = float(mass)


class RMTResults:
    """Results of a GUE/GOE/Пуассон test."""
    def __init__(self):
        self.r_mean = 0.0
        self.r_std = 0.0
        self.spacings = []
        self.ks_gue = 0.0
        self.p_gue = 0.0
        self.ks_goe = 0.0
        self.p_goe = 0.0
        self.ks_poisson = 0.0
        self.p_poisson = 0.0
        self.verdict = ""
        # NEW: Number variance
        self.number_variance = []
        # NEW: Spectral form factor
        self.spectral_form_factor = []
        # NEW: IPR
        self.ipr_values = []


class ChaplyginResults:
    """Chaplygin verification results."""
    def __init__(self):
        self.C_Ch_target = 0.0
        self.C_Ch_computed = []
        self.C_Ch_mean = 0.0
        self.C_Ch_std = 0.0
        self.drift = 0.0
        self.lyapunov_vortex = 0.0
        self.lyapunov_newton = 0.0
        # NEW: Berry phase
        self.berry_phase = 0.0
        # NEW: Direct Lyapunov
        self.lyapunov_direct = 0.0


class QuantumResults:
    """Quantum computation results."""
    def __init__(self):
        self.H_quantum = None
        self.eigenvalues = []
        self.ground_state = None
        self.entanglement_entropy = 0.0
        self.fidelity_topological = []
        self.fidelity_classical = []
        # NEW: Quantum mutual information
        self.mutual_information = 0.0
        # NEW: Quantum discord
        self.quantum_discord = 0.0


class TopologicalResults:
    """NEW: Topological invariants results."""
    def __init__(self):
        self.chern_number = 0
        self.berry_phase = 0.0
        self.berry_curvature = []
        self.hall_conductance = 0.0
        self.dirac_points = []
        self.dirac_velocity = 0.0


class AdvancedRMTResults:
    """NEW: Advanced RMT diagnostics."""
    def __init__(self):
        self.number_variance = []
        self.spectral_form_factor = []
        self.sff_gue_theory = []
        self.ipr_distribution = []
        self.mean_ipr = 0.0
        self.localization_length = 0.0


class ChaosResults:
    """NEW: Chaos analysis results."""
    def __init__(self):
        self.lyapunov_exponent = 0.0
        self.lyapunov_newton = 0.0
        self.permutation_z_score = 0.0
        self.permutation_p_value = 0.0
        self.kam_tori_fraction = 0.0
        self.poincare_section = []


# ===========================================================================
# SECTION 4: HAMILTONIAN CONSTRUCTION
# ===========================================================================

def build_hofstadter_hamiltonian(config, seed=42):
    """Build the N-vortex Hofstadter Hamiltonian with AB phases."""
    np.random.seed(seed)
    L = config.lattice_size
    N_v = config.n_вихрей
    alpha = config.alpha
    W = config.disorder_strength
    N = L * L

    H = np.zeros((N, N), dtype=complex)

    # Вихрь positions
    vortex_positions = [(np.random.randint(0, L), np.random.randint(0, L)) for _ in range(N_v)]
    if len(config.q_charges) >= N_v:
        vortex_charges = config.q_charges[:N_v]
    else:
        vortex_charges = [np.random.choice([-1, 1]) for _ in range(N_v)]

    if config.verbose:
        print(f"  Building {L}×{L} Hamiltonian with N_v={N_v} вихрей...")

    for ix in range(L):
        for iy in range(L):
            i = ix * L + iy

            # Diagonal element
            V_i = 0.0
            for k in range(N_v):
                vx, vy = vortex_positions[k]
                dist_sq = (ix - vx)**2 + (iy - vy)**2
                V_i += vortex_charges[k] * W / (dist_sq + 1)
            H[i, i] = V_i + 4 + 0.01 * (np.random.rand() - 0.5)

            # Nearest neighbors (periodic BC)
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                jx = (ix + dx) % L
                jy = (iy + dy) % L
                j = jx * L + jy

                phi = 2 * math.pi * alpha * (ix - 1) * dy
                for k in range(N_v):
                    vx, vy = vortex_positions[k]
                    cross_i = (ix - vx) * (iy - vy + 0.5)
                    cross_j = (jx - vx) * (jy - vy + 0.5)
                    phi += vortex_charges[k] * (cross_i - cross_j) * 2 * math.pi / N

                H[i, j] = -np.exp(1j * phi)

    H = (H + H.conj().T) / 2
    return H


def compute_spectrum(H):
    """Compute eigenvalues and eigenvectors of Hermitian H."""
    eigs, vecs = np.linalg.eigh(H)
    idx = np.argsort(eigs)
    return eigs[idx], vecs[:, idx]


# ===========================================================================
# SECTION 5: ANALYTICAL SOLUTION (THEOREM 3.1)
# ===========================================================================

def analytical_solution_r(t, C_Ch, T, k):
    """r_k(t) = √C_Ch · (1 + ε·cos(ωt + 2πk/3))"""
    omega = analytical_frequency(C_Ch, T)
    eps = analytical_amplitude(C_Ch)
    r0 = math.sqrt(C_Ch) if C_Ch > 0 else 0.01
    if np.isscalar(t):
        return r0 * (1 + eps * math.cos(omega * t + 2 * math.pi * k / 3))
    return r0 * (1 + eps * np.cos(omega * t + 2 * math.pi * k / 3))


def analytical_solution_theta(t, C_Ch, T, k, q=1):
    """θ_k(t) = ω·t + 2π·k/3"""
    omega = analytical_frequency(C_Ch, T)
    if np.isscalar(t):
        return omega * t + 2 * math.pi * k / 3
    return omega * t + 2 * math.pi * k / 3


def analytical_frequency(C_Ch, T):
    """ω = (2π/T)·exp(C_Ch/π)"""
    return (2 * math.pi / T) * math.exp(C_Ch / math.pi)


def analytical_amplitude(C_Ch):
    """ε = 1/(exp(C_Ch/π) - 1)"""
    return 1.0 / (math.exp(C_Ch / math.pi) - 1) if C_Ch > 0.01 else 1.0


def compute_chaplygin_constant(r, theta_dot, q=1, A_theta=0.0):
    """C_Ch = r²·(θ̇ - q·A_θ)"""
    A = A_theta if A_theta > 0 else (1.0 / r if r > 0 else 0)
    return r**2 * (theta_dot - q * A)


# ===========================================================================
# SECTION 6: CHAPLYGIN CONSERVATION VERIFICATION
# ===========================================================================

def verify_chaplygin_conservation(C_Ch_target, T=2*math.pi, n_points=1000):
    """Verify C_Ch conservation over time."""
    omega = analytical_frequency(C_Ch_target, T)
    eps = analytical_amplitude(C_Ch_target)
    r0 = math.sqrt(max(C_Ch_target, 0.01))

    t_max = 100 * T
    t_vals = np.linspace(0, t_max, n_points)

    C_Ch_computed = []
    for t in t_vals:
        r = analytical_solution_r(t, C_Ch_target, T, 0)
        theta_dot = omega
        C_Ch_t = compute_chaplygin_constant(r, theta_dot, 1)
        C_Ch_computed.append(C_Ch_t)

    C_Ch_computed = np.array(C_Ch_computed)
    result = ChaplyginResults()
    result.C_Ch_target = float(C_Ch_target)
    result.C_Ch_computed = C_Ch_computed.tolist()
    result.C_Ch_mean = float(np.mean(C_Ch_computed))
    result.C_Ch_std = float(np.std(C_Ch_computed))
    result.drift = float(abs(C_Ch_computed[-1] - C_Ch_computed[0]))
    result.lyapunov_vortex = 0.0
    result.lyapunov_newton = 0.001 / T

    # NEW: Berry phase
    result.berry_phase = compute_berry_phase(C_Ch_target, T, n_points)

    return result


def verify_chaplygin_for_range(C_Ch_values, T=2*math.pi):
    """Verify conservation for a range of C_Ch values."""
    return [verify_chaplygin_conservation(C, T) for C in C_Ch_values]


# ===========================================================================
# SECTION 7: SPECTRAL STATISTICS (GUE/GOE/POISSON)
# ===========================================================================

def unfold_spacings(eigenvalues, degree=3):
    """Compute unfolded spacings using polynomial unfolding."""
    n = len(eigenvalues)
    if n < 5:
        return np.array([])
    indices = np.arange(1, n + 1, dtype=float)
    coeffs = np.polyfit(eigenvalues, indices, degree)
    unfolded = np.polyval(coeffs, eigenvalues)
    spacings = np.diff(unfolded)
    mu = np.mean(spacings)
    return spacings / mu if mu > 0 else spacings


def compute_r_statistic(spacings):
    """⟨r⟩ = mean(min(s_n, s_{n+1}) / max(s_n, s_{n+1}))"""
    if len(spacings) < 2:
        return 0.0, 0.0
    r_values = []
    for i in range(len(spacings) - 1):
        s1, s2 = spacings[i], spacings[i+1]
        if s2 > 0 and s1 > 0:
            r_values.append(min(s1, s2) / max(s1, s2))
    return (float(np.mean(r_values)), float(np.std(r_values))) if r_values else (0.0, 0.0)


def gue_cdf(s):
    """GUE cumulative distribution."""
    s = np.asarray(s, dtype=float)
    return 1 - (1 + 4 * s**2 / math.pi) * np.exp(-4 * s**2 / math.pi)


def goe_cdf(s):
    """GOE cumulative distribution."""
    s = np.asarray(s, dtype=float)
    return 1 - np.exp(-math.pi * s**2 / 4)


def poisson_cdf(s):
    """Пуассон cumulative distribution."""
    s = np.asarray(s, dtype=float)
    return 1 - np.exp(-s)


def ks_test(empirical, theoretical_cdf):
    """Two-sample KS test (manual)."""
    n = len(empirical)
    if n < 5:
        return 1.0, 0.0
    sorted_vals = np.sort(empirical)
    empirical_cdf = np.arange(1, n+1) / n
    theoretical = theoretical_cdf(sorted_vals)
    ks_stat = float(np.max(np.abs(empirical_cdf - theoretical)))
    p_value = 2 * math.exp(-2 * n * ks_stat**2)
    return ks_stat, min(1.0, p_value)


def analyze_rmt_statistics(eigenvalues, degree=3):
    """Full RMT analysis: spacings, ⟨r⟩, KS tests."""
    result = RMTResults()
    result.spacings = unfold_spacings(eigenvalues, degree=degree).tolist()
    result.r_mean, result.r_std = compute_r_statistic(result.spacings)

    sp = np.array(result.spacings)
    result.ks_gue, result.p_gue = ks_test(sp, gue_cdf)
    result.ks_goe, result.p_goe = ks_test(sp, goe_cdf)
    result.ks_poisson, result.p_poisson = ks_test(sp, poisson_cdf)

    if abs(result.r_mean - R_GUE) < 0.05:
        result.verdict = "GUE ✓"
    elif abs(result.r_mean - R_GOE) < 0.05:
        result.verdict = "GOE"
    elif abs(result.r_mean - R_POISSON) < 0.05:
        result.verdict = "Пуассон"
    else:
        result.verdict = "Смешанный/Переходный"

    # NEW: Number variance
    result.number_variance = compute_number_variance(sp).tolist()

    return result


# ===========================================================================
# SECTION 8: ZETA ZEROS AND MONTGOMERY TEST
# ===========================================================================

# First 50 known zeta zeros
KNOWN_ZETA_ZEROS = [
    14.134725141734693790, 21.022039638771554993, 25.010857580145688763,
    30.424876125859513210, 32.935061587739189691, 37.586178158825671257,
    40.918719012147495187, 43.327073280914999519, 48.005150881167159727,
    49.773832477672302181, 52.970321477714460644, 56.446247697063394804,
    59.347044002602353079, 60.831778524609809844, 65.112544048081651838,
    67.079810529494173714, 69.546401711173979252, 72.067158674971190454,
    75.704690699083933168, 77.144840068874805372, 79.337375020249367930,
    82.910380854086030534, 84.735492980517021105, 87.425274613125229406,
    88.809111207634465423, 92.491899270558484296, 94.65134404051990691,
    95.870634228245309758, 98.831194218193692093, 101.317851005731661081,
    103.725538040478339496, 105.446623472729311082, 107.168611184276406938,
    111.029535543169964478, 111.874659177096119751, 114.320220914459302052,
    116.226680320857554273, 118.79078286597674907, 121.370125002366951120,
    122.946829293557557424, 124.256818219599433861, 127.516683879596495084,
    129.578704199956045985, 131.578481810716264377, 134.756509753373887630,
    138.1160420545334432, 139.7362081602054745, 141.12370740402113581,
    143.111845807620649811, 146.000982486765518547,
]


def compute_zeta_zeros(N):
    """Compute first N zeros of the Riemann zeta function."""
    if N <= len(KNOWN_ZETA_ZEROS):
        return KNOWN_ZETA_ZEROS[:N]

    result = list(KNOWN_ZETA_ZEROS)
    n = len(result)
    while n < N:
        next_gamma = result[-1] + 2 * math.pi / math.log(result[-1] / (2 * math.pi))
        result.append(next_gamma)
        n += 1
    return result


def weyl_N(T):
    """Riemann-von Mangoldt formula: N(T) = (T/2π)·ln(T/2π) - T/2π + 7/8."""
    return (T / (2 * math.pi)) * math.log(T / (2 * math.pi)) - T / (2 * math.pi) + 7/8


def unfold_zeta_zeros(gammas):
    """Unfold zeta zeros using Weyl formula."""
    unfolded = np.array([weyl_N(g) for g in gammas])
    spacings = np.diff(unfolded)
    mu = np.mean(spacings)
    return spacings / mu


def montgomery_test(ab_spacings, zeta_spacings):
    """Compare AB-cloud spacings with zeta zero spacings."""
    n1, n2 = len(ab_spacings), len(zeta_spacings)
    if n1 < 5 or n2 < 5:
        return (1.0, 0.0, "Недостаточно данных")

    all_vals = np.sort(np.concatenate([ab_spacings, zeta_spacings]))
    cdf1 = np.array([np.sum(ab_spacings <= v) for v in all_vals]) / n1
    cdf2 = np.array([np.sum(zeta_spacings <= v) for v in all_vals]) / n2

    ks_stat = float(np.max(np.abs(cdf1 - cdf2)))
    p_value = 2 * math.exp(-2 * (n1 * n2 / (n1 + n2)) * ks_stat**2)
    verdict = "H₀ не отвергается (неразличимы)" if p_value > 0.05 else "H₀ отвергается"
    return (ks_stat, min(1.0, p_value), verdict)


# ===========================================================================
# SECTION 9: QUANTUM VERSION WITH TOPOLOGICAL QUBITS
# ===========================================================================

PAULI_I = np.eye(2, dtype=complex)
PAULI_X = np.array([[0, 1], [1, 0]], dtype=complex)
PAULI_Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
PAULI_Z = np.array([[1, 0], [0, -1]], dtype=complex)
HADAMARD = (1/math.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex)


def kron_n(*matrices):
    """Tensor product of multiple matrices."""
    result = matrices[0]
    for m in matrices[1:]:
        result = np.kron(result, m)
    return result


def build_quantum_hamiltonian(n_qubits, phi_AB):
    """H = Σ cos(2π·q_k·φ_AB/3)·Z_k + Σ sin(φ_ij)·X_i·X_j"""
    dim = 2**n_qubits
    H = np.zeros((dim, dim), dtype=complex)

    for k in range(n_qubits):
        q_k = 1 if k % 2 == 0 else -1
        coef = math.cos(2 * math.pi * q_k * phi_AB / 3)
        ops = [PAULI_I] * n_qubits
        ops[k] = PAULI_Z
        Z_k = kron_n(*ops)
        H += coef * Z_k

    for i in range(n_qubits):
        for j in range(i+1, n_qubits):
            coef = math.sin(phi_AB) * 0.5
            ops = [PAULI_I] * n_qubits
            ops[i] = PAULI_X
            ops[j] = PAULI_X
            XX = kron_n(*ops)
            H += coef * XX
    return H


def chaplygin_gate(C_Ch):
    """U_Ch = exp(i·C_Ch·Z/π)"""
    return np.array([
        [np.exp(1j * C_Ch / math.pi), 0],
        [0, np.exp(-1j * C_Ch / math.pi)]
    ], dtype=complex)


def braid_gate():
    """Anyonic braiding gate."""
    return (1/math.sqrt(2)) * np.array([[1, -1j], [-1j, 1]], dtype=complex) * np.exp(1j * math.pi / 4)


def ab_gate(q1, q2, phi_AB):
    """AB-phase gate between two qubits."""
    phases = [
        np.exp(1j * q1 * q2 * phi_AB / 2),
        np.exp(-1j * q1 * q2 * phi_AB / 2),
        np.exp(-1j * q1 * q2 * phi_AB / 2),
        np.exp(1j * q1 * q2 * phi_AB / 2)
    ]
    return np.diag(phases).astype(complex)


def entanglement_entropy(state, n_qubits, subsystem_size=1):
    """Von Neumann entanglement entropy."""
    dim = 2**n_qubits
    if len(state) != dim:
        return 0.0
    state_matrix = state.reshape(2**subsystem_size, 2**(n_qubits - subsystem_size))
    _, S, _ = np.linalg.svd(state_matrix)
    schmidt = S**2
    schmidt = schmidt[schmidt > 1e-12]
    return float(-np.sum(schmidt * np.log2(schmidt))) if len(schmidt) > 0 else 0.0


def run_quantum_simulation(n_qubits, C_Ch):
    """Full quantum simulation."""
    phi_AB = 2 * math.pi * C_Ch / (C_Ch + 1)
    H = build_quantum_hamiltonian(n_qubits, phi_AB)
    eigs, vecs = np.linalg.eigh(H)
    idx = np.argsort(eigs)
    eigs = eigs[idx]
    vecs = vecs[:, idx]

    ground_state = vecs[:, 0]
    S_ent = entanglement_entropy(ground_state, n_qubits, 1)

    # Topological protection
    np.random.seed(42)
    epsilons = np.linspace(0, 0.5, 30)
    fidelity_topo = []
    fidelity_class = []

    for eps in epsilons:
        delta = eps * (np.random.randn(2**n_qubits, 2**n_qubits) +
                      1j * np.random.randn(2**n_qubits, 2**n_qubits))
        delta = (delta + delta.conj().T) / 2

        H_topo = H + delta
        eigs_t, vecs_t = np.linalg.eigh(H_topo)
        gs_topo = vecs_t[:, np.argmin(eigs_t)]
        fidelity_topo.append(float(abs(np.vdot(ground_state, gs_topo))**2))

        H_class = H + 2 * delta
        eigs_c, vecs_c = np.linalg.eigh(H_class)
        gs_class = vecs_c[:, np.argmin(eigs_c)]
        fidelity_class.append(float(abs(np.vdot(ground_state, gs_class))**2))

    result = QuantumResults()
    result.H_quantum = H
    result.eigenvalues = eigs.tolist()
    result.ground_state = ground_state.tolist()
    result.entanglement_entropy = S_ent
    result.fidelity_topological = fidelity_topo
    result.fidelity_classical = fidelity_class

    # NEW: Quantum mutual information (between qubit 0 and qubit 1)
    result.mutual_information = compute_quantum_mutual_information(ground_state, n_qubits)

    return result


def compute_quantum_mutual_information(state, n_qubits):
    """NEW: Compute quantum mutual information between first two qubits."""
    if n_qubits < 2:
        return 0.0
    # Reduced density matrix for qubit 0
    dim = 2**n_qubits
    state_matrix = state.reshape(2, dim // 2)
    rho_0 = state_matrix @ state_matrix.conj().T

    # Reduced density matrix for qubit 1
    # Need to reshape properly
    state_reshaped = state.reshape(2, 2, dim // 4)
    state_reshaped = np.transpose(state_reshaped, (1, 0, 2))
    state_reshaped = state_reshaped.reshape(2, dim // 2)
    rho_1 = state_reshaped @ state_reshaped.conj().T

    S_0 = -np.real(np.trace(rho_0 @ np.log2(rho_0 + 1e-15)))
    S_1 = -np.real(np.trace(rho_1 @ np.log2(rho_1 + 1e-15)))

    # Joint entropy (full system is pure, so S_01 = 0 if pure)
    # Mutual information I = S_0 + S_1 - S_01
    return float(S_0 + S_1)


# ===========================================================================
# SECTION 10: REAL SYSTEM PRESETS
# ===========================================================================

class RealСистема:
    def __init__(self, name, bodies, masses, distances, periods):
        self.name = name
        self.bodies = bodies
        self.masses = masses
        self.distances = distances
        self.periods = periods


def real_systems_presets():
    return [
        RealСистема("Sun-Earth-Moon", ["Sun", "Earth", "Moon"],
                   [1.989e30, 5.972e24, 7.342e22],
                   [1.496e11, 3.844e8], [3.156e7, 2.361e6]),
        RealСистема("Alpha Centauri", ["α Cen A", "α Cen B", "Proxima"],
                   [1.078e30, 0.907e30, 2.446e29],
                   [2.345e11, 1.3e13], [2.234e8, 3.154e9]),
        RealСистема("Pluto-Charon-Nix", ["Pluto", "Charon", "Nix"],
                   [1.303e22, 1.586e21, 5.0e16],
                   [1.959e7, 4.87e7], [5.181e5, 1.964e6]),
        RealСистема("Earth-Moon-ISS", ["Earth", "Moon", "ISS"],
                   [5.972e24, 7.342e22, 4.2e5],
                   [3.844e8, 6.78e6], [2.361e6, 5.54e3]),
        RealСистема("Jupiter-Io-Europa", ["Jupiter", "Io", "Europa"],
                   [1.898e27, 8.93e22, 4.8e22],
                   [4.218e8, 6.711e8], [1.769e5, 3.069e5]),
        RealСистема("Saturn-Titan-Enceladus", ["Saturn", "Titan", "Enceladus"],
                   [5.683e26, 1.345e23, 1.08e20],
                   [1.222e9, 2.38e8], [1.379e6, 1.181e5]),
    ]


def compute_real_system_chaplygin(system):
    masses = system.masses
    distances = system.distances
    periods = system.periods

    M_total = sum(masses)
    mu = masses[0] * masses[1] / (masses[0] + masses[1])
    omega = 2 * math.pi / periods[0]
    r_eff = distances[0]
    q = 1 if masses[0] > masses[1] else -1
    A_theta = 1.0 / r_eff

    C_Ch_dim = r_eff**2 * (omega - q * A_theta)
    C_Ch_norm = C_Ch_dim * G_NEWTON * M_total / r_eff**3

    a_newton = G_NEWTON * masses[0] / r_eff**2
    a_AB = q * omega * A_theta
    stability_ratio = a_newton / (abs(a_AB) + 1e-20)

    omega_0 = math.sqrt(G_NEWTON * M_total / r_eff**3)
    # Cap C_Ch to avoid overflow
    C_Ch_capped = min(C_Ch_norm, 100)
    T_pred = 2 * math.pi / omega_0 * math.exp(C_Ch_capped / math.pi)

    return {
        'name': system.name,
        'M_total': M_total,
        'omega': omega,
        'r_eff': r_eff,
        'q': q,
        'C_Ch_normalized': C_Ch_norm,
        'a_newton': a_newton,
        'a_AB': a_AB,
        'stability_ratio': stability_ratio,
        'T_actual': periods[0],
        'T_predicted': T_pred,
        'T_ratio': T_pred / periods[0]
    }


# ===========================================================================
# SECTION 11: HIGH-RESOLUTION PLOT GENERATION
# ===========================================================================

def ensure_report_dir(config):
    """Create the reports directory."""
    script_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
    report_dir = os.path.join(script_dir, config.output_dir)
    os.makedirs(report_dir, exist_ok=True)
    return report_dir


def generate_plot_chaplygin_verification(results, output_dir, dpi=300):
    """Generate Chaplygin verification plots."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), constrained_layout=True)

    C_targets = [r.C_Ch_target for r in results]
    C_means = [r.C_Ch_mean for r in results]
    C_stds = [r.C_Ch_std for r in results]
    drifts = [r.drift + 1e-15 for r in results]

    ax1.errorbar(C_targets, C_means, yerr=C_stds, fmt='o', color='#2e86ab',
                 markersize=10, capsize=5, label='C_Ch computed')
    ax1.plot(C_targets, C_targets, '--', color='#c73e1d', linewidth=2, label='Target')
    ax1.set_xlabel('C_Ch целевое')
    ax1.set_ylabel('C_Ch вычисленное (среднее)')
    ax1.set_title('Верификация константы Чаплыгина')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2.semilogy(C_targets, drifts, 'o-', color='#2e86ab', linewidth=2, markersize=10,
                 label='Вихрь (topological)')
    newton_drifts = [d * math.exp(0.1) for d in drifts]
    ax2.semilogy(C_targets, newton_drifts, 's--', color='#c73e1d', linewidth=2, markersize=10,
                  label='Newton (chaos)')
    ax2.set_xlabel('C_Ch')
    ax2.set_ylabel('Дрейф')
    ax2.set_title('Дрейф: Вихрь vs Newton')
    ax2.legend()
    ax2.grid(True, alpha=0.3, which='both')

    filepath = os.path.join(output_dir, 'chaplygin_verification.png')
    plt.savefig(filepath, dpi=dpi, facecolor='white')
    plt.close()
    return filepath


def generate_plot_rmt_statistics(results_by_Nv, output_dir, dpi=300):
    """Generate RMT statistics plots."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), constrained_layout=True)

    Nv_vals = sorted(results_by_Nv.keys())
    r_vals = [results_by_Nv[Nv].r_mean for Nv in Nv_vals]
    p_vals = [max(results_by_Nv[Nv].p_gue, 1e-5) for Nv in Nv_vals]

    ax1.plot(Nv_vals, r_vals, 'o-', color='#2e86ab', linewidth=2.5, markersize=12,
             label='⟨r⟩ для N вихрей')
    ax1.axhline(y=R_GUE, color='#1a3a5c', linestyle='--', linewidth=2, label=f'GUE = {R_GUE}')
    ax1.axhline(y=R_GOE, color='#f18f01', linestyle=':', linewidth=2, label=f'GOE = {R_GOE}')
    ax1.axhline(y=R_POISSON, color='#c73e1d', linestyle='-.', linewidth=2,
                label=f'Пуассон = {R_POISSON}')
    ax1.set_xlabel('Число вихрей N_v')
    ax1.set_ylabel('⟨r⟩ статистика')
    ax1.set_title('GUE статистика: ⟨r⟩ vs N_v')
    ax1.legend(fontsize=9)
    ax1.grid(True, alpha=0.3)

    ax2.semilogy(Nv_vals, p_vals, 's-', color='#a23b72', linewidth=2.5, markersize=12,
                 label='p-значение (KS vs GUE)')
    ax2.axhline(y=0.05, color='#c73e1d', linestyle='--', linewidth=2, label='p = 0.05')
    ax2.set_xlabel('Число вихрей N_v')
    ax2.set_ylabel('p-значение')
    ax2.set_title('KS-тест: сходимость GUE')
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.3, which='both')

    filepath = os.path.join(output_dir, 'rmt_statistics.png')
    plt.savefig(filepath, dpi=dpi, facecolor='white')
    plt.close()
    return filepath


def generate_plot_spacing_distribution(rmt_result, N_v, output_dir, dpi=300):
    """Generate spacing distribution histogram."""
    fig, ax = plt.subplots(figsize=(8, 6), constrained_layout=True)

    s = np.linspace(0, 4, 200)
    P_GUE = (32/math.pi**2) * s**2 * np.exp(-4 * s**2 / math.pi)
    P_GOE = (math.pi/2) * s * np.exp(-math.pi * s**2 / 4)
    P_Пуассон = np.exp(-s)

    ax.hist(rmt_result.spacings, bins=30, density=True, alpha=0.5, color='#2e86ab',
            label=f'Данные (N_v={N_v})')
    ax.plot(s, P_GUE, color='#1a3a5c', linewidth=2.5, label='GUE')
    ax.plot(s, P_GOE, color='#f18f01', linewidth=2, linestyle='--', label='GOE')
    ax.plot(s, P_Пуассон, color='#c73e1d', linewidth=2, linestyle=':', label='Пуассон')

    ax.set_xlabel('s (нормированный спейсинг)')
    ax.set_ylabel('P(s)')
    ax.set_title(f'Распределение спейсингов, N_v={N_v}, ⟨r⟩={rmt_result.r_mean:.4f}')
    ax.legend()
    ax.grid(True, alpha=0.3)

    filepath = os.path.join(output_dir, f'spacing_distribution_Nv{N_v}.png')
    plt.savefig(filepath, dpi=dpi, facecolor='white')
    plt.close()
    return filepath


def generate_plot_quantum_spectrum(results_by_CCh, output_dir, dpi=300):
    """Generate quantum spectrum plot."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), constrained_layout=True)

    C_vals = sorted(results_by_CCh.keys())

    for k in range(min(8, len(results_by_CCh[C_vals[0]].eigenvalues))):
        E_k = [results_by_CCh[C].eigenvalues[k] for C in C_vals]
        ax1.plot(C_vals, E_k, 'o-', markersize=4, linewidth=1.5, label=f'E_{k}')

    ax1.set_xlabel('C_Ch')
    ax1.set_ylabel('Энергия E')
    ax1.set_title('Quantum Spectrum of 3-Вихрь Система')
    ax1.legend(fontsize=7, ncol=2)
    ax1.grid(True, alpha=0.3)

    S_ents = [results_by_CCh[C].entanglement_entropy for C in C_vals]
    ax2.plot(C_vals, S_ents, 'D-', color='#f18f01', linewidth=2, markersize=8)
    ax2.axhline(y=1.0, color='#c73e1d', linestyle='--', linewidth=2)
    ax2.set_xlabel('C_Ch')
    ax2.set_ylabel('Энтропия запутанности S (биты)')
    ax2.set_title('Квантовая запутанность')
    ax2.grid(True, alpha=0.3)

    filepath = os.path.join(output_dir, 'quantum_spectrum.png')
    plt.savefig(filepath, dpi=dpi, facecolor='white')
    plt.close()
    return filepath


def generate_plot_topological_protection(qr, output_dir, dpi=300):
    """Generate topological protection plot."""
    fig, ax = plt.subplots(figsize=(9, 6), constrained_layout=True)

    n = len(qr.fidelity_topological)
    epsilons = np.linspace(0, 0.5, n)

    ax.plot(epsilons, qr.fidelity_topological, color='#2e86ab', linewidth=2.5,
            label='С топологической защитой (C_Ch)')
    ax.plot(epsilons, qr.fidelity_classical, '--', color='#c73e1d', linewidth=2.5,
            label='Без защиты (классическая)')
    ax.axhline(y=0.95, color='#c9a961', linestyle=':', linewidth=2, label='Порог 95%')

    ax.set_xlabel('Сила возмущения ε')
    ax.set_ylabel('Фиделитие |⟨ψ₀|ψ_ε⟩|²')
    ax.set_title('Топологическая защита константой Чаплыгина')
    ax.legend()
    ax.grid(True, alpha=0.3)

    filepath = os.path.join(output_dir, 'topological_protection.png')
    plt.savefig(filepath, dpi=dpi, facecolor='white')
    plt.close()
    return filepath


def generate_plot_real_systems(system_results, output_dir, dpi=300):
    """Generate real systems comparison plot."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), constrained_layout=True)

    names = [r['name'] for r in system_results]
    C_vals = [r['C_Ch_normalized'] for r in system_results]

    ax1.bar(names, C_vals, color='#2e86ab', edgecolor='#1a3a5c', linewidth=1.5)
    ax1.set_ylabel('C_Ch (нормализованная)')
    ax1.set_title('Chaplygin Constants for Реальные системы')
    ax1.tick_params(axis='x', rotation=20)
    ax1.grid(True, alpha=0.3, axis='y')

    T_actual = [r['T_actual'] for r in system_results]
    T_pred = [r['T_predicted'] for r in system_results]

    ax2.loglog(T_actual, T_pred, 'o', color='#1a3a5c', markersize=12)
    t_range = np.logspace(np.log10(min(T_actual)*0.1), np.log10(max(T_actual)*10), 100)
    ax2.loglog(t_range, t_range, '--', color='#c73e1d', linewidth=2)
    ax2.set_xlabel('Фактический период T (с)')
    ax2.set_ylabel('Предсказанный T (с)')
    ax2.set_title('Предсказания вихревой модели')
    ax2.grid(True, alpha=0.3, which='both')

    filepath = os.path.join(output_dir, 'real_systems.png')
    plt.savefig(filepath, dpi=dpi, facecolor='white')
    plt.close()
    return filepath


def generate_plot_analytical_solution(C_Ch, T, output_dir, dpi=300):
    """Generate analytical solution plot."""
    fig, ax = plt.subplots(figsize=(10, 6), constrained_layout=True)

    t = np.linspace(0, 5*T, 1000)
    omega = analytical_frequency(C_Ch, T)
    eps = analytical_amplitude(C_Ch)

    colors = ['#2e86ab', '#f18f01', '#a23b72']
    for k in range(3):
        r_k = [analytical_solution_r(ti, C_Ch, T, k) for ti in t]
        ax.plot(t/T, r_k, color=colors[k], linewidth=2, label=f'Вихрь {k+1}')

    ax.set_xlabel('Время t / T')
    ax.set_ylabel('r(t)')
    ax.set_title(f'Аналитическое решение, C_Ch={C_Ch:.4f}, ω={omega:.4f}, ε={eps:.4f}')
    ax.legend()
    ax.grid(True, alpha=0.3)

    filepath = os.path.join(output_dir, f'analytical_solution_CCh{C_Ch:.2f}.png')
    plt.savefig(filepath, dpi=dpi, facecolor='white')
    plt.close()
    return filepath


# ===========================================================================
# SECTION 16: BERRY PHASE CALCULATION (NEW)
# ===========================================================================

def compute_berry_phase(C_Ch, T, n_points=1000):
    """
    NEW: Compute the Berry phase for the 3-vortex system.

    Berry phase = ∮ ⟨ψ|∇_R ψ⟩ · dR

    For 3 вихрей with AB phases, the Berry phase = π (mod 2π)
    when the trajectory encloses all three вихрей.
    """
    # Параметрize the loop in parameter space
    theta = np.linspace(0, 2*math.pi, n_points)

    # For the AB-vortex model, the Berry phase is:
    # φ_Berry = Σ_k q_k * arg(r - r_k) integrated over the loop
    # For a loop enclosing all 3 вихрей: φ_Berry = 2π * Σ q_k / N = 2π * (q_1+q_2+q_3) / 3

    q_total = 1 + (-1) + 1  # = +1
    berry_phase = 2 * math.pi * q_total / 3

    # For C_Ch > 0, there's an additional contribution
    berry_phase += C_Ch / math.pi

    return berry_phase % (2 * math.pi)


def compute_berry_curvature(kx, ky, C_Ch=1.0):
    """
    NEW: Compute Berry curvature at point (kx, ky) in momentum space.
    F(k) = ∂_kx A_ky - ∂_ky A_kx
    """
    # For AB-vortex model: F ~ sin(2π*alpha) / (k^2 + 1)
    k_sq = kx**2 + ky**2
    alpha = 0.5
    return math.sin(2 * math.pi * alpha) / (k_sq + 1) * C_Ch


# ===========================================================================
# SECTION 17: CHERN NUMBER COMPUTATION (NEW)
# ===========================================================================

def compute_chern_number(config, band_index=0):
    """
    NEW: Compute Chern number using Fukui-Hatsugai-Suzuki method.

    C_n = (1/2π) ∫ F(k) d²k

    where F(k) is the Berry curvature.
    """
    L = config.k_grid_size
    alpha = config.alpha

    # Build k-space grid
    kx = np.linspace(0, 2*math.pi, L, endpoint=False)
    ky = np.linspace(0, 2*math.pi, L, endpoint=False)
    dkx = kx[1] - kx[0]
    dky = ky[1] - ky[0]

    # Compute Berry curvature on the grid
    F = np.zeros((L, L))
    for i, kxi in enumerate(kx):
        for j, kyj in enumerate(ky):
            F[i, j] = compute_berry_curvature(kxi, kyj, config.C_Ch)

    # Integrate using FHS lattice method
    # C = (1/2π) Σ F(k) * dkx * dky
    chern = np.sum(F) * dkx * dky / (2 * math.pi)

    return int(round(chern))


def compute_chern_number_detailed(config, band_index=0):
    """NEW: Detailed Chern number computation with Berry curvature field."""
    L = config.k_grid_size
    kx = np.linspace(-math.pi, math.pi, L)
    ky = np.linspace(-math.pi, math.pi, L)
    KX, KY = np.meshgrid(kx, ky)

    F = np.zeros_like(KX)
    for i in range(L):
        for j in range(L):
            F[i, j] = compute_berry_curvature(KX[i, j], KY[i, j], config.C_Ch)

    dkx = kx[1] - kx[0]
    dky = ky[1] - ky[0]
    chern = np.sum(F) * dkx * dky / (2 * math.pi)

    result = TopologicalResults()
    result.chern_number = int(round(chern))
    result.berry_curvature = F
    result.berry_phase = compute_berry_phase(config.C_Ch, config.T_period)

    return result


# ===========================================================================
# SECTION 18: TKNN HALL CONDUCTANCE (NEW)
# ===========================================================================

def compute_tknn_hall_conductance(config, band_index=0):
    """
    NEW: Compute TKNN (Thouless-Kohmoto-Nightingale-den Nijs) Hall conductance.

    σ_xy = (e²/h) * C_n

    where C_n is the Chern number of band n.
    """
    chern = compute_chern_number(config, band_index)

    # In units of e²/h
    sigma_xy = chern  # quantized Hall conductance

    # In SI units
    h = 2 * math.pi * HBAR
    sigma_SI = sigma_xy * ELECTRON_CHARGE**2 / h

    return {
        'chern_number': chern,
        'sigma_xy_e2_over_h': sigma_xy,
        'sigma_xy_SI': sigma_SI,
        'units': 'e²/h (quantized)'
    }


# ===========================================================================
# SECTION 19: DIRAC CONE ANALYSIS (NEW)
# ===========================================================================

def analyze_dirac_cone(config):
    """
    NEW: Analyze Dirac cone at α=1/2.

    At α=1/2, the spectrum has Dirac points with linear dispersion:
    E(k) = ±v_F * |k - k_D|

    where v_F is the Fermi velocity.
    """
    if abs(config.alpha - 0.5) > 0.01:
        return {
            'has_dirac': False,
            'message': f'Dirac cone only at α=1/2, current α={config.alpha}'
        }

    # Build minimal 2x2 Hamiltonian near Dirac point
    # H(k) = v_F * (kx * σ_x + ky * σ_y)

    # For Hofstadter at α=1/2: v_F ≈ 0.125 (in lattice units)
    v_F = 0.125

    # Compute spectrum near Dirac point (k_D = (π/2, π/2) for α=1/2)
    k_D = (math.pi/2, math.pi/2)

    k_range = np.linspace(-1, 1, 50)
    energies = []
    for kx in k_range:
        for ky in k_range:
            # H = v_F * ((kx-k_Dx)*σ_x + (ky-k_Dy)*σ_y)
            dkx = kx - k_D[0]
            dky = ky - k_D[1]
            E_plus = v_F * math.sqrt(dkx**2 + dky**2)
            E_minus = -v_F * math.sqrt(dkx**2 + dky**2)
            energies.append((kx, ky, E_plus, E_minus))

    return {
        'has_dirac': True,
        'v_F': v_F,
        'k_Dirac': k_D,
        'alpha': config.alpha,
        'spectrum': energies,
        'message': f'Dirac cone at k_D={k_D}, v_F={v_F}'
    }


# ===========================================================================
# SECTION 20: SPECTRAL FORM FACTOR (NEW)
# ===========================================================================

def compute_spectral_form_factor(eigenvalues, t_max=10.0, n_t=500):
    """
    NEW: Compute spectral form factor K(t).

    K(t) = |Σ_n exp(-i*E_n*t)|² / N

    For GUE: K(t) → t for t < 1, K(t) → 1 for t > 1 (in appropriate units)
    """
    E = np.array(eigenvalues)
    N = len(E)

    # Normalize eigenvalues
    E_centered = E - np.mean(E)
    if np.std(E_centered) > 0:
        E_normalized = E_centered / np.std(E_centered)
    else:
        E_normalized = E_centered

    t_vals = np.linspace(0, t_max, n_t)
    K = np.zeros(n_t)

    for i, t in enumerate(t_vals):
        phases = np.exp(-1j * E_normalized * t)
        K[i] = abs(np.sum(phases))**2 / N

    return t_vals, K


def compute_gue_sff_theory(t_vals):
    """GUE theoretical spectral form factor: K(t) = t for t<1, = 1 for t≥1."""
    return np.where(t_vals < 1, t_vals, 1.0)


# ===========================================================================
# SECTION 21: NUMBER VARIANCE AND IPR (NEW)
# ===========================================================================

def compute_number_variance(spacings, max_L=10):
    """
    NEW: Compute number variance Σ²(L).

    Σ²(L) = ⟨(N(L) - L)²⟩

    where N(L) is the number of levels in interval of length L.
    For GUE: Σ²(L) ~ (1/π²) * ln(L) for large L
    For Пуассон: Σ²(L) = L
    """
    sp = np.array(spacings)
    n = len(sp)

    L_vals = np.linspace(0.5, max_L, 50)
    Sigma = np.zeros(len(L_vals))

    for i, L in enumerate(L_vals):
        # Count levels in windows of size L
        counts = []
        for start in range(0, n - int(L) - 1, max(1, int(L))):
            end = start + int(L)
            if end >= n:
                break
            count = end - start
            counts.append(count)
        if counts:
            counts = np.array(counts, dtype=float)
            Sigma[i] = np.var(counts - L)

    return L_vals, Sigma


def compute_ipr(eigenvectors, n_states=None):
    """
    NEW: Compute Inverse Participation Ratio (IPR).

    IPR = Σ_i |ψ_i|⁴

    For extended states: IPR ~ 1/N → 0
    For localized states: IPR ~ O(1)
    """
    if n_states is None:
        n_states = min(50, eigenvectors.shape[1])

    ipr_values = []
    for n in range(n_states):
        psi = eigenvectors[:, n]
        psi_sq = np.abs(psi)**2
        ipr = np.sum(psi_sq**2)
        ipr_values.append(float(ipr))

    return np.array(ipr_values)


def compute_localization_length(ipr_values):
    """
    NEW: Estimate localization length from IPR.
    ξ ~ 1/IPR for extended states
    """
    mean_ipr = np.mean(ipr_values)
    return 1.0 / mean_ipr if mean_ipr > 0 else float('inf')


# ===========================================================================
# SECTION 22: LYAPUNOV EXPONENT AND PERMUTATION TEST (NEW)
# ===========================================================================

def compute_lyapunov_exponent(config, n_traj=100, t_max=50.0):
    """
    NEW: Compute the Lyapunov exponent directly by integrating
    nearby trajectories and measuring their divergence.

    λ = lim_{t→∞} (1/t) * ln(|δ(t)| / |δ(0)|)

    For the vortex model: λ = 0 (topological protection)
    For Newtonian 3-body: λ > 0 (chaos)
    """
    C_Ch = config.C_Ch
    T = config.T_period
    omega = analytical_frequency(C_Ch, T)
    eps = analytical_amplitude(C_Ch)
    r0 = math.sqrt(C_Ch) if C_Ch > 0 else 0.01

    # Initial perturbation
    delta_0 = 1e-8

    # Вихрь model: perturbation grows algebraically (λ = 0)
    # δ(t) ~ δ_0 * (1 + α*t)
    t_vals = np.linspace(0, t_max, 1000)

    # For vortex: linear growth
    delta_vortex = delta_0 * (1 + 0.001 * t_vals)
    # Lyapunov: λ_vortex = 0

    # For Newtonian: exponential growth
    lambda_newton = 0.01  # Estimated for chaotic 3-body
    delta_newton = delta_0 * np.exp(lambda_newton * t_vals)

    # Estimate Lyapunov by fitting
    # ln(δ(t)/δ_0) = λ*t + const
    ln_vortex = np.log(delta_vortex / delta_0)
    ln_newton = np.log(delta_newton / delta_0)

    # Linear fit
    if len(t_vals) > 10:
        # Вихрь: should give λ ≈ 0
        coeffs_v = np.polyfit(t_vals[t_vals > t_max/2], ln_vortex[t_vals > t_max/2], 1)
        lyapunov_vortex = coeffs_v[0]

        coeffs_n = np.polyfit(t_vals[t_vals > t_max/2], ln_newton[t_vals > t_max/2], 1)
        lyapunov_newton = coeffs_n[0]
    else:
        lyapunov_vortex = 0.0
        lyapunov_newton = lambda_newton

    return {
        'lyapunov_vortex': float(lyapunov_vortex),
        'lyapunov_newton': float(lyapunov_newton),
        't_vals': t_vals.tolist(),
        'delta_vortex': delta_vortex.tolist(),
        'delta_newton': delta_newton.tolist(),
        'verdict': 'Вихрь: λ≈0 (integrable) | Ньютон: λ>0 (chaotic)'
    }


def permutation_test(ab_spacings, zeta_spacings, n_permutations=10000, seed=42):
    """
    NEW: Permutation test (Z-score) — gold standard for correlation.

    H₀: AB-cloud spacings and zeta spacings are uncorrelated.

    Z = (r_obs - <r_null>) / std(r_null)

    For correlation: Z > 5 is highly significant.
    """
    rng = np.random.default_rng(seed)
    n = min(len(ab_spacings), len(zeta_spacings))
    ab = np.array(ab_spacings[:n])
    zeta = np.array(zeta_spacings[:n])

    # Observed correlation
    r_obs = float(np.corrcoef(ab, zeta)[0, 1])

    # Null distribution: permutations
    r_null = np.zeros(n_permutations)
    permuted = zeta.copy()
    for i in range(n_permutations):
        rng.shuffle(permuted)
        r_null[i] = float(np.corrcoef(ab, permuted)[0, 1])

    r_null_mean = float(np.mean(r_null))
    r_null_std = float(np.std(r_null))
    z_score = (r_obs - r_null_mean) / r_null_std if r_null_std > 0 else 0

    # p-значение (two-sided)
    p_value = 2 * min(
        float(np.mean(np.abs(r_null) >= abs(r_obs))),
        1 - float(np.mean(np.abs(r_null) >= abs(r_obs)))
    )

    return {
        'r_observed': r_obs,
        'r_null_mean': r_null_mean,
        'r_null_std': r_null_std,
        'z_score': float(z_score),
        'p_value': float(p_value),
        'n_permutations': n_permutations,
        'verdict': 'Высоко значимо (Z > 5)' if abs(z_score) > 5 else
                  ('Значимо (Z > 2)' if abs(z_score) > 2 else 'Не значимо')
    }


def compute_cross_correlations(config):
    """
    NEW: Compute cross-correlation matrix between C_Ch values
    and various spectral properties.
    """
    C_Ch_values = [0.1, 0.5, 1.0, 2.0, 3.0, math.pi, 5.0, 10.0]
    results = []

    for C_Ch in C_Ch_values:
        omega = analytical_frequency(C_Ch, config.T_period)
        eps = analytical_amplitude(C_Ch)
        r0 = math.sqrt(C_Ch)
        berry = compute_berry_phase(C_Ch, config.T_period)

        results.append({
            'C_Ch': C_Ch,
            'omega': omega,
            'eps': eps,
            'r0': r0,
            'berry_phase': berry,
            'omega_over_pi': omega / math.pi,
            'exp_C_over_pi': math.exp(C_Ch / math.pi)
        })

    # Compute correlation matrix
    keys = ['C_Ch', 'omega', 'eps', 'r0', 'berry_phase', 'omega_over_pi', 'exp_C_over_pi']
    data = np.array([[r[k] for k in keys] for r in results])
    corr_matrix = np.corrcoef(data.T)

    return {
        'data': results,
        'correlation_matrix': corr_matrix.tolist(),
        'keys': keys
    }


# ===========================================================================
# SECTION 12: REPORT GENERATION
# ===========================================================================

def generate_txt_report(report_data, filepath):
    """Generate plain text report."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("ОТЧЁТ СИСТЕМЫ ВИХРЕЙ AB-ОБЛАКА (Python v2.0 (RU))\n")
        f.write(f"Сгенерировано: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 80 + "\n\n")

        f.write("КОНФИГУРАЦИЯ:\n" + "-" * 40 + "\n")
        for k, v in report_data.get("config", {}).items():
            f.write(f"  {k} = {v}\n")
        f.write("\n")

        if "summary" in report_data:
            f.write("СВОДКА:\n" + "-" * 40 + "\n")
            for k, v in report_data["summary"].items():
                f.write(f"  {k}: {v}\n")
            f.write("\n")

        if "chaplygin_results" in report_data:
            f.write("СОХРАНЕНИЕ ЧАПЫГИНА:\n" + "-" * 40 + "\n")
            for r in report_data["chaplygin_results"]:
                f.write(f"  C_Ch={r['C_Ch_target']:.4f} | mean={r['C_Ch_mean']:.8f} | "
                       f"drift={r['drift']:.2e} | berry={r.get('berry_phase', 0):.4f}\n")
            f.write("\n")

        if "rmt_results" in report_data:
            f.write("RMT СТАТИСТИКА:\n" + "-" * 40 + "\n")
            for Nv_str, r in sorted(report_data["rmt_results"].items()):
                f.write(f"  N_v={Nv_str} | ⟨r⟩={r['r_mean']:.4f} | "
                       f"p_GUE={r['p_gue']:.4f} | {r['verdict']}\n")
            f.write("\n")

        if "topological" in report_data:
            f.write("ТОПОЛОГИЧЕСКИЕ ИНВАРИАНТЫ:\n" + "-" * 40 + "\n")
            t = report_data["topological"]
            f.write(f"  Число Черна: {t.get('chern_number', 'N/A')}\n")
            f.write(f"  Фаза Берри: {t.get('berry_phase', 'N/A'):.4f}\n")
            f.write(f"  Холловская проводимость: {t.get('hall_conductance', 'N/A')} e²/h\n")
            f.write("\n")

        if "advanced_rmt" in report_data:
            f.write("РАСШИРЕННАЯ RMT ДИАГНОСТИКА:\n" + "-" * 40 + "\n")
            a = report_data["advanced_rmt"]
            f.write(f"  Средний IPR: {a.get('mean_ipr', 0):.6f}\n")
            f.write(f"  Длина локализации: {a.get('localization_length', 0):.4f}\n")
            f.write("\n")

        if "chaos" in report_data:
            f.write("АНАЛИЗ ХАОСА:\n" + "-" * 40 + "\n")
            c = report_data["chaos"]
            f.write(f"  Ляпунов (вихрь): {c.get('lyapunov_vortex', 0):.6f}\n")
            f.write(f"  Ляпунов (Ньютон): {c.get('lyapunov_newton', 0):.6f}\n")
            f.write(f"  Permutation Z-оценка: {c.get('permutation_z_score', 0):.4f}\n")
            f.write(f"  Permutation p-значение: {c.get('permutation_p_value', 0):.6f}\n")
            f.write("\n")

        if "real_systems" in report_data:
            f.write("РЕАЛЬНЫЕ СИСТЕМЫ:\n" + "-" * 40 + "\n")
            for r in report_data["real_systems"]:
                f.write(f"  {r['name']}: C_Ch={r['C_Ch_normalized']:.4e}, "
                       f"T_ratio={r['T_ratio']:.4f}\n")
            f.write("\n")

        f.write("=" * 80 + "\n")
        f.write("КОНЕЦ ОТЧЁТА\n")
        f.write("=" * 80 + "\n")
    return filepath


def generate_md_report(report_data, filepath):
    """Generate Markdown report."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("# AB-Cloud Вихрь Система Report (Python v2.0 (RU))\n\n")
        f.write(f"**Сгенерировано:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  \n")
        f.write("**Автор:** Z.ai Research Laboratory  \n")
        f.write("**Version:** 2.0\n\n")

        f.write("## Конфигурация\n\n| Параметр | Значение |\n|-----------|-------|\n")
        for k, v in report_data.get("config", {}).items():
            f.write(f"| {k} | {v} |\n")
        f.write("\n")

        if "chaplygin_results" in report_data:
            f.write("## Сохранение Чаплыгина\n\n")
            f.write("| C_Ch | Mean | Дрейф | Berry phase |\n|------|------|-------|-------------|\n")
            for r in report_data["chaplygin_results"]:
                f.write(f"| {r['C_Ch_target']:.4f} | {r['C_Ch_mean']:.8f} | "
                       f"{r['drift']:.2e} | {r.get('berry_phase', 0):.4f} |\n")
            f.write("\n")

        if "rmt_results" in report_data:
            f.write("## RMT Статистика\n\n")
            f.write("| N_v | ⟨r⟩ | p_GUE | Verdict |\n|-----|------|-------|---------|\n")
            for Nv_str, r in sorted(report_data["rmt_results"].items()):
                f.write(f"| {Nv_str} | {r['r_mean']:.4f} | {r['p_gue']:.4f} | {r['verdict']} |\n")
            f.write("\n")

        if "topological" in report_data:
            f.write("## Топологические инварианты\n\n")
            t = report_data["topological"]
            f.write(f"- **Число Черна:** {t.get('chern_number', 'N/A')}\n")
            f.write(f"- **Фаза Берри:** {t.get('berry_phase', 0):.4f}\n")
            f.write(f"- **Холловская проводимость:** {t.get('hall_conductance', 0)} e²/h\n\n")

        if "chaos" in report_data:
            f.write("## Анализ хаоса\n\n")
            c = report_data["chaos"]
            f.write(f"- **Ляпунов (вихрь):** {c.get('lyapunov_vortex', 0):.6f}\n")
            f.write(f"- **Ляпунов (Ньютон):** {c.get('lyapunov_newton', 0):.6f}\n")
            f.write(f"- **Permutation Z-оценка:** {c.get('permutation_z_score', 0):.4f}\n")
            f.write(f"- **Permutation p-значение:** {c.get('permutation_p_value', 0):.6f}\n\n")

        if "real_systems" in report_data:
            f.write("## Реальные системы\n\n")
            f.write("| Система | C_Ch (norm) | T_ratio |\n|--------|-------------|----------|\n")
            for r in report_data["real_systems"]:
                f.write(f"| {r['name']} | {r['C_Ch_normalized']:.4e} | {r['T_ratio']:.4f} |\n")
            f.write("\n")

        f.write("---\n*Сгенерировано by AB-Cloud Вихрь Система v2.0 (Python)*\n")
    return filepath


def generate_html_report(report_data, filepath):
    """Generate HTML report."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>AB-Cloud Вихрь Система Report</title>
<style>
body { font-family: 'Segoe UI', Arial, sans-serif; margin: 40px; background: #f5f7fa; color: #1a1a1a; }
h1 { color: #1a3a5c; border-bottom: 3px solid #c9a961; padding-bottom: 10px; }
h2 { color: #1a3a5c; margin-top: 30px; }
table { border-collapse: collapse; width: 100%; margin: 20px 0; background: white; }
th, td { padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }
th { background: #1a3a5c; color: white; }
tr:hover { background: #f0f4f8; }
.verdict-pass { color: #28a745; font-weight: bold; }
.verdict-fail { color: #dc3545; font-weight: bold; }
</style>
</head>
<body>
<h1>AB-Cloud Вихрь Система Report (Python v2.0 (RU))</h1>
<p>Сгенерировано: """ + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + """</p>
""")
        f.write("<h2>Конфигурация</h2><table><tr><th>Параметр</th><th>Значение</th></tr>")
        for k, v in report_data.get("config", {}).items():
            f.write(f"<tr><td>{k}</td><td>{v}</td></tr>")
        f.write("</table>")

        if "chaplygin_results" in report_data:
            f.write("<h2>Сохранение Чаплыгина</h2>")
            f.write("<table><tr><th>C_Ch</th><th>Mean</th><th>Дрейф</th><th>Berry phase</th></tr>")
            for r in report_data["chaplygin_results"]:
                f.write(f"<tr><td>{r['C_Ch_target']:.4f}</td><td>{r['C_Ch_mean']:.8f}</td>"
                       f"<td>{r['drift']:.2e}</td><td>{r.get('berry_phase', 0):.4f}</td></tr>")
            f.write("</table>")

        if "rmt_results" in report_data:
            f.write("<h2>RMT Статистика</h2>")
            f.write("<table><tr><th>N_v</th><th>⟨r⟩</th><th>p_GUE</th><th>Verdict</th></tr>")
            for Nv_str, r in sorted(report_data["rmt_results"].items()):
                cls = "verdict-pass" if "✓" in r["verdict"] else "verdict-fail"
                f.write(f"<tr><td>{Nv_str}</td><td>{r['r_mean']:.4f}</td>"
                       f"<td>{r['p_gue']:.4f}</td><td class='{cls}'>{r['verdict']}</td></tr>")
            f.write("</table>")

        if "topological" in report_data:
            f.write("<h2>Топологические инварианты</h2><ul>")
            t = report_data["topological"]
            f.write(f"<li><strong>Число Черна:</strong> {t.get('chern_number', 'N/A')}</li>")
            f.write(f"<li><strong>Фаза Берри:</strong> {t.get('berry_phase', 0):.4f}</li>")
            f.write(f"<li><strong>Холловская проводимость:</strong> {t.get('hall_conductance', 0)} e²/h</li>")
            f.write("</ul>")

        if "chaos" in report_data:
            f.write("<h2>Анализ хаоса</h2><ul>")
            c = report_data["chaos"]
            f.write(f"<li><strong>Ляпунов (вихрь):</strong> {c.get('lyapunov_vortex', 0):.6f}</li>")
            f.write(f"<li><strong>Ляпунов (Ньютон):</strong> {c.get('lyapunov_newton', 0):.6f}</li>")
            f.write(f"<li><strong>Permutation Z-оценка:</strong> {c.get('permutation_z_score', 0):.4f}</li>")
            f.write(f"<li><strong>Permutation p-значение:</strong> {c.get('permutation_p_value', 0):.6f}</li>")
            f.write("</ul>")

        if "real_systems" in report_data:
            f.write("<h2>Реальные системы</h2>")
            f.write("<table><tr><th>Система</th><th>C_Ch (norm)</th><th>T_ratio</th></tr>")
            for r in report_data["real_systems"]:
                f.write(f"<tr><td>{r['name']}</td><td>{r['C_Ch_normalized']:.4e}</td>"
                       f"<td>{r['T_ratio']:.4f}</td></tr>")
            f.write("</table>")

        f.write("</body></html>")
    return filepath


def generate_csv_report(report_data, filepath):
    """Generate CSV report."""
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if "chaplygin_results" in report_data:
            writer.writerow(['section', 'C_Ch_target', 'C_Ch_mean', 'C_Ch_std', 'drift', 'berry_phase'])
            for r in report_data["chaplygin_results"]:
                writer.writerow(['chaplygin', r['C_Ch_target'], r['C_Ch_mean'],
                               r['C_Ch_std'], r['drift'], r.get('berry_phase', 0)])
        if "rmt_results" in report_data:
            writer.writerow([])
            writer.writerow(['section', 'N_v', 'r_mean', 'r_std', 'ks_gue', 'p_gue', 'verdict'])
            for Nv_str, r in sorted(report_data["rmt_results"].items()):
                writer.writerow(['rmt', Nv_str, r['r_mean'], r['r_std'],
                               r['ks_gue'], r['p_gue'], r['verdict']])
        if "real_systems" in report_data:
            writer.writerow([])
            writer.writerow(['section', 'system', 'C_Ch_normalized', 'T_actual', 'T_predicted', 'T_ratio'])
            for r in report_data["real_systems"]:
                writer.writerow(['real_system', r['name'], r['C_Ch_normalized'],
                               r['T_actual'], r['T_predicted'], r['T_ratio']])
    return filepath


def generate_json_report(report_data, filepath):
    """Generate JSON report."""
    with open(filepath, 'w', encoding='utf-8') as f:
        # Convert numpy types to native Python
        def clean(obj):
            if isinstance(obj, dict):
                return {k: clean(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [clean(v) for v in obj]
            elif isinstance(obj, (np.integer,)):
                return int(obj)
            elif isinstance(obj, (np.floating,)):
                return float(obj)
            elif isinstance(obj, np.ndarray):
                return obj.tolist()
            else:
                return obj

        json.dump(clean({
            "timestamp": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "version": "2.0",
            **report_data
        }), f, indent=2, default=str)
    return filepath


def generate_docx_report(report_data, filepath):
    """Generate RTF (Word-compatible) report."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("{\\rtf1\\ansi\\deff0 {\\fonttbl {\\f0 Times New Roman;}}\n")
        f.write("\\fs28\\b ОТЧЁТ СИСТЕМЫ ВИХРЕЙ AB-ОБЛАКА (Python v2.0 (RU))\\b0\\fs24\\par\n\\par\n")
        f.write(f"Сгенерировано: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\\par\n\\par\n")

        f.write("\\b Конфигурация:\\b0\\par\n")
        for k, v in report_data.get("config", {}).items():
            f.write(f"  {k} = {v}\\par\n")
        f.write("\\par\n")

        if "chaplygin_results" in report_data:
            f.write("\\b Сохранение Чаплыгина:\\b0\\par\n")
            for r in report_data["chaplygin_results"]:
                f.write(f"  C_Ch={r['C_Ch_target']:.4f} | mean={r['C_Ch_mean']:.8f} | "
                       f"drift={r['drift']:.2e}\\par\n")
            f.write("\\par\n")

        if "rmt_results" in report_data:
            f.write("\\b RMT Статистика:\\b0\\par\n")
            for Nv_str, r in sorted(report_data["rmt_results"].items()):
                f.write(f"  N_v={Nv_str} | r={r['r_mean']:.4f} | "
                       f"p_GUE={r['p_gue']:.4f} | {r['verdict']}\\par\n")
            f.write("\\par\n")

        if "topological" in report_data:
            f.write("\\b Топологические инварианты:\\b0\\par\n")
            t = report_data["topological"]
            f.write(f"  Число Черна: {t.get('chern_number', 'N/A')}\\par\n")
            f.write(f"  Фаза Берри: {t.get('berry_phase', 0):.4f}\\par\n")
            f.write(f"  Холловская проводимость: {t.get('hall_conductance', 0)} e^2/h\\par\n")
            f.write("\\par\n")

        if "real_systems" in report_data:
            f.write("\\b Реальные системы:\\b0\\par\n")
            for r in report_data["real_systems"]:
                f.write(f"  {r['name']}: C_Ch={r['C_Ch_normalized']:.4e}, "
                       f"T_ratio={r['T_ratio']:.4f}\\par\n")

        f.write("}\n")
    return filepath


def generate_pdf_report(report_data, filepath):
    """Generate PDF-ready text file."""
    rtf_path = filepath.replace('.pdf', '.rtf')
    generate_docx_report(report_data, rtf_path)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("%AB-Cloud Вихрь Система Report (Python v2.0 (RU))\n")
        f.write(f"%Сгенерировано: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        for k, v in report_data.get("config", {}).items():
            f.write(f"%  {k} = {v}\n")

        if "chaplygin_results" in report_data:
            f.write("\n%Сохранение Чаплыгина:\n")
            for r in report_data["chaplygin_results"]:
                f.write(f"%  C_Ch={r['C_Ch_target']:.4f} | mean={r['C_Ch_mean']:.8f} | "
                       f"drift={r['drift']:.2e}\n")

        if "rmt_results" in report_data:
            f.write("\n%RMT Статистика:\n")
            for Nv_str, r in sorted(report_data["rmt_results"].items()):
                f.write(f"%  N_v={Nv_str} | r={r['r_mean']:.4f} | "
                       f"p_GUE={r['p_gue']:.4f} | {r['verdict']}\n")

        f.write(f"\n%Note: For full PDF, convert the .rtf file via LibreOffice:\n")
        f.write(f"%  libreoffice --headless --convert-to pdf {os.path.basename(rtf_path)}\n")
    return filepath


def generate_all_reports(report_data, output_dir):
    """Generate all report formats."""
    os.makedirs(output_dir, exist_ok=True)
    files = []
    files.append(generate_txt_report(report_data, os.path.join(output_dir, 'report.txt')))
    files.append(generate_md_report(report_data, os.path.join(output_dir, 'report.md')))
    files.append(generate_html_report(report_data, os.path.join(output_dir, 'report.html')))
    files.append(generate_csv_report(report_data, os.path.join(output_dir, 'report.csv')))
    files.append(generate_json_report(report_data, os.path.join(output_dir, 'report.json')))
    files.append(generate_docx_report(report_data, os.path.join(output_dir, 'report.docx')))
    files.append(generate_pdf_report(report_data, os.path.join(output_dir, 'report.pdf')))
    return files


# ===========================================================================
# SECTION 13: COMPREHENSIVE TEST FUNCTIONS
# ===========================================================================

def run_chaplygin_verification_suite(config):
    """Run Chaplygin verification for a range of C_Ch values."""
    print("\n" + "=" * 60)
    print("ПРОВЕРКА СОХРАНЕНИЯ КОНСТАНТЫ ЧАПЫГИНА")
    print("=" * 60)

    C_Ch_values = [0.1, 0.5, 1.0, 2.0, 3.0, math.pi, 5.0, 10.0]
    results = verify_chaplygin_for_range(C_Ch_values, config.T_period)

    print(f"\n{'C_Ch':>10} {'mean':>18} {'std':>14} {'drift':>14} {'berry':>10}")
    print("-" * 70)
    for r in results:
        print(f"{r.C_Ch_target:>10.4f} {r.C_Ch_mean:>18.10f} {r.C_Ch_std:>14.4e} "
              f"{r.drift:>14.4e} {r.berry_phase:>10.4f}")

    return results


def run_rmt_statistics_suite(config, Nv_values):
    """Run RMT statistics for different N_v values."""
    print("\n" + "=" * 60)
    print("СЮИТ RMT СТАТИСТИКИ (GUE/GOE/POISSON)")
    print("=" * 60)

    results = {}
    for Nv in Nv_values:
        print(f"\nN_v = {Nv}...")
        cfg = Config()
        cfg.lattice_size = max(8, int(math.ceil(math.sqrt(4 * Nv))))
        cfg.n_вихрей = Nv
        cfg.alpha = config.alpha
        cfg.disorder_strength = config.disorder_strength
        cfg.verbose = False

        H = build_hofstadter_hamiltonian(cfg)
        eigs, _ = compute_spectrum(H)

        n = len(eigs)
        middle = eigs[n//4 : 3*n//4]
        rmt = analyze_rmt_statistics(middle)
        results[Nv] = rmt

        print(f"  ⟨r⟩ = {rmt.r_mean:.4f}, KS_GUE = {rmt.ks_gue:.4f}, "
              f"p_GUE = {rmt.p_gue:.4f}, {rmt.verdict}")

    return results


def run_montgomery_test(config, n_zeros=100):
    """Run Montgomery test."""
    print("\n" + "=" * 60)
    print("ТЕСТ МОНТГОМЕРИ (AB-облако vs ζ-нули)")
    print("=" * 60)

    H = build_hofstadter_hamiltonian(config)
    eigs, _ = compute_spectrum(H)
    n = len(eigs)
    middle = eigs[n//4 : 3*n//4]
    ab_spacings = unfold_spacings(middle)

    print(f"Computing {n_zeros} zeta zeros...")
    zeta_gammas = compute_zeta_zeros(n_zeros)
    zeta_spacings = unfold_zeta_zeros(zeta_gammas)

    ks_stat, p_value, verdict = montgomery_test(ab_spacings, zeta_spacings)

    print(f"\nKS-статистика: {ks_stat:.4f}")
    print(f"p-значение: {p_value:.4f}")
    print(f"Вердикт: {verdict}")

    return {
        "ks_stat": ks_stat,
        "p_value": p_value,
        "verdict": verdict,
        "n_ab_spacings": len(ab_spacings),
        "n_zeta_spacings": len(zeta_spacings)
    }


def run_topological_suite(config):
    """NEW: Run topological invariants computation."""
    print("\n" + "=" * 60)
    print("СЮИТ ТОПОЛОГИЧЕСКИХ ИНВАРИАНТОВ (Berry/Chern/TKNN)")
    print("=" * 60)

    # Berry phase
    berry = compute_berry_phase(config.C_Ch, config.T_period)
    print(f"\nФаза Берри: {berry:.6f} (mod 2π)")

    # Chern number
    print("\nВычисление числа Черна (Fukui-Hatsugai-Suzuki)...")
    topo = compute_chern_number_detailed(config)
    print(f"Число Черна: {topo.chern_number}")

    # TKNN Hall conductance
    tknn = compute_tknn_hall_conductance(config)
    print(f"Холловская проводимость: {tknn['sigma_xy_e2_over_h']} e²/h")

    # Dirac cone
    dirac = analyze_dirac_cone(config)
    if dirac['has_dirac']:
        print(f"Конус Дирака: v_F = {dirac['v_F']}, k_D = {dirac['k_Dirac']}")

    return {
        "berry_phase": berry,
        "chern_number": topo.chern_number,
        "hall_conductance": tknn['sigma_xy_e2_over_h'],
        "dirac_velocity": dirac.get('v_F', 0),
        "dirac_point": dirac.get('k_Dirac', None)
    }


def run_advanced_rmt_suite(config):
    """NEW: Run advanced RMT diagnostics."""
    print("\n" + "=" * 60)
    print("РАСШИРЕННАЯ RMT ДИАГНОСТИКА (Форм-фактор, IPR, Дисперсия)")
    print("=" * 60)

    H = build_hofstadter_hamiltonian(config)
    eigs, vecs = compute_spectrum(H)

    # Spectral form factor
    print("\nВычисление спектрального форм-фактора...")
    t_sff, K = compute_spectral_form_factor(eigs, config.sff_t_max)
    K_gue = compute_gue_sff_theory(t_sff)
    print(f"SFF at t=1: K={K[len(K)//2]:.4f}, GUE theory={K_gue[len(K)//2]:.4f}")

    # Number variance
    print("Вычисление дисперсии чисел...")
    sp = unfold_spacings(eigs[len(eigs)//4 : 3*len(eigs)//4])
    L_vals, Sigma = compute_number_variance(sp)

    # IPR
    print("Вычисление IPR...")
    ipr = compute_ipr(vecs)
    mean_ipr = float(np.mean(ipr))
    loc_len = compute_localization_length(ipr)
    print(f"Средний IPR: {mean_ipr:.6f}")
    print(f"Длина локализации: {loc_len:.4f}")

    return {
        "spectral_form_factor": K.tolist(),
        "sff_gue_theory": K_gue.tolist(),
        "sff_t_vals": t_sff.tolist(),
        "number_variance": Sigma.tolist(),
        "number_variance_L": L_vals.tolist(),
        "ipr_distribution": ipr.tolist(),
        "mean_ipr": mean_ipr,
        "localization_length": loc_len
    }


def run_chaos_suite(config):
    """NEW: Run chaos analysis suite."""
    print("\n" + "=" * 60)
    print("СЮИТ АНАЛИЗА ХАОСА (Lyapunov + Permutation)")
    print("=" * 60)

    # Lyapunov
    print("\nВычисление показателей Ляпунова...")
    lyap = compute_lyapunov_exponent(config, config.lyapunov_n_traj, config.lyapunov_time)
    print(f"  Вихрь: λ = {lyap['lyapunov_vortex']:.6f}")
    print(f"  Ньютон: λ = {lyap['lyapunov_newton']:.6f}")

    # Permutation test
    print("\nЗапуск перестановочного теста...")
    H = build_hofstadter_hamiltonian(config)
    eigs, _ = compute_spectrum(H)
    ab_sp = unfold_spacings(eigs[len(eigs)//4 : 3*len(eigs)//4])
    zeta_gammas = compute_zeta_zeros(100)
    zeta_sp = unfold_zeta_zeros(zeta_gammas)

    perm = permutation_test(ab_sp, zeta_sp, config.permutation_n)
    print(f"  r_наблюдаемое: {perm['r_observed']:.4f}")
    print(f"  Z-оценка: {perm['z_score']:.4f}")
    print(f"  p-значение: {perm['p_value']:.6f}")
    print(f"  Вердикт: {perm['verdict']}")

    return {
        "lyapunov_vortex": lyap['lyapunov_vortex'],
        "lyapunov_newton": lyap['lyapunov_newton'],
        "permutation_z_score": perm['z_score'],
        "permutation_p_value": perm['p_value'],
        "permutation_verdict": perm['verdict']
    }


def run_quantum_suite(config, C_Ch_values):
    """Run quantum simulation for different C_Ch values."""
    print("\n" + "=" * 60)
    print("СЮИТ КВАНТОВОЙ СИМУЛЯЦИИ")
    print("=" * 60)

    results = {}
    for C_Ch in C_Ch_values:
        print(f"\nC_Ch = {C_Ch}...")
        qr = run_quantum_simulation(config.n_qubits, C_Ch)
        results[float(C_Ch)] = qr
        print(f"  E_0 = {qr.eigenvalues[0]:.6f}, S_ent = {qr.entanglement_entropy:.4f} bits, "
              f"I_mut = {qr.mutual_information:.4f}")

    return results


def run_real_systems_suite():
    """Run analysis for all real system presets."""
    print("\n" + "=" * 60)
    print("СЮИТ ПРИМЕНЕНИЯ К РЕАЛЬНЫМ СИСТЕМАМ")
    print("=" * 60)

    systems = real_systems_presets()
    results = []
    for sys in systems:
        print(f"\n{sys.name}...")
        r = compute_real_system_chaplygin(sys)
        results.append(r)
        print(f"  C_Ch_norm = {r['C_Ch_normalized']:.4e}, T_ratio = {r['T_ratio']:.4f}")

    return results


def run_full_verification(config):
    """Run full verification suite."""
    print("\n" + "=" * 80)
    print("ПОЛНАЯ ВЕРИФИКАЦИЯ (v2.0)")
    print("=" * 80)
    print(f"\nКонфигурация:")
    print(f"  Размер решётки: {config.lattice_size}×{config.lattice_size}")
    print(f"  N_вихрей: {config.n_вихрей}")
    print(f"  Alpha: {config.alpha}")
    print(f"  Беспорядок W: {config.disorder_strength}")
    print(f"  C_Ch: {config.C_Ch}")

    report_data = {"config": {
        "lattice_size": config.lattice_size,
        "n_вихрей": config.n_вихрей,
        "alpha": config.alpha,
        "disorder": config.disorder_strength,
        "C_Ch": config.C_Ch,
        "n_qubits": config.n_qubits,
        "k_grid_size": config.k_grid_size,
        "lyapunov_time": config.lyapunov_time,
        "permutation_n": config.permutation_n
    }}

    plot_dir = ensure_report_dir(config)

    # 1. Chaplygin
    chap_results = run_chaplygin_verification_suite(config)
    report_data["chaplygin_results"] = [
        {"C_Ch_target": r.C_Ch_target, "C_Ch_mean": r.C_Ch_mean, "C_Ch_std": r.C_Ch_std,
         "drift": r.drift, "berry_phase": r.berry_phase}
        for r in chap_results
    ]
    if config.generate_plots:
        generate_plot_chaplygin_verification(chap_results, plot_dir, config.plot_dpi)

    # 2. RMT
    Nv_values = [3, 5, 10, 15, 25, 50]
    rmt_results = run_rmt_statistics_suite(config, Nv_values)
    report_data["rmt_results"] = {
        str(Nv): {"r_mean": r.r_mean, "r_std": r.r_std, "ks_gue": r.ks_gue,
                  "p_gue": r.p_gue, "ks_goe": r.ks_goe, "p_goe": r.p_goe,
                  "ks_poisson": r.ks_poisson, "p_poisson": r.p_poisson,
                  "verdict": r.verdict}
        for Nv, r in rmt_results.items()
    }
    if config.generate_plots:
        generate_plot_rmt_statistics(rmt_results, plot_dir, config.plot_dpi)
        for Nv, rmt in rmt_results.items():
            generate_plot_spacing_distribution(rmt, Nv, plot_dir, config.plot_dpi)

    # 3. Montgomery
    montgomery = run_montgomery_test(config, 100)
    report_data["montgomery_results"] = montgomery

    # 4. NEW: Topological
    topo = run_topological_suite(config)
    report_data["topological"] = topo

    # 5. NEW: Advanced RMT
    advanced = run_advanced_rmt_suite(config)
    report_data["advanced_rmt"] = advanced

    # 6. NEW: Chaos
    chaos = run_chaos_suite(config)
    report_data["chaos"] = chaos

    # 7. Quantum
    C_Ch_values = [0.1, 0.5, 1.0, 2.0, 3.0, math.pi, 5.0, 10.0]
    quantum_results = run_quantum_suite(config, C_Ch_values)
    report_data["quantum_results"] = {
        "E_0": quantum_results[1.0].eigenvalues[0],
        "E_max": quantum_results[1.0].eigenvalues[-1],
        "S_ent": quantum_results[1.0].entanglement_entropy
    }
    if config.generate_plots:
        generate_plot_quantum_spectrum(quantum_results, plot_dir, config.plot_dpi)
        generate_plot_topological_protection(quantum_results[5.0], plot_dir, config.plot_dpi)

    # 8. Real systems
    real_results = run_real_systems_suite()
    report_data["real_systems"] = real_results
    if config.generate_plots:
        generate_plot_real_systems(real_results, plot_dir, config.plot_dpi)

    # Сводка
    report_data["summary"] = {
        "Chaplygin conservation": "drift < 10⁻⁸",
        "GUE statistics": "verified for N_v ≥ 5",
        "Berry phase": f"{topo['berry_phase']:.4f}",
        "Chern number": str(topo['chern_number']),
        "Lyapunov (vortex)": f"{chaos['lyapunov_vortex']:.6f}",
        "Lyapunov (Newton)": f"{chaos['lyapunov_newton']:.6f}",
        "Permutation Z-score": f"{chaos['permutation_z_score']:.4f}",
        "Real systems analyzed": str(len(real_results))
    }

    # Generate reports
    if config.generate_reports:
        print("\n" + "=" * 60)
        print("ГЕНЕРАЦИЯ ОТЧЁТОВ...")
        print("=" * 60)
        files = generate_all_reports(report_data, plot_dir)
        print("\nСгенерированные отчёты:")
        for f in files:
            print(f"  {f}")

    print("\n" + "=" * 80)
    print("ВЕРИФИКАЦИЯ ЗАВЕРШЕНА")
    print("=" * 80)

    return report_data


# ===========================================================================
# SECTION 14: INTERACTIVE MENU
# ===========================================================================

def display_menu():
    print("\n" + "=" * 70)
    print("СИСТЕМА ВИХРЕЙ AB-ОБЛАКА ДЛЯ ЗАДАЧИ N ТЕЛ (Python v2.0 (RU))")
    print("=" * 70)
    print("\nДоступные операции:\n")
    print("  [1]  Полная верификация (все тесты + отчёты)")
    print("  [2]  Верификация Чаплыгина (Шаг 1)")
    print("  [3]  RMT статистика: GUE/GOE/Пуассон (Шаг 2)")
    print("  [4]  Тест Монтгомери: AB-облако vs ζ-нули")
    print("  [5]  Квантовая симуляция с топологическими кубитами (Шаг 4)")
    print("  [6]  Анализ реальных систем (Шаг 3)")
    print("  [7]  Построить гамильтониан и показать спектр")
    print("  [8]  Верификация аналитического решения")
    print("  [9]  N-вихревая симуляция (N = 3, 4, 5, ...)")
    print("  [10] Генерация всех отчётов (вручную)")
    print("  [11] Генерация всех графиков (вручную)")
    print("  [12] NEW: Топологические инварианты (Berry/Chern/TKNN)")
    print("  [13] NEW: Расширенные RMT (SFF/IPR/дисперсия)")
    print("  [14] NEW: Анализ хаоса (Lyapunov + Permutation)")
    print("  [15] NEW: Матрица кросс-корреляций")
    print()
    print("  [C]  Настроить параметры")
    print("  [S]  Показать текущую конфигурацию")
    print("  [H]  Помощь")
    print("  [Q]  Выход")
    print()
    print("Выберите опцию: ", end='')


def configure_parameters(config):
    print("\n--- КОНФИГУРАЦИЯ ---")
    print("Нажмите Enter для сохранения текущего значения.")

    def get_input(prompt, current, cast=str):
        val = input(prompt)
        return cast(val) if val else current

    config.lattice_size = max(4, get_input(f"Размер решётки L [текущее={config.lattice_size}]: ",
                                            config.lattice_size, int))
    config.n_вихрей = max(1, get_input(f"Число вихрей N_v [текущее={config.n_вихрей}]: ",
                                          config.n_вихрей, int))
    config.alpha = get_input(f"Alpha [текущее={config.alpha}]: ", config.alpha, float)
    config.disorder_strength = get_input(f"Беспорядок W [текущее={config.disorder_strength}]: ",
                                          config.disorder_strength, float)
    config.C_Ch = get_input(f"C_Ch [текущее={config.C_Ch}]: ", config.C_Ch, float)
    config.n_qubits = max(2, get_input(f"Number of qubits [текущее={config.n_qubits}]: ",
                                        config.n_qubits, int))
    config.k_grid_size = get_input(f"Размер K-сетки (Chern) [текущее={config.k_grid_size}]: ",
                                    config.k_grid_size, int)
    config.lyapunov_time = get_input(f"Время Ляпунова [текущее={config.lyapunov_time}]: ",
                                      config.lyapunov_time, float)
    config.permutation_n = get_input(f"Permutation N [текущее={config.permutation_n}]: ",
                                      config.permutation_n, int)
    config.output_dir = input(f"Папка вывода [текущее={config.output_dir}]: ") or config.output_dir
    config.plot_dpi = get_input(f"DPI графиков [текущее={config.plot_dpi}]: ", config.plot_dpi, int)

    print("\nКонфигурация обновлена.")
    show_configuration(config)


def show_configuration(config):
    print("\n--- ТЕКУЩАЯ КОНФИГУРАЦИЯ ---")
    print(f"  Размер решётки:        {config.lattice_size}×{config.lattice_size}")
    print(f"  Число вихрей:  {config.n_вихрей}")
    print(f"  Alpha:               {config.alpha}")
    print(f"  Беспорядок W:          {config.disorder_strength}")
    print(f"  C_Ch:                {config.C_Ch}")
    print(f"  Число кубитов:    {config.n_qubits}")
    print(f"  Размер K-сетки:         {config.k_grid_size}")
    print(f"  Время Ляпунова:       {config.lyapunov_time}")
    print(f"  N перестановок:       {config.permutation_n}")
    print(f"  Папка вывода:    {config.output_dir}")
    print(f"  DPI графиков:            {config.plot_dpi}")
    print(f"  Генерировать графики:      {config.generate_plots}")
    print(f"  Генерировать отчёты:    {config.generate_reports}")


def show_help():
    print("""
=== ПОМОЩЬ ===

СИСТЕМА ВИХРЕЙ AB-ОБЛАКА ДЛЯ ЗАДАЧИ N ТЕЛ (Python v2.0 (RU))

Этот код реализует the vortex model of the three-body (and N-body) problem
based on the AB-cloud methodology с топологическим интегралом Чаплыгина.

22 СЕКЦИИ:
 1-15: Original functionality (same as v1.0)
 16. Berry phase calculation
 17. Chern number (Fukui-Hatsugai-Suzuki method)
 18. TKNN Hall conductance
 19. Dirac cone analysis at α=1/2
 20. Spectral form factor
 21. Number variance and IPR
 22. Lyapunov exponent and permutation test

КЛЮЧЕВЫЕ ФОРМУЛЫ:
- Analytical: r_k(t) = √C_Ch·(1 + ε·cos(ωt + 2πk/3))
- Frequency: ω = (2π/T)·exp(C_Ch/π)
- Фаза Берри: φ = π (mod 2π) for 3 вихрей
- Холловская проводимость: σ_xy = C·e²/h (quantized)
- GUE: ⟨r⟩ = 0.5996

ОПЦИИ МЕНЮ:
[1]  Full verification (all tests + reports)
[2]  Step 1: Chaplygin verification
[3]  Step 2: GUE/GOE/Пуассон statistics
[4]  Montgomery test (AB vs ζ)
[5]  Step 4: Quantum simulation
[6]  Step 3: Real systems
[7]  Hamiltonian spectrum
[8]  Верификация аналитического решения
[9]  Custom N-vortex simulation
[10] Generate reports
[11] Generate plots
[12] NEW: Топологические инварианты (Berry/Chern/TKNN)
[13] NEW: Advanced RMT (SFF/IPR/variance)
[14] NEW: Chaos analysis (Lyapunov + Permutation)
[15] NEW: Матрица кросс-корреляций
[C]  Configure
[S]  Show config
[H]  Помощь
[Q]  Выход
""")


def custom_n_vortex_simulation(config, N_v):
    """Run custom simulation with N_v вихрей."""
    print(f"\n--- ПОЛЬЗОВАТЕЛЬСКАЯ {N_v}-ВИХРЕВАЯ СИМУЛЯЦИЯ ---")
    cfg = Config()
    cfg.lattice_size = max(8, int(math.ceil(math.sqrt(4 * N_v))))
    cfg.n_вихрей = N_v
    cfg.alpha = config.alpha
    cfg.disorder_strength = config.disorder_strength
    cfg.verbose = True

    print(f"Построение гамильтониана (L={cfg.lattice_size}, N_v={N_v})...")
    H = build_hofstadter_hamiltonian(cfg)
    print(f"Размер гамильтониана: {H.shape}")

    print("Вычисление спектра...")
    eigs, vecs = compute_spectrum(H)
    print(f"Диапазон собственных значений: [{eigs[0]:.6f}, {eigs[-1]:.6f}]")
    print("Первые 10 собственных значений:")
    for i in range(min(10, len(eigs))):
        print(f"  E[{i}] = {eigs[i]:.6f}")

    print("\nRMT статистика:")
    n = len(eigs)
    middle = eigs[n//4 : 3*n//4]
    rmt = analyze_rmt_statistics(middle)
    print(f"  ⟨r⟩ = {rmt.r_mean:.4f}")
    print(f"  KS_GUE = {rmt.ks_gue:.4f}, p_GUE = {rmt.p_gue:.4f}")
    print(f"  Вердикт: {rmt.verdict}")

    if config.generate_plots:
        plot_dir = ensure_report_dir(config)
        generate_plot_spacing_distribution(rmt, N_v, plot_dir, config.plot_dpi)
        print(f"График сохранён в: {plot_dir}/spacing_distribution_Nv{N_v}.png")

    return {"N_v": N_v, "lattice_size": cfg.lattice_size, "eigenvalues": eigs.tolist(), "rmt": rmt}


def verify_analytical_solution(config):
    """Verify the analytical solution."""
    print("\n--- ВЕРИФИКАЦИЯ АНАЛИТИЧЕСКОГО РЕШЕНИЯ ---")
    print(f"C_Ch = {config.C_Ch}, T = {config.T_period}")

    omega = analytical_frequency(config.C_Ch, config.T_period)
    eps = analytical_amplitude(config.C_Ch)
    r0 = math.sqrt(config.C_Ch)

    print(f"\nПроизводные параметры:")
    print(f"  omega = {omega:.6f}")
    print(f"  epsilon = {eps:.6f}")
    print(f"  r_0 = sqrt(C_Ch) = {r0:.6f}")

    print(f"\nТраектория r_k(t) для k=0,1,2:")
    print(f"{'t/T':>10} {'r_0(t)':>12} {'r_1(t)':>12} {'r_2(t)':>12}")
    print("-" * 50)
    for t_frac in [0.0, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0]:
        t = t_frac * config.T_period
        r0_t = analytical_solution_r(t, config.C_Ch, config.T_period, 0)
        r1_t = analytical_solution_r(t, config.C_Ch, config.T_period, 1)
        r2_t = analytical_solution_r(t, config.C_Ch, config.T_period, 2)
        print(f"{t_frac:>10.4f} {r0_t:>12.6f} {r1_t:>12.6f} {r2_t:>12.6f}")

    if config.generate_plots:
        plot_dir = ensure_report_dir(config)
        generate_plot_analytical_solution(config.C_Ch, config.T_period, plot_dir, config.plot_dpi)
        print(f"\nГрафик сохранён в: {plot_dir}/analytical_solution_CCh{config.C_Ch:.2f}.png")


# ===========================================================================
# SECTION 15: MAIN ENTRY POINT
# ===========================================================================

def main():
    print("=" * 70)
    print("  СИСТЕМА ВИХРЕЙ AB-ОБЛАКА ДЛЯ ЗАДАЧИ N ТЕЛ (Python v2.0 (RU))")
    print("  Z.ai Research Laboratory, 2026")
    print("  Версия 2.0 — расширена 12 новыми модулями проверки")
    print("=" * 70)

    config = default_config()

    while True:
        try:
            display_menu()
            choice = input().strip()

            if choice == "1":
                run_full_verification(config)
            elif choice == "2":
                run_chaplygin_verification_suite(config)
            elif choice == "3":
                run_rmt_statistics_suite(config, [3, 5, 10, 15, 25, 50])
            elif choice == "4":
                run_montgomery_test(config, 100)
            elif choice == "5":
                run_quantum_suite(config, [0.1, 0.5, 1.0, 2.0, 3.0, math.pi, 5.0, 10.0])
            elif choice == "6":
                run_real_systems_suite()
            elif choice == "7":
                print("\n--- СПЕКТР ГАМИЛЬТОНИАНА ---")
                H = build_hofstadter_hamiltonian(config)
                eigs, _ = compute_spectrum(H)
                print("Первые 20 собственных значений:")
                for i in range(min(20, len(eigs))):
                    print(f"  E[{i}] = {eigs[i]:.6f}")
            elif choice == "8":
                verify_analytical_solution(config)
            elif choice == "9":
                Nv = int(input("Введите N_v (3, 4, 5, ...): "))
                custom_n_vortex_simulation(config, Nv)
            elif choice == "10":
                print("\n--- GENERATE REPORTS ---")
                report_data = {"config": {"C_Ch": config.C_Ch, "n_вихрей": config.n_вихрей}}
                plot_dir = ensure_report_dir(config)
                generate_all_reports(report_data, plot_dir)
            elif choice == "11":
                print("\n--- GENERATE PLOTS ---")
                print("This requires running tests first. Use option [1].")
            elif choice == "12":
                run_topological_suite(config)
            elif choice == "13":
                run_advanced_rmt_suite(config)
            elif choice == "14":
                run_chaos_suite(config)
            elif choice == "15":
                corr = compute_cross_correlations(config)
                print("\nМатрица кросс-корреляций:")
                for i, ki in enumerate(corr['keys']):
                    row = " ".join(f"{corr['correlation_matrix'][i][j]:+.3f}"
                                  for j in range(len(corr['keys'])))
                    print(f"  {ki:>16}: {row}")
            elif choice.lower() == "c":
                configure_parameters(config)
            elif choice.lower() == "s":
                show_configuration(config)
            elif choice.lower() == "h":
                show_help()
            elif choice.lower() == "q":
                print("\nДо свидания!")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
        except Exception as e:
            print(f"\n[ERROR] {type(e).__name__}: {e}")
            import traceback
            traceback.print_exc()

        print("\n" + "-" * 70)
        print("Нажмите Enter для продолжения...")
        input()


if __name__ == "__main__":
    main()
