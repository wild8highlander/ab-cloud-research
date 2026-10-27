<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:a78bfa,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ audit/](../README.md) · [🏠 Root README](../../../README.md)**

</div>
# 🛠 `audit/src` — Build Sources of the HPB Canonization Audit

> **🧭 Navigation:** [audit/](../README.md) · [Hilbert_Polya/](../../README.md) · [Root README](../../../README.md)

The build pipeline of the analytical report
`HPB_audit_canonization_2026-10-13_ru` (its shipped outputs — `.pdf` and
`.docx` — live one level up in [`../`](../)). Nothing here is runtime code of
the Hilbert–Pólya audit battery; this folder is how the *document* is produced
from the battery's committed results.

| File | Role |
|---|---|
| [`audit_build.py`](audit_build.py) | the orchestrator: assembles the body via ReportLab (with TOC) and the cover via the Template-01 (HUD) html2poster path, then merges the intermediate `_body.pdf` + `_cover.pdf` build artifacts into the final PDF; hashes every input for the build log |
| [`audit_content.py`](audit_content.py) / [`audit_content2.py`](audit_content2.py) / [`audit_content3.py`](audit_content3.py) | the chapter content modules — text, tables and verdict rows of the report, in assembly order |
| [`content.json`](content.json) | the structured content dump consumed by the docx branch |
| [`audit_docx.js`](audit_docx.js) | the `.docx` build branch (Node) mirroring the same content |

## Rebuild

```bash
# PDF (Python + ReportLab + a PDF-skill html2poster cover):
python3 audit_build.py                 # writes ../HPB_audit_canonization_2026-10-13_ru.pdf

# DOCX (Node):
node audit_docx.js
```

> [!NOTE]
> The report's numbers are **not** re-derived here — they quote the committed
> battery results verbatim. If the battery re-runs, update the content modules
> and rebuild; the build log's input hashes will reflect the change.

Landing page of the shipped report: [`../README.md`](../README.md)

---

<!-- enriched-r3 -->

This folder holds the **pipeline scripts** of its module: the deterministic code paths that turn frozen inputs into reports, figures and verdicts. The scripts follow the repository's seed discipline — same input, same seed, same bytes out — so a re-run on the pinned platform reproduces the committed artifacts. Nothing here is executed at import time by other modules; they are entry points, documented in the module README.

The build sources of the HPB canonization audit: the scripts that regenerate the audit document from the committed verdicts.

## Folder contents

| File | Size | What it is |
|---|---|---|
| `audit_build.py` | 17 KB | Python source |
| `audit_content.py` | 63 KB | Python source |
| `audit_content2.py` | 24 KB | Python source |
| `audit_content3.py` | 27 KB | Python source |
| `audit_docx.js` | 16 KB | JavaScript source |
| `content.json` | 115 KB | JSON data / config |

<div align="center">

<img src="../../../assets/svg/divider-violet.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="../README.md">⬆ parent section</a></sub>

</div>
