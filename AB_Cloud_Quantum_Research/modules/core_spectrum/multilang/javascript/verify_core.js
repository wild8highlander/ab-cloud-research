// verify_core.js — двойник Node ≥ 18: Γ-замыкание + Λ-сито
const fs = require('fs');
const LC = [0.99999999999980993, 676.5203681218851, -1259.1392167224028,
  771.32342877765313, -176.61502916214059, 12.507343278686905,
  -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7];
function cgamma(x, y) {
  let zr = x - 1, zi = y;
  let sr = LC[0], si = 0;
  for (let i = 1; i < 9; i++) {
    const dr = zr + i, di = zi, d = dr*dr + di*di;
    sr += LC[i]*dr/d; si += -LC[i]*di/d;
  }
  const tr = zr + 7.5, ti = zi;
  const ltR = 0.5*Math.log(tr*tr + ti*ti), ltI = Math.atan2(ti, tr);
  const lsR = 0.5*Math.log(sr*sr + si*si), lsI = Math.atan2(si, sr);
  const ar = zr + 0.5, ai = zi;
  const Lr = 0.5*Math.log(2*Math.PI) + (ar*ltR - ai*ltI) - tr + lsR;
  const Li = (ar*ltI + ai*ltR) + lsI;
  return [Math.exp(Lr)*Math.cos(Li), Math.exp(Lr)*Math.sin(Li)];
}
let maxres = 0;
for (const u of [0.5, 1, 2, 3]) {
  const [gr, gi] = cgamma(0.5, u);
  const lhs = gr*gr + gi*gi, rhs = Math.PI/Math.cosh(Math.PI*u);
  maxres = Math.max(maxres, Math.abs(lhs - rhs)/rhs);
}
const N = 100000;
const spf = new Int32Array(N + 1);
let lsum = 0;
for (let i = 2; i <= N; i++) if (!spf[i])
  for (let p = i; p <= N; p *= i) {
    lsum += Math.log(i)/Math.pow(p, 1.5);
    for (let j = i; j <= N; j += i) if (!spf[j]) spf[j] = i;
  }
console.log(`gamma_closure_max_res = ${maxres.toExponential(3)}`);
console.log(`lambda_sum_check = ${lsum.toFixed(10)}`);
console.log(`n_sieve = ${N}`);
if (process.argv[2]) fs.writeFileSync(process.argv[2],
  `gamma_closure_max_res = ${maxres.toExponential(3)}\n` +
  `lambda_sum_check = ${lsum.toFixed(10)}\nn_sieve = ${N}\n`);
