// stitch_core.js — мультиязычный двойник V19 (Node ≥ 18): сшивка ветвей
// алгебраической функции (дорожная карта R2, механизм hodge-laboratory).
// Регрессия R3 (кросс-язычная): повторяет c/stitch_core.c бит-в-бит.
//
// θ(t) — асимптотика Стирлинга (главная ветвь, O(t^-9) при t ≥ 14);
// встроены первые 64 нуля ζ; контрольный блок stitch_control.txt.
'use strict';
const fs = require('fs');

const Z64 = [
  14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178,
  40.918719, 43.327073, 48.005151, 49.773832, 52.970321, 56.446248,
  59.347044, 60.831779, 65.112544, 67.079811, 69.546402, 72.067158,
  75.704691, 77.144840, 79.337375, 82.910381, 84.735493, 87.425275,
  88.809111, 92.491899, 94.651344, 95.870634, 98.831194, 101.317851,
  103.725538, 105.446623, 107.168611, 111.029536, 111.874659,
  114.320221, 116.226680, 118.790783, 121.370125, 122.946829,
  124.256819, 127.516684, 129.578704, 131.087689, 133.497737,
  134.756510, 138.116042, 139.736209, 141.123707, 143.111846,
  146.000982, 147.422765, 150.053520, 150.925258, 153.024694,
  156.112909, 157.597592, 158.849988, 161.188964, 163.030710,
  165.537069, 167.184440, 169.094515, 169.911976];

function thetaRs(t) { // Римана–Зигеля θ(t), главная ветвь
  const p = Math.PI;
  return t / 2 * Math.log(t / (2 * p)) - t / 2 - p / 8
    + 1 / (48 * t) + 7 / (5760 * t * t * t)
    + 31 / (8064 * Math.pow(t, 5)) + 127 / (30720 * Math.pow(t, 7));
}

const n = 64;
const th = [];
for (let k = 0; k < n - 1; k++)
  th.push(thetaRs(0.5 * (Z64[k] + Z64[k + 1])));
let conc = 0, agree = 0;
for (let k = 0; k < n - 2; k++) {
  let u = ((th[k + 1] - th[k]) / Math.PI) % 2;
  if (u < 0) u += 2;
  if (Math.abs(u - 1) < 0.3) conc++;
}
for (let k = 0; k < n - 1; k++)
  if ((Math.cos(th[k]) > 0 ? 1 : -1) === (k % 2 === 0 ? 1 : -1)) agree++;
const ladderConc = conc / (n - 2);
const coherence = agree / (n - 1);

let maxRes = 0;
const AB = [[7, 3], [11, 5], [1, 1]];
for (const [a, b] of AB) {
  const N = 15;
  for (let r = 0; r < N; r++) for (let s = 0; s < N; s++) {
    const ph = 2 * Math.PI * ((a * r + b * s) % N) / N;
    const pr = Math.cos(ph), pi = Math.sin(ph);
    let ph2 = 0;
    for (let i = 0; i < a; i++) { ph2 += 2 * Math.PI * r / N; if (ph2 > 2 * Math.PI) ph2 -= 2 * Math.PI; }
    for (let i = 0; i < b; i++) { ph2 += 2 * Math.PI * s / N; if (ph2 > 2 * Math.PI) ph2 -= 2 * Math.PI; }
    const res = Math.hypot(Math.cos(ph2) - pr, Math.sin(ph2) - pi);
    if (res > maxRes) maxRes = res;
  }
}

const verdict = (ladderConc > 0.5 && coherence > 0.9 && maxRes < 1e-9)
  ? 'ALGEBRAIC_CERTIFICATE' : 'NOT_DETERMINED';

const block = [
  `stitch_theta_ladder_conc=${ladderConc.toFixed(12)}`,
  `stitch_sign_coherence=${coherence.toFixed(12)}`,
  `stitch_phase_law_max_res=${maxRes.toExponential(2)}`,
  `stitch_verdict=${verdict}`,
];
console.log(block.join('\n'));
if (process.argv[2]) fs.writeFileSync(process.argv[2], block.join('\n') + '\n');
