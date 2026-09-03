import React, { useEffect, useState } from 'react';
import { LineChart, BarChart, Stat, useWorker } from '../components/ui.jsx';

export default function ZerosStats({ zeros }) {
  const { run, busy } = useWorker();
  const [res, setRes] = useState(null);

  useEffect(() => {
    if (zeros && zeros.length && !res) {
      run('stats', { zeros }).then(r => { if (r.ok) setRes(r.result); });
    }
  }, [zeros, res, run]);

  if (!zeros) return <p className="muted">Loading the 50,000 Odlyzko zeros…</p>;
  if (busy && !res) return <p className="muted">Computing real-time statistics in a Web Worker…</p>;
  if (!res) return null;

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

  return (
    <section>
      <h2>Real-time statistics of the ζ zeros <span className="pill">Web Worker</span></h2>
      <p className="muted">
        The same diagnostics as the Julia suite (tests 1–5, 13, 14), computed
        live in your browser from the embedded Odlyzko dataset of 50,000 zeros.
      </p>
      <div className="stats-grid">
        <Stat label="⟨r⟩ (all 50,000)" value={res.rMean.toFixed(4)}
          refVal="0.59965 (GUE)" ok={Math.abs(res.rMean - 0.59965) < 0.02} />
        <Stat label={`KS D vs GUE ratio law (n=${res.nRatios})`}
          value={res.ks.D.toFixed(4)} refVal={`p = ${res.ks.p.toExponential(2)}`} />
        <Stat label="b(N = 50000)" value={res.bN[res.bN.length - 1].b.toFixed(4)}
          refVal="1.2126 (suite Test 1)" ok={Math.abs(res.bN[res.bN.length - 1].b - 1.2126) < 0.05} />
        <Stat label="POISSON / GOE / GUE"
          value={`${res.refs.R_POISSON} / ${res.refs.R_GOE} / ${res.refs.R_GUE}`} />
      </div>

      <h3>b(N) convergence</h3>
      <LineChart logX xLabel="N" yLabel="b(N)"
        series={[{ name: 'b(N) — in-browser', points: res.bN.map(p => [p.N, p.b]) }]} />

      <h3>Spacing-ratio histogram (first 5,000 zeros) vs GUE ratio law</h3>
      <BarChart points={hist} xLabel="r = min/max" yLabel="count" />

      <h3>Σ²(L) — number variance</h3>
      <LineChart logX xLabel="L" yLabel="Σ²(L)"
        series={[
          { name: 'zeros (in-browser)', points: res.sig2.map(p => [p.L, p.sigma2]) },
          { name: 'Poisson L', points: res.sig2.map(p => [p.L, p.L]) },
        ]} />

      <h3>Δ₃(L) — spectral rigidity</h3>
      <LineChart logX xLabel="L" yLabel="Δ₃(L)"
        series={[{ name: 'zeros (in-browser)', points: res.d3.map(p => [p.L, p.delta3]) }]} />
    </section>
  );
}
