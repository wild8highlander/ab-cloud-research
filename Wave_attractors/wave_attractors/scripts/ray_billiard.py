#!/usr/bin/env python3
"""
ray_billiard.py — Core ray dynamics of waves in hyperbolic cavities.

Reference study
---------------
"Hyperbolic wave attractors" — Nature Physics (2026),
CUNY Advanced Science Research Center. Numerical reproduction package
for the AB-Cloud Research repository (study W1).

Physics
-------
We use the TE-like scalar polarization of a 2D anisotropic medium with a
magnetic permeability tensor

    mu = diag(mu_x, mu_y) = diag(1, -eta),      eta > 0,

i.e. an indefinite (hyperbolic) material. The dispersion relation is

    k_y^2 - k_x^2 / eta = K^2,      K = omega / c,

an iso-frequency hyperbola opening along +/-y with two branches
(sign of k_y). The group velocity is normal to the iso-frequency contour:

    v_g  ∝  (-k_x / eta,  k_y),

so the energy flow is confined to a propagation cone of half-angle

    alpha_max = arctan(1 / sqrt(eta))

around the optical axis (the y-axis): the defining property of a
hyperbolic medium ("waves propagate only along narrow prescribed
directions").

Reflection off a perfectly conducting (PEC) wall
------------------------------------------------
Translation invariance along the wall conserves the tangential
wave-vector component k_t. Writing k = k_t * t + k_n * n with an
orthonormal (tangent t, inward normal n) wall basis, the dispersion
relation becomes a quadratic in k_n:

    A k_n^2 + B k_n + C = 0,
    A = n_y^2 - n_x^2/eta
    B = 2 k_t (t_y n_y - t_x n_x / eta)
    C = k_t^2 (t_y^2 - t_x^2/eta) - K^2

The incident wave is one root; the reflected wave is the other root
(Vieta). This is generally NON-specular: mirror symmetry is broken by
the material, which is the mechanism behind hyperbolic wave attractors.
The isotropic control medium (mu = 1, circular iso-frequency contour)
gives the familiar mirror reflection k_n -> -k_n.

Because the incident wave itself lies on the iso-frequency contour, the
quadratic always has two real roots — in a hyperbolic medium reflection
from a PEC wall never becomes evanescent (no total-internal-reflection
gap), one of the practical advantages of hyperabolic media.

State: the ray state is (position, k on the iso-frequency contour).
Propagation between walls is along v_g (group velocity), NOT along k —
in a hyperbolic medium the wave vector and the energy flow differ.

Author: AB-Cloud Research (study W1), 2026
License: see repository LICENSE (Custom Research License)
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass, field
from typing import List, Optional, Sequence, Tuple

import numpy as np

EPS_ROOT = 1e-12


# ----------------------------------------------------------------------------
# Media
# ----------------------------------------------------------------------------
@dataclass(frozen=True)
class Medium:
    """Scalar 2D medium: hyperbolic (eta > 0) or isotropic control."""

    kind: str = "hyperbolic"   # "hyperbolic" | "isotropic"
    eta: float = 100.0         # anisotropy |mu_y| with mu = diag(1, -eta)

    def cone_half_angle(self) -> float:
        """Half-angle of the group-velocity cone around the optical axis."""
        if self.kind == "isotropic":
            return math.pi / 2
        return math.atan(1.0 / math.sqrt(self.eta))

    def group_velocity(self, k: np.ndarray) -> np.ndarray:
        """Group velocity direction (unnormalised) for wave vector k."""
        kx, ky = k
        if self.kind == "isotropic":
            return np.array([kx, ky], dtype=float)
        return np.array([-kx / self.eta, ky], dtype=float)

    def dispersion_coeffs(self, kt: float, n: np.ndarray, t: np.ndarray,
                          K: float) -> Tuple[float, float, float]:
        """A, B, C of the k_n quadratic for a wall basis (t, n)."""
        if self.kind == "isotropic":
            # k_n^2 = K^2 - k_t^2  ->  A=1, B=0, C = kt^2 - K^2
            return 1.0, 0.0, kt * kt - K * K
        nx, ny = n
        tx, ty = t
        A = ny * ny - nx * nx / self.eta
        B = 2.0 * kt * (ty * ny - tx * nx / self.eta)
        C = kt * kt * (ty * ty - tx * tx / self.eta) - K * K
        return A, B, C


# ----------------------------------------------------------------------------
# Chambers (simple polygons, may be non-convex)
# ----------------------------------------------------------------------------
@dataclass
class Chamber:
    """Simple polygonal cavity; vertices in CCW order, closed automatically."""

    vertices: np.ndarray
    name: str = "chamber"

    @staticmethod
    def from_points(pts: Sequence[Sequence[float]], name: str = "chamber") -> "Chamber":
        v = np.asarray(pts, dtype=float)
        if not np.allclose(v[0], v[-1]):
            v = np.vstack([v, v[0]])
        return Chamber(vertices=v, name=name)

    def mirror_x(self, name: Optional[str] = None) -> "Chamber":
        """Mirror image across the vertical axis x -> -x (chirality test)."""
        v = self.vertices.copy()
        v[:, 0] = -v[:, 0]
        # keep CCW orientation
        if self._signed_area(v) < 0:
            v = v[::-1]
        return Chamber(vertices=v, name=name or (self.name + "_mirrored"))

    @staticmethod
    def _signed_area(v: np.ndarray) -> float:
        x, y = v[:, 0], v[:, 1]
        return 0.5 * np.sum(x[:-1] * y[1:] - x[1:] * y[:-1])

    @property
    def signed_area(self) -> float:
        return self._signed_area(self.vertices)

    def walls(self) -> List[Tuple[np.ndarray, np.ndarray, np.ndarray]]:
        """List of (P0, t_hat, n_inward) for each wall segment (CCW polygon).

        Index i corresponds to segment [v_i, v_i+1]; degenerate (zero-length)
        segments are kept as entries so that edge indices stay aligned with
        first_hit().
        """
        out = []
        v = self.vertices
        for i in range(len(v) - 1):
            p0 = v[i]
            p1 = v[i + 1]
            e = p1 - p0
            L = np.hypot(*e)
            if L < 1e-14:
                # degenerate segment: neutral entry (never hit)
                out.append((p0, np.array([1.0, 0.0]), np.array([0.0, 1.0])))
                continue
            t = e / L
            # rotate t by +90 deg; ensure it points to the interior
            n_in = np.array([-t[1], t[0]])
            centroid = v[:-1].mean(axis=0)
            if np.dot(n_in, centroid - p0) < 0:
                n_in = -n_in
            out.append((p0, t, n_in))
        return out

    def contains(self, p: np.ndarray, tol: float = 1e-9) -> bool:
        """Even-odd point-in-polygon test."""
        x, y = p
        v = self.vertices
        inside = False
        n = len(v) - 1
        for i in range(n):
            x1, y1 = v[i]
            x2, y2 = v[i + 1]
            if (y1 > y) != (y2 > y):
                xint = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                if x < xint:
                    inside = not inside
        return inside

    def first_hit(self, p: np.ndarray, d: np.ndarray,
                  exclude_edge: Optional[int] = None) -> Optional[Tuple[float, int]]:
        """Nearest positive intersection of ray p + s*d with the boundary.

        Returns (s, edge_index) or None. s > EPS_HIT required.
        """
        best_s, best_i = np.inf, -1
        v = self.vertices
        for i in range(len(v) - 1):
            if i == exclude_edge:
                continue
            a = v[i]
            e = v[i + 1] - a
            # solve p + s d = a + u e,  0 <= u <= 1, s > EPS
            M = np.array([[d[0], -e[0]], [d[1], -e[1]]])
            det = M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]
            if abs(det) < 1e-15:
                continue
            rhs = a - p
            s = (rhs[0] * M[1, 1] - rhs[1] * M[0, 1]) / det
            u = (M[0, 0] * rhs[1] - M[1, 0] * rhs[0]) / det
            if s > 1e-11 and -1e-9 <= u <= 1.0 + 1e-9 and s < best_s:
                best_s, best_i = s, i
        if best_i < 0:
            return None
        return best_s, best_i

    def bbox(self) -> Tuple[float, float, float, float]:
        v = self.vertices
        return v[:, 0].min(), v[:, 0].max(), v[:, 1].min(), v[:, 1].max()


# ----------------------------------------------------------------------------
# Reflection
# ----------------------------------------------------------------------------
def reflect(k: np.ndarray, t: np.ndarray, n: np.ndarray, med: Medium,
            K: float) -> np.ndarray:
    """Exact k-vector reflection law for the anisotropic dispersion.

    Conserves k_t, solves the dispersion quadratic for k_n and returns the
    root different from the incident one. Falls back to Vieta when the
    quadratic degenerates (wall normal aligned with the dispersion
    asymptote).
    """
    kt = float(np.dot(k, t))
    kn_inc = float(np.dot(k, n))
    A, B, C = med.dispersion_coeffs(kt, n, t, K)

    if abs(A) < EPS_ROOT:
        if abs(B) < EPS_ROOT:
            # fully degenerate: keep incident state (grazing)
            return k.copy()
        kn_new = -C / B
    else:
        disc = B * B - 4.0 * A * C
        if disc < 0.0:
            # numerically should not happen (incident root exists);
            # clamp to the marginal case
            disc = 0.0
        sq = math.sqrt(disc)
        r1 = (-B - sq) / (2.0 * A)
        r2 = (-B + sq) / (2.0 * A)
        # pick the root that differs from the incident one
        kn_new = r2 if abs(r2 - kn_inc) >= abs(r1 - kn_inc) else r1

    k_new = kt * t + kn_new * n
    # numerical re-projection onto the dispersion contour ( polishing ):
    # rescale the k_n component so that F(k) = K^2 to machine-ish precision
    k_new = _polish_on_contour(k_new, kt, t, n, med, K)
    return k_new


def _polish_on_contour(k: np.ndarray, kt: float, t: np.ndarray, n: np.ndarray,
                       med: Medium, K: float) -> np.ndarray:
    """One Newton step of re-projection: adjust k_n so that F(k)=K^2."""
    kn = float(np.dot(k, n))
    A, B, C = med.dispersion_coeffs(kt, n, t, K)
    F = A * kn * kn + B * kn + C          # residual (should be 0)
    dF = 2.0 * A * kn + B                 # dF/dkn
    if abs(dF) < 1e-14:
        return k
    return kt * t + (kn - F / dF) * n


# ----------------------------------------------------------------------------
# Ray propagation
# ----------------------------------------------------------------------------
@dataclass
class RayResult:
    bounce_points: np.ndarray      # (M, 2) wall hit points, starting with p0
    k_history: np.ndarray          # (M+1, 2) k at each free flight start
    vg_history: np.ndarray         # (M+1, 2) group velocity directions (unit)
    seg_lengths: np.ndarray        # (M,) free-flight lengths
    edges: List[int]               # wall index of each bounce
    closed_loop: Optional[np.ndarray] = None   # (m, 2) limit cycle if found
    period: int = 0                            # attractor period m


def unit(v: np.ndarray) -> np.ndarray:
    L = np.hypot(*v)
    if L < 1e-15:
        raise ValueError("zero-length vector")
    return v / L


def _rotate(k: np.ndarray, ang: float) -> np.ndarray:
    c, s = math.cos(ang), math.sin(ang)
    return np.array([c * k[0] - s * k[1], s * k[0] + c * k[1]])


def propagate_ray(chamber: Chamber, med: Medium, p0: np.ndarray, k0: np.ndarray,
                  K: float, max_bounces: int = 300,
                  loop_tol: float = 1e-6,
                  loop_window: int = 60,
                  corner_retry: int = 8) -> RayResult:
    """Propagate one ray up to max_bounces wall reflections.

    Also attempts limit-cycle detection: if the last bounce sequence
    becomes periodic with period m <= loop_window within loop_tol, the
    closing loop is recorded.
    """
    pts = [p0.copy()]
    ks = [k0.copy()]
    vgs = [unit(med.group_velocity(k0))]
    segs = []
    edges = []

    p = p0.copy()
    k = k0.copy()
    last_edge: Optional[int] = None

    scale = float(np.ptp(chamber.vertices, axis=0).max())
    corner_eps = 1e-7 * scale
    WALLS = chamber.walls()
    n_verts = len(chamber.vertices) - 1

    for bounce_i in range(max_bounces):
        d = unit(med.group_velocity(k))
        hit = chamber.first_hit(p, d)
        if hit is None:
            raise RuntimeError(
                f"ray escaped chamber at p={p}, d={d} (degenerate geometry?)")
        s, edge = hit
        p_hit = p + s * d

        # --- corner robustness: a hit (almost) exactly at a vertex is
        # reflected off the BISECTOR of the two adjacent wall normals
        # (a rounded-corner defect model; deterministic, identical across
        # language implementations — required for cross-verification).
        corner_hit = False
        v = chamber.vertices
        dmin = np.min(np.hypot(v[:-1, 0] - p_hit[0], v[:-1, 1] - p_hit[1]))
        if dmin <= corner_eps:
            j = int(np.argmin(np.hypot(v[:-1, 0] - p_hit[0],
                                       v[:-1, 1] - p_hit[1])))
            n1 = WALLS[j][2]
            j2 = (j - 1) % n_verts
            n2 = WALLS[j2][2]
            n_eff = unit(n1 + n2)
            t_eff = np.array([-n_eff[1], n_eff[0]])
            k = reflect(k, t_eff, n_eff, med, K)
            corner_hit = True
            edge = j

        p = p_hit
        pts.append(p.copy())
        segs.append(float(s))
        edges.append(edge)

        if corner_hit:
            n_out = n_eff
        else:
            _, t, n = WALLS[edge]
            k = reflect(k, t, n, med, K)
            n_out = n
        ks.append(k.copy())
        vg_new = unit(med.group_velocity(k))
        vgs.append(vg_new)
        last_edge = edge
        # tiny step along the INWARD NORMAL so the next free flight starts
        # strictly inside the domain (safe at corners and for grazing rays:
        # n_eff lies inside both adjacent half-planes by construction)
        p = p + n_out * (1e-9 * scale)

    pts_arr = np.asarray(pts)
    loop, period = detect_limit_cycle(pts_arr, loop_tol, loop_window)
    return RayResult(
        bounce_points=pts_arr,
        k_history=np.asarray(ks),
        vg_history=np.asarray(vgs),
        seg_lengths=np.asarray(segs),
        edges=edges,
        closed_loop=loop,
        period=period,
    )


def detect_limit_cycle(pts: np.ndarray, tol: float = 1e-6,
                       max_period: int = 60) -> Tuple[Optional[np.ndarray], int]:
    """Detect a closing periodic orbit in the bounce-point sequence.

    Finds the smallest period m such that the trajectory retraces itself:
    |P_{i+m} - P_i| < tol for a window of consecutive bounces.
    """
    M = len(pts)
    if M < 8:
        return None, 0
    # check recent tail only (converged regime)
    tail_start = max(0, M - max_period - 10)
    for m in range(2, min(max_period, (M - tail_start) // 2) + 1):
        idx0 = M - m
        ok = True
        for j in range(m):
            i1 = idx0 - j
            i2 = idx0 - j - m
            if i2 < tail_start:
                break
            if np.hypot(*(pts[i1] - pts[i2])) > tol:
                ok = False
                break
        if ok:
            loop = pts[M - m:].copy()
            return loop, m
    return None, 0


def distance_to_loop(p: np.ndarray, loop: np.ndarray) -> float:
    """Distance from point p to a closed polyline (loop, unsorted segments)."""
    if loop is None or len(loop) < 2:
        return np.inf
    dmin = np.inf
    L = np.vstack([loop, loop[:1]])
    for i in range(len(L) - 1):
        a, b = L[i], L[i + 1]
        ab = b - a
        L2 = float(ab @ ab)
        if L2 < 1e-18:
            d = np.hypot(*(p - a))
        else:
            u = float(np.clip((p - a) @ ab / L2, 0.0, 1.0))
            d = np.hypot(*(p - (a + u * ab)))
        dmin = min(dmin, d)
    return dmin


# ----------------------------------------------------------------------------
# Chirality (net signed turning of a closed loop)
# ----------------------------------------------------------------------------
def chirality_index(loop: np.ndarray) -> float:
    """Net signed rotation (in full turns) of the tangent along a closed loop.

    Positive = counter-clockwise, negative = clockwise. |C| ~ 1 for a
    simple convex loop.
    """
    L = np.vstack([loop, loop[:1], loop[1:2]])
    d = L[1:-1] - L[:-2]
    ang = np.arctan2(d[:, 1], d[:, 0])
    dphi = np.diff(np.unwrap(ang))
    return float(np.sum(dphi) / (2.0 * np.pi))


# ----------------------------------------------------------------------------
# Standard chambers used by the study
# ----------------------------------------------------------------------------
def chamber_trapezoid(slope: float = 0.28, w: float = 1.0, h: float = 1.0,
                      name: str = "trapezoid") -> Chamber:
    """Ocean-inspired trapezoid: vertical side walls replaced by slopes.

    slope: horizontal displacement of the bottom corners relative to top.
    """
    pts = [(0.0, h), (w, h), (w - slope, 0.0), (slope, 0.0)]
    return Chamber.from_points(pts, name=name)


def chamber_hexagon(s: float = 0.03, y_v: float = 0.3, w: float = 1.0,
                    h: float = 1.0, name: str = "hexagon") -> Chamber:
    """Rectangle with two bottom corners cut by shallow slopes.

    Vertical side walls (x=0, x=w) for y in [y_v, h]; shallow slopes connect
    the vertical walls to the bottom. The vertical walls flip the horizontal
    drift without changing |k| (for the hyperbolic dispersion the reflection
    off a vertical wall is 'specular': kx -> -kx, ky conserved), while the
    shallow slopes provide the wavelength cascade. Their combination yields
    robust closed-loop attractors.
    """
    pts = [(0.0, h), (w, h), (w, y_v), (w - s, 0.0), (s, 0.0), (0.0, y_v)]
    return Chamber.from_points(pts, name=name)


def chamber_hexagon_asym(s_left: float = 0.03, s_right: float = 0.06,
                         y_v: float = 0.35, w: float = 1.0, h: float = 1.0,
                         name: str = "hexagon_asym") -> Chamber:
    """Hexagon with DIFFERENT left/right slope lengths (mirror-asymmetric).

    The geometric asymmetry selects a single circulation sense of the
    attractor (chirality); its mirror image selects the opposite sense.
    """
    pts = [(0.0, h), (w, h), (w, y_v), (w - s_right, 0.0), (s_left, 0.0),
           (0.0, y_v)]
    return Chamber.from_points(pts, name=name)


def chamber_odd(seed: int = 7, scale: float = 1.0,
                name: str = "odd") -> Chamber:
    """Irregular pentagon ('odd-shaped cavity' of the reference study)."""
    rng = np.random.default_rng(seed)
    ang = np.sort(rng.uniform(0, 2 * np.pi, 5))
    rad = scale * (0.42 + 0.20 * rng.uniform(0, 1, 5))
    pts = np.column_stack([0.5 + rad * np.cos(ang), 0.5 + rad * np.sin(ang)])
    c = Chamber.from_points(pts, name=name)
    return c


# ----------------------------------------------------------------------------
# Self-tests (run: python3 ray_billiard.py)
# ----------------------------------------------------------------------------
def _selftest() -> None:
    print("== ray_billiard self-tests ==")
    ok = True

    # T1: isotropic reflection is specular
    med_iso = Medium("isotropic")
    t = np.array([1.0, 0.0]); n = np.array([0.0, 1.0])
    k = np.array([0.3, -0.9]); K = 1.0
    kn = k / np.hypot(*k)                     # normalise onto |k| = K
    kr = reflect(kn, t, n, med_iso, K)
    spec_ok = bool(np.allclose(kr, np.array([kn[0], -kn[1]]), atol=1e-12))
    print(f"T1 isotropic specular: {'PASS' if spec_ok else 'FAIL'} "
          f"(k_in=({kn[0]:.3f},{kn[1]:.3f}) -> k_out=({kr[0]:.3f},{kr[1]:.3f}))")
    ok &= spec_ok

    # T2: hyperbolic reflection stays on the dispersion contour
    med_hyp = Medium("hyperbolic", eta=16.0)
    K = 1.0
    k0 = np.array([2.0, math.sqrt(K*K + 4.0/med_hyp.eta)])  # on contour, branch +
    # wall tilted 30 degrees
    th = math.radians(30)
    t = np.array([math.cos(th), math.sin(th)])
    n = np.array([-math.sin(th), math.cos(th)])
    if np.dot(n, np.array([0.0, -1.0])) < 0:
        n = -n
    kr = reflect(k0, t, n, med_hyp, K)
    F = kr[1]**2 - kr[0]**2/med_hyp.eta - K*K
    t_ok = abs(F) < 1e-9
    print(f"T2 dispersion conserved: {'PASS' if t_ok else 'FAIL'} (F={F:.2e})")
    ok &= t_ok

    # T3: kt conserved
    kt_ok = abs(np.dot(kr, t) - np.dot(k0, t)) < 1e-9
    print(f"T3 tangential k conserved: {'PASS' if kt_ok else 'FAIL'}")
    ok &= kt_ok

    # T4: group velocity leaves the wall (vg . n > 0)
    vg = med_hyp.group_velocity(kr)
    vg_ok = np.dot(vg, n) > 0
    print(f"T4 vg into chamber: {'PASS' if vg_ok else 'FAIL'}")
    ok &= vg_ok

    # T5: cone confinement
    ang_all = []
    for kx in np.linspace(-6, 6, 2001):
        ky = math.sqrt(K*K + kx*kx/med_hyp.eta)
        vg = med_hyp.group_velocity(np.array([kx, ky]))
        ang_all.append(abs(math.degrees(math.atan2(vg[0], vg[1]))))
    cone_ok = max(ang_all) <= math.degrees(med_hyp.cone_half_angle()) + 1e-6
    print(f"T5 cone confinement: {'PASS' if cone_ok else 'FAIL'} "
          f"(max deviation {max(ang_all):.4f} deg, alpha_max="
          f"{math.degrees(med_hyp.cone_half_angle()):.4f} deg)")
    ok &= cone_ok

    # T6: closed trapezoid chamber keeps rays inside for both media
    for med in [Medium("hyperbolic", eta=100.0), Medium("isotropic")]:
        ch = chamber_trapezoid()
        rng = np.random.default_rng(3)
        for _ in range(20):
            p0 = np.array([0.5 + 0.05*(rng.uniform()-0.5), 0.8])
            kx = rng.uniform(-3, 3)
            ky = math.sqrt(1.0 + kx*kx/med.eta) if med.kind == "hyperbolic" \
                else math.sqrt(max(1e-6, 1.0 - 0.5*kx*kx))
            k0 = np.array([kx, -ky if rng.uniform() > 0.5 else ky])
            res = propagate_ray(ch, med, p0, k0, 1.0, max_bounces=150)
            assert np.all(res.bounce_points[-1] >= -1e-9)
    print("T6 containment: PASS")

    # T7: anisotropic billiard in trapezoid develops closed loops (attractor)
    med = Medium("hyperbolic", eta=100.0)
    ch = chamber_trapezoid()
    rng = np.random.default_rng(11)
    n_loop = 0
    for _ in range(30):
        p0 = np.array([0.3 + 0.4 * rng.uniform(), 0.85])
        kx = rng.uniform(-1.5, 1.5)
        ky = math.sqrt(1.0 + kx * kx / med.eta)
        k0 = np.array([kx, -ky])  # launched downward
        res = propagate_ray(ch, med, p0, k0, 1.0, max_bounces=400)
        if res.closed_loop is not None:
            n_loop += 1
    print(f"T7 attractor loops found: {n_loop}/30 rays "
          f"{'PASS' if n_loop >= 20 else 'WARN/FAIL'}")
    ok &= n_loop >= 20
    print("== self-tests:", "ALL PASS" if ok else "SOME FAILED", "==")
    if not ok:
        raise SystemExit(1)


if __name__ == "__main__":
    _selftest()
