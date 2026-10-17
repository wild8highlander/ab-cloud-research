# Th2. Finite-dimensional self-adjointness — theorem derivation

**Campaign:** V8 · **Formal reduction:** A2b (decay of the defect norm) · **Documents:**
`theorem_th2_{ru,en}.{pdf,docx}` ·
**Figure:** `figures/th2_4dim_ru.png`, `figures/th2_4dim_en.png`
(2×2 tile, four dimensions, 600 dpi)

## Statement

A symmetric operator on ℂ^N is essentially self-adjoint: defect indices (0, 0); e^{−iHt} is unitary; Im⟨ψ, Hψ⟩ = 0.

## Proof idea

On ℂ^N every symmetric bounded operator is self-adjoint. Key estimate: ‖(H ∓ iI)ψ‖² = ‖Hψ‖² + ‖ψ‖² ≥ ‖ψ‖² > 0 — the cross term vanishes by the symmetry of H, hence ker(H* ∓ iI) are empty. Consequences: a real spectrum, a unitary e^{−iHt}, a real form.

## The four dimensions of the figure

a) defect indices n+/n− across L = 12/16/24/32 — all zero; b) the smallest singular value of H−iI ≈ 1.0 across L; c) the unitarity drift 2.2e−16 and Im⟨ψ,Hψ⟩ = 0 against the 1e−12 threshold; d) spectrum shifts under a boundary change (open/torus, 4 twists) for L12/L24 — finite and decaying with L.

## Campaign certificate and artifacts

test_th2_selfadjoint.py (defects, unitarity, form realness); computations/V08_self_adjoint/; claim_v08.json

## Boundaries (honest)

The theorem is finite-dimensional; the transfer to L → ∞ requires essential-spectrum estimates — open obligation O03.
