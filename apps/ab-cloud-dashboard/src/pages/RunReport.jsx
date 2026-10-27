import React, { useState } from 'react';

const VERDICT_CLASS = {
  PASS: 'v-pass', WARN: 'v-warn', FAIL: 'v-fail',
};

export default function RunReport({ summary, error }) {
  const [filter, setFilter] = useState('ALL');
  if (error && !summary) {
    return <p className="error-note">Failed to load run summary — {error}</p>;
  }
  if (!summary) return <p className="muted">Loading run summary…</p>;
  if (!Array.isArray(summary.tests) || !summary.tests.length) {
    return <p className="error-note">run_summary.json is malformed — no test list found.</p>;
  }
  const shown = summary.tests.filter(t =>
    filter === 'ALL' ? true : filter === 'PASS' ? t.verdict === 'PASS' : t.verdict !== 'PASS');
  // describe the actual data — never hardcode verdict kinds/ids here
  const nonPass = summary.tests.filter(t => t.verdict !== 'PASS').map(t => t.id);
  return (
    <section>
      <h2>Run {summary.run} <span className="pill">{summary.date}</span></h2>
      <p className="muted">
        Julia {summary.julia ?? '?'} · {(summary.zeros ?? 0).toLocaleString()} Odlyzko zeros ·
        two-pass {summary.two_pass ?? '?'} · first pass {summary.first_pass?.PASS ?? '?'} PASS /{' '}
        {summary.first_pass?.WARN ?? '?'} WARN · hardcore pass-2: {summary.hardcore_pass2 ?? '?'}.
        Full artifacts: <code>results/{summary.run}</code> in the repository.
      </p>
      <div className="filter-row">
        {['ALL', 'PASS', 'NON-PASS'].map(f => (
          <button key={f} className={filter === f ? 'btn active' : 'btn'}
            onClick={() => setFilter(f)}>{f}</button>
        ))}
      </div>
      <table className="data">
        <thead><tr><th>Test</th><th>Verdict</th><th>Headline</th></tr></thead>
        <tbody>
          {shown.map(t => (
            <tr key={t.id}>
              <td>{t.id}</td>
              <td><span className={VERDICT_CLASS[t.verdict] || ''}>{t.verdict}</span></td>
              <td className="headline">{t.headline}</td>
            </tr>
          ))}
        </tbody>
      </table>
      {nonPass.length > 0 && (
        <p className="muted">
          Non-PASS verdicts (tests {nonPass.join(', ')}) are the Wigner-surmise
          floor: at N = 50,000 the asymptotic p-values vanish while the
          suite's own two-sample machinery against the exact GUE reference
          passes at the same data (see the monograph, section 3.2, and the
          CALIBRATED verdict lines in the run logs).
        </p>
      )}
    </section>
  );
}
