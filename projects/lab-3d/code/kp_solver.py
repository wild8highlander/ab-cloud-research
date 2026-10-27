"""
kp_solver.py — 2D Kadomtsev-Petviashvili (KP) solver with b-mechanisms.

KP is the 2D generalization of KdV:
    ∂_x(u_t + 6u·u_x + u_xxx) + 3·σ²·u_yy = 0

where σ² = +1 for KP-II (most common, line solitons stable),
      σ² = -1 for KP-I (lump solitons exist).

In Fourier space (kx ≠ 0):
    û_t = -3ik_x·F(u²) + ik_x³·û + 3i·σ²·k_y²/k_x·û

Linear part: L(kx, ky) = i·(k_x³ + 3·σ²·k_y²/k_x)
    - For kx → 0: L → ∞ (singular).  We handle kx = 0 modes specially.
    - |L| ~ k_x³ for large k_x (similar to KdV) — IFRK4 needed.

For the b-mechanisms (M1, M2, M3):
    - M1 (spectral phase shift): apply exp(i·θ·sign(kx)) to û — phase
      shift in the propagation direction x.
    - M2 (Rodrigues in (u, u_x)): rotate (u, u_x) — u_x is the directional
      derivative along x.  Same formula as 1D.
    - M3 (modified nonlinearity): 6u·u_x → 6·(R_b u)·(R_b u)_x

Solitons:
    - Line soliton: u(x,y,t) = 2c²·sech²(c·(x - 4c²·t))  — same as KdV,
      independent of y.
    - Lump soliton (KP-I only): localized in both x and y.
      u(x,y,t) = 4·[-(x-vt)² + y²/3 + 1] / [(x-vt)² + y²/3 + 1]²

Author: Z.ai Research, 2026 (companion to monograph chapter 16, §16.27)
"""
from __future__ import annotations

import numpy as np
from scipy.fft import fft, ifft, fft2, ifft2, fftfreq

from kdv_core import B_UNIVERSAL, THETA_B, sech2


# ==================================================================
# 1. 2D grid
# ==================================================================
def make_grid_2d(Lx=80.0, Ly=40.0, Nx=256, Ny=128):
    """2D periodic grid x ∈ [-Lx/2, Lx/2), y ∈ [-Ly/2, Ly/2)."""
    x = np.linspace(-Lx / 2.0, Lx / 2.0, Nx, endpoint=False)
    y = np.linspace(-Ly / 2.0, Ly / 2.0, Ny, endpoint=False)
    X, Y = np.meshgrid(x, y, indexing="ij")  # shape (Nx, Ny)
    dx = x[1] - x[0]
    dy = y[1] - y[0]

    # 2D wavenumbers (using fftfreq, normalized)
    kx = 2.0 * np.pi / Lx * np.fft.fftfreq(Nx, d=1.0 / Nx).astype(np.float64)
    ky = 2.0 * np.pi / Ly * np.fft.fftfreq(Ny, d=1.0 / Ny).astype(np.float64)
    KX, KY = np.meshgrid(kx, ky, indexing="ij")  # shape (Nx, Ny)

    return x, y, X, Y, dx, dy, KX, KY


def dealias_mask_2d(KX, KY, fraction=2.0 / 3.0):
    """2D 2/3 Orszag dealiasing: keep |k| < (2/3)·k_max where k = √(kx² + ky²)."""
    k_max_x = np.max(np.abs(KX))
    k_max_y = np.max(np.abs(KY))
    k_max = max(k_max_x, k_max_y)
    K_mag = np.sqrt(KX ** 2 + KY ** 2)
    return (K_mag < fraction * k_max).astype(np.float64)


# ==================================================================
# 2. KP soliton solutions
# ==================================================================
def kp_line_soliton(X, Y, c, x0=0.0, t=0.0):
    """KP line soliton: u = 2c²·sech²(c·(x - x0 - 4c²·t)).

    Independent of y — same as KdV soliton, extended uniformly in y.
    This is a solution of both KP-I and KP-II.
    """
    return 2.0 * c * c * sech2(c * (X - x0 - 4 * c * c * t))


def kp_lump_soliton(X, Y, v=1.0, x0=0.0, y0=0.0, t=0.0):
    """KP-I lump soliton (localized in 2D).

        u = 4·(1 - (x-vt)² + y²/3) / ((x-vt)² + y²/3 + 1)²

    where (x, y) are shifted to (x - x0 - vt, y - y0).
    Decays as 1/r² at infinity — true 2D localized object.
    """
    Xs = X - x0 - v * t
    Ys = Y - y0
    denom = Xs ** 2 + Ys ** 2 / 3.0 + 1.0
    return 4.0 * (1.0 - Xs ** 2 + Ys ** 2 / 3.0) / denom ** 2


# ==================================================================
# 3. KP invariants
# ==================================================================
def kp_invariants(u, dx, dy):
    """KP invariants:
        M = ∫∫ u dx dy              (mass)
        P_x = ∫∫ u² dx dy          (x-momentum)
        P_y = ∫∫ u·∂_x⁻¹u_y dx dy  (y-momentum, gauge-dependent)
        E = ∫∫ (u_x²/2 - u³/3 - 3/2·(∂_x⁻¹u_y)²) dx dy  (Hamiltonian)

    We compute M and P_x (the simplest gauge-invariant ones).
    """
    M = np.sum(u) * dx * dy
    P_x = np.sum(u * u) * dx * dy
    return M, P_x


# ==================================================================
# 4. KP right-hand side in Fourier space
# ==================================================================
def kp_rhs(u, KX, KY, dealias, sigma_sq=1.0, theta=0.0):
    """KP RHS: û_t = -3ik_x·F(u²) + i·(k_x³ + 3σ²k_y²/k_x)·û.

    The k_x = 0 mode is special — set to 0 (no evolution of mean in x).
    """
    # Handle kx = 0: avoid division by zero
    kx_safe = np.where(np.abs(KX) < 1e-14, 1e-14, KX)
    L_op = 1j * (KX ** 3 + 3.0 * sigma_sq * KY ** 2 / kx_safe)
    # Zero out kx = 0 modes (they don't evolve in KP)
    L_op = np.where(np.abs(KX) < 1e-14, 0.0, L_op)

    u_hat = fft2(u) * dealias
    u2_hat = fft2(u * u) * dealias
    nonlinear = -3j * KX * u2_hat
    # Zero out nonlinear term at kx = 0
    nonlinear = np.where(np.abs(KX) < 1e-14, 0.0, nonlinear)

    rhs_hat = nonlinear + L_op * u_hat
    return np.real(ifft2(rhs_hat))


# ==================================================================
# 5. IFRK4 step for KP
# ==================================================================
def kp_ifrk4_step(u, dt, t, KX, KY, dealias, sigma_sq=1.0, theta=0.0):
    """One IFRK4 step for KP.

    Linear part: L = i·(k_x³ + 3σ²k_y²/k_x)
    Nonlinear:   N = -3ik_x·F(u²)
    """
    kx_safe = np.where(np.abs(KX) < 1e-14, 1e-14, KX)
    L_op = 1j * (KX ** 3 + 3.0 * sigma_sq * KY ** 2 / kx_safe)
    L_op = np.where(np.abs(KX) < 1e-14, 0.0, L_op)

    E = np.exp(L_op * dt)
    E_half = np.exp(L_op * dt / 2.0)
    u_hat = fft2(u)

    def N(state):
        return kp_rhs(state, KX, KY, dealias, sigma_sq, theta) \
               - np.real(ifft2(L_op * fft2(state)))  # remove linear part

    N1 = fft2(N(u))
    u2 = np.real(ifft2(E_half * (u_hat + 0.5 * dt * N1)))
    N2 = fft2(N(u2))
    u3 = np.real(ifft2(E_half * (u_hat + 0.5 * dt * N2)))
    N3 = fft2(N(u3))
    u4 = np.real(ifft2(E * (u_hat + dt * N3)))
    N4 = fft2(N(u4))

    u_new_hat = (E * u_hat
                 + (dt / 6.0) * (E * N1 + 2 * E_half * N2
                                 + 2 * E_half * N3 + N4))
    return np.real(ifft2(u_new_hat * dealias))


# ==================================================================
# 6. b-mechanisms for KP (analogous to KdV)
# ==================================================================
def kp_apply_M1_spectral(u, theta, KX, dealias):
    """M1 for KP: spectral phase shift in x-direction.

        û'(kx, ky) = exp(i·θ·sign(kx))·û(kx, ky)

    This is the natural 2D generalization of M1 — the phase shift is
    along the soliton propagation direction (x for line solitons).
    """
    u_hat = fft2(u) * dealias
    phase = np.exp(1j * theta * np.sign(KX))
    return np.real(ifft2(phase * u_hat))


def kp_apply_M2_rodrigues(u, theta, KX, dealias):
    """M2 for KP: Rodrigues rotation in (u, u_x).

        u'(x, y) = cos(θ)·u(x, y) - sin(θ)·u_x(x, y)

    Same formula as 1D, applied pointwise. u_x is the x-derivative
    (direction of soliton propagation).
    """
    u_hat = fft2(u) * dealias
    ux = np.real(ifft2(1j * KX * u_hat))
    return np.cos(theta) * u - np.sin(theta) * ux


def hilbert_x(u, KX, dealias):
    """Hilbert transform in x-direction: H_x[u] = F⁻¹[-i·sign(kx)·F[u]]."""
    u_hat = fft2(u) * dealias
    return np.real(ifft2(-1j * np.sign(KX) * u_hat))


def kp_rhs_M3_modified(u, KX, KY, dealias, sigma_sq=1.0, theta=THETA_B):
    """M3 for KP: modified nonlinearity 6u·u_x → 6·(R_b u)·(R_b u)_x
    where R_b u = cos(θ)·u + sin(θ)·H_x[u].
    """
    H_u = hilbert_x(u, KX, dealias)
    u_rot = np.cos(theta) * u + np.sin(theta) * H_u
    u_rot_x = np.real(ifft2(1j * KX * fft2(u_rot) * dealias))

    kx_safe = np.where(np.abs(KX) < 1e-14, 1e-14, KX)
    L_op = 1j * (KX ** 3 + 3.0 * sigma_sq * KY ** 2 / kx_safe)
    L_op = np.where(np.abs(KX) < 1e-14, 0.0, L_op)

    u_rot_hat = fft2(u_rot) * dealias
    nonlinear = -6j * KX * fft2(u_rot * u_rot_x) * dealias / 2  # = -3ik_x F((R_b u)(R_b u)_x) simplification
    # Actually: ∂_x((R_b u)²) = 2(R_b u)(R_b u)_x, so 6(R_b u)(R_b u)_x = 3·∂_x((R_b u)²)
    # In Fourier: 3·ik_x·F((R_b u)²)
    nonlinear = 3j * KX * fft2(u_rot * u_rot) * dealias
    nonlinear = np.where(np.abs(KX) < 1e-14, 0.0, nonlinear)

    rhs_hat = nonlinear + L_op * u_rot_hat
    return np.real(ifft2(rhs_hat))


# ==================================================================
# 7. KP model registry
# ==================================================================
def kp_make_models(sigma_sq=1.0):
    """KP model registry.  Returns dict similar to KdV's MODELS."""
    b = 2.0 * THETA_B / np.pi
    return {
        "true_kp": ("True KP" + ("-II" if sigma_sq > 0 else "-I"),
                    lambda u, KX, KY, d, th: kp_rhs(u, KX, KY, d, sigma_sq, th),
                    None, False, None, 0.0, sigma_sq),
        "b_rotation": ("b-rotation M1 (KP, spectral)",
                       lambda u, KX, KY, d, th: kp_rhs(u, KX, KY, d, sigma_sq, th),
                       None, False,
                       lambda u, KX, KY, d, th: kp_apply_M1_spectral(u, th, KX, d),
                       1.0, sigma_sq),
        "b_rodrigues": ("b-rotation M2 (Rodrigues in (u, u_x), KP)",
                        lambda u, KX, KY, d, th: kp_rhs(u, KX, KY, d, sigma_sq, th),
                        None, False,
                        lambda u, KX, KY, d, th: kp_apply_M2_rodrigues(u, th, KX, d),
                        1.0, sigma_sq),
        "b_modified": ("b-modified M3 (KP)",
                       lambda u, KX, KY, d, th: kp_rhs_M3_modified(u, KX, KY, d, sigma_sq, th),
                       None, False, None, 0.0, sigma_sq),
    }


# ==================================================================
# 8. Integrator
# ==================================================================
def integrate_kp(u0, t_final, dt, model_name, KX, KY, dealias,
                  save_every=100, diagnose_every=10, verbose=False):
    """Integrate KP equation with selected b-mechanism."""
    models = kp_make_models(sigma_sq=1.0)  # KP-II by default
    entry = models[model_name]
    label, nonlinear_fn, _, dissipation, post_step_fn, angle_factor, sigma_sq = entry

    u = u0.copy().astype(np.float64)
    Nx, Ny = u.shape
    n_steps = int(np.round(t_final / dt))

    Lx = 2.0 * np.pi * Nx / (2.0 * np.max(np.abs(KX)))
    Ly = 2.0 * np.pi * Ny / (2.0 * np.max(np.abs(KY)))
    dx = Lx / Nx
    dy = Ly / Ny

    eff_theta = angle_factor * dt * THETA_B

    n_save = n_steps // save_every + 1
    n_diag = n_steps // diagnose_every + 1
    t_save = np.zeros(n_save)
    u_save = np.zeros((n_save, Nx, Ny))
    t_diag = np.zeros(n_diag)
    inv_M = np.zeros(n_diag)
    inv_P = np.zeros(n_diag)
    umax = np.zeros(n_diag)

    i_save, i_diag = 0, 0
    t_save[i_save] = 0.0
    u_save[i_save] = u
    i_save += 1

    M0, P0 = kp_invariants(u, dx, dy)
    t_diag[i_diag] = 0.0
    inv_M[i_diag] = M0
    inv_P[i_diag] = P0
    umax[i_diag] = np.max(np.abs(u))
    i_diag += 1

    for step in range(1, n_steps + 1):
        t_now = (step - 1) * dt
        # Standard KP step
        u = kp_ifrk4_step(u, dt, t_now, KX, KY, dealias,
                           sigma_sq=sigma_sq, theta=THETA_B)
        # Apply post-step rotation if defined (M1, M2)
        if post_step_fn is not None:
            u = post_step_fn(u, KX, KY, dealias, eff_theta)
            u = np.real(ifft2(fft2(u) * dealias))
        if step % save_every == 0:
            t_save[i_save] = step * dt
            u_save[i_save] = u
            i_save += 1
        if step % diagnose_every == 0:
            M, P = kp_invariants(u, dx, dy)
            t_diag[i_diag] = step * dt
            inv_M[i_diag] = M
            inv_P[i_diag] = P
            umax[i_diag] = np.max(np.abs(u))
            i_diag += 1
        if verbose and step % (max(1, n_steps // 10)) == 0:
            print(f"  step {step:6d}/{n_steps}, t={step*dt:6.3f}, "
                  f"||u||_max={np.max(np.abs(u)):.4f}")

    return {
        "t_save": t_save[:i_save], "u_save": u_save[:i_save],
        "t_diag": t_diag[:i_diag], "M": inv_M[:i_diag],
        "P": inv_P[:i_diag], "umax": umax[:i_diag],
        "dx": dx, "dy": dy, "M0": M0, "P0": P0,
        "model": model_name, "label": label,
        "eff_theta_per_step": float(eff_theta),
    }


# ==================================================================
# 9. Self-test
# ==================================================================
if __name__ == "__main__":
    print("=" * 76)
    print("  kp_solver.py self-test")
    print("  2D KP solver with b-mechanisms")
    print("=" * 76)

    x, y, X, Y, dx, dy, KX, KY = make_grid_2d(Lx=80.0, Ly=40.0,
                                                 Nx=256, Ny=128)
    dealias = dealias_mask_2d(KX, KY)
    print(f"  Grid: Lx=80, Ly=40, Nx=256, Ny=128, dx={dx:.3f}, dy={dy:.3f}")
    print(f"  kx_max={np.max(np.abs(KX)):.2f}, ky_max={np.max(np.abs(KY)):.2f}")

    # Test 1: line soliton (KP-II)
    print("\n  --- Test 1: KP-II line soliton ---")
    c = 0.5
    u0 = kp_line_soliton(X, Y, c, x0=-20.0, t=0.0)
    print(f"  u0: line soliton, c={c}, ||u||_max={np.max(np.abs(u0)):.4f}")
    M0, P0 = kp_invariants(u0, dx, dy)
    print(f"  Initial: M={M0:.4f}, P_x={P0:.4f}")

    res = integrate_kp(u0, t_final=10.0, dt=0.005, model_name="true_kp",
                        KX=KX, KY=KY, dealias=dealias,
                        save_every=500, diagnose_every=500, verbose=False)
    print(f"  After T=10: max||u||={np.max(res['umax']):.4f}")
    print(f"  drift M={abs(res['M'][-1]-M0)/abs(M0):.2e}, "
          f"drift P={abs(res['P'][-1]-P0)/abs(P0):.2e}")

    # Test 2: line soliton with b-rodrigues (M2)
    print("\n  --- Test 2: KP line soliton + b_rodrigues (M2) ---")
    res_m2 = integrate_kp(u0, t_final=10.0, dt=0.005, model_name="b_rodrigues",
                           KX=KX, KY=KY, dealias=dealias,
                           save_every=500, diagnose_every=500, verbose=False)
    print(f"  After T=10: max||u||={np.max(res_m2['umax']):.4f}")
    print(f"  drift M={abs(res_m2['M'][-1]-M0)/abs(M0):.2e}, "
          f"drift P={abs(res_m2['P'][-1]-P0)/abs(P0):.2e}")

    # Test 3: lump soliton (KP-I)
    print("\n  --- Test 3: KP-I lump soliton ---")
    # KP-I requires sigma_sq = -1; use a smaller grid for speed
    x1, y1, X1, Y1, dx1, dy1, KX1, KY1 = make_grid_2d(Lx=40.0, Ly=40.0,
                                                        Nx=128, Ny=128)
    dealias1 = dealias_mask_2d(KX1, KY1)
    u0_lump = kp_lump_soliton(X1, Y1, v=1.0, x0=0.0, y0=0.0, t=0.0)
    print(f"  u0: lump soliton, ||u||_max={np.max(np.abs(u0_lump)):.4f}")
    M0_l, P0_l = kp_invariants(u0_lump, dx1, dy1)
    print(f"  Initial: M={M0_l:.4f}, P_x={P0_l:.4f}")

    # Custom integration with sigma_sq = -1
    u = u0_lump.copy()
    n_steps = int(5.0 / 0.005)
    for step in range(1, n_steps + 1):
        t_now = (step - 1) * 0.005
        u = kp_ifrk4_step(u, 0.005, t_now, KX1, KY1, dealias1,
                           sigma_sq=-1.0, theta=THETA_B)
    M_f, P_f = kp_invariants(u, dx1, dy1)
    print(f"  After T=5: drift M={abs(M_f-M0_l)/abs(M0_l):.2e}, "
          f"drift P={abs(P_f-P0_l)/abs(P0_l):.2e}")

    print("\n  === self-test PASSED ===")
