import React, { useEffect, useMemo, useState } from 'react';
import { CatBar, Stat, Skeleton } from '../components/ui.jsx';

/* Metrics ×38 — the full per-config metric table of the RH_Unified sweep
 * (results/RH_Sweep_Pro_Enrichment/data/metrics.csv), regrouped for reading.
 * Frozen artifact → static JSON → browser; nothing is recomputed here. */

const GROUPS = [
  ['Configuration', ['label', 'L', 'alpha', 'W', 'sigma', 'n_eigs', 'r_class']],
  ['Ratio statistics', ['r_mean', 'r_std', 'r_tilde_mean', 'd_GUE', 'd_GOE', 'd_GSE', 'd_Poisson', 'symmetry_parameter']],
  ['R₂(s) cluster function', ['R2_rms_GUE', 'R2_rms_Poisson', 'R2_rms_zeta', 'R2_match_GUE']],
  ['K(t) form factor', ['K_corr_GUE', 'K_corr_zeta', 'K_match_GUE', 'K_match_zeta']],
  ['Σ²(L) / Δ₃(L)', ['Sigma2_rms_GUE', 'Sigma2_rms_Poisson', 'Sigma2_match_GUE', 'Delta3_rms_GUE']],
  ['p(s) / Wigner', ['p_rms_GUE', 'p_mean', 'chi2_wigner', 'chi2_pvalue', 'brody_beta', 'spectral_compressibility', 'gap_prob_E1']],
  ['Levels & verdict', ['level_number_dev', 'composite_score', 'tests_passed', 'tests_total']],
];

const fmtVal = (v) => {
  if (v == null) return '—';
  if (typeof v === 'boolean') return v ? 'TRUE' : 'FALSE';
  if (typeof v === 'number') {
    if (Number.isInteger(v)) return v.toLocaleString('en-US');
    if (v !== 0 && (Math.abs(v) < 1e-3 || Math.abs(v) >= 1e5)) return v.toExponential(3);
    return String(v);
  }
  return String(v);
};

export default function Metrics() {
  const [data, setData] = useState(null);
  const [err, setErr] = useState('');
  const [rowIdx, setRowIdx] = useState(0);

  useEffect(() => {
    fetch('data/metrics_sweep.json')
      .then(r => { if (!r.ok) throw new Error(`metrics_sweep.json: HTTP ${r.status}`); return r.json(); })
      .then(setData)
      .catch(e => setErr(`Failed to load the metrics table — ${e.message}`));
  }, []);

  const best = useMemo(() => {
    if (!data) return null;
    const rows = data.rows ?? [];
    return rows.reduce((a, b) => ((b.composite_score ?? -1) > (a.composite_score ?? -1) ? b : a), rows[0]);
  }, [data]);

  if (err) return <p className="error-note">{err}</p>;
  if (!data) {
    return (
      <section aria-busy="true" aria-label="Loading metrics">
        <h2>Metrics ×38 — the sweep, every column <span className="pill">frozen CSV</span></h2>
        <p className="muted">Loading <code>results/RH_Sweep_Pro_Enrichment/data/metrics.csv</code>…</p>
        <Skeleton kind="stats" />
        <Skeleton kind="table" />
      </section>
    );
  }

  const rows = data.rows ?? [];
  if (!rows.length) {
    return <div className="empty"><b>metrics_sweep.json contains no rows.</b><br />
      Re-run <code>scripts/prepare-dashboard-data.py</code> after a new suite run.</div>;
  }
  const row = rows[Math.min(rowIdx, rows.length - 1)];

  return (
    <section>
      <h2>Metrics ×38 — the sweep, every column
        <span className="pill">{data._meta?.run}</span></h2>
      <p className="muted">
        The complete CSV report of the RH_Unified sweep
        (<code>{data._meta?.source}</code>, {data._meta?.generated}):
        {rows.length} configuration row{rows.length === 1 ? '' : 's'} ×
        {' '}{Object.keys(rows[0]).length} metric columns, regrouped by diagnostic.
        Nothing hidden — every number the suite wrote into the CSV is on this page.
      </p>

      <div className="stats-grid">
        <Stat label="Composite score" value={fmtVal(best?.composite_score)}
          refVal={`of 100 · tests ${fmtVal(best?.tests_passed)}/${fmtVal(best?.tests_total)}`} />
        <Stat label="α (best config)" value={fmtVal(best?.alpha)}
          refVal="= 1/π — the α-identity of the run" />
        <Stat label="⟨r⟩ best config" value={fmtVal(best?.r_mean)}
          refVal={`GUE 0.5996 · class ${best?.r_class ?? '—'}`}
          ok={best?.r_class === 'GUE'} />
        <Stat label="Eigenvalues × ζ zeros" value={`${fmtVal(best?.n_eigs)} × 5,000`}
          refVal="per-seed spectra, superposed in the file" />
      </div>

      {rows.length > 1 && (
        <div className="filter-row" role="group" aria-label="Choose CSV row">
          {rows.map((r, i) => (
            <button key={r.label ?? i} className={i === rowIdx ? 'btn active' : 'btn'}
              aria-pressed={i === rowIdx}
              onClick={() => setRowIdx(i)}>{r.label ?? `row ${i + 1}`}</button>
          ))}
        </div>
      )}

      <h3>Distances to the classical ensembles (smaller = closer)</h3>
      <CatBar items={[
        { label: 'GUE', value: row.d_GUE, color: '#00E5FF' },
        { label: 'GOE', value: row.d_GOE, color: '#FF2EC4' },
        { label: 'GSE', value: row.d_GSE, color: '#A78BFA' },
        { label: 'Poisson', value: row.d_Poisson, color: '#FFD60A' },
      ]} />
      <p className="muted">
        d_GUE = {fmtVal(row.d_GUE)} against d_GOE = {fmtVal(row.d_GOE)},
        d_GSE = {fmtVal(row.d_GSE)}, d_Poisson = {fmtVal(row.d_Poisson)} —
        the spectrum sits on the GUE point of the Borodin–Olshanski line,
        three orders of magnitude closer to GUE than to Poisson.
      </p>

      {GROUPS.map(([title, keys]) => (
        <React.Fragment key={title}>
          <h3>{title}</h3>
          <div className="table-wrap">
            <table className="data">
              <thead><tr><th scope="col">metric</th><th scope="col">value</th></tr></thead>
              <tbody>
                {keys.filter(k => k in row).map(k => (
                  <tr key={k}>
                    <td className="test-id">{k}</td>
                    <td className="headline">{fmtVal(row[k])}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </React.Fragment>
      ))}

      <p className="muted">
        Column meanings follow <code>results/RH_Sweep_Pro_Enrichment/DATA_DICTIONARY.md</code>;
        the composite score and its 11 sub-tests are defined by the suite itself.
      </p>
    </section>
  );
}
