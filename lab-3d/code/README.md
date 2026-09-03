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

## 📁 Complete file inventory

| Entry | Size | Kind |
|---|---|---|
| `figs/` | directory, 1 files inside | folder |
| `AB_CLOUD_ALL_HYPOTHESES.py` | 15.3 KB | Python source |
| `AB_Cloud_FEM_v6_python.py` | 43.9 KB | Python source |
| `AB_Cloud_FEM_v6_python_en.py` | 43.5 KB | Python source |
| `AB_Cloud_FEM_v8c.py` | 19.9 KB | Python source |
| `AB_Cloud_FEM_v8c_en.py` | 20.0 KB | Python source |
| `AB_Cloud_FEM_v8d.py` | 15.6 KB | Python source |
| `AB_Cloud_FEM_v8d_en.py` | 15.0 KB | Python source |
| `AB_Cloud_Vortex_System_v2.py` | 85.4 KB | Python source |
| `AB_Cloud_Vortex_System_v2_EN.py` | 85.4 KB | Python source |
| `AB_Cloud_Vortex_System_v2_RU.py` | 90.1 KB | Python source |
| `AB_Cloud_topological_magnetism_simulations.py` | 24.6 KB | Python source |
| `CODE_OF_CONDUCT.md` | 5.4 KB | markdown guide |
| `Generate_Zeta_Zeros_PythonCall_EN.jl` | 24.2 KB | Julia source |
| `README.md` | 4.4 KB | markdown guide |
| `__init__.py` | 687 B | Python source |
| `__init___v2.py` | 42 B | Python source |
| `ab_cloud_3d.jl` | 221.1 KB | Julia source |
| `ab_cloud_3d.py` | 77.9 KB | Python source |
| `ab_cloud_3d_en.jl` | 214.0 KB | Julia source |
| `ab_cloud_3d_en.py` | 76.4 KB | Python source |
| `ab_cloud_advanced.py` | 21.3 KB | Python source |
| `ab_cloud_advanced_v2.py` | 33.8 KB | Python source |
| `ab_cloud_extended_kopt_study.py` | 23.4 KB | Python source |
| `ab_cloud_extended_kopt_study_en.py` | 23.8 KB | Python source |
| `ab_cloud_genus_universality.py` | 16.9 KB | Python source |
| `ab_cloud_genus_universality_en.py` | 17.2 KB | Python source |
| `ab_cloud_hamiltonian.py` | 7.5 KB | Python source |
| `ab_cloud_hamiltonian_v2.py` | 11.3 KB | Python source |
| `ab_cloud_hybrid_approach.py` | 17.6 KB | Python source |
| `ab_cloud_hybrid_approach_en.py` | 18.0 KB | Python source |
| `ab_cloud_jacobi_verify.py` | 31.4 KB | Python source |
| `ab_cloud_jacobi_verify_en.py` | 31.7 KB | Python source |
| `ab_cloud_jc_choptuik_n_study.py` | 18.9 KB | Python source |
| `ab_cloud_jc_choptuik_n_study_en.py` | 19.2 KB | Python source |
| `ab_cloud_jc_verify_v2.py` | 34.5 KB | Python source |
| `ab_cloud_jc_verify_v2_en.py` | 34.9 KB | Python source |
| `ab_cloud_ktheory.py` | 42.7 KB | Python source |
| `ab_cloud_robustness_study.py` | 18.6 KB | Python source |
| `ab_cloud_robustness_study_en.py` | 19.0 KB | Python source |
| `ab_cloud_spinor.py` | 5.7 KB | Python source |
| `ab_cloud_spinor_v2.py` | 4.2 KB | Python source |
| `ab_cloud_stats.py` | 10.0 KB | Python source |
| `ab_cloud_stats_v2.py` | 10.9 KB | Python source |
| `ab_cloud_sweeps.py` | 18.5 KB | Python source |
| `ab_cloud_sweeps_v2.py` | 13.7 KB | Python source |
| `ab_cloud_vortex_fine_search.py` | 12.7 KB | Python source |
| `ab_cloud_vortex_powers_final.py` | 11.2 KB | Python source |
| `ab_cloud_vortex_powers_final;py` | 11.0 KB | file |
| `ab_cloud_vortex_powers_final_en.py` | 11.6 KB | Python source |
| `ab_cloud_vortex_search.py` | 17.5 KB | Python source |
| `ab_cloud_vortex_search_en.py` | 17.9 KB | Python source |
| `ab_cloud_zeta.py` | 2.6 KB | Python source |
| `ab_cloud_zeta_v2.py` | 5.9 KB | Python source |
| `collect_summary_data.py` | 6.0 KB | Python source |
| `config.py` | 8.5 KB | Python source |
| `extended_solvers.py` | 18.9 KB | Python source |
| `full_AB_simulation.py` | 17.1 KB | Python source |
| `full_AB_simulation_en.py` | 16.6 KB | Python source |
| `generate_3d_nse_figures.py` | 9.5 KB | Python source |
| `generate_report.py` | 93.0 KB | Python source |
| `generate_report_en.py` | 93.1 KB | Python source |
| `generate_report_v2.py` | 122.4 KB | Python source |
| `generate_report_v2_en.py` | 122.5 KB | Python source |
| `generate_report_v3.py` | 142.4 KB | Python source |
| `generate_report_v3_en.py` | 142.6 KB | Python source |
| `generate_report_v4.py` | 162.0 KB | Python source |
| `generate_report_v4_en.py` | 162.2 KB | Python source |
| `isospectral_b.py` | 26.5 KB | Python source |
| `isospectral_b_en.py` | 25.6 KB | Python source |
| `kdv_core.py` | 16.3 KB | Python source |
| `kp_solver.py` | 15.0 KB | Python source |
| `large_matrix_demo.py` | 2.6 KB | Python source |
| `monograph_constants.py` | 18.6 KB | Python source |
| `monograph_verification.py` | 83.6 KB | Python source |
| `monograph_verification_en.py` | 82.0 KB | Python source |
| `monograph_verification_part2.py` | 48.4 KB | Python source |
| `monograph_verification_part2_en.py` | 48.1 KB | Python source |
| `monograph_verification_part3.py` | 60.4 KB | Python source |
| `monograph_verification_part3_en.py` | 60.4 KB | Python source |
| `monograph_verification_part4.py` | 74.3 KB | Python source |
| `monograph_verification_part4_en.py` | 73.9 KB | Python source |
| `nse3d_core.py` | 23.2 KB | Python source |
| `polchinski_rg.py` | 14.6 KB | Python source |
| `quick_start.py` | 2.6 KB | Python source |
| `run_3d_nse_stepwise.py` | 2.4 KB | Python source |
| `run_all_75_tasks.py` | 3.1 KB | Python source |
| `run_all_75_tasks_en.py` | 3.3 KB | Python source |
| `run_batched.py` | 6.7 KB | Python source |
| `run_experiments.py` | 16.6 KB | Python source |
| `run_experiments_final.py` | 14.7 KB | Python source |
| `run_experiments_part2.py` | 24.2 KB | Python source |
| `run_extended_experiments.py` | 24.3 KB | Python source |
| `run_final_extensions.py` | 20.3 KB | Python source |
| `run_monumental.py` | 54.0 KB | Python source |
| `run_verification.py` | 46.8 KB | Python source |
| `run_verification_extended.py` | 62.1 KB | Python source |
| `tasks_parametric.py` | 20.0 KB | Python source |
| `verifier_core.py` | 8.1 KB | Python source |
| **Total (files)** | **3.7 MB** | 98 files + 1 subdirectories |

## 🔬 Deep dive — the rendering and physics pipelines

The lab code separates cleanly into *physics* (build the 3D Hofstadter
operator for a given ladder and flux; extract surfaces, textures and
invariants) and *rendering* (turn those arrays into the committed 600-dpi
PNGs and the web-consumable meshes). That separation is what allows the
browser app and the offline pipeline to share the physics while differing
only in the rendering backend — a screenshot and a printed plate are two
views of one computation, not two computations.

Every script here is deterministic: fixed seeds, fixed ladders, explicit
parameter blocks at the top of the file. Re-running a script reproduces
its committed output byte-for-byte or reports why not — silent drift is
treated as a bug, not as entropy.
