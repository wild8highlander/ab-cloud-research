//! =============================================================================
//! AB-CLOUD VERIFICATION SUITE — BILINGUAL (EN/RU)
//! Modern Rust · Result Handling · Efficient
//! =============================================================================
//! Проверочный пакет AB-Cloud — билингвальный (английский/русский)
//! Три возражения против гипотезы Римана:
//!   Возражение 1: b(N) → 0?  (сходимость отклонений Грама)
//!   Возражение 2: GUE间距 KS-тест (уровневые промежутки)
//!   Возражение 3: Large-T decay slope ≈ -0.5
//! =============================================================================

#[allow(dead_code)]
mod verify_en;
#[allow(dead_code)]
mod verify_ru;

use std::env;
use std::f64::consts::{E, PI, TAU};

const TWO_PI: f64 = TAU;

/// Verification result for a single objection
#[derive(Debug, Clone)]
struct VerifyResult {
    label: String,
    value: f64,
    pass: bool,
    detail: String,
}

/// Parsed CLI arguments
struct Args {
    n_zeros: usize,
    source: String,
    objection: u8, // 0 = all
    lang: u8,      // 0 = bilingual, 1 = en, 2 = ru
}

fn parse_args() -> Args {
    let mut args = Args {
        n_zeros: 10_000,
        source: "auto".to_string(),
        objection: 0,
        lang: 0,
    };

    let cli: Vec<String> = env::args().collect();
    let mut i = 1;
    while i < cli.len() {
        match cli[i].as_str() {
            "--zeros" if i + 1 < cli.len() => {
                i += 1;
                args.n_zeros = cli[i].parse().unwrap_or(10_000);
            }
            "--source" if i + 1 < cli.len() => {
                i += 1;
                args.source = cli[i].clone();
            }
            "--objection" if i + 1 < cli.len() => {
                i += 1;
                args.objection = match cli[i].as_str() {
                    "all" => 0,
                    s => s.parse().unwrap_or(0),
                };
            }
            "--lang" if i + 1 < cli.len() => {
                i += 1;
                args.lang = match cli[i].as_str() {
                    "en" => 1,
                    "ru" => 2,
                    _ => 0,
                };
            }
            _ => {}
        }
        i += 1;
    }
    args
}

// =============================================================================
// Load zeta zeros from data file
// =============================================================================
fn load_zeros(n_request: usize, source: &str) -> Result<Vec<f64>, String> {
    let filepath = if source != "auto" {
        format!("../data/{}", source)
    } else if n_request <= 13_661 {
        "../data/zeta_zeros_50000.txt".to_string()
    } else if n_request <= 500_000 {
        "../data/zeta_zeros_500k_odlyzko.txt".to_string()
    } else if n_request <= 2_000_000 {
        "../data/zeta_zeros_2M_odlyzko.txt".to_string()
    } else {
        "../data/zeros6.txt".to_string()
    };

    println!("  Data file: {}", filepath);

    let content =
        std::fs::read_to_string(&filepath).map_err(|e| format!("Cannot open {}: {}", filepath, e))?;

    let mut zeros: Vec<f64> = Vec::with_capacity(n_request);
    for line in content.lines() {
        let trimmed = line.trim();
        if trimmed.is_empty() || trimmed.starts_with('#') {
            continue;
        }
        if let Ok(v) = trimmed.parse::<f64>() {
            if v > 0.0 {
                zeros.push(v);
                if zeros.len() >= n_request {
                    break;
                }
            }
        }
    }

    if zeros.is_empty() {
        return Err("No valid zeros loaded".to_string());
    }

    Ok(zeros)
}

// =============================================================================
// Lambert W (principal branch) via Halley's method
// =============================================================================
fn lambert_w0(x: f64) -> f64 {
    if x == 0.0 {
        return 0.0;
    }
    let mut w = x.ln().max(-70.0);
    if w > 0.0 {
        w = w.ln();
    }

    for _ in 0..50 {
        let ew = w.exp();
        let f = w * ew - x;
        let fp = ew * (w + 1.0);
        let fpp = ew * (w + 2.0);
        let delta = f / (fp - 0.5 * f * fpp / fp);
        w -= delta;
        if delta.abs() < 1e-15 * w.abs() {
            break;
        }
    }
    w
}

/// Gram point: γ̃_n = 2π · W₀(n/e)
fn gram_point(n: usize) -> f64 {
    TWO_PI * lambert_w0(n as f64 / E)
}

// =============================================================================
// Objection 1: b(N) = (1/N) * Σ|γ_k - γ̃_k|
// =============================================================================
fn compute_objection1(gammas: &[f64], lang: u8) -> VerifyResult {
    let n = gammas.len();
    let s: f64 = gammas
        .iter()
        .enumerate()
        .map(|(k, &gk)| (gk - gram_point(k + 1)).abs())
        .sum();
    let b_n = s / n as f64;
    let pass = b_n < 1.0;

    if lang == 2 {
        println!();
        println!("═══════════════════════════════════════════════════");
        println!("  ВОЗРАЖЕНИЕ 1: Сходимость b(N)");
        println!("  b(N) = (1/N) · Σ|γ_k − γ̃_k|, точки Грама через W Ламберта");
        println!("═══════════════════════════════════════════════════");
        println!("    N       = {}", n);
        println!("    b(N)    = {:.8e}", b_n);
        println!("    Пройдено: {}", pass);
    } else {
        println!();
        println!("═══════════════════════════════════════════════════");
        println!("  OBJECTION 1: b(N) Convergence");
        println!("  b(N) = (1/N) · Σ|γ_k − γ̃_k|, Gram pts via Lambert W");
        println!("═══════════════════════════════════════════════════");
        println!("    N       = {}", n);
        println!("    b(N)    = {:.8e}", b_n);
        println!("    Pass:   {}", pass);
    }

    VerifyResult {
        label: "1:b(N)".to_string(),
        value: b_n,
        pass,
        detail: format!("{:.8e}", b_n),
    }
}

// =============================================================================
// GUE PDF: p(s) = (πs/2) · exp(-πs²/4)
// =============================================================================
fn gue_pdf(s: f64) -> f64 {
    (PI * s / 2.0) * (-PI * s * s / 4.0).exp()
}

/// GUE CDF via Simpson's rule
fn gue_cdf(s: f64) -> f64 {
    if s <= 0.0 {
        return 0.0;
    }
    let nsteps = 200;
    let h = s / nsteps as f64;
    let mut sum = 0.0;
    for i in 0..=nsteps {
        let x = i as f64 * h;
        let w = if i == 0 || i == nsteps {
            1.0
        } else if i % 2 == 1 {
            4.0
        } else {
            2.0
        };
        sum += w * gue_pdf(x);
    }
    (h / 3.0 * sum).min(1.0)
}

/// Approximate Kolmogorov p-value
fn kolmogorov_pvalue(d: f64, n: f64) -> f64 {
    let z = d * n.sqrt();
    let mut pval = 0.0;
    for k in -10..=10_i32 {
        let term = (-2.0 * (2.0 * k as f64 * z + z).powi(2)).exp();
        pval += k_is_odd(k) * term;
    }
    pval.clamp(0.0, 1.0)
}

fn k_is_odd(k: i32) -> f64 {
    if k % 2 == 0 { 1.0 } else { -1.0 }
}

// =============================================================================
// Objection 2: GUE spacing KS test
// s_k = (γ_{k+1} - γ_k) · log(γ_k/(2π)) / (2π)
// =============================================================================
fn compute_objection2(gammas: &[f64], lang: u8) -> VerifyResult {
    let n = gammas.len();
    let m = n - 1;

    // Compute normalized spacings
    let mut spacings: Vec<f64> = Vec::with_capacity(m);
    for k in 0..m {
        let log_factor = (gammas[k] / TWO_PI).ln();
        let sk = (gammas[k + 1] - gammas[k]) * log_factor / TWO_PI;
        spacings.push(sk);
    }

    // Sort for empirical CDF
    spacings.sort_by(|a, b| a.partial_cmp(b).unwrap_or(std::cmp::Ordering::Equal));

    // KS statistic
    let mut ks_stat = 0.0_f64;
    for (k, &sk) in spacings.iter().enumerate() {
        let cdf_emp = (k + 1) as f64 / m as f64;
        let cdf_theo = gue_cdf(sk);
        let d_plus = (cdf_emp - cdf_theo).abs();
        if d_plus > ks_stat {
            ks_stat = d_plus;
        }
    }

    let ks_pval = kolmogorov_pvalue(ks_stat, m as f64);
    let pass = ks_pval > 0.05;

    if lang == 2 {
        println!();
        println!("═══════════════════════════════════════════════════");
        println!("  ВОЗРАЖЕНИЕ 2: GUE-интервалы, KS-критерий");
        println!("  s_k = Δγ_k · log(γ_k/2π) / 2π,  p(s) = (πs/2)·e^{{-πs²/4}}");
        println!("═══════════════════════════════════════════════════");
        println!("    Кол-во интервалов = {}", m);
        println!("    KS-статистика     = {:.8e}", ks_stat);
        println!("    p-значение        = {:.8e}", ks_pval);
        println!("    Пройдено (p>0.05): {}", pass);
    } else {
        println!();
        println!("═══════════════════════════════════════════════════");
        println!("  OBJECTION 2: GUE Spacing KS Test");
        println!("  s_k = Δγ_k · log(γ_k/2π) / 2π,  p(s) = (πs/2)·e^{{-πs²/4}}");
        println!("═══════════════════════════════════════════════════");
        println!("    Spacing count    = {}", m);
        println!("    KS statistic     = {:.8e}", ks_stat);
        println!("    p-value          = {:.8e}", ks_pval);
        println!("    Pass (p>0.05):   {}", pass);
    }

    VerifyResult {
        label: "2:KS".to_string(),
        value: ks_stat,
        pass,
        detail: format!("p={:.4e}", ks_pval),
    }
}

// =============================================================================
// Objection 3: Large-T decay slope ≈ -0.5
// Fit log|Δγ_k| vs log(γ_k)
// =============================================================================
fn compute_objection3(gammas: &[f64], lang: u8) -> VerifyResult {
    let n = gammas.len();
    let i_start = n / 2 + 1;
    let m = n - i_start;

    if m < 10 {
        return VerifyResult {
            label: "3:slope".to_string(),
            value: 0.0,
            pass: false,
            detail: "insufficient data".to_string(),
        };
    }

    // Compute means
    let mut x_mean = 0.0_f64;
    let mut y_mean = 0.0_f64;
    for k in i_start..(n - 1) {
        x_mean += gammas[k].ln();
        y_mean += (gammas[k + 1] - gammas[k]).abs().ln();
    }
    x_mean /= m as f64;
    y_mean /= m as f64;

    // Linear regression
    let mut sxx = 0.0_f64;
    let mut sxy = 0.0_f64;
    for k in i_start..(n - 1) {
        let xv = gammas[k].ln();
        let yv = (gammas[k + 1] - gammas[k]).abs().ln();
        sxx += (xv - x_mean).powi(2);
        sxy += (xv - x_mean) * (yv - y_mean);
    }
    let slope = sxy / sxx;
    let deviation = (slope + 0.5).abs();
    let pass = deviation < 0.15;

    if lang == 2 {
        println!();
        println!("═══════════════════════════════════════════════════");
        println!("  ВОЗРАЖЕНИЕ 3: Наклон убывания при больших T");
        println!("  log|Δγ_k| ~ slope · log(γ_k),  ожидается slope ≈ -0.5");
        println!("═══════════════════════════════════════════════════");
        println!("    Точек регрессии = {}", m);
        println!("    Наклон (slope)  = {:.4}", slope);
        println!("    Отклонение      = {:.4}", deviation);
        println!("    Пройдено:       {}", pass);
    } else {
        println!();
        println!("═══════════════════════════════════════════════════");
        println!("  OBJECTION 3: Large-T Decay Slope");
        println!("  log|Δγ_k| ~ slope · log(γ_k),  expected slope ≈ -0.5");
        println!("═══════════════════════════════════════════════════");
        println!("    Regression pts  = {}", m);
        println!("    Slope           = {:.4}", slope);
        println!("    Deviation       = {:.4}", deviation);
        println!("    Pass:           {}", pass);
    }

    VerifyResult {
        label: "3:slope".to_string(),
        value: slope,
        pass,
        detail: format!("dev={:.4}", deviation),
    }
}

// =============================================================================
// Print summary table
// =============================================================================
fn print_summary(results: &[VerifyResult], lang: u8) {
    if lang == 2 {
        println!();
        println!("  ┌──────────┬────────────────────┬────────┐");
        println!("  │ Возраж.  │    Значение        │ Стат.  │");
        println!("  ├──────────┼────────────────────┼────────┤");
    } else {
        println!();
        println!("  ┌──────────┬────────────────────┬────────┐");
        println!("  │ Obj.     │    Value           │ Status │");
        println!("  ├──────────┼────────────────────┼────────┤");
    }

    for r in results {
        let status = if r.pass { "PASS" } else { "FAIL" };
        println!("  │ {:<8} │ {:>16.6e} │ {:<6} │", r.label, r.value, status);
    }

    println!("  └──────────┴────────────────────┴────────┘");
}

// =============================================================================
// Main entry
// =============================================================================
fn main() -> Result<(), String> {
    let args = parse_args();

    // Banner
    println!();
    if args.lang == 2 {
        println!("  ╔═══════════════════════════════════════════════╗");
        println!("  ║   AB-CLOUD ПРОВЕРКА — ГИПОТЕЗА РИМАНА        ║");
        println!("  ║   Три возражения: b(N), GUE KS, Large-T      ║");
        println!("  ╚═══════════════════════════════════════════════╝");
    } else {
        println!("  ╔═══════════════════════════════════════════════╗");
        println!("  ║   AB-CLOUD VERIFICATION — RIEMANN HYPOTHESIS  ║");
        println!("  ║   Three objections: b(N), GUE KS, Large-T     ║");
        println!("  ╚═══════════════════════════════════════════════╝");
    }
    println!();

    // Load zeros
    let gammas = load_zeros(args.n_zeros, &args.source)?;
    let n_loaded = gammas.len();

    if args.lang == 2 {
        println!("  Загружено нулей: {} (γ-ординаты)", n_loaded);
    } else {
        println!("  Zeros loaded: {} (gamma ordinates)", n_loaded);
    }

    let t_start = std::time::Instant::now();

    // Run objections
    let mut results: Vec<VerifyResult> = Vec::new();

    if args.objection == 0 || args.objection == 1 {
        results.push(compute_objection1(&gammas, args.lang));
    }
    if args.objection == 0 || args.objection == 2 {
        results.push(compute_objection2(&gammas, args.lang));
    }
    if args.objection == 0 || args.objection == 3 {
        results.push(compute_objection3(&gammas, args.lang));
    }

    print_summary(&results, args.lang);

    let elapsed = t_start.elapsed().as_secs_f64();
    if args.lang == 2 {
        println!("  Общее время: {:.3} с", elapsed);
    } else {
        println!("  Total time: {:.3} s", elapsed);
    }

    Ok(())
}
