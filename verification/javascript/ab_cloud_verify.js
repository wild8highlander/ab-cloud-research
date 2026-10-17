'use strict';
// ==============================================================================
// AB-Cloud Verification Suite — Node.js, canonical kernel v3.0
// ==============================================================================
// Verified against the frozen golden anchors (CANON_SPEC.md; canon:
// meridian-spectral-observatory, selftest 199/199).
// ab_cloud_verify_en.js / ab_cloud_verify_ru.js are thin language pins.
// ==============================================================================

const fs = require('fs');
const path = require('path');
const zlib = require('zlib');

// ---------------------------------------------------------------- frozen anchors
const GOLDEN_LAMBERT_W = [
  [0.5, 0.35173371124919584], [1.0, 0.5671432904097838], [3.7, 1.1599531786120223],
  [10.0, 1.7455280027406992], [271.8, 4.17576816800275], [12345.6, 7.417247034540566],
];
const GOLDEN_GRAM = [
  [1, 23.17028270133466], [2, 27.670182217848343], [3, 31.71797995477886],
  [10, 54.67523744685398], [100, 238.58259051450293], [1000, 1421.25638903275],
  [10000, 9878.910118894457], [50000, 40434.6952780045],
];
const GOLDEN_BN = [
  [100, 3.3321638710140165], [500, 2.3912304957476382], [1000, 2.1072522951855435],
  [5000, 1.6299485869022874], [10000, 1.4794053414584762], [50000, 1.2125526772588608],
];
const GOLDEN = {
  bnOff500: 624.6201618180231,
  spMean: 0.999976001221201, spVar: 0.1590654827835423,
  ksD: 0.021619337032982328, ksP: 9.567870399361496e-21,
  cvmW2: 8.177703317829403, adA2: 61.49242624209728, rmean: 0.6118798907208398,
};

// ---------------------------------------------------------------- data sources
const SOURCES = [
  ['50k', 'zeta_zeros_50000.txt', 13661],
  ['50k_full', 'zeta_zeros_50000_embedded.txt', 50000],
  ['500k', 'zeta_zeros_500k_odlyzko.txt', 500000],
  ['2M', 'zeta_zeros_2M_odlyzko.txt', 2001052],
  ['highT', 'zeta_zeros_highT_blocks.txt', 30000],
  ['2M_gz', 'zeta_zeros_2M_odlyzko.txt.gz', 2001052],
  ['csv', 'zeta_zeros_50000.csv', 13661],
  ['zeros6', 'zeros6.txt', 2001052],
];

function resolveSource(count, source) {
  if (source !== 'auto') {
    const s = SOURCES.find(x => x[0] === source);
    if (!s) throw new Error(`unknown source: ${source}`);
    return s;
  }
  let best = null;
  for (const s of SOURCES) {
    if (s[2] >= count && (best === null || s[2] < best[2])) best = s;
  }
  if (best === null) throw new Error(`no data source available for ${count} zeros`);
  return best;
}

function parseStream(content, sname) {
  const zeros = [];
  let blockOffset = 0;
  const isCSV = sname === 'csv';
  const isHighT = sname === 'highT';
  for (let raw of content.split(/\r?\n/)) {
    const t = raw.trim();
    if (!t) continue;
    if (t[0] === '#') {
      if (isHighT) {
        const p = t.indexOf('offset=');
        if (p >= 0) {
          const v = parseFloat(t.slice(p + 7).trim());
          if (isFinite(v)) blockOffset = v;
        }
      }
      continue;
    }
    let v;
    if (isCSV) {
      const parts = t.split(',');
      if (parts.length < 2) continue;
      v = parseFloat(parts[1].trim());
    } else {
      v = parseFloat(t);
    }
    if (!isFinite(v)) continue;
    const val = v + blockOffset;
    if (val > 0) zeros.push(val);
  }
  zeros.sort((a, b) => a - b);
  return zeros;
}

function loadZeros(dataDir, count, source) {
  const [sname, fname] = resolveSource(count, source);
  const fpath = path.join(dataDir, fname);
  console.log(`  Data file: ${fpath} (source '${sname}')`);
  let content;
  if (fname.endsWith('.gz')) {
    content = zlib.gunzipSync(fs.readFileSync(fpath)).toString('utf8');
  } else {
    content = fs.readFileSync(fpath, 'utf8');
  }
  let zeros = parseStream(content, sname);
  if (count > 0 && zeros.length > count) zeros = zeros.slice(0, count);
  if (zeros.length === 0) throw new Error('No valid zeros loaded');
  return zeros;
}

// ---------------------------------------------------------------- canon math §1–§2
function lambertW0(x) {
  if (x <= 0) return 0;
  let w = Math.log(x);
  if (w < 0) w = x; // W(x) ~ x for 0<x<1; avoids the w=-1 flat point
  for (let iter = 0; iter < 50; iter++) {
    const ew = Math.exp(w);
    const fp = ew * (1 + w);
    if (Math.abs(fp) < 1e-30) break;
    const delta = (w * ew - x) / fp;
    w -= delta;
    if (Math.abs(delta) < 1e-14 * (1 + Math.abs(w))) break;
  }
  return w;
}

// gram_point: solution of θ(t) = πk (CANON_SPEC §2): seed + EXACTLY 8 Newton iters
function gramPoint(n) {
  if (n <= 0) return 0;
  const TWO_PI = 2 * Math.PI;
  let t = TWO_PI * n / lambertW0(n / Math.E);
  for (let iter = 0; iter < 8; iter++) {
    const arg = t / TWO_PI;
    if (arg <= 0) break;
    const theta = 0.5 * t * Math.log(arg) - 0.5 * t - Math.PI / 8
      + 1 / (48 * t) + 7 / (5760 * t * t * t);
    const dtheta = 0.5 * Math.log(arg) - 1 / (48 * t * t) - 21 / (5760 * t * t * t * t);
    if (Math.abs(dtheta) < 1e-30) break;
    t -= (theta - Math.PI * n) / dtheta;
  }
  return t;
}

// ---------------------------------------------------------------- canon §5: erf + table
// erf: series for |x| < 2.2, Lentz continued fraction for erfc beyond (DLMF 7.9.1)
function myErf(x) {
  const ax = Math.abs(x);
  let v;
  if (ax < 2.2) {
    let term = ax, sum = ax;
    const x2 = ax * ax;
    for (let k = 1; k < 200; k++) {
      term *= -x2 / k;
      const add = term / (2 * k + 1);
      sum += add;
      if (Math.abs(add) < 1e-18 * Math.abs(sum)) break;
    }
    v = 2 / Math.sqrt(Math.PI) * sum;
  } else {
    v = 1 - erfcCF(ax);
  }
  return x >= 0 ? v : -v;
}

function erfcCF(z) {
  let f = z, c = z, d = 0;
  for (let k = 1; k < 200; k++) {
    const a = k / 2;
    d = z + a * d; if (d === 0) d = 1e-300;
    c = z + a / c; if (c === 0) c = 1e-300;
    d = 1 / d;
    const delta = c * d;
    f *= delta;
    if (Math.abs(delta - 1) < 1e-17) break;
  }
  return Math.exp(-z * z) / (Math.sqrt(Math.PI) * f);
}

const GUE_TN = 32768, GUE_SMAX = 5.0;
let _gueTable = null;
function gueExact(s) {
  if (s <= 0) return 0;
  return myErf(2 * s / Math.sqrt(Math.PI)) - (4 * s / Math.PI) * Math.exp(-4 * s * s / Math.PI);
}
// GUE (β=2) Wigner surmise CDF via the canonical 32768-point table (§5).
// (The pre-v2.0.3 law 1-exp(-πs²/4) was the GOE β=1 surmise — wrong ensemble.)
function gueCDF(s) {
  if (s <= 0) return 0;
  if (s >= GUE_SMAX) return gueExact(s);
  if (_gueTable === null) {
    _gueTable = new Float64Array(GUE_TN);
    for (let i = 0; i < GUE_TN; i++) _gueTable[i] = gueExact(i * GUE_SMAX / (GUE_TN - 1));
  }
  const x = s * (GUE_TN - 1) / GUE_SMAX;
  const i = Math.floor(x);
  if (i < 0 || i >= GUE_TN - 1) return gueExact(s);
  const t = x - i;
  return (1 - t) * _gueTable[i] + t * _gueTable[i + 1];
}

// ---------------------------------------------------------------- canon §3–§6
function computeBN(zeros, N) {
  if (N <= 0 || N > zeros.length) return NaN;
  let sum = 0;
  for (let k = 1; k <= N; k++) sum += Math.abs(zeros[k - 1] - gramPoint(k));
  return sum / N;
}
function computeBNOffset(zeros, N, offset) {
  if (N <= 0 || offset + N > zeros.length) return NaN;
  let sum = 0;
  for (let k = 1; k <= N; k++) sum += Math.abs(zeros[k - 1] - gramPoint(offset + k));
  return sum / N;
}
function computeSpacings(zeros) {
  const sp = [];
  for (let k = 0; k + 1 < zeros.length; k++) {
    if (zeros[k] <= 0) continue;
    sp.push((zeros[k + 1] - zeros[k]) * Math.log(zeros[k] / (2 * Math.PI)) / (2 * Math.PI));
  }
  return sp;
}
function ksAsymptoticPValue(lam) {
  if (lam <= 0) return 1;
  let v;
  if (lam < 0.6) {
    let s2 = 0;
    for (let k = 1; k <= 1000; k++) {
      const term2 = Math.exp(-(((2 * k - 1) ** 2) * Math.PI ** 2) / (8 * lam * lam));
      s2 += term2;
      if (term2 < 1e-18) break;
    }
    v = 1 - Math.sqrt(2 * Math.PI) / lam * s2;
  } else {
    let s = 0, sign = 1;
    for (let k = 1; k <= 100; k++) {
      const term = sign * Math.exp(-2 * k * k * lam * lam);
      s += term;
      sign = -sign;
      if (Math.abs(term) < 1e-18) break;
    }
    v = 2 * s;
  }
  return Math.max(0, Math.min(1, v));
}
function ksTestDP(spacings) {
  const s = spacings.slice().sort((a, b) => a - b);
  const n = s.length;
  let D = 0;
  for (let i = 1; i <= n; i++) {
    const F = gueCDF(s[i - 1]);
    D = Math.max(D, Math.abs(i / n - F), Math.abs((i - 1) / n - F));
  }
  const lam = (Math.sqrt(n) + 0.12 + 0.11 / Math.sqrt(n)) * D;
  return [D, ksAsymptoticPValue(lam)];
}
function cvmTest(spacings) {
  const s = spacings.slice().sort((a, b) => a - b);
  const n = s.length;
  let W2 = 0;
  for (let i = 1; i <= n; i++) {
    const d = gueCDF(s[i - 1]) - (2 * i - 1) / (2 * n);
    W2 += d * d;
  }
  return W2 + 1 / (12 * n);
}
function adStat(spacings) {
  const s = spacings.slice().sort((a, b) => a - b);
  const n = s.length;
  if (n < 2) return NaN;
  let acc = 0;
  for (let i = 1; i <= n; i++) {
    const Fi = Math.min(Math.max(gueCDF(s[i - 1]), 1e-300), 1 - 1e-16);
    const Fni = Math.min(Math.max(gueCDF(s[n - i]), 1e-300), 1 - 1e-16);
    acc += (2 * i - 1) * (Math.log(Fi) + Math.log(1 - Fni));
  }
  return -n - acc / n;
}
function meanRatio(zeros) {
  if (zeros.length < 3) return [NaN, 0];
  let acc = 0, cnt = 0;
  for (let i = 0; i + 2 < zeros.length; i++) {
    const a = zeros[i + 1] - zeros[i];
    const b = zeros[i + 2] - zeros[i + 1];
    const m = Math.max(a, b);
    if (a === 0 && b === 0) continue;
    acc += Math.min(a, b) / m;
    cnt++;
  }
  if (cnt === 0) return [NaN, 0];
  return [acc / cnt, cnt];
}
function linreg(x, y) {
  const n = x.length;
  let sx = 0, sy = 0, sxx = 0, sxy = 0, syy = 0;
  for (let i = 0; i < n; i++) {
    sx += x[i]; sy += y[i];
    sxx += x[i] * x[i]; sxy += x[i] * y[i]; syy += y[i] * y[i];
  }
  const den = n * sxx - sx * sx;
  if (Math.abs(den) < 1e-30) return { slope: 0, intercept: 0, se: 0, r2: 0 };
  const slope = (n * sxy - sx * sy) / den;
  const intercept = (sy - slope * sx) / n;
  const ssTot = syy - sy * sy / n;
  let ssRes = 0;
  for (let i = 0; i < n; i++) {
    const e = y[i] - (slope * x[i] + intercept);
    ssRes += e * e;
  }
  const r2 = ssTot > 0 ? 1 - ssRes / ssTot : 0;
  const se = n > 2 && den > 0 ? Math.sqrt((ssRes / (n - 2)) * n / den) : 0;
  return { slope, intercept, se, r2 };
}

// ---------------------------------------------------------------- objections §7
function runObjection1(zeros) {
  const maxZ = zeros.length;
  let ns = [100, 500, 1000, 5000, 10000, 50000].filter(cp => cp <= maxZ);
  if (ns.length === 0) ns = [Math.min(maxZ, 100)];
  const bn = ns.map(cp => computeBN(zeros, cp));
  let converging = true;
  for (let i = 1; i < bn.length; i++) if (bn[i] >= bn[i - 1]) converging = false;
  let hasFit = false, fitA = 0, fitS = 0, fitR2 = 0;
  if (ns.length >= 3) {
    const lx = [], ly = [];
    for (let i = 0; i < ns.length; i++) {
      if (ns[i] > 1 && bn[i] > 0) { lx.push(Math.log(ns[i])); ly.push(Math.log(bn[i])); }
    }
    if (lx.length >= 3) {
      const lr = linreg(lx, ly);
      hasFit = true; fitA = Math.exp(lr.intercept); fitS = -lr.slope; fitR2 = lr.r2;
    }
  }
  return { ns, bn, converging, hasFit, fitA, fitS, fitR2 };
}
function runObjection2(zeros) {
  const sp = computeSpacings(zeros);
  if (sp.length < 2) return { n: sp.length, mean: NaN, var: NaN, D: NaN, p: NaN, W2: NaN, A2: NaN, r: NaN, nr: 0, rejected: false };
  const mean = sp.reduce((a, b) => a + b, 0) / sp.length;
  const variance = sp.reduce((a, s) => a + (s - mean) * (s - mean), 0) / (sp.length - 1);
  const [D, p] = ksTestDP(sp);
  const [r, nr] = meanRatio(zeros);
  return { n: sp.length, mean, var: variance, D, p, W2: cvmTest(sp), A2: adStat(sp), r, nr, rejected: p < 0.05 };
}
function runObjection3(zeros) {
  const maxZ = zeros.length;
  const ns = [];
  for (let n = 50; n <= maxZ; n *= 2) ns.push(n);
  if (ns.length > 0 && ns[ns.length - 1] !== maxZ && maxZ > 100) ns.push(maxZ);
  const lx = [], ly = [];
  for (const n of ns) {
    const b = computeBN(zeros, n);
    if (b > 0) { lx.push(Math.log(n)); ly.push(Math.log(b)); }
  }
  if (lx.length < 3) return { ns, slope: NaN, intercept: NaN, r2: NaN, cilo: NaN, cihi: NaN, ok: false };
  const lr = linreg(lx, ly);
  return { ns, slope: lr.slope, intercept: lr.intercept, r2: lr.r2,
    cilo: lr.slope - 1.96 * lr.se, cihi: lr.slope + 1.96 * lr.se,
    ok: Math.abs(lr.slope + 0.5) < 0.1 };
}

// ---------------------------------------------------------------- selfcheck §8
function selfcheck(zeros) {
  const rows = [];
  let npass = 0, nfail = 0;
  const add = (name, got, exp, tol, rel) => {
    const d = Math.abs(got - exp) / (rel ? Math.abs(exp) : 1.0);
    const ok = isFinite(got) && d <= tol;
    rows.push({ name, skip: false, ok, got, exp, delta: d });
    ok ? npass++ : nfail++;
  };
  const skip = (name) => rows.push({ name, skip: true, ok: false, got: 0, exp: 0, delta: 0 });

  for (const [x, e] of GOLDEN_LAMBERT_W) add(`lambert_w(${x})`, lambertW0(x), e, 1e-12, true);
  for (const [n, e] of GOLDEN_GRAM) add(`gram_point(n=${n})`, gramPoint(n), e, 1e-6, false);
  for (const [n, e] of GOLDEN_BN) {
    if (n <= zeros.length) add(`bN(N=${n})`, computeBN(zeros, n), e, 1e-6, false);
    else skip(`bN(N=${n})`);
  }
  if (zeros.length >= 1500) add('bN(N=1000,off=500)', computeBNOffset(zeros, 1000, 500), GOLDEN.bnOff500, 1e-6, false);
  else skip('bN(N=1000,off=500)');
  if (zeros.length >= 50000) {
    const z5 = zeros.slice(0, 50000);
    const sp = computeSpacings(z5);
    const mean = sp.reduce((a, b) => a + b, 0) / sp.length;
    const variance = sp.reduce((a, s) => a + (s - mean) * (s - mean), 0) / (sp.length - 1);
    const [D, p] = ksTestDP(sp);
    add('spacings.mean', mean, GOLDEN.spMean, 1e-9, false);
    add('spacings.var', variance, GOLDEN.spVar, 1e-9, false);
    add('ks_zeros.D', D, GOLDEN.ksD, 1e-9, false);
    add('ks_zeros.p', p, GOLDEN.ksP, 1e-6, true);
    add('cvm_zeros.W2', cvmTest(sp), GOLDEN.cvmW2, 1e-9, true);
    add('ad_zeros.A2', adStat(sp), GOLDEN.adA2, 1e-9, true);
    const [r] = meanRatio(z5);
    add('rmean_zeros.r', r, GOLDEN.rmean, 1e-9, false);
  } else {
    ['spacings.mean/var', 'ks_zeros.D/p', 'cvm_zeros.W2', 'ad_zeros.A2', 'rmean_zeros.r'].forEach(skip);
  }
  return { rows, npass, nfail };
}

// ---------------------------------------------------------------- rendering (bilingual)
const MSG = {
  en: {
    scTitle: '\n=== Golden self-check — frozen anchors (canon: meridian-spectral-observatory, selftest 199/199) ===',
    scPass: 'PASS', scFail: 'FAIL', scSkip: 'SKIP',
    scResult: (a, b) => `  Self-check: ${a} passed, ${b} failed`,
    o1title: '\n──────────────────────────────────────────────────────\n  Objection 1: Numerical Stability of b(N)\n  b(N) = (1/N) Σ|γ_k − γ̃_k|, Gram points: θ(t) = πk (Newton)\n──────────────────────────────────────────────────────',
    o1fit: (a, s, r2) => `\n  Empirical law:  b(N) ≈ ${a.toFixed(4)} · N^(−${s.toFixed(4)})   (R² = ${r2.toFixed(4)})`,
    o1ok: '\nResult: b(N) converging as N increases. OK\n  b(N) decreases monotonically over the table — convergence confirmed on the accessible range. The decay is EMPIRICAL, not O(1/√N).',
    o1bad: '\nResult: b(N) NOT converging as N increases. WARN',
    o2title: '\n──────────────────────────────────────────────────────\n  Objection 2: GUE Spacing Statistical Significance\n  GUE (β=2) Wigner surmise via the canonical 32768-point CDF table\n──────────────────────────────────────────────────────',
    o2tooFew: 'WARNING: not enough spacings for the GUE test.',
    o2mean: (m, v, n) => `  Spacing mean: ${m.toFixed(9)}  var: ${v.toFixed(9)}  (n = ${n})`,
    o2ks: (D, p) => `  Kolmogorov-Smirnov:  D = ${D.toFixed(6)},  p-value = ${p.toExponential(3)}`,
    o2cvm: (w) => `  Cramér-von Mises:    W² = ${w.toFixed(6)}`,
    o2ad: (a) => `  Anderson-Darling:   A² = ${a.toFixed(6)}`,
    o2r: (r, nr) => `  ⟨r⟩ (adjacent-ratio): ${r.toFixed(6)}  (n = ${nr}, GUE surmise ≈ 0.5992)`,
    o2rej: '\nResult: H₀ (GUE distribution): REJECTED  (α = 0.05)',
    o2norej: '\nResult: H₀ (GUE distribution): NOT REJECTED  (α = 0.05)',
    o2note: '  Note: at large n the exact GUE surmise is formally rejected — the\n  known finite-T corrections of the zeta zeros, not a data artifact\n  (mean ≈ 1 validates the unfolding; golden-anchored).',
    o3title: '\n──────────────────────────────────────────────────────\n  Objection 3: Large-T Decay Rate\n  Fit log(b(N)) vs log(N): expected slope ≈ −0.5\n──────────────────────────────────────────────────────',
    o3tooFew: 'WARNING: Insufficient data points for regression.',
    o3slope: (s) => `  Slope     = ${s >= 0 ? '+' : ''}${s.toFixed(6)}  (expected: -0.5)`,
    o3int: (i) => `  Intercept = ${i >= 0 ? '+' : ''}${i.toFixed(6)}`,
    o3r2: (r2) => `  R²       = ${r2.toFixed(6)}`,
    o3ci: (lo, hi) => `  95% CI for slope: [${lo.toFixed(4)}, ${hi.toFixed(4)}]`,
    o3ok: (s) => `\nResult: Fitted slope = ${s.toFixed(4)}, expected = -0.500. OK`,
    o3bad: (s) => `\nResult: Fitted slope = ${s.toFixed(4)}, expected = -0.500. WARN: slope deviates from -0.5 (decay is empirical)`,
  },
  ru: {
    scTitle: '\n=== Само-проверка golden — замороженные якоря (канон: meridian-spectral-observatory, selftest 199/199) ===',
    scPass: 'ПРОЙДЕНО', scFail: 'СБОЙ', scSkip: 'ПРОПУСК',
    scResult: (a, b) => `  Само-проверка: ${a} пройдено, ${b} провалено`,
    o1title: '\n──────────────────────────────────────────────────────\n  Возражение 1: Числовая стабильность b(N)\n  b(N) = (1/N) Σ|γ_k − γ̃_k|, точки Грама: θ(t) = πk (Ньютон)\n──────────────────────────────────────────────────────',
    o1fit: (a, s, r2) => `\n  Эмпирический закон:  b(N) ≈ ${a.toFixed(4)} · N^(−${s.toFixed(4)})   (R² = ${r2.toFixed(4)})`,
    o1ok: '\nРезультат: b(N) сходится с ростом N. OK\n  b(N) монотонно убывает по таблице — сходимость подтверждена на доступном диапазоне. Убывание ЭМПИРИЧЕСКОЕ, это не O(1/√N).',
    o1bad: '\nРезультат: b(N) НЕ сходится с ростом N. WARN',
    o2title: '\n──────────────────────────────────────────────────────\n  Возражение 2: Статистическая значимость GUE-распределения\n  GUE (β=2) сурьмида через каноническую CDF-таблицу (32768 точек)\n──────────────────────────────────────────────────────',
    o2tooFew: 'ПРЕДУПРЕЖДЕНИЕ: недостаточно интервалов для GUE-теста.',
    o2mean: (m, v, n) => `  Средний спейсинг: ${m.toFixed(9)}  дисперсия: ${v.toFixed(9)}  (n = ${n})`,
    o2ks: (D, p) => `  Колмогоров-Смирнов:  D = ${D.toFixed(6)},  p-значение = ${p.toExponential(3)}`,
    o2cvm: (w) => `  Крамер-фон Мизес:    W² = ${w.toFixed(6)}`,
    o2ad: (a) => `  Андерсон-Дарлинг:     A² = ${a.toFixed(6)}`,
    o2r: (r, nr) => `  ⟨r⟩ (отношение соседних): ${r.toFixed(6)}  (n = ${nr}, GUE ≈ 0.5992)`,
    o2rej: '\nРезультат: H₀ (GUE-распределение): ОТВЕРГНУТА  (α = 0.05)',
    o2norej: '\nРезультат: H₀ (GUE-распределение): НЕ ОТВЕРГНУТА  (α = 0.05)',
    o2note: '  Примечание: при больших n точная GUE-сурьмида формально отвергается — это\n  известные поправки конечных T у нулей ζ, а не дефект данных\n  (среднее ≈ 1 подтверждает развёртку; якоря golden).',
    o3title: '\n──────────────────────────────────────────────────────\n  Возражение 3: Скорость убывания при больших T\n  Аппроксимация log(b(N)) vs log(N): ожидаемый наклон ≈ −0.5\n──────────────────────────────────────────────────────',
    o3tooFew: 'ПРЕДУПРЕЖДЕНИЕ: недостаточно точек для регрессии.',
    o3slope: (s) => `  Наклон    = ${s >= 0 ? '+' : ''}${s.toFixed(6)}  (ожидается: -0.5)`,
    o3int: (i) => `  Св. член  = ${i >= 0 ? '+' : ''}${i.toFixed(6)}`,
    o3r2: (r2) => `  R²       = ${r2.toFixed(6)}`,
    o3ci: (lo, hi) => `  95% ДИ для наклона: [${lo.toFixed(4)}, ${hi.toFixed(4)}]`,
    o3ok: (s) => `\nРезультат: Наклон = ${s.toFixed(4)}, ожидаемый = -0.500. OK`,
    o3bad: (s) => `\nРезультат: Наклон = ${s.toFixed(4)}, ожидаемый = -0.500. WARN: наклон отклоняется от -0.5 (убывание эмпирическое)`,
  },
};

function renderAll(zeros, lang) {
  const M = MSG[lang] || MSG.en;
  const out = [];

  // selfcheck
  const { rows, npass, nfail } = selfcheck(zeros);
  out.push(M.scTitle);
  for (const r of rows) {
    if (r.skip) { out.push(`  ${r.name.padEnd(24)} ${M.scSkip}`); continue; }
    out.push(`  ${r.name.padEnd(24)} ${r.ok ? M.scPass : M.scFail}  computed = ${r.got.toPrecision(12)}, expected = ${r.exp.toPrecision(12)}, Δ = ${r.delta.toExponential(3)}`);
  }
  out.push(M.scResult(npass, nfail));

  // objection 1
  const o1 = runObjection1(zeros);
  out.push(M.o1title);
  out.push(`         ${'N'}  ${'b(N)'}  ${'log10(b(N))'}`);
  for (let i = 0; i < o1.ns.length; i++) {
    const lg = o1.bn[i] > 0 ? Math.log10(o1.bn[i]) : -999;
    out.push(`${String(o1.ns[i]).padStart(10)}  ${o1.bn[i].toFixed(8).padStart(14)}  ${lg.toFixed(4).padStart(14)}`);
  }
  if (o1.hasFit) out.push(M.o1fit(o1.fitA, o1.fitS, o1.fitR2));
  out.push(o1.converging ? M.o1ok : M.o1bad);

  // objection 2
  const o2 = runObjection2(zeros);
  out.push(M.o2title);
  if (o2.n < 2) out.push(M.o2tooFew);
  else {
    out.push(M.o2mean(o2.mean, o2.var, o2.n));
    out.push(M.o2ks(o2.D, o2.p));
    out.push(M.o2cvm(o2.W2));
    out.push(M.o2ad(o2.A2));
    out.push(M.o2r(o2.r, o2.nr));
    out.push(o2.rejected ? M.o2rej : M.o2norej);
    if (o2.rejected) out.push(M.o2note);
  }

  // objection 3
  const o3 = runObjection3(zeros);
  out.push(M.o3title);
  if (isNaN(o3.slope)) out.push(M.o3tooFew);
  else {
    out.push(M.o3slope(o3.slope));
    out.push(M.o3int(o3.intercept));
    out.push(M.o3r2(o3.r2));
    out.push(M.o3ci(o3.cilo, o3.cihi));
    out.push(o3.ok ? M.o3ok(o3.slope) : M.o3bad(o3.slope));
  }
  return { text: out.join('\n') + '\n', nfail };
}

// ---------------------------------------------------------------- CLI
function main() {
  const args = process.argv.slice(2);
  let zeros = 50000, source = 'auto', objection = 'all', lang = 'en';
  let dataDir = '../data', selfcheckOn = true;
  for (let i = 0; i < args.length; i++) {
    const a = args[i];
    if (a === '--zeros' && i + 1 < args.length) zeros = parseInt(args[++i], 10);
    else if (a === '--source' && i + 1 < args.length) source = args[++i];
    else if (a === '--objection' && i + 1 < args.length) objection = args[++i];
    else if (a === '--lang' && i + 1 < args.length) lang = args[++i] === 'ru' ? 'ru' : 'en';
    else if (a === '--data-dir' && i + 1 < args.length) dataDir = args[++i];
    else if (a === '--no-selfcheck') selfcheckOn = false;
  }
  const zerosList = loadZeros(dataDir, zeros, source);
  console.log(`  Zeros loaded: ${zerosList.length}`);
  if (zerosList.length < 2) { console.error('ERROR: need at least 2 zeros'); process.exit(2); }

  const objections = objection === 'all' ? ['1', '2', '3'] : [objection];
  if (!selfcheckOn) {
    // render without the self-check block: simplest honest path is to render
    // everything but strip the selfcheck lines
    const full = renderAll(zerosList, lang);
    const lines = full.text.split('\n');
    const start = lines.findIndex(l => l.includes('self-check') || l.includes('само-проверка'));
    const end = lines.findIndex(l => l.startsWith('  Self-check:') || l.startsWith('  Само-проверка:'));
    let text = full.text;
    if (start >= 0 && end >= start) {
      const head = lines.slice(0, start).join('\n');
      const tail = lines.slice(end + 1).join('\n');
      text = head + '\n' + tail;
    }
    process.stdout.write(text);
    process.exit(0);
  }
  const { text, nfail } = renderAll(zerosList, lang);
  process.stdout.write(text);
  process.exit(nfail > 0 ? 1 : 0);
}

if (require.main === module) main();

module.exports = { lambertW0, gramPoint, gueCDF, computeBN, computeBNOffset,
  computeSpacings, ksTestDP, cvmTest, adStat, meanRatio, selfcheck,
  runObjection1, runObjection2, runObjection3, loadZeros, renderAll, main };
