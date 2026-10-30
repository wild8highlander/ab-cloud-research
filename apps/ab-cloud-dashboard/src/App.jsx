import React, { useEffect, useState } from 'react';
import RunReport from './pages/RunReport.jsx';
import ZerosStats from './pages/ZerosStats.jsx';
import Spinor64 from './pages/Spinor64.jsx';

const TABS = [
  ['run', 'Run report (37 tests)'],
  ['zeros', 'Live ζ statistics'],
  ['spinor', 'Test 38 · 64 spinors'],
];

export default function App() {
  const [summary, setSummary] = useState(null);
  const [zeros, setZeros] = useState(null);
  const [tab, setTab] = useState('run');
  const [loadErr, setLoadErr] = useState('');

  useEffect(() => {
    fetch('data/run_summary.json')
      .then(r => { if (!r.ok) throw new Error(`run_summary.json: HTTP ${r.status}`); return r.json(); })
      .then(setSummary)
      .catch(e => setLoadErr(p => p + `run summary: ${e.message}. `));
    fetch('data/zeta_zeros_50000_embedded.txt')
      .then(r => { if (!r.ok) throw new Error(`zeros dataset: HTTP ${r.status}`); return r.text(); })
      .then(t => {
        setZeros(t.split('\n').filter(l => l && !l.startsWith('#')).map(Number));
      })
      .catch(e => setLoadErr(p => p + `${e.message}. `));
  }, []);

  return (
    <div className="app">
      <a className="skip-link" href="#main">Skip to content</a>
      <header className="hero">
        <p className="kicker">AB-Cloud · Hilbert–Pólya suite</p>
        <h1>
          <span className="grad">Verification dashboard:<br />the evidence, recomputed in front of you</span>
        </h1>
        <p className="sub">
          <b>37 tests</b> across two passes · <b>50,000</b> Odlyzko zeros ·
          statistics live in a Web Worker · Isaev Iskhak Khamzatovich
          (ORCID 0009-0003-7299-0701)
        </p>
      </header>
      <div className="tabbar-wrap">
        <nav className="tabbar" aria-label="Dashboard sections">
          {TABS.map(([k, label]) => (
            <button key={k} className={tab === k ? 'btn active' : 'btn'}
              aria-current={tab === k ? 'true' : undefined}
              onClick={() => setTab(k)}>{label}</button>
          ))}
        </nav>
      </div>
      <main id="main">
        {loadErr && (
          <p className="error-note" role="alert">
            Failed to load datasets: {loadErr}
            <br />Check that <code>data/</code> is deployed next to this page and reload.
          </p>
        )}
        {tab === 'run' && <RunReport summary={summary} error={loadErr} />}
        {tab === 'zeros' && <ZerosStats zeros={zeros} error={loadErr} />}
        {tab === 'spinor' && <Spinor64 />}
      </main>
      <footer>
        <div className="links">
          <a href="https://github.com/wild8highlander/ab-cloud-research" target="_blank" rel="noopener">GitHub repository</a>
          <a href="https://github.com/wild8highlander/ab-cloud-research/blob/main/LICENSE" target="_blank" rel="noopener">License</a>
          <a href="https://doi.org/10.5281/zenodo.21825394" target="_blank" rel="noopener">Zenodo DOI</a>
          <a href="/" >Portal home</a>
        </div>
        <div>
          Source: <code>apps/ab-cloud-dashboard/</code> (React + Vite).
          Data: embedded Odlyzko 50k zeros and the frozen spinor classes of
          <code>verification/spinor64/</code>. DOI 10.5281/zenodo.21825394.
        </div>
      </footer>
    </div>
  );
}
