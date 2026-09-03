# lab-3d/code — Simulation Sources (Python + Julia)

All source modules of the 3D laboratory. Every experiment is reachable from
the interactive menu of the main script, and every module can also be run or
imported standalone.

## Entry points

| File | Lines | Role |
|---|---|---|
| `ab_cloud_3d_en.py` | ~2009 | main solver, **English UI**, 10 modes A–J |
| `ab_cloud_3d.py` | ~2009 | main solver, Russian UI |
| `ab_cloud_3d_en.jl` | — | Julia original, English UI |
| `ab_cloud_3d.jl` | — | Julia original, Russian UI |
| `quick_start.py` | — | minimal end-to-end demo (one lattice, one spectrum, one figure) |

## Module map (by category)

| Category | Modules | Purpose |
|---|---|---|
| Hamiltonians | `ab_cloud_hamiltonian.py`, `ab_cloud_hamiltonian_v2.py` | AB-Cloud operator construction (flux, vortices, disorder, OBC) |
| RMT | `ab_cloud_zeta.py`, `ab_cloud_zeta_v2.py` | ζ-zero analysis: unfolding, ⟨r⟩, KS, Σ², Δ₃, K(τ) |
| Spinor / topology | `ab_cloud_spinor.py`, `ab_cloud_spinor_v2.py`, `ab_cloud_ktheory.py` | spinor fields, Arf invariant, K-theory invariants |
| Advanced 3D | `ab_cloud_advanced.py`, `ab_cloud_advanced_v2.py` | Chern marker, edge states, probability current, exceptional points |
| Statistics | `ab_cloud_stats.py`, `ab_cloud_stats_v2.py` | shared statistical utilities (bootstrap, permutation tests) |
| Sweeps | `ab_cloud_sweeps.py`, `ab_cloud_sweeps_v2.py` | parameter sweeps (α, σ grids), phase diagrams |
| PDE solvers | `nse3d_core.py`, `kdv_core.py`, `kp_solver.py` | 3D Navier–Stokes, KdV, Kadomtsev–Petviashvili side-experiments |
| RG | `polchinski_rg.py` | Polchinski renormalization-group flow |
| Isospectral | `isospectral_b.py`, `isospectral_b_en.py` | isospectral *b*-correction verification |
| FEM | `AB_Cloud_FEM_v6_python.py`, `AB_Cloud_FEM_v8c*.py`, `AB_Cloud_FEM_v8d*.py` | finite-element solvers (versions v6/v8c/v8d, RU/EN) |
| Vortex systems | `AB_Cloud_Vortex_System_v2.py`, `AB_Cloud_Vortex_System_v2_RU/EN.py`, `ab_cloud_vortex_*.py` | vortex lattice dynamics and searches |
| Verification | `verifier_core.py`, `monograph_verification*.py`, `run_verification*.py`, `AB_CLOUD_ALL_HYPOTHESES.py` | monograph hypothesis checks (parts 1–4), consolidated 11-hypothesis run |
| Extended studies | `ab_cloud_hybrid_approach*.py`, `ab_cloud_extended_kopt_study*.py`, `ab_cloud_genus_universality*.py`, `ab_cloud_robustness_study*.py`, `ab_cloud_jc_*.py`, `extended_solvers.py`, `large_matrix_demo.py` | kopt scans, genus universality, Jaffe–Choptuik-style checks, robustness |
| Runners / reports | `run_experiments*.py`, `run_batched.py`, `run_all_75_tasks*.py`, `run_3d_nse_stepwise.py`, `run_final_extensions.py`, `run_monumental.py`, `generate_report*.py` | batch drivers and the JSON/MD/HTML/TXT/CSV report engine |
| Config / constants | `config.py`, `monograph_constants.py`, `tasks_parametric.py` | defaults, physical constants, parameterised task lists |
| Julia originals | `ab_cloud_3d.jl`, `ab_cloud_3d_en.jl`, `Generate_Zeta_Zeros_PythonCall_EN.jl` | the Julia side incl. zero generation via PythonCall |

Naming convention: `_en` suffix = English console output; `_v2` suffix =
second-generation revision of the same experiment. One quirk preserved from
the author's upload: `ab_cloud_vortex_powers_final;py` (a stray semicolon in
the filename) is a duplicate of `ab_cloud_vortex_powers_final.py`.

## Run examples

```bash
cd lab-3d/code
python3 ab_cloud_3d_en.py              # full interactive menu (modes A–J)
python3 quick_start.py                 # 1-minute demo
python3 AB_CLOUD_ALL_HYPOTHESES.py     # consolidated 11-hypothesis verification
python3 run_experiments_final.py       # batch experiment suite
julia ab_cloud_3d_en.jl                # Julia original
```

Dependencies: `numpy scipy matplotlib sympy mpmath` (see `../requirements.txt`).

## Кратко (по-русски)

- Все модули 3D-лаборатории: гамильтонианы, RMT-статистики, спинор/топология,
  FEM-солверы, вихревые системы, PDE-эксперименты (Навье–Стокс, KdV, KP),
  генераторы отчётов.
- Входные точки: `ab_cloud_3d_en.py` (меню A–J), `quick_start.py`,
  `AB_CLOUD_ALL_HYPOTHESES.py`; суффикс `_en` — английский вывод, `_v2` —
  вторая редакция.
- Зависимости — `numpy scipy matplotlib sympy mpmath` из
  `../requirements.txt`.
