# spinor64 — Verification of All 64 Spinor Structures of the Klein Quartic

Reference implementation and full run that **corrected the v21 monograph**:
the claim that "only spinor structure idx=38 gives GUE-consistent statistics
(p = 0.598)" is withdrawn as a computational artifact. The verified truth:
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
statistically from all others is impossible by design — the v21 uniqueness
was a lattice artifact.

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

### Why v21 saw "uniqueness of idx=38"

1. A lattice artifact: correctly constructed operators are isospectral inside
   orbits, so a unique structure cannot exist (v21 itself called the effect a
   "Z₄ lattice artifact" in §3.2.3 — numerically confirmed here for all 64).
2. An internal contradiction: by the monograph's **own** formula
   Arf(ε) = ε₁ε₂ + ε₃ε₄ + ε₅ε₆, the vector ε(38) = (0,1,1,0,0,1) gives
   **Arf = 0**, not 1 as stated in v21 §3.2.1 and §12.4.

## Contents

| Path | Description |
|---|---|
| `spinor64_core.py` | library: PSL(2,7) over F₇; Klein graph {3,7} built as a regular map via C₇/C₃/C₂ stabilisers; 64 spin structures as Kasteleyn signature systems (odd face-parity + canonical gauge); GF(2) linear algebra; Hofstadter `:monumental` port; RMT statistics **without scipy** |
| `run_spinor64.py` | full E1+E2 run → `output/` (≈ 10 min, 2 cores; the recorded run took 639 s) |
| `data/spinor_classes.csv` | frozen classes: `class_idx, orbit, arf, signs_84` (84 ±1 Kasteleyn signs per structure) |
| `data/klein_graph_edges.csv` | Klein graph topology: 84 edges, 56 vertices |
| `data/reference_spectrum.csv` | frozen spectrum of the odd-orbit representative |
| `data/reference_stats.json` | frozen ⟨r⟩ and zero-mode counts — the contract every `<lang>/spinor38` port must reproduce |
| `output/spinor64_results.json` | full machine-readable dump of the E1+E2 run |
| `output/spinor64_table.csv` | 64 rows: per-structure orbit, Arf, ⟨r⟩, p-value, verdict |
| `output/spinor64_report.md` | human-readable report of the recorded run |
| `output/run_log.txt` | console log of the recorded run |

## Reproduce

```bash
python3 verification/spinor64/run_spinor64.py
```

Requires Python 3.10+ and NumPy only (RMT statistics are hand-rolled). The
frozen `data/` files make the run deterministic; deleting `output/` and
re-running regenerates it with matching numbers (folder timestamps differ).

## Downstream ports (Test 38)

`verification/{python,cpp,javascript,julia,rust,go,fortran,haskell,r,matlab}/spinor38/`
each re-verify the frozen contract **independently** — their own Jacobi
eigensolver, no LAPACK. The C++ and JavaScript ports were compiled and run
during v1.1.0 preparation: isospectrality 3.4·10⁻¹⁴, ⟨r⟩ = 0.4515710793 —
VERDICT PASS.

## Кратко (по-русски)

- Каталог содержит эталонную верификацию **всех 64 спинорных структур**
  квартики Клейна и исправляет утверждение монографии v21 об «уникальности
  idx=38» (снято как вычислительный артефакт).
- E1: орбиты PSL(2,7) 28/21/7/7/1, точная изоспектральность внутри орбит
  (8.9e-15), калибровочная инвариантность 7.1e-15, нулевые моды 2/3/3/3/7.
- E2: AB-облако (L=44, α=1/2, Nv=54, калибровка :monumental) — все 64
  структуры GUE-согласованы, ⟨r⟩ = 0.5984 ± 0.0035, min p = 0.36.
- Запуск: `python3 verification/spinor64/run_spinor64.py` (~10 минут);
  замороженные данные в `data/` делают прогон воспроизводимым.
- Порты Test 38 на 10 языках проверяют тот же контракт собственным
  алгоритмом Якоби.
