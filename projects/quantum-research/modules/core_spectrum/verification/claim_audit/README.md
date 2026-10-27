<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:ff2ec4,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ core_spectrum/](../../README.md) · [🏠 Root README](../../../../../README.md)**

</div>
# verification/claim_audit/ — the claim audit (campaign V14)

`claims/` holds one file per campaign, `claim_v01.json` …
`claim_v19.json`. The schema (Solution 14 of the plan): **statement**
(the exact statement), **premises**, **code** (reproducible code),
**controls** (with passed flags), **does_not_prove** (what the result
does NOT prove), **status** (proven/measured/conjecture/refuted).

The auditor checks (`rpbridge/audit.py`): A1 — all five parts are
non-empty; A2 — status hygiene (proven requires a passed control and
non-implications, p-values are banned); A3 — coverage of all verdicts
data/v*.json.

The statuses of the series: **proven** — V4, V7, V8, V9, V12, V15;
**measured** — the remaining thirteen (V16–V19 included with
v1.1.0/v1.2.0). An audit regression is a release stopper.

<div align="center">

<img src="../../../../../assets/svg/divider-magenta.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../../../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="../../README.md">⬆ parent section</a></sub>

</div>
