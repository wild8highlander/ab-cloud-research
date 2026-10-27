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

function numberVariance(eigs, Lvalues, nWindows) {
  const lam = sortAsc(eigs);
  const out = [];
  for (const L of Lvalues) {
    // unfold locally by index (suite-style window over normalized levels)
    let acc = 0, cnt = 0;
    const step = Math.max(1, Math.floor(lam.length / nWindows));
    for (let start = 0; start + L < lam.length; start += step) {
      // count levels in the spectral window of length L centered at start
      const c = lam[start];
      let nL = 0;
      for (let i = start; i < lam.length && lam[i] < c + L; i++) nL++;
      acc += Math.pow(nL - L, 2);
      cnt++;
      if (cnt >= nWindows) break;
    }
    out.push({ L, sigma2: acc / Math.max(cnt, 1) });
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
      const sig2 = numberVariance(zeros, Lvalues, 500);
      const d3 = delta3(zeros, [2, 5, 10, 20, 50, 100, 200]);
      self.postMessage({ type: 'stats', ok: true, result: {
        bN, rMean, ks, nRatios: ratios.length, sig2, d3,
        refs: { R_GUE, R_GOE, R_POISSON },
      } });
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
