# figures/ — Publication figures (600 dpi) + animation

| File | Test | Content |
|---|---|---|
| `fig_D1_dirac_cone.png` | D1 | π-flux bands through the cone · E₁(1/L) fit · lattice tower vs Dirac shells |
| `fig_D2_zero_tower.png` | D2 | Tower count = 4 ∀L · machine-precision pinning |
| `fig_D3_berry_phase.png` | D3 | Berry curvature map (4 π-peaks) · Wilson-loop winding to π |
| `fig_D4_landau_levels.png` | D4 | Dirac ladders E_n² ∝ n (3 fields) · Schrödinger control · lattice n=0 LL |
| `fig_D5_klein_tunneling.png` | D5 | T(θ) Dirac vs Schrödinger · packet mid-flight |
| `fig_D6_zitterbewegung.png` | D6 | ⟨x(t)⟩ trembling (ω = 2E₁) · torus dipole oscillation |
| `fig_D7_zeta_decoration.png` | D7 | Clean/ζ spectra · ⟨r⟩ bars vs GUE/GOE · E₁·L → 4π |
| `fig_D8_chiral_symmetry.png` | D8 | E ↔ −E paired spectrum of the ζ-decorated lattice |
| `fig_D9_index_restoration.png` | D9 | Wall-mode density maps (bare / in ζ cloud) · kernel census · restoration contrast 7×10⁶ |
| `fig_D10_montgomery_transport.png` | D10 | Pair correlation vs Montgomery · number variance · transport R/T bars · momentum fingerprint |
| `fig_D11_berry_keating.png` | D11 | BK staircase residual on the real zeros · Dirichlet trace comb · drive form factor vs GUE/Poisson · transport along the dilation orbit |
| `fig_D12_bk_ladder_infinite.png` | D12 | comb → Connes delta train (Dirichlet envelope over 2 decades of N_u) · zero-window coverage · ⟨r⟩(L) at fixed density vs clean/random · GUE ramp of the L = 48 cloud |
| `fig_D13_wall_under_drive.png` | D13 | wall mode vs the two drives (orbit pinned 3.9e-9 / generator band gap/679) · adiabatic fidelity & localization along the orbit · quasi-zero band vs isolation scale |
| `fig_D14_odlyzko_form_factor.png` | D14 | K(τ) main band vs GUE/synthetic control/Poisson · Odlyzko band t ≈ 1e5 vs low band · ramp region τ ≤ 0.75 · K(0.5) across the channels |
| `anim_D5_klein.gif` | D5 | Animated Klein crossing (mid-flight frames) |

All PNGs are 600 dpi and embed directly into the LaTeX and DOCX monograph
editions. Every test folder in [`../tests/`](../tests/) additionally carries its
own focused figure set (the canonical panel + companion panels recomputed from
the same modules and seed) next to its per-test monograph.

Regenerate: `python3 ../code/dirac_lab.py` + `python3 ../code/dirac_lab_extensions.py`
+ `python3 ../code/dirac_lab_extensions2.py` + `python3 ../code/dirac_lab_extensions3.py`
(figures are written automatically during the runs, 600 dpi throughout).
