// verify_core.js — JavaScript-двойник ядра. Запуск: node verify_core.js [out]
const fs = require("fs");
const G = 7.0;
const C = [0.99999999999980993, 676.5203681218851, -1259.1392167224028,
  771.32342877765313, -176.61502916214059, 12.507343278686905,
  -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7];

function modGamma(re, u) {
  const zr = re - 1, zi = u;
  let xr = C[0], xi = 0;
  for (let i = 1; i < 9; i++) {
    const dr = zr + i, di = zi, den = dr * dr + di * di;
    xr += C[i] * dr / den; xi -= C[i] * di / den;
  }
  const tr = zr + G + 0.5, ti = zi;
  const mt = 0.5 * Math.log(tr * tr + ti * ti), at = Math.atan2(ti, tr);
  const pe = (zr + 0.5) * mt - ti * at, ph = ti * mt + (zr + 0.5) * at;
  const ar = Math.exp(pe) * Math.cos(ph), ai = Math.exp(pe) * Math.sin(ph);
  const e = Math.exp(-tr), br = e * Math.cos(-ti), bi = e * Math.sin(-ti);
  const c1r = ar * xr - ai * xi, c1i = ar * xi + ai * xr;
  const d1r = c1r * br - c1i * bi, d1i = c1r * bi + c1i * br;
  const gr = Math.sqrt(2 * Math.PI) * d1r, gi = Math.sqrt(2 * Math.PI) * d1i;
  return Math.sqrt(gr * gr + gi * gi);
}

const out = process.argv[2] || "verify_control.txt";
let maxRes = 0;
for (const u of [0.5, 1, 2, 3]) {
  const ref = Math.sqrt(Math.PI / Math.cosh(Math.PI * u));
  maxRes = Math.max(maxRes, Math.abs(modGamma(0.5, u) - ref) / ref);
}
const N = 100000;
const spf = new Int32Array(N + 1);
let sum = 0;
for (let i = 2; i <= N; i++) if (!spf[i]) for (let j = i; j <= N; j += i) if (!spf[j]) spf[j] = i;
for (let p = 2; p <= N; p++) if (spf[p] === p)
  for (let pk = p; pk <= N; pk *= p) sum += Math.log(p) / Math.pow(pk, 1.5);
fs.writeFileSync(out, `gamma_closure_max_res = ${maxRes.toExponential(3)}\nlambda_sum_check = ${sum.toFixed(10)}\nn_sieve = ${N}\n`);
console.log("js twin OK:", maxRes.toExponential(2), sum.toFixed(10));
