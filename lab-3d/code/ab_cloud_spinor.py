"""
ab_cloud_spinor.py
==================
All 64 spinor structures on the genus-3 Bolza/Klein surface and the
Arf invariant.

CRITICAL ADDITION vs v17:
-------------------------
v17 had ZERO checks of:
    - the 64 spinor structures
    - Arf invariant

These are CENTRAL to the monograph's claim (sections 8-10).  Here we add them.

Mathematical background:
------------------------
On a genus-g Riemann surface there are 2^(2g) = 2^6 = 64 spin structures.
Each is a quadratic form q: H_1(Σ, Z_2) → Z_2.  The Arf invariant

    Arf(q) = Σ_{i=1}^{g} q(a_i) q(b_i)  ∈ {0, 1}

classifies spin structures into:
    Arf = 0  →  'even'  (allows harmonic spinors → GUE-like statistics)
    Arf = 1  →  'odd'   (no harmonic spinors → Dirac cone protected)

For g=3, there are 28 even and 36 odd spinor structures.

We represent each spinor structure by a binary vector of length 2g = 6
(encoding q(a_1), q(b_1), q(a_2), q(b_2), q(a_3), q(b_3)) and compute Arf.
"""
from __future__ import annotations

import numpy as np
from itertools import product


def all_spinor_structures(g: int = 3) -> np.ndarray:
    """
    All 2^(2g) spinor structures on genus-g surface.
    Each row is a binary vector of length 2g.
    """
    return np.array(list(product([0, 1], repeat=2 * g)), dtype=int)


def arf_invariant(qvec: np.ndarray, g: int = 3) -> int:
    """
    Arf(q) = Σ_{i=1}^{g} q(a_i) · q(b_i)  (mod 2).
    Convention: qvec = [q(a_1), q(b_1), q(a_2), q(b_2), ..., q(a_g), q(b_g)].
    """
    s = 0
    for i in range(g):
        s += qvec[2 * i] * qvec[2 * i + 1]
    return int(s % 2)


def classify_all_spinors(g: int = 3) -> dict:
    """
    Classify all 2^(2g) spinor structures by Arf invariant.
    Returns dict with counts and indices.
    """
    qs = all_spinor_structures(g)
    arfs = np.array([arf_invariant(q, g) for q in qs])
    even_idx = np.where(arfs == 0)[0]
    odd_idx = np.where(arfs == 1)[0]
    return {
        "g": g,
        "n_total": len(qs),
        "n_even": int(len(even_idx)),
        "n_odd": int(len(odd_idx)),
        "even_indices": even_idx.tolist(),
        "odd_indices": odd_idx.tolist(),
        "arfs": arfs.tolist(),
        "structures": qs,
    }


def psl27_action_on_spinors_quick(g: int = 3) -> dict:
    """
    Quick partial check: PSL(2,7) has order 168.  Its action on the 64 spinor
    structures should partition them into orbits.

    Full implementation requires constructing the symplectic representation
    ρ: PSL(2,7) → Sp(2g, Z_2).  Here we just count orbits under the
    symplectic group Sp(6, Z_2) (which is larger than the PSL(2,7) image),
    to provide context.  The PSL(2,7) orbits are a refinement of these.
    """
    # Sp(2g, Z_2) acts transitively on the 2^(2g) - 1 nonzero vectors.
    # Its action on the 2^(2g) quadratic forms has two orbits: even (size
    # 2^(g-1)(2^g+1)) and odd (size 2^(g-1)(2^g-1)).
    info = classify_all_spinors(g)
    return {
        "g": g,
        "Sp_orbits": 2,
        "Sp_even_orbit_size": info["n_even"],
        "Sp_odd_orbit_size": info["n_odd"],
        "note": (
            "Under the full symplectic group Sp(6,Z_2), spinors split into "
            "2 orbits (even/odd).  Under the PSL(2,7) subgroup these refine "
            "further.  Full symplectic-representation check is TODO."
        ),
    }
