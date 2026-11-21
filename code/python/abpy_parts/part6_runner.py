

# ═══════════════════════════════════════════════════════════════════════════
# 18. TEST REGISTRY, TWO-PASS RUNNER, REPORT, CLI
# ═══════════════════════════════════════════════════════════════════════════

LEDGER: List[Dict] = []


def log_result(line: str) -> None:
    print(line)
    LEDGER.append(line)


TESTS: Dict[int, Dict] = {}


def register(tid: int, name: str, slug: str, primary, hardcore=None,
             third: Optional[List] = None, self_second: bool = False):
    TESTS[tid] = {"name": name, "slug": slug, "primary": primary,
                  "hardcore": hardcore, "third": third or [],
                  "self_second": self_second}


register(1, "b(N) Convergence Table", "test_01_bN_convergence",
         test1_convergence_table, test1b_convergence_hardcore)
register(2, "Monotonicity Check", "test_02_bN_monotonicity",
         test2_monotonicity, test2b_monotonicity_hardcore)
register(3, "Convergence Rate (power-law fit)", "test_03_bN_rate",
         test3_convergence_rate, test3b_rate_hardcore)
register(4, "GUE KS Test (Full Range)", "test_04_gue_ks_full",
         test4_gue_ks_full, test4b_gue_ks_full_hardcore)
register(5, "GUE KS Test (High-T Only)", "test_05_gue_ks_highT",
         test5_gue_ks_highT, test5b_gue_ks_highT_hardcore)
register(6, "χ² Histogram Test", "test_06_chi2_hist",
         test6_chi2_histogram, test6b_chi2_hardcore)
register(7, "Decay Slope (log-log regression)", "test_07_decay_slope",
         test7_decay_slope, test7b_decay_slope_hardcore)
register(8, "Residual Analysis", "test_08_residuals",
         test8_residual_analysis, test8b_residuals_hardcore)
register(9, "Bootstrap CI for Slope", "test_09_bootstrap_ci",
         test9_bootstrap_slope, test9b_bootstrap_hardcore)
register(10, "Cross-Validation Stability", "test_10_cross_validation",
         test10_cross_validation, test10b_crossval_hardcore)
register(11, "Anderson–Darling (tail-sensitive)", "test_11_anderson_darling",
         test11_anderson_darling, test11b_ad_hardcore)
register(12, "2-sample KS vs simulated GUE", "test_12_two_sample_ks",
         test12_two_sample_ks, test12b_two_ks_hardcore)
register(13, "Number Variance Σ²(L)", "test_13_number_variance",
         test13_number_variance, test13b_numbervar_hardcore)
register(14, "Spectral Rigidity Δ₃(L)", "test_14_spectral_rigidity",
         test14_spectral_rigidity, test14b_d3_hardcore)
register(15, "AB-cloud Hamiltonian Construction", "test_15_ab_construction",
         test15_ab_cloud_construction, test15b_construction_hardcore)
register(16, "AB-cloud Eigenvalue Spacing → GUE", "test_16_ab_gue_class",
         test16_ab_cloud_gue_classification, test16b_gue_classification_hardcore)
register(17, "Connes Self-Duality α ↔ 1/α", "test_17_connes_self_duality",
         test17_alpha_half_self_duality, test17b_self_duality_hardcore)
register(18, "Chiral Symmetry AIII at α = 1/2", "test_18_chiral_AIII",
         test18_chiral_symmetry_AIII, test18b_chiral_hardcore)
register(19, "Dirac Cone Linear Dispersion v_F", "test_19_dirac_cone",
         test19_dirac_cone_velocity, test19b_dirac_velocity_hardcore,
         third=[test19c_dirac_alpha_series, test19d_dirac_cone_audit])
register(20, "TKNN Chern Number (magnetic BZ, FHS)", "test_20_chern_tknn",
         test20_chern_number_tknn, test20b_chern_hardcore)
register(21, "γ* Spinorial Phase ≈ π/2", "test_21_gamma_phase",
         test21_gamma_star_phase, test21b_gamma_star_hardcore)
register(22, "AB Phase Φ_AB = π/7 = δ_C", "test_22_ab_phase",
         test22_ab_phase, None)
register(23, "Complex Fractal Factor CF", "test_23_fractal_factor",
         test23_complex_factor, test23b_complex_factor_hardcore)
register(24, "Dirac String Flux Verification", "test_24_dirac_string_flux",
         test24_dirac_string_flux, test24b_dirac_flux_hardcore)
register(25, "Byers-Yang Theorem Check", "test_25_byers_yang",
         test25_byers_yang_theorem, test25b_byers_hardcore)
register(26, "PBC Torus with Wrapped Dirac String", "test_26_pbc_torus",
         test26_pbc_torus_dirac_string, test26b_torus_hardcore)
register(27, "Binary Chiral Symmetry at α=1/2", "test_27_binary_chiral",
         test27_chiral_binary_alpha_half, test27b_chiral_binary_hardcore)
register(28, "f_GUE Figure of Merit", "test_28_f_gue_merit",
         test28_f_gue_figure_of_merit, test28b_fgue_hardcore)
register(29, "Dirac Dip in DOS at α=1/2", "test_29_dirac_dip",
         test29_dirac_dip_dos, test29b_dirac_dip_hardcore,
         third=[test29c_dirac_dip_series])
register(30, "Dirac Cone Velocity v_F (1/L fit)", "test_30_vf_scaling",
         test30_dirac_cone_vF, test30b_vF_hardcore)
register(31, "Hatano–Nelson Skin Effect", "test_31_hatano_nelson",
         test31_hatano_nelson, test31b_hatano_hardcore,
         third=[test31c_hatano_series])
register(32, "Multi-realization ⟨r⟩ bootstrap", "test_32_rmean_bootstrap",
         test32_200_realization_rmean, test32b_rmean_hardcore)
register(33, "L-Scaling ⟨r⟩", "test_33_l_scaling_rmean",
         test33_lattice_L_scaling, test33b_lscaling_hardcore)
register(34, "DIRECT AB-cloud vs ζ (Hilbert-Pólya)", "test_34_direct_vs_zeta",
         test34_direct_ab_vs_zeta, test34b_ab_vs_zeta_hardcore)
register(35, "Spectral Form Factor K(t)", "test_35_form_factor_Kt",
         test35_form_factor_Kt, test35b_form_factor_hardcore)
register(36, "Byte-level Robustness", "test_36_byte_robust",
         test36_byte_robustness, None, self_second=True)
register(37, "(1/2)! via Γ & GUE normalization", "test_37_half_factorial_gamma",
         test37_half_factorial_gamma, test37b_half_factorial_hardcore)
register(38, "Curie Point of the vortex-flux lattice magnet", "test_38_curie",
         test38_curie, None)
register(39, "TEST 34G — geometry sweep", "test_39_geometry_sweep",
         test39_t34g_geometry_sweep, None)

SUITE_IDS = sorted(TESTS.keys())


def run_test_two_pass(tid: int, zeros: np.ndarray, cfg: Config) -> Tuple[bool, str]:
    """Pass 1 primary → pass 2 hardcore on the secondary lattice → third passes."""
    info = TESTS[tid]
    t0 = time.time()
    print(f"\n┌─ [{tid:>2}] {info['name']} — two-pass run")
    ok1, h1 = info["primary"](zeros, cfg)
    pass2_ok = True
    if info["hardcore"] is not None:
        saved = (cfg.ab_nx, cfg.ab_ny, cfg.ab_nv_list, cfg.pass2)
        cfg.pass2 = True
        cfg.ab_nx, cfg.ab_ny = cfg.ab_nx_secondary, cfg.ab_ny_secondary
        cfg.ab_nv_list = cfg.ab_nv_list_secondary
        try:
            if info["self_second"]:
                pass2_ok, h2 = info["primary"](zeros, cfg)
            else:
                pass2_ok, h2 = info["hardcore"](zeros, cfg)
        finally:
            cfg.ab_nx, cfg.ab_ny, cfg.ab_nv_list, cfg.pass2 = saved
    elif info["self_second"]:
        cfg.pass2 = True
        try:
            pass2_ok, h2 = info["primary"](zeros, cfg)
        finally:
            cfg.pass2 = False
    thirds_ok = True
    if cfg.ab_run_third_pass and info["third"]:
        for tf in info["third"]:
            tok, _ = tf(zeros, cfg)
            thirds_ok &= tok
    ok = ok1 and pass2_ok and thirds_ok
    dt = time.time() - t0
    verdict = msg(cfg, "pass") if ok else msg(cfg, "warn")
    print(f"└─ [{tid:>2}] done in {int(dt//60):02d}:{dt%60:04.1f} → {verdict}")
    return ok, h1


def run_all_tests(zeros: np.ndarray, cfg: Config) -> bool:
    all_ok = True
    t_start = time.time()
    for tid in SUITE_IDS:
        try:
            ok, _ = run_test_two_pass(tid, zeros, cfg)
        except Exception as e:  # a failed test must not kill the suite
            import traceback
            traceback.print_exc()
            log_result(f" Test {tid}: ERROR — {type(e).__name__}: {e} → FAIL")
            ok = False
        all_ok &= ok
        print(f"[Test {tid:>2}] cumulative verdict: {'PASS' if ok else 'WARN/FAIL'} "
              f"— {time.time()-t_start:.0f}s elapsed")
    return all_ok


def write_report(cfg: Config, all_ok: bool, elapsed: float) -> None:
    os.makedirs(cfg.output_dir, exist_ok=True)
    lines = []
    lines.append("# AB-Cloud Verification Suite — Python port run report")
    lines.append("")
    lines.append(f"- Generated: {time.strftime('%Y-%m-%dT%H:%M:%S')}")
    lines.append(f"- Profile: {cfg.profile} (exact = frozen-v19 defaults; "
                 f"fast = documented performance knobs)")
    lines.append(f"- Data: {cfg.zeros_count} zeros from source '{cfg.source}' "
                 f"({cfg.data_dir})")
    lines.append(f"- Lattice: primary {cfg.ab_nx}×{cfg.ab_ny}, "
                 f"secondary {cfg.ab_nx_secondary}×{cfg.ab_ny_secondary} "
                 f"(RAM guard: ≤ {_max_sites_bytes()} sites per dense solve)")
    lines.append(f"- GUE reference: {cfg.gue_matrix_size}² seed {cfg.gue_matrix_seed}")
    lines.append(f"- Total wall time: {elapsed/60:.1f} min")
    lines.append("")
    lines.append("## Verdict ledger")
    lines.append("")
    lines.append("```")
    lines.extend(LEDGER)
    lines.append("```")
    lines.append("")
    lines.append("## Deviations vs the canonical Julia run (v19)")
    lines.append("")
    lines.append("- RNG: numpy MT19937 with the same seed constants; Julia dSFMT "
                 "streams differ, so seed-dependent quantities (bootstrap CIs, MC "
                 "nulls, simulated-GUE columns) match to statistical noise only.")
    lines.append("- Presentation engines (ABUI ANSI, HTML, hand-rolled PNG) are "
                 "replaced by this Markdown/JSON report; numeric verdicts are 1:1.")
    lines.append("- Lattice sizes respect the session RAM guard (secondary 96² → 72²), "
                 "printed at run start; Julia's own suite applies the same kind of "
                 "guard (t38_ram).")
    lines.append("- Fast profile additionally trims: GUE ref 12000²→4000², "
                 "Σ²/Δ₃ window counts, realization floors, Test-38 C2 ladder.")
    with open(os.path.join(cfg.output_dir, "report.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    with open(os.path.join(cfg.output_dir, "results.json"), "w", encoding="utf-8") as f:
        json.dump({"ledger": LEDGER, "profile": cfg.profile,
                   "zeros": cfg.zeros_count, "source": cfg.source,
                   "all_ok": bool(all_ok), "elapsed_s": elapsed},
                  f, ensure_ascii=False, indent=2)
    print(f"\nReport written: {cfg.output_dir}/report.md, results.json")


def parse_args(cfg: Config, argv: List[str]) -> None:
    i = 0
    while i < len(argv):
        a = argv[i]

        def need() -> str:
            nonlocal i
            i += 1
            if i >= len(argv):
                raise SystemExit(f"ERROR: {a} expects a value")
            return argv[i]

        if a == "--test":
            cfg.test = need()
        elif a == "--zeros":
            cfg.zeros_count = int(need())
        elif a == "--source":
            cfg.source = need()
        elif a == "--lang":
            cfg.lang = need()
        elif a == "--data-dir":
            cfg.data_dir = need()
        elif a == "--output-dir":
            cfg.output_dir = need()
        elif a == "--profile":
            cfg.profile = need()
        elif a == "--gue-matrix-size":
            cfg.gue_matrix_size = int(need())
        elif a == "--gue-matrix-seed":
            cfg.gue_matrix_seed = int(need())
        elif a == "--ab-nx":
            cfg.ab_nx = cfg.ab_ny = int(need())
        elif a == "--ab-nx-secondary":
            cfg.ab_nx_secondary = cfg.ab_ny_secondary = int(need())
        elif a == "--ab-hc-nreal":
            cfg.ab_hc_nreal = int(need())
        elif a == "--ab-n-realizations":
            cfg.ab_n_realizations = int(need())
        elif a == "--t31-lmax":
            cfg.t31_lmax = int(need())
        elif a == "--t38-quick":
            cfg.t38_quick = True
        elif a == "--t34g-L":
            cfg.t34g_L = int(need())
        elif a == "--t34g-reps":
            cfg.t34g_reps = int(need())
        elif a == "--no-two-pass":
            cfg.ab_run_two_pass = False
        elif a == "--no-third-pass":
            cfg.ab_run_third_pass = False
        elif a == "--list":
            print("Test ledger (39 tests, two-pass):")
            for tid in SUITE_IDS:
                print(f"  {tid:>2}. {TESTS[tid]['name']}")
            raise SystemExit(0)
        elif a == "--help":
            print(__doc__)
            raise SystemExit(0)
        else:
            raise SystemExit(f"ERROR: unknown flag {a} (see --help)")
        i += 1


def main(argv: Optional[List[str]] = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    cfg = Config()
    parse_args(cfg, argv)
    if cfg.profile == "fast":
        apply_fast_profile(cfg)
    # RAM guard: cap the secondary lattice for this session (printed once);
    # the cap is rounded DOWN to a multiple of 12 so that α=1/2, 1/3, 1/4, 1/6
    # torus rows keep their modular structure.
    cap = int(math.sqrt(_max_sites_bytes()))
    cap = (cap // 12) * 12
    if cfg.ab_nx_secondary > cap:
        print(f"[RAM guard] secondary lattice {cfg.ab_nx_secondary}² exceeds the "
              f"session budget → {cap}² (canonical Julia value was 96²)")
        cfg.ab_nx_secondary = cfg.ab_ny_secondary = cap
    if cfg.lang == "en" and os.environ.get("LANG", "").startswith("ru"):
        cfg.lang = "ru"

    print("╔════════════════════════════════════════════════════════════════════╗")
    print("║ ✦ AB-CLOUD — VERIFICATION SUITE · AURORA EDITION — Python port     ║")
    print("╚════════════════════════════════════════════════════════════════════╝")
    print(f" Profile: {cfg.profile} | zeros: {cfg.zeros_count} from '{cfg.source}' | "
          f"test: {cfg.test} | lang: {cfg.lang}")

    zeros = load_zeros(cfg)
    if len(zeros) == 0:
        print(msg(cfg, "no_data"))
        return 1

    t0 = time.time()
    if cfg.test == "all":
        all_ok = run_all_tests(zeros, cfg)
    else:
        # multi-test: "1,2,3", "1-14", "15-39", or mixed "1-14,37"
        ids: List[int] = []
        try:
            for part in cfg.test.split(","):
                part = part.strip()
                if "-" in part:
                    lo, hi = part.split("-")
                    ids.extend(range(int(lo), int(hi) + 1))
                else:
                    ids.append(int(part))
        except ValueError:
            print("ERROR: --test expects 'all', an integer, or a list/range like '1-14,37'")
            return 1
        bad = [t for t in ids if t not in TESTS]
        if bad:
            print(f"ERROR: unknown test ids {bad} (valid 1-39)")
            return 1
        all_ok = True
        for tid in ids:
            if cfg.ab_run_two_pass:
                ok, _ = run_test_two_pass(tid, zeros, cfg)
            else:
                ok, _ = TESTS[tid]["primary"](zeros, cfg)
            all_ok &= ok
    elapsed = time.time() - t0
    write_report(cfg, all_ok, elapsed)
    print(f"\n{'═'*60}")
    print(f" Suite complete: {'ALL PASS' if all_ok else 'FAIL/WARN present'} "
          f"in {elapsed/60:.1f} min")
    print(f"{'═'*60}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
