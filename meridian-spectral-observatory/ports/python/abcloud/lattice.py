# -*- coding: utf-8 -*-
"""AB-cloud Hofstadter Hamiltonian — 1:1 with ab_cloud_full.jl §6.

Landau gauge along y: phase (up link) carries 2*pi*alpha*iy (torus wrap:
2*pi*alpha*Ny, requires alpha*Ny integer). Two vortex-phase models:
  - "monumental": smooth gauge on vertical links (ab_phase_vortex_monumental)
  - "dirac":      smooth gauge + Dirac string +-2*pi*q on the same links
Disorder: W>0 residual eps uses the portable classic MT19937 (the Julia
original uses dSFMT — documented divergence; all golden anchors are W=0).

Eigenvalues: cyclic Jacobi for complex Hermitian matrices (no LAPACK;
agrees with zheevr to ~1e-12, inside the golden tolerances).
"""

from math import pi, fabs, sqrt, atan2, floor, sin, cos, isnan
from cmath import exp as cexp, phase as _carg


def _conj(z):
    return z.conjugate()

from .mt19937 import MT19937

MODEL_MONUMENTAL = "monumental"   # smooth vortex gauge on vertical links
MODEL_DIRAC = "dirac"             # smooth gauge + Dirac string ±2πq


class Vortex(object):
    __slots__ = ("x", "y", "q")

    def __init__(self, x, y, q):
        self.x = float(x)
        self.y = float(y)
        self.q = float(q)

    def __repr__(self):
        return "Vortex(%r, %r, %r)" % (self.x, self.y, self.q)


class ABCloudConfig(object):
    def __init__(self, Nx, Ny, vortices, alpha, t, lattice, W,
                 disorder_seed=96, model="monumental"):
        self.Nx = int(Nx)
        self.Ny = int(Ny)
        self.vortices = list(vortices)
        self.alpha = float(alpha)
        self.t = float(t)
        self.lattice = lattice        # "open" | "torus"
        self.W = float(W)
        self.disorder_seed = int(disorder_seed)
        self.model = model            # "monumental" | "dirac"


def ab_phase_vortex_monumental(ri, rj, vort):
    """Smooth charge-1/2 gauge: phase = sum_k q_k/2 * (theta_kj - theta_ki)."""
    phase = 0.0
    for vk in vort:
        dx1 = ri[0] - vk.x
        dy1 = ri[1] - vk.y
        dx2 = rj[0] - vk.x
        dy2 = rj[1] - vk.y
        a1 = atan2(dy1, dx1) if (dx1 != 0 or dy1 != 0) else 0.0
        a2 = atan2(dy2, dx2) if (dx2 != 0 or dy2 != 0) else 0.0
        phase += vk.q * (a2 - a1) * 0.5
    return phase


def ab_phase_2d(ri, rj, rk, qk):
    ti = atan2(ri[1] - rk[1], ri[0] - rk[0])
    tj = atan2(rj[1] - rk[1], rj[0] - rk[0])
    return qk * (ti - tj)


def dirac_string_phase(ri, rj, rk, qk, torus, Nx):
    """Dirac string on vertical links crossing vortex column x=rk[0]."""
    if fabs(ri[0] - rj[0]) > 1e-12:
        return 0.0
    y_lo = min(ri[1], rj[1])
    y_hi = max(ri[1], rj[1])
    if not (y_lo < rk[1] < y_hi):
        return 0.0
    if torus:
        if fabs(ri[0] - float(int(floor(rk[0])))) < 0.5:
            return 0.0
    else:
        if ri[0] <= rk[0]:
            return 0.0
    return -2 * pi * qk if ri[1] < rj[1] else 2 * pi * qk


def ab_phase_2d_full(ri, rj, rk, qk, torus, Nx):
    return ab_phase_2d(ri, rj, rk, qk) + \
        dirac_string_phase(ri, rj, rk, qk, torus, Nx)


def vortex_onsite_potential(ri, vort, W, N, rng):
    if not vort and W == 0.0:
        return 0.0
    v = 0.0
    ninv = 1.0 / float(max(N, 1))
    for vk in vort:
        dx = ri[0] - vk.x
        dy = ri[1] - vk.y
        v += vk.q * W / ((dx * dx + dy * dy) * ninv + 1.0)
    if W > 0:
        v += (rng.random() - 0.5) * 0.02
    return v


def build_ab_cloud_hamiltonian(cfg):
    """Return the N x N Hermitian Hamiltonian as a list of lists (complex)."""
    Nx, Ny = cfg.Nx, cfg.Ny
    N = Nx * Ny
    H = [[complex(0.0, 0.0)] * N for _ in range(N)]
    torus = (cfg.lattice == "torus")
    if torus and fabs(cfg.alpha * Ny - round(cfg.alpha * Ny)) >= 1e-10:
        raise AssertionError("torus needs alpha*Ny integer")
    rng = MT19937(cfg.disorder_seed & 0xFFFFFFFF)
    for iy in range(1, Ny + 1):
        for ix in range(1, Nx + 1):
            i = (iy - 1) * Nx + ix - 1
            ri = (float(ix), float(iy))
            # right neighbour
            jx, jy, wrap = ix + 1, iy, False
            if jx > Nx:
                if torus:
                    jx, wrap = 1, True
                else:
                    jx = 0
            if jx != 0:
                j = (jy - 1) * Nx + jx - 1
                phi = 2 * pi * cfg.alpha * iy
                if cfg.model == "dirac":
                    rjp = (float(Nx + 1) if wrap else float(jx), float(jy))
                    for v in cfg.vortices:
                        rk = (v.x, v.y)
                        phi += ab_phase_2d_full(ri, rjp, rk, v.q, torus, Nx)
                hop = -cfg.t * cexp(complex(0.0, phi))
                H[i][j] += hop
                H[j][i] += _conj(hop)
            # up neighbour
            jx, jy, wrap = ix, iy + 1, False
            if jy > Ny:
                if torus:
                    jy, wrap = 1, True
                else:
                    jy = 0
            if jy != 0:
                j = (jy - 1) * Nx + jx - 1
                phi = 2 * pi * cfg.alpha * Ny if wrap else 0.0
                rjp = (float(ix), float(iy) + 1.0)   # unwrapped top
                if cfg.model == "monumental":
                    phi += ab_phase_vortex_monumental(ri, rjp, cfg.vortices)
                else:
                    for v in cfg.vortices:
                        rk = (v.x, v.y)
                        phi += ab_phase_2d_full(ri, rjp, rk, v.q, torus, Nx)
                hop = -cfg.t * cexp(complex(0.0, phi))
                H[i][j] += hop
                H[j][i] += _conj(hop)
            H[i][i] += vortex_onsite_potential(ri, cfg.vortices, cfg.W, N, rng)
    # Hermitian symmetrization (H + H^dagger)/2
    for r in range(N):
        Hr = H[r]
        for c in range(r + 1, N):
            a = Hr[c]
            b = H[c][r]
            m = 0.5 * (a + _conj(b))
            Hr[c] = m
            H[c][r] = _conj(m)
    # numpy array — the HP stack layer uses H.conj().T and vectorized ops
    import numpy as np
    return np.array(H, dtype=complex)


def jacobi_eigvals(H, max_sweeps=60):
    """Cyclic Jacobi for complex Hermitian matrices -> sorted real eigenvalues.

    Operates on a deep copy; H is a list of lists of complex.
    """
    N = len(H)
    A = [list(row) for row in H]   # copy (np rows would alias the input)
    off_norm0 = 0.0
    for r in range(N):
        Ar = A[r]
        for c in range(r + 1, N):
            off_norm0 += abs(Ar[c]) ** 2
    thresh = 1e-15 * sqrt(2.0 * off_norm0 + 1e-300)
    for _ in range(max_sweeps):
        off = 0.0
        for r in range(N):
            Ar = A[r]
            for c in range(r + 1, N):
                off += abs(Ar[c]) ** 2
        if sqrt(2.0 * off) < thresh:
            break
        for p in range(N - 1):
            for q in range(p + 1, N):
                apq = A[p][q]
                if abs(apq) <= thresh:
                    continue
                app = A[p][p].real
                aqq = A[q][q].real
                tau = (aqq - app) / (2.0 * abs(apq))
                t = (1.0 if tau >= 0 else -1.0) / (fabs(tau) + sqrt(1.0 + tau * tau))
                c = 1.0 / sqrt(1.0 + t * t)
                s = t * c                      # normalized rotation (tan = t)
                ph = apq / abs(apq)            # e^{i phi}
                se = s * ph                    # s * e^{i phi}
                sec = _conj(se)
                # rows/cols p,q update: A' = G^dagger A G
                for k in range(N):
                    if k == p or k == q:
                        continue
                    Ak = A[k]
                    akp = Ak[p]
                    akq = Ak[q]
                    nkp = c * akp - sec * akq
                    nkq = se * akp + c * akq
                    Ak[p] = nkp
                    A[p][k] = _conj(nkp)
                    Ak[q] = nkq
                    A[q][k] = _conj(nkq)
                npp = app - t * abs(apq)
                nqq = aqq + t * abs(apq)
                A[p][p] = complex(npp, 0.0)
                A[q][q] = complex(nqq, 0.0)
                A[p][q] = complex(0.0, 0.0)
                A[q][p] = complex(0.0, 0.0)
    ev = sorted(A[r][r].real for r in range(N))
    return ev


def safe_eigvals(H):
    return jacobi_eigvals(H)


def plaquette_flux(H, Nx, Ny, ix, iy, torus=False):
    """CCW sum of arg(-H[b,a]) around the elementary plaquette at (ix, iy)."""
    ix_r = (ix % Nx) + 1 if torus else ix + 1
    iy_t = (iy % Ny) + 1 if torus else iy + 1
    i_bl = (iy - 1) * Nx + ix - 1
    i_br = (iy - 1) * Nx + ix_r - 1
    i_tr = (iy_t - 1) * Nx + ix_r - 1
    i_tl = (iy_t - 1) * Nx + ix - 1
    fb = _carg(-H[i_br][i_bl])
    fr = _carg(-H[i_tr][i_br])
    ft = _carg(-H[i_tl][i_tr])
    fl = _carg(-H[i_bl][i_tl])
    return fb + fr + ft + fl


def flux_circdist(a, b):
    m = (a - b + pi) % (2 * pi)
    return fabs(m - pi)


def central_band_eigs(s, frac):
    """Central band: floor(n*frac/2) levels on each side of the spectrum middle."""
    n = len(s)
    if n == 0:
        return []
    frac = min(max(frac, 0.05), 1.0)
    if frac >= 1.0:
        return list(s)
    half = int(floor(n * frac / 2.0))
    j_lo = max(1, n // 2 - half)
    j_hi = min(n, n // 2 + half)
    return [s[j - 1] for j in range(j_lo, j_hi + 1)]


def chiral_symmetry_defect(H, Nx, Ny):
    """||S H S + H||_F / ||H||_F with S_{(ix,iy)} = (-1)^{ix+iy} — streamed."""
    N = Nx * Ny
    norm_h = 0.0
    num = 0.0
    for r in range(N):
        sr = 1 if (((r % Nx) + 1) + (r // Nx + 1)) % 2 == 0 else -1
        Hr = H[r]
        for c in range(N):
            sc = 1 if (((c % Nx) + 1) + (c // Nx + 1)) % 2 == 0 else -1
            v = (sr * sc) * Hr[c] + Hr[c]
            num += abs(v) ** 2
            norm_h += abs(Hr[c]) ** 2
    return sqrt(num) / max(sqrt(norm_h), 1e-30)


def verify_hermitian(H):
    N = len(H)
    max_err = 0.0
    norm_m = 0.0
    for r in range(N):
        Hr = H[r]
        for c in range(N):
            norm_m += abs(Hr[c]) ** 2
            err = abs(Hr[c] - _conj(H[c][r]))
            if err > max_err:
                max_err = err
    return max_err / max(sqrt(norm_m), 1e-30) < 1e-12


def time_reversal_asymmetry(H):
    diff = 0.0
    norm_m = 0.0
    for row in H:
        for v in row:
            norm_m += abs(v) ** 2
            diff += abs(v - _conj(v)) ** 2
    return sqrt(diff) / max(sqrt(norm_m), 1e-30)
