"""RU and EN message catalogues must have identical key sets."""
import json
import re
from pathlib import Path


def _shared(pkg):
    ru = json.loads((pkg / "06_code/shared/i18n/ru.json").read_text(encoding="utf-8"))
    en = json.loads((pkg / "06_code/shared/i18n/en.json").read_text(encoding="utf-8"))
    return ru, en


def test_shared_catalogues_parity(pkg):
    ru, en = _shared(pkg)
    assert set(ru) == set(en), "shared i18n keys diverge"
    assert ru["banner_title"] != en["banner_title"]  # actually translated
    assert len(ru["steps"]) == len(en["steps"]) == 5


def test_cli_messages_parity():
    src = Path(__file__).resolve().parents[2] / "06_code/python/run.py"
    text = src.read_text(encoding="utf-8")
    m = re.search(r"MESSAGES = \{(.*?)\n\}\n", text, re.S)
    assert m, "MESSAGES dict not found in run.py"
    ru_keys = set(re.findall(r'"(\w+)":', m.group(1).split('"ru"')[-1].split('"en"')[0]))
    en_keys = set(re.findall(r'"(\w+)":', m.group(1).split('"en"')[-1]))
    assert ru_keys == en_keys, f"run.py i18n keys diverge: {ru_keys ^ en_keys}"


def test_web_lab_i18n_parity(pkg):
    html = (pkg / "07_web_lab/index.html").read_text(encoding="utf-8")
    i_en = html.index("en: {")
    i_ru = html.index("ru: {")
    i_end = html.index("}", html.index("bars_note", i_ru))
    keys = lambda b: set(re.findall(r"^\s{4}(\w+):", b, re.M))
    ru, en = keys(html[i_ru:i_end]), keys(html[i_en:i_ru])
    assert ru and en, "web lab I18N blocks not found"
    assert ru == en, f"web lab i18n keys diverge: {ru ^ en}"


def test_glossary_ids_stable(pkg):
    def ids(lang):
        rows = (pkg / f"00_meta/glossary/glossary.{lang}.md").read_text(encoding="utf-8")
        return [l.split("|")[1].strip() for l in rows.splitlines() if l.startswith("| ") and "---" not in l][1:]
    assert ids("ru") == ids("en") == ids("zh"), "glossary ids must be stable across languages"
