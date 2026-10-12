// verify_core.rs — двойник Rust ≥ 1.70: Γ-замыкание + Λ-сито
// Запуск: rustc -O verify_core.rs && ./verify_core [verify_control.txt]
use std::f64::consts::PI;

fn cgamma(x: f64, y: f64) -> (f64, f64) {
    let (zr, zi) = (x - 1.0, y);
    let lc: [f64; 9] = [0.99999999999980993, 676.5203681218851,
        -1259.1392167224028, 771.32342877765313, -176.61502916214059,
        12.507343278686905, -0.13857109526572012, 9.9843695780195716e-6,
        1.5056327351493116e-7];
    let (mut sr, mut si) = (lc[0], 0.0);
    for i in 1..9 {
        let (dr, di) = (zr + i as f64, zi);
        let d = dr * dr + di * di;
        sr += lc[i] * dr / d;
        si += -lc[i] * di / d;
    }
    let (tr, ti) = (zr + 7.5, zi);
    let lt_r = 0.5 * (tr * tr + ti * ti).ln();
    let lt_i = ti.atan2(tr);
    let ls_r = 0.5 * (sr * sr + si * si).ln();
    let ls_i = si.atan2(sr);
    let (ar, ai) = (zr + 0.5, zi);
    let lr = 0.5 * (2.0 * PI).ln() + (ar * lt_r - ai * lt_i) - tr + ls_r;
    let li = (ar * lt_i + ai * lt_r) + ls_i;
    (lr.exp() * li.cos(), lr.exp() * li.sin())
}

fn main() {
    let mut maxres = 0.0f64;
    for &u in &[0.5, 1.0, 2.0, 3.0] {
        let (gr, gi) = cgamma(0.5, u);
        let lhs = gr * gr + gi * gi;
        let rhs = PI / ((PI * u).cosh());
        maxres = maxres.max((lhs - rhs).abs() / rhs);
    }
    const N: usize = 100_000;
    let mut spf = vec![0usize; N + 1];
    let mut lsum = 0.0f64;
    for i in 2..=N {
        if spf[i] == 0 {
            let mut p = i as u64;
            while p <= N as u64 {
                lsum += (i as f64).ln() / (p as f64).powf(1.5);
                let mut j = i;
                while j <= N {
                    if spf[j] == 0 { spf[j] = i; }
                    j += i;
                }
                p *= i as u64;
            }
        }
    }
    println!("gamma_closure_max_res = {:.3e}", maxres);
    println!("lambda_sum_check = {:.10}", lsum);
    println!("n_sieve = {}", N);
    if let Some(path) = std::env::args().nth(1) {
        std::fs::write(&path, format!(
            "gamma_closure_max_res = {:.3e}\nlambda_sum_check = {:.10}\n\
             n_sieve = {}\n", maxres, lsum, N)).unwrap();
    }
}
