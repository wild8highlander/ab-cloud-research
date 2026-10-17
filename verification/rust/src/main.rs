//! =============================================================================
//! AB-CLOUD VERIFICATION SUITE — bilingual (EN/RU), canonical kernel v3.0
//! =============================================================================
//! Objections against the AB-Cloud claims, verified against the frozen golden
//! anchors (CANON_SPEC.md; canon: meridian-spectral-observatory, selftest
//! 199/199). verify_en.rs / verify_ru.rs are thin rendering layers.
//! =============================================================================

#[allow(dead_code)]
mod verify_en;
#[allow(dead_code)]
mod verify_ru;

use std::env;
use std::f64::consts::PI;

// ---------------------------------------------------------------------------
// CLI
// ---------------------------------------------------------------------------
struct Args {
    n_zeros: usize,
    source: String,
    objection: u8, // 0 = all
    lang: u8,      // 1 = en, 2 = ru
    data_dir: String,
    selfcheck: bool,
}

fn parse_args() -> Args {
    let mut a = Args {
        n_zeros: 50_000,
        source: "auto".to_string(),
        objection: 0,
        lang: 1,
        data_dir: "../data".to_string(),
        selfcheck: true,
    };
    let cli: Vec<String> = env::args().collect();
    let mut i = 1;
    while i < cli.len() {
        match cli[i].as_str() {
            "--zeros" if i + 1 < cli.len() => { i += 1; a.n_zeros = cli[i].parse().unwrap_or(50_000); }
            "--source" if i + 1 < cli.len() => { i += 1; a.source = cli[i].clone(); }
            "--objection" if i + 1 < cli.len() => {
                i += 1;
                a.objection = match cli[i].as_str() { "all" => 0, s => s.parse().unwrap_or(0) };
            }
            "--lang" if i + 1 < cli.len() => { i += 1; a.lang = if cli[i] == "ru" { 2 } else { 1 }; }
            "--data-dir" if i + 1 < cli.len() => { i += 1; a.data_dir = cli[i].clone(); }
            "--no-selfcheck" => { a.selfcheck = false; }
            _ => {}
        }
        i += 1;
    }
    a
}

// ---------------------------------------------------------------------------
// Data sources (CANON_SPEC §9)
// ---------------------------------------------------------------------------
const SOURCES: &[(&str, &str, usize)] = &[
    ("50k", "zeta_zeros_50000.txt", 13_661),
    ("50k_full", "zeta_zeros_50000_embedded.txt", 50_000),
    ("500k", "zeta_zeros_500k_odlyzko.txt", 500_000),
    ("2M", "zeta_zeros_2M_odlyzko.txt", 2_001_052),
    ("highT", "zeta_zeros_highT_blocks.txt", 30_000),
    ("csv", "zeta_zeros_50000.csv", 13_661),
    ("zeros6", "zeros6.txt", 2_001_052),
];

fn resolve_source(count: usize, source: &str) -> Result<(&'static str, &'static str), String> {
    if source == "2M_gz" {
        return Err("source '2M_gz' is not supported in the Rust port; use '2M'".into());
    }
    if source != "auto" {
        for (n, f, _) in SOURCES {
            if *n == source {
                return Ok((n, f));
            }
        }
        return Err(format!("unknown source: {}", source));
    }
    let mut best: Option<(&str, &str, usize)> = None;
    for s in SOURCES {
        if s.2 >= count && best.map_or(true, |b| s.2 < b.2) {
            best = Some(*s);
        }
    }
    best.map(|b| (b.0, b.1)).ok_or_else(|| format!("no data source available for {} zeros", count))
}

fn load_zeros(data_dir: &str, n_request: usize, source: &str) -> Result<Vec<f64>, String> {
    let (sname, fname) = resolve_source(n_request, source)?;
    let filepath = format!("{}/{}", data_dir, fname);
    println!("  Data file: {} (source '{}')", filepath, sname);
    let content = std::fs::read_to_string(&filepath)
        .map_err(|e| format!("Cannot open {}: {}", filepath, e))?;

    let is_csv = sname == "csv";
    let is_hight = sname == "highT";
    let mut zeros: Vec<f64> = Vec::with_capacity(n_request);
    let mut block_offset = 0.0f64;
    for line in content.lines() {
        let t = line.trim();
        if t.is_empty() { continue; }
        if t.starts_with('#') {
            if is_hight {
                if let Some(p) = t.find("offset=") {
                    if let Ok(v) = t[p + 7..].trim().parse::<f64>() { block_offset = v; }
                }
            }
            continue;
        }
        let parsed = if is_csv {
            t.split(',').nth(1).and_then(|s| s.trim().parse::<f64>().ok())
        } else {
            t.parse::<f64>().ok()
        };
        if let Some(v) = parsed {
            let val = v + block_offset;
            if val > 0.0 {
                zeros.push(val);
                if zeros.len() >= n_request { break; }
            }
        }
    }
    zeros.sort_by(|a, b| a.partial_cmp(b).unwrap_or(std::cmp::Ordering::Equal));
    if zeros.is_empty() {
        return Err("No valid zeros loaded".into());
    }
    Ok(zeros)
}

// ---------------------------------------------------------------------------
// Canonical math kernel (CANON_SPEC §1–§6)
// ---------------------------------------------------------------------------
fn lambert_w(x: f64) -> f64 {
    if x <= 0.0 { return 0.0; }
    let mut w = x.ln();
    if w < 0.0 { w = x; } // W(x) ~ x for 0<x<1; avoids the w=-1 flat point
    for _ in 0..50 {
        let ew = w.exp();
        let f = w * ew - x;
        let fp = ew * (w + 1.0);
        if fp.abs() < 1e-30 { break; }
        let delta = f / fp;
        w -= delta;
        if delta.abs() < 1e-14 * (1.0 + w.abs()) { break; }
    }
    w
}

/// gram_point: solution of theta(t) = pi*n (CANON_SPEC §2).
fn gram_point(n: usize) -> f64 {
    if n == 0 { return 0.0; }
    let nf = n as f64;
    let mut t = 2.0 * PI * nf / lambert_w(nf / std::f64::consts::E);
    for _ in 0..8 {
        let arg = t / (2.0 * PI);
        if arg <= 0.0 { break; }
        let theta = 0.5 * t * arg.ln() - 0.5 * t - PI / 8.0
            + 1.0 / (48.0 * t) + 7.0 / (5760.0 * t * t * t);
        let dtheta = 0.5 * arg.ln() - 1.0 / (48.0 * t * t)
            - 21.0 / (5760.0 * t * t * t * t);
        if dtheta.abs() < 1e-30 { break; }
        t -= (theta - nf * PI) / dtheta;
    }
    t
}

const GUE_TN: usize = 32768;
const GUE_SMAX: f64 = 5.0;

fn gue_exact(s: f64) -> f64 {
    if s <= 0.0 { return 0.0; }
    erfl(2.0 * s / PI.sqrt()) - (4.0 * s / PI) * (-4.0 * s * s / PI).exp()
}

/// erf via the series/continued-fraction split (accuracy ~1e-15):
/// Taylor series around 0 for |x| < 2.2, Lentz continued fraction for
/// erfc beyond (DLMF 7.9.1).
fn erfl(x: f64) -> f64 {
    let ax = x.abs();
    let v = if ax < 2.2 {
        // Taylor series of erf: 2/sqrt(pi) * sum (-1)^k x^(2k+1)/(k!(2k+1))
        let mut term = ax;
        let mut sum = ax;
        let x2 = ax * ax;
        for k in 1..200 {
            term *= -x2 / k as f64;
            let add = term / (2.0 * k as f64 + 1.0);
            sum += add;
            if add.abs() < 1e-18 * sum.abs() { break; }
        }
        2.0 / PI.sqrt() * sum
    } else {
        1.0 - erfc_cf(ax)
    };
    if x >= 0.0 { v } else { -v }
}

/// erfc(z) for z >= 2.2 via the Lentz continued fraction
///   sqrt(pi) e^{z^2} erfc(z) ~ 1/(z + (1/2)/(z + 1/(z + (3/2)/(z + ...))))
/// (partial numerators k/2, partial denominators z; DLMF 7.9.1).
fn erfc_cf(z: f64) -> f64 {
    let tiny = 1e-300;
    // G = z + (1/2)/(z + 1/(z + (3/2)/(z + ...))) via modified Lentz
    let mut f = z;
    let mut c = f;
    let mut d = 0.0;
    for k in 1..200 {
        let a = k as f64 / 2.0;
        d = z + a * d;
        if d == 0.0 { d = tiny; }
        c = z + a / c;
        if c == 0.0 { c = tiny; }
        d = 1.0 / d;
        let delta = c * d;
        f *= delta;
        if (delta - 1.0).abs() < 1e-17 { break; }
    }
    // F = 1/G; erfc = F * e^{-z^2} / sqrt(pi)
    (-z * z).exp() / (PI.sqrt() * f)
}

fn gue_cdf(s: f64) -> f64 {
    if s <= 0.0 { return 0.0; }
    if s >= GUE_SMAX { return gue_exact(s); }
    // canonical 32768-point table (CANON_SPEC §5), built lazily once
    fn table() -> &'static Vec<f64> {
        use std::sync::OnceLock;
        static TBL: OnceLock<Vec<f64>> = OnceLock::new();
        TBL.get_or_init(|| {
            (0..GUE_TN)
                .map(|i| gue_exact(i as f64 * GUE_SMAX / (GUE_TN - 1) as f64))
                .collect()
        })
    }
    let tbl = table();
    let x = s * (GUE_TN - 1) as f64 / GUE_SMAX;
    let i = x.floor() as isize;
    if i < 0 || i as usize >= GUE_TN - 1 { return gue_exact(s); }
    let t = x - i as f64;
    (1.0 - t) * tbl[i as usize] + t * tbl[i as usize + 1]
}

fn compute_bn(zeros: &[f64], n: usize) -> f64 {
    if n == 0 || n > zeros.len() { return f64::NAN; }
    let mut sum = 0.0;
    for k in 1..=n {
        sum += (zeros[k - 1] - gram_point(k)).abs();
    }
    sum / n as f64
}

fn compute_bn_offset(zeros: &[f64], n: usize, offset: usize) -> f64 {
    if n == 0 || offset + n > zeros.len() { return f64::NAN; }
    let mut sum = 0.0;
    for k in 1..=n {
        sum += (zeros[k - 1] - gram_point(offset + k)).abs();
    }
    sum / n as f64
}

fn compute_spacings(zeros: &[f64]) -> Vec<f64> {
    let mut sp = Vec::with_capacity(zeros.len());
    for k in 0..zeros.len().saturating_sub(1) {
        if zeros[k] <= 0.0 { continue; }
        sp.push((zeros[k + 1] - zeros[k]) * (zeros[k] / (2.0 * PI)).ln() / (2.0 * PI));
    }
    sp
}

fn ks_asymptotic_pvalue(lam: f64) -> f64 {
    if lam <= 0.0 { return 1.0; }
    let v = if lam < 0.6 {
        let mut s2 = 0.0;
        for k in 1..=1000 {
            let term2 = (-((((2.0 * k as f64 - 1.0) * (2.0 * k as f64 - 1.0)) * PI * PI) / (8.0 * lam * lam))).exp();
            s2 += term2;
            if term2 < 1e-18 { break; }
        }
        1.0 - (2.0 * PI).sqrt() / lam * s2
    } else {
        let mut s = 0.0;
        let mut sign = 1.0;
        for k in 1..=100 {
            let term = sign * (-2.0 * (k as f64) * (k as f64) * lam * lam).exp();
            s += term;
            sign = -sign;
            if term.abs() < 1e-18 { break; }
        }
        2.0 * s
    };
    v.clamp(0.0, 1.0)
}

fn ks_test_dp(sp: &mut Vec<f64>) -> (f64, f64) {
    sp.sort_by(|a, b| a.partial_cmp(b).unwrap_or(std::cmp::Ordering::Equal));
    let n = sp.len() as f64;
    let mut d = 0.0f64;
    for i in 1..=sp.len() {
        let f = gue_cdf(sp[i - 1]);
        d = d.max((i as f64 / n - f).abs()).max(((i as f64 - 1.0) / n - f).abs());
    }
    let lam = (n.sqrt() + 0.12 + 0.11 / n.sqrt()) * d;
    (d, ks_asymptotic_pvalue(lam))
}

fn cvm_test(sp: &Vec<f64>) -> f64 {
    let mut s = sp.clone();
    s.sort_by(|a, b| a.partial_cmp(b).unwrap_or(std::cmp::Ordering::Equal));
    let n = s.len() as f64;
    let mut w2 = 0.0;
    for i in 1..=s.len() {
        let u = gue_cdf(s[i - 1]);
        let d = u - (2.0 * i as f64 - 1.0) / (2.0 * n);
        w2 += d * d;
    }
    w2 + 1.0 / (12.0 * n)
}

fn ad_stat(sp: &Vec<f64>) -> f64 {
    let mut s = sp.clone();
    s.sort_by(|a, b| a.partial_cmp(b).unwrap_or(std::cmp::Ordering::Equal));
    let n = s.len() as f64;
    if s.len() < 2 { return f64::NAN; }
    let mut acc = 0.0;
    for i in 1..=s.len() {
        let fi = gue_cdf(s[i - 1]).clamp(1e-300, 1.0 - 1e-16);
        let fni = gue_cdf(s[s.len() - i]).clamp(1e-300, 1.0 - 1e-16);
        acc += (2.0 * i as f64 - 1.0) * (fi.ln() + (1.0 - fni).ln());
    }
    -n - acc / n
}

fn mean_ratio(zeros: &[f64]) -> (f64, usize) {
    if zeros.len() < 3 { return (f64::NAN, 0); }
    let mut acc = 0.0;
    let mut cnt = 0usize;
    for i in 0..zeros.len() - 2 {
        let a = zeros[i + 1] - zeros[i];
        let b = zeros[i + 2] - zeros[i + 1];
        let m = a.max(b);
        if a == 0.0 && b == 0.0 { continue; }
        acc += a.min(b) / m;
        cnt += 1;
    }
    if cnt == 0 { return (f64::NAN, 0); }
    (acc / cnt as f64, cnt)
}

struct Linreg { slope: f64, intercept: f64, se: f64, r2: f64 }

fn linreg(x: &[f64], y: &[f64]) -> Linreg {
    let n = x.len() as f64;
    let (mut sx, mut sy, mut sxx, mut sxy, mut syy) = (0.0, 0.0, 0.0, 0.0, 0.0);
    for i in 0..x.len() {
        sx += x[i]; sy += y[i];
        sxx += x[i] * x[i]; sxy += x[i] * y[i]; syy += y[i] * y[i];
    }
    let den = n * sxx - sx * sx;
    if den.abs() < 1e-30 { return Linreg { slope: 0.0, intercept: 0.0, se: 0.0, r2: 0.0 }; }
    let slope = (n * sxy - sx * sy) / den;
    let intercept = (sy - slope * sx) / n;
    let ss_tot = syy - sy * sy / n;
    let mut ss_res = 0.0;
    for i in 0..x.len() {
        let e = y[i] - (slope * x[i] + intercept);
        ss_res += e * e;
    }
    let r2 = if ss_tot > 0.0 { 1.0 - ss_res / ss_tot } else { 0.0 };
    let se = if x.len() > 2 && den > 0.0 { ((ss_res / (n - 2.0)) * n / den).sqrt() } else { 0.0 };
    Linreg { slope, intercept, se, r2 }
}

// ---------------------------------------------------------------------------
// Objections (CANON_SPEC §7) — structured results, rendered by verify_en/ru
// ---------------------------------------------------------------------------
pub struct Obj1Res { pub ns: Vec<usize>, pub bn: Vec<f64>, pub converging: bool,
    pub has_fit: bool, pub fit_a: f64, pub fit_s: f64, pub fit_r2: f64 }
pub struct Obj2Res { pub n: usize, pub mean: f64, pub var: f64, pub d: f64, pub p: f64,
    pub w2: f64, pub a2: f64, pub r: f64, pub nr: usize, pub rejected: bool }
pub struct Obj3Res { pub ns: Vec<usize>, pub bn: Vec<f64>, pub slope: f64,
    pub intercept: f64, pub r2: f64, pub cilo: f64, pub cihi: f64, pub ok: bool }

pub fn run_objection1(zeros: &[f64]) -> Obj1Res {
    let maxz = zeros.len();
    let ns: Vec<usize> = [100usize, 500, 1000, 5000, 10000, 50000]
        .iter().copied().filter(|&n| n <= maxz).collect();
    let ns = if ns.is_empty() { vec![maxz.min(100)] } else { ns };
    let bn: Vec<f64> = ns.iter().map(|&n| compute_bn(zeros, n)).collect();
    let mut converging = true;
    for i in 1..bn.len() { if bn[i] >= bn[i - 1] { converging = false; } }
    let mut res = Obj1Res { ns, bn, converging, has_fit: false, fit_a: 0.0, fit_s: 0.0, fit_r2: 0.0 };
    if res.ns.len() >= 3 {
        let mut lx = Vec::new(); let mut ly = Vec::new();
        for i in 0..res.ns.len() {
            if res.ns[i] > 1 && res.bn[i] > 0.0 {
                lx.push((res.ns[i] as f64).ln());
                ly.push(res.bn[i].ln());
            }
        }
        if lx.len() >= 3 {
            let lr = linreg(&lx, &ly);
            res.has_fit = true;
            res.fit_a = lr.intercept.exp();
            res.fit_s = -lr.slope;
            res.fit_r2 = lr.r2;
        }
    }
    res
}

pub fn run_objection2(zeros: &[f64]) -> Obj2Res {
    let mut sp = compute_spacings(zeros);
    if sp.len() < 2 {
        return Obj2Res { n: sp.len(), mean: f64::NAN, var: f64::NAN, d: f64::NAN,
            p: f64::NAN, w2: f64::NAN, a2: f64::NAN, r: f64::NAN, nr: 0, rejected: false };
    }
    let mean = sp.iter().sum::<f64>() / sp.len() as f64;
    let var = sp.iter().map(|s| (s - mean) * (s - mean)).sum::<f64>() / (sp.len() - 1) as f64;
    let (d, p) = ks_test_dp(&mut sp);
    let w2 = cvm_test(&sp);
    let a2 = ad_stat(&sp);
    let (r, nr) = mean_ratio(zeros);
    Obj2Res { n: sp.len(), mean, var, d, p, w2, a2, r, nr, rejected: p < 0.05 }
}

pub fn run_objection3(zeros: &[f64]) -> Obj3Res {
    let maxz = zeros.len();
    let mut ns: Vec<usize> = Vec::new();
    let mut n = 50usize;
    while n <= maxz { ns.push(n); n *= 2; }
    if let Some(&last) = ns.last() {
        if last != maxz && maxz > 100 { ns.push(maxz); }
    }
    let mut lx = Vec::new(); let mut ly = Vec::new();
    for &n in &ns {
        let bn = compute_bn(zeros, n);
        if bn > 0.0 { lx.push((n as f64).ln()); ly.push(bn.ln()); }
    }
    if lx.len() < 3 {
        return Obj3Res { ns, bn: vec![], slope: f64::NAN, intercept: f64::NAN,
            r2: f64::NAN, cilo: f64::NAN, cihi: f64::NAN, ok: false };
    }
    let lr = linreg(&lx, &ly);
    let ok = (lr.slope + 0.5).abs() < 0.1;
    Obj3Res { ns, bn: vec![], slope: lr.slope, intercept: lr.intercept, r2: lr.r2,
        cilo: lr.slope - 1.96 * lr.se, cihi: lr.slope + 1.96 * lr.se, ok }
}

// ---------------------------------------------------------------------------
// Self-check (CANON_SPEC §8)
// ---------------------------------------------------------------------------
pub struct SCRow { pub name: String, pub skip: bool, pub ok: bool,
    pub got: f64, pub exp: f64, pub delta: f64 }

pub fn selfcheck(zeros: &[f64]) -> (Vec<SCRow>, usize, usize) {
    let mut rows: Vec<SCRow> = Vec::new();
    let (mut npass, mut nfail) = (0usize, 0usize);
    fn add(rows: &mut Vec<SCRow>, npass: &mut usize, nfail: &mut usize,
           name: &str, got: f64, exp: f64, tol: f64, rel: bool) {
        let d = (got - exp).abs() / if rel { exp.abs() } else { 1.0 };
        let ok = !got.is_nan() && d <= tol;
        rows.push(SCRow { name: name.to_string(), skip: false, ok, got, exp, delta: d });
        if ok { *npass += 1 } else { *nfail += 1 }
    }
    {
        for (x, e) in [(0.5, 0.35173371124919584), (1.0, 0.5671432904097838),
                       (3.7, 1.1599531786120223), (10.0, 1.7455280027406992),
                       (271.8, 4.17576816800275), (12345.6, 7.417247034540566)] {
            add(&mut rows, &mut npass, &mut nfail, &format!("lambert_w({})", x), lambert_w(x), e, 1e-12, true);
        }
        for (n, e) in [(1usize, 23.17028270133466), (2, 27.670182217848343),
                       (3, 31.71797995477886), (10, 54.67523744685398),
                       (100, 238.58259051450293), (1000, 1421.25638903275),
                       (10000, 9878.910118894457), (50000, 40434.6952780045)] {
            add(&mut rows, &mut npass, &mut nfail, &format!("gram_point(n={})", n), gram_point(n), e, 1e-6, false);
        }
        for (n, e) in [(100usize, 3.3321638710140165), (500, 2.3912304957476382),
                       (1000, 2.1072522951855435), (5000, 1.6299485869022874),
                       (10000, 1.4794053414584762), (50000, 1.2125526772588608)] {
            if n <= zeros.len() {
                add(&mut rows, &mut npass, &mut nfail, &format!("bN(N={})", n), compute_bn(zeros, n), e, 1e-6, false);
            } else {
                rows.push(SCRow { name: format!("bN(N={})", n), skip: true, ok: false,
                    got: 0.0, exp: e, delta: 0.0 });
            }
        }
        if zeros.len() >= 1500 {
            add(&mut rows, &mut npass, &mut nfail, "bN(N=1000,off=500)", compute_bn_offset(zeros, 1000, 500), 624.6201618180231, 1e-6, false);
        } else {
            rows.push(SCRow { name: "bN(N=1000,off=500)".into(), skip: true, ok: false,
                got: 0.0, exp: 624.6201618180231, delta: 0.0 });
        }
        if zeros.len() >= 50000 {
            let z5 = &zeros[..50000];
            let mut sp = compute_spacings(z5);
            let mean = sp.iter().sum::<f64>() / sp.len() as f64;
            let var = sp.iter().map(|s| (s - mean) * (s - mean)).sum::<f64>() / (sp.len() - 1) as f64;
            let (d, p) = ks_test_dp(&mut sp);
            add(&mut rows, &mut npass, &mut nfail, "spacings.mean", mean, 0.999976001221201, 1e-9, false);
            add(&mut rows, &mut npass, &mut nfail, "spacings.var", var, 0.1590654827835423, 1e-9, false);
            add(&mut rows, &mut npass, &mut nfail, "ks_zeros.D", d, 0.021619337032982328, 1e-9, false);
            add(&mut rows, &mut npass, &mut nfail, "ks_zeros.p", p, 9.567870399361496e-21, 1e-6, true);
            add(&mut rows, &mut npass, &mut nfail, "cvm_zeros.W2", cvm_test(&sp), 8.177703317829403, 1e-9, true);
            add(&mut rows, &mut npass, &mut nfail, "ad_zeros.A2", ad_stat(&sp), 61.49242624209728, 1e-9, true);
            let (r, _) = mean_ratio(z5);
            add(&mut rows, &mut npass, &mut nfail, "rmean_zeros.r", r, 0.6118798907208398, 1e-9, false);
        } else {
            for nm in ["spacings.mean/var", "ks_zeros.D/p", "cvm_zeros.W2", "ad_zeros.A2", "rmean_zeros.r"] {
                rows.push(SCRow { name: nm.into(), skip: true, ok: false, got: 0.0, exp: 0.0, delta: 0.0 });
            }
        }
    }
    (rows, npass, nfail)
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------
fn main() {
    let args = parse_args();

    println!();
    if args.lang == 2 {
        println!("  ╔═══════════════════════════════════════════════╗");
        println!("  ║   AB-CLOUD ПРОВЕРКА — ГИПОТЕЗА РИМАНА        ║");
        println!("  ╚═══════════════════════════════════════════════╝");
    } else {
        println!("  ╔═══════════════════════════════════════════════╗");
        println!("  ║   AB-CLOUD VERIFICATION — RIEMANN HYPOTHESIS  ║");
        println!("  ╚═══════════════════════════════════════════════╝");
    }
    println!();

    let zeros = match load_zeros(&args.data_dir, args.n_zeros, &args.source) {
        Ok(z) => z,
        Err(e) => { eprintln!("ERROR: {}", e); std::process::exit(2); }
    };
    println!("  Zeros loaded: {}", zeros.len());
    if zeros.len() < 2 {
        eprintln!("ERROR: need at least 2 zeros");
        std::process::exit(2);
    }

    let mut sc_fail = -1i32;
    if args.selfcheck {
        let (rows, npass, nfail) = selfcheck(&zeros);
        if args.lang == 2 {
            print!("{}", verify_ru::render_selfcheck_ru(&rows, npass, nfail));
        } else {
            print!("{}", verify_en::render_selfcheck_en(&rows, npass, nfail));
        }
        sc_fail = nfail as i32;
    }

    if args.objection == 0 || args.objection == 1 {
        let r = run_objection1(&zeros);
        if args.lang == 2 { print!("{}", verify_ru::render_obj1_ru(&r)); }
        else { print!("{}", verify_en::render_obj1_en(&r)); }
    }
    if args.objection == 0 || args.objection == 2 {
        let r = run_objection2(&zeros);
        if args.lang == 2 { print!("{}", verify_ru::render_obj2_ru(&r)); }
        else { print!("{}", verify_en::render_obj2_en(&r)); }
    }
    if args.objection == 0 || args.objection == 3 {
        let r = run_objection3(&zeros);
        if args.lang == 2 { print!("{}", verify_ru::render_obj3_ru(&r)); }
        else { print!("{}", verify_en::render_obj3_en(&r)); }
    }

    println!("\n  AB-Cloud Verification Suite — complete.\n");
    if sc_fail > 0 { std::process::exit(1); }
}
