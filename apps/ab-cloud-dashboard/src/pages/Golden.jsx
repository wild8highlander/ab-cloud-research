import React, { useEffect, useMemo, useState } from 'react';
import { Stat, Skeleton } from '../components/ui.jsx';

/* Golden values — the frozen reference constants of the suite
 * (verification/data/abcloud_golden.json): the exact numbers every
 * implementation (Julia, Python, Fortran, Rust, …) must reproduce.
 * Pure reading: search + group filter over a static JSON. */

const fmtVal = (v) => {
  if (v == null) return '—';
  if (typeof v === 'number') {
    if (Number.isInteger(v)) return v.toLocaleString('en-US');
    if (v !== 0 && (Math.abs(v) < 1e-4 || Math.abs(v) >= 1e7)) return v.toExponential(6);
    return String(v);
  }
  return JSON.stringify(v);
};

export default function Golden() {
  const [data, setData] = useState(null);
  const [err, setErr] = useState('');
  const [query, setQuery] = useState('');
  const [group, setGroup] = useState('ALL');

  useEffect(() => {
    fetch('data/golden_values.json')
      .then(r => { if (!r.ok) throw new Error(`golden_values.json: HTTP ${r.status}`); return r.json(); })
      .then(setData)
      .catch(e => setErr(`Failed to load the golden values — ${e.message}`));
  }, []);

  const { rows, groups, nValues } = useMemo(() => {
    if (!data) return { rows: [], groups: [], nValues: 0 };
    const out = [];
    for (const [g, vals] of Object.entries(data)) {
      if (g.startsWith('_')) continue;
      if (vals && typeof vals === 'object' && !Array.isArray(vals)) {
        for (const [k, v] of Object.entries(vals)) out.push({ group: g, key: k, value: v });
      } else {
        out.push({ group: g, key: '(value)', value: vals });
      }
    }
    return {
      rows: out,
      groups: [...new Set(out.map(r => r.group))].sort(),
      nValues: out.length,
    };
  }, [data]);

  if (err) return <p className="error-note">{err}</p>;
  if (!data) {
    return (
      <section aria-busy="true" aria-label="Loading golden values">
        <h2>Golden values — the frozen reference constants <span className="pill">SHA-256</span></h2>
        <p className="muted">Loading <code>verification/data/abcloud_golden.json</code>…</p>
        <Skeleton kind="stats" />
        <Skeleton kind="table" />
      </section>
    );
  }

  const q = query.trim().toLowerCase();
  const shown = rows.filter(r =>
    (group === 'ALL' || r.group === group) &&
    (!q || r.group.toLowerCase().includes(q) || r.key.toLowerCase().includes(q)
      || String(r.value).toLowerCase().includes(q)));

  return (
    <section>
      <h2>Golden values — the frozen reference constants
        <span className="pill">SHA-256</span></h2>
      <p className="muted">
        Every number in <code>verification/data/abcloud_golden.json</code> is a
        reference the 10-language verification stack must reproduce bit-for-bit
        (within its own tolerance protocol): Δ₃, K(t) checkpoints, Σ², the
        Byers–Yang flux defect A₂, AICc, b(N) ladder and more —
        {' '}{nValues} values in {groups.length} groups.
      </p>

      <div className="stats-grid">
        <Stat label="Groups" value={groups.length} refVal="top-level keys of the golden JSON" />
        <Stat label="Values" value={nValues} refVal="leaf entries, all frozen" />
        <Stat label="Shown" value={shown.length}
          refVal={query ? `filtered by “${query}”` : group !== 'ALL' ? `group ${group}` : 'no filter'} />
        <Stat label="Source" value="verification/data/"
          refVal="abcloud_golden.json · 12.9 KB" />
      </div>

      <div className="filter-row" role="group" aria-label="Filter golden values">
        <input type="search" className="search" placeholder="Search group, key or value…"
          value={query} aria-label="Search golden values"
          onChange={e => setQuery(e.target.value)} />
        {['ALL', ...groups].map(g => (
          <button key={g} className={group === g ? 'btn active' : 'btn'}
            aria-pressed={group === g} onClick={() => setGroup(g)}>{g}</button>
        ))}
      </div>

      {shown.length === 0 ? (
        <div className="empty">
          <b>Nothing matches this filter.</b><br />
          Try a shorter query — for example “K” or “L=50” — or reset the group to ALL.
        </div>
      ) : (
        <div className="table-wrap">
          <table className="data">
            <thead>
              <tr><th scope="col">group</th><th scope="col">key</th><th scope="col">value</th></tr>
            </thead>
            <tbody>
              {shown.slice(0, 240).map((r, i) => (
                <tr key={`${r.group}/${r.key}/${i}`}>
                  <td className="test-id">{r.group}</td>
                  <td className="test-id">{r.key}</td>
                  <td className="headline">{fmtVal(r.value)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
      {shown.length > 240 && (
        <p className="muted">Showing the first 240 of {shown.length} matching rows — refine the filter to narrow the table.</p>
      )}
    </section>
  );
}
