// spinor38 (Rust port) — Test 38: 64 spinor structures of the Klein quartic.
// Self-implemented cyclic Jacobi eigenvalue algorithm; std only, no crates.
// Build: cargo build --release   Run: cargo run --release -- [repo-root]
use std::env;
use std::fs;
use std::path::{Path, PathBuf};
use std::process::exit;

struct Cls {
    cls: i32,
    orbit: i32,
    #[allow(dead_code)]
    arf: i32,
    signs: Vec<f64>,
}

fn find_data_dir(root_arg: Option<&String>) -> PathBuf {
    let mut roots: Vec<PathBuf> = Vec::new();
    if let Some(r) = root_arg {
        roots.push(PathBuf::from(r));
    }
    roots.push(env::current_dir().unwrap_or_else(|_| PathBuf::from(".")));
    for r in roots {
        let mut b = r.clone();
        for _ in 0..6 {
            let cand = b.join("verification/spinor64/data/spinor_classes.csv");
            if cand.exists() {
                return b.join("verification/spinor64/data");
            }
            b = b.join("..");
        }
    }
    eprintln!("data dir not found; pass repo root as argument");
    exit(2);
}

fn jacobi_eigen(a_in: &Vec<Vec<f64>>) -> Vec<f64> {
    let n = a_in.len();
    let mut a = a_in.clone();
    for _sweep in 0..200 {
        let mut off = 0.0f64;
        for p in 0..n {
            for q in (p + 1)..n {
                off += a[p][q] * a[p][q];
            }
        }
        if off < 1e-24 {
            break;
        }
        for p in 0..n {
            for q in (p + 1)..n {
                if a[p][q].abs() < 1e-15 {
                    continue;
                }
                let tau = (a[q][q] - a[p][p]) / (2.0 * a[p][q]);
                let t = if tau >= 0.0 { 1.0 } else { -1.0 }
                    / (tau.abs() + (1.0 + tau * tau).sqrt());
                let c = 1.0 / (1.0 + t * t).sqrt();
                let s = t * c;
                for k in 0..n {
                    let akp = a[k][p];
                    let akq = a[k][q];
                    a[k][p] = c * akp - s * akq;
                    a[k][q] = s * akp + c * akq;
                }
                for k in 0..n {
                    let apk = a[p][k];
                    let aqk = a[q][k];
                    a[p][k] = c * apk - s * aqk;
                    a[q][k] = s * apk + c * aqk;
                }
            }
        }
    }
    let mut eig: Vec<f64> = (0..n).map(|i| a[i][i]).collect();
    eig.sort_by(|x, y| x.partial_cmp(y).unwrap());
    eig
}

fn extract_json_num(js: &str, key: &str) -> f64 {
    let pat = format!("\"{}\":", key);
    if let Some(i) = js.find(&pat) {
        let rest = &js[i + pat.len()..];
        let end = rest
            .find(|ch: char| !"0123456789.eE-".contains(ch))
            .unwrap_or(rest.len());
        return rest[..end].parse().unwrap_or(0.0);
    }
    0.0
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let dd = find_data_dir(args.get(1));

    let txt = fs::read_to_string(dd.join("spinor_classes.csv")).expect("classes");
    let mut classes: Vec<Cls> = Vec::new();
    for (i, line) in txt.lines().enumerate() {
        if i == 0 || line.is_empty() {
            continue;
        }
        let parts: Vec<&str> = line.splitn(4, ',').collect();
        let signs: Vec<f64> = parts[3]
            .split_whitespace()
            .map(|x| x.parse::<f64>().unwrap())
            .collect();
        classes.push(Cls {
            cls: parts[0].parse().unwrap(),
            orbit: parts[1].parse().unwrap(),
            arf: parts[2].parse().unwrap(),
            signs,
        });
    }
    let txt = fs::read_to_string(dd.join("klein_graph_edges.csv")).expect("edges");
    let mut edges: Vec<(usize, usize)> = Vec::new();
    for (i, line) in txt.lines().enumerate() {
        if i == 0 || line.is_empty() {
            continue;
        }
        let p: Vec<&str> = line.split(',').collect();
        edges.push((p[1].parse().unwrap(), p[2].parse().unwrap()));
    }
    let js = fs::read_to_string(dd.join("reference_stats.json")).expect("stats");
    let r_ref = extract_json_num(&js, "r_mean_reference");
    let n_zero_ref = extract_json_num(&js, "n_zero_modes") as i32;
    let representative = extract_json_num(&js, "representative_class") as i32;

    let n = 56usize;
    let n_odd = classes.iter().filter(|c| c.orbit == 0).count();

    let mut spectra: Vec<Vec<f64>> = Vec::new();
    let mut rep_spectrum: Vec<f64> = Vec::new();
    for c in &classes {
        if c.orbit != 0 {
            continue;
        }
        let mut a = vec![vec![0.0f64; n]; n];
        for (k, (u, v)) in edges.iter().enumerate() {
            let s = c.signs[k];
            a[*u][*v] = s;
            a[*v][*u] = s;
        }
        let w = jacobi_eigen(&a);
        if c.cls == representative {
            rep_spectrum = w.clone();
        }
        spectra.push(w);
    }

    let mut isomax = 0.0f64;
    for a in 0..spectra.len() {
        for b in (a + 1)..spectra.len() {
            for i in 0..n {
                let d = (spectra[a][i] - spectra[b][i]).abs();
                if d > isomax {
                    isomax = d;
                }
            }
        }
    }

    let mut n_zero = 0i32;
    let mut lam: Vec<f64> = rep_spectrum.iter().map(|v| v.abs()).collect();
    for v in &lam {
        if *v < 1e-8 {
            n_zero += 1;
        }
    }
    lam.sort_by(|x, y| x.partial_cmp(y).unwrap());
    let mut dsp: Vec<f64> = Vec::new();
    for i in 0..lam.len() - 1 {
        let d = lam[i + 1] - lam[i];
        if d > 1e-8 {
            dsp.push(d);
        }
    }
    let mut rsum = 0.0;
    for i in 0..dsp.len() - 1 {
        rsum += dsp[i].min(dsp[i + 1]) / dsp[i].max(dsp[i + 1]);
    }
    let r_mean = rsum / (dsp.len() as f64 - 1.0);

    println!("Test 38 - 64 spinor structures of the Klein quartic (Rust port)");
    println!("classes loaded: {} | odd-orbit members: {}", classes.len(), n_odd);
    println!(
        "isospectrality within the odd orbit: max|dlambda| = {:.3e} -> {}",
        isomax,
        if isomax < 1e-9 { "PASS" } else { "FAIL" }
    );
    println!("zero modes (representative): {} (expected {})", n_zero, n_zero_ref);
    let r_ok = (r_mean - r_ref).abs() < 1e-6;
    println!(
        "<r> (representative): {:.10} (reference 0.4515710793) -> {}",
        r_mean,
        if r_ok { "PASS" } else { "FAIL" }
    );
    let ok = isomax < 1e-9 && n_zero == n_zero_ref && r_ok;
    println!("VERDICT: {}", if ok { "PASS" } else { "FAIL" });
    exit(if ok { 0 } else { 1 });
}
