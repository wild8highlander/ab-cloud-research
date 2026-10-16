// ============================================================================
// abcloud — Rust port of the meridian-spectral-observatory suite.
//
// Bit-faithful kernel port of ab_cloud_full.jl / hp_audit_standalone.jl /
// AB_Cloud_Monumental_v6_3.jl (computational core), mirroring abcloud_port.cpp.
//
// Build:  cargo build --release
// Run:    cargo run --release -- selftest
//
// Eigenvalues: cyclic Jacobi for complex Hermitian matrices (no LAPACK;
// agrees with LAPACK to ~1e-12 on these spectra — inside golden tolerances).
// Disorder note: W>0 residual eps uses the portable classic MT19937 (Julia
// uses dSFMT — documented divergence; all golden anchors are W=0).
// ============================================================================

use std::env;
use std::fs;
use std::process::exit;

const PI: f64 = std::f64::consts::PI;

// ─────────────────────────────────────────────────────────────────────────────
// Minimal complex number (no external crates)
// ─────────────────────────────────────────────────────────────────────────────
#[derive(Clone, Copy, Default, Debug)]
struct Cx {
    re: f64,
    im: f64,
}

impl Cx {
    fn new(re: f64, im: f64) -> Self {
        Cx { re, im }
    }
    fn zero() -> Self {
        Cx { re: 0.0, im: 0.0 }
    }
    fn norm2(self) -> f64 {
        self.re * self.re + self.im * self.im
    }
    fn abs(self) -> f64 {
        self.norm2().sqrt()
    }
    fn arg(self) -> f64 {
        self.im.atan2(self.re)
    }
    fn conj(self) -> Self {
        Cx { re: self.re, im: -self.im }
    }
    fn scale(self, a: f64) -> Self {
        Cx { re: self.re * a, im: self.im * a }
    }
    fn add(self, o: Cx) -> Self {
        Cx { re: self.re + o.re, im: self.im + o.im }
    }
    fn sub(self, o: Cx) -> Self {
        Cx { re: self.re - o.re, im: self.im - o.im }
    }
    fn mul(self, o: Cx) -> Self {
        Cx {
            re: self.re * o.re - self.im * o.im,
            im: self.re * o.im + self.im * o.re,
        }
    }
    fn exp_i(phi: f64) -> Self {
        Cx { re: phi.cos(), im: phi.sin() }
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// Classic MT19937 (init_genrand) — bit-identical in all language ports.
// ─────────────────────────────────────────────────────────────────────────────
struct Mt19937 {
    mt: [u32; 624],
    idx: usize,
}

impl Mt19937 {
    fn new(seed: u32) -> Self {
        let mut mt = [0u32; 624];
        mt[0] = seed;
        for i in 1..624 {
            let prev = mt[i - 1];
            mt[i] = 1812433253u32
                .wrapping_mul(prev ^ (prev >> 30))
                .wrapping_add(i as u32);
        }
        Mt19937 { mt, idx: 624 }
    }
    fn next_u32(&mut self) -> u32 {
        if self.idx >= 624 {
            for kk in 0..624 {
                let y = (self.mt[kk] & 0x80000000) | (self.mt[(kk + 1) % 624] & 0x7fffffff);
                let mut nxt = self.mt[(kk + 397) % 624] ^ (y >> 1);
                if y & 1 != 0 {
                    nxt ^= 0x9908b0dfu32;
                }
                self.mt[kk] = nxt;
            }
            self.idx = 0;
        }
        let mut y = self.mt[self.idx];
        self.idx += 1;
        y ^= y >> 11;
        y ^= (y << 7) & 0x9d2c5680;
        y ^= (y << 15) & 0xefc60000;
        y ^= y >> 18;
        y
    }
    fn random(&mut self) -> f64 {
        let a = (self.next_u32() >> 5) as f64;
        let b = (self.next_u32() >> 6) as f64;
        (a * 67108864.0 + b) / 9007199254740992.0
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// Scalar special functions (see special.py / abcloud_port.cpp)
// ─────────────────────────────────────────────────────────────────────────────
const LANCZOS_COEF: [f64; 9] = [
    0.99999999999980993,
    676.5203681218851,
    -1259.1392167224028,
    771.32342877765313,
    -176.61502916214059,
    12.507343278686905,
    -0.13857109526572012,
    9.9843695780195716e-6,
    1.5056327351493116e-7,
];

fn lgamma_lanczos(x: f64) -> f64 {
    if x < 0.5 {
        return (PI / (PI * x).sin()).ln() - lgamma_lanczos(1.0 - x);
    }
    let x = x - 1.0;
    let mut a = LANCZOS_COEF[0];
    let t = x + 7.0 + 0.5;
    for i in 1..=7 {
        a += LANCZOS_COEF[i] / (x + i as f64);
    }
    0.5 * (2.0 * PI).ln() + (x + 0.5) * t.ln() - t + a.ln()
}

fn gammp_series(a: f64, x: f64) -> f64 {
    let mut ap = a;
    let mut total = 1.0 / a;
    let mut delta = total;
    for _ in 0..200 {
        ap += 1.0;
        delta *= x / ap;
        total += delta;
        if delta.abs() < total.abs() * 1e-15 {
            break;
        }
    }
    total * (-x + a * x.ln() - lgamma_lanczos(a)).exp()
}

fn gammq_cf(a: f64, x: f64) -> f64 {
    const FPMIN: f64 = 1e-300;
    let mut b = x + 1.0 - a;
    let mut c = 1.0 / FPMIN;
    let mut d = 1.0 / b;
    let mut h = d;
    for i in 1..=200 {
        let an = -(i as f64) * (i as f64 - a);
        b += 2.0;
        d = an * d + b;
        if d.abs() < FPMIN {
            d = FPMIN;
        }
        c = b + an / c;
        if c.abs() < FPMIN {
            c = FPMIN;
        }
        d = 1.0 / d;
        let delta = d * c;
        h *= delta;
        if (delta - 1.0).abs() < 1e-15 {
            break;
        }
    }
    (-x + a * x.ln() - lgamma_lanczos(a)).exp() * h
}

fn regularized_gamma_p(a: f64, x: f64) -> f64 {
    if x <= 0.0 {
        return 0.0;
    }
    if x < a + 1.0 {
        gammp_series(a, x)
    } else {
        1.0 - gammq_cf(a, x)
    }
}

fn chi2_cdf(x: f64, df: f64) -> f64 {
    regularized_gamma_p(df / 2.0, x / 2.0)
}

fn ks_asymptotic_pvalue(lam: f64) -> f64 {
    if lam <= 0.0 {
        return 1.0;
    }
    if lam < 0.6 {
        let mut s2 = 0.0;
        for k in 1..=1000u32 {
            let kk = 2.0 * k as f64 - 1.0;
            let term2 = (-(kk * kk) * PI * PI / (8.0 * lam * lam)).exp();
            s2 += term2;
            if term2 < 1e-18 {
                break;
            }
        }
        (1.0 - (2.0 * PI).sqrt() / lam * s2).clamp(0.0, 1.0)
    } else {
        let mut s = 0.0;
        let mut sign = 1.0;
        for k in 1..=100u32 {
            let term = sign * (-2.0 * (k as f64) * (k as f64) * lam * lam).exp();
            s += term;
            sign = -sign;
            if term.abs() < 1e-18 {
                break;
            }
        }
        (2.0 * s).clamp(0.0, 1.0)
    }
}

fn goe_surmise_cdf(s: f64) -> f64 {
    1.0 - (-PI * s * s / 4.0).exp()
}

fn gue2_surmise_cdf(s: f64) -> f64 {
    if s < 0.0 {
        return 0.0;
    }
    let x2 = 4.0 * s * s / PI;
    regularized_gamma_p(0.5, x2) - (4.0 * s / PI) * (-x2).exp()
}

fn gue2_surmise_pdf(s: f64) -> f64 {
    (32.0 / (PI * PI)) * s * s * (-4.0 * s * s / PI).exp()
}

fn lambert_w(x: f64) -> f64 {
    if x <= -1.0 / std::f64::consts::E {
        return -1.0;
    }
    let mut w = if x < 1.5 { x } else { x.ln() - x.ln().ln() };
    for _ in 0..50 {
        let ew = w.exp();
        let f = w * ew - x;
        let fp = ew * (w + 1.0);
        let fpp = ew * (w + 2.0);
        let delta = -f / (fp - 0.5 * f * fpp / fp);
        w += delta;
        if delta.abs() < 1e-15 * w.abs() {
            break;
        }
    }
    w
}

fn gram_point(n: i64) -> f64 {
    if n <= 0 {
        return 0.0;
    }
    let mut t = 2.0 * PI * n as f64 / lambert_w(n as f64 / std::f64::consts::E);
    for _ in 0..8 {
        let arg = t / (2.0 * PI);
        if arg <= 0.0 {
            break;
        }
        let theta = t / 2.0 * arg.ln() - t / 2.0 - PI / 8.0
            + 1.0 / (48.0 * t)
            + 7.0 / (5760.0 * t * t * t);
        let dtheta = 0.5 * arg.ln() - 1.0 / (48.0 * t * t) - 21.0 / (5760.0 * t * t * t * t);
        if dtheta.abs() < 1e-30 {
            break;
        }
        t -= (theta - n as f64 * PI) / dtheta;
    }
    t
}

fn compute_bn(z: &[f64], n: i64, offset: i64) -> f64 {
    let n = n.min(z.len() as i64);
    let mut s = 0.0;
    for k in 1..=n {
        s += (z[(k - 1) as usize] - gram_point(offset + k)).abs();
    }
    s / n as f64
}

// ─────────────────────────────────────────────────────────────────────────────
// RMT reference-law engine (see rmt_table.py)
// ─────────────────────────────────────────────────────────────────────────────
struct RmtTable {
    table: Vec<f64>,
    quant: Vec<f64>,
}

impl RmtTable {
    fn new() -> Self {
        RmtTable { table: Vec::new(), quant: Vec::new() }
    }
    fn table_cdf(&mut self, s: f64) -> f64 {
        if s < 0.0 {
            return 0.0;
        }
        if self.table.is_empty() {
            self.table = (0..32768)
                .map(|i| gue2_surmise_cdf(i as f64 * 5.0 / 32767.0))
                .collect();
        }
        if s >= 5.0 {
            return gue2_surmise_cdf(s);
        }
        let x = s * 32767.0 / 5.0;
        let i = x.floor() as usize;
        if i >= 32767 {
            return gue2_surmise_cdf(s);
        }
        let t = x - i as f64;
        (1.0 - t) * self.table[i] + t * self.table[i + 1]
    }
    fn gue_cdf(&mut self, s: f64) -> f64 {
        self.table_cdf(s)
    }
    fn build_quant(&mut self) {
        let smax = 5.0;
        let umax = self.gue_cdf(smax);
        let m = 4096usize;
        let mut q = vec![0.0; m + 1];
        for j in 0..=m {
            let u = umax * j as f64 / m as f64;
            let (mut lo, mut hi) = (0.0f64, smax);
            for _ in 0..48 {
                let mid = 0.5 * (lo + hi);
                if self.gue_cdf(mid) < u {
                    lo = mid;
                } else {
                    hi = mid;
                }
            }
            q[j] = 0.5 * (lo + hi);
        }
        self.quant = q;
    }
    fn sample(&mut self, rng: &mut Mt19937, out: &mut [f64]) {
        if self.quant.is_empty() {
            self.build_quant();
        }
        let m = 4096usize;
        for k in 0..out.len() {
            let x = rng.random() * m as f64;
            let mut j = x.floor() as i64;
            if j > m as i64 - 1 {
                j = m as i64 - 1;
            }
            if j < 0 {
                j = 0;
            }
            let t = (x - j as f64).min(1.0);
            out[k] = (1.0 - t) * self.quant[j as usize] + t * self.quant[j as usize + 1];
        }
    }
}

// [PART2]
// ─────────────────────────────────────────────────────────────────────────────
// GOF + long-range statistics (see gof.py; rmt table passed explicitly)
// ─────────────────────────────────────────────────────────────────────────────
fn normalized_spacings(z: &[f64]) -> Vec<f64> {
    let mut sp = Vec::new();
    for k in 0..z.len().saturating_sub(1) {
        if z[k] > 0.0 {
            sp.push((z[k + 1] - z[k]) * (z[k] / (2.0 * PI)).ln() / (2.0 * PI));
        }
    }
    sp
}

struct Linreg {
    a: f64,
    b: f64,
    r2: f64,
    se_b: f64,
    res: Vec<f64>,
}

fn linreg(x: &[f64], y: &[f64]) -> Linreg {
    let n = x.len();
    let mx = x.iter().sum::<f64>() / n as f64;
    let my = y.iter().sum::<f64>() / n as f64;
    let sxx: f64 = x.iter().map(|v| (v - mx) * (v - mx)).sum();
    let sxy: f64 = x.iter().zip(y).map(|(xi, yi)| (xi - mx) * (yi - my)).sum();
    if sxx == 0.0 || n < 2 {
        return Linreg { a: 0.0, b: 0.0, r2: 0.0, se_b: f64::NAN, res: vec![0.0; n] };
    }
    let b = sxy / sxx;
    let a = my - b * mx;
    let mut res = Vec::with_capacity(n);
    let mut ss_res = 0.0;
    let mut ss_tot = 0.0;
    for i in 0..n {
        let r = y[i] - (a + b * x[i]);
        res.push(r);
        ss_res += r * r;
        ss_tot += (y[i] - my) * (y[i] - my);
    }
    let r2 = if ss_tot > 0.0 { 1.0 - ss_res / ss_tot } else { 0.0 };
    let se_b = if n > 2 && sxx > 0.0 {
        (ss_res / ((n - 2) as f64 * sxx)).sqrt()
    } else {
        f64::NAN
    };
    Linreg { a, b, r2, se_b, res }
}

fn ks_test(r: &mut RmtTable, sp: &[f64]) -> (f64, f64) {
    let n = sp.len();
    let mut s = sp.to_vec();
    s.sort_by(|a, b| a.partial_cmp(b).unwrap());
    let mut d = 0.0f64;
    for i in 1..=n {
        let f = r.gue_cdf(s[i - 1]);
        d = d.max(((i as f64) / n as f64 - f).abs())
            .max((((i - 1) as f64) / n as f64 - f).abs());
    }
    let lam = ((n as f64).sqrt() + 0.12 + 0.11 / (n as f64).sqrt()) * d;
    (d, ks_asymptotic_pvalue(lam))
}

fn cvm_test(r: &mut RmtTable, sp: &[f64]) -> f64 {
    let n = sp.len();
    let mut s = sp.to_vec();
    s.sort_by(|a, b| a.partial_cmp(b).unwrap());
    let mut w2 = 0.0;
    for i in 1..=n {
        let u = r.gue_cdf(s[i - 1]);
        let dev = u - (2.0 * i as f64 - 1.0) / (2.0 * n as f64);
        w2 += dev * dev;
    }
    w2 + 1.0 / (12.0 * n as f64)
}

fn anderson_darling_stat(r: &mut RmtTable, sp: &[f64]) -> f64 {
    let n = sp.len();
    let mut s = sp.to_vec();
    s.sort_by(|a, b| a.partial_cmp(b).unwrap());
    let mut acc = 0.0;
    for i in 1..=n {
        let fi = r.gue_cdf(s[i - 1]).clamp(1e-300, 1.0 - 1e-16);
        let fni = r.gue_cdf(s[n - i]).clamp(1e-300, 1.0 - 1e-16);
        acc += (2.0 * i as f64 - 1.0) * (fi.ln() + (1.0 - fni).ln());
    }
    -(n as f64) - acc / n as f64
}

fn chi2_gue_test(r: &mut RmtTable, sp: &[f64], nbins: usize) -> (f64, i64, f64) {
    let mut s = sp.to_vec();
    s.sort_by(|a, b| a.partial_cmp(b).unwrap());
    let s_max = (*s.last().unwrap()).min(4.0);
    let mut obs = vec![0i64; nbins];
    for v in &s {
        if *v >= s_max {
            obs[nbins - 1] += 1;
        } else {
            let b = (((v / s_max * nbins as f64).floor() as usize) + 1).min(nbins);
            obs[b - 1] += 1;
        }
    }
    let n = s.len();
    let mut edges = vec![0.0; nbins + 1];
    for (i, e) in edges.iter_mut().enumerate() {
        *e = s_max * i as f64 / nbins as f64;
    }
    let mut chi2 = 0.0;
    let mut df = 0i64;
    for i in 1..=nbins {
        let ec = if i < nbins {
            n as f64 * (r.gue_cdf(edges[i]) - r.gue_cdf(edges[i - 1]))
        } else {
            n as f64 * (1.0 - r.gue_cdf(edges[i - 1]))
        };
        if ec < 5.0 {
            continue;
        }
        chi2 += (obs[i - 1] as f64 - ec).powi(2) / ec;
        df += 1;
    }
    df = (df - 1).max(1);
    let p = 1.0 - chi2_cdf(chi2, df as f64);
    (chi2, df, p)
}

fn mean_adjacent_spacing_ratio(eigs: &[f64]) -> (f64, i64) {
    let n = eigs.len();
    if n < 3 {
        return (f64::NAN, 0);
    }
    let mut s = eigs.to_vec();
    s.sort_by(|a, b| a.partial_cmp(b).unwrap());
    let d: Vec<f64> = (0..n - 1).map(|i| s[i + 1] - s[i]).collect();
    if d.len() < 2 {
        return (f64::NAN, 0);
    }
    let mut acc = 0.0;
    let mut cnt = 0i64;
    for i in 0..d.len() - 1 {
        let (a, b) = (d[i], d[i + 1]);
        let m = a.max(b);
        if a == 0.0 && b == 0.0 {
            continue;
        }
        acc += a.min(b) / m;
        cnt += 1;
    }
    if cnt <= 0 {
        return (f64::NAN, 0);
    }
    (acc / cnt as f64, cnt)
}

fn smooth_counting_function(t: f64) -> f64 {
    if t <= 0.0 {
        return 0.0;
    }
    let x = t / (2.0 * PI);
    x * x.ln() - x + 7.0 / 8.0
}

fn unfolded_positions(z: &[f64]) -> Vec<f64> {
    z.iter().map(|t| smooth_counting_function(*t)).collect()
}

fn number_variance(pos: &[f64], l: f64, n_windows: usize, rng: &mut Mt19937) -> f64 {
    let ltot = *pos.last().unwrap() - pos[0];
    if ltot <= l {
        return f64::NAN;
    }
    let mut counts = Vec::with_capacity(n_windows);
    for _ in 0..n_windows {
        let x0 = pos[0] + rng.random() * (ltot - l);
        let lo = pos.partition_point(|v| *v < x0);
        let hi = pos.partition_point(|v| *v < x0 + l);
        counts.push((hi - lo) as f64);
    }
    let mean = counts.iter().sum::<f64>() / n_windows as f64;
    let var: f64 = counts.iter().map(|c| (c - mean) * (c - mean)).sum();
    var / (n_windows - 1) as f64
}

fn delta3_rigidity(pos: &[f64], l: f64, n_windows: usize, n_grid: usize,
                   rng: &mut Mt19937) -> f64 {
    let ltot = *pos.last().unwrap() - pos[0];
    if ltot <= l {
        return f64::NAN;
    }
    let xs: Vec<f64> = (0..n_grid).map(|i| l * i as f64 / (n_grid - 1) as f64).collect();
    let mut total = 0.0;
    for _ in 0..n_windows {
        let x0 = pos[0] + rng.random() * (ltot - l);
        let idx0 = pos.partition_point(|v| *v < x0);
        let nv: Vec<f64> = xs
            .iter()
            .map(|x| (pos.partition_point(|v| *v < x0 + x) - idx0) as f64)
            .collect();
        let r = linreg(&xs, &nv);
        total += r.res.iter().map(|e| e * e).sum::<f64>() / n_grid as f64;
    }
    total / n_windows as f64
}

fn compute_k_single_seed(eigs: &[f64], tvals: &[f64]) -> Vec<f64> {
    let n = eigs.len();
    if n < 10 {
        return vec![0.0; tvals.len()];
    }
    let mut s = eigs.to_vec();
    s.sort_by(|a, b| a.partial_cmp(b).unwrap());
    let window = (((n as f64) * 0.05).round() as i64).max(3) as usize;
    let mut u = vec![0.0; n];
    for i in 1..n {
        let i_lo = i.saturating_sub(window);
        let i_hi = (i + window).min(n - 1);
        let dens = (i_hi - i_lo + 1) as f64 / (s[i_hi] - s[i_lo] + 1e-12);
        u[i] = u[i - 1] + (s[i] - s[i - 1]) * dens;
    }
    let ms = (u[n - 1] - u[0]) / (n - 1) as f64;
    if ms > 1e-12 {
        for v in u.iter_mut() {
            *v /= ms;
        }
    }
    let mut k = Vec::with_capacity(tvals.len());
    for t in tvals {
        if *t == 0.0 {
            k.push(0.0);
            continue;
        }
        let mut re = 0.0;
        let mut im = 0.0;
        for uu in &u {
            let ph = 2.0 * PI * t * uu;
            re += ph.cos();
            im += ph.sin();
        }
        k.push(((re * re + im * im) / n as f64).max(0.0));
    }
    let w = 3usize;
    if k.len() > 2 * w {
        let mut ks = k.clone();
        for j in w..k.len() - w {
            if tvals[j] < 0.5 {
                continue;
            }
            let acc: f64 = k[j - w..=j + w].iter().sum();
            ks[j] = acc / (2 * w + 1) as f64;
        }
        k = ks;
    }
    k
}

fn compute_k_form_factor(eigs: &[f64], tvals: &[f64]) -> Vec<f64> {
    compute_k_single_seed(eigs, tvals)
}

fn hp_kgue_envelope(t: f64) -> f64 {
    if t < 1.0 {
        let x = 2.0 * PI * t;
        let sn = if x.abs() < 1e-12 { 1.0 } else { x.sin() / x };
        t * (1.0 - sn)
    } else {
        1.0
    }
}

fn hp_unfold_local(eigs: &[f64], win_frac: f64) -> Vec<f64> {
    let mut s = eigs.to_vec();
    s.sort_by(|a, b| a.partial_cmp(b).unwrap());
    let n = s.len();
    if n < 10 {
        return (0..n).map(|i| i as f64).collect();
    }
    let window = (((n as f64) * win_frac).round() as i64).max(3) as usize;
    let mut u = vec![0.0; n];
    for i in 1..n {
        let i_lo = i.saturating_sub(window);
        let i_hi = (i + window).min(n - 1);
        let dens = (i_hi - i_lo + 1) as f64 / (s[i_hi] - s[i_lo] + 1e-12);
        u[i] = u[i - 1] + (s[i] - s[i - 1]) * dens;
    }
    let ms = (u[n - 1] - u[0]) / ((n - 1).max(1) as f64);
    if ms > 1e-12 {
        for v in u.iter_mut() {
            *v /= ms;
        }
    }
    u
}

fn unit_spacings(u: &[f64]) -> Vec<f64> {
    let mut d: Vec<f64> = u.windows(2).map(|w| w[1] - w[0]).collect();
    if d.is_empty() {
        return d;
    }
    let m = d.iter().sum::<f64>() / d.len() as f64;
    if m > 1e-300 {
        for v in d.iter_mut() {
            *v /= m;
        }
    }
    d
}

fn ks2(a: &[f64], b: &[f64]) -> f64 {
    let mut xs = a.to_vec();
    let mut ys = b.to_vec();
    xs.sort_by(|p, q| p.partial_cmp(q).unwrap());
    ys.sort_by(|p, q| p.partial_cmp(q).unwrap());
    let (n, m) = (xs.len(), ys.len());
    let (mut i, mut j) = (0usize, 0usize);
    let mut d = 0.0f64;
    while i < n && j < m {
        if xs[i] < ys[j] {
            i += 1;
        } else if ys[j] < xs[i] {
            j += 1;
        } else {
            let xv = xs[i];
            while i < n && xs[i] == xv {
                i += 1;
            }
            while j < m && ys[j] == xv {
                j += 1;
            }
        }
        d = d.max((i as f64 / n as f64 - j as f64 / m as f64).abs());
    }
    d
}

// [PART3]
// ─────────────────────────────────────────────────────────────────────────────
// Lattice (see lattice.py) + cyclic Jacobi Hermitian eigensolver
// ─────────────────────────────────────────────────────────────────────────────
#[derive(Clone, Copy)]
struct Vortex {
    x: f64,
    y: f64,
    q: f64,
}

struct AbCloudConfig {
    nx: usize,
    ny: usize,
    vortices: Vec<Vortex>,
    alpha: f64,
    t: f64,
    lattice: String, // "open" | "torus"
    w: f64,
    disorder_seed: u32,
    model: String, // "monumental" | "dirac"
}

impl AbCloudConfig {
    fn new(nx: usize, ny: usize, vortices: Vec<Vortex>, alpha: f64, t: f64,
           lattice: &str, w: f64) -> Self {
        AbCloudConfig {
            nx, ny, vortices, alpha, t,
            lattice: lattice.to_string(),
            w,
            disorder_seed: 96,
            model: "monumental".to_string(),
        }
    }
    fn with(mut self, seed: u32, model: &str) -> Self {
        self.disorder_seed = seed;
        self.model = model.to_string();
        self
    }
}

fn ab_phase_vortex_monumental(ri: [f64; 2], rj: [f64; 2], vort: &[Vortex]) -> f64 {
    let mut phase = 0.0;
    for vk in vort {
        let (dx1, dy1) = (ri[0] - vk.x, ri[1] - vk.y);
        let (dx2, dy2) = (rj[0] - vk.x, rj[1] - vk.y);
        let a1 = if dx1 != 0.0 || dy1 != 0.0 { dy1.atan2(dx1) } else { 0.0 };
        let a2 = if dx2 != 0.0 || dy2 != 0.0 { dy2.atan2(dx2) } else { 0.0 };
        phase += vk.q * (a2 - a1) * 0.5;
    }
    phase
}

fn ab_phase_2d(ri: [f64; 2], rj: [f64; 2], rk: [f64; 2], qk: f64) -> f64 {
    let ti = (ri[1] - rk[1]).atan2(ri[0] - rk[0]);
    let tj = (rj[1] - rk[1]).atan2(rj[0] - rk[0]);
    qk * (ti - tj)
}

fn dirac_string_phase(ri: [f64; 2], rj: [f64; 2], rk: [f64; 2], qk: f64,
                      torus: bool, nx: usize) -> f64 {
    if (ri[0] - rj[0]).abs() > 1e-12 {
        return 0.0;
    }
    let (y_lo, y_hi) = (ri[1].min(rj[1]), ri[1].max(rj[1]));
    if !(y_lo < rk[1] && rk[1] < y_hi) {
        return 0.0;
    }
    if torus {
        if (ri[0] - rk[0].floor()).abs() < 0.5 {
            return 0.0;
        }
    } else if ri[0] <= rk[0] {
        return 0.0;
    }
    let _ = nx;
    if ri[1] < rj[1] {
        -2.0 * PI * qk
    } else {
        2.0 * PI * qk
    }
}

fn ab_phase_2d_full(ri: [f64; 2], rj: [f64; 2], rk: [f64; 2], qk: f64,
                    torus: bool, nx: usize) -> f64 {
    ab_phase_2d(ri, rj, rk, qk) + dirac_string_phase(ri, rj, rk, qk, torus, nx)
}

fn vortex_onsite_potential(ri: [f64; 2], vort: &[Vortex], w: f64, n: usize,
                           rng: &mut Mt19937) -> f64 {
    if vort.is_empty() && w == 0.0 {
        return 0.0;
    }
    let mut v = 0.0;
    let ninv = 1.0 / n.max(1) as f64;
    for vk in vort {
        let (dx, dy) = (ri[0] - vk.x, ri[1] - vk.y);
        v += vk.q * w / ((dx * dx + dy * dy) * ninv + 1.0);
    }
    if w > 0.0 {
        v += (rng.random() - 0.5) * 0.02;
    }
    v
}

fn build_ab_cloud_hamiltonian(cfg: &AbCloudConfig) -> Vec<Cx> {
    let (nx, ny) = (cfg.nx, cfg.ny);
    let n = nx * ny;
    let torus = cfg.lattice == "torus";
    if torus && (cfg.alpha * ny as f64 - (cfg.alpha * ny as f64).round()).abs() >= 1e-10 {
        eprintln!("ASSERT: torus needs alpha*Ny integer");
        exit(2);
    }
    let mut rng = Mt19937::new(cfg.disorder_seed);
    let mut h = vec![Cx::zero(); n * n];
    for iy in 1..=ny {
        for ix in 1..=nx {
            let i = (iy - 1) * nx + ix - 1;
            let ri = [ix as f64, iy as f64];
            // right neighbour
            {
                let (mut jx, mut wrap) = (ix + 1, false);
                if jx > nx {
                    if torus {
                        jx = 1;
                        wrap = true;
                    } else {
                        jx = 0;
                    }
                }
                if jx != 0 {
                    let j = (iy - 1) * nx + jx - 1;
                    let mut phi = 2.0 * PI * cfg.alpha * iy as f64;
                    if cfg.model == "dirac" {
                        let rjp = [if wrap { (nx + 1) as f64 } else { jx as f64 }, iy as f64];
                        for v in &cfg.vortices {
                            phi += ab_phase_2d_full(ri, rjp, [v.x, v.y], v.q, torus, nx);
                        }
                    }
                    let hop = Cx::new(-cfg.t, 0.0).mul(Cx::exp_i(phi));
                    h[i * n + j] = h[i * n + j].add(hop);
                    h[j * n + i] = h[j * n + i].add(hop.conj());
                }
            }
            // up neighbour
            {
                let (mut jy, mut wrap) = (iy + 1, false);
                if jy > ny {
                    if torus {
                        jy = 1;
                        wrap = true;
                    } else {
                        jy = 0;
                    }
                }
                if jy != 0 {
                    let j = (jy - 1) * nx + ix - 1;
                    let mut phi = if wrap { 2.0 * PI * cfg.alpha * ny as f64 } else { 0.0 };
                    let rjp = [ix as f64, (iy + 1) as f64]; // unwrapped top
                    if cfg.model == "monumental" {
                        phi += ab_phase_vortex_monumental(ri, rjp, &cfg.vortices);
                    } else {
                        for v in &cfg.vortices {
                            phi += ab_phase_2d_full(ri, rjp, [v.x, v.y], v.q, torus, nx);
                        }
                    }
                    let hop = Cx::new(-cfg.t, 0.0).mul(Cx::exp_i(phi));
                    h[i * n + j] = h[i * n + j].add(hop);
                    h[j * n + i] = h[j * n + i].add(hop.conj());
                }
            }
            h[i * n + i] = h[i * n + i].add(Cx::new(
                vortex_onsite_potential(ri, &cfg.vortices, cfg.w, n, &mut rng),
                0.0,
            ));
        }
    }
    // Hermitian symmetrization (H + H†)/2
    for r in 0..n {
        for c in (r + 1)..n {
            let a = h[r * n + c];
            let b = h[c * n + r];
            let m = Cx::new(0.5, 0.0).mul(a.add(b.conj()));
            h[r * n + c] = m;
            h[c * n + r] = m.conj();
        }
    }
    h
}

fn off_norm(h: &[Cx], n: usize) -> f64 {
    let mut acc = 0.0;
    for r in 0..n {
        for c in (r + 1)..n {
            acc += h[r * n + c].norm2();
        }
    }
    acc
}

fn jacobi_eigvals(h_in: &[Cx], n: usize) -> Vec<f64> {
    let mut h = h_in.to_vec();
    let max_sweeps = 60usize;
    let off0: f64 = off_norm(&h, n);
    let thresh = 1e-15 * (2.0 * off0 + 1e-300).sqrt();
    for _ in 0..max_sweeps {
        let off = off_norm(&h, n);
        if (2.0 * off).sqrt() < thresh {
            break;
        }
        for p in 0..n - 1 {
            for q in (p + 1)..n {
                let apq = h[p * n + q];
                if apq.abs() <= thresh {
                    continue;
                }
                let app = h[p * n + p].re;
                let aqq = h[q * n + q].re;
                let tau = (aqq - app) / (2.0 * apq.abs());
                let t = (if tau >= 0.0 { 1.0 } else { -1.0 })
                    / (tau.abs() + (1.0 + tau * tau).sqrt());
                let c = 1.0 / (1.0 + t * t).sqrt();
                let s = t * c; // normalized rotation
                let phase = apq.scale(1.0 / apq.abs());
                let se = phase.scale(s);
                let sec = se.conj();
                for k in 0..n {
                    if k == p || k == q {
                        continue;
                    }
                    let akp = h[k * n + p];
                    let akq = h[k * n + q];
                    let nkp = akp.scale(c).sub(sec.mul(akq));
                    let nkq = se.mul(akp).add(akq.scale(c));
                    h[k * n + p] = nkp;
                    h[p * n + k] = nkp.conj();
                    h[k * n + q] = nkq;
                    h[q * n + k] = nkq.conj();
                }
                let npp = app - t * apq.abs();
                let nqq = aqq + t * apq.abs();
                h[p * n + p] = Cx::new(npp, 0.0);
                h[q * n + q] = Cx::new(nqq, 0.0);
                h[p * n + q] = Cx::zero();
                h[q * n + p] = Cx::zero();
            }
        }
    }
    let mut ev: Vec<f64> = (0..n).map(|r| h[r * n + r].re).collect();
    ev.sort_by(|a, b| a.partial_cmp(b).unwrap());
    ev
}

fn plaquette_flux(h: &[Cx], nx: usize, ny: usize, ix: usize, iy: usize,
                  torus: bool) -> f64 {
    let n = nx * ny;
    let ix_r = if torus { (ix % nx) + 1 } else { ix + 1 };
    let iy_t = if torus { (iy % ny) + 1 } else { iy + 1 };
    let i_bl = (iy - 1) * nx + ix - 1;
    let i_br = (iy - 1) * nx + ix_r - 1;
    let i_tr = (iy_t - 1) * nx + ix_r - 1;
    let i_tl = (iy_t - 1) * nx + ix - 1;
    let fb = Cx::new(-1.0, 0.0).mul(h[i_br * n + i_bl]).arg();
    let fr = Cx::new(-1.0, 0.0).mul(h[i_tr * n + i_br]).arg();
    let ft = Cx::new(-1.0, 0.0).mul(h[i_tl * n + i_tr]).arg();
    let fl = Cx::new(-1.0, 0.0).mul(h[i_bl * n + i_tl]).arg();
    fb + fr + ft + fl
}

fn flux_circdist(a: f64, b: f64) -> f64 {
    let m = (a - b + PI) % (2.0 * PI);
    let m = if m < 0.0 { m + 2.0 * PI } else { m };
    (m - PI).abs()
}

fn central_band_eigs(s: &[f64], frac: f64) -> Vec<f64> {
    let n = s.len();
    if n == 0 {
        return vec![];
    }
    let frac = frac.clamp(0.05, 1.0);
    if frac >= 1.0 {
        return s.to_vec();
    }
    let half = ((n as f64) * frac / 2.0).floor() as i64;
    let j_lo = (n as i64 / 2 - half).max(1) as usize;
    let j_hi = ((n as i64 / 2 + half).min(n as i64)) as usize;
    s[j_lo - 1..j_hi].to_vec()
}

fn chiral_symmetry_defect(h: &[Cx], nx: usize, ny: usize) -> f64 {
    let n = nx * ny;
    let mut num = 0.0;
    let mut den = 0.0;
    for r in 0..n {
        let sr = if (((r % nx) + 1) + (r / nx + 1)) % 2 == 0 { 1.0 } else { -1.0 };
        for c in 0..n {
            let sc = if (((c % nx) + 1) + (c / nx + 1)) % 2 == 0 { 1.0 } else { -1.0 };
            let v = h[r * n + c].scale(sr * sc).add(h[r * n + c]);
            num += v.norm2();
            den += h[r * n + c].norm2();
        }
    }
    num.sqrt() / den.sqrt().max(1e-30)
}

fn verify_hermitian(h: &[Cx], n: usize) -> bool {
    let mut max_err = 0.0f64;
    let mut norm = 0.0f64;
    for r in 0..n {
        for c in 0..n {
            norm += h[r * n + c].norm2();
            max_err = max_err.max(h[r * n + c].sub(h[c * n + r].conj()).abs());
        }
    }
    max_err / norm.sqrt().max(1e-30) < 1e-12
}

fn time_reversal_asymmetry(h: &[Cx]) -> f64 {
    let mut diff = 0.0;
    let mut norm = 0.0;
    for v in h {
        norm += v.norm2();
        diff += v.sub(Cx::new(v.re, -v.im)).norm2();
    }
    diff.sqrt() / norm.sqrt().max(1e-30)
}

// [PART4]
// ─────────────────────────────────────────────────────────────────────────────
// Minimal JSON reader for the golden file
// ─────────────────────────────────────────────────────────────────────────────
#[derive(Clone, Debug)]
enum Json {
    Obj(Vec<(String, Json)>),
    Arr(Vec<Json>),
    Num(f64),
    Str(String),
}

struct JsonParser<'a> {
    b: &'a [u8],
    p: usize,
}

impl<'a> JsonParser<'a> {
    fn new(s: &'a str) -> Self {
        JsonParser { b: s.as_bytes(), p: 0 }
    }
    fn ws(&mut self) {
        while self.p < self.b.len() && (self.b[self.p] as char).is_ascii_whitespace() {
            self.p += 1;
        }
    }
    fn parse(&mut self) -> Json {
        self.ws();
        match self.b[self.p] {
            b'{' => {
                self.p += 1;
                let mut obj = Vec::new();
                self.ws();
                if self.b[self.p] == b'}' {
                    self.p += 1;
                    return Json::Obj(obj);
                }
                loop {
                    self.ws();
                    let key = self.parse_string();
                    self.ws();
                    self.p += 1; // ':'
                    let v = self.parse();
                    obj.push((key, v));
                    self.ws();
                    match self.b[self.p] {
                        b',' => {
                            self.p += 1;
                        }
                        b'}' => {
                            self.p += 1;
                            break;
                        }
                        _ => panic!("json: expected , or }}"),
                    }
                }
                Json::Obj(obj)
            }
            b'[' => {
                self.p += 1;
                let mut arr = Vec::new();
                self.ws();
                if self.b[self.p] == b']' {
                    self.p += 1;
                    return Json::Arr(arr);
                }
                loop {
                    arr.push(self.parse());
                    self.ws();
                    match self.b[self.p] {
                        b',' => {
                            self.p += 1;
                        }
                        b']' => {
                            self.p += 1;
                            break;
                        }
                        _ => panic!("json: expected , or ]"),
                    }
                }
                Json::Arr(arr)
            }
            b'"' => Json::Str(self.parse_string()),
            _ => {
                let start = self.p;
                while self.p < self.b.len()
                    && (self.b[self.p].is_ascii_digit()
                        || matches!(self.b[self.p], b'-' | b'+' | b'.' | b'e' | b'E'))
                {
                    self.p += 1;
                }
                let s = std::str::from_utf8(&self.b[start..self.p]).unwrap();
                Json::Num(s.parse().unwrap_or(0.0))
            }
        }
    }
    fn parse_string(&mut self) -> String {
        self.p += 1; // opening quote
        let mut out = String::new();
        while self.b[self.p] != b'"' {
            if self.b[self.p] == b'\\' {
                self.p += 1;
                match self.b[self.p] {
                    b'n' => out.push('\n'),
                    b't' => out.push('\t'),
                    b'r' => out.push('\r'),
                    b'u' => {
                        let hex = std::str::from_utf8(&self.b[self.p + 1..self.p + 5]).unwrap();
                        let code = u32::from_str_radix(hex, 16).unwrap_or(0xFFFD);
                        if let Some(ch) = char::from_u32(code) {
                            out.push(ch);
                        }
                        self.p += 4;
                    }
                    c => out.push(c as char),
                }
                self.p += 1;
            } else {
                // UTF-8 pass-through
                let len = if self.b[self.p] < 0x80 {
                    1
                } else if self.b[self.p] >> 5 == 0b110 {
                    2
                } else if self.b[self.p] >> 4 == 0b1110 {
                    3
                } else {
                    4
                };
                out.push_str(std::str::from_utf8(&self.b[self.p..self.p + len]).unwrap_or("?"));
                self.p += len;
            }
        }
        self.p += 1; // closing quote
        out
    }
}

impl Json {
    fn get(&self, key: &str) -> Option<&Json> {
        match self {
            Json::Obj(v) => v.iter().find(|(k, _)| k == key).map(|(_, v)| v),
            _ => None,
        }
    }
    fn num(&self) -> f64 {
        match self {
            Json::Num(v) => *v,
            _ => 0.0,
        }
    }
}

fn load_zeros(path: &str) -> Vec<f64> {
    let text = fs::read_to_string(path).unwrap_or_else(|_| {
        eprintln!("ERROR: cannot open zeros file: {}", path);
        exit(2);
    });
    let mut z: Vec<f64> = text
        .split_whitespace()
        .filter_map(|t| t.parse::<f64>().ok())
        .collect();
    z.sort_by(|a, b| a.partial_cmp(b).unwrap());
    z
}

fn shortest(v: f64) -> String {
    for prec in 1..=17 {
        let s = format!("{:.*}", prec, v);
        if !s.contains('e') && s.parse::<f64>() == Ok(v) {
            if !s.contains('.') {
                return format!("{}.0", s);
            }
            return s;
        }
    }
    for prec in 1..=17 {
        let s = format!("{:.*e}", prec, v);
        if s.parse::<f64>() == Ok(v) {
            return s;
        }
    }
    format!("{}", v)
}

struct Sec(std::collections::BTreeMap<String, f64>);

fn compute_all(zeta: &[f64], golden: &Json) -> std::collections::BTreeMap<String, Sec> {
    let mut sec: std::collections::BTreeMap<String, Sec> = std::collections::BTreeMap::new();
    let mut rmt = RmtTable::new();

    // 1. Lambert W / Gram points
    for x in [0.5f64, 1.0, 3.7, 10.0, 271.8, 12345.6] {
        sec.entry("lambert_w".into()).or_insert(Sec(Default::default())).0
            .insert(format!("x={}", shortest(x)), lambert_w(x));
    }
    for n in [1i64, 2, 3, 10, 100, 1000, 10000, 50000] {
        sec.entry("gram_point".into()).or_insert(Sec(Default::default())).0
            .insert(format!("n={}", n), gram_point(n));
    }
    // 2. b(N)
    for n in [100i64, 500, 1000, 5000, 10000, 50000] {
        sec.entry("bN".into()).or_insert(Sec(Default::default())).0
            .insert(format!("N={}", n), compute_bn(zeta, n, 0));
    }
    sec.entry("bN".into()).or_insert(Sec(Default::default())).0
        .insert("N=1000_off500".into(), compute_bn(zeta, 1000, 500));
    // 3. spacings
    let sp = normalized_spacings(zeta);
    {
        let mean = sp.iter().sum::<f64>() / sp.len() as f64;
        let var = sp.iter().map(|s| (s - mean) * (s - mean)).sum::<f64>() / (sp.len() - 1) as f64;
        let d = sec.entry("spacings".into()).or_insert(Sec(Default::default()));
        d.0.insert("n".into(), sp.len() as f64);
        d.0.insert("mean".into(), mean);
        d.0.insert("var".into(), var);
    }
    // 4. surmises / special
    for s in [0.05f64, 0.1, 0.25, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 4.9] {
        let k = format!("s={}", shortest(s));
        sec.entry("gue2_cdf".into()).or_insert(Sec(Default::default())).0
            .insert(k.clone(), gue2_surmise_cdf(s));
        sec.entry("goe_cdf".into()).or_insert(Sec(Default::default())).0
            .insert(k.clone(), goe_surmise_cdf(s));
        sec.entry("gue2_pdf".into()).or_insert(Sec(Default::default())).0
            .insert(k, gue2_surmise_pdf(s));
    }
    for (a, x) in [(0.5f64, 0.1), (0.5, 2.0), (1.0, 1.0), (2.0, 3.0), (0.5, 12.0)] {
        sec.entry("gamma_p".into()).or_insert(Sec(Default::default())).0
            .insert(format!("a={}_x={}", shortest(a), shortest(x)), regularized_gamma_p(a, x));
    }
    for (x, df) in [(3.84f64, 1.0), (16.92, 29.0), (25.0, 10.0)] {
        sec.entry("chi2_cdf".into()).or_insert(Sec(Default::default())).0
            .insert(format!("x={}_df={}", shortest(x), shortest(df)), chi2_cdf(x, df));
    }
    for lam in [0.5f64, 1.3, 0.02] {
        sec.entry("ks_pvalue".into()).or_insert(Sec(Default::default())).0
            .insert(format!("lam={}", shortest(lam)), ks_asymptotic_pvalue(lam));
    }
    // 5. GOF
    {
        let (d_ks, p_ks) = ks_test(&mut rmt, &sp);
        let d = sec.entry("ks_zeros".into()).or_insert(Sec(Default::default()));
        d.0.insert("D".into(), d_ks);
        d.0.insert("p".into(), p_ks);
        sec.entry("cvm_zeros".into()).or_insert(Sec(Default::default())).0
            .insert("W2".into(), cvm_test(&mut rmt, &sp));
        sec.entry("ad_zeros".into()).or_insert(Sec(Default::default())).0
            .insert("A2".into(), anderson_darling_stat(&mut rmt, &sp));
        let (chi2, df, p) = chi2_gue_test(&mut rmt, &sp, 30);
        let d = sec.entry("chi2_zeros".into()).or_insert(Sec(Default::default()));
        d.0.insert("chi2".into(), chi2);
        d.0.insert("df".into(), df as f64);
        d.0.insert("p".into(), p);
        let (rr, n_r) = mean_adjacent_spacing_ratio(zeta);
        let d = sec.entry("rmean_zeros".into()).or_insert(Sec(Default::default()));
        d.0.insert("r".into(), rr);
        d.0.insert("n_r".into(), n_r as f64);
    }
    // 6. S2 / D3 — one MT19937(777) stream shared across S2→D3 (as gen_golden.jl)
    let pos = unfolded_positions(zeta);
    {
        let mut rng = Mt19937::new(777);
        for l in [5.0f64, 10.0, 20.0, 50.0, 100.0] {
            sec.entry("S2".into()).or_insert(Sec(Default::default())).0
                .insert(format!("L={}", shortest(l)), number_variance(&pos, l, 3000, &mut rng));
        }
        for l in [5.0f64, 10.0, 20.0, 50.0] {
            sec.entry("D3".into()).or_insert(Sec(Default::default())).0
                .insert(format!("L={}", shortest(l)), delta3_rigidity(&pos, l, 300, 300, &mut rng));
        }
    }
    // 7. K form factor
    {
        let tvals: Vec<f64> = match golden.get("grids").and_then(|g| g.get("tvals")) {
            Some(Json::Arr(a)) => a.iter().map(|v| v.num()).collect(),
            _ => vec![],
        };
        let k = compute_k_form_factor(zeta, &tvals);
        for (i, t) in tvals.iter().enumerate() {
            if [0.2f64, 0.5, 1.0, 2.0, 3.0].contains(t) {
                sec.entry("K_zeros".into()).or_insert(Sec(Default::default())).0
                    .insert(format!("t={}", shortest(*t)), k[i]);
            }
        }
        let mut acc = 0.0;
        let mut cnt = 0;
        for (i, t) in tvals.iter().enumerate() {
            if *t >= 0.3 {
                let e = hp_kgue_envelope(*t);
                acc += (k[i] - e) * (k[i] - e);
                cnt += 1;
            }
        }
        sec.entry("K_zeros".into()).or_insert(Sec(Default::default())).0
            .insert("rms_env".into(), (acc / cnt as f64).sqrt());
    }
    // 8. H1 zeta positive control
    {
        let omega: Vec<f64> = match golden.get("grids").and_then(|g| g.get("omega")) {
            Some(Json::Arr(a)) => a.iter().map(|v| v.num()).collect(),
            _ => vec![],
        };
        let zs = &zeta[..zeta.len().min(20000)];
        let n = zs.len();
        let w: Vec<f64> = (0..n)
            .map(|i| 0.5 * (1.0 - (2.0 * PI * i as f64 / (n - 1).max(1) as f64).cos()))
            .collect();
        let sw2: f64 = w.iter().map(|wi| wi * wi).sum();
        let mut p = vec![0.0; omega.len()];
        for (fi, om) in omega.iter().enumerate() {
            let mut re = 0.0;
            let mut im = 0.0;
            for i in 0..n {
                re += w[i] * (om * zs[i]).cos();
                im -= w[i] * (om * zs[i]).sin();
            }
            p[fi] = (re * re + im * im) / sw2;
        }
        let mut ps = p.clone();
        ps.sort_by(|a, b| a.partial_cmp(b).unwrap());
        let med = if ps.len() % 2 == 1 {
            ps[ps.len() / 2]
        } else {
            0.5 * (ps[ps.len() / 2 - 1] + ps[ps.len() / 2])
        };
        let d = sec.entry("h1_zeta".into()).or_insert(Sec(Default::default()));
        d.0.insert("median".into(), med);
        for pr in [2i64, 3, 5, 7, 11, 13] {
            let tgt = (pr as f64).ln();
            let best = omega
                .iter()
                .enumerate()
                .min_by(|(_, a), (_, b)| {
                    (**a - tgt).abs().partial_cmp(&(**b - tgt).abs()).unwrap()
                })
                .map(|(i, _)| i)
                .unwrap();
            d.0.insert(format!("snr_log{}", pr), p[best] / med);
        }
    }
    // 9. Hamiltonian goldens
    fn store_eigs(sec: &mut std::collections::BTreeMap<String, Sec>, name: &str, ev: &[f64]) {
        let n = ev.len();
        let d = sec.entry(name.into()).or_insert(Sec(Default::default()));
        d.0.insert("eig1".into(), ev[0]);
        d.0.insert("eig2".into(), ev[1]);
        d.0.insert("eig3".into(), ev[2]);
        d.0.insert("eigmid".into(), ev[n / 2 - 1]);
        // Julia: for k in 0:2 put!("eigend$(3-k)", ev[n-k]) → eigend3 = max
        d.0.insert("eigend1".into(), ev[n - 3]);
        d.0.insert("eigend2".into(), ev[n - 2]);
        d.0.insert("eigend3".into(), ev[n - 1]);
    }
    let e1 = jacobi_eigvals(&build_ab_cloud_hamiltonian(
        &AbCloudConfig::new(8, 8, vec![], 0.5, 1.0, "open", 0.0).with(96, "monumental")), 64);
    store_eigs(&mut sec, "ham_L8_open_a05_clean", &e1);
    let e2 = jacobi_eigvals(&build_ab_cloud_hamiltonian(
        &AbCloudConfig::new(8, 8, vec![Vortex{x:3.5,y:3.5,q:1.0},Vortex{x:6.5,y:6.5,q:-1.0}],
                            0.25, 1.0, "open", 0.0).with(96, "monumental")), 64);
    store_eigs(&mut sec, "ham_L8_open_a025_2vort", &e2);
    let e3 = jacobi_eigvals(&build_ab_cloud_hamiltonian(
        &AbCloudConfig::new(10, 10, vec![], 0.2, 1.0, "torus", 0.0).with(96, "monumental")), 100);
    store_eigs(&mut sec, "ham_L10_torus_a02_clean", &e3);
    // 9d Byers–Yang (:dirac)
    {
        let a = jacobi_eigvals(&build_ab_cloud_hamiltonian(
            &AbCloudConfig::new(8, 8, vec![Vortex{x:3.5,y:3.5,q:1.0},Vortex{x:6.5,y:6.5,q:-1.0}],
                                0.3, 1.0, "open", 0.0).with(96, "dirac")), 64);
        let b = jacobi_eigvals(&build_ab_cloud_hamiltonian(
            &AbCloudConfig::new(8, 8, vec![Vortex{x:3.5,y:3.5,q:2.0},Vortex{x:6.5,y:6.5,q:0.0}],
                                0.3, 1.0, "open", 0.0).with(96, "dirac")), 64);
        let dmax = a.iter().zip(&b).map(|(x, y)| (x - y).abs()).fold(0.0, f64::max);
        sec.entry("byers_yang".into()).or_insert(Sec(Default::default())).0
            .insert("L8_max_diff".into(), dmax);
    }
    // 9e Connes
    {
        let a = jacobi_eigvals(&build_ab_cloud_hamiltonian(
            &AbCloudConfig::new(12, 12, vec![], 0.5, 1.0, "open", 0.0)), 144);
        let b = jacobi_eigvals(&build_ab_cloud_hamiltonian(
            &AbCloudConfig::new(12, 12, vec![], 2.0, 1.0, "open", 0.0)), 144);
        let na = a.iter().map(|v| v * v).sum::<f64>().sqrt();
        let nb = a.iter().zip(&b).map(|(x, y)| (x - y) * (x - y)).sum::<f64>().sqrt();
        sec.entry("connes".into()).or_insert(Sec(Default::default())).0
            .insert("L12_a05_defect_W0".into(), nb / na.max(1e-30));
    }
    // 9f chiral
    {
        let h = build_ab_cloud_hamiltonian(
            &AbCloudConfig::new(12, 12, vec![], 0.5, 1.0, "open", 0.0).with(96, "monumental"));
        sec.entry("chiral".into()).or_insert(Sec(Default::default())).0
            .insert("L12_a05_defect".into(), chiral_symmetry_defect(&h, 12, 12));
    }
    // 9g Dirac flux
    {
        let h = build_ab_cloud_hamiltonian(
            &AbCloudConfig::new(8, 8, vec![Vortex{x:3.5,y:3.5,q:1.0}], 0.25, 1.0, "open", 0.0)
                .with(96, "dirac"));
        let mut maxdev = 0.0f64;
        for iy in 1..8usize {
            for ix in 1..8usize {
                let flux = plaquette_flux(&h, 8, 8, ix, iy, false);
                let tgt = 2.0 * PI * 0.25 + if (ix, iy) == (3, 3) { 2.0 * PI } else { 0.0 };
                maxdev = maxdev.max(flux_circdist(flux, tgt));
            }
        }
        sec.entry("dirac_flux".into()).or_insert(Sec(Default::default())).0
            .insert("L8_max_dev".into(), maxdev);
    }
    // 10. unfold / linreg / aicc / wald / spearman
    {
        let u = hp_unfold_local(&zeta[..2000], 0.05);
        let d = sec.entry("unfold".into()).or_insert(Sec(Default::default()));
        d.0.insert("u2".into(), u[1]);
        d.0.insert("u1000".into(), u[999]);
        d.0.insert("u2000".into(), u[1999]);
    }
    {
        let x: Vec<f64> = (1..=20).map(|i| i as f64).collect();
        let y: Vec<f64> = x.iter().map(|xi| 2.0 + 0.5 * xi + 0.1 * xi.sin()).collect();
        let r = linreg(&x, &y);
        let d = sec.entry("linreg".into()).or_insert(Sec(Default::default()));
        d.0.insert("a".into(), r.a);
        d.0.insert("b".into(), r.b);
        d.0.insert("R2".into(), r.r2);
    }
    {
        let n = 40; let rss = 10.0f64; let k = 3;
        let denom = n - k - 1;
        let aic = n as f64 * (rss.max(1e-300) / n as f64).ln() + 2.0 * k as f64;
        sec.entry("aicc".into()).or_insert(Sec(Default::default())).0
            .insert("n40_rss10_k3".into(),
                    if denom > 0 { aic + 2.0 * k as f64 * (k + 1) as f64 / denom as f64 } else { aic });
    }
    {
        let (k, n) = (7usize, 20usize);
        let p = k as f64 / n as f64;
        let h = 1.96 * (p * (1.0 - p) / n as f64).sqrt();
        let d = sec.entry("wald".into()).or_insert(Sec(Default::default()));
        d.0.insert("p".into(), p);
        d.0.insert("lo".into(), (p - h).clamp(0.0, 1.0));
        d.0.insert("hi".into(), (p + h).clamp(0.0, 1.0));
    }
    {
        let x = vec![1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0];
        let y = vec![1.1, 2.3, 2.9, 4.2, 5.1, 5.8, 7.2, 7.9];
        let rk = |v: &[f64]| -> Vec<f64> {
            let mut ord: Vec<usize> = (0..v.len()).collect();
            ord.sort_by(|a, b| v[*a].partial_cmp(&v[*b]).unwrap());
            let mut ranks = vec![0.0; v.len()];
            let mut i = 0;
            while i < ord.len() {
                let mut j = i;
                while j + 1 < ord.len() && v[ord[j + 1]] == v[ord[i]] {
                    j += 1;
                }
                let avg = (i + j) as f64 / 2.0 + 1.0;
                for kk in i..=j {
                    ranks[ord[kk]] = avg;
                }
                i = j + 1;
            }
            ranks
        };
        let (rx, ry) = (rk(&x), rk(&y));
        let mx = rx.iter().sum::<f64>() / rx.len() as f64;
        let my = ry.iter().sum::<f64>() / ry.len() as f64;
        let sxy: f64 = rx.iter().zip(&ry).map(|(a, b)| (a - mx) * (b - my)).sum();
        let sxx: f64 = rx.iter().map(|a| (a - mx) * (a - mx)).sum();
        let syy: f64 = ry.iter().map(|b| (b - my) * (b - my)).sum();
        sec.entry("spearman".into()).or_insert(Sec(Default::default())).0
            .insert("xy".into(), sxy / (sxx * syy).sqrt());
    }
    // 11
    {
        let sp2 = normalized_spacings(zeta);
        sec.entry("test11".into()).or_insert(Sec(Default::default())).0
            .insert("A2_full".into(), anderson_darling_stat(&mut rmt, &sp2));
    }
    sec
}

fn run_selftest(zeta: &[f64], golden_path: &str) -> bool {
    let text = fs::read_to_string(golden_path).unwrap_or_else(|_| {
        eprintln!("ERROR: golden file not found: {}", golden_path);
        exit(2);
    });
    let golden = JsonParser::new(&text).parse();
    let results = compute_all(zeta, &golden);
    let tol: std::collections::BTreeMap<&str, (f64, f64)> = std::collections::BTreeMap::from([
        ("lambert_w", (1e-9, 0.0)), ("gram_point", (1e-9, 0.0)), ("bN", (1e-9, 0.0)),
        ("spacings", (1e-9, 0.0)), ("gue2_cdf", (1e-7, 0.0)), ("goe_cdf", (1e-9, 0.0)),
        ("gue2_pdf", (1e-9, 0.0)), ("gamma_p", (1e-7, 0.0)), ("chi2_cdf", (1e-7, 0.0)),
        ("ks_pvalue", (1e-9, 0.0)), ("ks_zeros", (1e-6, 0.0)), ("cvm_zeros", (1e-6, 0.0)),
        ("ad_zeros", (1e-6, 0.0)), ("chi2_zeros", (1e-6, 0.0)), ("rmean_zeros", (1e-9, 0.0)),
        ("S2", (1e-7, 1e-12)), ("D3", (1e-7, 1e-12)), ("K_zeros", (1e-6, 0.0)),
        ("h1_zeta", (1e-6, 0.0)), ("ham_L8_open_a05_clean", (1e-7, 1e-8)),
        ("ham_L8_open_a025_2vort", (1e-7, 1e-8)), ("ham_L10_torus_a02_clean", (1e-7, 1e-8)),
        ("byers_yang", (1e-6, 1e-10)), ("connes", (1e-5, 1e-8)), ("chiral", (1e-5, 1e-9)),
        ("dirac_flux", (1e-6, 1e-10)), ("unfold", (1e-8, 0.0)), ("linreg", (1e-8, 0.0)),
        ("aicc", (1e-8, 0.0)), ("wald", (1e-9, 0.0)), ("spearman", (1e-8, 0.0)),
        ("test11", (1e-6, 0.0)),
    ]);
    println!("==============================================================================");
    println!("ABCLOUD RUST PORT — GOLDEN SELFTEST");
    println!("==============================================================================");
    let (mut n_ok, mut n_all) = (0, 0);
    if let Json::Obj(sections) = &golden {
        for (section, gsec) in sections {
            if section == "meta" || section == "grids" {
                continue;
            }
            let (rtol, atol) = tol.get(section.as_str()).copied().unwrap_or((1e-6, 0.0));
            if let Json::Obj(keys) = gsec {
                for (key, gv) in keys {
                    n_all += 1;
                    let g = gv.num();
                    let cv = results
                        .get(section)
                        .and_then(|s| s.0.get(key))
                        .copied()
                        .unwrap_or(f64::NAN);
                    let (err, ok) = if g == 0.0 && cv == 0.0 {
                        (0.0, true)
                    } else if g == 0.0 {
                        (cv.abs(), cv.abs() <= atol + rtol)
                    } else {
                        let e = (cv - g).abs() / g.abs();
                        (e, e <= rtol || (cv - g).abs() <= atol)
                    };
                    if ok {
                        n_ok += 1;
                    }
                    println!(" [{}] {:<28} {:<18} g={:<22.17} p={:<22.17} rel={:.2e}",
                             if ok { "PASS" } else { "FAIL" }, section, key, g, cv, err);
                }
            }
        }
    }
    println!("------------------------------------------------------------------------------");
    println!(" RESULT: {}/{} checks passed", n_ok, n_all);
    println!("==============================================================================");
    let ok = n_ok == n_all;
    println!("SELFTEST: {}", if ok {
        "PASS — Rust kernel matches the Julia golden references."
    } else {
        "FAIL"
    });
    ok
}

// [PART5]
// ─────────────────────────────────────────────────────────────────────────────
// Suite (portable subset — same 25 tests) + CLI
// ─────────────────────────────────────────────────────────────────────────────
fn run_suite(zeta: &[f64]) {
    println!("==============================================================================");
    println!("ABCLOUD SUITE (portable subset, Rust)");
    println!("==============================================================================");
    let mut rmt = RmtTable::new();
    let sp = normalized_spacings(zeta);
    let ladder: Vec<i64> = vec![100, 500, 1000, 5000, 10000, 50000];
    let (mut n_pass, mut n_fail, mut n_warn, mut n_info) = (0, 0, 0, 0);

    macro_rules! verdict {
        ($v:expr, $tid:expr, $title:expr, $lines:expr) => {{
            let v = $v;
            match v {
                "PASS" => n_pass += 1,
                "FAIL" => n_fail += 1,
                "WARN" => n_warn += 1,
                _ => n_info += 1,
            }
            let mark = match v { "PASS" => "[PASS]", "FAIL" => "[FAIL]", "WARN" => "[WARN]", _ => "[INFO]" };
            println!("{} TEST {:>2} — {}", mark, $tid, $title);
            for l in &$lines {
                println!("{}", l);
            }
        }};
    }

    // 1
    {
        let vals: Vec<f64> = ladder.iter().map(|n| compute_bn(zeta, *n, 0)).collect();
        let ok = vals.last().unwrap().is_finite() && vals.last() < vals.first();
        let ladder_str: Vec<String> = vals.iter().map(|v| format!("{:.4}", v)).collect();
        verdict!(if ok { "PASS" } else { "FAIL" }, 1, "b(N) convergence table",
                 vec![format!("  ladder: {}", ladder_str.join("  ")),
                      format!("  b(50000) = {:.6} (audit anchor 1.2126)", vals[5])]);
    }
    // 2
    {
        let vals: Vec<f64> = ladder.iter().map(|n| compute_bn(zeta, *n, 0)).collect();
        let mono = vals.windows(2).all(|w| w[1] <= w[0] + 1e-9);
        let ladder_str: Vec<String> = vals.iter().map(|v| format!("{:.4}", v)).collect();
        verdict!(if mono { "PASS" } else { "FAIL" }, 2, "b(N) monotonicity",
                 vec![format!("  ladder: {}", ladder_str.join(" "))]);
    }
    // 3
    {
        let vals: Vec<f64> = ladder.iter().map(|n| compute_bn(zeta, *n, 0)).collect();
        let lx: Vec<f64> = ladder.iter().map(|n| (*n as f64).ln()).collect();
        let ly: Vec<f64> = vals.iter().map(|v| v.ln()).collect();
        let r = linreg(&lx, &ly);
        let ok = (-1.5..-0.05).contains(&r.b) && r.r2 > 0.9;
        verdict!(if ok { "PASS" } else { "FAIL" }, 3, "b(N) convergence rate (power law)",
                 vec![format!("  slope={:+.4}  R2={:.6}  (asymptotic -0.5, 1/log T correction)", r.b, r.r2)]);
    }
    // 4,5
    {
        let (d, p) = ks_test(&mut rmt, &sp);
        verdict!(if d < 0.10 { "PASS" } else { "FAIL" }, 4, "GUE KS test (full range)",
                 vec![format!("  KS D={:.6}  p={:.3e}  n={}  (effect-size gate D<0.10)", d, p, sp.len())]);
    }
    {
        let sp2 = normalized_spacings(&zeta[zeta.len() / 2..]);
        let (d, p) = ks_test(&mut rmt, &sp2);
        verdict!(if d < 0.10 { "PASS" } else { "FAIL" }, 5, "GUE KS test (high-T half)",
                 vec![format!("  high-T half: D={:.6}  p={:.3e}  n={}", d, p, sp2.len())]);
    }
    // 6
    {
        let (chi2, df, p) = chi2_gue_test(&mut rmt, &sp, 30);
        verdict!("INFO", 6, "spacing chi2 histogram",
                 vec![format!("  chi2={:.2}  df={}  p={:.3e}  (low p = finite-data GUE miss)", chi2, df, p)]);
    }
    // 7
    {
        let tail: Vec<i64> = vec![5000, 10000, 50000];
        let vals: Vec<f64> = tail.iter().map(|n| compute_bn(zeta, *n, 0)).collect();
        let lx: Vec<f64> = tail.iter().map(|n| (*n as f64).ln()).collect();
        let ly: Vec<f64> = vals.iter().map(|v| v.ln()).collect();
        let r = linreg(&lx, &ly);
        let ok = (-0.9..-0.05).contains(&r.b) && r.r2 > 0.9;
        verdict!(if ok { "PASS" } else { "FAIL" }, 7, "decay slope (large-T)",
                 vec![format!("  tail slope={:+.4}  R2={:.6}", r.b, r.r2)]);
    }
    // 8
    {
        let vals: Vec<f64> = ladder.iter().map(|n| compute_bn(zeta, *n, 0)).collect();
        let lx: Vec<f64> = ladder.iter().map(|n| (*n as f64).ln()).collect();
        let ly: Vec<f64> = vals.iter().map(|v| v.ln()).collect();
        let r = linreg(&lx, &ly);
        let max_rel = r
            .res
            .iter()
            .zip(&ly)
            .map(|(e, y)| e.abs() / y.abs().max(1e-12))
            .fold(0.0, f64::max);
        verdict!(if max_rel < 0.2 { "PASS" } else { "WARN" }, 8, "residual analysis of fit",
                 vec![format!("  max |relative residual| = {:.4}", max_rel)]);
    }
    // 9
    {
        let base: Vec<f64> = ladder.iter().map(|n| compute_bn(zeta, *n, 0)).collect();
        let mut rng = Mt19937::new(777);
        let (mut lo, mut hi) = (1e9f64, -1e9f64);
        for _ in 0..200 {
            let bs: Vec<f64> = base
                .iter()
                .map(|v| (v * (1.0 + 0.02 * (rng.random() - 0.5) * 2.0).sqrt()).ln())
                .collect();
            let lx: Vec<f64> = ladder.iter().map(|n| (*n as f64).ln()).collect();
            let r = linreg(&lx, &bs);
            lo = lo.min(r.b);
            hi = hi.max(r.b);
        }
        let ok = lo > -1.5 && hi < -0.1;
        verdict!(if ok { "PASS" } else { "WARN" }, 9, "bootstrap CI for slope",
                 vec![format!("  bootstrap slope CI [{:+.4}, {:+.4}] (200 resamples, seed 777)", lo, hi)]);
    }
    // 10
    {
        let half = zeta.len() / 2;
        let lad: Vec<i64> = vec![100, 500, 1000, 5000];
        let v1: Vec<f64> = lad.iter().map(|n| compute_bn(zeta, *n, 0)).collect();
        let v2: Vec<f64> = lad.iter().map(|n| compute_bn(&zeta[half..], *n, half as i64)).collect();
        let lx: Vec<f64> = lad.iter().map(|n| (*n as f64).ln()).collect();
        let r1 = linreg(&lx, &v1.iter().map(|v| v.ln()).collect::<Vec<_>>());
        let r2 = linreg(&lx, &v2.iter().map(|v| v.ln()).collect::<Vec<_>>());
        let mono = v1.windows(2).all(|w| w[1] <= w[0] + 1e-9)
            && v2.windows(2).all(|w| w[1] <= w[0] + 1e-9);
        let ok = mono && r1.r2 > 0.85 && r2.r2 > 0.85;
        verdict!(if ok { "PASS" } else { "FAIL" }, 10, "cross-validation stability",
                 vec![format!("  slopes {:+.3}/{:+.3}, R2 {:.3}/{:.3}; both monotone (height gap = 1/log T offset)",
                              r1.b, r2.b, r1.r2, r2.r2)]);
    }
    // 11
    {
        let a2 = anderson_darling_stat(&mut rmt, &sp);
        let mut rng = Mt19937::new(777);
        let mut buf = vec![0.0; sp.len()];
        let mut count = 0;
        for _ in 0..200 {
            rmt.sample(&mut rng, &mut buf);
            if anderson_darling_stat(&mut rmt, &buf) >= a2 {
                count += 1;
            }
        }
        verdict!("INFO", 11, "Anderson-Darling (honest)",
                 vec![format!("  A2 = {:.4}  law-exact MC p = {:.4} (200 draws, seed 777)", a2, (count + 1) as f64 / 201.0)]);
    }
    // 12
    {
        let n_mat = 200usize;
        let mut rng = Mt19937::new(4242);
        let mut h = vec![Cx::zero(); n_mat * n_mat];
        let gauss = |rng: &mut Mt19937| -> f64 {
            let u1 = rng.random().max(1e-300);
            (-2.0 * u1.ln()).sqrt() * (2.0 * PI * rng.random()).cos()
        };
        for r in 0..n_mat {
            h[r * n_mat + r] = Cx::new(gauss(&mut rng), 0.0);
            for c in (r + 1)..n_mat {
                let v = Cx::new(gauss(&mut rng) / 2.0f64.sqrt(), gauss(&mut rng) / 2.0f64.sqrt());
                h[r * n_mat + c] = v;
                h[c * n_mat + r] = v.conj();
            }
        }
        for r in 0..n_mat {
            for c in r..n_mat {
                let m = h[r * n_mat + c].scale(0.5);
                h[r * n_mat + c] = m;
                h[c * n_mat + r] = m.conj();
            }
        }
        let ev = jacobi_eigvals(&h, n_mat);
        let band = &ev[n_mat / 10..9 * n_mat / 10];
        let gp = unit_spacings(band);
        let d = ks2(&sp, &gp);
        verdict!(if d < 0.10 { "PASS" } else { "FAIL" }, 12, "two-sample KS vs GUE matrix",
                 vec![format!("  two-sample KS (zeta n={} vs GUE n={}): D={:.6}", sp.len(), gp.len(), d)]);
    }
    // 13,14
    {
        let pos = unfolded_positions(zeta);
        let mut rng = Mt19937::new(777);
        let mut ok = true;
        let mut lines = Vec::new();
        for l in [5.0f64, 10.0, 20.0, 50.0] {
            let s2 = number_variance(&pos, l, 3000, &mut rng);
            ok = ok && s2 < l;
            lines.push(format!("  S2(L={:5.1}) = {:.4}   [Poisson {:.1}]", l, s2, l));
        }
        lines.push("  gate: S2(L) << L (GUE rigidity)".into());
        verdict!(if ok { "PASS" } else { "FAIL" }, 13, "number variance S2(L)", lines);
    }
    {
        let pos = unfolded_positions(zeta);
        let mut rng = Mt19937::new(777);
        let mut ok = true;
        let mut lines = Vec::new();
        for l in [5.0f64, 10.0, 20.0, 50.0] {
            let d3 = delta3_rigidity(&pos, l, 300, 300, &mut rng);
            ok = ok && d3 < l / 15.0;
            lines.push(format!("  D3(L={:5.1}) = {:.4}   [Poisson {:.4}]", l, d3, l / 15.0));
        }
        verdict!(if ok { "PASS" } else { "FAIL" }, 14, "spectral rigidity D3(L)", lines);
    }
    // 15,16
    {
        let h = build_ab_cloud_hamiltonian(
            &AbCloudConfig::new(16, 16, vec![Vortex{x:4.5,y:4.5,q:1.0}], 0.5, 1.0, "open", 0.0));
        let herm = verify_hermitian(&h, 256);
        let tau = time_reversal_asymmetry(&h);
        let ev = jacobi_eigvals(&h, 256);
        let band = central_band_eigs(&ev, 0.6);
        let (r, n_r) = mean_adjacent_spacing_ratio(&band);
        verdict!(if herm && tau > 1e-12 { "PASS" } else { "FAIL" }, 15, "AB-cloud construction",
                 vec![format!("  hermitian={}  tau_TRB={:.3e}  <r>(central 60%)={:.4} (n_r={})", herm, tau, r, n_r)]);
    }
    {
        let h = build_ab_cloud_hamiltonian(&AbCloudConfig::new(
            24, 24, vec![Vortex{x:6.5,y:6.5,q:1.0},Vortex{x:17.5,y:17.5,q:-1.0}], 0.5, 1.0, "open", 0.0));
        let ev = jacobi_eigvals(&h, 576);
        let band = central_band_eigs(&ev, 0.6);
        let (r, n_r) = mean_adjacent_spacing_ratio(&band);
        let ok = (r - 0.5992).abs() < 0.06;
        verdict!(if ok { "PASS" } else { "WARN" }, 16, "AB-cloud GUE classification",
                 vec![format!("  <r> = {:.4} vs GUE 0.5992 +/- 0.06 (n_r={}; L=24 finite-size band)", r, n_r)]);
    }
    // 17,18
    {
        let ea = jacobi_eigvals(&build_ab_cloud_hamiltonian(
            &AbCloudConfig::new(12, 12, vec![], 0.5, 1.0, "open", 0.0)), 144);
        let eb = jacobi_eigvals(&build_ab_cloud_hamiltonian(
            &AbCloudConfig::new(12, 12, vec![], 2.0, 1.0, "open", 0.0)), 144);
        let na = ea.iter().map(|v| v * v).sum::<f64>().sqrt();
        let nb = ea.iter().zip(&eb).map(|(x, y)| (x - y) * (x - y)).sum::<f64>().sqrt();
        verdict!("INFO", 17, "Connes self-duality",
                 vec![format!("  alpha<->1/alpha relative L2 defect (open 12x12, W=0) = {:.6}", nb / na),
                      "  finite open lattice: duality is boundary-spoiled (documented)".into()]);
    }
    {
        let h = build_ab_cloud_hamiltonian(
            &AbCloudConfig::new(12, 12, vec![], 0.5, 1.0, "open", 0.0).with(96, "monumental"));
        let hw = build_ab_cloud_hamiltonian(
            &AbCloudConfig::new(12, 12, vec![], 0.5, 1.0, "open", 4.0).with(96, "monumental"));
        let d0 = chiral_symmetry_defect(&h, 12, 12);
        let dw = chiral_symmetry_defect(&hw, 12, 12);
        verdict!(if d0 < 1e-10 { "PASS" } else { "FAIL" }, 18, "chiral AIII at alpha=1/2",
                 vec![format!("  defect(W=0) = {:.3e} (gate <1e-10)   defect(W=4, breaker) = {:.4}", d0, dw)]);
    }
    // 24,25,26
    {
        let h = build_ab_cloud_hamiltonian(
            &AbCloudConfig::new(8, 8, vec![Vortex{x:3.5,y:3.5,q:1.0}], 0.25, 1.0, "open", 0.0).with(96, "dirac"));
        let mut maxdev = 0.0f64;
        for iy in 1..8usize {
            for ix in 1..8usize {
                let flux = plaquette_flux(&h, 8, 8, ix, iy, false);
                let tgt = 2.0 * PI * 0.25 + if (ix, iy) == (3, 3) { 2.0 * PI } else { 0.0 };
                maxdev = maxdev.max(flux_circdist(flux, tgt));
            }
        }
        verdict!(if maxdev < 1e-9 { "PASS" } else { "FAIL" }, 24, "Dirac-string flux",
                 vec![format!("  max circular deviation from 2pa + 2q = {:.3e} (:dirac)", maxdev)]);
    }
    {
        let e1 = jacobi_eigvals(&build_ab_cloud_hamiltonian(&AbCloudConfig::new(
            16, 16, vec![Vortex{x:4.5,y:4.5,q:1.0},Vortex{x:11.5,y:11.5,q:-1.0}], 0.3, 1.0, "open", 0.0).with(96, "dirac")), 256);
        let e2 = jacobi_eigvals(&build_ab_cloud_hamiltonian(&AbCloudConfig::new(
            16, 16, vec![Vortex{x:4.5,y:4.5,q:2.0},Vortex{x:11.5,y:11.5,q:0.0}], 0.3, 1.0, "open", 0.0).with(96, "dirac")), 256);
        let e3 = jacobi_eigvals(&build_ab_cloud_hamiltonian(&AbCloudConfig::new(
            16, 16, vec![Vortex{x:4.5,y:4.5,q:0.3},Vortex{x:11.5,y:11.5,q:-0.3}], 0.3, 1.0, "open", 0.0).with(96, "dirac")), 256);
        let d_int = e1.iter().zip(&e2).map(|(a, b)| (a - b).abs()).fold(0.0, f64::max);
        let d_frac = e1.iter().zip(&e3).map(|(a, b)| (a - b).abs()).fold(0.0, f64::max);
        let ok = d_int < 1e-9 && d_frac > 1e-4;
        verdict!(if ok { "PASS" } else { "FAIL" }, 25, "Byers-Yang theorem",
                 vec![format!("  integer q->q+1: {:.3e}   fractional q=0.3 control: {:.3e} (must differ)", d_int, d_frac)]);
    }
    {
        let h = build_ab_cloud_hamiltonian(&AbCloudConfig::new(12, 12, vec![], 0.25, 1.0, "torus", 0.0));
        let mut maxdev = 0.0f64;
        for iy in 1..=12usize {
            for ix in 1..=12usize {
                maxdev = maxdev.max(flux_circdist(plaquette_flux(&h, 12, 12, ix, iy, true), 2.0 * PI * 0.25));
            }
        }
        verdict!(if maxdev < 1e-9 { "PASS" } else { "FAIL" }, 26, "PBC torus flux",
                 vec![format!("  torus 12x12 alpha=0.25: max flux deviation = {:.3e}", maxdev)]);
    }
    // 34
    {
        let h = build_ab_cloud_hamiltonian(&AbCloudConfig::new(
            28, 28, vec![Vortex{x:7.5,y:7.5,q:1.0},Vortex{x:20.5,y:20.5,q:-1.0}], 0.5, 1.0, "open", 0.0).with(96, "monumental"));
        let ev = jacobi_eigvals(&h, 784);
        let band = central_band_eigs(&ev, 0.6);
        let absp = unit_spacings(&hp_unfold_local(&band, 0.05));
        let zsp = unit_spacings(&sp);
        let d = ks2(&absp, &zsp);
        verdict!(if d < 0.10 { "PASS" } else { "WARN" }, 34, "DIRECT AB-cloud vs zeta",
                 vec![format!("  DIRECT AB-cloud (L=28, n={}) vs zeta: KS D={:.6}", absp.len(), d)]);
    }
    // 35
    {
        let tvals: Vec<f64> = (1..=30).map(|i| 0.1 * i as f64).collect();
        let k = compute_k_form_factor(zeta, &tvals);
        let mut acc = 0.0;
        let mut cnt = 0;
        for (i, t) in tvals.iter().enumerate() {
            if *t >= 0.3 {
                let e = hp_kgue_envelope(*t);
                acc += (k[i] - e) * (k[i] - e);
                cnt += 1;
            }
        }
        let rms = (acc / cnt as f64).sqrt();
        verdict!(if rms < 1.0 { "PASS" } else { "FAIL" }, 35, "form factor K(t)",
                 vec![format!("  RMS(K - K_box) over t>=0.3 = {:.4}  (gate <1.0)", rms)]);
    }
    // 36
    {
        let h = build_ab_cloud_hamiltonian(
            &AbCloudConfig::new(16, 16, vec![Vortex{x:4.5,y:4.5,q:1.0}], 0.5, 1.0, "open", 0.0));
        let ev = jacobi_eigvals(&h, 256);
        let band = central_band_eigs(&ev, 0.6);
        let (r0, _) = mean_adjacent_spacing_ratio(&band);
        let (lo, span) = (band[0], band[band.len() - 1] - band[0]);
        let nlev = 4096usize;
        let quant: Vec<f64> = band
            .iter()
            .map(|e| lo + ((e - lo) / span * (nlev - 1) as f64).round() / (nlev - 1) as f64 * span)
            .collect();
        let (rq, _) = mean_adjacent_spacing_ratio(&quant);
        let dr = (rq - r0).abs();
        let mut rng = Mt19937::new(12345);
        let mut counts = [0i64; 256];
        let nb = 200000;
        for _ in 0..nb {
            counts[(rng.next_u32() & 0xFF) as usize] += 1;
        }
        let exp = nb as f64 / 256.0;
        let mut ent = 0.0;
        let mut chi2z = 0.0;
        for c in counts {
            if c > 0 {
                let p = c as f64 / nb as f64;
                ent -= p * p.log2();
            }
            chi2z += (c as f64 - exp).powi(2) / exp;
        }
        let z = (chi2z - 255.0) / ((2.0f64) * 255.0).sqrt();
        let ok = dr < 0.02 && (ent - 8.0).abs() < 0.01 && z.abs() < 3.0;
        verdict!(if ok { "PASS" } else { "FAIL" }, 36, "byte-level robustness",
                 vec![format!("  |d<r>| under {}-level quantization = {:.5} (gate 0.02)", nlev, dr),
                      format!("  RNG entropy = {:.6} bits/byte, chi2 z = {:+.2} (|z|<3)", ent, z)]);
    }
    // 37
    {
        let e1 = (lgamma_lanczos(0.5).exp() - PI.sqrt()).abs();
        let e2 = (lgamma_lanczos(1.5).exp() - PI.sqrt() / 2.0).abs();
        let (n, smax) = (2000i64, 10.0f64);
        let h = smax / n as f64;
        let (mut integ, mut m2) = (0.0, 0.0);
        for i in 0..=n {
            let wgt = if i == 0 || i == n { 1.0 } else if i % 2 == 1 { 4.0 } else { 2.0 };
            let p = gue2_surmise_pdf(i as f64 * h);
            integ += wgt * p;
            m2 += wgt * p * (i as f64 * h) * (i as f64 * h);
        }
        integ *= h / 3.0;
        m2 *= h / 3.0;
        let ok = e1 < 1e-9 && e2 < 1e-9 && (integ - 1.0).abs() < 1e-4 && (m2 - 3.0 * PI / 8.0).abs() < 5e-3;
        verdict!(if ok { "PASS" } else { "FAIL" }, 37, "(1/2)! via Gamma + GUE normalization",
                 vec![format!("  G(1/2)-sqrt(pi) = {:.2e}   G(3/2)-sqrt(pi)/2 = {:.2e}   int p2 = {:.6}   <s2> = {:.6}",
                              e1, e2, integ, m2)]);
    }

    let not_ported: [(i64, &str); 14] = [
        (19, "four-pass Dirac-cone audit"), (20, "TKNN Chern number"),
        (21, "spinorial phase"), (22, "AB phase identity"), (23, "fractal factor"),
        (27, "binary chiral + zeta-dictionary"), (28, "f_GUE merit"), (29, "DOS dip"),
        (30, "v_F scaling ladder"), (31, "Hatano-Nelson skin"),
        (32, "multi-realization <r> bootstrap (dSFMT parity)"),
        (33, "L-scaling <r> (dSFMT parity)"), (38, "Curie point three-pass"),
        (39, "Test-34G geometry sweep"),
    ];
    println!("------------------------------------------------------------------------------");
    for (tid, note) in not_ported {
        println!("[SKIP] TEST {:>2} — not ported: {}", tid, note);
    }
    println!("------------------------------------------------------------------------------");
    println!("SUITE RESULT: {} PASS, {} FAIL, {} WARN, {} INFO", n_pass, n_fail, n_warn, n_info);
    println!("==============================================================================");
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        eprintln!("usage: abcloud <selftest|zeros|suite|bN|gram|test11|hp|sweep> [options]");
        exit(2);
    }
    let cmd = args[1].clone();
    let mut data = String::new();
    let mut golden = String::new();
    let mut ns: Vec<i64> = Vec::new();
    let mut offset = 0i64;
    let mut mc = 200usize;
    let mut seed = 777u32;
    let mut i = 2;
    while i < args.len() {
        match args[i].as_str() {
            "--data" => {
                i += 1;
                data = args.get(i).cloned().unwrap_or_default();
            }
            "--golden" => {
                i += 1;
                golden = args.get(i).cloned().unwrap_or_default();
            }
            "--N" | "--n" => {
                i += 1;
                while i < args.len() && !args[i].starts_with('-') {
                    ns.push(args[i].parse().unwrap_or(0));
                    i += 1;
                }
                i -= 1;
            }
            "--offset" => {
                i += 1;
                offset = args.get(i).and_then(|v| v.parse().ok()).unwrap_or(0);
            }
            "--mc" => {
                i += 1;
                mc = args.get(i).and_then(|v| v.parse().ok()).unwrap_or(200);
            }
            "--seed" => {
                i += 1;
                seed = args.get(i).and_then(|v| v.parse().ok()).unwrap_or(777);
            }
            _ => {}
        }
        i += 1;
    }
    // resolve exe-relative default paths (ports/rust/target/release → repo root)
    let exe_dir = env::current_exe()
        .ok()
        .and_then(|p| p.parent().map(|d| d.to_path_buf()))
        .unwrap_or_default();
    // target/release → ports/rust/target/release: up 3 = ports/, up 4 = meridian
    // exe at ports/rust/target/release → up 3 = ports/, up 4 = meridian/
    let zeros_path = if data.is_empty() {
        exe_dir.join("../../../../zeros50k.txt")
    } else {
        std::path::PathBuf::from(&data)
    };
    let golden_path = if golden.is_empty() {
        exe_dir.join("../../../golden/abcloud_golden.json")
    } else {
        std::path::PathBuf::from(&golden)
    };
    let zeros_path = zeros_path.to_string_lossy().to_string();
    let golden_path = golden_path.to_string_lossy().to_string();

    match cmd.as_str() {
        "selftest" => {
            let z = load_zeros(&zeros_path);
            if !run_selftest(&z, &golden_path) {
                exit(1);
            }
        }
        "suite" => {
            let z = load_zeros(&zeros_path);
            run_suite(&z);
        }
        "bN" => {
            let z = load_zeros(&zeros_path);
            if ns.is_empty() {
                ns = vec![100, 1000, 10000];
            }
            for n in ns {
                println!("b(N={:6}, offset={}) = {:.10}", n, offset, compute_bn(&z, n, offset));
            }
        }
        "gram" => {
            if ns.is_empty() {
                ns = vec![1, 10, 100];
            }
            for n in ns {
                println!("g_{} = {:.10}", n, gram_point(n));
            }
        }
        "test11" => {
            let z = load_zeros(&zeros_path);
            let sp = normalized_spacings(&z);
            let mut rmt = RmtTable::new();
            let a2 = anderson_darling_stat(&mut rmt, &sp);
            println!("Test 11 (honest): exact A2 on n={} spacings: {:.6}", sp.len(), a2);
            if mc > 0 {
                let mut rng = Mt19937::new(seed);
                let mut buf = vec![0.0; sp.len()];
                let mut count = 0;
                for _ in 0..mc {
                    rmt.sample(&mut rng, &mut buf);
                    if anderson_darling_stat(&mut rmt, &buf) >= a2 {
                        count += 1;
                    }
                }
                println!("MC null ({} draws): p = {:.6}  ({}/{} >= A2)", mc,
                         (count + 1) as f64 / (mc + 1) as f64, count, mc);
            }
        }
        "hp" => {
            let z = load_zeros(&zeros_path);
            let n = z.len();
            let om: Vec<f64> = (0..726).map(|k| 0.3 + 0.004 * k as f64).collect();
            let w: Vec<f64> = (0..n)
                .map(|i| 0.5 * (1.0 - (2.0 * PI * i as f64 / (n - 1).max(1) as f64).cos()))
                .collect();
            let sw2: f64 = w.iter().map(|x| x * x).sum();
            let mut p = vec![0.0; om.len()];
            for (fi, omv) in om.iter().enumerate() {
                let (mut re, mut im) = (0.0, 0.0);
                for i in 0..n {
                    re += w[i] * (omv * z[i]).cos();
                    im -= w[i] * (omv * z[i]).sin();
                }
                p[fi] = (re * re + im * im) / sw2;
            }
            let mut ps = p.clone();
            ps.sort_by(|a, b| a.partial_cmp(b).unwrap());
            let med = 0.5 * (ps[ps.len() / 2 - 1] + ps[ps.len() / 2]);
            println!("H1 primary detector on {} positions:", n);
            let mut hits = 0;
            for pr in [2i64, 3, 5, 7, 11, 13] {
                let tgt = (pr as f64).ln();
                let best = om.iter().enumerate()
                    .min_by(|(_, a), (_, b)| (**a - tgt).abs().partial_cmp(&(**b - tgt).abs()).unwrap())
                    .map(|(i, _)| i).unwrap();
                let snr = p[best] / med;
                if snr >= 10.0 {
                    hits += 1;
                }
                println!("  SNR(log {:2}) = {:.6e}  [{}]", pr, snr, if snr >= 10.0 { "PEAK" } else { "-" });
            }
            println!("  verdict: {}/6 prime harmonics above SNR 10", hits);
        }
        "sweep" => {
            let z = load_zeros(&zeros_path);
            if ns.is_empty() {
                ns = vec![100, 500, 1000, 5000, 10000, 50000];
            }
            println!("  N        b(N)");
            for n in ns {
                println!("{:6}  {:.8}", n, compute_bn(&z, n, 0));
            }
        }
        "zeros" => {
            let z = load_zeros(&zeros_path);
            let sp = normalized_spacings(&z);
            let mut rmt = RmtTable::new();
            let mean = sp.iter().sum::<f64>() / sp.len() as f64;
            let var = sp.iter().map(|s| (s - mean) * (s - mean)).sum::<f64>() / (sp.len() - 1) as f64;
            let (d, p) = ks_test(&mut rmt, &sp);
            println!("zeros: n={}  g1={:.6}  gN={:.6}", z.len(), z[0], z[z.len() - 1]);
            println!("spacings: n={}  mean={:.6}  var={:.6}", sp.len(), mean, var);
            println!("KS  : D={:.6}  p={:.6e}", d, p);
            println!("CvM : W2={:.6}", cvm_test(&mut rmt, &sp));
            println!("A2  : {:.6}", anderson_darling_stat(&mut rmt, &sp));
            let (chi2, df, pchi) = chi2_gue_test(&mut rmt, &sp, 30);
            println!("chi2: {:.4}  df={}  p={:.6e}", chi2, df, pchi);
            let (r, n_r) = mean_adjacent_spacing_ratio(&z);
            println!("<r> : {:.6}  (n_r={})", r, n_r);
            let pos = unfolded_positions(&z);
            let mut rng = Mt19937::new(777);
            for l in [5.0f64, 10.0, 20.0, 50.0, 100.0] {
                println!("S2(L={:6.1}) = {:.6}", l, number_variance(&pos, l, 3000, &mut rng));
            }
            for l in [5.0f64, 10.0, 20.0, 50.0] {
                println!("D3(L={:6.1}) = {:.6}", l, delta3_rigidity(&pos, l, 300, 300, &mut rng));
            }
        }
        _ => {
            eprintln!("unknown command: {}", cmd);
            exit(2);
        }
    }
}
