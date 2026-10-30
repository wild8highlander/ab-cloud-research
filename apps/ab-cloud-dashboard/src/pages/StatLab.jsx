import React, { useState } from 'react';
import { LineChart, BarChart, CatBar, Stat, Skeleton, useWorker } from '../components/ui.jsx';

/* The live test battery — every card re-computes a suite-family statistic
 * from the embedded 50,000-zero dataset inside the Web Worker. */
const LAB_TESTS = [
  {
    id: 'paircorr', title: 'Pair correlation R₂(s)',
    desc: 'All pairwise separations of the unfolded zeros against the GUE sine-kernel prediction 1 − (sin πs / πs)². Level repulsion = the dip at s → 0. Suite family: Tests 4–5.',
    unit: 'mirror of Tests 4–5',
  },
  {
    id: 'spacing', title: 'Spacing histogram vs Wigner–GUE surmise',
    desc: 'Unfolded nearest-neighbor spacings (Riemann–von Mangoldt unfolding) vs the GUE surmise (32/π²)s²e^{−4s²/π}, with one-sample KS.',
    unit: 'mirror of Test 6',
  },
  {
    id: 'qq', title: 'QQ plot vs the GUE ratio law',
    desc: 'Quantile–quantile plot of the observed spacing ratios against the exact GUE ratio law 27/8·(r+r²)²/(1+r+r²)⁵. A straight diagonal = perfect fit.',
    unit: 'mirror of Tests 4/12',
  },
  {
    id: 'chi2', title: 'χ² goodness-of-fit (20 bins)',
    desc: 'Pearson χ² of the spacing histogram against the GUE surmise, p-value from the regularized incomplete gamma. Suite family: Test 6.',
    unit: 'mirror of Test 6',
  },
  {
    id: 'autocorr', title: 'Autocorrelation of ratios (lags 1–12)',
    desc: 'Serial autocorrelation of the spacing-ratio sequence. Independent eigenvalues ⇒ every lag inside the ±1.96/√n band.',
    unit: 'independence check',
  },
  {
    id: 'runs', title: 'Wald–Wolfowitz runs test',
    desc: 'Runs above/below the median ratio vs the expected count under independence. Suite family: Test 8 (residual runs).',
    unit: 'mirror of Test 8',
  },
  {
    id: 'evenodd', title: 'Even/odd index split (two-sample KS)',
    desc: '⟨r⟩ over even-indexed vs odd-indexed spacings + two-sample KS: the statistic must not depend on the position in the sequence.',
    unit: 'stability check',
  },
  {
    id: 'halves', title: 'Height split: first vs second half',
    desc: '⟨r⟩ on the lower vs upper 25,000 zeros + two-sample KS — stationarity of the statistics across height. Suite family: Test 5 (high-T) and Test 12.',
    unit: 'mirror of Tests 5/12',
  },
  {
    id: 'entropy', title: 'Shannon entropy of the ratio law',
    desc: 'H = −Σp·ln p of the 40-bin ratio histogram vs the same-binned GUE reference — one number for “how GUE is the whole distribution”.',
    unit: 'information view',
  },
];

export default function StatLab({ zeros }) {
  const { run, busy } = useWorker();
  const [results, setResults] = useState({});
  const [errors, setErrors] = useState({});

  const doRun = async (id) => {
    const res = await run('lab', { zeros, test: id });
    if (res.ok) {
      setResults(p => ({ ...p, [id]: res.result }));
    } else {
      setErrors(p => ({ ...p, [id]: res.error || 'computation failed' }));
    }
  };
  const runAll = async () => {
    for (const t of LAB_TESTS) await doRun(t.id);
  };

  if (!zeros) {
    return (
      <section>
        <h2>Stat lab <span className="pill">9 live tests</span></h2>
        <p className="muted">Loading the 50,000-zero dataset…</p>
        <Skeleton kind="stats" /><Skeleton kind="chart" />
      </section>
    );
  }

  const doneCount = Object.keys(results).length;

  return (
    <section>
      <h2>Stat lab <span className="pill">{LAB_TESTS.length} live tests</span></h2>
      <p className="muted">
        The statistics layer of the Julia suite, re-implemented in the browser
        worker: every test below recomputes its diagnostic from the embedded{' '}
        <b>{zeros.length.toLocaleString('en-US')} Odlyzko zeros</b> — no server,
        no pre-baked numbers. “mirror of Test N” links each card to the frozen
        suite result it reproduces.
      </p>
      <div className="filter-row">
        <button className="btn active" onClick={runAll} disabled={busy} aria-busy={busy}>
          {busy ? 'computing…' : `▶ Run all ${LAB_TESTS.length}`}
        </button>
        {doneCount > 0 && <span className="muted">{doneCount}/{LAB_TESTS.length} done</span>}
      </div>

      {LAB_TESTS.map(t => {
        const r = results[t.id];
        const err = errors[t.id];
        return (
          <article key={t.id} className="panel lab-card">
            <div className="lab-head">
              <div>
                <h3 style={{ margin: '0 0 4px' }}>{t.title} <span className="pill">{t.unit}</span></h3>
                <p className="muted" style={{ margin: 0, maxWidth: 620 }}>{t.desc}</p>
              </div>
              <button className="btn" onClick={() => doRun(t.id)} disabled={busy && !r}>
                {r ? '↻ re-run' : '▶ run'}
              </button>
            </div>
            {err && <p className="error-note">{err}</p>}
            {!r && !err && <div className="skeleton sk-chart" aria-hidden="true" />}
            {r && <LabResult id={t.id} r={r} />}
          </article>
        );
      })}
    </section>
  );
}

function LabResult({ id, r }) {
  if (id === 'paircorr') {
    return (
      <>
        <LineChart width={680} height={340} xLabel="s (unfolded)" yLabel="R₂(s)"
          hLines={[{ value: 1, color: '#4A4A4A', label: 'R₂=1' }]}
          series={[
            { name: 'data R₂(s)', points: r.bins.map(b => [b.s, b.r]) },
            { name: 'GUE 1−sinc²', points: r.gue.map(b => [b.s, b.r]) },
          ]} />
        <div className="stats-grid">
          <Stat label="zeros" value={r.n.toLocaleString('en-US')} />
          <Stat label="pairs inside s≤3.2" value={r.pairs.toLocaleString('en-US')} />
          <Stat label="R₂(s→0) repulsion dip"
            value={(r.bins[0].r < 0.15 ? 'strong ✓' : r.bins[0].r.toPrecision(3))}
            refVal="GUE: → 0 quadratically" ok={r.bins[0].r < 0.15} />
        </div>
      </>
    );
  }
  if (id === 'spacing') {
    return (
      <>
        <LineChart width={680} height={320} xLabel="s (unfolded spacing)" yLabel="p(s)"
          series={[
            { name: 'data histogram', points: r.bins.map(b => [b.s, b.p]) },
            { name: 'GUE surmise', points: r.bins.map(b => [b.s, b.gue]) },
          ]} />
        <div className="stats-grid">
          <Stat label="KS statistic D" value={r.D.toPrecision(4)} />
          <Stat label="KS p-value" value={r.p === 0 ? '< 1e-16 (surmise floor)' : r.p.toPrecision(3)}
            refVal="surmise ≠ exact law — the suite’s known WARN" />
          <Stat label="⟨s⟩ (unfolded)" value={r.mean.toPrecision(6)} refVal="1 (by construction)" ok={Math.abs(r.mean - 1) < 0.02} />
          <Stat label="σ(s)" value={r.sd.toPrecision(4)} refVal="GUE surmise: 0.4227" />
        </div>
      </>
    );
  }
  if (id === 'qq') {
    return (
      <>
        <LineChart width={560} height={480} xLabel="GUE ratio-law quantile" yLabel="data quantile"
          hLines={[{ value: 0.5, color: '#4A4A4A', label: 'diagonal' }]}
          series={[{ name: 'QQ (39 quantiles)', points: r.pts }]} />
        <div className="stats-grid">
          <Stat label="KS vs exact GUE law" value={r.D.toPrecision(4)} />
          <Stat label="p-value" value={r.p.toPrecision(3)} />
          <Stat label="quantiles" value={r.pts.length} />
        </div>
      </>
    );
  }
  if (id === 'chi2') {
    const used = r.rows.filter(x => x.used);
    return (
      <>
        <CatBar width={700} items={used.map(x => ({
          label: `${x.range[0].toFixed(1)}–${x.range[1].toFixed(1)}`,
          value: ((x.O - x.E) / x.E).toFixed(3),
        }))} unit="  (O−E)/E" />
        <div className="stats-grid">
          <Stat label="χ²" value={r.chi.toPrecision(5)} />
          <Stat label="dof" value={r.dof} />
          <Stat label="p-value" value={r.p.toPrecision(4)}
            refVal="vs surmise — see Test 6 discussion" />
          <Stat label="bins used / total" value={`${used.length}/${r.rows.length}`} />
        </div>
      </>
    );
  }
  if (id === 'autocorr') {
    return (
      <>
        <BarChart width={680} height={300} xLabel="lag" yLabel="autocorrelation"
          points={r.out.map(o => [o.lag, o.ac])} />
        <div className="stats-grid">
          <Stat label="95% band ±" value={r.ci.toPrecision(3)} refVal="all lags must sit inside" />
          <Stat label="max |ac|" value={Math.max(...r.out.map(o => Math.abs(o.ac))).toPrecision(3)}
            ok={Math.max(...r.out.map(o => Math.abs(o.ac))) < r.ci * 1.5} />
          <Stat label="n ratios" value={r.n.toLocaleString('en-US')} />
        </div>
      </>
    );
  }
  if (id === 'runs') {
    return (
      <div className="stats-grid">
        <Stat label="runs observed" value={r.runs} />
        <Stat label="runs expected (indep.)" value={r.mu.toPrecision(6)} />
        <Stat label="z-score" value={r.z.toPrecision(4)} />
        <Stat label="two-sided p" value={r.p.toPrecision(3)} ok={r.p > 0.01} />
        <Stat label="above / below median" value={`${r.n1} / ${r.n2}`} />
      </div>
    );
  }
  if (id === 'evenodd') {
    return (
      <div className="stats-grid">
        <Stat label="⟨r⟩ even indices" value={r.rEven.toPrecision(6)} refVal={`GUE ${r.refs.R_GUE}`} />
        <Stat label="⟨r⟩ odd indices" value={r.rOdd.toPrecision(6)} />
        <Stat label="|Δ⟨r⟩|" value={Math.abs(r.rEven - r.rOdd).toPrecision(3)} ok={Math.abs(r.rEven - r.rOdd) < 0.005} />
        <Stat label="two-sample KS D" value={r.D.toPrecision(4)} />
        <Stat label="KS p" value={r.p.toPrecision(3)} />
      </div>
    );
  }
  if (id === 'halves') {
    return (
      <div className="stats-grid">
        <Stat label="⟨r⟩ lower half" value={r.r1.toPrecision(6)} refVal="first 25k zeros" />
        <Stat label="⟨r⟩ upper half" value={r.r2.toPrecision(6)} refVal="last 25k zeros" />
        <Stat label="|Δ⟨r⟩|" value={Math.abs(r.r1 - r.r2).toPrecision(3)} />
        <Stat label="two-sample KS D" value={r.D.toPrecision(4)} />
        <Stat label="KS p" value={r.p.toPrecision(3)} />
      </div>
    );
  }
  if (id === 'entropy') {
    return (
      <>
        <BarChart width={680} height={280} xLabel="ratio bin k/40" yLabel="count"
          points={r.counts.map(c => [c.k, c.c])} />
        <div className="stats-grid">
          <Stat label="H (data)" value={r.H.toPrecision(6)} />
          <Stat label="H (GUE reference)" value={r.Hg.toPrecision(6)} />
          <Stat label="ΔH" value={r.dH.toPrecision(4)} refVal="0 = indistinguishable" ok={Math.abs(r.dH) < 0.05} />
          <Stat label="n ratios" value={r.n.toLocaleString('en-US')} />
        </div>
      </>
    );
  }
  return null;
}
