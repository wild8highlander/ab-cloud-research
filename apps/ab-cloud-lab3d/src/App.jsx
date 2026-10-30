import React, { useEffect, useRef, useState } from 'react';
import { makeScene, buildHofstadter, buildDiracCone, buildZetaStrip } from './modules/scenes.js';
import { zetaSelfCheck } from './modules/zeta.js';

const TABS = [
  ['hofstadter', 'Hofstadter lattice'],
  ['dirac', 'Dirac cone'],
  ['zeta', 'ζ critical strip'],
];

function webglSupported() {
  try {
    const c = document.createElement('canvas');
    return !!(window.WebGLRenderingContext &&
      (c.getContext('webgl2') || c.getContext('webgl')));
  } catch {
    return false;
  }
}

export default function App() {
  const hostRef = useRef(null);
  const sceneRef = useRef(null);
  const [tab, setTab] = useState('hofstadter');
  const [alpha, setAlpha] = useState(0.5);
  const [nv, setNv] = useState(4);
  const [info, setInfo] = useState('');
  const [check, setCheck] = useState(null);
  const [glError, setGlError] = useState('');

  useEffect(() => {
    setCheck(zetaSelfCheck());
  }, []);

  useEffect(() => {
    if (!hostRef.current) return;
    if (!webglSupported()) {
      setGlError('WebGL is not available in this browser or environment. ' +
        'The 3D laboratory needs hardware (or software) WebGL — try Chrome, ' +
        'Firefox or Safari with hardware acceleration enabled.');
      return;
    }
    try {
      sceneRef.current = makeScene(hostRef.current);
    } catch (e) {
      setGlError(`Failed to initialize the WebGL renderer — ${e.message}`);
      return;
    }
    return () => {
      if (sceneRef.current) sceneRef.current.dispose();
      sceneRef.current = null;
    };
  }, []);

  useEffect(() => {
    const s = sceneRef.current;
    if (!s || glError) return;
    // A throwing scene builder must degrade to an error note, never unmount
    // the React root (which would blank the whole page).
    try {
      if (tab === 'hofstadter') {
        const { vortices } = buildHofstadter(s, 18, alpha, nv);
        setInfo(`Lattice 18×18, α = ${alpha}, ${vortices.length} vortices (red cones, q=+1). Site bars are colored by the Landau phase 2πα·j — the GUE mechanism of the suite is the vortex phase field (:monumental gauge).`);
      } else if (tab === 'dirac') {
        buildDiracCone(s, 6, 1.9);
        setInfo('Dirac cone E(k) = v_F·|k| at α = 1/2 (vortex q=+1): the chiral tower of suite tests 19/30, v_F(2π) = 1.9.');
      } else {
        buildZetaStrip(s, 40, 61, 200);
        setInfo(`|ζ(σ+it)| for σ ∈ [0, 1.2], t ∈ [0, 40] — the critical strip (3D-34). Yellow line: Re s = 1/2; red spheres: embedded zeros γ₁..γ₁₅. JS ζ-evaluator self-check: |ζ(2)−π²/6| = ${check ? check.z2err.toExponential(2) : '…'}.`);
      }
    } catch (e) {
      setGlError(`Failed to build the "${tab}" scene — ${e?.message || e}. ` +
        'Reload the page; if it persists, try another browser.');
    }
  }, [tab, alpha, nv, check, glError]);

  return (
    <div className="app">
      <a className="skip-link" href="#main">Skip to content</a>
      <header className="hero">
        <p className="kicker">AB-Cloud · 3D laboratory</p>
        <h1>
          <span className="grad">The lattice, the cone and the strip:<br />experiments 3D-1…3D-34, live</span>
        </h1>
        <p className="sub">
          Hofstadter lattice with vortices · Dirac cone · ζ critical strip —
          <b> WebGL and Three.js, computed in real time</b>. Every scene is
          procedural: no prebaked pictures, no server.
        </p>
      </header>
      <div className="tabbar-wrap">
        <nav className="tabbar" aria-label="Scenes">
          {TABS.map(([k, label]) => (
            <button key={k} className={tab === k ? 'btn active' : 'btn'}
              aria-current={tab === k ? 'true' : undefined}
              onClick={() => setTab(k)}>{label}</button>
          ))}
        </nav>
      </div>
      {tab === 'hofstadter' && (
        <div className="controls">
          <label>α = <span className="val">{alpha.toFixed(2)}</span>
            <input type="range" min="0" max="1" step="0.05" value={alpha}
              onChange={e => setAlpha(+e.target.value)} />
          </label>
          <label>vortices = <span className="val">{nv}</span>
            <input type="range" min="0" max="12" value={nv}
              onChange={e => setNv(+e.target.value)} />
          </label>
        </div>
      )}
      <main id="main">
        <div ref={hostRef} className="canvas-host" />
        {glError && <p className="gl-error" role="alert">{glError}</p>}
        {!glError && <p className="info">{info}</p>}
      </main>
      <footer>
        <div className="links">
          <a href="https://github.com/wild8highlander/ab-cloud-research" target="_blank" rel="noopener">GitHub repository</a>
          <a href="https://github.com/wild8highlander/ab-cloud-research/blob/main/LICENSE" target="_blank" rel="noopener">License</a>
          <a href="https://doi.org/10.5281/zenodo.21825394" target="_blank" rel="noopener">Zenodo DOI</a>
          <a href="/">Portal home</a>
        </div>
        <div>
          Source: <code>apps/ab-cloud-lab3d/</code> (React 19 + Vite + Three.js).
          ζ evaluator: self-anchored Euler–Maclaurin (port of 3D-34);
          check anchors ζ(2)=π²/6, ζ(4)=π⁴/90, ζ(1/2)≈−1.4603545.
        </div>
      </footer>
    </div>
  );
}
