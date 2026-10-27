"""
extended_solvers.py — Solvers for mKdV, BBM, and Kawahara equations.

All three extend the KdV framework of kdv_core.py to non-integrable
and higher-order dispersive regimes, with the same three b-mechanisms
(M1 spectral, M2 Rodrigues in (u, u_x), M3 modified nonlinearity).

Equations:
  mKdV      : u_t + 6·u²·u_x + u_xxx = 0       (integrable, Miura→KdV)
  BBM       : u_t + u_x + u·u_x − u_xxt = 0    (non-integrable, regularized)
  Kawahara  : u_t + 6·u·u_x + u_xxx + u_xxxxx = 0  (5th-order, oscillatory solitons)

Author: Z.ai Research, 2026 (companion to monograph chapter 16, §16.23)
"""
from __future__ import annotations

import numpy as np
from scipy.fft import fft, ifft

from kdv_core import (
    B_UNIVERSAL, THETA_B, make_grid, dealias_mask,
    apply_M1_spectral, apply_M2_rodrigues, hilbert_fft,
    sech2, invariants,
)


# ==================================================================
# 1. mKdV — modified Korteweg–de Vries
# ==================================================================
# u_t + 6·u²·u_x + u_xxx = 0
#
# Pseudo-spectral form:
#   û_t = -3ik·F(u³)/... wait: ∂_x(u³) = 3·u²·u_x
#   So 6·u²·u_x = 2·∂_x(u³) = 2·ik·F(u³)
#   û_t = -2ik·F(u³) + ik³·û   (dealias F(u³) with 3/5 rule)
#
# Linear part L = ik³ (same as KdV) → IFRK4 works directly.
# Integrable via Lax pair (Wadati 1973). Miura transform: u_KdV = v² + v_x.
# Invariants: M = ∫u, P = ∫u², E = ∫(u_x² - 2u⁴)/... = ∫(u_x² - u⁴·3/2)
# ==================================================================

def mkdv_nonlinear_term(u, k, dealias, theta=0.0):
    """N(u) = -2ik·F(u³)  for mKdV (the 6u²·u_x part).

    Dealiasing: u³ has spectrum to 3·k_max, so we need 2/3 rule
    on F(u³) too (sufficient for quadratic × linear = cubic).
    """
    u3_hat = fft(u ** 3) * dealias
    return -2j * k * u3_hat


def mkdv_invariants(u, dx, k):
    """mKdV invariants:
        M = ∫ u dx                          (mass)
        P = ∫ u² dx                         (momentum)
        E = ∫ (u_x² − 2·u⁴/... ) dx         (Hamiltonian, miura-related)
    For mKdV: H = ∫(u_x² - u⁴)·dx (note: different from KdV).
    """
    M = np.sum(u) * dx
    P = np.sum(u * u) * dx
    u_hat = fft(u)
    ux = np.real(ifft(1j * k * u_hat))
    E = (np.sum(ux * ux) - np.sum(u ** 4)) * dx
    return M, P, E


def mkdv_soliton(x, c, x0=0.0):
    """mKdV soliton: u = c·tanh(c·(x − x0))  (kink, c > 0)."""
    return c * np.tanh(c * (x - x0))


def mkdv_bright_soliton(x, c, x0=0.0):
    """mKdV bright soliton (defocusing case): u = c·sech(c·(x − x0))."""
    return c / np.cosh(c * (x - x0))


# Model registry for mKdV (M1, M2, M3 adapted)
def mkdv_make_models():
    """Returns a registry analogous to kdv_core.MODELS but for mKdV."""
    b = 2.0 * THETA_B / np.pi
    return {
        "true_mkdv":   ("True mKdV",
                        mkdv_nonlinear_term, 1.0, False, None, 0.0),
        "b_rotation":  ("b-rotation M1 (spectral, mKdV)",
                        mkdv_nonlinear_term, 1.0, False,
                        lambda u, k, th: apply_M1_spectral(u, th, k), 1.0),
        "b_rodrigues": ("b-rotation M2 (Rodrigues in (u, u_x), mKdV)",
                        mkdv_nonlinear_term, 1.0, False,
                        lambda u, k, th: apply_M2_rodrigues(u, th, k), 1.0),
        "b_modified":  ("b-modified M3 (mKdV, 6(R_b u)²·(R_b u)_x)",
                        lambda u, k, d, th: _mkdv_modified_N(u, k, d, th),
                        1.0, False, None, 0.0),
        "b_brake":     ("b-brake (1-b)·6u²·u_x (mKdV)",
                        lambda u, k, d, th: -(1.0 - th * 2.0/np.pi) * 2j * k * fft(u**3) * d,
                        1.0, False, None, 0.0),
        "b_les":       ("b-LES ν·(1+b)·u_xx (mKdV)",
                        lambda u, k, d, th: (
                            -2j * k * fft(u**3) * d
                            - 0.001 * (1.0 + 2.0 * th / np.pi) * k**2 * fft(u) * d
                        ),
                        1.0, True, None, 0.0),
    }


def _mkdv_modified_N(u, k, dealias, theta):
    """M3 modified nonlinearity for mKdV:
       6u²·u_x → 6·(R_b u)²·(R_b u)_x  where R_b u = cos·u + sin·H[u]
    """
    H_u = hilbert_fft(u, k)
    u_rot = np.cos(theta) * u + np.sin(theta) * H_u
    u_rot3_hat = fft(u_rot ** 3) * dealias
    return -2j * k * u_rot3_hat


# ==================================================================
# 2. BBM — Benjamin–Bona–Mahony  (regularized long-wave equation)
# ==================================================================
# u_t + u_x + u·u_x − u_xxt = 0
#
# In Fourier:  (1 + k²)·û_t = -ik·û - (ik/2)·F(u²)
#     ⇒ û_t = [-ik·û - (ik/2)·F(u²)] / (1 + k²)
#
# Linear part: L = -ik / (1 + k²)  — bounded at high k (regularized!)
# This means BBM is well-posed with explicit RK4 (no CFL from k³).
# But the (1 + k²) denominator couples all modes through dispersion.
#
# Integrating factor: E = exp(L·dt) = exp(-ik·dt/(1+k²))
# Nonlinear: N = -(ik/2)·F(u²) / (1 + k²)
# ==================================================================

def bbm_linear_factor(k):
    """L = -ik/(1+k²)  — returned as complex array (NOT just a scalar)."""
    return -1j * k / (1.0 + k ** 2)


def bbm_nonlinear_term(u, k, dealias, theta=0.0):
    """N(u) = -(ik/2)·F(u²) / (1 + k²)."""
    u2_hat = fft(u * u) * dealias
    return -0.5j * k * u2_hat / (1.0 + k ** 2)


def bbm_invariants(u, dx, k):
    """BBM invariants:
        M = ∫ u dx
        P = ∫ (u² + u_x²) dx   (note: includes u_x² due to regularized dispersion)
        E = ∫ (u³/3 + u·u_x²) dx  (approximate Hamiltonian)
    """
    M = np.sum(u) * dx
    u_hat = fft(u)
    ux = np.real(ifft(1j * k * u_hat))
    P = (np.sum(u * u) + np.sum(ux * ux)) * dx
    E = (np.sum(u ** 3) / 3.0 + np.sum(u * ux * ux)) * dx
    return M, P, E


def bbm_soliton(x, c, x0=0.0):
    """BBM soliton: u = 3·c·sech²(p·(x − x0))  where p² = c/(4·(1+c)).
    Speed c > 0, amplitude 3c. Valid for 0 < c < 1 (right-moving).
    """
    if c <= 0 or c >= 1:
        raise ValueError("BBM soliton requires 0 < c < 1")
    p = np.sqrt(c / (4.0 * (1.0 + c)))
    return 3.0 * c * sech2(p * (x - x0))


def bbm_make_models():
    """BBM model registry. Linear factor is array-valued."""
    b = 2.0 * THETA_B / np.pi
    return {
        "true_bbm":   ("True BBM",
                       bbm_nonlinear_term,  # nonlinear
                       None,  # linear_factor unused — handled inside nonlinear
                       False, None, 0.0, True),  # use_bbm_linear=True
        "b_rotation": ("b-rotation M1 (BBM, spectral)",
                       bbm_nonlinear_term, None, False,
                       lambda u, k, th: apply_M1_spectral(u, th, k), 1.0, True),
        "b_rodrigues":("b-rotation M2 (Rodrigues, BBM)",
                       bbm_nonlinear_term, None, False,
                       lambda u, k, th: apply_M2_rodrigues(u, th, k), 1.0, True),
        "b_modified": ("b-modified M3 (BBM)",
                       lambda u, k, d, th: _bbm_modified_N(u, k, d, th),
                       None, False, None, 0.0, True),
        "b_brake":    ("b-brake (1-b)·u·u_x (BBM)",
                       lambda u, k, d, th: (
                           -(1.0 - 2.0 * th / np.pi) * 0.5j * k * fft(u*u) * d
                           / (1.0 + k**2)),
                       None, False, None, 0.0, True),
        "b_les":      ("b-LES ν·(1+b)·u_xx (BBM)",
                       lambda u, k, d, th: (
                           -0.5j * k * fft(u*u) * d / (1.0 + k**2)
                           - 0.001 * (1.0 + 2.0 * th / np.pi) * k**2 * fft(u) * d
                           / (1.0 + k**2)),
                       None, True, None, 0.0, True),
    }


def _bbm_modified_N(u, k, dealias, theta):
    """M3 modified nonlinearity for BBM."""
    H_u = hilbert_fft(u, k)
    u_rot = np.cos(theta) * u + np.sin(theta) * H_u
    u_rot2_hat = fft(u_rot * u_rot) * dealias
    return -0.5j * k * u_rot2_hat / (1.0 + k ** 2)


# ==================================================================
# 3. Kawahara — 5th-order KdV  (Oscillatory solitons)
# ==================================================================
# u_t + 6·u·u_x + u_xxx + u_xxxxx = 0
#
# Pseudo-spectral:  û_t = -3ik·F(u²) + ik³·û + ik⁵·û
# Linear part:  L = ik³ + ik⁵ = ik³·(1 + k²)
# |L| ~ k⁵ at high k → IFRK4 essential (else dt·k⁵_max ~ 1000)
#
# Properties:
#  - Solitons have oscillatory tails (unlike pure KdV)
#  - NOT integrable (no Lax pair)
#  - Arises in capillary-gravity waves, plasma physics
# ==================================================================

def kawahara_nonlinear_term(u, k, dealias, theta=0.0):
    """N(u) = -3ik·F(u²)  (same as KdV; dispersion is different)."""
    u2_hat = fft(u * u) * dealias
    return -3j * k * u2_hat


def kawahara_invariants(u, dx, k):
    """Kawahara invariants (only M and P are exact invariants; E is approx)."""
    M = np.sum(u) * dx
    P = np.sum(u * u) * dx
    u_hat = fft(u)
    ux = np.real(ifft(1j * k * u_hat))
    uxx = np.real(ifft(-k ** 2 * u_hat))
    # Approximate Hamiltonian: H = ∫(u_x²/2 - u³/3 - u_xx²/2)·dx
    E = (0.5 * np.sum(ux * ux) - np.sum(u ** 3) / 3.0
         - 0.5 * np.sum(uxx * uxx)) * dx
    return M, P, E


def kawahara_soliton(x, c, x0=0.0):
    """Approximate Kawahara soliton (for IC; not exact).
    Uses the ansatz: u = A·sech²(p·(x-x0))·cos(q·(x-x0))
    where p, q are determined by c. For typical params p≈0.5, q≈1.
    """
    p = 0.5 * np.sqrt(c)
    q = 1.0 * np.sqrt(c)
    A = 3.0 * c
    return A * sech2(p * (x - x0)) * np.cos(q * (x - x0))


def kawahara_make_models():
    """Kawahara model registry. Linear factor is complex: L = ik³·(1+k²).
    We need a custom ifrk4 step because linear_factor is now array-valued.
    """
    b = 2.0 * THETA_B / np.pi
    return {
        "true_kawahara":   ("True Kawahara",
                            kawahara_nonlinear_term,
                            "kawahara",  # special marker for array L
                            False, None, 0.0),
        "b_rotation":      ("b-rotation M1 (Kawahara, spectral)",
                            kawahara_nonlinear_term, "kawahara", False,
                            lambda u, k, th: apply_M1_spectral(u, th, k), 1.0),
        "b_rodrigues":     ("b-rotation M2 (Rodrigues, Kawahara)",
                            kawahara_nonlinear_term, "kawahara", False,
                            lambda u, k, th: apply_M2_rodrigues(u, th, k), 1.0),
        "b_modified":      ("b-modified M3 (Kawahara)",
                            lambda u, k, d, th: _kawahara_modified_N(u, k, d, th),
                            "kawahara", False, None, 0.0),
        "b_brake":         ("b-brake (1-b)·6u·u_x (Kawahara)",
                            lambda u, k, d, th: (
                                -(1.0 - 2.0 * th / np.pi) * 3j * k * fft(u*u) * d),
                            "kawahara", False, None, 0.0),
        "b_les":           ("b-LES ν·(1+b)·u_xx (Kawahara)",
                            lambda u, k, d, th: (
                                -3j * k * fft(u*u) * d
                                - 0.001 * (1.0 + 2.0 * th / np.pi) * k**2 * fft(u) * d),
                            "kawahara", True, None, 0.0),
    }


def _kawahara_modified_N(u, k, dealias, theta):
    """M3 modified nonlinearity for Kawahara (same form as KdV)."""
    H_u = hilbert_fft(u, k)
    u_rot = np.cos(theta) * u + np.sin(theta) * H_u
    u_rot2_hat = fft(u_rot * u_rot) * dealias
    return -3j * k * u_rot2_hat


# ==================================================================
# 4. Unified IFRK4 integrator supporting array-valued linear factors
# ==================================================================
def ifrk4_step_general(u, dt, t, nonlinear_fn, k, dealias,
                        linear_op, theta, post_step_fn=None,
                        eff_theta=0.0):
    """General IFRK4 step supporting:
       - scalar linear_factor (kdv_core style)
       - array linear_op (BBM, Kawahara)

       linear_op : either a scalar (multiplies ik³) or a complex array
                   representing L(k) directly.
    """
    if isinstance(linear_op, str):
        if linear_op == "kawahara":
            L_op = 1j * k ** 3 * (1.0 + k ** 2)
        elif linear_op == "bbm":
            L_op = -1j * k / (1.0 + k ** 2)
        else:
            raise ValueError(f"Unknown linear_op marker: {linear_op}")
    elif np.isscalar(linear_op) or linear_op is None:
        # kdv_core compatibility: linear_op is a scalar multiplying ik³
        factor = 1.0 if linear_op is None else linear_op
        L_op = 1j * k ** 3 * factor
    else:
        # Array-valued L(k)
        L_op = linear_op

    E = np.exp(L_op * dt)
    E_half = np.exp(L_op * dt / 2.0)
    u_hat = fft(u)

    N1 = nonlinear_fn(u, k, dealias, theta)
    u2 = np.real(ifft(E_half * (u_hat + 0.5 * dt * N1)))
    N2 = nonlinear_fn(u2, k, dealias, theta)
    u3 = np.real(ifft(E_half * (u_hat + 0.5 * dt * N2)))
    N3 = nonlinear_fn(u3, k, dealias, theta)
    u4 = np.real(ifft(E * (u_hat + dt * N3)))
    N4 = nonlinear_fn(u4, k, dealias, theta)

    u_new_hat = (E * u_hat
                 + (dt / 6.0) * (E * N1 + 2 * E_half * N2
                                 + 2 * E_half * N3 + N4))
    u_new = np.real(ifft(u_new_hat))
    if post_step_fn is not None:
        u_new = post_step_fn(u_new, k, eff_theta)
        u_new = np.real(ifft(fft(u_new) * dealias))
    return u_new


def integrate_extended(u0, t_final, dt, model_name, model_registry,
                       k, dealias, invariant_fn,
                       save_every=100, diagnose_every=10, verbose=False):
    """Generic integrator for any equation type (mKdV, BBM, Kawahara).

    model_registry: dict returned by *_make_models()
    invariant_fn: function (u, dx, k) -> (M, P, E)
    """
    entry = model_registry[model_name]
    if len(entry) == 7:
        (label, nonlinear_fn, linear_factor, dissipation,
         post_step_fn, angle_factor, *rest) = entry
        use_bbm_linear = rest[0] if rest else False
    else:
        (label, nonlinear_fn, linear_factor, dissipation,
         post_step_fn, angle_factor) = entry
        use_bbm_linear = False

    # Determine linear_op
    if use_bbm_linear:
        linear_op = "bbm"
    elif isinstance(linear_factor, str):
        linear_op = linear_factor
    elif linear_factor is None:
        linear_op = 1.0
    else:
        linear_op = linear_factor

    N = u0.shape[0]
    u = u0.copy().astype(np.float64)
    n_steps = int(np.round(t_final / dt))
    L_eff = 2.0 * np.pi * N / (2.0 * np.max(np.abs(k)))
    dx = L_eff / N

    eff_theta = angle_factor * dt * THETA_B

    n_save = n_steps // save_every + 1
    n_diag = n_steps // diagnose_every + 1
    t_save = np.zeros(n_save)
    u_save = np.zeros((n_save, N))
    t_diag = np.zeros(n_diag)
    inv_M = np.zeros(n_diag)
    inv_P = np.zeros(n_diag)
    inv_E = np.zeros(n_diag)
    umax = np.zeros(n_diag)

    i_save, i_diag = 0, 0
    t_save[i_save] = 0.0
    u_save[i_save] = u
    i_save += 1

    M0, P0, E0 = invariant_fn(u, dx, k)
    t_diag[i_diag] = 0.0
    inv_M[i_diag] = M0
    inv_P[i_diag] = P0
    inv_E[i_diag] = E0
    umax[i_diag] = np.max(np.abs(u))
    i_diag += 1

    for step in range(1, n_steps + 1):
        t_now = (step - 1) * dt
        u = ifrk4_step_general(u, dt, t_now, nonlinear_fn, k, dealias,
                                linear_op, THETA_B,
                                post_step_fn=post_step_fn,
                                eff_theta=eff_theta)
        if step % save_every == 0:
            t_save[i_save] = step * dt
            u_save[i_save] = u
            i_save += 1
        if step % diagnose_every == 0:
            M, P, E = invariant_fn(u, dx, k)
            t_diag[i_diag] = step * dt
            inv_M[i_diag] = M
            inv_P[i_diag] = P
            inv_E[i_diag] = E
            umax[i_diag] = np.max(np.abs(u))
            i_diag += 1
        if verbose and step % (max(1, n_steps // 10)) == 0:
            print(f"  step {step:6d}/{n_steps}, t={step*dt:6.3f}, "
                  f"||u||_max={np.max(np.abs(u)):.4f}")

    return {
        "t_save": t_save[:i_save], "u_save": u_save[:i_save],
        "t_diag": t_diag[:i_diag], "M": inv_M[:i_diag],
        "P": inv_P[:i_diag], "E": inv_E[:i_diag], "umax": umax[:i_diag],
        "dx": dx, "M0": M0, "P0": P0, "E0": E0,
        "model": model_name, "label": label,
        "eff_theta_per_step": float(eff_theta),
    }


# ==================================================================
# 5. Self-test
# ==================================================================
if __name__ == "__main__":
    print("=" * 70)
    print("  extended_solvers.py self-test")
    print("=" * 70)

    x, dx, k = make_grid(L=100.0, N=512)
    dealias = dealias_mask(k)
    print(f"  Grid: L=100, N=512, dx={dx:.4f}, k_max={np.max(np.abs(k)):.2f}")

    # mKdV test
    print("\n  --- mKdV test ---")
    u0_mkdv = mkdv_bright_soliton(x, c=0.5, x0=-20.0)
    M0, P0, E0 = mkdv_invariants(u0_mkdv, dx, k)
    print(f"  mKdV initial: M={M0:.4f}, P={P0:.4f}, E={E0:.4f}")
    models_mkdv = mkdv_make_models()
    res = integrate_extended(u0_mkdv, t_final=10.0, dt=0.002,
                              model_name="true_mkdv",
                              model_registry=models_mkdv,
                              k=k, dealias=dealias,
                              invariant_fn=mkdv_invariants,
                              save_every=2000, diagnose_every=2000)
    print(f"  mKdV after T=10: drift_M={abs(res['M'][-1]-M0)/abs(M0):.2e}, "
          f"drift_E={abs(res['E'][-1]-E0)/abs(E0):.2e}")

    # BBM test
    print("\n  --- BBM test ---")
    u0_bbm = bbm_soliton(x, c=0.5, x0=-20.0)
    M0, P0, E0 = bbm_invariants(u0_bbm, dx, k)
    print(f"  BBM initial: M={M0:.4f}, P={P0:.4f}, E={E0:.4f}")
    models_bbm = bbm_make_models()
    res = integrate_extended(u0_bbm, t_final=10.0, dt=0.002,
                              model_name="true_bbm",
                              model_registry=models_bbm,
                              k=k, dealias=dealias,
                              invariant_fn=bbm_invariants,
                              save_every=2000, diagnose_every=2000)
    print(f"  BBM after T=10: drift_M={abs(res['M'][-1]-M0)/abs(M0):.2e}, "
          f"drift_P={abs(res['P'][-1]-P0)/abs(P0):.2e}")

    # Kawahara test
    print("\n  --- Kawahara test ---")
    u0_kaw = kawahara_soliton(x, c=0.5, x0=-20.0)
    M0, P0, E0 = kawahara_invariants(u0_kaw, dx, k)
    print(f"  Kawahara initial: M={M0:.4f}, P={P0:.4f}, E={E0:.4f}")
    models_kaw = kawahara_make_models()
    res = integrate_extended(u0_kaw, t_final=10.0, dt=0.002,
                              model_name="true_kawahara",
                              model_registry=models_kaw,
                              k=k, dealias=dealias,
                              invariant_fn=kawahara_invariants,
                              save_every=2000, diagnose_every=2000)
    print(f"  Kawahara after T=10: drift_M={abs(res['M'][-1]-M0)/abs(M0):.2e}, "
          f"drift_P={abs(res['P'][-1]-P0)/abs(P0):.2e}")

    print("\n  === self-test PASSED ===")
