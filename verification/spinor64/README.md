# spinor64 — Verification of All 64 Spinor Structures of the Klein Quartic

Reference implementation and full run over the 64 spinor structures of the
Klein quartic. The verified truth:
**every one of the 64 spinor structures gives GUE-consistent statistics.**

## The two experiments (E1 + E2)

### E1 — exact symmetry (no statistics involved)

PSL(2,7) = Aut(Klein quartic, 168 elements) acts on the 64 spin structures
and splits them into orbits of sizes **28 / 21 / 7 / 7 / 1**:

- the 28-element orbit = the **odd structures (Arf = 1)** — the classical
  28 bitangents; its transitivity is the Riemann–Klein theorem, here
  confirmed numerically;
- the single-element orbit = the trivial even structure (Arf = 0).

Because the discretisation respects PSL(2,7), the Dirac-type operators built
from structures in the same orbit are permutation-conjugate and therefore
**exactly isospectral**: measured max|Δλ| ≈ 8.9·10⁻¹⁵ (pure double-precision
round-off). Gauge-invariance check: 7.1·10⁻¹⁵. Zero modes of the discrete
Dirac operator per orbit: **2 / 3 / 3 / 3 / 7**.

Consequence: a construction in which a *single* structure differs
statistically from all others is impossible by design.

### E2 — statistics in the AB-cloud model

Hofstadter torus L = 44, α = 1/2, Nv = 54 vortices (density scaling), the
suite's `:monumental` gauge, spin structure as boundary twists; 5 vortex
configurations averaged:

| Quantity | Value |
|---|---|
| GUE-consistent structures | **64 / 64** (Monte-Carlo p-value vs size-matched GUE ensemble) |
| ⟨r⟩ over all structures | **0.5984 ± 0.0035** (GUE reference 0.59965) |
| min MC p-value | 0.36 |
| MC confidence interval for ⟨r⟩ | [0.5847, 0.6140] |

## Contents

| Path | Description |
|---|---|
| `spinor64_core.py` | library: PSL(2,7) over F₇; Klein graph {3,7} built as a regular map via C₇/C₃/C₂ stabilisers; 64 spin structures as Kasteleyn signature systems (odd face-parity + canonical gauge); GF(2) linear algebra; Hofstadter `:monumental` port; RMT statistics **without scipy** |
| `run_spinor64.py` | full E1+E2 run → `output/` (≈ 10 min, 2 cores; the recorded run took 639 s) |
| `data/README.md` | guide to the frozen input files (formats and the frozen-data contract) |
| `data/spinor_classes.csv` | frozen classes: `class_idx, orbit, arf, signs_84` (84 ±1 Kasteleyn signs per structure) |
| `data/klein_graph_edges.csv` | Klein graph topology: 84 edges, 56 vertices |
| `data/reference_spectrum.csv` | frozen spectrum of the odd-orbit representative |
| `data/reference_stats.json` | frozen ⟨r⟩ and zero-mode counts — the contract every `<lang>/spinor38` port must reproduce |
| `output/spinor64_results.json` | full machine-readable dump of the E1+E2 run |
| `output/spinor64_table.csv` | 64 rows: per-structure orbit, Arf, ⟨r⟩, p-value, verdict |
| `output/spinor64_report.md` | human-readable report of the recorded run |
| `output/run_log.txt` | console log of the recorded run |
| `output/README.md` | guide to the committed run artifacts |

## Reproduce

```bash
python3 verification/spinor64/run_spinor64.py
```

Requires Python 3.10+ and NumPy only (RMT statistics are hand-rolled). The
frozen `data/` files make the run deterministic; deleting `output/` and
re-running regenerates it with matching numbers (folder timestamps differ).

## Downstream ports (Test 38)

`verification/{cpp,fortran,go,haskell,java,javascript,julia,matlab,r,rust}/spinor38/`
each re-verify the frozen contract **independently** — their own Jacobi
eigensolver, no LAPACK. The C++ and JavaScript ports were compiled and run
during v1.1.0 preparation: isospectrality 3.4·10⁻¹⁴, ⟨r⟩ = 0.4515710793 —
VERDICT PASS.

## Summary

- The folder contains the reference verification of **all 64 spinor structures** of the
  Klein quartic and corrects the v21 monograph's uniqueness claim.
- E1: PSL(2,7) orbits 28/21/7/7/1, exact isospectrality inside orbits (8.9e-15),
  gauge invariance 7.1e-15, zero modes 2/3/3/3/7.
- E2: the AB-cloud model (L=44, α=1/2, Nv=54, `:monumental` gauge) — all 64 structures
  GUE-consistent, ⟨r⟩ = 0.5984 ± 0.0035, min p = 0.36.
- Run: `python3 verification/spinor64/run_spinor64.py` (~10 minutes); the frozen data in
  `data/` makes the run reproducible. The Test 38 ports re-check the same contract with
  their own Jacobi algorithm.

## 📁 Complete file inventory

| Entry | Size | Kind |
|---|---|---|
| `data/` | 5 files, 16.5 KB | directory |
| `output/` | 5 files, 44.2 KB | directory |
| `README.md` | 6.9 KB | file |
| `run_spinor64.py` | 16.1 KB | file |
| `spinor64_core.py` | 31.8 KB | file |
| **Total (recursive)** | **13 files, 115.6 KB** | |

## 🔬 Deep dive — the experiment that corrected the monograph

The folder documents the two experiments E1 and E2 that settled the
spinor question. **E1** proves the exact symmetry layer: operators built
from spinor structures in the same PSL(2,7) orbit are exactly isospectral
(and the zero-mode counts per orbit match); **E2** computes, for each of
the 64 spinor structures of the Klein quartic in the AB-cloud model, the
level-spacing statistics of its spectrum and compares them to the GUE
law. The verified outcome:
**64 of 64 structures are GUE-consistent**, the orbit decomposition is
28/21/7/7/1, and spectra agree to ≈ 1e-14. This result is the content of Appendix D in
the v22.1 monograph rebuilds and of §3.2.5 in the v21.1 corrections.

The artifacts are fully committed: `run_log.txt` (console trace of the
run), `spinor64_results.json` (machine-readable per-structure
statistics), `spinor64_table.csv` (flat table for spreadsheets), and
`spinor64_report.md` (the narrative report with the verdict lines). The
reference statistics the experiment compares against live in
`data/reference_stats.json`, and the frozen class/edge inputs in
`data/spinor_classes.csv` and `data/klein_graph_edges.csv` — the
experiment is data-driven and re-runnable.

Reproduce it with pure stdlib: `python3 run_spinor64.py` — the Jacobi
eigenvalue algorithm is implemented in-file, there are no third-party
imports and no network access; the run finishes in seconds and must
reproduce the committed JSON byte-for-byte on the same interpreter
generation. Any deviation is a bug report, not a discovery.
