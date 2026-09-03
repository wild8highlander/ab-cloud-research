#!/usr/bin/env node
/**
 * spinor38.js — Test 38: 64 spinor structures of the Klein quartic (JS port).
 *
 * Self-implemented cyclic Jacobi eigenvalue algorithm (no external libs).
 * Verifies: (1) the 28 odd (Arf=1) spinor structures are exactly isospectral
 * (max pairwise spectral distance ~ 1e-14) — no spinor structure is unique;
 * (2) <r> of the representative spectrum matches the reference.
 *
 * Run: node spinor38.js [repo-root]
 */
'use strict';
const fs = require('fs');
const path = require('path');

function findDataDir(rootArg) {
  const roots = [];
  if (rootArg) roots.push(rootArg);
  let base = process.cwd();
  roots.push(base);
  for (const r of roots) {
    let b = r;
    for (let up = 0; up < 6; up++) {
      const cand = path.join(b, 'verification', 'spinor64', 'data',
        'spinor_classes.csv');
      if (fs.existsSync(cand)) return path.join(b, 'verification', 'spinor64',
        'data');
      b = path.join(b, '..');
    }
  }
  console.error('data dir not found; pass repo root as argument');
  process.exit(2);
}

function parseCsvClasses(file) {
  const lines = fs.readFileSync(file, 'utf8').trim().split('\n');
  const out = [];
  for (let i = 1; i < lines.length; i++) {
    if (!lines[i]) continue;
    const parts = lines[i].split(',');
    const cls = parseInt(parts[0], 10);
    const orbit = parseInt(parts[1], 10);
    const arf = parseInt(parts[2], 10);
    const signs = parts[3].trim().split(/\s+/).map(Number);
    out.push({ cls, orbit, arf, signs });
  }
  return out;
}

function parseEdges(file) {
  const lines = fs.readFileSync(file, 'utf8').trim().split('\n');
  const out = [];
  for (let i = 1; i < lines.length; i++) {
    if (!lines[i]) continue;
    const p = lines[i].split(',');
    out.push([parseInt(p[1], 10), parseInt(p[2], 10)]);
  }
  return out;
}

// cyclic Jacobi eigenvalues of a real symmetric matrix (n x n, 2D array)
function jacobiEigen(Ain) {
  const n = Ain.length;
  const A = Ain.map((row) => row.slice());
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
        const c = 1 / Math.sqrt(1 + t * t);
        const s = t * c;
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
  eig.sort((a, b) => a - b);
  return eig;
}

function main() {
  const dd = findDataDir(process.argv[2]);
  const classes = parseCsvClasses(path.join(dd, 'spinor_classes.csv'));
  const edges = parseEdges(path.join(dd, 'klein_graph_edges.csv'));
  const stats = JSON.parse(fs.readFileSync(path.join(dd,
    'reference_stats.json'), 'utf8'));
  const N = 56;
  const nOdd = classes.filter((c) => c.orbit === 0).length;

  const spectra = [];
  let repSpectrum = null;
  for (const c of classes) {
    if (c.orbit !== 0) continue;
    const A = [];
    for (let i = 0; i < N; i++) A.push(new Array(N).fill(0));
    edges.forEach(([u, v], k) => {
      const s = c.signs[k];
      A[u][v] = s; A[v][u] = s;
    });
    const w = jacobiEigen(A);
    if (c.cls === stats.representative_class) repSpectrum = w;
    spectra.push(w);
  }

  let isomax = 0;
  for (let a = 0; a < spectra.length; a++)
    for (let b = a + 1; b < spectra.length; b++)
      for (let i = 0; i < N; i++)
        isomax = Math.max(isomax, Math.abs(spectra[a][i] - spectra[b][i]));

  let nZero = 0;
  const lam = repSpectrum.map((v) => Math.abs(v)).sort((a, b) => a - b);
  for (const v of lam) if (v < 1e-8) nZero++;
  const dsp = [];
  for (let i = 0; i + 1 < lam.length; i++) {
    const d = lam[i + 1] - lam[i];
    if (d > 1e-8) dsp.push(d);
  }
  let rsum = 0;
  for (let i = 0; i + 1 < dsp.length; i++)
    rsum += Math.min(dsp[i], dsp[i + 1]) / Math.max(dsp[i], dsp[i + 1]);
  const rMean = rsum / (dsp.length - 1);

  console.log('Test 38 - 64 spinor structures of the Klein quartic (JS port)');
  console.log(`classes loaded: ${classes.length} | odd-orbit members: ${nOdd}`);
  console.log(`isospectrality within the odd orbit: max|dlambda| = ` +
    `${isomax.toExponential(3)} -> ${isomax < 1e-9 ? 'PASS' : 'FAIL'}`);
  console.log(`zero modes (representative): ${nZero} (expected ` +
    `${stats.n_zero_modes})`);
  const rOk = Math.abs(rMean - stats.r_mean_reference) < 1e-6;
  console.log(`<r> (representative): ${rMean.toFixed(10)} ` +
    `(reference 0.4515710793) -> ${rOk ? 'PASS' : 'FAIL'}`);
  const ok = isomax < 1e-9 && nZero === stats.n_zero_modes && rOk;
  console.log(`VERDICT: ${ok ? 'PASS' : 'FAIL'}`);
  process.exit(ok ? 0 : 1);
}

main();
