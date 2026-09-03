import React, { useEffect, useMemo, useState } from 'react';

const VERDICT_CLASS = {
  PASS: 'v-pass', WARN: 'v-warn', FAIL: 'v-fail',
};

export default function RunReport({ summary }) {
  const [filter, setFilter] = useState('ALL');
  if (!summary) return <p className="muted">Loading run summary…</p>;
  const shown = summary.tests.filter(t =>
    filter === 'ALL' ? true : filter === 'WARN' ? t.verdict !== 'PASS' : t.verdict === 'PASS');
  return (
    <section>
      <h2>Run {summary.run} <span className="pill">{summary.date}</span></h2>
      <p className="muted">
        Julia {summary.julia} · {summary.zeros.toLocaleString()} Odlyzko zeros ·
        two-pass {summary.two_pass} · first pass {summary.first_pass.PASS} PASS /{' '}
        {summary.first_pass.WARN} WARN · hardcore pass-2: {summary.hardcore_pass2}.
        Full artifacts: <code>results/{summary.run}/</code> in the repository.
      </p>
      <div className="filter-row">
        {['ALL', 'PASS', 'WARN'].map(f => (
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
      <p className="muted">
        The five WARN verdicts (tests 4, 5, 6, 11, 12) are the Wigner-surmise
        floor: at N = 50,000 the asymptotic p-values vanish while the
        suite's own two-sample machinery against the exact GUE reference
        passes at the same data (see the monograph, section 3.2, and the
        CALIBRATED verdict lines in the run logs).
      </p>
    </section>
  );
}
