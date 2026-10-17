# 🛠 `audit/src` — Build Sources of the HPB Canonization Audit

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
