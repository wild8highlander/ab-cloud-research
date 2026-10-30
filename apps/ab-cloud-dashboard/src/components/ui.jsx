import React, { useCallback, useEffect, useRef, useState } from 'react';

/* ---------- tiny SVG chart helpers (no chart deps) ---------- */
/* Dark-theme palette: brand cyan leads, series colors follow the
   repo banner palette (#00e5ff · #ff2ec4 · #a78bfa · #ffd60a). */

const SERIES_COLORS = ['#00E5FF', '#FF2EC4', '#A78BFA', '#FFD60A', '#4ADE80'];
const MONO = "'Geist Mono Variable', ui-monospace, 'SF Mono', Consolas, monospace";

export function LineChart({ series, width = 640, height = 320, xLabel, yLabel,
  logX = false, hLines = [] }) {
  const pad = { l: 56, r: 16, t: 16, b: 40 };
  const all = series.flatMap(s => s.points);
  if (!all.length) return null;
  const xs = all.map(p => p[0]), ys = all.map(p => p[1]);
  const xMin = logX ? Math.log10(Math.min(...xs)) : Math.min(...xs);
  const xMax = logX ? Math.log10(Math.max(...xs)) : Math.max(...xs);
  const yMin = Math.min(0, Math.min(...ys)), yMax = Math.max(...ys) * 1.05;
  const X = v => pad.l + ((logX ? Math.log10(v) : v) - xMin) / (xMax - xMin || 1) * (width - pad.l - pad.r);
  const Y = v => height - pad.b - (v - yMin) / (yMax - yMin || 1) * (height - pad.t - pad.b);
  return (
    <div className="chart-frame">
      <svg width="100%" viewBox={`0 0 ${width} ${height}`} role="img">
        <rect x={pad.l} y={pad.t} width={width - pad.l - pad.r} height={height - pad.t - pad.b}
          fill="#181818" stroke="#313131" />
        {hLines.map((h, i) => (
          <g key={i}>
            <line x1={pad.l} x2={width - pad.r} y1={Y(h.value)} y2={Y(h.value)}
              stroke={h.color} strokeDasharray="5 4" />
            <text x={width - pad.r - 4} y={Y(h.value) - 4} fontSize="11"
              fill={h.color} textAnchor="end" fontFamily={MONO}>{h.label}</text>
          </g>
        ))}
        {series.map((s, i) => (
          <polyline key={i} fill="none" stroke={SERIES_COLORS[i % SERIES_COLORS.length]} strokeWidth="1.8"
            points={s.points.map(p => `${X(p[0])},${Y(p[1])}`).join(' ')} />
        ))}
        {series.map((s, i) => (
          <text key={'lg' + i} x={pad.l + 8 + (i % 2) * 250} y={pad.t + 14 + Math.floor(i / 2) * 16}
            fontSize="12" fill={SERIES_COLORS[i % SERIES_COLORS.length]} fontFamily={MONO}>{s.name}</text>
        ))}
        <text x={width / 2} y={height - 8} fontSize="12" textAnchor="middle" fill="#9B9B9B"
          fontFamily={MONO}>{xLabel}</text>
        <text x={14} y={height / 2} fontSize="12" textAnchor="middle" fill="#9B9B9B"
          fontFamily={MONO} transform={`rotate(-90 14 ${height / 2})`}>{yLabel}</text>
        {[0, 0.25, 0.5, 0.75, 1].map((f, i) => (
          <text key={'y' + i} x={pad.l - 6} y={Y(yMin + f * (yMax - yMin)) + 4}
            fontSize="10" textAnchor="end" fill="#9B9B9B" fontFamily={MONO}>
            {(yMin + f * (yMax - yMin)).toPrecision(3)}</text>
        ))}
        {[0, 0.5, 1].map((f, i) => {
          const v = xMin + f * (xMax - xMin);
          return <text key={'x' + i} x={X(logX ? Math.pow(10, v) : v)} y={height - pad.b + 14}
            fontSize="10" textAnchor="middle" fill="#9B9B9B" fontFamily={MONO}>
            {(logX ? Math.pow(10, v) : v).toPrecision(3)}</text>;
        })}
      </svg>
    </div>
  );
}

export function BarChart({ points, width = 640, height = 300, xLabel, yLabel }) {
  const pad = { l: 56, r: 16, t: 16, b: 40 };
  const xMax = Math.max(...points.map(p => p[0])) * 1.02;
  const yMax = Math.max(...points.map(p => p[1])) * 1.1;
  const X = v => pad.l + v / xMax * (width - pad.l - pad.r);
  const Y = v => height - pad.b - v / yMax * (height - pad.t - pad.b);
  return (
    <div className="chart-frame">
      <svg width="100%" viewBox={`0 0 ${width} ${height}`} role="img">
        <rect x={pad.l} y={pad.t} width={width - pad.l - pad.r} height={height - pad.t - pad.b}
          fill="#181818" stroke="#313131" />
        {points.map((p, i) => (
          <rect key={i} x={X(p[0])} y={Y(p[1])} width={Math.max(1, (width - pad.l - pad.r) / xMax)}
            height={height - pad.b - Y(p[1])} fill="#00E5FF" opacity="0.75" />
        ))}
        <text x={width / 2} y={height - 8} fontSize="12" textAnchor="middle" fill="#9B9B9B"
          fontFamily={MONO}>{xLabel}</text>
        <text x={14} y={height / 2} fontSize="12" textAnchor="middle" fill="#9B9B9B"
          fontFamily={MONO} transform={`rotate(-90 14 ${height / 2})`}>{yLabel}</text>
        {[0, 0.5, 1].map((f, i) => {
          const v = xMax * f;
          return <text key={'x' + i} x={X(v)} y={height - pad.b + 14} fontSize="10"
            textAnchor="middle" fill="#9B9B9B" fontFamily={MONO}>{v.toFixed(2)}</text>;
        })}
      </svg>
    </div>
  );
}

/* Categorical horizontal bars — for label/value pairs (verdicts, groups,
 * ensemble distances). Complements BarChart, which needs numeric x. */
export function CatBar({ items, width = 640, rowHeight = 34, unit = '' }) {
  if (!items.length) return null;
  const max = Math.max(...items.map(i => Math.abs(i.value))) || 1;
  const labelW = 120;
  const barW = width - labelW - 96;
  return (
    <div className="chart-frame">
      <svg width="100%" viewBox={`0 0 ${width} ${items.length * rowHeight + 16}`} role="img">
        {items.map((it, i) => {
          const y = 8 + i * rowHeight;
          const w = Math.max(2, (Math.abs(it.value) / max) * barW);
          const color = it.color || '#00E5FF';
          return (
            <g key={i}>
              <text x={labelW - 10} y={y + 17} fontSize="12" textAnchor="end"
                fill="#9B9B9B" fontFamily={MONO}>{it.label}</text>
              <rect x={labelW} y={y + 6} width={barW} height={rowHeight - 12}
                fill="#181818" stroke="#313131" />
              <rect x={labelW} y={y + 6} width={w} height={rowHeight - 12} fill={color} opacity="0.8" />
              <text x={labelW + barW + 8} y={y + 17} fontSize="12"
                fill="#FFFFFF" fontFamily={MONO}>
                {typeof it.value === 'number' ? it.value.toPrecision(6).replace(/\.?0+$/, '') : it.value}{unit}
              </text>
            </g>
          );
        })}
      </svg>
    </div>
  );
}

export function Stat({ label, value, refVal, ok }) {
  return (
    <div className="stat">
      <div className="stat-label">{label}</div>
      <div className="stat-value">{value}</div>
      {refVal != null && (
        <div className={ok === undefined ? 'stat-ref' : ok ? 'stat-ref ok' : 'stat-ref bad'}>
          reference: {refVal}{ok === undefined ? '' : ok ? '  ✓' : '  ✗'}
        </div>
      )}
    </div>
  );
}

/* Skeleton loaders (B9): shaped like the real layout, not spinners. */
export function Skeleton({ kind }) {
  if (kind === 'stats') {
    return (
      <div className="stats-grid" aria-hidden="true">
        {[0, 1, 2, 3].map(i => <div key={i} className="skeleton sk-stat" />)}
      </div>
    );
  }
  if (kind === 'table') {
    return (
      <div aria-hidden="true">
        {[0, 1, 2, 3, 4, 5, 6, 7].map(i => (
          <div key={i} className="skeleton sk-row" style={{ opacity: 1 - i * 0.09 }} />
        ))}
      </div>
    );
  }
  return <div className="skeleton sk-chart" aria-hidden="true" />;
}

export function useWorker() {
  const workerRef = useRef(null);
  const [busy, setBusy] = useState(false);
  useEffect(() => {
    // Module-worker construction can THROW in environments without support
    // (older Firefox, some Android WebViews, strict CSP without worker-src).
    // An uncaught throw inside useEffect would unmount the whole React root
    // (white screen). Instead: remember the failure and let run() resolve
    // with an error payload the pages render as a normal error note.
    try {
      workerRef.current = new Worker(
        new URL('../worker/stats.worker.js', import.meta.url), { type: 'module' });
    } catch (e) {
      workerRef.current = null;
      workerRef.initError = String(e?.message || e);
    }
    return () => { workerRef.current?.terminate(); workerRef.current = null; };
  }, []);
  // stable identity: keeps page-level effects from re-firing on every render
  const run = useCallback((type, payload) => new Promise((resolve) => {
    const w = workerRef.current;
    if (!w) {
      resolve({ type, ok: false, error: workerRef.initError || 'worker unavailable in this browser' });
      return;
    }
    setBusy(true);
    // safety net: a lost/unknown message must never leave the UI spinning forever
    const timer = setTimeout(() => finish({ type, ok: false, error: 'worker timed out' }), 120000);
    const finish = (data) => {
      clearTimeout(timer);
      w.removeEventListener('message', handler);
      w.removeEventListener('error', onErr);
      setBusy(false);
      resolve(data);
    };
    const handler = (e) => {
      if (e.data && e.data.type === type) finish(e.data);
    };
    const onErr = (e) => {
      e.preventDefault();
      finish({ type, ok: false, error: String(e.message || 'worker error') });
    };
    w.addEventListener('message', handler);
    w.addEventListener('error', onErr);
    w.postMessage({ type, payload });
  }), []);
  return { run, busy };
}
