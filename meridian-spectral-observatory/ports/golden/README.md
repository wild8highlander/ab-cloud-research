<div align="center">

# 🥇 Golden — the Reference Anchors

**The single source of truth of the whole ports family: JSON files of
anchors generated from the UNMODIFIED Julia originals, plus the Julia
scripts that produce them. No anchor, no test.**

*199 base anchors · 279 stack anchors · ω/t grids inside · `%.17g` exact round-trip*

<img src="../assets/divider.svg" width="1152" alt="Animated neon divider"/>

</div>

## What lives here

| File | What it is |
|---|---|
| [`gen_golden.jl`](gen_golden.jl) (435 lines) | the base generator: includes the **unmodified** originals (`ab_cloud_full.jl` and friends), runs every section, writes the base JSON — 35 sections, 199 anchors, plus the ω (726) and t (30) grids |
| [`abcloud_golden.json`](abcloud_golden.json) | **the base contract** — every scalar the ports must reproduce: bN ladder, Gram points, GOF statistics, RMT tables, lattice theorems (Byers–Yang, Dirac flux, chiral, Connes), §8 vector tier |
| [`gen_golden_stack.jl`](gen_golden_stack.jl) (491 lines) | the stack generator: HP gates H1–H8 + RH SP/v5 + Monumental gallery + rng semantics → 27 sections |
| [`abcloud_golden_stack.json`](abcloud_golden_stack.json) | **the stack contract** — 27 sections; consumed by the Python stack selftest (279/279 anchors) |
| [`gen_hp_battery.jl`](gen_hp_battery.jl) + [`hp_battery_checkpoint.jl`](hp_battery_checkpoint.jl) | the standalone H-battery generator and its resumable checkpoint script |
| [`hp_battery_golden.json`](hp_battery_golden.json) | the 8 HP gates alone (9 sections) — the battery headline numbers |

## How the contract works

1. **Generation**: `gen_golden.jl` includes the Julia sources verbatim — no
   reimplementation on the Julia side either — and runs each section through
   the original functions. Every float is written with `%.17g`, so the JSON
   round-trips the Julia Float64 exactly.
2. **Consumption**: each port's `selftest` recomputes every section from the
   same inputs (the 50,000 Odlyzko zeros in the meridian root) and compares
   against the JSON with the per-section tolerances of
   [`../PORT_SPEC.md`](../PORT_SPEC.md) §3 (1e-9 scalars → 1e-6 Fourier/§8).
3. **Keys**: section keys use Julia `string(Float64)` formatting — shortest
   round-trip representation with a decimal point (`1.0 → "1.0"`, `0.05 →
   "0.05"`); a key-format mismatch is a FAIL, not a near-miss.
4. **RNG**: all window sampling is the classic MT19937 embedded identically
   in the generator and all four ports — Σ²/Δ₃ windows are bit-identical
   across languages. Julia's own `MersenneTwister` (dSFMT) is deliberately
   NOT used anywhere in the parity surface.

```bash
# regenerate (Julia 1.10+, stdlib only, zeros50k.txt in the meridian root):
julia gen_golden.jl <meridian_dir> <out.json>
julia gen_golden_stack.jl . ../abcloud_golden_stack.json
julia gen_hp_battery.jl   . ../hp_battery_golden.json
```

> [!IMPORTANT]
> The committed JSONs are the contract. Regenerate them only to re-derive
> them from the originals — never to "fix" a failing port. If a port
> disagrees with the golden, the port is wrong until proven otherwise
> (and the proof belongs in `PORT_SPEC.md` §7, next to the other traps).

<div align="center">

**[↑ Ports overview](../README.md)** · [PORT_SPEC.md](../PORT_SPEC.md) · [Julia originals](../../)

</div>
