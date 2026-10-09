// verify_core.rs — Rust-двойник ядра. Запуск: rustc -O verify_core.rs -o /tmp/hpb_rs
use std::f64::consts::PI;

const G: f64 = 7.0;
const C: [f64; 9] = [0.99999999999980993, 676.5203681218851, -1259.1392167224028,
    771.32342877765313, -176.61502916214059, 12.507343278686905,
    -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7];

fn mod_gamma(re: f64, u: f64) -> f64 {
    let (mut zr, zi) = (re - 1.0, u);
    let (mut xr, mut xi) = (C[0], 0.0);
    for i in 1..9 {
        let (dr, di) = (zr + i as f64, zi);
        let den = dr * dr + di * di;
        xr += C[i] * dr / den;
        xi -= C[i] * di / den;
    }
    let (tr, ti) = (zr + G + 0.5, zi);
    let mt = 0.5 * (tr * tr + ti * ti).ln();
    let at = ti.atan2(tr);
    let pe = (zr + 0.5) * mt - ti * at;
    let ph = ti * mt + (zr + 0.5) * at;
    let (ar, ai) = (pe.exp() * ph.cos(), pe.exp() * ph.sin());
    let e = (-tr).exp();
    let (br, bi) = (e * (-ti).cos(), e * (-ti).sin());
    let (c1r, c1i) = (ar * xr - ai * xi, ar * xi + ai * xr);
    let (d1r, d1i) = (c1r * br - c1i * bi, c1r * bi + c1i * br);
    let (gr, gi) = ((2.0 * PI).sqrt() * d1r, (2.0 * PI).sqrt() * d1i);
    (gr * gr + gi * gi).sqrt()
}

fn main() {
    let out = std::env::args().nth(1).unwrap_or_else(|| "verify_control.txt".into());
    let mut max_res = 0.0f64;
    for &u in &[0.5, 1.0, 2.0, 3.0] {
        let rfr = (PI / (PI * u).cosh()).sqrt();
        let res = ((mod_gamma(0.5, u) - rfr) / rfr).abs();
        if res > max_res { max_res = res; }
    }
    const N: usize = 100000;
    let mut spf = vec![0usize; N + 1];
    let mut sum = 0.0f64;
    for i in 2..=N {
        if spf[i] == 0 {
            let mut j = i;
            while j <= N { if spf[j] == 0 { spf[j] = i; } j += i; }
        }
    }
    for p in 2..=N {
        if spf[p] == p {
            let mut pk: u64 = p as u64;
            while pk <= N as u64 {
                sum += (p as f64).ln() / (pk as f64).powf(1.5);
                pk *= p as u64;
            }
        }
    }
    std::fs::write(&out, format!("gamma_closure_max_res = {:.3e}\nlambda_sum_check = {:.10}\nn_sieve = {}\n", max_res, sum, N)).unwrap();
    println!("rust twin OK: {:e} {}", max_res, sum);
}
