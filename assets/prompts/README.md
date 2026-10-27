# assets/prompts — AI image prompts registry

Registry of the prompts used to generate every AI-rendered visual in the
repository (section banners, avatars, concept illustrations). Each entry is
identified by a stable id (`P-01`, `P-10`, …) that the enriched READMEs cite
in their art credits (`<!-- AI end-cap — prompt P-10 -->` blocks).

- [`AI_PROMPTS.md`](AI_PROMPTS.md) — the full prompt catalogue with palette
  annotations (`#05060f · #00e5ff · #ff2ec4 · #a78bfa · #ffd60a`).
- [`../manifest.json`](../manifest.json) — machine-readable asset map
  (which prompt produced which file).
- [`../`](../README.md) — how the visual system fits together.

Regenerate or extend artwork only through the registry: add the prompt here
first, then the rendered file under `assets/banners/`, `assets/visuals/` or
`assets/avatars/`, then wire the id into the README end-cap.
