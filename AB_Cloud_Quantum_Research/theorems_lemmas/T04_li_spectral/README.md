# Th4. The spectral formula of the Li coefficients — theorem derivation

**Campaign:** V15 · **Formal reduction:** A6 (convergence of the Li series) · **Documents:**
`theorem_th4_{ru,en}.{pdf,docx}` ·
**Figure:** `figures/th4_4dim_ru.png`, `figures/th4_4dim_en.png`
(2×2 tile, four dimensions, 600 dpi)

## Statement

The Li coefficients admit the spectral form λ_n = Tr g_n(H_ξ), g_n(E) = 1 − (1 − 1/ρ(E))^n, ρ(E) = ½ − iE/2; the series converges absolutely; the two computational paths agree with |Δ| ≤ 4.4e−11 for n ≤ 3000.

## Proof idea

By definition λ_n = Σ_ρ [1 − (1 − 1/ρ)^n]; the bijection spec H_ξ ↔ the zero pairs {γ, −γ} turns the trace into a sum over pairs with the contributions O(n/γ²) — absolute convergence by Σ 1/γ². The poles of g_n sit at ρ = 1 (E = −i) — outside the real spectrum of H_ξ.

## The four dimensions of the figure

a) λ_n at n = 1/100/1000/3000 (log) with λ_min = 0.0231 > 0; b) the two-path agreement 4.4e−11 against the 1e−9 threshold; c) the certified tail ≤ 0.115; d) the control: the gate rank correlation −1.0 against r = 0.9996 for H_ξ.

## Campaign certificate and artifacts

test_th4_li.py; computations/V15_li_criterion/; claim_v15.json; the zero file zeta_zeros_50000_embedded.txt

## Boundaries (honest)

The positivity of λ_n is certified numerically up to n = 3000 (O11 — computed; tails ≤ 0.115); for all n the question is equivalent to RH by the classical Li/Bombieri–Lagarias criterion (O12 — proven). The path agreement depends on the tail model.
