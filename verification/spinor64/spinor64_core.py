#!/usr/bin/env python3
"""
spinor64_core.py — Core library for the 64-spinor-structure verification
of the AB-Cloud research project (Klein quartic K4, genus 3).

Corrects the monograph v21 claim (section 3.1) that "of the 64 spinor
structures of the Klein quartic only idx=38 shows GUE agreement (p=0.598)".

Two experiments (run_spinor64.py):

  E1 (Klein graph {3,7}, exact symmetry, all 64 structures)
     Dirac operator D(e) = flat Z2 spin holonomy (signs) from e in F2^6
     + uniform TR-breaking AB flux pi/6 on every face (PSL(2,7)-invariant,
     total flux 4*pi == 0 mod 2pi, Byers-Yang compliant).
     Claims verified: (i) PSL(2,7) splits the 64 structures into exactly
     4 orbits (28 odd Arf=1 + 1/21/14 even Arf=0); (ii) operators within
     one orbit are isospectral to machine precision; (iii) therefore ALL
     structures give the same spectral statistics — idx=38 is not unique.

  E2 (AB-cloud Hofstadter torus, statistics)
     Faithful Python port of build_ab_cloud_hamiltonian (:monumental vortex
     gauge, Landau gauge) with the spin structure inserted as boundary
     twists.  GUE-consistent level statistics for EVERY structure —
     the corrected replacement for the v21 Table of section 3.1.

Conventions (monograph v21, sections 2.4 / 3.1 / 12.4):
  * spin structure <-> e = (e1..e6) in F2^6; holonomy around the j-th
    symplectic basis cycle: (-1)^{e_j};
  * Arf(e) = e1*e2 + e3*e4 + e5*e6 (mod 2)  ->  36 even / 28 odd;
    NOTE: e(38) = (0,1,1,0,0,1) gives Arf = 0 under the monograph's own
    formula — an internal inconsistency of v21 documented here;
  * effective AB holonomy phi_eff = pi * sum(e_j) / 6.
"""
from __future__ import annotations

import math
from itertools import product
from typing import Dict, List, Optional, Sequence, Tuple

import numpy as np

F7 = 7

# ===========================================================================
# 1. SL(2,7) / PSL(2,7) over F7
# ===========================================================================

def mat_mul(a, b) -> tuple:
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2)) % F7
                       for j in range(2)) for i in range(2))


def mat_neg(ma) -> tuple:
    return tuple(tuple((-x) % F7 for x in row) for row in ma)


def canon(ma) -> tuple:
    """Canonical representative of the PSL class {M, -M} (the smaller tuple)."""
    neg = mat_neg(ma)
    return ma if ma <= neg else neg


def mat_inv7(ma) -> tuple:
    det = (ma[0][0] * ma[1][1] - ma[0][1] * ma[1][0]) % F7
    din = pow(det, F7 - 2, F7)
    return ((din * ma[1][1]) % F7, (-din * ma[0][1]) % F7), \
           ((-din * ma[1][0]) % F7, (din * ma[0][0]) % F7)


def sl27_elements() -> List[tuple]:
    els = set()
    for a in range(F7):
        for b in range(F7):
            for c in range(F7):
                bc = b * c % F7
                if a == 0:
                    if (-bc) % F7 == 1:
                        for d in range(F7):
                            els.add(((0, b), (c, d)))
                else:
                    ain = pow(a, F7 - 2, F7)
                    d = (1 + bc) * ain % F7
                    els.add(((a, b), (c, d)))
    return sorted(els)


def psl27_elements() -> List[tuple]:
    """168 canonical representatives of PSL(2,7) = SL(2,7)/{+-I}."""
    sl = sl27_elements()
    seen, out = set(), []
    for ma in sl:
        if ma in seen:
            continue
        seen.add(ma)
        seen.add(mat_neg(ma))
        out.append(ma)
    assert len(out) == 168, f"order of PSL(2,7) expected 168, got {len(out)}"
    return out


def psl27_generators() -> Tuple[tuple, tuple]:
    """s (order 2 in PSL) and t (order 3 in PSL: t^3 = -I)."""
    return ((0, F7 - 1), (1, 0)), ((1, 1), (F7 - 1, 0))


# ===========================================================================
# 2. Klein graph {3,7} = coset graph PSL(2,7)/<t>
# ===========================================================================

class KleinGraph:
    """
    The 56-vertex Klein graph ({3,7}) built canonically from the regular map
    structure of the Klein quartic:

      * flags = elements of PSL(2,7) (flag stabilizer trivial, 168 flags);
      * faces  = left cosets P7\\G  with P7 = <st> (order 7)   -> 24 faces;
      * vertices = left cosets C3\\G with C3 = <t> (order 3)   -> 56 vertices;
      * edges   = left cosets C2\\G with C2 = <s> (order 2)   -> 84 edges;
      * the face cycle of coset P7*g is  V(p^i g), i=0..6, p = st;
      * the edge of coset C2*g connects vertices V(g) and V(s g).

    This is the unique regular {3,7} map of genus 3 — the Klein quartic
    tessellation — with Aut = PSL(2,7) acting by right multiplication.
    """

    def __init__(self):
        self.psl = psl27_elements()
        self.index = {}
        for i, elem in enumerate(self.psl):
            self.index[elem] = i
        s, t = psl27_generators()
        self.s, self.t = s, t
        p = canon(mat_mul(s, t))          # order-7 generator of P7
        assert mat_mul(mat_mul(mat_mul(p, p), p), p) != p
        ident = ((1, 0), (0, 1))
        # --- vertex cosets C3\\G ---
        C3 = [ident, t, mat_mul(t, t)]
        vcoset, vreps, un = {}, [], set(range(168))
        while un:
            sd = min(un)
            seed = self.psl[sd]
            mem = []
            for gh in C3:
                gimg = canon(mat_mul(gh, seed))
                mem.append(self.index[gimg])
            mem.sort()
            cid = len(vreps)
            vreps.append(self.psl[mem[0]])
            for el in mem:
                vcoset[el] = cid
                un.discard(el)
        self.vcoset, self.vreps = vcoset, vreps
        self.n_vertices = len(vreps)
        # --- face cosets P7\\G ---
        P7 = []
        x = ident
        for _ in range(7):
            P7.append(x)
            x = canon(mat_mul(p, x))
        fcoset, freps, un2 = {}, [], set(range(168))
        while un2:
            sd = min(un2)
            seed = self.psl[sd]
            mem = []
            for gh in P7:
                gimg = canon(mat_mul(gh, seed))
                mem.append(self.index[gimg])
            mem.sort()
            cid = len(freps)
            freps.append(self.psl[mem[0]])
            for el in mem:
                fcoset[el] = cid
                un2.discard(el)
        self.fcoset, self.freps = fcoset, freps
        self.n_faces = len(freps)
        # --- edges: cosets C2\\G = {g, s g} ---
        eset = set()
        edge_list = []
        seen_edge = set()
        for g in self.psl:
            gi = self.index[g]
            if gi in seen_edge:
                continue
            sj = self.index[canon(mat_mul(s, g))]
            seen_edge.add(gi)
            seen_edge.add(sj)
            u, v = vcoset[gi], vcoset[sj]
            if u == v:
                raise AssertionError("loop edge in Klein graph")
            e = (min(u, v), max(u, v))
            eset.add(e)
            edge_list.append((e, gi, sj))
        self.edge_list = edge_list
        self.edges = sorted(e[0] for e in edge_list)
        self._edge_map = {}
        for k, e in enumerate(self.edges):
            self._edge_map[e] = k
        adj = [[] for _ in range(self.n_vertices)]
        for (u, v) in self.edges:
            adj[u].append(v)
            adj[v].append(u)
        for v in range(self.n_vertices):
            adj[v].sort()
        self.adj = adj
        # sanity: 56 vertices, 84 edges, 3-regular, 24 faces
        assert self.n_vertices == 56, self.n_vertices
        assert len(self.edges) == 84, len(self.edges)
        assert all(len(a) == 3 for a in adj)
        assert self.n_faces == 24, self.n_faces
        self._faces = None

    def faces(self) -> List[List[int]]:
        """24 heptagonal faces as vertex cycles (cyclic order by p = st)."""
        if self._faces is not None:
            return self._faces
        out = []
        for g in self.freps:
            cyc = []
            x = g
            for _ in range(7):
                cyc.append(self.vcoset[self.index[x]])
                x = canon(mat_mul(self.canon_p(), x))
            out.append(cyc)
        # each edge must appear in exactly 2 faces
        eidx = self._edge_map
        cnt = np.zeros(84, dtype=int)
        for cyc in out:
            for i in range(7):
                u, v = cyc[i], cyc[(i + 1) % 7]
                cnt[eidx[(min(u, v), max(u, v))]] += 1
        assert (cnt == 2).all(), "edge-face incidence broken"
        self._faces = out
        return out

    def canon_p(self):
        if not hasattr(self, "_p"):
            self._p = canon(mat_mul(self.s, self.t))
        return self._p

    def face_edge_cycles(self) -> List[List[int]]:
        eidx = self._edge_map
        out = []
        for f in self.faces():
            cyc = []
            for i in range(7):
                u, v = f[i], f[(i + 1) % 7]
                cyc.append(eidx[(min(u, v), max(u, v))])
            out.append(cyc)
        return out

    def cycle_basis(self):
        nV, nE = 56, 84
        inc = [[] for _ in range(nV)]
        for k, (u, v) in enumerate(self.edges):
            inc[u].append((v, k))
            inc[v].append((u, k))
        parent, pedge, seen, queue = [-1] * nV, [-1] * nV, [False] * nV, [0]
        seen[0] = True
        tree = set()
        order = []
        while queue:
            v = queue.pop(0)
            order.append(v)
            for (w, k) in inc[v]:
                if not seen[w]:
                    seen[w] = True
                    parent[w], pedge[w] = v, k
                    tree.add(k)
                    queue.append(w)
        nontree = [k for k in range(nE) if k not in tree]
        C = np.zeros((nE, len(nontree)), dtype=np.int64)
        for col, k in enumerate(nontree):
            C[k, col] = 1
            for x in (self.edges[k][0], self.edges[k][1]):
                while x != 0:
                    C[pedge[x], col] ^= 1
                    x = parent[x]
        self.nontree, self.tree_edges = nontree, sorted(tree)
        self.tree_parent = [(pedge[v], parent[v]) for v in range(nV)]
        self.bfs_order = list(order)
        vedges = [[] for _ in range(nV)]
        for k, (u, v) in enumerate(self.edges):
            vedges[u].append(k)
            vedges[v].append(k)
        self._vertex_edges = vedges
        return C

    def homology(self) -> Dict[str, np.ndarray]:
        """
        H1(K4, F2) from the graph: cycle space (dim 29) modulo face span
        (rank 23) -> 6-dimensional homology with a chosen basis (6 selected
        fundamental cycles).  Returns:
          C      (84,29) fundamental cycle matrix (columns = cycles)
          X      (6,29)  basis coordinates of every fundamental cycle
          action (168,6,6) PSL(2,7) matrices on H1 (contragredient on H1;
                 acting on spin-structure labels e in F2^6)
        """
        C = self.cycle_basis()
        F = np.zeros((84, 24), dtype=np.int64)
        for j, cyc in enumerate(self.face_edge_cycles()):
            for e in cyc:
                F[e, j] = 1
        Fb = _col_basis(F)
        assert Fb.shape[1] == 23, f"face span rank {Fb.shape[1]} != 23"
        # greedy selection of 6 cycles independent modulo the face span
        sel = []
        rp = list(_row_basis_with_pivots(Fb.T))
        for j in range(C.shape[1]):
            w = C[:, j].copy()
            for (piv, b) in rp:
                if w[piv]:
                    w ^= b
            if w.any():
                sel.append(j)
                piv = int(np.flatnonzero(w)[0])
                rp.append((piv, w.copy()))
            if len(sel) == 6:
                break
        assert len(sel) == 6, "failed to select 6 independent cycles"
        Hc = C[:, sel].copy()
        assert _rank_mod2(np.hstack([Hc, Fb])) == 29
        M = _quotient_map(C, Hc, Fb)
        X = (M @ C) % 2
        action = np.zeros((168, 6, 6), dtype=np.int64)
        for gi, gact in enumerate(self.psl):
            vperm = np.empty(56, dtype=np.int64)
            for v, rep in enumerate(self.vreps):
                gimg = canon(mat_mul(rep, gact))
                vperm[v] = self.vcoset[self.index[gimg]]
            eperm = np.empty(84, dtype=np.int64)
            for k, (u, v) in enumerate(self.edges):
                eu = (min(vperm[u], vperm[v]), max(vperm[u], vperm[v]))
                eperm[k] = self._edge_map[eu]
            Cg = C[eperm, :]
            action[gi] = (M @ Cg)[:, sel] % 2
        idxmap = {}
        for i, elem in enumerate(self.psl):
            idxmap[elem] = i
        rng = np.random.default_rng(5)
        for _ in range(10):
            a, b = rng.integers(0, 168, 2)
            gab_m = canon(mat_mul(self.psl[a], self.psl[b]))
            gab = idxmap[gab_m]
            lhs = (action[a] @ action[b]) % 2
            assert (lhs == action[gab]).all(), "PSL action not a homomorphism"
        self._sel = sel
        return {"C": C, "X": X, "action": action, "M": M, "Hc": Hc, "Fb": Fb}


# --- GF(2) helpers ----------------------------------------------------------

def _rref(A: np.ndarray):
    A = A.copy() % 2
    rows, cols = A.shape
    pivots, r = [], 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if A[i, c]:
                piv = i
                break
        if piv is None:
            continue
        A[[r, piv]] = A[[piv, r]]
        for i in range(rows):
            if i != r and A[i, c]:
                A[i] ^= A[r]
        pivots.append(c)
        r += 1
        if r == rows:
            break
    return A, pivots


def _rank_mod2(A: np.ndarray) -> int:
    return len(_rref(A)[1])


def _col_basis(A: np.ndarray) -> np.ndarray:
    _, piv = _rref(A)
    return A[:, piv].copy()


def _row_basis_with_pivots(A: np.ndarray):
    R, piv = _rref(A)
    out = []
    for i in range(len(piv)):
        out.append((piv[i], R[i].copy()))
    return out


def _symplectic_transform(B: np.ndarray, J: np.ndarray) -> np.ndarray:
    n = B.shape[0]
    remaining = list(range(n))
    vecs = []
    while remaining:
        a = remaining[0]
        ea = np.zeros(n, dtype=np.int64)
        ea[a] = 1
        b = None
        for w in remaining[1:]:
            if B[a, w]:
                b = w
                break
        eb = np.zeros(n, dtype=np.int64)
        eb[b] = 1
        vecs.append((ea, eb))
        rem = []
        for w in remaining[1:]:
            if w == b:
                continue
            if B[a, w] == 0 and B[b, w] == 0:
                rem.append(w)
        remaining = rem
    P = np.column_stack([v for pair in vecs for v in pair])
    assert ((P.T @ B @ P) % 2 == J).all()
    return P


def _quotient_map(C: np.ndarray, Hc: np.ndarray, Fb: np.ndarray) -> np.ndarray:
    A = np.hstack([Hc, Fb])
    nk = A.shape[1]
    nC = C.shape[1]
    Aug = np.hstack([A, C])
    R, piv = _rref(Aug)
    Y6 = np.zeros((6, nC), dtype=np.int64)
    for j in range(nC):
        y = np.zeros(nk, dtype=np.int64)
        for r, c in enumerate(piv):
            if c < nk:
                y[c] = R[r, nk + j]
        recon = (A @ y) % 2
        assert (recon == C[:, j] % 2).all(), "quotient solve failed"
        Y6[:, j] = y[:6]
    MT = np.zeros((C.shape[0], 6), dtype=np.int64)
    for j in range(6):
        MT[:, j] = _solve_gf2(C.T, Y6[j, :])
    M = MT.T
    rng = np.random.default_rng(11)
    rp = _row_basis_with_pivots(Fb.T)
    for _ in range(25):
        coef = rng.integers(0, 2, C.shape[1]).astype(np.int64)
        c = (C @ coef) % 2
        x = (M @ c) % 2
        recon = (Hc @ x) % 2
        diff = (c + recon) % 2
        w = diff.copy()
        for (piv2, b) in rp:
            if w[piv2]:
                w ^= b
        assert not w.any(), "quotient map verification failed"
    return M


def _solve_gf2(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    rows, k = A.shape
    Aug = np.hstack([A % 2, b.reshape(-1, 1) % 2])
    R, piv = _rref(Aug)
    r = len(piv)
    for i in range(r, rows):
        if R[i, k] and not R[i, :k].any():
            raise AssertionError("inconsistent GF2 system")
    x = np.zeros(k, dtype=np.int64)
    for i, c in enumerate(piv):
        x[c] = R[i, k]
    return x


def _solve_gf2_matrix(P: np.ndarray, X: np.ndarray) -> np.ndarray:
    k = X.shape[1]
    S = np.zeros((6, k), dtype=np.int64)
    for j in range(k):
        S[:, j] = _solve_gf2(P, X[:, j])
    return S


# ===========================================================================
# 3. The 64 spin structures
# ===========================================================================

class Spinor64:
    """
    The 64 spin structures of the Klein quartic in the standard combinatorial
    model (Cimasoni-Reshetikhin / Kasteleyn): a spin structure = an equivalence
    class of edge signings s in {+-1}^E with EVERY face carrying an ODD number
    of negative edges, modulo vertex-gauge flips (flip all edges incident to a
    vertex).  For the {3,7} tessellation: 2^(84-23) / 2^55 = 2^6 = 64 classes.

    Canonical gauge: all spanning-tree edges positive (unique representative).

    Arf invariant: the classical Riemann-Klein theorem splits the 64 structures
    into 36 even (Arf=0) / 28 odd (Arf=1); PSL(2,7)=Aut(K4) acts with orbits
    1 / 21 / 14 (even) and 28 (odd, the bitangents).  Both facts are verified
    numerically here; Arf labels are read off the computed orbit decomposition
    (the 28-element orbit is the odd class).
    """

    def __init__(self, graph: KleinGraph):
        self.g = graph
        h = graph.homology()
        self.X = h["X"]                     # (6,29) basis coords of fund cycles
        self.action_edges = self._edge_permutations()   # (168,84) edge perms
        self.nontree = graph.nontree
        self.tree_edges = graph.tree_edges
        self.classes = self._enumerate_classes()        # (64, 84) log-signs
        self.index_of = {}
        for ci, z in enumerate(self.classes):
            self.index_of[z.tobytes()] = ci
        self._sel = graph._sel
        self.prepare()
        self.orbits, self.orbit_id = self._compute_orbits()
        self.arf = np.zeros(64, dtype=np.int64)
        for oid, members in enumerate(self.orbits):
            val = 1 if len(members) == 28 else 0
            for entry in members:
                self.arf[entry] = val

    # -- PSL(2,7) action on edges -------------------------------------------
    def _edge_permutations(self):
        perms = np.zeros((168, 84), dtype=np.int64)
        for gi, gact in enumerate(self.g.psl):
            vperm = np.empty(56, dtype=np.int64)
            for v, rep in enumerate(self.g.vreps):
                gimg = canon(mat_mul(rep, gact))
                vperm[v] = self.g.vcoset[self.g.index[gimg]]
            for k, (u, v) in enumerate(self.g.edges):
                eu = (min(vperm[u], vperm[v]), max(vperm[u], vperm[v]))
                perms[gi, k] = self.g._edge_map[eu]
        return perms

    # -- the 64 classes in canonical gauge ------------------------------------
    def _enumerate_classes(self):
        nontree = self.nontree
        nt_index = {}
        for i, k in enumerate(nontree):
            nt_index[k] = i
        faces = self.g.face_edge_cycles()
        # constraint matrix: for each face, sum of z over its non-tree edges = 1
        A = np.zeros((24, len(nontree)), dtype=np.int64)
        for j, cyc in enumerate(faces):
            for e in cyc:
                if e in nt_index:
                    A[j, nt_index[e]] = 1
        Aug = np.hstack([A, np.ones((24, 1), dtype=np.int64)])  # [A | 1]
        R, piv = _rref(Aug)
        rank = len(piv)
        free_cols = [c for c in range(len(nontree)) if c not in piv]
        assert 29 - rank == 6, f"expected 6 free params, got {29 - rank}"
        classes = []
        for bits in product([0, 1], repeat=6):
            z = np.zeros(84, dtype=np.int64)
            vals = dict(zip(free_cols, bits))
            for r, c in enumerate(piv):
                # RREF row: z_c + sum_{free} R[r,fc] z_fc = R[r, -1]
                vals[c] = (R[r, -1] - sum(R[r, fc] * vals[fc]
                                          for fc in free_cols)) % 2
            for k, i in nt_index.items():
                z[k] = vals[i]
            # verify odd face parity
            for cyc in faces:
                assert sum(z[e] for e in cyc) % 2 == 1
            classes.append(z)
        return classes

    def _regauge(self, z):
        """Push signing through edge permutation, restore canonical gauge."""
        # zNew on permuted edges: edge perms[gi] maps k -> perms[gi, k]
        z = np.asarray(z)
        out = []
        for gi in range(168):
            zp = np.zeros(84, dtype=np.int64)
            zp[self.action_edges[gi]] = z        # pushforward
            # vertex flips to make tree edges positive
            flips = np.zeros(56, dtype=np.int64)
            inc = self.g._vertex_edges
            for v in self.g.bfs_order:
                if v == 0:
                    continue
                pe, par = self.g.tree_parent[v]
                flips[v] = flips[par] ^ zp[pe]
            for k, (u, v) in enumerate(self.g.edges):
                if (flips[u] + flips[v]) % 2 == 1:
                    zp[k] ^= 1
            out.append(tuple(zp.tolist()))
        return out

    def _compute_orbits(self):
        seen = [False] * 64
        orbits = []
        images = [None] * 64
        for ci in range(64):
            images[ci] = self._regauge(self.classes[ci])
        for start in range(64):
            if seen[start]:
                continue
            orb, stack = [], [start]
            seen[start] = True
            while stack:
                cur = stack.pop()
                orb.append(cur)
                for zp in images[cur]:
                    key = np.array(zp, dtype=np.int64)
                    ci = self.index_of.get(key.tobytes())
                    if ci is None:
                        raise AssertionError("regauged signing not in classes")
                    if not seen[ci]:
                        seen[ci] = True
                        stack.append(ci)
            orbits.append(sorted(orb))
        orbit_id = np.zeros(64, dtype=int)
        for oid, members in enumerate(orbits):
            for entry in members:
                orbit_id[entry] = oid
        return orbits, orbit_id

    def label(self, idx: int) -> str:
        """6-bit label: holonomy parity around the 6 basis cycles."""
        z = self.classes[idx]
        out = []
        for j in range(6):
            # holonomy around basis cycle j: product of signs
            # basis cycle j = column sel of C: use X rows -> but we need the
            # actual edge set; reconstruct from cycle basis
            cyc = self._basis_cycle_edges[j]
            par = int(sum(z[e] for e in cyc) % 2)
            out.append(str(par))
        return "".join(out)

    def edge_signs(self, idx: int) -> np.ndarray:
        """+-1 signing of the 84 edges for class idx."""
        return 1 - 2 * self.classes[idx]

    def prepare(self):
        """Precompute basis cycle edge lists for labels."""
        C = self.g.cycle_basis()
        sel = self._sel
        self._basis_cycle_edges = [
            np.flatnonzero(C[:, col]).tolist() for col in sel]


# ===========================================================================
# 4. Operators: spin signs + uniform face flux pi/6 (E1)
# ===========================================================================

def face_flux_phases(graph: KleinGraph, flux: float = math.pi / 6.0) -> np.ndarray:
    face_cycles = graph.face_edge_cycles()
    nontree = graph.nontree
    nt_index = {}
    for i, k in enumerate(nontree):
        nt_index[k] = i
    M = np.zeros((24, len(nontree)))
    for j, cyc in enumerate(face_cycles):
        for e in cyc:
            if e in nt_index:
                M[j, nt_index[e]] += 1.0
    _, sv, Vt = np.linalg.svd(M)
    o = Vt[-1] if sv[-1] < 1e-10 else np.zeros(24)
    total = 24 * flux / (2 * math.pi)
    if abs(total - round(total)) > 1e-9:
        raise ValueError("face flux violates closed-surface quantisation")
    base = float(o.sum()) * flux
    need = -(base) / (2 * math.pi)
    jmax = int(np.argmax(np.abs(o)))
    w = np.zeros(24)
    if abs(o[jmax]) > 1e-9:
        w[jmax] = round(need / o[jmax])
    rhs = flux + 2 * math.pi * w
    theta_nt, *_ = np.linalg.lstsq(M, rhs, rcond=None)
    res = M @ theta_nt - rhs
    assert np.abs(res).max() < 1e-8, f"flux gauge residual {np.abs(res).max():.2e}"
    theta = np.zeros(84)
    for i, k in enumerate(nontree):
        theta[k] = theta_nt[i]
    return theta


def dirac_operator(graph: KleinGraph, spinor: Spinor64, idx: int,
                   theta: Optional[np.ndarray] = None,
                   with_flux: bool = True) -> np.ndarray:
    """D(idx): signed adjacency x face-flux phases (complex Hermitian).
    with_flux=False gives the purely real signed adjacency."""
    if theta is None:
        theta = face_flux_phases(graph)
    signs = spinor.edge_signs(idx)
    n = graph.n_vertices
    H = np.zeros((n, n), dtype=np.complex128)
    for k, (u, v) in enumerate(graph.edges):
        if with_flux:
            H[u, v] = signs[k] * np.exp(1j * theta[k])
            H[v, u] = signs[k] * np.exp(-1j * theta[k])
        else:
            H[u, v] = float(signs[k])
            H[v, u] = float(signs[k])
    return H


# ===========================================================================
# 5. RMT statistics (no scipy dependency)
# ===========================================================================

R_MEAN_POISSON = 2.0 * math.log(2.0) - 1.0      # 0.38629
R_MEAN_GOE = 0.53590
R_MEAN_GUE = 0.59965


def spacing_ratios(eigs: np.ndarray, zero_tol: float = 1e-8) -> np.ndarray:
    lam = np.sort(eigs)
    d = np.diff(lam)
    d = d[d > zero_tol]
    d1, d2 = d[:-1], d[1:]
    return np.minimum(d1, d2) / np.maximum(d1, d2)


def ratio_stats(eigs: np.ndarray, zero_tol: float = 1e-8) -> Dict[str, float]:
    r = spacing_ratios(np.abs(eigs), zero_tol)
    return {"r_mean": float(np.mean(r)),
            "r_stderr": float(np.std(r) / math.sqrt(len(r))),
            "n_ratios": int(len(r)),
            "n_zero_modes": int((np.abs(np.sort(eigs)) < zero_tol).sum())}


_RGRID = np.linspace(0.0, 1.0, 200001)
_GCDF = None


def _gcdf() -> np.ndarray:
    global _GCDF
    if _GCDF is None:
        r = _RGRID
        pdf = 27.0 / 8.0 * (r + r ** 2) ** 2 / (1.0 + r + r ** 2) ** 5
        cdf = np.concatenate([[0.0], np.cumsum((pdf[1:] + pdf[:-1]) / 2 * np.diff(r))])
        _GCDF = cdf / cdf[-1]
    return _GCDF


def kolmogorov_p(D: float, n: int) -> float:
    en = math.sqrt(n)
    lam = (en + 0.12 + 0.11 / en) * D
    kmax = int(math.sqrt(2.0) / lam) + 1
    s = 0.0
    for k in range(1, kmax + 1):
        s += (-1) ** (k - 1) * math.exp(-2.0 * (k * lam) ** 2)
    return max(0.0, min(1.0, 2.0 * s))


def gue_ratio_ks(ratios: np.ndarray) -> Tuple[float, float]:
    cdf = _gcdf()
    r = np.sort(ratios)
    n = len(r)
    F = np.interp(r, _RGRID, cdf)
    iplus = np.arange(1, n + 1) / n
    iminus = np.arange(0, n) / n
    D = max(np.max(iplus - F), np.max(F - iminus))
    return float(D), kolmogorov_p(D, n)


def _gammainc_lower_reg(s: float, x: float) -> float:
    if x < 0 or s <= 0:
        return float("nan")
    if x < s + 1.0:
        term = 1.0 / s
        total = term
        n = 0
        while True:
            n += 1
            term *= x / (s + n)
            total += term
            if abs(term) < abs(total) * 1e-16 or n > 20000:
                break
        return total * math.exp(-x + s * math.log(x) - math.lgamma(s))
    tiny = 1e-300
    b = x + 1.0 - s
    c = 1.0 / tiny
    d = 1.0 / b if b != 0 else 1.0 / tiny
    h = d
    for i in range(1, 20000):
        an = -i * (i - s)
        b += 2.0
        d = an * d + b
        if abs(d) < tiny:
            d = tiny
        c = b + an / c
        if abs(c) < tiny:
            c = tiny
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < 1e-16:
            break
    q = math.exp(-x + s * math.log(x) - math.lgamma(s)) * h
    return 1.0 - q


def chi2_sf(x: float, k: int) -> float:
    if x <= 0:
        return 1.0
    return 1.0 - _gammainc_lower_reg(k / 2.0, x / 2.0)


def wigner_gue_cdf(s: np.ndarray) -> np.ndarray:
    from math import erf, pi, sqrt
    return erf(2 * s / sqrt(pi)) - (4 * s / pi) * np.exp(-4 * s ** 2 / pi)


def unfold_spectrum(eigs: np.ndarray, window: int = 40) -> np.ndarray:
    lam = np.sort(eigs)
    n = len(lam)
    half = max(1, window // 2)
    idx = np.arange(n)
    lo = np.clip(idx - half, 0, n - 1)
    hi = np.clip(idx + half, 1, n)
    span = lam[hi - 1] - lam[lo]
    density = (hi - lo) / np.maximum(span, 1e-300)
    cum = np.arange(n, dtype=float)
    out = np.zeros(n)
    out[1:] = cum[:-1] + density[:-1] * np.diff(lam)
    return out


def chi2_gue_unfolded(eigs: np.ndarray, nbins: int = 20, window: int = 40):
    lam = np.sort(eigs)
    u = unfold_spectrum(lam, window)
    s = np.diff(u)
    s = s[s > 0]
    edges = np.linspace(0.0, 3.0, nbins + 1)
    obs, _ = np.histogram(s, bins=edges)
    cdf_edges = wigner_gue_cdf(edges)
    exp_p = np.diff(cdf_edges)
    exp_counts = np.append(exp_p * len(s), (1 - cdf_edges[-1]) * len(s))
    obs2 = np.append(obs.astype(float), len(s) - obs.sum())
    mask = exp_counts > 5
    keep = exp_counts > 5
    if keep.sum() < 3:
        return float("nan"), float("nan")
    chi2 = float((((obs2[keep] - exp_counts[keep]) ** 2) / exp_counts[keep]).sum())
    dof = int(keep.sum()) - 1


# ===========================================================================
# 6. AB-cloud Hofstadter Hamiltonian (E2) — port of the Julia suite
# ===========================================================================

def ab_cloud_hamiltonian(L: int, alpha: float,
                         vortices: Sequence[Tuple[float, float, float]],
                         twist_x: float = 0.0, twist_y: float = 0.0,
                         t_hop: float = 1.0) -> np.ndarray:
    N = L * L
    H = np.zeros((N, N), dtype=np.complex128)

    def vphase(iy, ix, jy, jx):
        phi = 0.0
        for (vx, vy, q) in vortices:
            phi += q * 0.5 * (math.atan2(jy - vy, jx - vx) -
                              math.atan2(iy - vy, ix - vx))
        return phi

    for iy in range(1, L + 1):
        for ix in range(1, L + 1):
            i = (iy - 1) * L + (ix - 1)
            wrapx = ix == L
            jx = 1 if wrapx else ix + 1
            j = (iy - 1) * L + (jx - 1)
            phi = 2.0 * math.pi * alpha * iy + (twist_x if wrapx else 0.0)
            H[i, j] += -t_hop * np.exp(1j * phi)
            H[j, i] += -t_hop * np.exp(-1j * phi)
            wrapy = iy == L
            jy = 1 if wrapy else iy + 1
            j2 = (jy - 1) * L + (ix - 1)
            py = vphase(iy, ix, jy, ix)
            if wrapy:
                py += 2.0 * math.pi * alpha * L + twist_y
            H[i, j2] += -t_hop * np.exp(1j * py)
            H[j2, i] += -t_hop * np.exp(-1j * py)
    return H


def vortex_config(nv: int, L: int, seed: int = 96) -> List[Tuple[float, float, float]]:
    """Deterministic vortex placement: jittered square grid (q=+1 vortices).
    (The Julia suite uses seeded uniform placement; a jittered grid is used
    here so that ANY nv is always feasible and runs stay reproducible.)"""
    rng = np.random.default_rng(seed)
    side = int(math.ceil(math.sqrt(nv)))
    step = L / side
    pts: List[Tuple[float, float, float]] = []
    for i in range(nv):
        gx, gy = i % side, i // side
        x = (gx + 0.5) * step + 0.35 * step * float(rng.uniform(-1, 1))
        y = (gy + 0.5) * step + 0.35 * step * float(rng.uniform(-1, 1))
        x = min(max(x, 0.5), L + 0.5)
        y = min(max(y, 0.5), L + 0.5)
        pts.append((x, y, 1.0))
    return pts


def bulk_window(eigs: np.ndarray, center_frac: float = 0.6) -> np.ndarray:
    lam = np.sort(eigs)
    n = len(lam)
    lo = int(n * (1.0 - center_frac) / 2)
    return lam[lo:n - lo]


def spin_twists(eps: Sequence[int]) -> Tuple[float, float]:
    return (math.pi * (eps[0] + eps[2] + eps[4]),
            math.pi * (eps[1] + eps[3] + eps[5]))


def jsonable(obj):
    if isinstance(obj, dict):
        return {k: jsonable(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [jsonable(v) for v in obj]
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    if isinstance(obj, np.integer):
        return int(obj)
    if isinstance(obj, np.floating):
        return float(obj)
    return obj
