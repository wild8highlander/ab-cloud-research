# SUMMARY · RH_Auto_5000_L64_s5_20261016_122739

```json
{
  "alpha": 0.3183098861837907,
  "W": 2.0,
  "sigma": 0.5,
  "L": 64,
  "n_seeds": 5,
  "eigs_per_seed": 1228,
  "n_eigs": 6140,
  "n_zeta_zeros": 5000,
  "r_mean": 0.59999,
  "r_std": 0.007093,
  "r_class": "GUE",
  "d_GUE": 0.00039,
  "R2_rms_GUE": 0.020975,
  "R2_rms_Poisson": 0.258933,
  "R2_rms_zeta": 0.024521,
  "K_corr_GUE": 0.988179,
  "K_corr_zeta": 0.941722,
  "Sigma2_rms_GUE": 0.394604,
  "Sigma2_rms_Poisson": 5.431828,
  "Delta3_rms_GUE": 0.162915,
  "p_rms_GUE": 0.016674,
  "chi2_wigner": 0.113724,
  "chi2_score_exp": 0.944724,
  "brody_beta": 1.718303,
  "spectral_compressibility": 0.083558,
  "gap_prob_E1": 0.520917,
  "r_tilde_mean": 0.361317,
  "level_number_dev": 0.871468,
  "symmetry_parameter": 1.49994,
  "composite_score": 84.846,
  "tests_passed": 10,
  "tests_total": 11,
  "vortex_layout": "hexagonal",
  "n_vortices": 6,
  "jitter_all_zero": true,
  "verdicts": {
    "r_near_GUE": true,
    "R2_closer_GUE_than_Poisson": true,
    "K_corr_zeta_above_0.8": true,
    "Sigma2_closer_GUE_than_Poisson": true,
    "Delta3_below_0.5": true,
    "p_rms_below_0.2": true,
    "chi2_below_0.5": true,
    "brody_2_pm_0.5": true,
    "compressibility_below_0.3": true,
    "gap_E1_0.171_pm_0.15": false,
    "r_tilde_0.3602_pm_0.05": true
  },
  "environment": "not captured by the original run (see config.json)",
  "source": "audit of RH_Auto_5000_L64_s5_20261016_122739.zip · 2026-10-16",
  "tool": "RH_Sweep_Pro_Enrichment v1.0"
}
```

Примечания. `chi2_score_exp` = exp(−χ²/2) — монотонная мера согласия,
не p-value. `gap_prob_E1` — единственный непройденный тест. Кривые для
независимого пересчёта создаются скриптом `example_post_run.jl`
(P1); GUE-пол — `gue_floor_control(64, 5)`.
