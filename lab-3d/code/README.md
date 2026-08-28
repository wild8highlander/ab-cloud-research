# AB Cloud Verification & Simulation Code

Python and Julia source code for the AB Cloud research project:
verification of the polarization correction *b* ≈ 0.0785,
3D Navier–Stokes regularity, Riemann zeta zeros correspondence,
and related mathematical physics computations.

## Overview

This directory contains **69 Python files** and **1 Julia file**
(`Generate_Zeta_Zeros_PythonCall_EN.jl`) implementing the full
numerical verification and simulation suite for the AB Cloud monograph.

### Quick Start

```bash
# Minimal demo
python quick_start.py

# Large matrix demonstration
python large_matrix_demo.py

# Full 3D AB Cloud simulation
python ab_cloud_3d.py       # Russian comments
python ab_cloud_3d_en.py    # English comments
```

### Dependencies

```bash
pip install numpy scipy matplotlib sympy mpmath
```

### Statistics

| Metric | Count |
|--------|-------|
| Python files | 69 |
| Total functions | 1126 |
| Total classes | 50 |
| Total code size | 2,246,665 bytes |

## File Reference

| File | Category | Functions | Classes | Size | Description |
|------|----------|-----------|---------|------|-------------|
| `AB_CLOUD_ALL_HYPOTHESES.py` | Hypothesis Verification | 8 | 0 | 15,630 | Consolidated verification script for all 11 hypotheses about AB-cloud monograph. |
| `AB_Cloud_FEM_v6_python.py` | FEM Solver | 23 | 0 | 44,128 | FEM Solver |
| `AB_Cloud_FEM_v8c.py` | FEM Solver | 21 | 0 | 20,349 | Исправленная генерация PSL(2,7) и классы сопряжённости |
| `AB_Cloud_FEM_v8d.py` | FEM Solver | 17 | 0 | 15,971 | КЛЮЧЕВОЕ ИЗМЕНЕНИЕ: вместо ошибочной slave-master идентификации граничных |
| `AB_Cloud_Vortex_System_v2.py` | Core System | 40 | 9 | 87,433 | AB-CLOUD VORTEX SYSTEM FOR N-BODY PROBLEM — PYTHON VERSION (v2.0) |
| `AB_Cloud_Vortex_System_v2_EN.py` | Core System | 40 | 9 | 87,433 | AB-CLOUD VORTEX SYSTEM FOR N-BODY PROBLEM — PYTHON VERSION (v2.0) |
| `AB_Cloud_Vortex_System_v2_RU.py` | Core System | 40 | 9 | 92,258 | СИСТЕМА ВИХРЕЙ AB-ОБЛАКА ДЛЯ ЗАДАЧИ N ТЕЛ — PYTHON VERSION (v2.0) |
| `AB_Cloud_topological_magnetism_simulations.py` | Topological Magnetism | 12 | 0 | 25,168 | AB-Cloud: Topological Magnetism — Numerical Simulations |
| `__init__.py` | Package Init | 0 | 0 | 0 | Package Init |
| `__init___v2.py` | Package Init | 0 | 0 | 42 | ab_cloud_monumental python package. |
| `ab_cloud_3d.py` | 3D NSE | 40 | 1 | 79,805 | AB-CLOUD 3D — Unified Preprint Verification File (PYTHON PORT, RUSSIAN UI) |
| `ab_cloud_3d_en.py` | 3D NSE | 40 | 1 | 78,232 | AB-CLOUD 3D — Unified Preprint Verification File (PYTHON PORT, ENGLISH UI) |
| `ab_cloud_advanced.py` | Advanced Analysis | 24 | 0 | 21,764 | Advanced statistics for the AB-cloud verification suite: |
| `ab_cloud_advanced_v2.py` | Advanced Analysis | 19 | 0 | 34,660 | ab_cloud_advanced.py |
| `ab_cloud_extended_kopt_study.py` | Other | 19 | 1 | 23,997 | EXTENDED STUDY: k_opt(n) for n=1..10 + Choptuik correction variations |
| `ab_cloud_genus_universality.py` | Genus Universality | 15 | 1 | 17,267 | GENUS UNIVERSALITY STUDY: c=T(g) for g=2,3,4,5,6 |
| `ab_cloud_hamiltonian.py` | Hamiltonian | 7 | 1 | 7,719 | Real AB-cloud Hamiltonian with topological vortices. |
| `ab_cloud_hamiltonian_v2.py` | Hamiltonian | 13 | 1 | 11,521 | ab_cloud_hamiltonian.py |
| `ab_cloud_hybrid_approach.py` | Hybrid Approach | 14 | 1 | 18,050 | HYBRID APPROACH: Simplified AB-cloud Hamiltonian without geometry (Chapter 14 §1 |
| `ab_cloud_jacobi_verify.py` | Jacobi Verification | 22 | 1 | 32,170 | AB-CLOUD JACOBIAN EXTENSION — Verification Suite (Chapter 14) |
| `ab_cloud_jc_choptuik_n_study.py` | JC Verification | 13 | 1 | 19,349 | JC VERIFICATION WITH CHOPTUIK CORRECTION FOR n = 1..6 (Chapter 14 §14.19-14.20) |
| `ab_cloud_jc_verify_v2.py` | JC Verification | 21 | 1 | 35,370 | JACOBIAN CONJECTURE VERIFICATION VIA AB-CLOUD HAMILTONIAN FLOW (Chapter 14 §14.1 |
| `ab_cloud_ktheory.py` | K-Theory | 22 | 0 | 43,695 | K-theory and topological invariants for the AB-Cloud monograph (V100–V110). |
| `ab_cloud_robustness_study.py` | Robustness Study | 17 | 1 | 19,089 | ROBUSTNESS STUDY: W_k = π^(-2k) — stability across T_flow, r_k, n_test_points |
| `ab_cloud_spinor.py` | Spinor | 5 | 0 | 5,842 | All 64 spinor structures on the genus-3 Bolza/Klein surface, Arf invariant, |
| `ab_cloud_spinor_v2.py` | Spinor | 5 | 1 | 4,343 | ab_cloud_spinor.py |
| `ab_cloud_stats.py` | Statistics | 15 | 0 | 10,281 | Honest GUE/RMT statistics: ⟨r⟩, Σ²(L), Δ₃(L), p(s), R₂(s). |
| `ab_cloud_stats_v2.py` | Statistics | 26 | 0 | 11,155 | ab_cloud_stats.py |
| `ab_cloud_sweeps.py` | Parameter Sweeps | 19 | 0 | 18,938 | Dense parameter-sweep infrastructure for the AB-cloud verification suite. |
| `ab_cloud_sweeps_v2.py` | Parameter Sweeps | 9 | 1 | 14,018 | ab_cloud_sweeps.py |
| `ab_cloud_vortex_fine_search.py` | Vortex Analysis | 11 | 1 | 13,014 | EXPLORATORY V2: Fine-grained search around 1/π² for absolute JC proof |
| `ab_cloud_vortex_powers_final.py` | Vortex Analysis | 12 | 1 | 11,475 | EXPLORATORY V3: Find optimal π^(-2k) for n=4 and confirm absolute JC for all n |
| `ab_cloud_vortex_search.py` | Vortex Analysis | 12 | 1 | 17,958 | EXPLORATORY: Vortex numerical values for absolute JC proof (Chapter 14 research) |
| `ab_cloud_zeta.py` | Zeta Zeros | 5 | 0 | 2,698 | Riemann zeros with PROPER Riemann-von Mangoldt unfolding. |
| `ab_cloud_zeta_v2.py` | Zeta Zeros | 10 | 0 | 6,005 | ab_cloud_zeta.py |
| `collect_summary_data.py` | Data Collection | 4 | 0 | 6,173 | Quick re-run of E6, E9, E10, E12 to save numerical summary data. |
| `config.py` | Configuration | 6 | 1 | 8,718 | Provides a Config dataclass with all adjustable parameters, loaded from |
| `extended_solvers.py` | Extended Solvers | 19 | 0 | 19,381 | All three extend the KdV framework of kdv_core.py to non-integrable |
| `full_AB_simulation.py` | Full Simulation | 8 | 0 | 17,487 | TASK 3: FULL AB-CLOUD SIMULATION WITH KERR-SCHWARZSCHILD METRIC |
| `generate_3d_nse_figures.py` | 3D NSE | 0 | 0 | 9,737 | Generate all 3D NSE figures from saved partial results. |
| `generate_report.py` | Report Generator | 11 | 0 | 95,241 | monograph): Russian text + English figure captions. |
| `generate_report_v2.py` | Report Generator | 12 | 0 | 125,290 | generate_report.py — Generates the bilingual DOCX report (Chapter 16 of the |
| `generate_report_v3.py` | Report Generator | 13 | 0 | 145,845 | generate_report.py — Generates the bilingual DOCX report (Chapter 16 of the |
| `generate_report_v4.py` | Report Generator | 14 | 0 | 165,916 | generate_report.py — Generates the bilingual DOCX report (Chapter 16 of the |
| `isospectral_b.py` | Isospectral | 21 | 0 | 27,180 | transformation, with Wilson RG interpretation. |
| `kdv_core.py` | KdV Solver | 18 | 0 | 16,737 | Implements: |
| `kp_solver.py` | KP Solver | 14 | 0 | 15,341 | KP is the 2D generalization of KdV: |
| `large_matrix_demo.py` | Large Matrix Demo | 1 | 0 | 2,645 | examples/large_matrix_demo.py |
| `monograph_constants.py` | Monograph Verification | 24 | 0 | 19,020 | Verifies the entire analytical chain of the monograph: |
| `monograph_verification.py` | Monograph Verification | 40 | 1 | 85,566 | ГИГАНТСКИЙ КОД ВЕРИФИКАЦИИ МОНОГРАФИИ — 75+ ЗАДАЧ |
| `monograph_verification_part2.py` | Monograph Verification | 21 | 0 | 49,571 | Часть II гигантского кода: задачи 31-75 |
| `monograph_verification_part3.py` | Monograph Verification | 29 | 0 | 61,869 | Часть III гигантского кода: задачи 51-75 |
| `monograph_verification_part4.py` | Monograph Verification | 32 | 0 | 76,093 | Часть IV: Задачи 76-100 — Расширенные симуляции NSE и продвинутые графики |
| `nse3d_core.py` | 3D NSE | 18 | 0 | 23,716 | Solves the 3D NSE in vorticity form: |
| `polchinski_rg.py` | Polchinski RG | 7 | 0 | 14,986 | Addresses the limitation noted in §16.24: discrete K_2 steps accumulate |
| `quick_start.py` | Quick Start | 1 | 0 | 2,619 | examples/quick_start.py |
| `run_3d_nse_stepwise.py` | 3D NSE | 0 | 0 | 2,409 | Run 3D NSE experiments one model at a time, saving partial results. |
| `run_all_75_tasks.py` | Experiment Runner | 1 | 0 | 3,220 | Запуск ВСЕХ 75 задач монографии. |
| `run_batched.py` | Experiment Runner | 3 | 0 | 6,833 | Run all 99 verifications in batches, saving intermediate results after each batc |
| `run_experiments.py` | Experiment Runner | 4 | 0 | 17,020 | and generates the 25+ professional figures (English labels) for the |
| `run_experiments_final.py` | Experiment Runner | 5 | 0 | 15,100 | Run only E15 (universality) and generate final summary figures. |
| `run_experiments_part2.py` | Experiment Runner | 5 | 0 | 24,799 | Runs the remaining 10 experiments and generates the corresponding figures. |
| `run_extended_experiments.py` | Experiment Runner | 5 | 0 | 24,894 | E16: mKdV + b (3 mechanisms) |
| `run_final_extensions.py` | Experiment Runner | 4 | 0 | 20,828 | E21: Polchinski-K_1 RG flow (10, 20, 50 steps) — iterated RG |
| `run_monumental.py` | Experiment Runner | 40 | 1 | 55,289 | Master runner for AB-Cloud monograph verification — monumental edition. |
| `run_verification.py` | Verification | 40 | 1 | 47,951 | Comprehensive AB-cloud verification suite — addresses ALL critique of v17. |
| `run_verification_extended.py` | Verification | 40 | 1 | 63,607 | EXTENDED verification suite for the AB-cloud monograph. |
| `tasks_parametric.py` | Parametric Tasks | 40 | 0 | 20,450 | These tasks perform systematic parameter scans to verify robustness |
| `verifier_core.py` | Verification | 10 | 2 | 8,307 | Contains the TaskRunner class that executes verification tasks, collects |

## Detailed Descriptions

### Core System

#### `AB_Cloud_Vortex_System_v2.py`

> ============================================================================
> AB-CLOUD VORTEX SYSTEM FOR N-BODY PROBLEM — PYTHON VERSION (v2.0)
> ============================================================================
> Massive Python implementation of the Three-Body (and N-Body) Problem
> verification via the AB-cloud vortex model with Chaplygin topological integral.
> 
> This is the MIRROR of the Julia version (AB_Cloud_Vortex_System_v2.jl).
> Both codes produce identical results and have the same 22-section structure.
> 
> Author: Z.ai Research Laboratory
> Version: 2.0
> Year: 2026
>

**Key functions:** `default_config()`, `build_hofstadter_hamiltonian()`, `compute_spectrum()`, `analytical_solution_r()`, `analytical_solution_theta()`, `analytical_frequency()`, `analytical_amplitude()`, `compute_chaplygin_constant()`, `verify_chaplygin_conservation()`, `verify_chaplygin_for_range()`, `unfold_spacings()`, `compute_r_statistic()`, `gue_cdf()`, `goe_cdf()`, `poisson_cdf()`
  ... and 16 more

**Classes:** `Config`, `Vortex`, `RMTResults`, `ChaplyginResults`, `QuantumResults`, `TopologicalResults`, `AdvancedRMTResults`, `ChaosResults`, `RealSystem`

**Dependencies:** csv, matplotlib, mpl_toolkits, mpmath, numpy, os, pathlib, scipy, traceback

---

#### `AB_Cloud_Vortex_System_v2_EN.py`

> ============================================================================
> AB-CLOUD VORTEX SYSTEM FOR N-BODY PROBLEM — PYTHON VERSION (v2.0)
> ============================================================================
> Massive Python implementation of the Three-Body (and N-Body) Problem
> verification via the AB-cloud vortex model with Chaplygin topological integral.
> 
> This is the MIRROR of the Julia version (AB_Cloud_Vortex_System_v2.jl).
> Both codes produce identical results and have the same 22-section structure.
> 
> Author: Z.ai Research Laboratory
> Version: 2.0
> Year: 2026
>

**Key functions:** `default_config()`, `build_hofstadter_hamiltonian()`, `compute_spectrum()`, `analytical_solution_r()`, `analytical_solution_theta()`, `analytical_frequency()`, `analytical_amplitude()`, `compute_chaplygin_constant()`, `verify_chaplygin_conservation()`, `verify_chaplygin_for_range()`, `unfold_spacings()`, `compute_r_statistic()`, `gue_cdf()`, `goe_cdf()`, `poisson_cdf()`
  ... and 16 more

**Classes:** `Config`, `Vortex`, `RMTResults`, `ChaplyginResults`, `QuantumResults`, `TopologicalResults`, `AdvancedRMTResults`, `ChaosResults`, `RealSystem`

**Dependencies:** csv, matplotlib, mpl_toolkits, mpmath, numpy, os, pathlib, scipy, traceback

---

#### `AB_Cloud_Vortex_System_v2_RU.py`

> ============================================================================
> СИСТЕМА ВИХРЕЙ AB-ОБЛАКА ДЛЯ ЗАДАЧИ N ТЕЛ — PYTHON VERSION (v2.0)
> ============================================================================
> Масштабная Python-реализация of the задачи трёх (и N) тел
> верификация через вихревую модель AB-облака с топологическим интегралом Чаплыгина.
> 
> Это ЗЕРКАЛО Julia-версии (AB_Cloud_Вихрь_Система_v2.jl).
> Оба кода дают идентичные результаты и имеют одинаковую 22-секционную структуру.
> 
> Автор: Z.ai Research Laboratory
> Версия: 2.0
> Год: 2026
> 
> 22 СЕКЦИИ:
>  1. Im

**Key functions:** `default_config()`, `build_hofstadter_hamiltonian()`, `compute_spectrum()`, `analytical_solution_r()`, `analytical_solution_theta()`, `analytical_frequency()`, `analytical_amplitude()`, `compute_chaplygin_constant()`, `verify_chaplygin_conservation()`, `verify_chaplygin_for_range()`, `unfold_spacings()`, `compute_r_statistic()`, `gue_cdf()`, `goe_cdf()`, `poisson_cdf()`
  ... and 16 more

**Classes:** `Config`, `Вихрь`, `RMTResults`, `ChaplyginResults`, `QuantumResults`, `TopologicalResults`, `AdvancedRMTResults`, `ChaosResults`, `RealСистема`

**Dependencies:** csv, matplotlib, mpl_toolkits, mpmath, numpy, os, pathlib, scipy, traceback

---

### FEM Solver

#### `AB_Cloud_FEM_v6_python.py`

**Key functions:** `psl27_character_table()`, `enumerate_psl27()`, `mat_mul_mod7()`, `build_mult_table()`, `element_order()`, `find_identity()`, `find_generators()`, `find_inverse()`, `classify_conjugacy_classes()`, `are_conjugate()`, `build_rep_matrices()`, `poincare_omega2()`, `moebius_rotation()`, `rotation_pi_around_origin()`, `geodesic_arc_points()`
  ... and 8 more

**Dependencies:** numpy, scipy, sys, time

---

#### `AB_Cloud_FEM_v8c.py`

> AB_Cloud_FEM_v8c.py — FEM на Клейне с матричными twisted BC
> Исправленная генерация PSL(2,7) и классы сопряжённости

**Key functions:** `mm()`, `minv()`, `mk()`, `nk()`, `eq()`, `order_psl()`, `gen_psl27()`, `classify()`, `build_all_reps()`, `psl_action()`, `psl_action()`, `extract_from_7a7a()`, `create_mesh()`, `om2()`, `assemble()`
  ... and 6 more

**Dependencies:** collections, numpy, scipy, time, traceback

---

#### `AB_Cloud_FEM_v8d.py`

> AB_Cloud_FEM_v8d.py — FEM на Клейне с калибровочным полем и BC Неймана
> 
> КЛЮЧЕВОЕ ИЗМЕНЕНИЕ: вместо ошибочной slave-master идентификации граничных
> узлов, используем естественные BC Неймана (все граничные узлы свободны)
> + калибровочное поле A для кодирования монодромии вокруг конических точек.
> 
> Для скалярного кручения (ω_A, ω_B, ω_C):
> - Коническая точка A: Dirichlet если |ω_A-1| > tol, иначе свободна
> - Коническая точка B: Dirichlet если |ω_B-1| > tol, иначе свободна
> - Коническая точка C: Dirichlet если |ω_C-1| > tol, иначе свободна
> - Все остальные граничные узлы: СВОБОДНЫ (Ne

**Key functions:** `mm()`, `minv()`, `mk()`, `nk()`, `eq()`, `order_psl()`, `gen_psl27()`, `classify()`, `build_reps()`, `psl_action()`, `create_mesh()`, `om2()`, `assemble_with_gauge()`, `find_triples()`, `cone_fixed()`
  ... and 2 more

**Dependencies:** collections, numpy, scipy, time

---

### Hamiltonian

#### `ab_cloud_hamiltonian.py`

> ab_cloud_hamiltonian.py
> =======================
> Real AB-cloud Hamiltonian with topological vortices.
> 
> CRITICAL FIX vs v17:
> --------------------
> v17 used build_H with V = W*(rand()-0.5) (uniform diagonal disorder) and a
> single Peierls phase 2*pi*phi*(i-1) in x-direction only.  That is the standard
> Hofstadter model with diagonal disorder, NOT the AB-cloud of the monograph.
> 
> Here we implement the actual monograph Hamiltonian:
> 
>     H_{ij} = -t_x e^{i A_x(r_i)} δ_{j,i+x̂}
>              -t_y e^{i A_y(r_i)} δ_{j,i+ŷ}
>              + V_i δ_{ij}
> 
> with
> 
>     A_x(r_i) = 

**Key functions:** `build_ab_cloud_hamiltonian()`, `build_pure_hofstadter()`, `build_random_anderson()`, `build_random_gue()`

**Classes:** `VortexConfig`

**Dependencies:** __future__, dataclasses, numpy

---

#### `ab_cloud_hamiltonian_v2.py`

> ab_cloud_hamiltonian.py
> =======================
> Core Hamiltonian builder for the AB-Cloud model with real Aharonov-Bohm vortices.
> 
> This module implements the lattice Hofstadter Hamiltonian on an L x L square lattice
> with Peierls phases in BOTH directions (proper magnetic flux) AND a real vortex
> configuration {q_k = +-1, r_k} with Coulomb-like interaction, exactly as described
> in the monograph. The model is:
> 
>     H = -t sum_{<i,j>} (e^{i theta_{ij}} c_i^+ c_j + h.c.)
>         + sum_i V_i c_i^+ c_i
> 
> where
>     theta_{ij} = 2*pi*alpha*(x_i + x_j)/2 * (y_j - y_i)   [Peierls

**Key functions:** `n_vortices()`, `net_charge()`, `default_vortex_config()`, `build_ab_cloud_hamiltonian()`, `idx()`, `build_pure_hofstadter()`, `idx()`, `build_hofstadter_with_disorder()`, `band_energies()`, `central_gap()`, `fast_central_eigs()`, `fast_central_eigsys()`

**Classes:** `VortexConfig`

**Dependencies:** dataclasses, fractions, numpy, scipy, typing

---

### Spinor

#### `ab_cloud_spinor.py`

> ab_cloud_spinor.py
> ==================
> All 64 spinor structures on the genus-3 Bolza/Klein surface, Arf invariant,
> and the special idx=38 structure claimed by the monograph to protect the
> Dirac cone at α=1/2.
> 
> CRITICAL ADDITION vs v17:
> -------------------------
> v17 had ZERO checks of:
>     - the 64 spinor structures
>     - Arf invariant
>     - idx=38 uniqueness
> 
> These are CENTRAL to the monograph's claim (sections 8-10).  Here we add them.
> 
> Mathematical background:
> ------------------------
> On a genus-g Riemann surface there are 2^(2g) = 2^6 = 64 spin structures.
>

**Key functions:** `all_spinor_structures()`, `arf_invariant()`, `classify_all_spinors()`, `check_idx38()`, `psl27_action_on_spinors_quick()`

**Dependencies:** __future__, itertools, numpy

---

#### `ab_cloud_spinor_v2.py`

> ab_cloud_spinor.py
> ==================
> Spinor classification and Arf invariant for AB-Cloud vortex configurations.
> 
> Implements the 64-spinor classification on the L x L lattice with bipartite
> structure (alpha = 1/2) and computes the Arf invariant under three conventions.
> 
> Monograph prediction: idx=38 spinor is in the odd-Arf sector.

**Key functions:** `weight()`, `generate_spinors()`, `quadratic_form_Q()`, `arf_invariant()`, `spinor_classification()`

**Classes:** `Spinor`

**Dependencies:** dataclasses, numpy, typing

---

### K-Theory

#### `ab_cloud_ktheory.py`

> ab_cloud_ktheory.py
> ===================
> K-theory and topological invariants for the AB-Cloud monograph (V100–V110).
> 
> This module implements the **fourth monumental batch** of verifications:
>   V100 - First Chern number (TKNN integer quantum Hall) via discretized
>          Berry curvature over the magnetic Brillouin zone
>   V101 - Vortex winding number sum rule (Sigma q_k = topological charge)
>   V102 - Z2 topological invariant (Kane-Mele style) at alpha = 1/2 chiral point
>   V103 - Bott index (Hastings-Loring real-space Chern number for disordered
>          Hofstadter, robust to 

**Key functions:** `first_chern_number()`, `link()`, `vortex_winding_sum_rule()`, `z2_invariant_kane_mele()`, `bott_index()`, `chiral_winding_number()`, `index_theorem_chiral()`, `k_theory_classification()`, `bulk_boundary_correspondence()`, `idx()`, `eta_invariant()`, `link()`, `second_chern_class_4d()`, `d_vec()`, `H_4d()`
  ... and 5 more

**Dependencies:** __future__, numpy, typing

---

### Jacobi Verification

#### `ab_cloud_jacobi_verify.py`

> AB-CLOUD JACOBIAN EXTENSION — Verification Suite (Chapter 14)
> =============================================================
> Numerical verification of the Lagrangian hierarchy with Jacobi theta-function
> insertion for the AB-cloud on the Klein quartic Jacobian J(K_4).
> 
> Pipeline:
>   1. Build the 3x3 period matrix tau of the Klein quartic (Tretkoff-Tretkoff).
>   2. Compute the genus-3 Jacobi theta function theta_eps(z, tau) via mpmath.
>   3. Construct the lattice Lagrangian with Jacobi-modulated phases.
>   4. Newton iteration for vortex solitons (Theorem 14.1).
>   5. QNM spectrum co

**Key functions:** `jacobi_theta_genus3()`, `jacobi_theta_fast()`, `odd_theta_characteristics()`, `verify_odd_thetas()`, `ab_phase()`, `build_ab_cloud_hamiltonian()`, `idx()`, `vortex_bogomolny_ansatz()`, `vortex_residual()`, `solve_vortex()`, `qnm_spectrum()`, `F_J()`, `monte_carlo_r_parameter()`, `gue_preservation_test()`, `fig_theta_heatmap()`
  ... and 5 more

**Classes:** `ABCloudConfig`

**Dependencies:** __future__, dataclasses, json, matplotlib, mpmath, numpy, os, scipy, sys, time, typing

---

### JC Verification

#### `ab_cloud_jc_choptuik_n_study.py`

> JC VERIFICATION WITH CHOPTUIK CORRECTION FOR n = 1..6 (Chapter 14 §14.19-14.20)
> ================================================================================
> Systematic study of how the Choptuik correction (1 - 1/π²) = 0.89868 affects
> the Jacobian Conjecture verification across dimensions n = 1, 2, 3, 4, 5, 6.
> 
> For each n we:
>   1. Build an AB-cloud Hamiltonian with N_v = n vortices (one per dimension).
>   2. Compute det(J_F) at multiple test points without and with the correction.
>   3. Measure:
>        - mean and std of det(J_F)
>        - relative deviation σ/|μ| (JC consta

**Key functions:** `build_vortex_data()`, `hamiltonian_flow_map()`, `dH_dpsi_bar()`, `dH_dpsi()`, `jacobian_det_flow()`, `generate_test_points()`, `verify_jc_for_n()`, `run_all_dimensions()`, `fig_jc_n_comparison()`, `fig_slowdown_n()`, `fig_jc_phase_diagram()`, `main()`

**Classes:** `ABCloudConfig`

**Dependencies:** __future__, dataclasses, matplotlib, numpy, os, typing

---

#### `ab_cloud_jc_verify_v2.py`

> JACOBIAN CONJECTURE VERIFICATION VIA AB-CLOUD HAMILTONIAN FLOW (Chapter 14 §14.12–14.16)
> ========================================================================================
> This script verifies the Keller Jacobian Conjecture (1939) for n=1, 2, 3 by using
> the AB-cloud Hamiltonian flow as the polynomial map F: C^n → C^n.
> 
> Key insight (user's clarification):
>     The AB-cloud with topological vortices q_k = ±1 defines a Hamiltonian flow
>     on the phase space (ψ, ψ̄) ≅ C^n. This flow is polynomial in the initial
>     data; its Jacobian determinant should be constant (Liouville'

**Key functions:** `build_vortex_hamiltonian()`, `hamiltonian_flow_map()`, `dH_dpsi_bar()`, `dH_dpsi()`, `jacobian_det_flow()`, `verify_n1()`, `verify_n2()`, `verify_n3()`, `verify_n4()`, `pinchuk_counterexample()`, `h()`, `F_pinchuk()`, `J_pinchuk()`, `dixmier_equivalence()`, `fig_jacobian_determinant()`
  ... and 5 more

**Classes:** `ABCloudConfig`

**Dependencies:** __future__, dataclasses, matplotlib, numpy, os, scipy, typing

---

### Zeta Zeros

#### `ab_cloud_zeta.py`

> ab_cloud_zeta.py
> ================
> Riemann zeros with PROPER Riemann-von Mangoldt unfolding.
> 
> CRITICAL FIX vs v17:
> --------------------
> v17 used polynomial regression  N(γ) ≈ a + b·γ + c·γ·log(γ)  as the unfolding.
> That is a hack: the coefficients a,b,c float to fit the data, so the unfolded
> sequence is by construction closer to mean-spacing 1 than a true Weyl unfolding
> would give.  Different choices of fitting basis give ⟨r⟩ in [0.51, 0.60] for
> N=1000 — i.e. the result is dominated by the unfolding choice, not by the data.
> 
> Here we use the EXACT Riemann-von Mangoldt for

**Key functions:** `riemann_von_mangoldt_N()`, `fetch_riemann_zeros()`, `unfold_rvm()`, `unfolded_spacings()`, `sanity_check_unfolding()`

**Dependencies:** __future__, mpmath, numpy

---

#### `ab_cloud_zeta_v2.py`

> ab_cloud_zeta.py
> ================
> Riemann zeta zeros and analytic number theory utilities.
> 
> - mpmath-based computation of zeta zeros (high precision)
> - Riemann-von Mangoldt explicit formula
> - Montgomery-Odlyzko pair correlation of zeta zeros
> - Bogomolny-Keating sigma_BK bootstrap
> - Spectral form factor of zeta zeros (long-time regime)

**Key functions:** `compute_zeta_zeros()`, `riemann_von_mangoldt_N()`, `unfold_zeta_zeros()`, `normalized_zeta_spacings()`, `pair_correlation_zeta()`, `bogomolny_keating_sigma()`, `zeta_form_factor()`, `hardy_Z()`, `prime_counting_comparison()`

**Dependencies:** json, mpmath, numpy, os, sympy

---

### Hypothesis Verification

#### `AB_CLOUD_ALL_HYPOTHESES.py`

> AB_CLOUD_ALL_HYPOTHESES.py
> ==========================
> Consolidated verification script for all 11 hypotheses about AB-cloud monograph.
> 
> This single file contains verification code for:
> - H1: idx=38 and 28 bitangents of Klein quartic (Riemann/Klein theorem)
> - H2: Factor of 2 in Langlands scale (K-theoretic Dirac doubling)
> - H3: E_8 and π/15 phase (Coxeter element, PSL(2,7)→W(E_8))
> - H4: Monster character restriction (ATLAS subgroup #10)
> - H5: Non-Hermitian skin effect (Hatano-Nelson, σ≠1/2)
> - H6: Connes Morita self-duality at α=1/2
> - H7: Ihara zeta and Ramanujan graphs (Kl

**Key functions:** `dirichlet_chi()`, `legendre_7()`, `dirac_hamiltonian()`, `generate_GOE()`, `generate_GUE()`, `generate_GSE()`, `compute_spacings()`, `wigner_dyson()`

**Dependencies:** collections, itertools, json, math, matplotlib, numpy

---

### Monograph Verification

#### `monograph_constants.py`

> monograph_constants.py — Verification of all 25 constants of the monograph.
> 
> Verifies the entire analytical chain of the monograph:
>    PSL(2,7) → α → L_min → e → b → γ → C_K → C_s → 3D NSE stabilization
> 
> Each constant is computed from first principles (geometry / number theory)
> and compared to the monograph's predicted value.  All residuals are ~1e-10
> or smaller, confirming the analytical derivation.
> 
> Run:   python3 monograph_constants.py

**Key functions:** `klein_alpha()`, `klein_alpha_root_check()`, `klein_L_min()`, `klein_volume()`, `selberg_zeta_leading()`, `selberg_zeta_full()`, `b_from_selberg()`, `euler_e_identity()`, `euler_e_residual()`, `gamma_from_e_and_b()`, `C_K_prediction()`, `smagorinsky_Lilly()`, `golden_ratio()`, `fibonacci_ratio()`, `anosov_lyapunov()`
  ... and 9 more

**Dependencies:** __future__, numpy, scipy

---

#### `monograph_verification.py`

> ================================================================================
> monograph_verification.py
> ГИГАНТСКИЙ КОД ВЕРИФИКАЦИИ МОНОГРАФИИ — 75+ ЗАДАЧ
> GIANT VERIFICATION CODE FOR THE MONOGRAPH — 75+ TASKS
> 
> Двуязычная монография: "Поправка b как поляризационное закручивание:
> аналитическое доказательство регулярности 3D Navier–Stokes без диссипации"
> 
> Bilingual monograph: "Correction b as polarization twisting:
> analytical proof of 3D Navier–Stokes regularity without dissipation"
> 
> СТРУКТУРА / STRUCTURE:
> - Часть I:   Задачи 1-10  — Аналитическое происхождение b
> - Час

**Key functions:** `log()`, `add_csv()`, `add_json()`, `save_figure()`, `finalize()`, `safe_norm()`, `safe_max()`, `rodrigues_rotation()`, `task_01()`, `task_02()`, `task_03()`, `task_04()`, `task_05()`, `task_06()`, `task_07()`
  ... and 24 more

**Classes:** `Output`

**Dependencies:** cmath, csv, dataclasses, json, math, matplotlib, mpl_toolkits, numpy, os, pathlib, sys, time, traceback, typing

---

#### `monograph_verification_part2.py`

> monograph_verification_part2.py
> Часть II гигантского кода: задачи 31-75
> Part II of the giant code: tasks 31-75
> 
> Импортирует задачи 1-30 из основного файла и добавляет:
> - Часть IV: Задачи 31-40 — F-аттрактор и анозовский поток
> - Часть V: Задачи 41-50 — b как фазовый поворот (теория)
> - Часть VI: Задачи 51-60 — Симуляции 2D NSE
> - Часть VII: Задачи 61-70 — Симуляции 3D NSE
> - Часть VIII: Задачи 71-75 — Универсальность и финальная верификация

**Key functions:** `task_31()`, `task_32()`, `task_33()`, `task_34()`, `task_35()`, `task_36()`, `task_37()`, `task_38()`, `task_39()`, `task_40()`, `task_41()`, `task_42()`, `task_43()`, `task_44()`, `task_45()`
  ... and 6 more

**Dependencies:** math, matplotlib, monograph_verification, mpl_toolkits, numpy, pathlib, sys, time, traceback

---

#### `monograph_verification_part3.py`

> monograph_verification_part3.py
> Часть III гигантского кода: задачи 51-75
> Part III: tasks 51-75
> 
> - Часть VI:  Задачи 51-60 — Симуляции 2D NSE
> - Часть VII: Задачи 61-70 — Симуляции 3D NSE
> - Часть VIII:Задачи 71-75 — Универсальность и финальная верификация

**Key functions:** `make_phi_attractor_initial_2d()`, `make_phi_attractor_initial_3d()`, `task_51()`, `task_52()`, `task_53()`, `task_54()`, `task_55()`, `task_56()`, `task_57()`, `task_58()`, `task_59()`, `task_60()`, `task_61()`, `task_62()`, `task_63()`
  ... and 14 more

**Dependencies:** math, matplotlib, monograph_verification, monograph_verification_part2, mpl_toolkits, numpy, pathlib, sys, time, traceback

---

#### `monograph_verification_part4.py`

> monograph_verification_part4.py
> Часть IV: Задачи 76-100 — Расширенные симуляции NSE и продвинутые графики
> Part IV: Tasks 76-100 — Extended NSE simulations and advanced plots
> 
> Включает:
> - Многомасштабные симуляции 2D/3D NSE на разных сетках
> - Спектральный анализ энергии
> - Визуализацию вихревых структур
> - Фазовые портреты
> - Анализ устойчивости φ-аттрактора
> - Сравнение численных методов
> - Влияние параметра b на стабилизацию
> - Зависимость от числа Рейнольдса
> - Энергетические каскады
> - Корреляционные функции

**Key functions:** `setup_grid_2d()`, `setup_grid_3d()`, `make_phi_attractor_2d()`, `make_phi_attractor_3d()`, `simulate_2d_nse()`, `simulate_3d_nse()`, `task_76()`, `task_77()`, `task_78()`, `task_79()`, `task_80()`, `task_81()`, `task_82()`, `task_83()`, `task_84()`
  ... and 17 more

**Dependencies:** cmath, csv, json, math, matplotlib, monograph_verification, mpl_toolkits, numpy, os, pathlib, sys, time, traceback, typing

---

### Verification

#### `run_verification.py`

> run_verification.py
> ===================
> Comprehensive AB-cloud verification suite — addresses ALL critique of v17.
> 
> KEY DESIGN DECISIONS:
> ---------------------
> 1. Every verification prints BOTH the point estimate AND its honest status.
>    We do NOT silently pass tests on weak tolerance.
> 
> 2. We distinguish four categories:
>        PASS_NOVEL      — nontrivial check that confirms a monograph claim
>        PASS_TRIVIAL    — tautology or restatement of a definition
>        PASS_WEAK       — passes only because tolerance is generous
>        FAIL            — check actually fai

**Key functions:** `get_zeta_zeros()`, `add()`, `summary()`, `V01_hofstadter_butterfly()`, `V02_choptuik_constant()`, `V03_dss_period()`, `V04_spectral_invariant()`, `V05_psl27_reps()`, `V06_bolza_genus()`, `V07_area_ratio()`, `V08_selberg_identity()`, `V09_klein_area()`, `V10_wigner_constant()`, `V11_hofstadter_vs_selberg()`, `V12_r_ab_cloud()`
  ... and 24 more

**Classes:** `Verifier`

**Dependencies:** __future__, collections, json, numpy, os, python, scipy, sys, time, traceback

---

#### `run_verification_extended.py`

> run_verification_extended.py
> ============================
> EXTENDED verification suite for the AB-cloud monograph.
> 
> This script adds verifications V38–V86 (49 NEW checks) on top of the
> existing V01–V37 in run_verification.py.  Every verification:
> 
>     1. Runs a DENSE parameter sweep (not just 1–2 points)
>     2. Produces a PNG plot saved to results/plots/
>     3. Reports an honest status (PASS_NOVEL / PASS_TRIVIAL / PASS_WEAK / FAIL)
>     4. Records all results to results/data/verification_report_extended.json
> 
> Total verifications in extended suite: 49 new (V38–V86) + 37 ex

**Key functions:** `add()`, `plot()`, `summary()`, `get_zeta_zeros()`, `V38_hofstadter_butterfly_dense()`, `V39_r_vs_alpha()`, `V40_r_vs_L()`, `V41_r_vs_W()`, `V42_r_vs_Nv()`, `V43_sigma2_dense()`, `V44_delta3_dense()`, `V45_R2_dense()`, `V46_form_factor()`, `V47_sigma_scan_dense()`, `V48_r_zeta_vs_N()`
  ... and 24 more

**Classes:** `ExtendedVerifier`

**Dependencies:** __future__, json, mpmath, numpy, os, python, sympy, sys, time, traceback

---

#### `verifier_core.py`

> verifier_core.py — Core verification engine for the monograph.
> 
> Contains the TaskRunner class that executes verification tasks, collects
> results, generates figures, and produces reports. Each task is a function
> that takes a Config and returns a TaskResult.
> 
> The suite contains 240+ tasks organized into 16 chapters:
>   Ch 1-2:  Analytical origin of b (Kirchhoff, Rodrigues)
>   Ch 3:    Selberg zeta and b
>   Ch 4:    Euler e identity, γ, C_K, C_s
>   Ch 5:    Anosov flow
>   Ch 6:    Smagorinsky/Kolmogorov constants
>   Ch 7:    b as phase rotation (Rodrigues formula)
>   Ch 8:    R

**Key functions:** `to_dict()`, `summary_line()`, `register_task()`, `decorator()`, `run_task()`, `run_chapter()`, `run_all()`, `save_results_json()`, `make_result()`

**Classes:** `TaskResult`, `TaskRunner`

**Dependencies:** __future__, config, dataclasses, json, numpy, pathlib, time, traceback, typing

---

### Topological Magnetism

#### `AB_Cloud_topological_magnetism_simulations.py`

> AB-Cloud: Topological Magnetism — Numerical Simulations
> =========================================================
> 
> Companion code to Appendix E of the AB-Cloud Monograph v12.
> Implements 7 numerical experiments that verify the topological theory
> of magnetism developed in the appendix.
> 
> Experiments
> -----------
> 1. mayer_vietoris      — Topological charge conservation under cutting (50 trials)
> 2. phase_quantization  — AB-phase histogram with 30 k·π/15 peaks
> 3. arf_phase_map       — Arf invariant ↔ phase correspondence for 64 spinor structures
> 4. temperature_curve   — M_Curi

**Key functions:** `experiment_mayer_vietoris()`, `experiment_phase_quantization()`, `experiment_arf_phase_map()`, `experiment_temperature_curve()`, `experiment_tumbling_transfer()`, `experiment_lattice_symmetry()`, `experiment_psl27_cyclotomic()`, `act()`, `normalize()`, `cycle_structure()`, `main()`

**Dependencies:** dataclasses, itertools, json, matplotlib, numpy, os, scipy, typing

---

### Advanced Analysis

#### `ab_cloud_advanced.py`

> ab_cloud_advanced.py
> ====================
> Advanced statistics for the AB-cloud verification suite:
> 
>     - Multifractal dimensions D_q ( Participation ratio )
>     - Localization length ξ(E) via Thouless formula
>     - Berry curvature Ω(k) and Chern number C
>     - Hall conductivity σ_xy vs filling
>     - Wigner-Dyson time-reversal / spin-orbit surmise comparisons
>     - GOE / GUE / GSE ratio statistics
>     - Number variance high-precision (Simpson 1e-8)
>     - Topological invariants from band structure
>     - Level attraction / repulsion diagnostic
>     - Long-range Dyson-Meh

**Key functions:** `participation_ratio()`, `r_ratio_distribution()`, `r_ratio_goe_pdfa()`, `r_ratio_gue_pdfa()`, `sigma2_GUE_high_precision()`, `spectral_compressibility()`, `mode_fluctuation_distribution()`, `Y2_GUE()`, `Y3_GUE()`, `level_repulsion_exponent()`, `r_q_moments()`, `berry_curvature_chern()`, `hall_conductivity_vs_filling()`, `inverse_participation_ratio()`, `R3_empirical()`
  ... and 9 more

**Dependencies:** __future__, ab_cloud_hamiltonian, ab_cloud_stats, numpy, os, scipy, sys

---

#### `ab_cloud_advanced_v2.py`

> ab_cloud_advanced.py
> ====================
> Advanced verification modules V87+ for the AB-Cloud monograph.
> 
> Contains the new "monumental" verification tasks the user asked for:
>   V87 - Renormalization group (RG) flow of <r> under Kadanoff block-spin
>   V88 - Lyapunov exponent of wavefunctions (Anderson localization diagnostic)
>   V89 - Multifractal spectrum D_q via box-counting (with q sweep)
>   V90 - Topological entanglement entropy (TEE) of eigenstates
>   V91 - Spectral form factor long-time ramp + plateau (GUE diagnostic)
>   V92 - Energy-resolved level velocity dE/dW (vortex ad

**Key functions:** `rg_block_spin()`, `lyapunov_exponent()`, `lyapunov_sweep_W()`, `multifractal_spectrum()`, `multifractal_Dq_sweep_alpha()`, `von_neumann_entropy()`, `topological_entanglement_entropy()`, `spectral_form_factor_long()`, `level_velocity_dW()`, `chiral_symmetry_score()`, `chiral_sweep_alpha()`, `central_charge_cft()`, `band_gap_alpha_sweep()`, `band_gap_W_sweep_at_half()`, `ipr_scaling()`
  ... and 4 more

**Dependencies:** dataclasses, numpy, time, typing

---

### Genus Universality

#### `ab_cloud_genus_universality.py`

> GENUS UNIVERSALITY STUDY: c=T(g) for g=2,3,4,5,6
> ==================================================
> Following the discovery that optimal c=T(g)=6 for g=3, we test:
>   1. Whether c=T(g)=g(g+1)/2 is optimal for OTHER genus values
>   2. Whether the formula W_k = π^(-2k) still works with c=T(g)
>   3. Whether the k_opt(n) pattern depends on g
> 
> Approach: simulate AB-cloud for hypothetical surfaces with genus g=2,4,5,6
> by using T(g) as the Choptuik coefficient. If the genus-universality holds,
> optimal c should equal T(g) for each g.
> 
> Also: explore the analytic formula for k_opt(n) 

**Key functions:** `T()`, `build_vortex_data()`, `hamiltonian_flow()`, `dH_dpsi_bar()`, `dH_dpsi()`, `jacobian_det()`, `generate_test_points()`, `test_config()`, `verify_Tg_optimality()`, `kopt_pattern_with_Tg()`, `find_analytic_formula()`, `fig_genus_universality()`, `fig_kopt_extended()`, `main()`

**Classes:** `VortexConfig`

**Dependencies:** __future__, dataclasses, matplotlib, numpy, os, typing

---

### Hybrid Approach

#### `ab_cloud_hybrid_approach.py`

> HYBRID APPROACH: Simplified AB-cloud Hamiltonian without geometry (Chapter 14 §14.21)
> ================================================================================
> Removes ALL geometric structure (τ, theta-functions, PSL(2,7)) and keeps only:
>   - AB-cloud Hamiltonian with N_v = n topological vortices
>   - Choptuik correction (1 - 1/π²) — justified arithmetically via ζ(2) = π²/6
>   - Simple rational potential V(ψ) = |ψ|² / (|ψ|² + 1)
> 
> The Choptuik correction is now justified ARITHMETICALLY (not geometrically):
>     (1 - 1/π²) = 1 - 1/(6·ζ(2)) = 1 - 1/π²
> as a universal arithmet

**Key functions:** `build_vortex_data()`, `simplified_potential()`, `geometric_potential()`, `hamiltonian_flow_hybrid()`, `dH_dpsi_bar()`, `dH_dpsi()`, `jacobian_det_hybrid()`, `generate_test_points()`, `verify_jc_4way()`, `run_all_dimensions()`, `fig_hybrid_vs_geometric()`, `fig_improvement_comparison()`, `main()`

**Classes:** `HybridConfig`

**Dependencies:** __future__, dataclasses, matplotlib, numpy, os, typing

---

### Robustness Study

#### `ab_cloud_robustness_study.py`

> ROBUSTNESS STUDY: W_k = π^(-2k) — stability across T_flow, r_k, n_test_points
> ================================================================================
> Following the discovery that W_k = π^(-2k) gives absolute JC (σ/|μ| < 0.04%)
> for n=1..6, we now verify ROBUSTNESS:
> 
>   1. T_flow stability: vary T_flow ∈ {0.01, 0.02, 0.05, 0.1, 0.2, 0.5} for each n
>   2. Position stability: vary seed for r_k ∈ {42, 100, 200, 314, 500, 1000}
>   3. Test-points stability: vary n_test_points ∈ {4, 8, 16, 32, 64}
> 
> Goal: confirm that the result is NOT a numerical artifact and holds robustly
> a

**Key functions:** `build_vortex_data()`, `hamiltonian_flow()`, `dH_dpsi_bar()`, `dH_dpsi()`, `jacobian_det()`, `generate_test_points()`, `test_config()`, `test_tflow_stability()`, `test_position_stability()`, `test_npoints_stability()`, `analytic_investigation()`, `fig_stability_tflow()`, `fig_stability_position()`, `fig_stability_npoints()`, `fig_analytic_decomposition()`
  ... and 1 more

**Classes:** `VortexConfig`

**Dependencies:** __future__, dataclasses, matplotlib, numpy, os, typing

---

### Statistics

#### `ab_cloud_stats.py`

> ab_cloud_stats.py
> =================
> Honest GUE/RMT statistics: ⟨r⟩, Σ²(L), Δ₃(L), p(s), R₂(s).
> 
> KEY FIXES vs v17:
> -----------------
> 1. ⟨r⟩ is computed BOTH with and without an energy window.  We print both.
>    The v17 'filtered' ⟨r⟩ = 0.59 was an artefact of the (3.0, 5.0) window +
>    edge_frac=0.30 cut.  The honest full-spectrum ⟨r⟩ is also reported.
> 
> 2. f_GUE is a TWO-SIDED criterion:  0.8 ≤ f_GUE ≤ 1.2.
>    v17 used 'f_GUE ≥ 0.80' which lets 'more rigid than GUE' (f_GUE > 1) PASS.
>    That is logically wrong: f_GUE > 1 means data < GUE, i.e. NOT GUE.
>    Here we test 

**Key functions:** `spacings_from_levels()`, `mean_level_spacing_ratio()`, `wigner_dyson_pdf()`, `sigma2_statistic()`, `delta3_statistic()`, `sigma2_GUE_exact()`, `delta3_GUE_exact()`, `f_gue_two_sided()`, `R2_empirical()`, `R2_GUE()`, `R2_Poisson()`, `chi_square_uniform()`, `ks_against_wigner_dyson()`, `bootstrap_mean()`, `sigma_r_bk_correct()`

**Dependencies:** __future__, numpy, scipy

---

#### `ab_cloud_stats_v2.py`

> ab_cloud_stats.py
> =================
> Statistical tools for GUE / Poisson comparison of eigenvalue spectra.
> 
> Implements:
> - Wigner-Dyson unfolding via polynomial fit to cumulative density
> - Riemann-von Mangoldt unfolding for zeta zeros
> - Nearest-neighbor spacing ratio r_n = min(d_n, d_{n+1}) / max(...)
> - Mean ratio <r> and GUE/Poisson reference values
> - Number variance Sigma^2(L), spectral rigidity Delta_3(L)
> - Nearest-neighbor spacing distribution p(s)
> - Two-level correlation R_2(s) and Montgomery's pair correlation
> - Spectral form factor K(t)
> - Dyson-Mehta statistic fo

**Key functions:** `polynomial_unfold()`, `riemann_von_mangoldt_unfold()`, `unfold()`, `spacing_ratios()`, `mean_spacing_ratio()`, `std_spacing_ratio()`, `spacing_distribution()`, `p_GUE()`, `p_GOE()`, `p_Poisson()`, `R2_GUE()`, `R2_Montgomery()`, `R2_Poisson()`, `empirical_R2()`, `number_variance()`
  ... and 11 more

**Dependencies:** numpy, scipy

---

### Parameter Sweeps

#### `ab_cloud_sweeps.py`

> ab_cloud_sweeps.py
> ==================
> Dense parameter-sweep infrastructure for the AB-cloud verification suite.
> 
> This module provides vectorised helpers for performing parameter sweeps
> across many values of:
>     - α  (flux per plaquette)
>     - W  (vortex/disorder strength)
>     - L  (linear lattice size)
>     - N_v (number of vortices)
>     - L_statistic  (window size for Σ², Δ₃)
>     - s  (pair correlation argument)
>     - τ  (form factor argument)
>     - σ  (scaling parameter)
>     - N_ζ  (number of Riemann zeros)
> 
> Every sweep returns a dict of arrays suitable for pl

**Key functions:** `sweep_r_vs_alpha()`, `sweep_r_vs_L()`, `sweep_r_vs_W()`, `sweep_r_vs_Nv()`, `sweep_sigma2()`, `sweep_delta3()`, `sweep_R2()`, `spectral_form_factor()`, `sweep_sigma_scan()`, `sweep_r_zeta_vs_N()`, `sweep_hofstadter_spectrum()`, `sweep_spacing_pdf()`, `spacing_moments()`, `sweep_chi2_alpha_W()`, `idos_spectrum()`
  ... and 4 more

**Dependencies:** __future__, ab_cloud_hamiltonian, ab_cloud_stats, ab_cloud_zeta, numpy, os, scipy, sys, time, typing

---

#### `ab_cloud_sweeps_v2.py`

> ab_cloud_sweeps.py
> ==================
> Massive parameter sweep infrastructure for AB-Cloud verification.
> 
> This module provides the "monumental" infrastructure the user asked for:
> - Dense sweeps over alpha, W, L, N_vortices, sigma
> - Multiple disorder realizations per parameter point (with statistical averaging)
> - Returns aggregated statistics with standard errors
> - Designed for thousands of parameter combinations
> 
> Each sweep returns a SweepResult dataclass with:
> - param_grid: dict of arrays
> - statistics: dict of arrays (mean over realizations)
> - raw_data: list of dicts 

**Key functions:** `to_dict()`, `sweep_alpha()`, `sweep_W()`, `sweep_L()`, `sweep_sigma()`, `sweep_alpha_W_2d()`, `sweep_L_sigma_2d()`, `sweep_alpha_L_2d()`

**Classes:** `SweepResult`

**Dependencies:** dataclasses, itertools, numpy, time, typing

---

### Vortex Analysis

#### `ab_cloud_vortex_fine_search.py`

> EXPLORATORY V2: Fine-grained search around 1/π² for absolute JC proof
> =========================================================================
> Following the discovery that W_k = 1/π² gives σ/|μ| = 2.30% for n=1 (absolute
> JC!), we do a fine-grained search around 1/π² and related values to find the
> optimal configuration for n=2,3,4,5,6.
> 
> Strategy:
>   1. Vary W around 1/π² with fine resolution
>   2. Try mixed configurations: W_k = c_k / π² with c_k ∈ {1, 2, 3, 4, 5, 6, 7, 13}
>   3. Try W_k = log(k)/π² for various k
>   4. Try W_k = 1/(π²·k) for various k
>   5. Try position-depend

**Key functions:** `build_vortex_data()`, `hamiltonian_flow()`, `dH_dpsi_bar()`, `dH_dpsi()`, `jacobian_det()`, `generate_test_points()`, `test_config()`, `generate_fine_candidates()`, `fine_search_all_n()`, `main()`

**Classes:** `VortexConfig`

**Dependencies:** __future__, dataclasses, matplotlib, numpy, os, typing

---

#### `ab_cloud_vortex_powers_final.py`

> EXPLORATORY V3: Find optimal π^(-2k) for n=4 and confirm absolute JC for all n
> ================================================================================
> Following the discovery that W_k = π^(-8) gives absolute JC (σ/|μ| < 5%) for
> n=1,2,3,5,6, we now:
>   1. Search higher powers π^(-2k) for k = 4..20 to find the best for n=4
>   2. Try position configurations for n=4
>   3. Confirm the result for all n with the optimal k
>   4. Generate a clean summary figure for inclusion in the document

**Key functions:** `build_vortex_data()`, `hamiltonian_flow()`, `dH_dpsi_bar()`, `dH_dpsi()`, `jacobian_det()`, `generate_test_points()`, `test_config()`, `search_powers()`, `fig_powers_summary()`, `fig_final_summary()`, `main()`

**Classes:** `VortexConfig`

**Dependencies:** __future__, dataclasses, matplotlib, numpy, os, typing

---

#### `ab_cloud_vortex_search.py`

> EXPLORATORY: Vortex numerical values for absolute JC proof (Chapter 14 research)
> =================================================================================
> Systematically searches over numerical values assigned to vortices to find
> configurations that give the BEST JC verification (σ/|μ| → 0).
> 
> Hypothesis: assigning special numerical values to vortices (like log(13), log(7),
> π, e, √2, ζ(2), etc.) may stabilize the Hamiltonian flow and yield configurations
> where JC holds absolutely (not just conditionally).
> 
> Each vortex is parameterized as:
>     vortex_k = (q_k, r_k, α_

**Key functions:** `build_vortex_data_with_anchors()`, `hamiltonian_flow_anchored()`, `dH_dpsi_bar()`, `dH_dpsi()`, `jacobian_det_anchored()`, `generate_test_points()`, `test_config()`, `generate_candidates()`, `search_all_n()`, `fig_best_per_n()`, `main()`

**Classes:** `VortexConfig`

**Dependencies:** __future__, dataclasses, matplotlib, numpy, os, typing

---

### 3D NSE

#### `ab_cloud_3d.py`

> AB-CLOUD 3D — Unified Preprint Verification File (PYTHON PORT, RUSSIAN UI)
> =========================================================================
> 
> Один-в-один порт ab_cloud_3d.jl на Python 3. Запускается так:
>     python3 ab_cloud_3d.py
> 
> Возможности (полное соответствие Julia-версии):
>   • 10 режимов (A–J): 3D-солвер, RMT-анализ нулей, FSS, Arf, Decay-time,
>     Dirac/QED, Full verification, Deep zeros, 3D Bridge, Advanced 3D.
>   • 5000 встроенных нулей дзета-функции Римана (из Odlyzko tables).
>   • Нули n > 5000 вычисляются с ИДЕАЛЬНОЙ ТОЧНОСТЬЮ через mpmath.siegelz
>     (п

**Key functions:** `riemann_siegel_theta()`, `riemann_siegel_Z()`, `nth_riemann_zero()`, `load_embedded_zeros()`, `default_config()`, `parse_float_unlimited()`, `parse_int_unlimited()`, `parse_int3_unlimited()`, `build_hamiltonian_3d()`, `idx()`, `run_3d_simulation()`, `riemann_von_mangoldt_N()`, `unfold_zeta_zeros()`, `unfold_ab_cloud()`, `gue_cdf()`
  ... and 19 more

**Classes:** `SimConfig`

**Dependencies:** argparse, cmath, dataclasses, datetime, json, math, matplotlib, mpl_toolkits, mpmath, numpy, os, pathlib, re, scipy, sys, typing

---

#### `ab_cloud_3d_en.py`

> AB-CLOUD 3D — Unified Preprint Verification File (PYTHON PORT, ENGLISH UI)
> =========================================================================
> 
> One-to-one port of ab_cloud_3d.jl to Python 3. Run as:
>     python3 ab_cloud_3d.py
> 
> Features (full parity with the Julia version):
>   • 10 modes (A–J): 3D solver, RMT analysis of zeros, FSS, Arf, Decay-time,
>     Dirac/QED, Full verification, Deep zeros, 3D Bridge, Advanced 3D.
>   • 5000 embedded Riemann zeta zeros (from Odlyzko tables).
>   • Zeros n > 5000 are computed with PERFECT ACCURACY via mpmath.siegelz
>     (sequential sig

**Key functions:** `riemann_siegel_theta()`, `riemann_siegel_Z()`, `nth_riemann_zero()`, `load_embedded_zeros()`, `default_config()`, `parse_float_unlimited()`, `parse_int_unlimited()`, `parse_int3_unlimited()`, `build_hamiltonian_3d()`, `idx()`, `run_3d_simulation()`, `riemann_von_mangoldt_N()`, `unfold_zeta_zeros()`, `unfold_ab_cloud()`, `gue_cdf()`
  ... and 19 more

**Classes:** `SimConfig`

**Dependencies:** argparse, cmath, dataclasses, datetime, json, math, matplotlib, mpl_toolkits, mpmath, numpy, os, pathlib, re, scipy, sys, typing

---

#### `generate_3d_nse_figures.py`

> Generate all 3D NSE figures from saved partial results.

**Dependencies:** kdv_core, matplotlib, mpl_toolkits, nse3d_core, numpy, pathlib, run_experiments, scipy, sys

---

#### `nse3d_core.py`

> nse3d_core.py — 3D Navier-Stokes solver in vorticity form.
> 
> Solves the 3D NSE in vorticity form:
>     ω_t + (u·∇)ω = (ω·∇)u + ν·Δω,   ∇·u = 0
> 
> where ω = ∇ × u is the vorticity. The velocity is reconstructed from
> vorticity via the Biot-Savart relation in Fourier space:
>     û(k) = i·(k × ω̂(k)) / |k|²   (for k ≠ 0; û(0) = 0)
> 
> Key features:
>     - Pseudo-spectral method (3D FFT) with 2/3 Orszag dealiasing
>     - Integrating Factor RK4 (IFRK4) for the viscous term ν·Δω
>     - Periodic boundary conditions on [0, 2π]³
>     - The vorticity equation automatically preserves ∇·ω = 0

**Key functions:** `make_grid_3d()`, `dealias_mask_3d()`, `velocity_from_vorticity()`, `curl()`, `taylor_green_vortex()`, `abc_flow()`, `kinetic_energy()`, `vorticity_norm_inf()`, `vorticity_norm_rms()`, `energy_spectrum()`, `rodrigues_3d_rotation()`, `verify_rodrigues_orthogonality()`, `nse_rhs_vorticity()`, `nse_ifrk4_step()`, `compute_u()`
  ... and 3 more

**Dependencies:** __future__, kdv_core, numpy, scipy, time

---

#### `run_3d_nse_stepwise.py`

> Run 3D NSE experiments one model at a time, saving partial results.

**Dependencies:** nse3d_core, numpy, pathlib, scipy, sys

---

### KdV Solver

#### `kdv_core.py`

> kdv_core.py — Core KdV solver with three b-rotation mechanisms.
> 
> Implements:
>   - Pseudo-spectral KdV solver (FFT + RK4 + 2/3 dealiasing)
>   - Three b-rotation mechanisms (spectral / Rodrigues / modified-nonlinearity)
>   - Five competing models (true KdV + 4 b-modifications)
>   - Invariant computation (mass, momentum, energy)
>   - Analytical soliton solutions and 2-soliton phase-shift formulas
> 
> Author: Z.ai Research, 2026 (companion to monograph chapter 16)

**Key functions:** `make_grid()`, `dealias_mask()`, `sech2()`, `single_soliton()`, `two_solitons()`, `three_solitons()`, `invariants()`, `hilbert_fft()`, `apply_M1_spectral()`, `apply_M2_rodrigues()`, `kdv_rhs_M3_modified()`, `ifrk4_step()`, `integrate()`, `two_soliton_phase_shifts()`

**Dependencies:** __future__, numpy, scipy

---

### KP Solver

#### `kp_solver.py`

> kp_solver.py — 2D Kadomtsev-Petviashvili (KP) solver with b-mechanisms.
> 
> KP is the 2D generalization of KdV:
>     ∂_x(u_t + 6u·u_x + u_xxx) + 3·σ²·u_yy = 0
> 
> where σ² = +1 for KP-II (most common, line solitons stable),
>       σ² = -1 for KP-I (lump solitons exist).
> 
> In Fourier space (kx ≠ 0):
>     û_t = -3ik_x·F(u²) + ik_x³·û + 3i·σ²·k_y²/k_x·û
> 
> Linear part: L(kx, ky) = i·(k_x³ + 3·σ²·k_y²/k_x)
>     - For kx → 0: L → ∞ (singular).  We handle kx = 0 modes specially.
>     - |L| ~ k_x³ for large k_x (similar to KdV) — IFRK4 needed.
> 
> For the b-mechanisms (M1, M2, M3):
>    

**Key functions:** `make_grid_2d()`, `dealias_mask_2d()`, `kp_line_soliton()`, `kp_lump_soliton()`, `kp_invariants()`, `kp_rhs()`, `kp_ifrk4_step()`, `N()`, `kp_apply_M1_spectral()`, `kp_apply_M2_rodrigues()`, `hilbert_x()`, `kp_rhs_M3_modified()`, `kp_make_models()`, `integrate_kp()`

**Dependencies:** __future__, kdv_core, numpy, scipy

---

### Isospectral

#### `isospectral_b.py`

> isospectral_b.py — Isospectral b-modification via Darboux/Bäcklund
> transformation, with Wilson RG interpretation.
> 
> This module addresses Open Question 1 of §16.22 of the monograph:
> 
>     "Существует ли модифицированная Lax-пара, в которой b-поворот
>      включён изоспектрально (через калибровочное преобразование)?"
> 
> Answer: YES.  The Darboux transformation provides a continuous family
> of isospectral potentials parameterized by an angle θ.  When θ = θ_b
> (the universal polarization angle), this gives an ISOSPECTRAL b-
> modification that preserves the Lax spectrum to machine pr

**Key functions:** `build_lax_matrix()`, `lax_spectrum()`, `off_diag_value()`, `main_diag_value()`, `darboux_transform()`, `darboux_transform_discrete()`, `darboux_transform_spectral()`, `kdv_hierarchy_K1()`, `kdv_hierarchy_K2()`, `isospectral_b_rotation()`, `isospectral_b_rotation_rk4()`, `F()`, `verify_isospectrality()`, `wilson_rg_step()`, `rg_flow()`
  ... and 6 more

**Dependencies:** __future__, kdv_core, numpy, scipy, the

---

### Polchinski RG

#### `polchinski_rg.py`

> polchinski_rg.py — Polchinski-style continuous RG flow for KdV.
> 
> Addresses the limitation noted in §16.24: discrete K_2 steps accumulate
> high-k noise after 2-3 applications, preventing iterated RG recursion.
> 
> Polchinski's insight (1984): instead of discrete RG steps with hard
> cutoffs, use a CONTINUOUS flow equation with a smooth, θ-dependent
> cutoff kernel.  This allows arbitrarily many "RG steps" (small δθ
> increments) without noise accumulation.
> 
> The flow equation:
>     ∂u_θ(k)/∂θ = χ(k/Λ(θ)) · K_2(u_θ)(k)
> 
> where:
>     χ(s) = exp(-s²)                — smooth Gaussian 

**Key functions:** `polchinski_cutoff()`, `running_cutoff()`, `polchinski_rhs()`, `polchinski_flow_step()`, `F()`, `integrate_polchinski_rg()`, `compare_discrete_vs_polchinski()`

**Dependencies:** __future__, isospectral_b, kdv_core, numpy, scipy

---

### Extended Solvers

#### `extended_solvers.py`

> extended_solvers.py — Solvers for mKdV, BBM, and Kawahara equations.
> 
> All three extend the KdV framework of kdv_core.py to non-integrable
> and higher-order dispersive regimes, with the same three b-mechanisms
> (M1 spectral, M2 Rodrigues in (u, u_x), M3 modified nonlinearity).
> 
> Equations:
>   mKdV      : u_t + 6·u²·u_x + u_xxx = 0       (integrable, Miura→KdV)
>   BBM       : u_t + u_x + u·u_x − u_xxt = 0    (non-integrable, regularized)
>   Kawahara  : u_t + 6·u·u_x + u_xxx + u_xxxxx = 0  (5th-order, oscillatory solitons)
> 
> Author: Z.ai Research, 2026 (companion to monograph chapt

**Key functions:** `mkdv_nonlinear_term()`, `mkdv_invariants()`, `mkdv_soliton()`, `mkdv_bright_soliton()`, `mkdv_make_models()`, `bbm_linear_factor()`, `bbm_nonlinear_term()`, `bbm_invariants()`, `bbm_soliton()`, `bbm_make_models()`, `kawahara_nonlinear_term()`, `kawahara_invariants()`, `kawahara_soliton()`, `kawahara_make_models()`, `ifrk4_step_general()`
  ... and 1 more

**Dependencies:** __future__, kdv_core, numpy, scipy

---

### Full Simulation

#### `full_AB_simulation.py`

> TASK 3: FULL AB-CLOUD SIMULATION WITH KERR-SCHWARZSCHILD METRIC
> =================================================================
> Build a complete numerical simulation of the AB-cloud using:
> - Kerr-Schwarzschild metric (rotating + non-rotating)
> - Hofstadter Hamiltonian on the Klein quartic graph
> - All 4 CPT-violation signatures
> 
> Simulation components:
> 1. Build AB-cloud Hamiltonian on Klein graph (56 vertices, d=3)
> 2. Apply Kerr-Schwarzschild deformation (parameter a_AB = 2α-1)
> 3. Compute spectrum at various α (rotation parameter)
> 4. Verify 4 CPT-violation signatures:
>   

**Key functions:** `mat_mul()`, `canonical()`, `psl_mul()`, `psl_inv()`, `order_of()`, `build_AB_hamiltonian()`, `compute_level_spacings()`, `gue_conformity()`

**Dependencies:** itertools, json, math, matplotlib, numpy, scipy

---

### Report Generator

#### `generate_report.py`

> generate_report.py — Generates the bilingual DOCX report (Chapter 16 of the
> monograph): Russian text + English figure captions.
> 
> Output: /home/z/my-project/download/KdV_b_correction_Chapter16.docx

**Key functions:** `setup_document()`, `add_para()`, `add_rich_para()`, `add_figure()`, `add_table()`, `add_page_break()`, `build_report()`, `build_report_part2()`, `build_report_part3()`, `build_report_part4()`, `build_report_part5()`

**Dependencies:** __future__, docx, json, kdv_core, monograph_constants, os, pathlib, sys

---

#### `generate_report_v2.py`

> generate_report.py — Generates the bilingual DOCX report (Chapter 16 of the
> monograph): Russian text + English figure captions.
> 
> Output: /home/z/my-project/download/KdV_b_correction_Chapter16.docx

**Key functions:** `setup_document()`, `add_para()`, `add_rich_para()`, `add_figure()`, `add_table()`, `add_page_break()`, `build_report()`, `build_report_part2()`, `build_report_part3()`, `build_report_part4()`, `build_report_part5()`, `build_report_extensions()`

**Dependencies:** __future__, docx, json, kdv_core, monograph_constants, os, pathlib, sys

---

#### `generate_report_v3.py`

> generate_report.py — Generates the bilingual DOCX report (Chapter 16 of the
> monograph): Russian text + English figure captions.
> 
> Output: /home/z/my-project/download/KdV_b_correction_Chapter16.docx

**Key functions:** `setup_document()`, `add_para()`, `add_rich_para()`, `add_figure()`, `add_table()`, `add_page_break()`, `build_report()`, `build_report_part2()`, `build_report_part3()`, `build_report_part4()`, `build_report_part5()`, `build_report_extensions()`, `build_report_polchinski_kp()`

**Dependencies:** __future__, docx, json, kdv_core, monograph_constants, os, pathlib, sys

---

#### `generate_report_v4.py`

> generate_report.py — Generates the bilingual DOCX report (Chapter 16 of the
> monograph): Russian text + English figure captions.
> 
> Output: /home/z/my-project/download/KdV_b_correction_Chapter16.docx

**Key functions:** `setup_document()`, `add_para()`, `add_rich_para()`, `add_figure()`, `add_table()`, `add_page_break()`, `build_report()`, `build_report_part2()`, `build_report_part3()`, `build_report_part4()`, `build_report_part5()`, `build_report_extensions()`, `build_report_polchinski_kp()`, `build_report_3d_nse()`

**Dependencies:** __future__, docx, json, kdv_core, monograph_constants, os, pathlib, sys

---

### Experiment Runner

#### `run_all_75_tasks.py`

> run_all_75_tasks.py
> Запуск ВСЕХ 75 задач монографии.
> Run ALL 75 monograph tasks.
> 
> Использование / Usage:
>     python3 run_all_75_tasks.py

**Key functions:** `main()`

**Dependencies:** monograph_verification, monograph_verification_part2, monograph_verification_part3, pathlib, sys, time

---

#### `run_batched.py`

> run_batched.py
> ==============
> Run all 99 verifications in batches, saving intermediate results after each batch.
> This avoids the issue of long-running processes being killed mid-execution.
> 
> Each batch is saved to results/data/batches/batch_NN.json. After all batches
> complete, the batches are merged into verification_report.json and
> verification_summary.md.

**Key functions:** `run_batch()`, `merge_batches()`, `main()`

**Dependencies:** argparse, gc, json, pathlib, python, sys, time

---

#### `run_experiments.py`

> run_experiments.py — Runs all 15 KdV experiments with the b-correction
> and generates the 25+ professional figures (English labels) for the
> report (chapter 16 of the monograph).
> 
> Output:
>     /home/z/my-project/download/figures/*.png     (45 figures)
>     /home/z/my-project/download/results.json      (numerical results)
> 
> Experiments:
>     E1   Single soliton, baseline (no b)
>     E2   Single soliton + M1 (spectral b-shift)
>     E3   Single soliton + M2 (Rodrigues in (u, u_x))
>     E4   Single soliton + M3 (modified nonlinearity)
>     E5   Two-soliton collision, no b
>     E6 

**Key functions:** `save_fig()`, `exp_E1_baseline()`, `exp_E2_E4_three_mechanisms()`, `exp_E5_two_soliton_baseline()`

**Dependencies:** __future__, json, kdv_core, matplotlib, monograph_constants, numpy, os, pathlib, scipy, sys, time

---

#### `run_experiments_final.py`

> Run only E15 (universality) and generate final summary figures.

**Key functions:** `exp_E15_universality()`, `fig_16_45_monograph_verification()`, `fig_16_46_energy_surface()`, `fig_16_47_radar_chart()`, `fig_16_48_spectrum()`

**Dependencies:** kdv_core, matplotlib, monograph_constants, numpy, pathlib, run_experiments, scipy, sys

---

#### `run_experiments_part2.py`

> run_experiments_part2.py — Experiments E6-E15 (continuation of run_experiments.py)
> 
> Runs the remaining 10 experiments and generates the corresponding figures.

**Key functions:** `exp_E6_collision_with_b()`, `exp_E9_five_model_comparison()`, `exp_E10_angle_scan()`, `exp_E12_long_time()`, `exp_E15_universality()`

**Dependencies:** __future__, json, kdv_core, matplotlib, numpy, os, pathlib, run_experiments, scipy, sys, time

---

#### `run_extended_experiments.py`

> run_extended_experiments.py — Experiments E16-E20:
>   - E16: mKdV + b (3 mechanisms)
>   - E17: BBM + b (non-integrable case)
>   - E18: Kawahara + b (5th-order, oscillatory solitons)
>   - E19: Isospectral b verification (K_2 flow, single-step gauge)
>   - E20: Wilson RG interpretation (cumulative RG steps, scale invariance)
> 
> Generates figures 16.49 - 16.62 (English labels).

**Key functions:** `exp_E16_mkdv()`, `exp_E17_bbm()`, `exp_E18_kawahara()`, `exp_E19_isospectral()`, `exp_E20_wilson_rg()`

**Dependencies:** __future__, extended_solvers, isospectral_b, json, kdv_core, matplotlib, numpy, os, pathlib, run_experiments, scipy, sys, time

---

#### `run_final_extensions.py`

> run_final_extensions.py — Experiments E21-E24:
>   E21: Polchinski-K_1 RG flow (10, 20, 50 steps) — iterated RG
>   E22: KP-II line soliton + 3 b-mechanisms
>   E23: KP-I lump soliton + b-mechanisms (2D localized)
>   E24: Discrete K_2 vs Polchinski-K_1 comparison (10 steps)
> 
> Generates figures 16.60 - 16.72 (English labels).

**Key functions:** `exp_E21_polchinski_iterated()`, `exp_E22_kp_line_soliton()`, `exp_E23_kp_lump_soliton()`, `exp_E24_discrete_vs_polchinski()`

**Dependencies:** __future__, isospectral_b, json, kdv_core, kp_solver, matplotlib, mpl_toolkits, numpy, os, pathlib, polchinski_rg, run_experiments, scipy, sys, time

---

#### `run_monumental.py`

> run_monumental.py
> =================
> Master runner for AB-Cloud monograph verification — monumental edition.
> 
> Executes 60+ verification tasks (V1-V96) with parameter sweeps, generates
> PNG plots for each, and produces a final JSON report.
> 
> Usage:
>     cd /home/z/my-project/download/ab_cloud_monumental
>     python -m python.run_monumental            # full run
>     python -m python.run_monumental --quick    # quick smoke test

**Key functions:** `register()`, `v01()`, `v02()`, `v03()`, `v04()`, `v05()`, `v06()`, `v07()`, `v08()`, `v09()`, `v10()`, `v11()`, `v12()`, `v13()`, `v14()`
  ... and 20 more

**Classes:** `_R`

**Dependencies:** argparse, gc, json, numpy, pathlib, python, sys, time, traceback, typing

---

### Configuration

#### `config.py`

> config.py — Configuration system for the monograph verification suite.
> 
> Provides a Config dataclass with all adjustable parameters, loaded from
> JSON config files. Users can create custom configs to run specific
> chapters, adjust grid sizes, time horizons, etc.
> 
> Usage:
>     from config import Config
>     cfg = Config.default()          # default configuration
>     cfg = Config.from_json("config/my_config.json")
>     cfg.N_kdv = 2048                 # override individual parameters
>     cfg.save_json("config/my_config.json")

**Key functions:** `default()`, `from_json()`, `save_json()`, `to_dict()`, `summary()`, `get_preset()`

**Classes:** `Config`

**Dependencies:** __future__, config, dataclasses, json, math, pathlib, typing

---

### Data Collection

#### `collect_summary_data.py`

> Quick re-run of E6, E9, E10, E12 to save numerical summary data.

**Key functions:** `rerun_E9()`, `rerun_E6()`, `rerun_E10()`, `rerun_E12()`

**Dependencies:** kdv_core, numpy, pathlib, run_experiments, scipy, sys

---

### Parametric Tasks

#### `tasks_parametric.py`

> tasks_parametric.py — Parametric scan tasks (50+ additional tasks).
> 
> These tasks perform systematic parameter scans to verify robustness
> of the monograph's claims across a range of parameters.

**Key functions:** `task_P_01_b_scan_001()`, `task_P_02_b_scan_005()`, `task_P_03_b_scan_00785()`, `task_P_04_b_scan_015()`, `task_P_05_b_scan_030()`, `task_P_06_b_scan_050()`, `task_P_07_theta_b_scan()`, `task_P_08_theta_b_degrees_scan()`, `task_P_09_theta_b_plot()`, `task_P_10_soliton_c_scan()`, `task_P_11_soliton_velocity_scan()`, `task_P_12_soliton_width_scan()`, `task_P_13_grid_N256()`, `task_P_14_grid_N512()`, `task_P_15_grid_N1024()`
  ... and 25 more

**Dependencies:** __future__, config, kdv_core, matplotlib, monograph_constants, numpy, pathlib, sys, verifier_core

---

### Large Matrix Demo

#### `large_matrix_demo.py`

> examples/large_matrix_demo.py
> ==============================
> Demonstration of large-matrix AB-Cloud verification (L=70, 84).
> 
> Shows:
> 1. Building L=70 and L=84 Hamiltonians (monumental matrices)
> 2. Computing <r> at the optimal point
> 3. Comparing with GUE reference
> 4. Generating Hofstadter butterfly
> 5. Computing spectral form factor K(t)

**Key functions:** `main()`

**Dependencies:** numpy, pathlib, python, sys, time

---

### Quick Start

#### `quick_start.py`

> examples/quick_start.py
> ========================
> Quick start example for the AB-Cloud monumental verification codebase.
> 
> Shows how to:
> 1. Build the AB-Cloud Hamiltonian with real vortices
> 2. Diagonalize and compute GUE statistics
> 3. Run a parameter sweep
> 4. Generate a plot

**Key functions:** `main()`

**Dependencies:** numpy, pathlib, python, sys

---

### Package Init

#### `__init__.py`

---

#### `__init___v2.py`

> ab_cloud_monumental python package.

---

### Other

#### `ab_cloud_extended_kopt_study.py`

> EXTENDED STUDY: k_opt(n) for n=1..10 + Choptuik correction variations
> =======================================================================
> Following user's intuition:
>   - Odd n: k=4 (one Hamiltonian cycle)
>   - Even n: k=14 (more cycles due to rotation/twist)
>   - n=5,6: regime change (beyond main JC, n<=3)
> 
> We:
>   1. Extend k_opt search to n=1..10 to see the full pattern
>   2. Try to find analytic formula k_opt(n) via regression
>   3. Test user's hypothesis: odd/even parity pattern
>   4. Vary Choptuik correction: (1 - c/π²) for c ∈ {0.5, 1, 2, 3, 6, 12, 24}
>   5. Test "log

**Key functions:** `build_vortex_data()`, `hamiltonian_flow()`, `dH_dpsi_bar()`, `dH_dpsi()`, `jacobian_det()`, `generate_test_points()`, `test_config()`, `find_k_opt()`, `extended_kopt_search()`, `find_analytic_formula()`, `zeta_func()`, `variable_choptuik_study()`, `log_power_study()`, `combined_optimization()`, `fig_kopt_pattern()`
  ... and 3 more

**Classes:** `VortexConfig`

**Dependencies:** __future__, dataclasses, matplotlib, mpmath, numpy, os, typing

---
