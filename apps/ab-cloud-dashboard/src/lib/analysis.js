/* analysis.js — client-side helpers for the ADDITIONAL live views.
 *
 * Nothing here replaces the frozen numerics: the worker (stats.worker.js)
 * and every frozen artifact stay untouched. These helpers only reshape the
 * embedded zeros into two extra classical views:
 *   • p(s) — nearest-neighbour spacing distribution after a moving-average
 *     unfolding (window ±W spacings), with the Wigner GUE surmise reference
 *   • E(s) — the survival function of the same unfolded spacings
 * The unfolding is intentionally simple and labelled as such in the UI;
 * the suite-grade poly-unfold deg-5 curves live in the Enrichment tab.
 */

const GUE_SURMISE = (s) =>
  (32 / (Math.PI * Math.PI)) * s * s * Math.exp((-4 * s * s) / Math.PI);

/** Unfold spacings by a moving average of width 2*W+1. */
export function unfoldSpacings(zeros, count, W = 50) {
  const lam = zeros.slice(0, count).map(Math.abs).sort((a, b) => a - b);
  const d = [];
  for (let i = 1; i < lam.length; i++) d.push(lam[i] - lam[i - 1]);
  const out = [];
  for (let i = 0; i < d.length; i++) {
    const a = Math.max(0, i - W), b = Math.min(d.length, i + W + 1);
    let s = 0;
    for (let j = a; j < b; j++) s += d[j];
    const loc = s / (b - a);
    if (loc > 0) out.push(d[i] / loc);
  }
  return out;
}

/** Density histogram + survival function on the grid 0..SMAX. */
export function psAndSurvival(unfolded, nBins = 40, sMax = 4) {
  const bins = new Array(nBins).fill(0);
  for (const v of unfolded) {
    if (v >= 0 && v < sMax) bins[Math.min(nBins - 1, Math.floor((v / sMax) * nBins))]++;
  }
  const n = unfolded.length, bw = sMax / nBins;
  const density = bins.map((c) => c / n / bw);
  const E = new Array(nBins);
  let acc = 0;
  for (let i = nBins - 1; i >= 0; i--) {
    acc += density[i] * bw;
    E[i] = acc;
  }
  return { density, E, bw };
}

/** Wigner GUE surmise evaluated at the same bin centres / survival grid. */
export function gueSurmiseCurves(nBins = 40, sMax = 4) {
  const bw = sMax / nBins;
  const density = [], E = new Array(nBins);
  for (let i = 0; i < nBins; i++) density.push(GUE_SURMISE((i + 0.5) * bw));
  let acc = 0;
  for (let i = nBins - 1; i >= 0; i--) {
    acc += density[i] * bw;
    E[i] = acc;
  }
  return { density, E };
}

/** Rows for the zeros browser: index (1-based), γ, gap to next, ratio min/max. */
export function zeroRows(zeros, from, to) {
  const lam = zeros.slice(0, Math.min(zeros.length, to + 1)).map(Math.abs).sort((a, b) => a - b);
  const rows = [];
  for (let i = from; i <= Math.min(to, lam.length - 2); i++) {
    const gap = lam[i] - lam[i - 1];
    const next = lam[i + 1] - lam[i];
    rows.push({
      n: i,
      gamma: lam[i - 1],
      gap,
      r: next > 0 || gap > 0 ? Math.min(gap, next) / Math.max(gap, next) : null,
    });
  }
  return rows;
}
