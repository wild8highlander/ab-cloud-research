# 08_assets — the visual identity of the unified edition

| Folder | Contents |
|---|---|
| [`avatars/`](avatars/) | the cast: author, core, processor, verifier, spinor (from AB_Cloud_Quantum_Research) + Riemann, Hilbert, Pólya (from Hilbert_Polya) |
| [`badges/`](badges/) | 12 SVG badges (levels, campaigns, theorems, tests, languages, verdicts, RH, honesty, monographs, i18n, licence, reproducibility) |
| [`logos/`](logos/) | `hero_banner.svg` (the **animated hero banner** of the master README), `logo_unified.svg` (the unified logo), `banner_unified.svg` (the static banner), the source programme's light/dark PNG logos |
| [`icons/`](icons/) | 10 level icons (`icon_core`, `icon_processor`, `icon_dirac`, `icon_bridge`, `icon_verification`, `icon_heritage`, `icon_observatory`, `icon_vortex`, `icon_wave`, `icon_spinor`) — used inline in the README architecture table |
| [`animations/`](animations/) | SMIL-animated decorations: `footer_wave.svg` (the flowing critical-strip wave of the README footer) and `divider_neon.svg` (the travelling-photon section divider) |
| [`themes/`](themes/) | 9 theme palettes (light, dark, neon, dracula, nord, catppuccin, solarized, gruvbox, accessible) — used by the CLI, the web lab and figure generation |
| `sounds/`, `fonts/`, `backgrounds/`, `illustrations/` | reserved slots per the unified structure specification |

## The palette of the unified edition

| Role | Colour | Used for |
|---|---|---|
| Deep graphite | `#0B1F35` | banner background, master text on light theme |
| Graphite blue | `#162032` / `#123252` | gradient stops |
| Gold | `#C9B97E` → `#E8DDB8` | the ζ node, frames, accents, typing text (dark theme) |
| Sage | `#7FC8A8` | the ζ zeros, positive accents |
| Slate blue | `#7FA8D0` | the lattice grid, secondary accents |
| Neon cyan | `#00E5FF` | the scan sweep, travelling pulses — the "observatory at night" glow |

## Animation notes

All motion is **SMIL** (`<animate>`, `<animateMotion>`, `<animateTransform>`)
inside self-contained SVG files: no JavaScript, no CSS keyframes, no external
requests. Every animated element sits on a fully rendered static base layer,
so if a consumer disables or filters SMIL, the banner, divider and footer
remain complete static graphics. GitHub serves repository SVGs through its
image pipeline, where SMIL animation is preserved; expect roughly a one-hour
camouflage cache delay after edits.

## Attribution

Avatar and logo files are byte copies from the source laboratories
(`AB_Cloud_Quantum_Research/assets/`, `Hilbert_Polya/assets/`) — see
`00_meta/provenance.jsonl`. The unified logo, banner and badges were
generated fresh for this edition (script: `scripts/gen_assets.py` pattern).
The animated hero banner, the neon divider, the footer wave and the ten level
icons were generated for the 2026-10 link-repair edition under the same
umbrella licence. Licences follow the umbrella `LICENSE` (attribution
preserved).
