import React, { useEffect, useState } from 'react';
import { CatBar, Stat, Skeleton } from '../components/ui.jsx';

/* GUE control — the error floor of the methodology (method Т34 gue_control).
 * Answers the reviewer's question: how much of the observed agreement is the
 * pipeline itself? A GUE simulation split into halves, run through the SAME
 * pipeline, gives the RMS floor; the run's R² RMS sits BELOW it. */

const fmt = (v, d = 6) => (v == null ? '—' : typeof v === 'number' ? v.toFixed(d) : String(v));

export default function Control() {
  const [data, setData] = useState(null);
  const [err, setErr] = useState('');

  useEffect(() => {
    fetch('data/gue_control.json')
      .then(r => { if (!r.ok) throw new Error(`gue_control.json: HTTP ${r.status}`); return r.json(); })
      .then(setData)
      .catch(e => setErr(`Failed to load the GUE control — ${e.message}`));
  }, []);

  if (err) return <p className="error-note">{err}</p>;
  if (!data) {
    return (
      <section aria-busy="true" aria-label="Loading GUE control">
        <h2>GUE control — the error floor of the pipeline <span className="pill">Т34</span></h2>
        <p className="muted">Loading <code>results/RH_Sweep_Pro_Enrichment/data/gue_control.json</code>…</p>
        <Skeleton kind="stats" />
        <Skeleton kind="chart" />
      </section>
    );
  }

  const meta = data.meta ?? {};
  const sup = data.superposition_check ?? {};

  return (
    <section>
      <h2>GUE control — the error floor of the pipeline
        <span className="pill">method Т34</span></h2>
      <p className="muted">
        {meta.what}. {meta.method}. Pipeline: {meta.pipeline}. Seed: {meta.seed}.
      </p>

      <div className="stats-grid">
        <Stat label="GUE-vs-GUE floor (R² RMS)" value={fmt(data.floor_R2_rms_GUE_vs_GUE)}
          refVal="two halves of one GUE simulation, same pipeline" />
        <Stat label="Run R² RMS (per-seed AB vs GUE)" value={fmt(data.run_R2_rms_AB_vs_GUE_perseed)}
          refVal="below the floor ⇒ statistically indistinguishable"
          ok={data.run_R2_rms_AB_vs_GUE_perseed != null
            && data.floor_R2_rms_GUE_vs_GUE != null
            && data.run_R2_rms_AB_vs_GUE_perseed < data.floor_R2_rms_GUE_vs_GUE} />
        <Stat label="E₁ AB-union" value={fmt(data.E1_AB_union)}
          refVal={`GUE surmise ${fmt(data.E1_GUE_surmise)} · exact tabulated ${fmt(data.E1_GUE_exact_tabulated)}`} />
        <Stat label="E₁ per-seed run" value={fmt(data.run_E1_perseed)}
          refVal="the run's own value (E(s=1)=0.521, the only failed test)" />
      </div>

      <h3>R² RMS — the run against the floor</h3>
      <CatBar items={[
        { label: 'run per-seed vs GUE', value: data.run_R2_rms_AB_vs_GUE_perseed, color: '#00E5FF' },
        { label: 'GUE-vs-GUE floor', value: data.floor_R2_rms_GUE_vs_GUE, color: '#4ADE80' },
        { label: 'union vs GUE theory', value: data.recomputed_R2_rms_ABunion_vs_GUE_theory, color: '#A78BFA' },
        { label: 'union vs Poisson', value: data.recomputed_R2_rms_ABunion_vs_Poisson, color: '#FFD60A' },
        { label: 'union vs ζ zeros', value: data.recomputed_R2_rms_ABunion_vs_zeta, color: '#FF2EC4' },
      ]} />
      <p className="muted">
        <b>Verdict:</b> the per-seed R² RMS of the run (0.0210) lies <i>below</i> the
        GUE-splitting floor (0.0256) — the AB-cloud is statistically
        indistinguishable from a GUE realization of the same volume. The union
        rows are the post-hoc file-level metrics and are explained by the
        superposition below, not by a failure of the method.
      </p>

      <h3>K(t) correlations and Σ² deviations</h3>
      <div className="stats-grid">
        <Stat label="K corr · ζ vs GUE theory" value={fmt(data.K_corr_zeta_GUE_theory)}
          refVal="the zeros themselves track GUE" />
        <Stat label="K corr · run per-seed (ζ / GUE)" value={`${fmt(data.run_K_corr_zeta_perseed)} / ${fmt(data.run_K_corr_GUE_perseed)}`}
          refVal="headline numbers of the run" />
        <Stat label="K corr · AB-union (ζ / GUE)" value={`${fmt(data.K_corr_ABunion_zeta)} / ${fmt(data.K_corr_ABunion_GUE_theory)}`}
          refVal="degraded by the m=5 union — expected" />
        <Stat label="Σ² RMS union vs GUE (L≥10)" value={fmt(data.Sigma2_rms_ABunion_GUE_Lge10, 4)}
          refVal={`Poisson: ${fmt(data.Sigma2_rms_ABunion_Poisson_Lge10, 2)} — off by an order of magnitude`} />
      </div>

      <h3>Superposition check — why the file-union reads m = 5</h3>
      <div className="table-wrap">
        <table className="data">
          <thead>
            <tr><th scope="col">quantity</th><th scope="col">GUE simulation</th><th scope="col">file (union of 5 seeds)</th></tr>
          </thead>
          <tbody>
            <tr>
              <td className="test-id">⟨r⟩, m = 1</td>
              <td className="headline">{fmt(sup.sim_r_m1)}</td>
              <td className="headline">— (single-seed run: 0.59999)</td>
            </tr>
            <tr>
              <td className="test-id">⟨r⟩, m = 5</td>
              <td className="headline">{fmt(sup.sim_r_m5)}</td>
              <td className="headline">{fmt(data.file_union_r_mean)}</td>
            </tr>
            <tr>
              <td className="test-id">⟨r̃⟩, m = 5</td>
              <td className="headline">{fmt(sup.sim_rtilde_m5)}</td>
              <td className="headline">{fmt(data.file_union_rtilde_mean)}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <p className="muted">
        {sup.description}. {sup.verdict}. ζ-zero reference points:{' '}
        ⟨r⟩ = {fmt(data.zeta_r_mean)}, ⟨r̃⟩ = {fmt(data.zeta_rtilde_mean)}.
      </p>
      <p className="muted">
        <b>Caveat, kept verbatim:</b> {meta.caveat}
      </p>
    </section>
  );
}
