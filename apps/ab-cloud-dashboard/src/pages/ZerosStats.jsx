import React, { useEffect, useMemo, useState } from 'react';
import { LineChart, BarChart, Stat, Skeleton, useWorker } from '../components/ui.jsx';
import { unfoldSpacings, psAndSurvival, gueSurmiseCurves, zeroRows } from '../lib/analysis.js';

const PAGE = 20;

export default function ZerosStats({ zeros, error: loadError }) {
  const { run, busy } = useWorker();
  const [res, setRes] = useState(null);
  const [err, setErr] = useState('');
  const [page, setPage] = useState(0);
  const [windowIdx, setWindowIdx] = useState(0);

  useEffect(() => {
    if (zeros && zeros.length && !res && !err) {
      run('stats', { zeros }).then(r => {
        if (r.ok) setRes(r.result);
        else setErr(r.error || 'worker computation failed');
      });
    }
  }, [zeros, res, err, run]);

  /* Additional live views (p(s), E(s)) — computed on the main thread from
   * the same embedded dataset; the worker and its frozen methodology are
   * untouched (see lib/analysis.js). */
  const extra = useMemo(() => {
    if (!zeros || !zeros.length) return null;
    const windows = [5000, 20000, 50000];
    const count = windows[windowIdx] ?? 5000;
    const unfolded = unfoldSpacings(zeros, count);
    const { density, E, bw } = psAndSurvival(unfolded);
    const gue = gueSurmiseCurves(density.length);
    return { count, density, E, gue, bw, windows };
  }, [zeros, windowIdx]);

  if (loadError && !zeros) {
    return <p className="error-note">Failed to load the zeros dataset — {loadError}</p>;
  }
  if (err) return <p className="error-note">Live statistics failed: {err}</p>;
  if (!zeros || (busy && !res)) {
    return (
      <section aria-busy="true" aria-label="Computing live statistics">
        <h2>Live statistics of the ζ zeros <span className="pill">Web Worker</span></h2>
        <p className="muted">Computing in a Web Worker from the embedded 50,000 Odlyzko zeros…</p>
        <Skeleton kind="stats" />
        <Skeleton kind="chart" />
      </section>
    );
  }
  if (!res || !res.bN || !res.bN.length) {
    return (
      <div className="empty">
        <b>Statistics are unavailable for this dataset.</b><br />
        Not enough zeros to build the b(N) checkpoints — check that the embedded dataset deployed correctly.
      </div>
    );
  }
  const lastB = res.bN[res.bN.length - 1].b;

  const nShown = 5000;
  const hist = (() => {
    const ratios = [];
    const lam = zeros.slice(0, nShown).map(Math.abs).sort((a, b) => a - b);
    const d = [];
    for (let i = 1; i < lam.length; i++) d.push(lam[i] - lam[i - 1]);
    for (let i = 0; i + 1 < d.length; i++) {
      const mn = Math.min(d[i], d[i + 1]), mx = Math.max(d[i], d[i + 1]);
      ratios.push(mn / mx);
    }
    const bins = new Array(40).fill(0);
    for (const r of ratios) bins[Math.min(39, Math.floor(r * 40))]++;
    return bins.map((v, i) => [(i + 0.5) / 40, v]);
  })();

  const maxPage = Math.max(0, Math.ceil((zeros.length - 2) / PAGE) - 1);
  const from = page * PAGE + 1;
  const rows = zeroRows(zeros, from, from + PAGE - 1);

  return (
    <section>
      <h2>Live statistics of the ζ zeros <span className="pill">Web Worker</span></h2>
      <p className="muted">
        The same diagnostics as the Julia suite (tests 1–5, 13, 14), computed
        live in your browser from the embedded Odlyzko dataset of 50,000 zeros.
      </p>
      <div className="stats-grid">
        <Stat label="⟨r⟩ (all 50,000)" value={res.rMean.toFixed(4)}
          refVal="0.59965 (GUE)" ok={Math.abs(res.rMean - 0.59965) < 0.02} />
        <Stat label={`KS D vs GUE ratio law (n=${res.nRatios})`}
          value={res.ks.D.toFixed(4)} refVal={`p = ${res.ks.p.toExponential(2)}`} />
        <Stat label="b(N = 50000)" value={lastB.toFixed(4)}
          refVal="1.2126 (suite Test 1)" ok={Math.abs(lastB - 1.2126) < 0.05} />
        <Stat label="POISSON / GOE / GUE"
          value={`${res.refs.R_POISSON} / ${res.refs.R_GOE} / ${res.refs.R_GUE}`} />
      </div>

      <h3>b(N) convergence</h3>
      <LineChart logX xLabel="N" yLabel="b(N)"
        series={[{ name: 'b(N) — in the browser', points: res.bN.map(p => [p.N, p.b]) }]} />

      <h3>Spacing-ratio histogram (first 5,000 zeros) vs GUE ratio law</h3>
      <BarChart points={hist} xLabel="r = min/max" yLabel="count" />

      <h3>Σ²(L) — number variance</h3>
      <LineChart logX xLabel="L" yLabel="Σ²(L)"
        series={[
          { name: 'zeros (in the browser)', points: res.sig2.map(p => [p.L, p.sigma2]) },
          { name: 'Poisson L', points: res.sig2.map(p => [p.L, p.L]) },
        ]} />

      <h3>Δ₃(L) — spectral rigidity</h3>
      <LineChart logX xLabel="L" yLabel="Δ₃(L)"
        series={[{ name: 'zeros (in the browser)', points: res.d3.map(p => [p.L, p.delta3]) }]} />

      <h3>p(s) — unfolded NNSD vs the Wigner GUE surmise <span className="pill">live</span></h3>
      <p className="muted">
        A quick moving-average unfolding (window ±50 spacings) of the first{' '}
        <b>{(extra?.count ?? 5000).toLocaleString()}</b> zeros, against the
        Wigner GUE surmise p(s) = (32/π²) s² e^(−4s²/π). The suite-grade
        poly-unfold deg-5 curve is in the Enrichment tab.
      </p>
      <div className="filter-row" role="group" aria-label="Choose how many zeros to unfold">
        {(extra?.windows ?? [5000]).map((w, i) => (
          <button key={w} className={windowIdx === i ? 'btn active' : 'btn'}
            aria-pressed={windowIdx === i}
            onClick={() => setWindowIdx(i)}>{w.toLocaleString('en-US')} zeros</button>
        ))}
      </div>
      <LineChart xLabel="s" yLabel="p(s)"
        series={[
          { name: 'zeros (moving-average unfold)', points: extra.density.map((v, j) => [Math.round(((j + 0.5) * extra.bw) * 1000) / 1000, v]) },
          { name: 'Wigner GUE surmise', points: extra.gue.density.map((v, j) => [Math.round(((j + 0.5) * extra.bw) * 1000) / 1000, v]) },
        ]} />

      <h3>E(s) — survival of the unfolded spacings</h3>
      <LineChart xLabel="s" yLabel="E(s)"
        series={[
          { name: 'zeros (live)', points: extra.E.map((v, j) => [Math.round(((j + 0.5) * extra.bw) * 1000) / 1000, v]) },
          { name: 'Wigner GUE surmise', points: extra.gue.E.map((v, j) => [Math.round(((j + 0.5) * extra.bw) * 1000) / 1000, v]) },
        ]} />
      <p className="muted">
        E(s) reads off the level-repulsion directly: near-zero density below
        s ≈ 0.3, and a survival at s = 1 consistent with the GUE surmise
        (0.467 exact-surmise value; the frozen table value is the exact-GUE
        0.171 — see the GUE control tab).
      </p>

      <h3>Zeros browser — γ₁…γ₅₀₀₀₀ <span className="pill">read-only</span></h3>
      <p className="muted">
        The embedded dataset itself: ordinate γ<sub>n</sub>, gap to the next
        zero, and the ratio r = min(Δ)/max(Δ) — the very rows the Julia suite
        reads from <code>verification/data/</code>.
      </p>
      <div className="table-wrap">
        <table className="data">
          <thead>
            <tr>
              <th scope="col">n</th><th scope="col">γₙ</th>
              <th scope="col">gap Δₙ</th><th scope="col">r = min/max</th>
            </tr>
          </thead>
          <tbody>
            {rows.map(rw => (
              <tr key={rw.n}>
                <td className="test-id">{rw.n}</td>
                <td className="headline">{rw.gamma.toFixed(6)}</td>
                <td className="headline">{rw.gap.toFixed(6)}</td>
                <td className="headline">{rw.r == null ? '—' : rw.r.toFixed(6)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <div className="browser-nav">
        <button className="btn" onClick={() => setPage(0)} disabled={page === 0}
          style={page === 0 ? { opacity: 0.4, cursor: 'default' } : undefined}>⇤ first</button>
        <button className="btn" onClick={() => setPage(p => Math.max(0, p - 1))} disabled={page === 0}
          style={page === 0 ? { opacity: 0.4, cursor: 'default' } : undefined}>← prev</button>
        <span className="muted browser-pos">
          rows {from.toLocaleString('en-US')}…{Math.min(from + PAGE - 1, zeros.length).toLocaleString('en-US')}
          {' '}of {zeros.length.toLocaleString('en-US')}
        </span>
        <button className="btn" onClick={() => setPage(p => Math.min(maxPage, p + 1))} disabled={page >= maxPage}
          style={page >= maxPage ? { opacity: 0.4, cursor: 'default' } : undefined}>next →</button>
        <button className="btn" onClick={() => setPage(maxPage)} disabled={page >= maxPage}
          style={page >= maxPage ? { opacity: 0.4, cursor: 'default' } : undefined}>last ⇥</button>
      </div>

      {busy && <p className="muted" role="status">computing…</p>}
    </section>
  );
}
