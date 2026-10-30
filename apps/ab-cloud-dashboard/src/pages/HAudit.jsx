import React, { useEffect, useState } from 'react';
import { Skeleton, CatBar } from '../components/ui.jsx';

const VERDICT_CLASS = { PASS: 'v-pass', WARN: 'v-warn', FAIL: 'v-fail' };
const STATUS_CLASS = { PASS: 'v-pass', WARN: 'v-warn', FAIL: 'v-fail' };

/* short label for each audit test — mirrors docs/audit_v2.0.3.md wording */
const FOCUS = {
  H1: 'prime-oscillation (Berry–Keating) fingerprint hunt: does the AB spectrum carry the Riemann–Weil log(p) comb?',
  H2: 'Weyl-law density on RAW eigenvalues: N(E) slope vs the expected quadratic growth',
  H3: 'power-law exponent of the real lattice spectrum (falsifies wrong scaling families)',
  H4: 'critical-q sharpness scan: is the "critical line" analogy actually sharp in q?',
  H5: 'large-ensemble × parameter-regime showdown: density × α 2×2 grid, model best-faith points',
  H6: 'self-adjointness and stability stress test of the operator',
  H7: 'sequence-level correlation between model eigenvalues and ζ zeros (Pearson/Spearman)',
  H8: 'all-numbers trace: integer comb, counting family, gap arithmetic end-to-end',
};

export default function HAudit() {
  const [data, setData] = useState(null);
  const [error, setError] = useState('');
  const [open, setOpen] = useState('H1');

  useEffect(() => {
    fetch('data/hp_audit.json')
      .then(r => { if (!r.ok) throw new Error(`hp_audit.json: HTTP ${r.status}`); return r.json(); })
      .then(setData)
      .catch(e => setError(e.message));
  }, []);

  if (error) return <p className="error-note">Failed to load the audit data — {error}</p>;
  if (!data) {
    return (
      <section aria-busy="true" aria-label="Loading audit">
        <Skeleton kind="stats" /><Skeleton kind="table" />
      </section>
    );
  }

  const tests = data.tests;
  const counts = tests.reduce((a, t) => { a[t.verdict] = (a[t.verdict] || 0) + 1; return a; }, {});
  const VERDICT_COLORS = { PASS: '#4ADE80', WARN: '#FBBF24', FAIL: '#F87171' };
  const nChecks = tests.reduce((a, t) => a + t.subchecks.length, 0);

  return (
    <section>
      <h2>Hilbert–Pólya deep audit <span className="pill">H1–H8 · {nChecks} sub-checks</span></h2>
      <p className="muted">
        The standalone <code>hp_audit_standalone.jl</code> battery: eight deep
        audit tests probing whether the AB-cloud operator behaves like the
        Hilbert–Pólya Hamiltonian — density growth, scaling exponents, critical
        line sharpness, stability, and correlation with ζ zeros. Detector-validity
        semantics: the battery verdict counts the <i>detector</i> outcome; the
        physics headlines live inside the sub-checks. Source:{' '}
        <code>results/Test H1-H8 hp_audit_standalone.jl/</code> (runs of
        2026-10-15, cumulative — each later run re-verified the earlier tests).
      </p>

      <h3>Battery at a glance</h3>
      <CatBar items={Object.entries(counts).map(([v, n]) => ({
        label: v, value: n, color: VERDICT_COLORS[v] || '#00E5FF',
      }))} unit=" tests" />

      <div className="stats-grid">
        {tests.map(t => (
          <button key={t.id} className={'stat hp-card' + (open === t.id ? ' active' : '')}
            onClick={() => setOpen(t.id)}
            aria-expanded={open === t.id}>
            <div className="stat-label">{t.id} <span className={STATUS_CLASS[t.verdict]}>{t.verdict}</span></div>
            <div className="hp-card-title">{t.title}</div>
            <div className="stat-ref">{FOCUS[t.id] || ''}</div>
          </button>
        ))}
      </div>

      {tests.filter(t => t.id === open).map(t => (
        <article key={t.id} className="panel hp-detail" aria-label={`${t.id} details`}>
          <h3>
            {t.id}. {t.title}{' '}
            <span className={VERDICT_CLASS[t.verdict] || ''}>{t.verdict}</span>
          </h3>
          {t.result && (
            <div className="result-line">
              <span className="result-tag">Result</span>
              <span className="headline">{t.result}</span>
            </div>
          )}
          {t.subchecks.length > 0 && (
            <div className="table-wrap" style={{ margin: '16px 0' }}>
              <table className="data">
                <thead>
                  <tr><th scope="col">sub-check</th><th scope="col">status</th><th scope="col">detail</th></tr>
                </thead>
                <tbody>
                  {t.subchecks.map((s, i) => (
                    <tr key={i}>
                      <td style={{ maxWidth: 220 }}>{s.check}</td>
                      <td><span className={STATUS_CLASS[s.status] || ''}>{s.status}</span></td>
                      <td className="headline" style={{ maxWidth: 560 }}>{s.detail}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
          {t.notes?.length > 0 && (
            <details className="reveal-block">
              <summary>Method notes ({t.notes.length})</summary>
              <div className="hp-notes">
                {t.notes.map((n, i) => <p key={i} className="muted">{n}</p>)}
              </div>
            </details>
          )}
          {t.params && (
            <details className="reveal-block">
              <summary>Parameters (preset of run {t.run})</summary>
              <pre className="console">{t.params}</pre>
            </details>
          )}
          <p className="muted">
            Frozen report:{' '}
            <a href={`https://github.com/wild8highlander/ab-cloud-research/blob/main/${t.report_path.replace('*', '')}`}
              target="_blank" rel="noopener">{t.report_path}</a>
          </p>
        </article>
      ))}
    </section>
  );
}
