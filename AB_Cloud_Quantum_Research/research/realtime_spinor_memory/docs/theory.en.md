# Theory: the machine with no long-term memory

## 1. The model

**Definition (spinor phase machine).** A machine M(θ) is a triple
(φ, step, read):

- the state is a single register φ ∈ [0, 2π) (the phase of a unit
  spinor);
- one real-time step: φ ← (φ + θ) mod 2π, with θ the fixed model angle
  (the spinor phase);
- the readout is the maximum-likelihood projection onto the lattice
  G_θ = {0, θ, 2θ, …}: index s = round(φ/θ) mod N.

The constants θ and N are the model specification known before the run;
they are not state. The only mutable register is φ. The state footprint
is 1 at all times; there are no history containers — storage = 0 by
construction.

**Model phases.** θ = π/2 (S1), θ = π/3 (S2), θ = π/7 (S3). For any
phase π/k the lattice closes after N = 2k steps (theorem TS1): the cycle
consists of 2k roots of unity — S1 is the "quadrant" machine with 4
states, S2 the "sextant" machine with 6, S3 the 14-phase machine.

## 2. Why the machine has no long-term memory — and why that is a feature

Three independent arguments, each with its own certificate:

**(a) Information (TS2/ES2).** The state carries exactly log₂N bits
regardless of runtime. After a reset the post-state is degenerate:
I(S_pre; S_post) = 0, and no observer reconstructs the past above the
chance level 1/N. About time, the machine remembers only t mod N — the
share of consistent moments over a horizon T is 1/N. This is the strict
meaning of "no long-term memory": not "bad memory" but "no history
carrier at all".

**(b) Computational (ES4).** Despite the single register the machine
computes for real: the modular counter out_t ≡ (out_0 + t) (mod N) runs
300,000 steps with accuracy 1.0 in all three models. The phase is itself
the counter — the machine has no external clock register. The parent
program's "reads, does not carry" (V23/E17) is the same claim: the
result lives in the step stream, not in storage.

**(c) Timing (TS3/ES3).** A step costs O(1) at all t — the cost profile
is flat (slope −1.5e−12 ms/step, 0 misses of the 1 ms deadline over
200,000 steps). The contrast LogMachine with an eternal log and full
replay carries Ω(t): ×129 mean-step cost growth by t = 2¹⁷, R² = 0.999.
For any deadline Δt there is t* beyond which the log misses deadlines.
Conclusion: hard real time and long-term memory are architecturally
incompatible — volatility is the condition of determinism.

## 3. Capacity vs robustness

Capacity grows as log₂N = log₂(2k), while the gap between neighboring
states shrinks as 2π/N = π/k. Under iid readout noise (observation
φ̂ = φ + ε, ε ~ N(0, σ)) the symbol error probability is 2Φ(−gap/2σ):
the silence zone σ* scales with the gap (measured: σ*_S1 = 0.135 ≥
σ*_S2 = 0.089 ≥ σ*_S3 = 0.038 rad; all inside [gap/12, gap/2]). At
σ = gap the channel breaks down (SER ≈ 0.62). The bits-vs-gap trade-off
is a fundamental property of the phase channel, published as an honest
boundary (ES5).

For accumulative noise (phase diffusion) the time to the first error
scales as t* ~ gap²/σ² — the exploratory measurement's −2 log-log slope
matches theory. Diffusion is deliberately kept threshold-free: it is a
different physics, not mixed with the readout channel.

## 4. Place in the program

The model is the degenerate case of the AB-cloud ISA (processor_ab
module): a phase rotation is one PHASE gate, and the state lattice is a
cyclic subgroup. TS1–TS3 thus give the processor track (P1, V21) a ready
theoretical footing: processor memory is volatile by architecture —
proved, not postulated. For O-J3 (QEC memory) the "volatile phase vs
eternal log" contrast sets the zero point of comparison.

## 5. Honest boundaries

The models abstract away coherent physics (decoherence, relaxation,
systematic drift — out of scope), erasure thermodynamics (no Landauer
claims), and quantum advantage (none claimed). The study is unrelated to
the Riemann hypothesis: the RH status remains blocked by the V13
obligation machine.

Полная русская версия: [`theory.md`](theory.md).
