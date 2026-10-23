# Th6. The Guinand–Weil trace formula — theorem derivation

> **🧭 Navigation:** [theorems_lemmas/](../README.md) · [AB_Cloud_Quantum_Research/](../../README.md) · [Root README](../../../README.md)

**Campaign:** V7 · **Formal reduction:** A3 (Hadamard product) · **Documents:**
`theorem_th6_{ru,en}.{pdf,docx}` ·
**Figure:** `figures/th6_4dim_ru.png`, `figures/th6_4dim_en.png`
(2×2 tile, four dimensions, 600 dpi)

## Statement

Q(a) = Σ_{γ>0} 2a/(a²+γ²) = ζ′/ζ(½+a) + 1/(½+a) + 1/(a−½) − ½ln π + ½ψ(¼+a/2) − B − C₀, where B = ½ln(4π) − 1 − γ/2, C₀ = −B; and K(x) = Tr e^{−xH_ξ} = (1/π)∫₀^∞ Q(a)·sin(ax) da.

## Proof idea

The logarithmic derivative of the Hadamard product of ξ(s) gives the sum over the zeros; the explicit pole terms (the ζ pole at s = 1, the functional equation at s = ½, the Γ-factor via ψ) assemble into the constants B and C₀ (re-derived — the parent-repository erratum fixed). The representation 2a/(a²+γ²) = 2∫e^{−γt} sin(at) dt and the exchange of the integration order give K(x); at a > ½ the series ζ′/ζ carries the weight Λ(n)/√n into the trace.

## The four dimensions of the figure

a) the arithmetic of the constants: |B−C₀| = 2.5e−10 and M0(Q) (log); b) the trace of H_ξ ↔ primes: r = 0.9996, the residual 0.027; c) the lattice gates: r_EF per gate (the mean 0.76); d) the H_ξ vs lattice contrast — the prime comb lives only in the trace of H_ξ.

## Campaign certificate and artifacts

test_th6_trace_formula.py; computations/V07_arithmetic_trace/; claim_v07.json

## Boundaries (honest)

The "working operator" reference is YES for H_ξ, NO for the lattice gates (hypothesis A: class A is confirmed, the architectural link of the gates to ζ — no); the constants are verified by the a → 0+ asymptotics.

---

<!-- enriched-r3 -->

This folder is the derivation shell of **Th6 · trace formula** — one of the six theorem tiles of the AB Cloud Quantum Research study. It keeps the bilingual derivation monographs (RU/EN, PDF + DOCX), each built around the 2×2 measurement figure. The certificate quoted by the theorem layer for this tile: **r = 0.9996**; the machine-readable statement and thresholds live in [`_json/`](../_json/README.md). The derivation narrative below is the source the documents render.

```mermaid
flowchart LR
    T1["Th1 · Hermiticity"] --> T2["Th2 · self-adjointness"] --> T3["Th3 · Kato corridors"] --> T4["Th4 · Li formula"] --> T5["Th5 · block reduction"] --> T6["Th6 · trace formula"]
    style T6 fill:#1f6feb,color:#fff
```

*The theorem chain Th1–Th6 — the highlighted node is this tile; certificates in the theorem-layer table.*

## Folder contents

| File | Size | What it is |
|---|---|---|
| `theorem_th6_en.docx` | 463 KB | Word document |
| `theorem_th6_en.pdf` | 928 KB | PDF document |
| `theorem_th6_ru.docx` | 480 KB | Word document |
| `theorem_th6_ru.pdf` | 969 KB | PDF document |

**Subfolders:** `figures/`


**Where next:** [machine-readable JSON](../_json/README.md)
