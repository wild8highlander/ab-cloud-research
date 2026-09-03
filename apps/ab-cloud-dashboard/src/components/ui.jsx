import React, { useEffect, useMemo, useRef, useState } from 'react';

/* ---------- tiny SVG chart helpers (no chart deps) ---------- */

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
  const colors = ['#2563eb', '#dc2626', '#059669', '#d97706', '#7c3aed'];
  return (
    <svg width="100%" viewBox={`0 0 ${width} ${height}`} role="img">
      <rect x={pad.l} y={pad.t} width={width - pad.l - pad.r} height={height - pad.t - pad.b}
        fill="#fafbff" stroke="#d7dce8" />
      {hLines.map((h, i) => (
        <g key={i}>
          <line x1={pad.l} x2={width - pad.r} y1={Y(h.value)} y2={Y(h.value)}
            stroke={h.color} strokeDasharray="5 4" />
          <text x={width - pad.r - 4} y={Y(h.value) - 4} fontSize="11"
            fill={h.color} textAnchor="end">{h.label}</text>
        </g>
      ))}
      {series.map((s, i) => (
        <polyline key={i} fill="none" stroke={colors[i % colors.length]} strokeWidth="1.8"
          points={s.points.map(p => `${X(p[0])},${Y(p[1])}`).join(' ')} />
      ))}
      {series.map((s, i) => (
        <text key={'lg' + i} x={pad.l + 8 + i * 150} y={pad.t + 14} fontSize="12"
          fill={colors[i % colors.length]}>{s.name}</text>
      ))}
      <text x={width / 2} y={height - 8} fontSize="12" textAnchor="middle" fill="#555">
        {xLabel}</text>
      <text x={14} y={height / 2} fontSize="12" textAnchor="middle" fill="#555"
        transform={`rotate(-90 14 ${height / 2})`}>{yLabel}</text>
      {[0, 0.25, 0.5, 0.75, 1].map((f, i) => (
        <text key={'y' + i} x={pad.l - 6} y={Y(yMin + f * (yMax - yMin)) + 4}
          fontSize="10" textAnchor="end" fill="#777">
          {(yMin + f * (yMax - yMin)).toPrecision(3)}</text>
      ))}
      {[0, 0.5, 1].map((f, i) => {
        const v = xMin + f * (xMax - xMin);
        return <text key={'x' + i} x={X(logX ? Math.pow(10, v) : v)} y={height - pad.b + 14}
          fontSize="10" textAnchor="middle" fill="#777">
          {(logX ? Math.pow(10, v) : v).toPrecision(3)}</text>;
      })}
    </svg>
  );
}

export function BarChart({ points, width = 640, height = 300, xLabel, yLabel }) {
  const pad = { l: 56, r: 16, t: 16, b: 40 };
  const xMax = Math.max(...points.map(p => p[0])) * 1.02;
  const yMax = Math.max(...points.map(p => p[1])) * 1.1;
  const X = v => pad.l + v / xMax * (width - pad.l - pad.r);
  const Y = v => height - pad.b - v / yMax * (height - pad.t - pad.b);
  return (
    <svg width="100%" viewBox={`0 0 ${width} ${height}`} role="img">
      <rect x={pad.l} y={pad.t} width={width - pad.l - pad.r} height={height - pad.t - pad.b}
        fill="#fafbff" stroke="#d7dce8" />
      {points.map((p, i) => (
        <rect key={i} x={X(p[0])} y={Y(p[1])} width={Math.max(1, (width - pad.l - pad.r) / xMax)}
          height={height - pad.b - Y(p[1])} fill="#2563eb" opacity="0.85" />
      ))}
      <text x={width / 2} y={height - 8} fontSize="12" textAnchor="middle" fill="#555">{xLabel}</text>
      <text x={14} y={height / 2} fontSize="12" textAnchor="middle" fill="#555"
        transform={`rotate(-90 14 ${height / 2})`}>{yLabel}</text>
    </svg>
  );
}

export function Stat({ label, value, ref: refVal, ok }) {
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

export function useWorker() {
  const workerRef = useRef(null);
  const [busy, setBusy] = useState(false);
  useEffect(() => {
    workerRef.current = new Worker(
      new URL('../worker/stats.worker.js', import.meta.url), { type: 'module' });
    return () => workerRef.current.terminate();
  }, []);
  const run = (type, payload) => new Promise((resolve) => {
    setBusy(true);
    const w = workerRef.current;
    const handler = (e) => {
      if (e.data.type !== type) return;
      w.removeEventListener('message', handler);
      setBusy(false);
      resolve(e.data);
    };
    w.addEventListener('message', handler);
    w.postMessage({ type, payload });
  });
  return { run, busy };
}
