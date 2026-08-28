// ==============================================================================
// AB-Cloud Verification Suite — JavaScript/Node.js (Bilingual: EN/RU)
// ==============================================================================
// Verifies three key objections against Riemann zeta zero data:
//   Objection 1: b(N) convergence  (Gram-point deviation via Lambert W)
//   Objection 2: GUE spacing KS test
//   Objection 3: Large-T decay slope ≈ -0.5
//
// Node.js 18+ required. Uses fs, readline, zlib (for .gz streams).
// ==============================================================================

'use strict';

const fs = require('fs');
const path = require('path');
const readline = require('readline');
const zlib = require('zlib');

// ==============================================================================
// Bilingual message tables
// ==============================================================================

const MSG = {
  en: {
    header:       'AB-Cloud Verification Suite — JavaScript/Node.js',
    separator:    '──────────────────────────────────────────────────────',
    loading:      'Loading zeros from: %s',
    loaded:       'Loaded %d zeros from %s',
    obj1_title:   'Objection 1: b(N) Convergence',
    obj1_desc:    'b(N) = (1/N) * Σ|γ_k - γ̃_k|, Gram points via Lambert W',
    obj1_n:       'N',
    obj1_bN:      'b(N)',
    obj1_status:  'Status',
    obj1_converge:'CONVERGING — b(N) → 0 supports AB-Cloud',
    obj1_stable:  'STABLE — b(N) near zero, AB-Cloud consistent',
    obj1_diverge: 'DIVERGING — b(N) not → 0, objection upheld',
    obj2_title:   'Objection 2: GUE Spacing KS Test',
    obj2_desc:    's_k = (γ_{k+1}-γ_k)·log(γ_k/2π)/(2π), vs p(s)=(πs/2)·exp(-πs²/4)',
    obj2_stat:    'D-statistic',
    obj2_pval:    'p-value',
    obj2_result:  'Result',
    obj2_pass:    'PASS — GUE spacing confirmed (p > 0.05)',
    obj2_fail:    'FAIL — GUE spacing rejected (p ≤ 0.05)',
    obj3_title:   'Objection 3: Large-T Decay Slope',
    obj3_desc:    'Linear regression of log|γ_k - γ̃_k| vs log(γ_k), expect slope ≈ -0.5',
    obj3_slope:   'Slope',
    obj3_stderr:  'Std Error',
    obj3_target:  'Target',
    obj3_result:  'Result',
    obj3_pass:    'PASS — Slope ≈ -0.5, AB-Cloud decay confirmed',
    obj3_fail:    'FAIL — Slope deviates from -0.5',
    no_data:      'ERROR: No zeros loaded. Check data directory.',
    done:         'Verification complete.',
  },
  ru: {
    header:       'Комплекс проверки AB-Cloud — JavaScript/Node.js',
    separator:    '──────────────────────────────────────────────────────',
    loading:      'Загрузка нулей из: %s',
    loaded:       'Загружено %d нулей из %s',
    obj1_title:   'Возражение 1: Сходимость b(N)',
    obj1_desc:    'b(N) = (1/N) * Σ|γ_k - γ̃_k|, точки Грама через W Ламберта',
    obj1_n:       'N',
    obj1_bN:      'b(N)',
    obj1_status:  'Статус',
    obj1_converge:'СХОДИТСЯ — b(N) → 0 подтверждает AB-Cloud',
    obj1_stable:  'СТАБИЛЬНО — b(N) ≈ 0, AB-Cloud согласуется',
    obj1_diverge: 'РАСХОДИТСЯ — b(N) ↛ 0, возражение подтверждено',
    obj2_title:   'Возражение 2: KS-тест интервалов GUE',
    obj2_desc:    's_k = (γ_{k+1}-γ_k)·log(γ_k/2π)/(2π), сравн. с p(s)=(πs/2)·exp(-πs²/4)',
    obj2_stat:    'D-статистика',
    obj2_pval:    'p-значение',
    obj2_result:  'Результат',
    obj2_pass:    'ПРОЙДЕНО — интервалы GUE подтверждены (p > 0.05)',
    obj2_fail:    'НЕ ПРОЙДЕНО — интервалы GUE отклонены (p ≤ 0.05)',
    obj3_title:   'Возражение 3: Наклон убывания при больших T',
    obj3_desc:    'Регрессия log|γ_k - γ̃_k| от log(γ_k), ожид. наклон ≈ -0.5',
    obj3_slope:   'Наклон',
    obj3_stderr:  'Стд. ошибка',
    obj3_target:  'Цель',
    obj3_result:  'Результат',
    obj3_pass:    'ПРОЙДЕНО — Наклон ≈ -0.5, убывание AB-Cloud подтверждено',
    obj3_fail:    'НЕ ПРОЙДЕНО — Наклон отклоняется от -0.5',
    no_data:      'ОШИБКА: Нули не загружены. Проверьте каталог данных.',
    done:         'Проверка завершена.',
  },
};

// ==============================================================================
// Lambert W (principal branch) — Halley's method
// ==============================================================================

function lambertW0(x) {
  if (x === 0) return 0;
  let w = x > 1 ? Math.log(x) - Math.log(Math.log(x)) : x;
  for (let iter = 0; iter < 50; iter++) {
    const ew  = Math.exp(w);
    const f   = w * ew - x;
    const fp  = ew * (1 + w);
    const fpp = ew * (2 + w);
    w -= (2 * f * fp) / (2 * fp * fp - f * fpp);
    if (Math.abs(f) < 1e-12 * Math.abs(x + 1)) break;
  }
  return w;
}

// ==============================================================================
// Gram point via Lambert W with Newton refinement
// ==============================================================================

function gramPoint(n) {
  if (n <= 0) return 0;
  const TWO_PI = 2 * Math.PI;
  let g = TWO_PI * n / lambertW0(n / Math.E);
  // Newton refinement using exact θ(t)
  for (let iter = 0; iter < 3; iter++) {
    const theta  = 0.5 * g * Math.log(g / TWO_PI) - 0.5 * g - Math.PI / 8;
    const dtheta = 0.5 * Math.log(g / TWO_PI);
    g += (Math.PI * n - theta) / dtheta;
  }
  return g;
}

function gramPointsVec(nVec) {
  return nVec.map(n => gramPoint(n));
}

// ==============================================================================
// GUE spacing CDF (Wigner surmise)
// ==============================================================================

function gueCDF(s) {
  return 1 - Math.exp(-Math.PI * s * s / 4);
}

// ==============================================================================
// Load zeros from data files (async, streaming)
// ==============================================================================

const FILE_MAP = {
  zeta_zeros_50000:     'zeta_zeros_50000.txt',
  zeta_zeros_500k:      'zeta_zeros_500k_odlyzko.txt',
  zeta_zeros_2M:        'zeta_zeros_2M_odlyzko.txt',
  zeta_zeros_highT:     'zeta_zeros_highT_blocks.txt',
  zeros6:               'zeros6.txt',
  zeta_zeros_50000_csv: 'zeta_zeros_50000.csv',
};

async function loadZeros(dataDir, count = 0, source = 'auto') {
  let selectedFile = null;
  let selectedName = null;

  if (source !== 'auto' && FILE_MAP[source]) {
    selectedFile = path.join(dataDir, FILE_MAP[source]);
    selectedName = source;
  } else {
    // Auto-select: pick first available, prefer small file for small counts
    const order = Object.keys(FILE_MAP);
    for (const nm of order) {
      const fp = path.join(dataDir, FILE_MAP[nm]);
      if (fs.existsSync(fp)) {
        selectedFile = fp;
        selectedName = nm;
        if (count > 0 && count <= 50000 && nm === 'zeta_zeros_50000') break;
      }
    }
  }

  if (!selectedFile || !fs.existsSync(selectedFile)) {
    throw new Error(`No data file found in: ${dataDir}`);
  }

  console.log(`Loading zeros from: ${selectedFile}`);

  const zeros = [];
  const ext = path.extname(selectedFile).toLowerCase();
  const isGz = selectedFile.endsWith('.gz');
  const isCsv = ext === '.csv';

  // Create read stream (handle .gz via zlib)
  let stream = fs.createReadStream(selectedFile, { encoding: 'utf8' });
  if (isGz) {
    stream = fs.createReadStream(selectedFile).pipe(zlib.createGunzip()).setEncoding('utf8');
  }

  const rl = readline.createInterface({ input: stream, crlfDelay: Infinity });

  let lineNumber = 0;
  for await (const line of rl) {
    lineNumber++;
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) continue;

    if (isCsv) {
      // CSV: split by comma, take first column
      const parts = trimmed.split(',');
      const val = parseFloat(parts[0]);
      if (!isNaN(val) && isFinite(val)) zeros.push(val);
    } else {
      // TXT: parse all floats on the line (handles whitespace-prefixed)
      const tokens = trimmed.split(/\s+/).filter(t => t.length > 0);
      for (const tok of tokens) {
        const val = parseFloat(tok);
        if (!isNaN(val) && isFinite(val)) zeros.push(val);
      }
    }

    // Early exit if count specified
    if (count > 0 && zeros.length >= count) {
      rl.close();
      break;
    }
  }

  // Trim to exact count
  if (count > 0 && zeros.length > count) zeros.length = count;

  console.log(`Loaded ${zeros.length} zeros from ${path.basename(selectedFile)}`);
  return zeros;
}

// ==============================================================================
// Objection 1: b(N) Convergence
// ==============================================================================

function objection1(zeros, M) {
  const N = zeros.length;
  console.log(`\n${M.separator}`);
  console.log(M.obj1_title);
  console.log(M.obj1_desc);
  console.log(M.separator);

  const checkpoints = [100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
    .filter(cp => cp <= N);

  const results = [];
  let prevBN = NaN;

  console.log(`\n${padR(M.obj1_n, 10)}  ${padR(M.obj1_bN, 14)}  ${padR(M.obj1_status, 8)}`);
  console.log(`${padR('──────────', 10)}  ${padR('──────────────', 14)}  ${padR('────────', 8)}`);

  for (const cp of checkpoints) {
    const idx = Array.from({ length: cp }, (_, i) => i + 1);
    const gram = gramPointsVec(idx);
    let sum = 0;
    for (let i = 0; i < cp; i++) sum += Math.abs(zeros[i] - gram[i]);
    const bN = sum / cp;

    let status;
    if (isNaN(prevBN)) status = '—';
    else if (bN < prevBN * 1.05) status = '↓';
    else status = '↑';

    console.log(`${padL(cp, 10)}  ${padL(bN.toFixed(8), 14)}  ${padR(status, 8)}`);
    results.push({ N: cp, bN, status });
    prevBN = bN;
  }

  const finalBN = results[results.length - 1].bN;
  let verdict;
  if (finalBN < 0.01) verdict = M.obj1_converge;
  else if (finalBN < 0.5) verdict = M.obj1_stable;
  else verdict = M.obj1_diverge;

  console.log(`\n${verdict}`);
  return results;
}

// ==============================================================================
// Objection 2: GUE Spacing KS Test
// ==============================================================================

function objection2(zeros, M) {
  const N = zeros.length;
  console.log(`\n${M.separator}`);
  console.log(M.obj2_title);
  console.log(M.obj2_desc);
  console.log(M.separator);

  // Compute normalized spacings
  const spacings = [];
  for (let k = 0; k < N - 1; k++) {
    const delta = zeros[k + 1] - zeros[k];
    const logFac = Math.log(zeros[k] / (2 * Math.PI)) / (2 * Math.PI);
    const s = delta * logFac;
    if (isFinite(s) && s > 0) spacings.push(s);
  }

  // Sort for empirical CDF
  spacings.sort((a, b) => a - b);
  const n = spacings.length;

  // KS test: max |F_emp(s) - F_GUE(s)|
  let Dplus = 0, Dminus = 0;
  for (let i = 0; i < n; i++) {
    const empVal = (i + 1) / n;
    const empPrev = i / n;
    const gueVal = gueCDF(spacings[i]);
    Dplus  = Math.max(Dplus, empVal - gueVal);
    Dminus = Math.max(Dminus, gueVal - empPrev);
  }
  const D = Math.max(Dplus, Dminus);

  // Kolmogorov p-value approximation
  const lambda = (Math.sqrt(n) + 0.12 + 0.11 / Math.sqrt(n)) * D;
  let pVal = 0;
  for (let k = -5; k <= 5; k++) {
    pVal += Math.pow(-1, k) * Math.exp(-2 * k * k * lambda * lambda);
  }
  pVal = Math.max(0, Math.min(1, pVal));

  console.log(`\n${padR(M.obj2_stat + ':', 18)} ${D.toFixed(8)}`);
  console.log(`${padR(M.obj2_pval + ':', 18)} ${pVal.toExponential(6)}`);

  const verdict = pVal > 0.05 ? M.obj2_pass : M.obj2_fail;
  console.log(`\n${verdict}`);
  return { D, pValue: pVal };
}

// ==============================================================================
// Objection 3: Large-T Decay Slope
// ==============================================================================

function objection3(zeros, M) {
  const N = zeros.length;
  console.log(`\n${M.separator}`);
  console.log(M.obj3_title);
  console.log(M.obj3_desc);
  console.log(M.separator);

  // Use upper half of data (large T region)
  const start = Math.max(1, Math.floor(N * 0.5));
  const idx = [];
  for (let i = start; i <= N; i++) idx.push(i);

  const gram = gramPointsVec(idx);
  const logGamma = [];
  const logDev = [];

  for (let i = 0; i < idx.length; i++) {
    const dev = Math.abs(zeros[idx[i] - 1] - gram[i]);
    if (isFinite(dev) && dev > 0) {
      logGamma.push(Math.log(zeros[idx[i] - 1]));
      logDev.push(Math.log(dev));
    }
  }

  // Linear regression: logDev = a + b * logGamma
  const n = logGamma.length;
  let sumX = 0, sumY = 0, sumXY = 0, sumX2 = 0;
  for (let i = 0; i < n; i++) {
    sumX  += logGamma[i];
    sumY  += logDev[i];
    sumXY += logGamma[i] * logDev[i];
    sumX2 += logGamma[i] * logGamma[i];
  }
  const denom = n * sumX2 - sumX * sumX;
  const intercept = (sumY * sumX2 - sumX * sumXY) / denom;
  const slope = (n * sumXY - sumX * sumY) / denom;

  // Standard error of slope
  let ssRes = 0;
  for (let i = 0; i < n; i++) {
    ssRes += Math.pow(logDev[i] - (intercept + slope * logGamma[i]), 2);
  }
  const s2 = ssRes / (n - 2);
  const stderr = Math.sqrt(s2 * n / denom);

  console.log(`\n${padR(M.obj3_slope + ':', 18)} ${slope.toFixed(6)}`);
  console.log(`${padR(M.obj3_stderr + ':', 18)} ${stderr.toFixed(6)}`);
  console.log(`${padR(M.obj3_target + ':', 18)} -0.5`);

  const verdict = Math.abs(slope - (-0.5)) < 0.15 ? M.obj3_pass : M.obj3_fail;
  console.log(`\n${verdict}`);
  return { slope, stderr };
}

// ==============================================================================
// String padding helpers
// ==============================================================================

function padL(str, len) { return String(str).padStart(len); }
function padR(str, len) { return String(str).padEnd(len); }

// ==============================================================================
// Main verification function
// ==============================================================================

async function abCloudVerify(options = {}) {
  const {
    dataDir   = '../data',
    zeros     = 0,
    source    = 'auto',
    objection = 'all',
    lang      = 'en',
  } = options;

  const M = MSG[lang] || MSG.en;

  console.log(`\n${M.separator}`);
  console.log(M.header);
  console.log(M.separator);

  // Load zeros
  const gammas = await loadZeros(dataDir, zeros, source);
  if (gammas.length === 0) {
    console.log(M.no_data);
    return null;
  }

  // Run selected objections
  const results = {};
  if (['all', '1'].includes(objection)) results.obj1 = objection1(gammas, M);
  if (['all', '2'].includes(objection)) results.obj2 = objection2(gammas, M);
  if (['all', '3'].includes(objection)) results.obj3 = objection3(gammas, M);

  console.log(`\n${M.separator}`);
  console.log(M.done);
  console.log('');
  return results;
}

// ==============================================================================
// Exports
// ==============================================================================

module.exports = {
  abCloudVerify,
  loadZeros,
  objection1,
  objection2,
  objection3,
  lambertW0,
  gramPoint,
  gramPointsVec,
  gueCDF,
  MSG,
};
