"""Reports suite + web laboratory integrity."""
import json
from pathlib import Path


def test_report_suite(pkg):
    for f in ("report.md", "report.pdf", "report.docx", "executive_summary.md",
              "lay_summary.md", "press_release.md", "policy_brief.md",
              "one_pager/one_pager.md", "slides/deck.md"):
        assert (pkg / "04_reports" / f).is_file(), f"missing 04_reports/{f}"


def test_report_honesty(pkg):
    text = (pkg / "04_reports/report.md").read_text(encoding="utf-8")
    assert "CERTIFIED" in text
    assert "does not" in text.lower() or "not establish" in text.lower()


def test_web_lab_data_injected(pkg):
    html = (pkg / "07_web_lab/index.html").read_text(encoding="utf-8")
    assert "const DATA" in html
    assert '"rh_status": "certified"' in html or '"rh_status":"certified"' in html
    assert html.count("data-theme") >= 1
    # zero external requests
    assert "http://" not in html and "https://doi.org" in html  # only the DOI link
    assert "<script src=" not in html  # no external scripts


def test_web_lab_offline(pkg):
    """No CDN references (fonts.googleapis etc. would phone home)."""
    html = (pkg / "07_web_lab/index.html").read_text(encoding="utf-8")
    for banned in ("fonts.googleapis", "cdn.", "unpkg", "jsdelivr"):
        assert banned not in html, f"external reference found: {banned}"


def test_metrics_json_matches_registry(pkg, registry):
    metrics = json.loads((pkg / "05_logs/metrics.json").read_text(encoding="utf-8"))
    assert metrics["verdicts"] == registry["verdicts"]
    assert metrics["display_stats"]["rh_status"] == "certified"
