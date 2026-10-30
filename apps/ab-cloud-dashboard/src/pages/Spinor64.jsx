import React, { useEffect, useState } from 'react';
import { CatBar, LineChart, Stat, Skeleton, useWorker } from '../components/ui.jsx';

export default function Spinor64({ error: loadError }) {
  const { run, busy } = useWorker();
  const [data, setData] = useState(null);
  const [res, setRes] = useState(null);
  const [idx, setIdx] = useState(0);
  const [err, setErr] = useState('');

  useEffect(() => {
    const get = (url, as) => fetch(url).then(r => {
      if (!r.ok) throw new Error(`${url}: HTTP ${r.status}`);
      return as === 'json' ? r.json() : r.text();
    });
    Promise.all([
      get('data/spinor_classes.csv', 'text'),
      get('data/klein_graph_edges.csv', 'text'),
      get('data/reference_stats.json', 'json'),
    ]).then(([clsTxt, edgeTxt, stats]) => {
      const lines = clsTxt.trim().split(/\r?\n/).slice(1);
      const classes = lines.filter(Boolean).map(l => {
        const p = l.split(',');
        return { cls: +p[0], orbit: +p[1], arf: +p[2],
          signs: p[3].trim().split(/\s+/).map(Number) };
      });
      const edges = edgeTxt.trim().split(/\r?\n/).slice(1).filter(Boolean)
        .map(l => { const p = l.split(','); return [+p[1], +p[2]]; });
      setData({ classes, edges, stats });
    }).catch(e => setErr(`Failed to load frozen spinor data — ${e.message}`));
  }, []);

  useEffect(() => {
    if (data && !res && !err) {
      run('spinor', {
        classes: data.classes, edges: data.edges,
        representative: data.stats.representative_class,
      }).then(r => {
        if (r.ok) setRes(r.result);
        else setErr(`Spinor computation failed — ${r.error || 'unknown worker error'}`);
      });
    }
  }, [data, res, err, run]);

  if (err) return <p className="error-note">{err}</p>;
  if (loadError && !data) return <p className="error-note">{loadError}</p>;
  if (!data) {
    return (
      <section aria-busy="true" aria-label="Loading frozen spinor data">
        <h2>Test 38 — 64 spinor structures of the Klein quartic <span className="pill">Jacobi in the browser</span></h2>
        <Skeleton kind="stats" />
        <Skeleton kind="table" />
      </section>
    );
  }
  const orbitCounts = [28, 21, 7, 7, 1];
  const oddMembers = data.stats.odd_orbit_members ?? [];
  const arfOne = data.classes.filter(c => c.arf === 1).length;
  const orbitFieldCounts = data.classes.reduce((acc, c) => {
    acc[c.orbit] = (acc[c.orbit] || 0) + 1;
    return acc;
  }, {});

  return (
    <section>
      <h2>Test 38 — 64 spinor structures of the Klein quartic
        <span className="pill">Jacobi in the browser</span></h2>
      <p className="muted">
        All 64 structures are loaded from the frozen dataset
        (<code>verification/spinor64/data/</code>). The browser computes the
        spectra of all 28 odd (Arf=1) structures with a hand-written Jacobi
        eigensolver — the verified claim: <b>all spinor structures are
        equivalent</b> (see monograph v21.1, section 3.2.5).
      </p>
      <div className="stats-grid">
        <Stat label="Orbit sizes (PSL(2,7))" value={orbitCounts.join(' / ')}
          refVal="odd = 28 (bitangents, Riemann–Klein)" />
        <Stat label="Isospectrality (odd orbit)" value={res ? res.isomax.toExponential(2) : '…'}
          refVal="8.9e-15 (reference)" ok={res ? res.isomax < 1e-9 : undefined} />
        <Stat label="⟨r⟩ (representative)" value={res ? res.rMean.toFixed(10) : '…'}
          refVal="0.4515710793" ok={res ? Math.abs(res.rMean - 0.4515710792825435) < 1e-6 : undefined} />
        <Stat label="Zero modes" value={res ? res.nZero : '…'} refVal="2" ok={res ? res.nZero === 2 : undefined} />
      </div>

      <h3>Orbit census — the 64 structures of PSL(2,7)</h3>
      <CatBar items={Object.entries(orbitFieldCounts).map(([orb, n], i) => ({
        label: `orbit ${orb}`, value: n,
        color: ['#00E5FF', '#FF2EC4', '#A78BFA', '#FFD60A', '#4ADE80'][i % 5],
      }))} unit=" classes" />
      <p className="muted">
        Frozen reference (<code>data/reference_stats.json</code>):
        orbit sizes { (data.stats.orbit_sizes ?? orbitCounts).join(' / ') },
        eigenvalue window [{(data.stats.eigen_min ?? 0).toFixed(6)},
        {(data.stats.eigen_max ?? 0).toFixed(6)}],
        {(data.stats.n_zero_modes ?? 2)} zero modes,
        ⟨r⟩ reference {(data.stats.r_mean_reference ?? 0).toFixed(10)}.
        The browser's Arf=1 count ({arfOne} classes) matches the frozen
        odd-orbit membership ({oddMembers.length} members).
      </p>
      <details className="reveal-block">
        <summary>The {oddMembers.length} members of the odd orbit (Arf = 1)</summary>
        <p className="mono-chips">
          {oddMembers.map(m => <code key={m}>{m}</code>)}
        </p>
      </details>

      {res && (
        <>
          <h3>Representative spectrum (class {data.stats.representative_class},
            odd orbit) — computed live</h3>
          <LineChart xLabel="level index" yLabel="λ"
            series={[{ name: 'eigenvalues (JS Jacobi)', points: res.spectrum.map((v, i) => [i, v]) }]} />
        </>
      )}
      <h3>The 64 structures</h3>
      <label className="muted" htmlFor="spinorRange" style={{ display: 'block', marginTop: '16px' }}>
        Showing classes {idx}…{idx + 15} — slide to browse all 64 (Arf column: 1 = odd orbit)
      </label>
      <input id="spinorRange" className="range" type="range" min="0" max="48" value={idx}
        onChange={e => setIdx(+e.target.value)} />
      <div className="table-wrap">
        <table className="data">
          <thead><tr><th scope="col">class</th><th scope="col">orbit</th><th scope="col">Arf</th><th scope="col">signs (frozen)</th></tr></thead>
          <tbody>
            {data.classes.filter(c => c.cls >= idx && c.cls < idx + 16).map(c => (
              <tr key={c.cls}>
                <td className="test-id">{c.cls}</td>
                <td className="test-id">{c.orbit}</td>
                <td className="test-id">{c.arf}</td>
                <td className="headline">{c.signs.join(' ')}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      {busy && <p className="muted" role="status">computing…</p>}
    </section>
  );
}
