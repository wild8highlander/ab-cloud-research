import React, { useEffect, useState } from 'react';
import { LineChart, BarChart, Stat, Skeleton } from '../components/ui.jsx';

/* Spectra — the post-run enrichment of RH_Auto_5000_L64_s5.
 * Every number and every curve is fetched from frozen artifacts generated
 * by the Julia suite (results/RH_Sweep_Pro_Enrichment/): no numerics run
 * in the browser on this tab, the browser only draws what the suite froze. */

const dropNulls = (xs, ys) => {
  const pts = [];
  for (let i = 0; i < xs.length && i < ys.length; i++) {
    if (ys[i] != null && xs[i] != null) pts.push([xs[i], ys[i]]);
  }
  return pts;
};

const fmt = (v, digits = 4) =>
  v == null ? '—' : typeof v === 'number' ? v.toFixed(digits) : String(v);

export default function Spectra() {
  const [data, setData] = useState(null);
  const [err, setErr] = useState('');

  useEffect(() => {
    const get = (url) => fetch(url).then(r => {
      if (!r.ok) throw new Error(`${url}: HTTP ${r.status}`);
      return r.json();
    });
    Promise.all([
      get('data/enrichment_summary.json'),
      get('data/enrichment_curves.json'),
    ]).then(([summary, curves]) => setData({ summary, curves }))
      .catch(e => setErr(`Failed to load the enrichment artifacts — ${e.message}`));
  }, []);

  if (err) return <p className="error-note">{err}</p>;
  if (!data) {
    return (
      <section aria-busy="true" aria-label="Loading enrichment artifacts">
        <h2>Enrichment run — AB-cloud vs ζ zeros vs GUE <span className="pill">frozen curves</span></h2>
        <p className="muted">Loading the frozen curves of <code>results/RH_Sweep_Pro_Enrichment/</code>…</p>
        <Skeleton kind="stats" />
        <Skeleton kind="chart" />
        <Skeleton kind="chart" />
      </section>
    );
  }

  const { summary, curves } = data;
  const h = summary.headline ?? {};
  const en = summary.post_run_enrichment ?? {};
  const kf = summary.key_finding ?? {};
  const best = h.best_config ?? {};

  const meta = curves._meta ?? {};
  const R2 = curves.R2, K = curves.K, S2 = curves.S2, D3 = curves.D3;
  const PS = curves.ps, RA = curves.ratio, SUP = curves.superposition;

  return (
    <section>
      <h2>Enrichment run — AB-cloud vs ζ zeros vs GUE
        <span className="pill">{summary.run}</span></h2>
      <p className="muted">
        The full post-run enrichment of {summary.run} ({summary.generated}), frozen in{' '}
        <code>results/RH_Sweep_Pro_Enrichment/</code>: {en.curves ?? 7} curves,{' '}
        {en.figures_new ?? 7} new figures and {en.animations_gif ?? 5} GIF animations
        produced by <code>RH_Results_Enricher.jl</code>. The operator was built with
        α = 1/π, W = {fmt(best.W, 1)}, σ = {fmt(best.sigma, 1)}, L = {best.L},
        superposition of {best.n_seeds} seeds — {(h.n_eigs ?? 0).toLocaleString()} eigenvalues
        against {(h.n_zeta_zeros ?? 0).toLocaleString()} ζ zeros.
      </p>

      <div className="stats-grid">
        <Stat label="Composite score" value={`${fmt(h.composite_score, 3)} / ${h.score_max ?? 100}`}
          refVal={`tests ${h.tests_passed ?? '—'} · RMT core ${h.rmt_core_tests ?? '—'}`} />
        <Stat label="⟨r⟩ per seed" value={fmt(h.r_mean_per_seed)}
          refVal={`GUE ${fmt(h.R_GUE)} · Δr = ${fmt(h.delta_r_vs_GUE, 5)}`}
          ok={h.delta_r_vs_GUE != null && h.delta_r_vs_GUE < 0.01} />
        <Stat label="Ratio class" value={h.r_class ?? '—'}
          refVal="d_GUE = 0.00039 « d_GOE = 0.064" />
        <Stat label="K correlation" value={`${fmt(h.K_corr_zeta)} ζ / ${fmt(h.K_corr_GUE)} GUE`}
          refVal="form-factor agreement" />
        <Stat label="R² RMS vs GUE" value={fmt(h.R2_rms_GUE)}
          refVal={`Poisson ${fmt(h.R2_rms_Poisson)}`}
          ok={h.R2_rms_GUE != null && h.R2_rms_GUE < h.R2_rms_Poisson} />
        <Stat label="GUE error floor" value={fmt(en.gue_control_floor_R2_rms)}
          refVal="run R² RMS below floor ⇒ indistinguishable from GUE"
          ok={en.gue_control_floor_R2_rms != null && h.R2_rms_GUE != null
            && h.R2_rms_GUE < en.gue_control_floor_R2_rms} />
      </div>

      <h3>R₂(s) — two-level cluster function</h3>
      <LineChart xLabel="s" yLabel="R₂(s)"
        series={[
          { name: 'AB-cloud', points: dropNulls(R2.s, R2.ab) },
          { name: 'ζ zeros', points: dropNulls(R2.s, R2.zz) },
          { name: 'GUE', points: dropNulls(R2.s, R2.gue) },
          { name: 'Poisson', points: dropNulls(R2.s, R2.poi) },
        ]} />

      <h3>K(t) — spectral form factor</h3>
      <LineChart xLabel="t" yLabel="K(t)"
        series={[
          { name: 'AB-cloud', points: dropNulls(K.t, K.ab) },
          { name: 'ζ zeros', points: dropNulls(K.t, K.zz) },
          { name: 'GUE', points: dropNulls(K.t, K.gue) },
          { name: 'Poisson', points: dropNulls(K.t, K.poi) },
        ]} />

      <h3>Σ²(L) — number variance</h3>
      <LineChart logX xLabel="L" yLabel="Σ²(L)"
        series={[
          { name: 'AB-cloud', points: dropNulls(S2.L, S2.ab) },
          { name: 'ζ zeros', points: dropNulls(S2.L, S2.zz) },
          { name: 'GUE', points: dropNulls(S2.L, S2.gue) },
          { name: 'Poisson', points: dropNulls(S2.L, S2.poi) },
        ]} />

      <h3>Δ₃(L) — spectral rigidity (Dyson–Mehta)</h3>
      <LineChart logX xLabel="L" yLabel="Δ₃(L)"
        series={[
          { name: 'AB-cloud', points: dropNulls(D3.L, D3.ab) },
          { name: 'ζ zeros', points: dropNulls(D3.L, D3.zz) },
        ]} />

      <h3>p(s) — nearest-neighbour spacing + survival E(s)</h3>
      <LineChart xLabel="s" yLabel="p(s)"
        series={[
          { name: 'AB-cloud', points: dropNulls(PS.s, PS.ab) },
          { name: 'GUE', points: dropNulls(PS.s, PS.gue) },
          { name: 'Poisson', points: dropNulls(PS.s, PS.poi) },
        ]} />

      <h3>E(s) — survival of the AB-cloud spacings</h3>
      <LineChart xLabel="s" yLabel="E(s)"
        series={[{ name: 'E(s) — AB-cloud', points: dropNulls(PS.s, PS.E) }]} />

      <h3>Histogram of r = min/max (file-union of 5 seeds)</h3>
      <BarChart xLabel="r" yLabel="density"
        points={dropNulls(RA.r.slice(1), RA.hist)} />

      <h3>Superposition of m independent GUE spectra — ⟨r⟩(m), ⟨r̃⟩(m)</h3>
      <LineChart xLabel="m" yLabel="⟨r⟩ / ⟨r̃⟩"
        series={[
          { name: '⟨r⟩(m)', points: dropNulls(SUP.m, SUP.r) },
          { name: '⟨r̃⟩(m)', points: dropNulls(SUP.m, SUP.rtilde) },
        ]} />
      <p className="muted">
        <b>Key finding, kept traceable:</b> {kf.what}. Consequence: {kf.consequence}.
        Verification: {kf.verification}. Fix: {kf.fix}.
      </p>

      <h3>Only failed test of the run</h3>
      <p className="muted">{h.only_failed_test}</p>
      <p className="muted">
        Enrichment verdict: {en.verdict}. Code fixes applied by the enricher: {en.code_fixes}.
        Curves source: <code>{meta.source}</code> ({meta.generated}).
      </p>
    </section>
  );
}
