//! =============================================================================
//! AB-CLOUD ПРОВЕРОЧНЫЙ ПАКЕТ — РУССКИЙ МОДУЛЬ
//! Современный Rust · Обработка Result · Эффективный
//! =============================================================================
//! Три возражения против гипотезы Римана (вывод на русском):
//!   Возражение 1: b(N) → 0?  (сходимость отклонений Грама)
//!   Возражение 2: GUE-интервалы, KS-критерий
//!   Возражение 3: Наклон убывания при больших T ≈ -0.5
//! =============================================================================

use std::f64::consts::{E, PI, TAU};

const TWO_PI: f64 = TAU;

/// Результат проверки
#[derive(Debug, Clone)]
pub struct VerifyResult {
    pub label: String,
    pub value: f64,
    pub pass: bool,
    pub detail: String,
}

// =============================================================================
// W Ламберта (главная ветвь) через метод Галлея
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

/// Точка Грама: γ̃_n = 2π · W₀(n/e)
fn gram_point(n: usize) -> f64 {
    TWO_PI * lambert_w0(n as f64 / E)
}

// =============================================================================
// Возражение 1: b(N) = (1/N) * Σ|γ_k - γ̃_k|
// =============================================================================
pub fn compute_objection1(gammas: &[f64]) -> VerifyResult {
    let n = gammas.len();
    let s: f64 = gammas
        .iter()
        .enumerate()
        .map(|(k, &gk)| (gk - gram_point(k + 1)).abs())
        .sum();
    let b_n = s / n as f64;
    let pass = b_n < 1.0;

    println!();
    println!("═══════════════════════════════════════════════════");
    println!("  ВОЗРАЖЕНИЕ 1: Сходимость b(N)");
    println!("  b(N) = (1/N) · Σ|γ_k − γ̃_k|, точки Грама через W Ламберта");
    println!("═══════════════════════════════════════════════════");
    println!("    N       = {}", n);
    println!("    b(N)    = {:.8e}", b_n);
    println!("    Пройдено: {}", pass);

    VerifyResult {
        label: "1:b(N)".to_string(),
        value: b_n,
        pass,
        detail: format!("{:.8e}", b_n),
    }
}

// =============================================================================
// GUE вспомогательные функции
// =============================================================================
fn gue_pdf(s: f64) -> f64 {
    (PI * s / 2.0) * (-PI * s * s / 4.0).exp()
}

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

fn kolmogorov_pvalue(d: f64, n: f64) -> f64 {
    let z = d * n.sqrt();
    let mut pval = 0.0;
    for k in -10_i32..=10 {
        let sign = if k % 2 == 0 { 1.0 } else { -1.0 };
        pval += sign * (-2.0 * (2.0 * k as f64 * z + z).powi(2)).exp();
    }
    pval.clamp(0.0, 1.0)
}

// =============================================================================
// Возражение 2: GUE-интервалы, KS-критерий
// =============================================================================
pub fn compute_objection2(gammas: &[f64]) -> VerifyResult {
    let n = gammas.len();
    let m = n - 1;

    let mut spacings: Vec<f64> = Vec::with_capacity(m);
    for k in 0..m {
        let log_factor = (gammas[k] / TWO_PI).ln();
        spacings.push((gammas[k + 1] - gammas[k]) * log_factor / TWO_PI);
    }
    spacings.sort_by(|a, b| a.partial_cmp(b).unwrap_or(std::cmp::Ordering::Equal));

    let mut ks_stat = 0.0_f64;
    for (k, &sk) in spacings.iter().enumerate() {
        let cdf_emp = (k + 1) as f64 / m as f64;
        let cdf_theo = gue_cdf(sk);
        let d = (cdf_emp - cdf_theo).abs();
        if d > ks_stat { ks_stat = d; }
    }

    let ks_pval = kolmogorov_pvalue(ks_stat, m as f64);
    let pass = ks_pval > 0.05;

    println!();
    println!("═══════════════════════════════════════════════════");
    println!("  ВОЗРАЖЕНИЕ 2: GUE-интервалы, KS-критерий");
    println!("  s_k = Δγ_k · log(γ_k/2π) / 2π,  p(s) = (πs/2)·e^{{-πs²/4}}");
    println!("═══════════════════════════════════════════════════");
    println!("    Кол-во интервалов = {}", m);
    println!("    KS-статистика     = {:.8e}", ks_stat);
    println!("    p-значение        = {:.8e}", ks_pval);
    println!("    Пройдено (p>0.05): {}", pass);

    VerifyResult {
        label: "2:KS".to_string(),
        value: ks_stat,
        pass,
        detail: format!("p={:.4e}", ks_pval),
    }
}

// =============================================================================
// Возражение 3: Наклон убывания при больших T ≈ -0.5
// =============================================================================
pub fn compute_objection3(gammas: &[f64]) -> VerifyResult {
    let n = gammas.len();
    let i_start = n / 2 + 1;
    let m = n - i_start;

    if m < 10 {
        return VerifyResult {
            label: "3:slope".to_string(),
            value: 0.0,
            pass: false,
            detail: "недостаточно данных".to_string(),
        };
    }

    let mut x_mean = 0.0_f64;
    let mut y_mean = 0.0_f64;
    for k in i_start..(n - 1) {
        x_mean += gammas[k].ln();
        y_mean += (gammas[k + 1] - gammas[k]).abs().ln();
    }
    x_mean /= m as f64;
    y_mean /= m as f64;

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

    println!();
    println!("═══════════════════════════════════════════════════");
    println!("  ВОЗРАЖЕНИЕ 3: Наклон убывания при больших T");
    println!("  log|Δγ_k| ~ slope · log(γ_k),  ожидается slope ≈ -0.5");
    println!("═══════════════════════════════════════════════════");
    println!("    Точек регрессии = {}", m);
    println!("    Наклон (slope)  = {:.4}", slope);
    println!("    Отклонение      = {:.4}", deviation);
    println!("    Пройдено:       {}", pass);

    VerifyResult {
        label: "3:slope".to_string(),
        value: slope,
        pass,
        detail: format!("откл={:.4}", deviation),
    }
}

// =============================================================================
// Сводная таблица (русский)
// =============================================================================
pub fn print_summary(results: &[VerifyResult]) {
    println!();
    println!("  ┌──────────┬────────────────────┬────────┐");
    println!("  │ Возраж.  │    Значение        │ Стат.  │");
    println!("  ├──────────┼────────────────────┼────────┤");
    for r in results {
        let status = if r.pass { "PASS" } else { "FAIL" };
        println!("  │ {:<8} │ {:>16.6e} │ {:<6} │", r.label, r.value, status);
    }
    println!("  └──────────┴────────────────────┴────────┘");
}
