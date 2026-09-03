/**
 * zeta.js — a self-anchored complex ζ(s) evaluator (Euler–Maclaurin),
 * a faithful JS port of the 3D-34 ζ evaluator of the Julia suite.
 * Self-check anchors: ζ(2)=π²/6, ζ(4)=π⁴/90, ζ(1/2)≈−1.4603545088095868.
 */
'use strict';

// complex numbers: [re, im]
export function cAdd(a, b) { return [a[0] + b[0], a[1] + b[1]]; }
export function cMul(a, b) {
  return [a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]];
}
export function cAbs(a) { return Math.hypot(a[0], a[1]); }

// complex power a^b with COMPLEX exponent b: a^b = exp(b * Log a)
export function cPow(a, b) {
  const r = Math.hypot(a[0], a[1]);
  if (r === 0) return [0, 0];
  const th = Math.atan2(a[1], a[0]);
  const lr = Math.log(r);
  const re = b[0] * lr - b[1] * th;
  const im = b[1] * lr + b[0] * th;
  const s = Math.exp(re);
  return [s * Math.cos(im), s * Math.sin(im)];
}

const factCache = [1];
function factorial(n) {
  for (let i = factCache.length; i <= n; i++) factCache[i] = factCache[i - 1] * i;
  return factCache[n];
}

const BERN = [1, -0.5, 1 / 6, 0, -1 / 30, 0, 1 / 42, 0, -1 / 30, 0,
  5 / 66, 0, -691 / 2730, 0, 7 / 6, 0, -3617 / 510];

/**
 * ζ(s) for complex s (s ≠ 1) via Euler–Maclaurin:
 *   ζ(s) = Σ_{k=1}^{N−1} k^{−s} + N^{1−s}/(s−1) + N^{−s}/2
 *          + Σ_{k=1}^{M} B_{2k}/(2k)! · (s)_{2k−1} · N^{1−s−2k},
 * where (s)_m = s(s+1)...(s+m−1) is the rising factorial.
 */
export function zeta(s) {
  const N = 40, M = 8;
  let sum = [0, 0];
  for (let k = 1; k < N; k++) {
    sum = cAdd(sum, cPow([k, 0], [-s[0], -s[1]]));
  }
  const Nc = [N, 0];
  const d = (s[0] - 1) * (s[0] - 1) + s[1] * s[1];
  const invS1 = [(s[0] - 1) / d, -s[1] / d];
  tail = cMul(invS1, cPow(Nc, [1 - s[0], -s[1]]));
  tail = cAdd(tail, cMul([0.5, 0], cPow(Nc, [-s[0], -s[1]])));
  let rising = [1, 0];               // (s)_0
  let asym = [0, 0];
  for (let k = 1; k <= M; k++) {
    rising = cMul(rising, [s[0] + 2 * k - 2, s[1]]);
    rising = cMul(rising, [s[0] + 2 * k - 1, s[1]]);
    const coef = BERN[2 * k] / factorial(2 * k);
    asym = cAdd(asym, cMul([coef, 0],
      cMul(rising, cPow(Nc, [1 - s[0] - 2 * k, -s[1]]))));
  }
  return cAdd(sum, cAdd(tail, asym));
}

export function zetaSelfCheck() {
  const z2 = zeta([2, 0]);
  const z4 = zeta([4, 0]);
  const zh = zeta([0.5, 0]);
  const zc = zeta([0.5, 14.134725142]);
  return {
    z2: z2[0], z2err: Math.abs(z2[0] - Math.PI * Math.PI / 6),
    z4: z4[0], z4err: Math.abs(z4[0] - Math.pow(Math.PI, 4) / 90),
    zh: zh[0], zherr: Math.abs(zh[0] + 1.4603545088095868),
    zcrit: cAbs(zc),
  };
}

// first zeros of γ (Odlyzko, embedded in the suite)
export const FIRST_ZEROS = [
  14.134725142, 21.022039639, 25.010857580, 30.424876126, 32.935061588,
  37.586178159, 40.918719012, 43.327073281, 48.005150881, 49.773832478,
  52.970321478, 56.446247697, 59.347044003, 60.831778525, 65.112544048,
];
