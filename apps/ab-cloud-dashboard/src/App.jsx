import React, { useEffect, useState } from 'react';
import RunReport from './pages/RunReport.jsx';
import ZerosStats from './pages/ZerosStats.jsx';
import Spinor64 from './pages/Spinor64.jsx';

export default function App() {
  const [summary, setSummary] = useState(null);
  const [zeros, setZeros] = useState(null);
  const [tab, setTab] = useState('run');

  useEffect(() => {
    fetch('data/run_summary.json').then(r => r.json()).then(setSummary);
    fetch('data/zeta_zeros_50000_embedded.txt').then(r => r.text()).then(t => {
      setZeros(t.split('\n').filter(l => l && !l.startsWith('#')).map(Number));
    });
  }, []);

  const tabs = [
    ['run', 'Run report (37 tests)'],
    ['zeros', 'Real-time ζ statistics'],
    ['spinor', 'Test 38 — 64 spinors'],
  ];

  return (
    <div className="app">
      <header>
        <h1>AB-Cloud — Verification Dashboard</h1>
        <p className="muted">
          Hilbert–Pólya suite · 37 tests · real-time in-browser statistics ·
          Isaev Iskhak Khamzatovich (ORCID 0009-0003-7299-0701)
        </p>
        <nav>
          {tabs.map(([k, label]) => (
            <button key={k} className={tab === k ? 'btn active' : 'btn'}
              onClick={() => setTab(k)}>{label}</button>
          ))}
        </nav>
      </header>
      <main>
        {tab === 'run' && <RunReport summary={summary} />}
        {tab === 'zeros' && <ZerosStats zeros={zeros} />}
        {tab === 'spinor' && <Spinor64 />}
      </main>
      <footer className="muted">
        Source: <code>apps/ab-cloud-dashboard/</code> (React + Vite).
        Data: embedded Odlyzko 50k zeros and the frozen spinor classes of
        `verification/spinor64/`. DOI 10.5281/zenodo.21825394.
      </footer>
    </div>
  );
}
