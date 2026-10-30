import React, { useEffect, useMemo, useState } from 'react';
import { LineChart, Stat, Skeleton } from '../components/ui.jsx';

const VERDICT_CLASS = { PASS: 'v-pass', WARN: 'v-warn', FAIL: 'v-fail', DONE: 'v-warn' };

function fmt(v) {
  if (v == null) return '—';
  if (typeof v !== 'number') return String(v);
  if (Number.isInteger(v)) return v.toLocaleString('en-US');
  return v.toPrecision(6).replace(/\.?0+$/, '');
}

/* one extracted console table → rendered rows +, when it has ≥2 numeric
   columns, a chart (col 0 = x, cols 1..3 = series) */
function TestTable({ table }) {
  const cols = table.rows[0]?.length ?? 0;
  const series = useMemo(() => {
    if (cols < 2) return null;
    const maxSeries = Math.min(cols - 1, 3);
    return Array.from({ length: maxSeries }, (_, c) => ({
      name: (table.header[c + 1] || `col ${c + 1}`).slice(0, 24),
      points: table.rows
        .filter(r => r[0] != null && r[c + 1] != null)
        .map(r => [r[0], r[c + 1]]),
    })).filter(s => s.points.length >= 3);
  }, [table, cols]);
  return (
    <div className="test-table">
      {table.title && <p className="muted table-title">{table.title}</p>}
      {series && <LineChart series={series} xLabel={table.header[0] || ''} yLabel="" />}
      <div className="table-wrap">
        <table className="data">
          {table.header.length > 0 && (
            <thead><tr>{table.header.map((h, i) => <th key={i} scope="col">{h}</th>)}</tr></thead>
          )}
          <tbody>
            {table.rows.map((r, i) => (
              <tr key={i}>{r.map((v, j) => <td key={j} className="headline">{fmt(v)}</td>)}</tr>
            ))}
          </tbody>
        </table>
      </div>
      {table.n_rows_total > table.rows.length && (
        <p className="muted">showing {table.rows.length} of {table.n_rows_total} rows</p>
      )}
    </div>
  );
}

function TestDetail({ t }) {
  return (
    <article className="test-detail" aria-label={`Test ${t.id} details`}>
      <div className="test-head">
        <h2>
          <span className="test-num">T{String(t.id).padStart(2, '0')}</span>{' '}
          {t.short}{' '}
          <span className={VERDICT_CLASS[t.verdict] || ''}>{t.verdict}</span>
        </h2>
        <p className="muted">
          <span className="pill">{t.category}</span>{' '}
          {t.generated && <span className="pill">{t.generated}</span>}
          {t.bench && <> · bench: <code>{t.bench.slice(0, 110)}</code></>}
        </p>
      </div>

      {t.description && (
        <p className="test-desc">{t.description}</p>
      )}
      {t.method && (
        <p className="muted">Method: {t.method}</p>
      )}
      {t.result && (
        <div className="result-line">
          <span className="result-tag">Result</span>
          <span className="headline">{t.result}</span>
        </div>
      )}

      {t.series?.length > 0 && (
        <>
          <h3>Extracted series</h3>
          {t.series.map((s, i) => (
            <LineChart key={i} logX={s.x === 'N'} xLabel={s.x} yLabel={s.name}
              series={[{ name: `${s.name} (${s.points.length} pts)`, points: s.points.map(p => [p[0], p[1]]) }]} />
          ))}
        </>
      )}

      {t.calc?.length > 0 && (
        <>
          <h3>Computation-log metrics <span className="muted">({t.n_calc_total} total)</span></h3>
          <div className="stats-grid">
            {t.calc.slice(0, 12).map((c, i) => (
              <Stat key={i} label={c.name} value={fmt(c.value)}
                refVal={c.note ? c.note.slice(0, 60) : null} />
            ))}
          </div>
          {t.calc.length > 12 && (
            <details className="reveal-block">
              <summary>All {t.calc.length} captured metrics (capped from {t.n_calc_total})</summary>
              <div className="table-wrap" style={{ margin: '12px 16px' }}>
                <table className="data">
                  <thead><tr><th scope="col">metric</th><th scope="col">value</th><th scope="col">context</th></tr></thead>
                  <tbody>
                    {t.calc.map((c, i) => (
                      <tr key={i}><td>{c.name}</td><td className="headline">{fmt(c.value)}</td>
                        <td className="muted">{c.note}</td></tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </details>
          )}
        </>
      )}

      {t.tables?.map((tb, i) => (
        <div key={i}>
          <h3>Console table {i + 1}</h3>
          <TestTable table={tb} />
        </div>
      ))}

      {t.subchecks?.length > 0 && (
        <>
          <h3>Hardcore sub-checks</h3>
          <div className="table-wrap">
            <table className="data">
              <thead><tr><th scope="col">#</th><th scope="col">Check</th></tr></thead>
              <tbody>
                {t.subchecks.map((s, i) => (
                  <tr key={i}><td className="test-id">{s.tag}</td>
                    <td className="headline">{s.text}</td></tr>
                ))}
              </tbody>
            </table>
          </div>
        </>
      )}

      {t.checks?.length > 0 && (
        <>
          <h3>Verdict lines from the console capture</h3>
          <ul className="check-list">
            {t.checks.map((c, i) => <li key={i} className="headline">{c}</li>)}
          </ul>
        </>
      )}

      <div className="test-links">
        {t.reproduce && (
          <p className="muted">Reproduce: <code>{t.reproduce}</code></p>
        )}
        <p className="muted">
          Full frozen report:{' '}
          <a href={`https://github.com/wild8highlander/ab-cloud-research/blob/main/${t.report_path}`}
            target="_blank" rel="noopener">{t.report_path}</a>
        </p>
      </div>

      {t.excerpt?.length > 0 && (
        <details className="reveal-block">
          <summary>Console capture — first {t.excerpt.length} lines</summary>
          <pre className="console">{t.excerpt.join('\n')}</pre>
        </details>
      )}
    </article>
  );
}

export default function Tests() {
  const [data, setData] = useState(null);
  const [error, setError] = useState('');
  const [cat, setCat] = useState('ALL');
  const [q, setQ] = useState('');
  const [sel, setSel] = useState(null);

  useEffect(() => {
    fetch('data/test_reports.json')
      .then(r => { if (!r.ok) throw new Error(`test_reports.json: HTTP ${r.status}`); return r.json(); })
      .then(d => {
        setData(d);
        const hash = window.location.hash.match(/^#T(\d+)$/);
        if (hash) setSel(Number(hash[1]));
      })
      .catch(e => setError(e.message));
  }, []);

  const tests = data?.tests ?? [];
  const cats = data?.categories ?? [];
  const shown = useMemo(() => {
    const ql = q.trim().toLowerCase();
    return tests.filter(t =>
      (cat === 'ALL' || t.category === cat) &&
      (!ql || t.title.toLowerCase().includes(ql) ||
        String(t.id) === ql || t.short.toLowerCase().includes(ql) ||
        t.focus.toLowerCase().includes(ql)));
  }, [tests, cat, q]);

  const current = tests.find(t => t.id === sel);

  const pick = (id) => {
    setSel(id);
    try { window.history.replaceState(null, '', id == null ? '#' : `#T${id}`); } catch { /* noop */ }
  };

  if (error) {
    return <p className="error-note">Failed to load the test reports — {error}</p>;
  }
  if (!data) {
    return (
      <section aria-busy="true" aria-label="Loading test explorer">
        <Skeleton kind="stats" /><Skeleton kind="table" /><Skeleton kind="chart" />
      </section>
    );
  }

  const nPass = tests.filter(t => t.verdict === 'PASS').length;

  return (
    <section>
      <h2>Test explorer <span className="pill">{tests.length} deep-dive panels</span></h2>
      <p className="muted">
        Every one of the <b>{tests.length} verification tests</b> of run
        <code> run_20260902_134759</code>, parsed from its frozen report:
        description, hardcore sub-checks, computation-log metrics
        ({data._meta.n_calc_metrics.toLocaleString('en-US')} numbers), console
        tables, verdict lines and the raw capture itself. In the final verdict
        list: <b>{nPass} PASS</b> / {tests.length - nPass} WARN-family rows —
        all traced to the Wigner-surmise floor (see “Run report”).
      </p>

      <div className="explorer">
        <nav className="explorer-list" aria-label="Test list">
          <input className="search" type="search" placeholder="Search tests…"
            value={q} aria-label="Search tests"
            onChange={e => setQ(e.target.value)} />
          <div className="filter-row cat-chips" role="group" aria-label="Filter by category">
            <button className={cat === 'ALL' ? 'btn active' : 'btn'} onClick={() => setCat('ALL')}>
              all {tests.length}
            </button>
            {cats.map(c => (
              <button key={c.name} className={cat === c.name ? 'btn active' : 'btn'}
                onClick={() => setCat(c.name)}>{c.name}</button>
            ))}
          </div>
          <ul className="test-list">
            {shown.map(t => (
              <li key={t.id}>
                <button className={'test-item' + (sel === t.id ? ' active' : '')}
                  aria-current={sel === t.id ? 'true' : undefined}
                  onClick={() => pick(t.id)}>
                  <span className="test-item-id">T{String(t.id).padStart(2, '0')}</span>
                  <span className="test-item-body">
                    <span className="test-item-title">{t.short}</span>
                    <span className="test-item-cat">{t.category}</span>
                  </span>
                  <span className={VERDICT_CLASS[t.verdict] || ''}>{t.verdict}</span>
                </button>
              </li>
            ))}
            {shown.length === 0 && (
              <li className="empty" style={{ marginTop: 8 }}>
                <b>Nothing matches “{q}”.</b><br />Try a test number (1…37) or a keyword.
              </li>
            )}
          </ul>
        </nav>
        <div className="explorer-detail">
          {current
            ? <TestDetail t={current} />
            : (
              <div className="empty">
                <b>Select a test on the left.</b><br />
                {tests.length} panels · {data._meta.n_calc_metrics.toLocaleString('en-US')} logged metrics ·{' '}
                {data._meta.n_tables} console tables · {data._meta.n_checks} verdict lines.
              </div>
            )}
        </div>
      </div>
    </section>
  );
}
