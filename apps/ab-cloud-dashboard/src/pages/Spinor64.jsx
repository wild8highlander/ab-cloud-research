import React, { useEffect, useState } from 'react';
import { LineChart, Stat, useWorker } from '../components/ui.jsx';

export default function Spinor64() {
  const { run, busy } = useWorker();
  const [data, setData] = useState(null);
  const [res, setRes] = useState(null);
  const [idx, setIdx] = useState(0);

  useEffect(() => {
    Promise.all([
      fetch('data/spinor_classes.csv').then(r => r.text()),
      fetch('data/klein_graph_edges.csv').then(r => r.text()),
      fetch('data/reference_stats.json').then(r => r.json()),
    ]).then(([clsTxt, edgeTxt, stats]) => {
      const lines = clsTxt.trim().split('\n').slice(1);
      const classes = lines.filter(Boolean).map(l => {
        const p = l.split(',');
        return { cls: +p[0], orbit: +p[1], arf: +p[2],
          signs: p[3].trim().split(/\s+/).map(Number) };
      });
      const edges = edgeTxt.trim().split('\n').slice(1).filter(Boolean)
        .map(l => { const p = l.split(','); return [+p[1], +p[2]]; });
      setData({ classes, edges, stats });
    });
  }, []);

  useEffect(() => {
    if (data && !res) {
      run('spinor', {
        classes: data.classes, edges: data.edges,
        representative: data.stats.representative_class,
      }).then(r => { if (r.ok) setRes(r.result); });
    }
  }, [data, res, run]);

  if (!data) return <p className="muted">Loading frozen spinor data…</p>;
  const orbitCounts = [28, 21, 7, 7, 1];

  return (
    <section>
      <h2>Test 38 — 64 spinor structures of the Klein quartic
        <span className="pill">in-browser Jacobi</span></h2>
      <p className="muted">
        All 64 structures are loaded from the frozen dataset
        (<code>verification/spinor64/data/</code>). The browser computes the
        spectra of all 28 odd (Arf=1) structures with a hand-written Jacobi
        eigensolver — the corrected claim: <b>all spinor structures are
        equivalent</b>; the v21 “idx=38 uniqueness” was a computational
        artifact (see monograph v21.1, section 3.2.5).
      </p>
      <div className="stats-grid">
        <Stat label="Orbit sizes (PSL(2,7))" value={orbitCounts.join(' / ')}
          refVal="odd = 28 (bitangents, Riemann–Klein)" />
        <Stat label="Isospectrality (odd orbit)" value={res ? res.isomax.toExponential(2) : '…'}
          refVal="8.9e-15 (reference)" ok={res && res.isomax < 1e-9} />
        <Stat label="⟨r⟩ (representative)" value={res ? res.rMean.toFixed(10) : '…'}
          refVal="0.4515710793" ok={res && Math.abs(res.rMean - 0.4515710792825435) < 1e-6} />
        <Stat label="Zero modes" value={res ? res.nZero : '…'} refVal="2" ok={res && res.nZero === 2} />
      </div>
      {res && (
        <>
          <h3>Representative spectrum (class {data.stats.representative_class},
            odd orbit) — computed live</h3>
          <LineChart xLabel="level index" yLabel="λ"
            series={[{ name: 'eigenvalues (JS Jacobi)', points: res.spectrum.map((v, i) => [i, v]) }]} />
        </>
      )}
      <h3>The 64 structures</h3>
      <table className="data">
        <thead><tr><th>class</th><th>orbit</th><th>Arf</th></tr></thead>
        <tbody>
          {data.classes.filter(c => c.cls >= idx && c.cls < idx + 16).map(c => (
            <tr key={c.cls}>
              <td>{c.cls}</td><td>{c.orbit}</td><td>{c.arf}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <input type="range" min="0" max="48" value={idx}
        onChange={e => setIdx(+e.target.value)} style={{ width: '100%' }} />
      {busy && <p className="muted">computing…</p>}
    </section>
  );
}
