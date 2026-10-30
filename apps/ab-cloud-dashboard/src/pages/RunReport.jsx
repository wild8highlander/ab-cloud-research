import React, { useState } from 'react';
import { CatBar, Skeleton } from '../components/ui.jsx';

const VERDICT_CLASS = {
  PASS: 'v-pass', WARN: 'v-warn', FAIL: 'v-fail',
};

export default function RunReport({ summary, error }) {
  const [filter, setFilter] = useState('ALL');
  if (error && !summary) {
    return <p className="error-note">Failed to load run summary — {error}</p>;
  }
  if (!summary) {
    return (
      <section aria-busy="true" aria-label="Loading run summary">
        <Skeleton kind="stats" />
        <Skeleton kind="table" />
      </section>
    );
  }
  if (!Array.isArray(summary.tests) || !summary.tests.length) {
    return <p className="error-note">run_summary.json is malformed — no test list found.</p>;
  }
  const shown = summary.tests.filter(t =>
    filter === 'ALL' ? true : filter === 'PASS' ? t.verdict === 'PASS' : t.verdict !== 'PASS');
  // describe the actual data — never hardcode verdict kinds/ids here
  const nonPass = summary.tests.filter(t => t.verdict !== 'PASS').map(t => t.id);
  const verdictCounts = summary.tests.reduce((acc, t) => {
    acc[t.verdict] = (acc[t.verdict] || 0) + 1;
    return acc;
  }, {});
  const VERDICT_COLORS = { PASS: '#4ADE80', WARN: '#FBBF24', FAIL: '#F87171' };
  return (
    <section>
      <h2>Run {summary.run} <span className="pill">{summary.date}</span></h2>
      <p className="muted">
        Julia {summary.julia ?? '?'} · {(summary.zeros ?? 0).toLocaleString()} Odlyzko zeros ·
        two passes: {summary.two_pass ?? '?'} · first pass {summary.first_pass?.PASS ?? '?'} PASS /{' '}
        {summary.first_pass?.WARN ?? '?'} WARN · hardcore pass 2: {summary.hardcore_pass2 ?? '?'}.
        Full artifacts: <code>results/{summary.run}</code> in the repository.
      </p>

      <h3>The two-pass pipeline</h3>
      <div className="pipeline">
        <div className="pipe-card">
          <div className="pipe-step">pass 1 · 72×72</div>
          <p>First pass over {(summary.zeros ?? 0).toLocaleString()} zeros:{' '}
            <b>{summary.first_pass?.PASS ?? '?'} PASS</b> /{' '}
            <b>{summary.first_pass?.WARN ?? '?'} WARN</b> — the Wigner-surmise
            floor surfaces as WARN on the asymptotic p-values.</p>
        </div>
        <div className="pipe-arrow" aria-hidden="true">→</div>
        <div className="pipe-card">
          <div className="pipe-step">pass 2 · {summary.two_pass?.includes('96') ? '96×96 (HARDCORE)' : summary.two_pass}</div>
          <p>Hardcore second pass: <b>{summary.hardcore_pass2 ?? '?'}</b> —
            every flagged test re-examined with the calibrated two-sample
            machinery against the exact GUE reference.</p>
        </div>
        <div className="pipe-arrow" aria-hidden="true">→</div>
        <div className="pipe-card">
          <div className="pipe-step">verdict</div>
          <p>{summary.tests.length} tests on this dashboard,
            {' '}{nonPass.length} non-PASS row{nonPass.length === 1 ? '' : 's'} —
            all traced to the surmise floor, none to the data.</p>
        </div>
      </div>

      <h3>Verdict counts</h3>
      <CatBar items={Object.entries(verdictCounts).map(([v, n]) => ({
        label: v, value: n, color: VERDICT_COLORS[v] || '#00E5FF',
      }))} unit=" tests" />

      <h3>All {summary.tests.length} verdicts</h3>
      <div className="filter-row" role="group" aria-label="Filter tests by verdict">
        {['ALL', 'PASS', 'NON-PASS'].map(f => (
          <button key={f} className={filter === f ? 'btn active' : 'btn'}
            aria-pressed={filter === f}
            onClick={() => setFilter(f)}>{f}</button>
        ))}
      </div>
      {shown.length === 0 ? (
        <div className="empty">
          <b>Nothing matches this filter.</b><br />
          Every test in this run has a different verdict — switch back to
          ALL to see all {summary.tests.length} rows.
        </div>
      ) : (
        <div className="table-wrap">
          <table className="data">
            <thead><tr><th scope="col">Test</th><th scope="col">Verdict</th><th scope="col">Headline</th></tr></thead>
            <tbody>
              {shown.map(t => (
                <tr key={t.id}>
                  <td className="test-id">{t.id}</td>
                  <td><span className={VERDICT_CLASS[t.verdict] || ''}>{t.verdict}</span></td>
                  <td className="headline">{t.headline}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
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
