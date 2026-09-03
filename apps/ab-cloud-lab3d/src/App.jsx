import React, { useEffect, useRef, useState } from 'react';
import { makeScene, buildHofstadter, buildDiracCone, buildZetaStrip } from './modules/scenes.js';
import { zetaSelfCheck } from './modules/zeta.js';

export default function App() {
  const hostRef = useRef(null);
  const sceneRef = useRef(null);
  const [tab, setTab] = useState('hofstadter');
  const [alpha, setAlpha] = useState(0.5);
  const [nv, setNv] = useState(4);
  const [info, setInfo] = useState('');
  const [check, setCheck] = useState(null);

  useEffect(() => {
    setCheck(zetaSelfCheck());
  }, []);

  useEffect(() => {
    if (!hostRef.current) return;
    sceneRef.current = makeScene(hostRef.current);
    return () => sceneRef.current.dispose();
  }, []);

  useEffect(() => {
    const s = sceneRef.current;
    if (!s) return;
    if (tab === 'hofstadter') {
      const { vortices } = buildHofstadter(s, 18, alpha, nv);
      setInfo(`Lattice 18×18, α = ${alpha}, ${vortices.length} vortices (red cones, q=+1). Site bars are colored by the Landau phase 2πα·j — the GUE mechanism of the suite is the vortex phase field (:monumental gauge).`);
    } else if (tab === 'dirac') {
      buildDiracCone(s, 6, 1.9);
      setInfo('Dirac cone E(k) = v_F·|k| at α = 1/2 (vortex q=+1): the chiral tower of suite tests 19/30, v_F(2π) = 1.9.');
    } else {
      const { eMax } = buildZetaStrip(s, 40, 61, 200);
      setInfo(`|ζ(σ+it)| for σ ∈ [0, 1.2], t ∈ [0, 40] — the critical strip (3D-34). Yellow line: Re s = 1/2; red spheres: embedded zeros γ₁..γ₁₅. JS ζ-evaluator self-check: |ζ(2)−π²/6| = ${check ? check.z2err.toExponential(2) : '…'}.`);
    }
  }, [tab, alpha, nv, check]);

  return (
    <div className="app">
      <header>
        <h1>AB-Cloud — 3D Laboratory</h1>
        <p className="muted">
          Hofstadter lattice with vortices · Dirac cone · ζ critical strip —
          WebGL/Three.js, real-time. Suite 3D-1…3D-34 (Julia) visualized.
        </p>
        <nav>
          <button className={tab === 'hofstadter' ? 'btn active' : 'btn'}
            onClick={() => setTab('hofstadter')}>Hofstadter lattice</button>
          <button className={tab === 'dirac' ? 'btn active' : 'btn'}
            onClick={() => setTab('dirac')}>Dirac cone</button>
          <button className={tab === 'zeta' ? 'btn active' : 'btn'}
            onClick={() => setTab('zeta')}>ζ critical strip</button>
        </nav>
        {tab === 'hofstadter' && (
          <div className="controls">
            <label>α = {alpha.toFixed(2)}
              <input type="range" min="0" max="1" step="0.05" value={alpha}
                onChange={e => setAlpha(+e.target.value)} />
            </label>
            <label>vortices = {nv}
              <input type="range" min="0" max="12" value={nv}
                onChange={e => setNv(+e.target.value)} />
            </label>
          </div>
        )}
      </header>
      <div ref={hostRef} className="canvas-host" />
      <p className="info">{info}</p>
      <footer className="muted">
        Source: <code>apps/ab-cloud-lab3d/</code> (React 18 + Vite + Three.js).
        ζ evaluator: self-anchored Euler–Maclaurin (port of 3D-34);
        check anchors ζ(2)=π²/6, ζ(4)=π⁴/90, ζ(1/2)≈−1.4603545.
      </footer>
    </div>
  );
}
