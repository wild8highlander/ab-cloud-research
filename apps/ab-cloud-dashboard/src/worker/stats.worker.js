/**
 * stats.worker.js — real-time RMT statistics for the AB-Cloud dashboard.
 * Implements the core diagnostics of the Julia suite in plain JS:
 *   b(N) convergence vs Gram points (suite convention, CANON_SPEC §2),
 *   spacing ratios <r>, KS vs the GUE ratio law,
 *   Sigma^2(L), Delta_3(L), R_2(s), and a 56x56 Jacobi eigensolver
 *   for the spinor-structure operators.
 */
'use strict';

const R_GUE = 0.59965, R_GOE = 0.53590, R_POISSON = 0.38629;

function sortAsc(a) { return a.slice().sort((x, y) => x - y); }

function spacingRatios(eigs) {
  const lam = sortAsc(eigs.map(Math.abs)).filter(v => v > 1e-8);
  const d = [];
  for (let i = 1; i < lam.length; i++) d.push(lam[i] - lam[i - 1]);
  const r = [];
  for (let i = 0; i + 1 < d.length; i++) {
    const mn = Math.min(d[i], d[i + 1]), mx = Math.max(d[i], d[i + 1]);
    r.push(mn / mx);
  }
  return r;
}

// CDF of the GUE (beta=2) ratio law p(r) = 27/8 (r+r^2)^2 / (1+r+r^2)^5
const RCDF = (() => {
  const N = 200001, grid = [], cdf = [0];
  for (let i = 0; i < N; i++) grid.push(i / (N - 1));
  let acc = 0;
  for (let i = 1; i < N; i++) {
    const f = (r) => (27 / 8) * Math.pow(r + r * r, 2) / Math.pow(1 + r + r * r, 5);
    acc += (f(grid[i]) + f(grid[i - 1])) / 2 * (grid[i] - grid[i - 1]);
    cdf.push(acc);
  }
  return { grid, cdf: cdf.map(v => v / acc) };
})();

function gcdf(r) {
  if (r <= 0) return 0;
  if (r >= 1) return 1;
  // binary search
  let lo = 0, hi = RCDF.grid.length - 1;
  while (hi - lo > 1) {
    const mid = (lo + hi) >> 1;
    if (RCDF.grid[mid] <= r) lo = mid; else hi = mid;
  }
  const t = (r - RCDF.grid[lo]) / (RCDF.grid[hi] - RCDF.grid[lo]);
  return RCDF.cdf[lo] * (1 - t) + RCDF.cdf[hi] * t;
}

function kolmogorovP(D, n) {
  if (!(D > 0) || !(n > 0)) return 1; // D=0 → perfect match; D<0/NaN → no evidence
  const en = Math.sqrt(n);
  const lam = (en + 0.12 + 0.11 / en) * D;
  // hard cap: for vanishing D the exact series needs astronomic k; p → 1 anyway.
  const kmax = Math.min(Math.floor(Math.sqrt(2) / lam) + 1, 200000);
  let s = 0;
  for (let k = 1; k <= kmax; k++) {
    const term = Math.exp(-2 * k * k * lam * lam);
    s += (k % 2 ? 1 : -1) * term;
    if (k > 50 && term < 1e-17) break; // terms decay monotonically past the first oscillations
  }
  return Math.max(0, Math.min(1, 2 * s));
}

function gueRatioKS(ratios) {
  const r = sortAsc(ratios);
  const n = r.length;
  let dp = 0, dm = 0;
  for (let i = 0; i < n; i++) {
    const F = gcdf(r[i]);
    dp = Math.max(dp, (i + 1) / n - F);
    dm = Math.max(dm, F - i / n);
  }
  const D = Math.max(dp, dm);
  return { D, p: kolmogorovP(D, n) };
}

function bNConvergence(zeros, checkpoints) {
  // Suite convention (CANON_SPEC §2; port of compute_bn in verification/rust):
  //   b(N) = (1/N) Σ_{k=1..N} |γ_k − gram_point(k)|,
  // where gram_point(k) solves θ(t) = πk (Riemann–Siegel theta).
  // Single incremental pass up to max(checkpoints), prefix sums at each N.
  const cps = [...checkpoints].sort((a, b) => a - b);
  const maxN = Math.min(cps[cps.length - 1], zeros.length);
  const out = [];
  let sum = 0;
  let ci = 0;
  for (let k = 1; k <= maxN; k++) {
    sum += Math.abs(zeros[k - 1] - gramPoint(k));
    while (ci < cps.length && cps[ci] === k) {
      out.push({ N: k, b: sum / k });
      ci++;
    }
  }
  return out;
}

// Lambert W (principal branch), x >= 0 — Newton iteration,
// port of the solver in verification/rust/src/main.rs.
function lambertW(x) {
  let w = Math.log(x > 1 ? x : 1);
  if (w < 0) w = x; // W(x) ~ x for 0<x<1; avoids the w=-1 flat point
  for (let i = 0; i < 50; i++) {
    const ew = Math.exp(w);
    const f = w * ew - x;
    const fp = ew * (w + 1);
    if (Math.abs(fp) < 1e-30) break;
    const delta = f / fp;
    w -= delta;
    if (Math.abs(delta) < 1e-14 * (1 + Math.abs(w))) break;
  }
  return w;
}

// gram_point(n): solution of theta(t) = pi*n (CANON_SPEC §2;
// faithful port of gram_point in verification/rust/src/main.rs).
function gramPoint(n) {
  if (n === 0) return 0;
  let t = (2 * Math.PI * n) / lambertW(n / Math.E);
  for (let i = 0; i < 8; i++) {
    const arg = t / (2 * Math.PI);
    if (arg <= 0) break;
    const theta = 0.5 * t * Math.log(arg) - 0.5 * t - Math.PI / 8
      + 1 / (48 * t) + 7 / (5760 * t * t * t);
    const dtheta = 0.5 * Math.log(arg) - 1 / (48 * t * t)
      - 21 / (5760 * t * t * t * t);
    if (Math.abs(dtheta) < 1e-30) break;
    t -= (theta - n * Math.PI) / dtheta;
  }
  return t;
}

// Smooth (average) zero-counting function N̄(T) — leading-order
// Riemann–von Mangoldt: N̄(T) = (T/2π)·ln(T/2π) − T/2 + 7/8.
// Port of smooth_counting_function (verification/julia/ab_cloud_full.jl §5);
// used ONLY to build cumulative unfolded positions for Σ²(L).
function smoothCounting(t) {
  if (t <= 0) return 0;
  const x = t / (2 * Math.PI);
  return x * Math.log(x) - x + 7 / 8;
}

// binary search: first index with arr[i] >= x (Julia searchsortedfirst)
function lowerBound(arr, x) {
  let lo = 0, hi = arr.length;
  while (lo < hi) {
    const mid = (lo + hi) >> 1;
    if (arr[mid] < x) lo = mid + 1; else hi = mid;
  }
  return lo;
}

function numberVariance(eigs, Lvalues, nWindows = 3000) {
  // Σ²(L) — number variance. Faithful port of number_variance in
  // verification/julia/ab_cloud_full.jl:
  //   1. unfold the zeros via the smooth counting function N̄(γ) (mean
  //      spacing → 1; a wide-neighborhood or raw-window unfolding would fold
  //      the slow 1/log density drift into Σ² and blow it up to O(L²));
  //   2. drop n_windows random windows of unfolded length L into [u₁, u_end]
  //      and take the variance of the level counts.
  // Poisson: Σ²(L) = L;  GUE: Σ²(L) = O(log L).
  const u = sortAsc(eigs).map(smoothCounting);
  const n = u.length;
  const uLo = u[0], uHi = u[n - 1];
  // seeded LCG (same convention as scenes.js) → the chart is deterministic
  // across reloads instead of jumpy Monte-Carlo noise
  let sd = 123456789;
  const rnd = () => (sd = (sd * 1103515245 + 12345) % 2147483648) / 2147483648;
  const out = [];
  const counts = new Float64Array(nWindows);
  for (const L of Lvalues) {
    if (uHi - uLo <= L) { out.push({ L, sigma2: NaN }); continue; }
    for (let w = 0; w < nWindows; w++) {
      const x0 = uLo + rnd() * (uHi - uLo - L);
      counts[w] = lowerBound(u, x0 + L) - lowerBound(u, x0);
    }
    let mean = 0;
    for (let w = 0; w < nWindows; w++) mean += counts[w];
    mean /= nWindows;
    let acc = 0;
    for (let w = 0; w < nWindows; w++) acc += (counts[w] - mean) ** 2;
    out.push({ L, sigma2: acc / Math.max(nWindows - 1, 1) }); // Julia var(): corrected
  }
  return out;
}

function delta3(eigs, Lvalues) {
  const lam = sortAsc(eigs);
  const out = [];
  for (const L of Lvalues) {
    const nW = 300;
    const step = Math.max(1, Math.floor(lam.length / nW));
    let acc = 0, cnt = 0;
    for (let start = 0; start + L < lam.length; start += step) {
      const ys = [];
      for (let i = start; i < lam.length && ys.length <= L + 1; i++) ys.push(i - start);
      const n = ys.length;
      if (n < 4) continue;
      // least-squares line fit of index vs spectral coordinate -> Delta_3
      let sx = 0, sy = 0, sxx = 0, sxy = 0;
      for (let i = 0; i < n; i++) {
        const x = lam[start + i];
        sx += x; sy += ys[i]; sxx += x * x; sxy += x * ys[i];
      }
      const denom = n * sxx - sx * sx;
      if (denom <= 0) continue;
      const slope = (n * sxy - sx * sy) / denom;
      const inter = (sy - slope * sx) / n;
      let sse = 0;
      for (let i = 0; i < n; i++) {
        const f = inter + slope * lam[start + i];
        sse += Math.pow(ys[i] - f, 2);
      }
      acc += sse / L; // Delta_3 = min over line of (1/L) integral
      cnt++;
      if (cnt >= nW) break;
    }
    out.push({ L, delta3: acc / Math.max(cnt, 1) });
  }
  return out;
}

// ── Stat Lab: additional live diagnostic tests ───────────────────────────
// Port of the Julia suite's statistics layer (ab_cloud_full.jl) to plain JS:
// pair correlation R₂(s), Wigner–GUE surmise KS/χ², QQ vs the GUE ratio law,
// autocorrelation of spacing ratios, even/odd + half-split stationarity,
// Shannon entropy of the ratio distribution and the Wald–Wolfowitz runs test.

function erf(x) {
  // Abramowitz & Stegun 7.1.26, |ε| ≤ 1.5e-7 — plenty for p-values
  const s = x < 0 ? -1 : 1;
  const a = Math.abs(x);
  const t = 1 / (1 + 0.3275911 * a);
  const y = 1 - (((((1.061405429 * t - 1.453152027) * t) + 1.421413741) * t
    - 0.284496736) * t + 0.254829592) * t * Math.exp(-a * a);
  return s * y;
}

function lnGamma(x) {
  // Lanczos approximation (g=7, n=9)
  const g = 7;
  const C = [0.99999999999980993, 676.5203681218851, -1259.1392167224028,
    771.32342877765313, -176.61502916214059, 12.507343278686905,
    -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7];
  if (x < 0.5) {
    return Math.log(Math.PI / Math.sin(Math.PI * x)) - lnGamma(1 - x);
  }
  x -= 1;
  let a = C[0];
  const t = x + g + 0.5;
  for (let i = 1; i < g + 2; i++) a += C[i] / (x + i);
  return 0.5 * Math.log(2 * Math.PI) + (x + 0.5) * Math.log(t) - t + Math.log(a);
}

// lower regularized incomplete gamma P(a,x) — series (x < a+1) / CF otherwise
function gammaP(a, x) {
  if (x <= 0) return 0;
  if (x < a + 1) {
    let ap = a, sum = 1 / a, del = sum;
    for (let n = 1; n < 500; n++) {
      ap += 1;
      del *= x / ap;
      sum += del;
      if (Math.abs(del) < Math.abs(sum) * 1e-15) break;
    }
    return sum * Math.exp(-x + a * Math.log(x) - lnGamma(a));
  }
  // continued fraction for Q(a,x) (Lentz)
  const FPMIN = 1e-300;
  let b = x + 1 - a, c = 1 / FPMIN, d = 1 / b, h = d;
  for (let i = 1; i < 500; i++) {
    const an = -i * (i - a);
    b += 2;
    d = an * d + b; if (Math.abs(d) < FPMIN) d = FPMIN;
    c = b + an / c; if (Math.abs(c) < FPMIN) c = FPMIN;
    d = 1 / d;
    const del = d * c;
    h *= del;
    if (Math.abs(del - 1) < 1e-15) break;
  }
  const q = Math.exp(-x + a * Math.log(x) - lnGamma(a)) * h;
  return 1 - q;
}

// CDF of the GUE (β=2) Wigner surmise p(s) = (32/π²)s²·e^(−4s²/π)
function gueSurmiseCdf(s) {
  if (s <= 0) return 0;
  return erf(2 * s / Math.sqrt(Math.PI)) - (4 * s / Math.PI) * Math.exp(-4 * s * s / Math.PI);
}

function unfold(zeros) {
  const u = sortAsc(zeros).map(smoothCounting);
  const d = [];
  for (let i = 1; i < u.length; i++) d.push(u[i] - u[i - 1]);
  return { u, d };
}

function twoSampleKS(a, b) {
  const xs = sortAsc(a), ys = sortAsc(b);
  const n1 = xs.length, n2 = ys.length;
  let i = 0, j = 0, dp = 0, dm = 0;
  while (i < n1 && j < n2) {
    const x = xs[i], y = ys[j];
    if (x <= y) { i++; }
    if (y <= x) { j++; }
    const f1 = i / n1, f2 = j / n2;
    dp = Math.max(dp, f1 - f2);
    dm = Math.max(dm, f2 - f1);
  }
  const D = Math.max(dp, dm);
  const en = Math.sqrt((n1 * n2) / (n1 + n2));
  const lam = (en + 0.12 + 0.11 / en) * D;
  return { D, p: kolmogorovP(D, Math.max(n1, n2)), lam, n1, n2 };
}

function histMean(counts, edges) {
  let sum = 0, tot = 0;
  for (let k = 0; k < counts.length; k++) {
    const mid = (edges[k] + edges[k + 1]) / 2;
    sum += mid * counts[k]; tot += counts[k];
  }
  return tot ? sum / tot : 0;
}

const LAB = {
  // R₂(s): all pairwise separations of unfolded zeros (window s ≤ 3.2)
  paircorr(zeros) {
    const { u } = unfold(zeros);
    const n = u.length, S_MAX = 3.2, nBins = 160, w = S_MAX / nBins;
    const counts = new Array(nBins).fill(0);
    let pairs = 0;
    for (let i = 0; i < n; i++) {
      for (let j = i + 1; j < n; j++) {
        const s = u[j] - u[i];
        if (s > S_MAX) break;
        counts[Math.min(nBins - 1, Math.floor(s / w))]++;
        pairs++;
      }
    }
    const bins = [], gue = [];
    for (let k = 0; k < nBins; k++) {
      const s = (k + 0.5) * w;
      // Montgomery convention (one-sided): R₂(s) = (1/N)·Σ_{i≠j, u_j−u_i=s} 1
      // = count(j>i pairs in bin) / (N·Δs) — integrates to 1, oscillates
      // around the sine-kernel curve 1 − sinc²(s).
      bins.push({ s, r: counts[k] / (n * w) });
      const t = Math.sin(Math.PI * s) / (Math.PI * s);
      gue.push({ s, r: 1 - t * t });
    }
    return { bins, gue, n, pairs };
  },

  // spacing histogram vs Wigner–GUE surmise + KS
  spacing(zeros) {
    const { d } = unfold(zeros);
    const n = d.length;
    const S_MAX = 4, nBins = 40, w = S_MAX / nBins;
    const counts = new Array(nBins).fill(0);
    const srt = sortAsc(d);
    for (const s of d) counts[Math.min(nBins - 1, Math.floor(s / w))]++;
    const bins = [];
    for (let k = 0; k < nBins; k++) {
      const lo = k * w, hi = lo + w;
      bins.push({ s: (lo + hi) / 2, p: counts[k] / (n * w),
        gue: (gueSurmiseCdf(hi) - gueSurmiseCdf(lo)) / w });
    }
    let dp = 0, dm = 0;
    for (let i = 0; i < n; i++) {
      const F = gueSurmiseCdf(srt[i]);
      dp = Math.max(dp, (i + 1) / n - F);
      dm = Math.max(dm, F - i / n);
    }
    const D = Math.max(dp, dm);
    let mean = 0;
    for (const s of d) mean += s;
    mean /= n;
    let va = 0;
    for (const s of d) va += (s - mean) ** 2;
    return { bins, n, D, p: kolmogorovP(D, n), mean, sd: Math.sqrt(va / n) };
  },

  // QQ plot: ratio quantiles vs the exact GUE ratio-law quantiles
  qq(zeros) {
    const r = sortAsc(spacingRatios(zeros));
    const n = r.length, pts = [];
    for (let k = 1; k < 40; k++) {
      const q = k / 40;
      // invert RCDF by binary search on the precomputed grid
      let lo = 0, hi = RCDF.cdf.length - 1;
      while (hi - lo > 1) {
        const mid = (lo + hi) >> 1;
        if (RCDF.cdf[mid] <= q) lo = mid; else hi = mid;
      }
      const t = (q - RCDF.cdf[lo]) / (RCDF.cdf[hi] - RCDF.cdf[lo] || 1);
      const theo = RCDF.grid[lo] * (1 - t) + RCDF.grid[hi] * t;
      pts.push([theo, r[Math.round(q * n) - 1]]);
    }
    const ks = gueRatioKS(spacingRatios(zeros));
    return { pts, n, D: ks.D, p: ks.p };
  },

  // autocorrelation of the spacing-ratio sequence (GUE: consistent with 0)
  autocorr(zeros) {
    const r = spacingRatios(zeros);
    const n = r.length;
    let m = 0;
    for (const v of r) m += v;
    m /= n;
    let c0 = 0;
    for (const v of r) c0 += (v - m) ** 2;
    c0 /= n;
    const out = [];
    for (let k = 1; k <= 12; k++) {
      let ck = 0;
      for (let i = 0; i + k < n; i++) ck += (r[i] - m) * (r[i + k] - m);
      ck /= n * (n - k);
      out.push({ lag: k, ac: ck / c0 });
    }
    return { out, n, ci: 1.96 / Math.sqrt(n) };
  },

  // even/odd split of the ratio sequence (index stability)
  evenodd(zeros) {
    const r = spacingRatios(zeros);
    const even = r.filter((_, i) => i % 2 === 0);
    const odd = r.filter((_, i) => i % 2 === 1);
    const mean = a => a.reduce((x, y) => x + y, 0) / a.length;
    const ks = twoSampleKS(even, odd);
    return { rEven: mean(even), rOdd: mean(odd), nEven: even.length, nOdd: odd.length,
      D: ks.D, p: ks.p, refs: { R_GUE, R_GOE, R_POISSON } };
  },

  // height-split stationarity: first vs second half of the zeros dataset
  halves(zeros) {
    const h = Math.floor(zeros.length / 2);
    const r1 = spacingRatios(zeros.slice(0, h));
    const r2 = spacingRatios(zeros.slice(h));
    const mean = a => a.reduce((x, y) => x + y, 0) / a.length;
    const ks = twoSampleKS(r1, r2);
    return { r1: mean(r1), r2: mean(r2), n1: r1.length, n2: r2.length,
      D: ks.D, p: ks.p };
  },

  // Shannon entropy of the ratio distribution vs the GUE reference
  entropy(zeros) {
    const r = spacingRatios(zeros);
    const nB = 40, counts = new Array(nB).fill(0);
    for (const v of r) counts[Math.min(nB - 1, Math.floor(v * nB))]++;
    let H = 0;
    for (const c of counts) {
      if (c > 0) { const p = c / r.length; H -= p * Math.log(p); }
    }
    // GUE reference with the same binning, from the exact ratio law pdf
    let Hg = 0;
    for (let k = 0; k < nB; k++) {
      const lo = k / nB, hi = (k + 1) / nB;
      const f = x => (27 / 8) * Math.pow(x + x * x, 2) / Math.pow(1 + x + x * x, 5);
      const p = (f((lo + hi) / 2)) / nB;
      if (p > 0) Hg -= p * Math.log(p);
    }
    return { H, Hg, dH: H - Hg, n: r.length, counts: counts.map((c, k) => ({ k, c })) };
  },

  // χ² GOF of the spacing histogram vs the Wigner–GUE surmise
  chi2(zeros) {
    const { d } = unfold(zeros);
    const n = d.length, S_MAX = 4, nBins = 20, w = S_MAX / nBins;
    const counts = new Array(nBins).fill(0);
    for (const s of d) counts[Math.min(nBins - 1, Math.floor(s / w))]++;
    let chi = 0, dof = 0;
    const rows = [];
    for (let k = 0; k < nBins; k++) {
      const lo = k * w, hi = lo + w;
      const E = n * (gueSurmiseCdf(hi) - gueSurmiseCdf(lo));
      if (E < 5) { rows.push({ range: [lo, hi], O: counts[k], E, used: false }); continue; }
      chi += (counts[k] - E) ** 2 / E;
      dof++;
      rows.push({ range: [lo, hi], O: counts[k], E, used: true });
    }
    dof -= 1; // no parameters fitted
    const p = 1 - gammaP(dof / 2, chi / 2);
    return { chi, dof, p, n, rows };
  },

  // Wald–Wolfowitz runs test on the ratio sequence (above/below median)
  runs(zeros) {
    const r = spacingRatios(zeros);
    const srt = sortAsc(r);
    const med = srt[Math.floor(srt.length / 2)];
    let n1 = 0, n2 = 0, runs = 1;
    const flags = r.map(v => v > med);
    for (const f of flags) { if (f) n1++; else n2++; }
    for (let i = 1; i < flags.length; i++) if (flags[i] !== flags[i - 1]) runs++;
    const n = n1 + n2;
    const mu = (2 * n1 * n2) / n + 1;
    const sd = Math.sqrt((2 * n1 * n2 * (2 * n1 * n2 - n)) / (n * n * (n - 1)));
    const z = (runs - mu) / sd;
    const p = 2 * (1 - gammaP(0.5, (z * z) / 2)); // two-sided normal approx
    return { runs, mu, sd, z, p, n1, n2, n };
  },
};

function labTest(zeros, test) {
  const fn = LAB[test];
  if (!fn) throw new Error(`unknown lab test: ${test}`);
  return fn(zeros);
}

// 56x56 Jacobi eigensolver (for the spinor-structure operators)
function jacobiEigen(Ain) {
  const n = Ain.length;
  const A = Ain.map(row => row.slice());
  for (let sweep = 0; sweep < 200; sweep++) {
    let off = 0;
    for (let p = 0; p < n; p++)
      for (let q = p + 1; q < n; q++) off += A[p][q] * A[p][q];
    if (off < 1e-24) break;
    for (let p = 0; p < n; p++) {
      for (let q = p + 1; q < n; q++) {
        if (Math.abs(A[p][q]) < 1e-15) continue;
        const tau = (A[q][q] - A[p][p]) / (2 * A[p][q]);
        const t = (tau >= 0 ? 1 : -1) / (Math.abs(tau) + Math.sqrt(1 + tau * tau));
        const c = 1 / Math.sqrt(1 + t * t), s = t * c;
        for (let k = 0; k < n; k++) {
          const akp = A[k][p], akq = A[k][q];
          A[k][p] = c * akp - s * akq;
          A[k][q] = s * akp + c * akq;
        }
        for (let k = 0; k < n; k++) {
          const apk = A[p][k], aqk = A[q][k];
          A[p][k] = c * apk - s * aqk;
          A[q][k] = s * apk + c * aqk;
        }
      }
    }
  }
  const eig = [];
  for (let i = 0; i < n; i++) eig.push(A[i][i]);
  return sortAsc(eig);
}

self.onmessage = (e) => {
  const { type, payload } = e.data;
  try {
    if (type === 'stats') {
      const { zeros } = payload;
      const checkpoints = [100, 500, 1000, 2000, 5000, 10000, 20000, 50000];
      const bN = bNConvergence(zeros, checkpoints);
      const ratios = spacingRatios(zeros);
      const ks = gueRatioKS(ratios);
      const rMean = ratios.reduce((a, b) => a + b, 0) / ratios.length;
      const Lvalues = [2, 5, 10, 20, 50, 100, 200, 500, 1000];
      const sig2 = numberVariance(zeros, Lvalues, 3000);
      const d3 = delta3(zeros, [2, 5, 10, 20, 50, 100, 200]);
      self.postMessage({ type: 'stats', ok: true, result: {
        bN, rMean, ks, nRatios: ratios.length, sig2, d3,
        refs: { R_GUE, R_GOE, R_POISSON },
      } });
    } else if (type === 'lab') {
      const { zeros, test } = payload;
      self.postMessage({ type: 'lab', test, ok: true, result: labTest(zeros, test) });
    } else if (type === 'spinor') {
      const { classes, edges, representative } = payload;
      const N = 56;
      const spectra = [];
      const odd = (classes || []).filter(c => c.orbit === 0);
      if (!odd.length || !Array.isArray(edges) || !edges.length) {
        throw new Error('no odd-orbit spinor classes or empty edge list in payload');
      }
      for (const c of odd) {
        if (!Array.isArray(c.signs) || c.signs.length < edges.length) {
          throw new Error(`class ${c.cls}: ${c.signs ? c.signs.length : 0} signs < ${edges.length} edges`);
        }
        const A = [];
        for (let i = 0; i < N; i++) A.push(new Array(N).fill(0));
        edges.forEach(([u, v], k) => {
          A[u][v] = c.signs[k];
          A[v][u] = c.signs[k];
        });
        const w = jacobiEigen(A);
        if (c.cls === representative) spectra.unshift(w);
        else spectra.push(w);
      }
      if (!spectra.length) {
        throw new Error(`representative class ${representative} not found among odd classes`);
      }
      const rep = spectra[0];
      let isomax = 0;
      for (let a = 0; a < spectra.length; a++)
        for (let b = a + 1; b < spectra.length; b++)
          for (let i = 0; i < N; i++)
            isomax = Math.max(isomax, Math.abs(spectra[a][i] - spectra[b][i]));
      const lam = sortAsc(rep.map(Math.abs));
      const dsp = [];
      for (let i = 0; i + 1 < lam.length; i++) {
        const d = lam[i + 1] - lam[i];
        if (d > 1e-8) dsp.push(d);
      }
      const ratios = [];
      for (let i = 0; i + 1 < dsp.length; i++)
        ratios.push(Math.min(dsp[i], dsp[i + 1]) / Math.max(dsp[i], dsp[i + 1]));
      const rMean = ratios.reduce((a, b) => a + b, 0) / ratios.length;
      self.postMessage({ type: 'spinor', ok: true, result: {
        nSpectra: spectra.length, isomax, rMean,
        spectrum: rep, nZero: lam.filter(v => v < 1e-8).length,
      } });
    }
  } catch (err) {
    self.postMessage({ type, ok: false, error: String(err) });
  }
};
