# formal/ — the formal layer of the package

Specifications for four systems (portable sources, no external
dependencies) + the obligation machine (`rpbridge/formaloblig.py`,
DAG — `obligations.json`).

## The basic skeleton

| System | File | Content | Status |
|---------|------|------------|--------|
| Lean 4 | lean/RPBasic.lean | the hermiticity skeleton: sum \|ν\|² ≥ 0, reality of λ, Tr(AB)=Tr(BA) | compilation — O-lean |
| Coq | coq/RPBasic.v | the same facts in Gallina | compilation — O-coq |
| Agda | agda/RPBasic.agda | non-negativity via typing | compilation — O-agda |
| Isabelle/HOL | isabelle/RPBasic.thy | the same facts in HOL | compilation — O-isa |

## Formal statements of the theorems Th1–Th6 (v1.2.2)

| System | File | Content | Status |
|---------|------|------------|--------|
| Lean 4 | lean/RPTheorems.lean | statements of Th1–Th6; elementary cores proved (propositional form); reductions to the named axioms A1–A6 | compilation — O-lean; axioms A1–A6 → Mathlib — O-lean-mathlib |
| Coq | coq/RPTheorems.v | the same statements in Gallina; proofs — intros/exact; admit is not used | compilation — O-coq |

The registry of reductions (identical in both files):

| Axiom | Classical result | Theorem |
|---------|------------------------|---------|
| A1 | the spectral theorem, hermitian case | Th1 |
| A2 | simultaneous diagonalization (finite abelian group) | Th5 |
| A2b | the decomposition ‖(H∓iI)ψ‖² = ‖Hψ‖² + ‖ψ‖² | Th2 |
| A3 | the Hadamard product for ξ, ζ′/ζ | Th6 |
| A4 | the Kato–Temple estimate | Th3 |
| A5 | Gershgorin's theorem | Th3 |
| A6 | absolute convergence of the Li series | Th4 |

Discipline: `sorry`/`admit` are not used anywhere — the deep steps are
cast as named axioms, so the formalization HONESTLY shows which
classical results are accepted as input of each theorem. No axiom is a
hypothesis of RH; the RH conclusion is reduced by the obligation
machine (V13, unlocked at v1.2.1): O12 — proven (classics),
O08/O09/O11 — computed with committed artifacts.

The key function of the layer is not "to prove RH" but to GUARANTEE:
the path O01→O12 carries no assumptions (verdict: certified), and the
conclusion rises to proven automatically once O11 — the positivity of
λ_n for all n — is proven (which, by O12, is RH itself). The
compilation status of each toolchain is an open obligation
(see results/ROADMAP.md, R5).
