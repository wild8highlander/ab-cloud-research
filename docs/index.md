---
title: AB-Cloud Research
icon: material/home
---

# AB-Cloud — a phase resonator for the ζ zeros

The **AB-cloud** is a Hofstadter Hamiltonian decorated with topological
vortices whose Aharonov–Bohm phases are **derived from the non-trivial zeros
of the Riemann zeta function**. This repository is fully dedicated to that
single programme: monographs, the canonical 37-test Julia suite, an
independent 10-language verification stack, and a 3D lattice laboratory.

$$H\psi_n = \gamma_n \psi_n, \qquad \zeta(\tfrac12 + i\gamma_n) = 0$$

## Headline numbers (all traceable to named tests)

| Quantity | Value | Status |
|---|---|---|
| ⟨r⟩ vs GUE 0.5992 | **0.5848 ± 0.0260** | consistent (dev −2.4 %) |
| Montgomery KS (cloud vs ζ zeros) | **0.047** (p = 0.27, N = 500) | H₀ not rejected |
| Byers–Yang flux defect | **3.5·10⁻¹⁵** | machine precision |
| Connes self-duality | **4 zero modes**, C₁ = 2 | machine precision |
| Dirac dynamics | E_min ∝ 1/L, **R² = 0.9997** | confirmed |

!!! quote "Author"
    **Isaev Iskhak Khamzatovich** · ORCID
    [0009-0003-7299-0701](https://orcid.org/0009-0003-7299-0701) · DOI
    [10.5281/zenodo.21825394](https://doi.org/10.5281/zenodo.21825394)

## Where to go next

- :material-rocket-launch: [Quick start](quickstart.md) — run the suite in 5 minutes
- :material-book-open-variant: [Monographs](monographs.md) — 5 editions, 131 figures
- :material-test-tube: [Verification](verification.md) — 10 languages, 2M zeros
- :material-cube-outline: [3D laboratory](lab3d.md) — 36³ lattices with vortex lines
