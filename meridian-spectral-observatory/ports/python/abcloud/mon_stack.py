# -*- coding: utf-8 -*-
"""abcloud.mon_stack — Python port of the AB_Cloud_Monumental_v6_3.jl gallery.

1:1 port of the golden-anchored surface of ``AB_Cloud_Monumental_v6_3.jl``:
spectral statistics, multifractal/entanglement observables, the topology
suite (Fukui-Hatsugai Chern, Bott, Z2, winding, index theorem, eta, 4D C2),
the zeta mini-lab, number theory and verification tasks v01/v05/v50/v100.

Faithful-quirk notes (bug-for-bug with the Julia original):
  * ``_rational_alpha`` uses the Float64 method (L2148): the exact binary
    rational of the float almost always has denominator > 50, so the
    Euclidean loop ``for qq in 1:50`` decides (e.g. 1/3 -> (1,2), 2/3 -> (1,1),
    1/pi -> (1,2)).  All vortex counts and Bloch lattice sizes follow from it.
  * ``build_ab_cloud_hamiltonian`` is 0-based, torus-wrapped (mod L) in BOTH
    directions, x-major site order (site = x*L + y), and consumes one
    rand() per site for the disorder eps (even at sigma=0).
  * Julia ``eigen(Hermitian(H))`` -> numpy.linalg.eigh (LAPACK both sides);
    eigenvector-dependent observables are gauge-covariant, so they match to
    ~1e-12 across the libm/LAPACK boundary.
"""

import math
from fractions import Fraction
from math import gcd, log, sqrt, atan2, pi, cos, sin, exp, isnan, isinf, ceil

import numpy as np

from .mt19937 import MT19937

PI = math.pi

R_GUE = 0.5996
R_POISSON = 0.3863

# CONFIG defaults (AB_Cloud_Monumental_v6_3.jl L100-210)
CONFIG = {
    "L_default": 56, "L_small": 56, "L_medium": 56, "L_large": 56,
    "alpha_default": 0.5, "W_default": 2.0, "sigma_default": 0.5,
    "seed_default": 0,
    "n_realizations": 2, "central_window": 0.3,
    "chern_n_k": 80, "chiral_n_k": 6000,
    "chern_alphas_extended": [1 / 3, 0.5, 2 / 3, 3 / 5, 1 / 4, 3 / 4,
                              0.75, 0.9, 0.137, 0.127, 0.89, 0.13, 0.013],
    "hofstadter_test_alphas": [1 / 3, 1 / 2, 2 / 5, 3 / 7, 1 / 4, 2 / 3],
}


def rational_alpha(alpha):
    """Julia _rational_alpha(::Float64) — exact binary rational, then the
    Euclidean fallback loop when the denominator exceeds 50."""
    f = Fraction(alpha)
    p, q = f.numerator, f.denominator
    if q > 50:
        for qq in range(1, 51):
            pp = round(alpha * qq)
            if pp > 0 and gcd(pp, qq) == 1:
                return pp, qq
    return p, q


class VortexConfig(object):
    def __init__(self, positions, charges):
        self.positions = [(float(x), float(y)) for x, y in positions]
        self.charges = list(charges)

    @property
    def n_vortices(self):
        return len(self.charges)

    @property
    def net_charge(self):
        return sum(self.charges)


def default_vortex_config(L, alpha, seed=0):
    p, q = rational_alpha(alpha)
    n_pos = q // 2 + (q % 2)
    n_neg = q // 2
    charges = [+1] * n_pos + [-1] * n_neg
    n_total = n_pos + n_neg
    side = int(ceil(sqrt(max(n_total, 1))))
    positions = []
    for k in range(1, n_total + 1):
        i = (k - 1) % side
        j = (k - 1) // side
        positions.append(((i + 0.5) * L / side, (j + 0.5) * L / side))
    return VortexConfig(positions, charges)


def build_ab_cloud_hamiltonian(L, alpha, W=2.0, sigma=0.5, seed=0,
                               vortex_config=None, t=1.0):
    """0-based torus builder, x-major site order, per-site rand consumption."""
    N = L * L
    rng = MT19937(seed)
    if vortex_config is None:
        vortex_config = default_vortex_config(L, alpha, seed=seed)
    H = np.zeros((N, N), dtype=complex)
    # x-direction hops with Peierls phase 2*pi*alpha*y
    for x in range(L):
        for y in range(L):
            i = x % L * L + y % L
            j = (x + 1) % L * L + y % L
            phase_x = 2.0 * pi * alpha * y
            H[i, j] -= t * complex(math.cos(phase_x), math.sin(phase_x))
            H[j, i] -= t * complex(math.cos(-phase_x), math.sin(-phase_x))
    # y-direction hops with vortex phase
    for x in range(L):
        for y in range(L):
            i = x % L * L + y % L
            j = x % L * L + (y + 1) % L
            phase_y = 0.0
            for k, (vx, vy) in enumerate(vortex_config.positions):
                qk = vortex_config.charges[k]
                dx1, dy1 = x - vx, y - vy
                dx2, dy2 = x - vx, y + 1 - vy
                arg1 = atan2(dy1, dx1) if (dx1 != 0 or dy1 != 0) else 0.0
                arg2 = atan2(dy2, dx2) if (dx2 != 0 or dy2 != 0) else 0.0
                phase_y += qk * (arg2 - arg1) * 0.5
            H[i, j] -= t * complex(math.cos(phase_y), math.sin(phase_y))
            H[j, i] -= t * complex(math.cos(-phase_y), math.sin(-phase_y))
    # On-site: vortex Coulomb + disorder (one rand() per site, always)
    for i in range(N):
        xi = i // L
        yi = i % L
        V_i = 0.0
        for k, (vx, vy) in enumerate(vortex_config.positions):
            qk = vortex_config.charges[k]
            r2 = (xi - vx) ** 2 + (yi - vy) ** 2
            V_i += qk * W / (r2 / N + 1.0)
        eps_i = (rng.random() - 0.5) * 2 * sigma
        H[i, i] += V_i + eps_i
    return H


def build_pure_hofstadter(L, alpha, t=1.0):
    N = L * L
    H = np.zeros((N, N), dtype=complex)
    for x in range(L):
        for y in range(L):
            i = x % L * L + y % L
            j = (x + 1) % L * L + y % L
            phase_x = 2.0 * pi * alpha * y
            H[i, j] -= t * complex(math.cos(phase_x), math.sin(phase_x))
            H[j, i] -= t * complex(math.cos(-phase_x), math.sin(-phase_x))
            j = x % L * L + (y + 1) % L
            H[i, j] -= t
            H[j, i] -= t
    return H


# ── spectral statistics ─────────────────────────────────────────────────────

def spacing_ratios(eigs):
    s = sorted(eigs)
    d = [s[i + 1] - s[i] for i in range(len(s) - 1)]
    if len(d) < 2:
        return []
    return [min(d[i], d[i + 1]) / max(d[i], d[i + 1]) for i in range(len(d) - 1)]


def mean_spacing_ratio(eigs):
    r = spacing_ratios(eigs)
    return sum(r) / len(r) if r else float("nan")


def polynomial_unfold(eigs, deg=4):
    n = np.arange(1.0, len(eigs) + 1)
    A = np.column_stack([np.asarray(eigs, dtype=float) ** k for k in range(deg + 1)])
    coeffs, _, _, _ = np.linalg.lstsq(A, n, rcond=None)
    e = np.asarray(eigs, dtype=float)
    xi = np.zeros_like(e)
    for k in range(deg + 1):
        xi += coeffs[k] * e ** k
    return xi - xi[0]


def number_variance_mon(eigs, Ls):
    xi = np.sort(np.asarray(polynomial_unfold(eigs)))
    n = len(xi)
    out = []
    if n < 4:
        return [float("nan")] * len(Ls)
    xi_min, xi_max = xi[0], xi[-1]
    span = xi_max - xi_min
    for L in Ls:
        if not math.isfinite(L) or L <= 0 or L > span / 2:
            out.append(float("nan"))
            continue
        starts = xi[xi <= xi_max - L]
        if len(starts) < 2:
            out.append(float("nan"))
            continue
        counts = np.array([np.sum((xi >= x) & (xi < x + L)) for x in starts],
                          dtype=float)
        if len(counts) == 0 or np.all(counts == 0):
            out.append(float("nan"))
            continue
        mu = counts.mean()
        out.append(float(counts.var(ddof=1)))
    return out


def spectral_form_factor_mon(eigs, ts):
    xi = np.asarray(polynomial_unfold(eigs))
    K = []
    for t in ts:
        ph = np.exp(1j * t * xi)
        K.append(float(abs(np.sum(ph)) ** 2 / len(xi)))
    return K


def f_GUE_score(eigs):
    r = spacing_ratios(eigs)
    if not r:
        return float("nan")
    emp = sum(r) / len(r)
    return 1.0 - 2.0 * max(abs(emp - R_GUE), abs(emp - R_POISSON))


def chirality_index(eigs):
    e = sorted(eigs)
    n = len(e)
    # Julia: pairs = [(e[i], e[n+1-i]) for i in 1:(n div 2)]  (1-based)
    pairs = [(e[i - 1], e[n - i]) for i in range(1, n // 2 + 1)]
    chi = sum((a + b) / 2 for a, b in pairs) / len(pairs)
    sums = [a + b for a, b in pairs]
    m = sum(sums) / len(sums)
    spread = math.sqrt(sum((v - m) ** 2 for v in sums) / (len(sums) - 1)) \
        if len(sums) > 1 else 0.0
    return {"chirality_index": chi, "spread": spread, "n_pairs": len(pairs)}


# ── eigen-helpers (numpy eigh == Julia LAPACK within ~1e-12) ────────────────

def _eigh(H):
    ev, V = np.linalg.eigh(H)
    return ev, V


def _central_idx(eigs, n_states):
    e_centered = eigs - np.mean(eigs)
    order = sorted(range(len(eigs)), key=lambda i: abs(e_centered[i]))
    return order[:n_states]


# ── multifractal / entanglement ─────────────────────────────────────────────

def multifractal_spectrum(L, alpha, W, sigma, seed=0, n_states=3,
                          qs=None):
    if qs is None:
        qs = [float(q) for q in range(-16, 17)]
    H = build_ab_cloud_hamiltonian(L, alpha, W=W, sigma=sigma, seed=seed)
    eigs, vecs = _eigh(H)
    e_centered = eigs - np.mean(eigs)
    central_idx = _central_idx(eigs, n_states)
    N = L * L
    box_sizes = sorted(set([b for b in [1, 2, 4, 8, 16, 32, L // 4, L // 2, L]
                            if 1 <= b <= L]))
    qs = [float(q) for q in qs]
    Dq = []
    for q in qs:
        tau_q_vals = []
        for k in central_idx:
            psi2 = np.abs(vecs[:, k]) ** 2
            grid = np.asarray(psi2).reshape(L, L).T   # Julia column-major
            grid = grid / grid.sum()
            log_boxes = []
            log_sizes = []
            for b in box_sizes:
                nb = L // b
                if nb < 1:
                    continue
                P = np.zeros((nb, nb))
                for ix in range(nb):
                    for iy in range(nb):
                        P[ix, iy] = grid[ix * b:(ix + 1) * b,
                                         iy * b:(iy + 1) * b].sum()
                P = P[P > 1e-15]
                if P.size == 0:
                    continue
                if abs(q - 1.0) < 1e-10:
                    log_boxes.append(-float(np.sum(P * np.log(P))))
                else:
                    log_boxes.append(float(np.log(np.sum(P ** q)) / (q - 1)))
                log_sizes.append(log(1.0 / b))
            if len(log_boxes) >= 2:
                slope = (log_boxes[-1] - log_boxes[0]) / \
                        (log_sizes[-1] - log_sizes[0])
                tau_q_vals.append(slope)
        Dq.append(sum(tau_q_vals) / len(tau_q_vals) if tau_q_vals
                  else float("nan"))
    D0 = Dq[qs.index(0.0)] if 0.0 in qs else float("nan")
    D1 = Dq[qs.index(1.0)] if 1.0 in qs else float("nan")
    D2 = Dq[qs.index(2.0)] if 2.0 in qs else float("nan")
    return {"qs": qs, "Dq": Dq, "D0": D0, "D1": D1, "D2": D2,
            "monograph_prediction": "D_q -> 2 (extended) at alpha=1/2"}


def von_neumann_entropy(psi, L, subsystem_fraction=0.5):
    N = L * L
    assert len(psi) == N
    L_A = max(1, min(L - 1, round(L * subsystem_fraction)))
    n_A = L * L_A
    psi = np.asarray(psi)
    # Julia: psi_mat = reshape(psi, L, L) (column-major); rows 1:L_A, all cols,
    # flattened column-major -> element order (y-major, then x)
    psi_A = np.array([psi[y * L + x] for y in range(L) for x in range(L_A)])
    C_A = np.outer(psi_A, psi_A.conj())
    eigs = np.linalg.eigvalsh(C_A)
    eigs = np.clip(eigs, 1e-12, 1.0 - 1e-12)
    return float(-np.sum(eigs * np.log(eigs) +
                         (1 - eigs) * np.log(1 - eigs)))


def topological_entanglement_entropy(L, alpha, W, sigma, seed=0,
                                     n_states=3, subsystem_fractions=None):
    if subsystem_fractions is None:
        subsystem_fractions = [0.25, 0.35, 0.5, 0.65, 0.75, 0.76, 0.77, 0.78,
                               0.79, 0.8, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86,
                               0.87, 0.88, 0.89, 0.9, 0.91, 0.92, 0.93, 0.94,
                               0.95, 0.96, 0.97, 0.98, 0.99, 1, 2, 3, 4, 5, 6,
                               7, 8, 9, 10, 12, 14, 16, 18, 20, 24, 28, 32,
                               36, 40, 44, 48, 56, 64]
    H = build_ab_cloud_hamiltonian(L, alpha, W=W, sigma=sigma, seed=seed)
    eigs, vecs = _eigh(H)
    e_centered = eigs - np.mean(eigs)
    central_idx = _central_idx(eigs, n_states)
    S_mean = []
    S_std = []
    for frac in subsystem_fractions:
        vals = [von_neumann_entropy(vecs[:, k], L, frac) for k in central_idx]
        S_mean.append(sum(vals) / len(vals))
        S_std.append(float(np.std(vals, ddof=1)) if len(vals) > 1 else 0.0)
    boundaries = [L * f for f in subsystem_fractions]
    slope = 0.0
    gamma_top = 0.0
    if len(boundaries) >= 2:
        X = np.column_stack([boundaries, np.ones(len(boundaries))])
        coef, _, _, _ = np.linalg.lstsq(X, np.array(S_mean), rcond=None)
        slope = float(coef[0])
        gamma_top = -float(coef[1])
    return {"subsystem_fractions": list(subsystem_fractions),
            "S_mean": S_mean, "S_std": S_std,
            "boundary_lengths": boundaries,
            "slope_alpha": slope, "gamma_top": gamma_top,
            "monograph_prediction": "gamma_top = log(sqrt(N_vortices)) for AB anyons"}


def ipr_scaling(L_grid=(14, 28, 42, 56, 70, 84), alpha=0.5, W=2.0,
                sigma=0.5, n_states=3):
    Ns = [int(L * L) for L in L_grid]
    IPR = []
    for L in L_grid:
        H = build_ab_cloud_hamiltonian(L, alpha, W=W, sigma=sigma, seed=0)
        eigs, vecs = _eigh(H)
        e_centered = eigs - np.mean(eigs)
        central_idx = _central_idx(eigs, n_states)
        vals = [float(np.sum(np.abs(vecs[:, k]) ** 4)) for k in central_idx]
        IPR.append(sum(vals) / len(vals))
    logN = np.log(np.array(Ns, dtype=float))
    logIPR = np.log(np.array(IPR))
    if len(Ns) >= 2:
        X = np.column_stack([logN, np.ones(len(Ns))])
        slope = float(np.linalg.lstsq(X, logIPR, rcond=None)[0][0])
    else:
        slope = 0.0
    D2 = -2.0 * slope
    return {"L": list(L_grid), "N": Ns, "IPR": IPR, "D2": D2,
            "monograph_prediction": "D_2 -> 2 (extended) at alpha=1/2"}


def lyapunov_exponent(L, alpha, W, sigma, seed=0, n_states=3):
    H = build_ab_cloud_hamiltonian(L, alpha, W=W, sigma=sigma, seed=seed)
    eigs, vecs = _eigh(H)
    e_centered = eigs - np.mean(eigs)
    central_idx = _central_idx(eigs, n_states)
    ipr_vals = [float(np.sum(np.abs(vecs[:, k]) ** 4)) for k in central_idx]
    gamma = [-log(v) / L for v in ipr_vals]
    g_mean = sum(gamma) / len(gamma)
    g_std = float(np.std(gamma, ddof=1)) if len(gamma) > 1 else 0.0
    return {"gamma_mean": g_mean, "gamma_std": g_std, "L": L, "alpha": alpha,
            "W": W,
            "monograph_prediction": "gamma -> 0 (extended) at alpha=1/2"}


# ── Bloch / topology suite ──────────────────────────────────────────────────

def bloch_hofstadter(q, alpha, kx, ky, t=1.0):
    p, qq = rational_alpha(alpha)
    if qq != q:
        q = qq
    kx_f = float(kx)
    ky_f = float(ky)
    H = np.zeros((q, q), dtype=complex)
    for n in range(1, q + 1):
        H[n - 1, n - 1] = 2.0 * t * math.cos(2.0 * pi * alpha * (n - 1) + kx_f)
        if n < q:
            H[n - 1, n] = -t
            H[n, n - 1] = -t
    # magnetic unit cell boundary
    H[0, q - 1] = -t * np.exp(1j * q * ky_f)
    H[q - 1, 0] = -t * np.exp(-1j * q * ky_f)
    return H


def _link(u1, u2):
    ip = np.vdot(u1, u2)   # conj(u1) . u2, like Julia dot
    if abs(ip) > 1e-15:
        return ip / abs(ip)
    return complex(1.0, 0.0)


def first_chern_number(alpha, band_index=0, n_k=40):
    p, q = rational_alpha(alpha)
    kx = np.linspace(-pi / q, pi / q, n_k)
    ky = np.linspace(-pi, pi, n_k)
    if abs(kx[-1] - kx[0] - 2 * pi / q) < 1e-10:
        kx = kx[:-1]
    if abs(ky[-1] - ky[0] - 2 * pi) < 1e-10:
        ky = ky[:-1]
    nx, ny = len(kx), len(ky)
    berry_sum = 0.0
    for i in range(nx):
        ip = (i + 1) % nx
        for j in range(ny):
            jp = (j + 1) % ny
            Us = []
            for (ii, jj) in ((i, j), (ip, j), (ip, jp), (i, jp)):
                Hk = bloch_hofstadter(q, alpha, kx[ii], ky[jj])
                _, V = _eigh(Hk)
                Us.append(V[:, band_index])
            U1 = _link(Us[0], Us[1])
            U2 = _link(Us[1], Us[2])
            U3 = _link(Us[2], Us[3])
            U4 = _link(Us[3], Us[0])
            F_val = float(np.imag(np.log(U1 * U2 * U3 * U4 + 0j)))
            berry_sum += F_val
    nu = int(round(berry_sum / (2.0 * pi)))
    # Diophantine check
    s = pow(p, -1, q) if q > 1 else 0
    nu_dioph = (p * s * (band_index + 1)) % q
    nu_dioph_signed = (nu_dioph if nu_dioph <= q // 2 else nu_dioph - q) \
        if p > 0 else (-nu_dioph if nu_dioph <= q // 2 else q - nu_dioph)
    expected = 1 if (alpha == 0.5 and band_index == 0) else None
    if alpha == 0.5 and band_index == 0 and nu == 0:
        confirms = True
        gap_status = "closed (Dirac cone at alpha=1/2)"
    elif expected is not None:
        confirms = (nu == expected)
        gap_status = "open" if confirms else "ambiguous"
    else:
        confirms = True
        gap_status = "open"
    return {"nu": nu, "alpha": alpha, "p": p, "q": q,
            "diophantine_s": s,
            "nu_diophantine_prediction": nu_dioph_signed,
            "band_index": band_index, "n_k": n_k,
            "confirms_monograph": confirms, "gap_status": gap_status,
            "expected_at_alpha_half_band0": expected}


def vortex_winding_sum_rule(L, alpha, seed=0,
                            custom_n_vortices=(2, 4, 6, 8, 12, 16, 20, 24,
                                               28, 32, 36, 40, 44, 48)):
    p, q = rational_alpha(alpha)
    configs = []
    for n_total in custom_n_vortices:
        n_pos = n_total // 2 + (n_total % 2)
        n_neg = n_total // 2
        charges = [+1] * n_pos + [-1] * n_neg
        side = int(ceil(sqrt(max(n_total, 1))))
        positions = [((float((k - 1) % side + 0.5)) * L / side,
                      (float((k - 1) // side + 0.5)) * L / side)
                     for k in range(1, n_total + 1)]
        theta_grid = np.linspace(0, 2 * pi, 64)
        windings = []
        for (vx, vy) in positions:
            phases = []
            for th in theta_grid:
                x = vx + 1.5 * math.cos(th)
                y = vy + 1.5 * math.sin(th)
                phase = 0.0
                for ((vx2, vy2), qk2) in zip(positions, charges):
                    phase += qk2 * math.atan2(y - vy2, x - vx2)
                phases.append(phase)
            for k in range(1, len(phases)):
                while phases[k] - phases[k - 1] > pi:
                    phases[k] -= 2 * pi
                while phases[k] - phases[k - 1] < -pi:
                    phases[k] += 2 * pi
            windings.append(int(round((phases[-1] - phases[0]) / (2 * pi))))
        total_winding = sum(windings)
        total_charge = sum(charges)
        configs.append({"n_vortices": n_total, "n_positive": n_pos,
                        "n_negative": n_neg, "total_charge": total_charge,
                        "winding_per_vortex": windings,
                        "winding_sum": total_winding,
                        "matches_total_charge": total_winding == total_charge})
    monograph_pred = 1 if (q % 2 == 1 and p % 2 == 1) else 0
    confirms = all(c["matches_total_charge"] for c in configs) and \
        configs[0]["total_charge"] == monograph_pred
    return {"alpha": alpha, "p": p, "q": q, "configurations": configs,
            "monograph_prediction_total_charge": monograph_pred,
            "confirms_monograph": confirms}


def z2_invariant_kane_mele(L, alpha, W, sigma, seed=0):
    chern_res = first_chern_number(alpha, band_index=0, n_k=400)
    nu = chern_res["nu"]
    z2_from_chern = nu % 2
    p, q = rational_alpha(alpha)
    tr_points = [(0.0, 0.0), (pi / q, 0.0), (0.0, pi), (pi / q, pi)]
    n_occ_at_TR = [int(np.sum(np.linalg.eigvalsh(
        bloch_hofstadter(q, alpha, kx, ky)) < 0))
        for (kx, ky) in tr_points]
    z2_from_TR = sum(n_occ_at_TR) % 2
    return {"alpha": alpha,
            "z2_from_chern_parity": z2_from_chern,
            "z2_from_TR_Kramers": z2_from_TR,
            "chern_nu": nu,
            "n_occupied_at_TR_points": n_occ_at_TR,
            "tr_points": list(tr_points),
            "consistent": z2_from_chern == z2_from_TR,
            "is_topological": z2_from_chern == 1,
            "confirms_monograph": (alpha == 0.5 and z2_from_chern == 1)}


def bott_index(L, alpha, W, sigma, seed=0, target_band=0):
    H = build_ab_cloud_hamiltonian(L, alpha, W=W, sigma=sigma, seed=seed)
    eigs, vecs = _eigh(H)
    N = L * L
    p, q = rational_alpha(alpha)
    n_per_band = max(1, N // q)
    gap_idx = min((target_band + 1) * n_per_band, N)
    # Julia (1-based): E_fermi = (eigs[gap_idx-1] + eigs[gap_idx]) / 2
    # -> 0-based: elements gap_idx-2 and gap_idx-1
    E_fermi = (eigs[gap_idx - 2] + eigs[gap_idx - 1]) / 2 if gap_idx > 1 else eigs[0]
    P_mask = eigs < E_fermi
    n_occ = int(np.sum(P_mask))
    if n_occ == 0 or n_occ == N:
        return {"bott": 0, "n_occupied": n_occ, "E_fermi": float(E_fermi),
                "error": "no states to project onto"}
    Psi = vecs[:, P_mask]
    # x-major flat coordinates (site = x*L + y)
    X_flat = np.array([float(x) for x in range(L) for y in range(L)])
    Y_flat = np.array([float(y) for x in range(L) for y in range(L)])
    phase_x = np.exp(2j * pi * X_flat / L)
    phase_y = np.exp(2j * pi * Y_flat / L)
    U_proj = Psi.conj().T @ (phase_x[:, None] * Psi)
    V_proj = Psi.conj().T @ (phase_y[:, None] * Psi)
    W_mat = V_proj @ U_proj @ V_proj.conj().T @ U_proj.conj().T
    eigvals_W = np.linalg.eigvals(W_mat)
    log_phases = np.log(eigvals_W + 1e-30)
    bott = int(round(float(np.sum(np.imag(log_phases))) / (2 * pi)))
    expected = 1 if (alpha == 0.5 and target_band == 0 and W >= 1.5) else None
    confirms = True if expected is None else (bott == expected)
    return {"bott": bott, "n_occupied": n_occ, "E_fermi": float(E_fermi),
            "alpha": alpha, "L": L, "W": W, "sigma": sigma,
            "target_band": target_band,
            "expected_monograph": expected, "confirms_monograph": confirms}


def chiral_winding_number(alpha, n_k=60):
    if alpha != 0.5:
        return {"alpha": alpha, "winding": None,
                "note": "chiral symmetry only at alpha = 1/2",
                "confirms_monograph": False}
    theta_grid = np.linspace(0, 2 * pi, n_k)
    R = 0.3
    phases = []
    for th in theta_grid:
        kx = pi / 2 + R * math.cos(th)
        ky = R * math.sin(th)
        Hk = bloch_hofstadter(2, alpha, kx, ky)
        vals, V = _eigh(Hk)
        pos_idx = int(np.argmax(vals))
        neg_idx = int(np.argmin(vals))
        q_mat = np.vdot(V[:, neg_idx], Hk @ V[:, pos_idx])
        phases.append(float(np.angle(q_mat)))
    for k in range(1, len(phases)):
        while phases[k] - phases[k - 1] > pi:
            phases[k] -= 2 * pi
        while phases[k] - phases[k - 1] < -pi:
            phases[k] += 2 * pi
    dphi = [phases[k + 1] - phases[k] for k in range(len(phases) - 1)]
    dphi = [((d + pi) % (2 * pi)) - pi for d in dphi]
    winding = int(round(sum(dphi) / (2 * pi)))
    return {"alpha": alpha, "winding": winding,
            "winding_absolute": abs(winding), "n_k": n_k,
            "loop_radius_k": R, "dirac_point": (pi / 2, 0.0),
            "chiral_class": "AIII",
            "confirms_monograph": (alpha == 0.5 and abs(winding) == 1)}


def index_theorem_chiral(L, alpha, W, sigma, seed=0):
    H = build_ab_cloud_hamiltonian(L, alpha, W=W, sigma=sigma, seed=seed)
    eigs, vecs = _eigh(H)
    parity = [(x + y) % 2 for x in range(L) for y in range(L)]
    Gamma = np.diag(np.array([1 - 2 * p for p in parity], dtype=complex))
    E_max = float(np.max(np.abs(eigs)))
    epsilon = 0.02 * E_max
    zero_idx = [i for i in range(len(eigs)) if abs(eigs[i]) < epsilon]
    n_pos = 0
    n_neg = 0
    for k in zero_idx:
        psi = vecs[:, k]
        chi = float(np.real(np.vdot(psi, Gamma @ psi)))
        if chi > 0.5:
            n_pos += 1
        elif chi < -0.5:
            n_neg += 1
    idx_num = n_pos - n_neg
    cfg = default_vortex_config(L, alpha, seed=seed)
    idx_pred = cfg.net_charge
    expected = 1 if alpha == 0.5 else None
    confirms = True if expected is None else (idx_num == expected)
    return {"alpha": alpha, "L": L, "W": W, "sigma": sigma,
            "n_zero_modes": len(zero_idx),
            "n_positive_chirality": n_pos,
            "n_negative_chirality": n_neg,
            "idx_numerical": idx_num,
            "idx_predicted_vortex_charge": idx_pred,
            "expected_monograph": expected,
            "confirms_monograph": confirms, "epsilon": epsilon}


def eta_invariant(L, alpha, W, sigma, seed=0, epsilon=1e-6):
    H = build_ab_cloud_hamiltonian(L, alpha, W=W, sigma=sigma, seed=seed)
    eigs = np.linalg.eigvalsh(H)
    Lambda = (eigs[-1] - eigs[0]) / 4.0
    eta_reg = float(np.sum(np.sign(eigs) *
                           (1.0 - np.exp(-np.abs(eigs) / Lambda))))
    eta_norm = eta_reg / 2.0
    n_pos = int(np.sum(eigs > epsilon))
    n_neg = int(np.sum(eigs < -epsilon))
    n_zero = int(np.sum(np.abs(eigs) <= epsilon))
    return {"alpha": alpha, "L": L, "W": W, "sigma": sigma,
            "eta_regularized": eta_reg, "eta_normalized_by_2": eta_norm,
            "n_positive_eigenvalues": n_pos,
            "n_negative_eigenvalues": n_neg,
            "n_zero_eigenvalues": n_zero,
            "spectral_asymmetry_n_plus_minus_n_minus": n_pos - n_neg,
            "Lambda_cutoff": float(Lambda),
            "confirms_monograph": (alpha == 0.5 and n_pos > n_neg)}


def second_chern_class_4d(alpha, n_k=12):
    if alpha != 0.5:
        return {"alpha": alpha, "C_2": None,
                "note": "4D topological invariant computed only at alpha = 1/2",
                "confirms_monograph": False}
    sigmax = np.array([[0, 1], [1, 0]], dtype=complex)
    sigmay = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sigmaz = np.array([[1, 0], [0, -1]], dtype=complex)
    id2 = np.eye(2, dtype=complex)
    Gamma = [np.kron(sigmax, id2), np.kron(sigmay, id2),
             np.kron(sigmaz, sigmax), np.kron(sigmaz, sigmay),
             np.kron(sigmaz, sigmaz)]
    m = 1.0

    def d_vec(k1, k2, k3, k4):
        return [sin(k1), sin(k2), sin(k3), sin(k4),
                cos(k1) + cos(k2) + cos(k3) + cos(k4) - 4 + m]

    def H_4d(k1, k2, k3, k4):
        dv = d_vec(k1, k2, k3, k4)
        Hm = np.zeros((4, 4), dtype=complex)
        for a in range(5):
            Hm += dv[a] * Gamma[a]
        return Hm

    n_k_eff = min(n_k, 12)
    ks = np.linspace(-pi, pi, n_k_eff)
    dk = ks[1] - ks[0]
    dk_small = 0.15
    C2_sum = 0.0
    F12_max = 0.0
    offsets12 = [(0, 0, 0, 0), (dk_small, 0, 0, 0),
                 (dk_small, dk_small, 0, 0), (0, dk_small, 0, 0)]
    offsets34 = [(0, 0, 0, 0), (0, 0, dk_small, 0),
                 (0, 0, dk_small, dk_small), (0, 0, 0, dk_small)]
    for k1 in ks:
        for k2 in ks:
            for k3 in ks:
                for k4 in ks:
                    Us = []
                    for o in offsets12:
                        Hk = H_4d(k1 + o[0], k2 + o[1], k3 + o[2], k4 + o[3])
                        _, V = _eigh(Hk)
                        Us.append(V[:, 0])
                    F12 = float(np.imag(np.log(_link(Us[0], Us[1]) *
                                               _link(Us[1], Us[2]) *
                                               _link(Us[2], Us[3]) *
                                               _link(Us[3], Us[0]) + 0j)))
                    Us2 = []
                    for o in offsets34:
                        Hk = H_4d(k1 + o[0], k2 + o[1], k3 + o[2], k4 + o[3])
                        _, V = _eigh(Hk)
                        Us2.append(V[:, 0])
                    F34 = float(np.imag(np.log(_link(Us2[0], Us2[1]) *
                                               _link(Us2[1], Us2[2]) *
                                               _link(Us2[2], Us2[3]) *
                                               _link(Us2[3], Us2[0]) + 0j)))
                    F12_max = max(F12_max, abs(F12))
                    C2_sum += F12 * F34 * dk ** 4
    C2 = int(round(C2_sum / (8.0 * pi ** 2)))
    is_topo = 0 < m < 2
    has_curv = F12_max > 0.01
    return {"alpha": alpha, "C_2": C2,
            "C_2_diagnostic_max_curvature": F12_max,
            "is_topological_phase": is_topo,
            "has_nontrivial_curvature": has_curv,
            "n_k_per_dim": n_k_eff, "total_k_points": n_k_eff ** 4,
            "mass_term_m": m,
            "confirms_monograph": (alpha == 0.5 and is_topo and has_curv)}


def ab_phase_winding_per_vortex(L, alpha, R_loop=2.0, n_theta=128):
    cfg = default_vortex_config(L, alpha, seed=0)
    theta_grid = np.linspace(0, 2 * pi, n_theta)
    per_vortex = []
    for (vx, vy), qk in zip(cfg.positions, cfg.charges):
        phases = []
        for th in theta_grid:
            x = vx + R_loop * math.cos(th)
            y = vy + R_loop * math.sin(th)
            phase = 0.0
            for (vx2, vy2), qk2 in zip(cfg.positions, cfg.charges):
                phase += qk2 * math.atan2(y - vy2, x - vx2)
            phases.append(phase)
        for k in range(1, len(phases)):
            while phases[k] - phases[k - 1] > pi:
                phases[k] -= 2 * pi
            while phases[k] - phases[k - 1] < -pi:
                phases[k] += 2 * pi
        winding = int(round((phases[-1] - phases[0]) / (2 * pi)))
        per_vortex.append({"vortex_position": (vx, vy),
                           "vortex_charge_q_k": qk,
                           "numerical_winding": winding,
                           "matches_q_k": winding == qk,
                           "loop_radius_R": R_loop,
                           "n_theta_points": n_theta})
    total_winding = sum(p["numerical_winding"] for p in per_vortex)
    total_charge = sum(p["vortex_charge_q_k"] for p in per_vortex)
    all_match = all(p["matches_q_k"] for p in per_vortex)
    return {"alpha": alpha, "L": L, "n_vortices": len(per_vortex),
            "per_vortex_windings": per_vortex,
            "total_winding": total_winding,
            "total_vortex_charge": total_charge,
            "all_match_q_k": all_match,
            "confirms_monograph": (all_match and total_winding == total_charge)}


# ── zeta mini-lab ───────────────────────────────────────────────────────────

def riemann_von_mangoldt_N(T):
    if T <= 0:
        return 0.0
    return T / (2 * pi) * log(T / (2 * pi * math.e)) + 7 / 8


_ZETA_CACHE = {}


def zeta_zeros(n):
    """First n zeros — the _ZETA_ZEROS_1000 table (extracted provenance file)."""
    if "z" not in _ZETA_CACHE:
        here = os.path.dirname(os.path.abspath(__file__))
        path = os.path.normpath(os.path.join(
            here, "..", "..", "data", "monumental_zeta_zeros_1000.txt"))
        zs = []
        with open(path, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    zs.append(float(line))
        _ZETA_CACHE["z"] = zs
    zs = _ZETA_CACHE["z"]
    return zs[:min(n, len(zs))]


def unfold_zeta_zeros(zs):
    n = np.arange(1.0, len(zs) + 1)
    lz = np.log(np.asarray(zs, dtype=float))
    A = np.column_stack([np.ones(len(zs)), lz, lz ** 2])
    coeffs, _, _, _ = np.linalg.lstsq(A, n, rcond=None)
    return [float(coeffs[0] + coeffs[1] * math.log(z) +
                  coeffs[2] * math.log(z) ** 2) for z in zs]


def pair_correlation_zeta(zs, s_grid):
    xi = unfold_zeta_zeros(zs)
    d = [xi[i + 1] - xi[i] for i in range(len(xi) - 1)]
    R2 = []
    for s in s_grid:
        cnt = 0
        for j in range(len(d)):
            for k in range(len(d)):
                if j != k and abs((j - k) - s) < 0.5:
                    cnt += 1
        R2.append(cnt / len(d))
    return R2


def bogomolny_keating_sigma(N):
    return 0.27 / sqrt(N)


# ── parameter sweeps ────────────────────────────────────────────────────────

def _central_eigs(H, central_window=0.3):
    eigs = np.linalg.eigvalsh(H)
    e0 = np.quantile(eigs, 0.5 - central_window / 2)
    e1 = np.quantile(eigs, 0.5 + central_window / 2)
    return eigs[(eigs >= e0) & (eigs <= e1)]


def sweep_alpha(L=56, W=2.0, sigma=0.5, alpha_grid=None, n_realizations=2,
                use_vortices=True, central_window=0.3):
    if alpha_grid is None:
        alpha_grid = CONFIG["alpha_grid"]
    rs_mean = []
    rs_std = []
    fGUE = []
    for alpha in alpha_grid:
        r_vals = []
        for s in range(n_realizations):
            H = build_ab_cloud_hamiltonian(L, alpha, W=W, sigma=sigma, seed=s) \
                if use_vortices else build_pure_hofstadter(L, alpha)
            ce = _central_eigs(H, central_window)
            r = spacing_ratios(ce)
            if len(r) >= 5:
                r_vals.append(sum(r) / len(r))
        if r_vals:
            m = sum(r_vals) / len(r_vals)
            sd = (float(np.std(r_vals, ddof=1)) / sqrt(len(r_vals))
                  if len(r_vals) > 1 else 0.0)
        else:
            m, sd = 0.0, 0.0
        rs_mean.append(m)
        rs_std.append(sd)
        fGUE.append(1 - 2 * max(abs(m - R_GUE), abs(m - R_POISSON))
                    if r_vals else 0.0)
    return {"alpha": list(alpha_grid), "r_mean": rs_mean, "r_std": rs_std,
            "f_GUE": fGUE}


# ── number theory ───────────────────────────────────────────────────────────

def sieve_of_eratosthenes(n):
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False
    i = 2
    while i * i <= n:
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
        i += 1
    return [k for k in range(2, n + 1) if sieve[k]]


def prime_counting(n):
    if n < 0:
        return []
    pi_arr = [0] * (n + 1)
    if n < 2:
        return pi_arr
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False
    count = 0
    for k in range(1, n + 1):
        if sieve[k]:
            count += 1
            if k * k <= n:
                for j in range(k * k, n + 1, k):
                    sieve[j] = False
        pi_arr[k] = count
    return pi_arr


def mobius_function(n):
    if n < 1:
        return []
    mu = [1] * (n + 1)   # 1-based; index 0 unused
    mu[0] = 0
    for p in sieve_of_eratosthenes(n):
        for k in range(2 * p, n + 1, p):
            mu[k] = -mu[k]
        p2 = p * p
        if p2 <= n:
            for k in range(p2, n + 1, p2):
                mu[k] = 0
    return mu[1:]


def mobius_sum(n):
    if n < 1:
        return []
    mu = mobius_function(n)
    M = []
    s = 0
    for k in range(n):
        s += mu[k]
        M.append(s)
    return M


def prime_gaps(n):
    primes = sieve_of_eratosthenes(n)
    if len(primes) < 2:
        return [], primes
    return [primes[k + 1] - primes[k] for k in range(len(primes) - 1)], primes


# ── verification tasks (golden-anchored subset) ─────────────────────────────

def v01(L=56, alpha=0.5, W=2.0, sigma=0.5, seed=0):
    H = build_ab_cloud_hamiltonian(L, alpha, W=W, sigma=sigma, seed=seed)
    err = float(np.max(np.abs(H - H.conj().T)))
    return {"hermitian_error": err, "passes": err < 1e-10,
            "L": L, "alpha": alpha, "W": W, "sigma": sigma, "seed": seed}


def v05(L=56, alphas=None):
    if alphas is None:
        alphas = CONFIG["hofstadter_test_alphas"]
    results = []
    for alpha in alphas:
        cfg = default_vortex_config(L, alpha)
        p, q = rational_alpha(alpha)
        results.append({"alpha": alpha, "q": q,
                        "n_vortices": cfg.n_vortices,
                        "passes": cfg.n_vortices == q})
    return {"results": results,
            "all_pass": all(r["passes"] for r in results), "L": L}


def v50(L=56, alpha=2 / 5, seed=0):
    cfg = default_vortex_config(L, alpha, seed=seed)
    return {"positions": list(cfg.positions), "charges": list(cfg.charges),
            "n_vortices": cfg.n_vortices, "L": L, "alpha": alpha}


def v100(alphas=None, n_k=80, band_index=0):
    if alphas is None:
        alphas = CONFIG["chern_alphas_extended"]
    return {"multi_alpha_chern": [
                {"alpha": a,
                 "chern": first_chern_number(float(a), band_index=band_index,
                                             n_k=n_k)}
                for a in alphas],
            "alpha_half_band1": first_chern_number(0.5, band_index=1, n_k=n_k)}


import os  # noqa: E402  (used by zeta_zeros)
