"""The monograph must keep its honesty structure and full section skeleton."""
import re
from pathlib import Path


SECTIONS_RU = ["Аннотация", "Введение", "Связанные работы", "Архитектура",
               "Уровень I", "Уровень II", "Уровень III", "Уровень IV",
               "Спинор-исследование", "Данные и воспроизводимость",
               "Сводный экспериментальный регистр", "Результаты и вердикты",
               "Обсуждение: стена локальности", "Ограничения", "Заключение",
               "Литература", "Приложение A", "Приложение B",
               "научно-этические заявления"]
SECTIONS_EN = ["Abstract", "Introduction", "Related work", "Architecture",
               "Level I", "Level II", "Level III", "Level IV",
               "spinor study", "Data and reproducibility",
               "experiment register", "Results and verdicts",
               "locality wall", "Limitations", "Conclusion",
               "References", "Appendix A", "Appendix B", "ethics statements"]


def test_ru_monograph_sections(pkg):
    text = (pkg / "01_monographs/ru/monograph_ru.md").read_text(encoding="utf-8")
    low = text.lower()
    missing = [s for s in SECTIONS_RU if s.lower() not in low]
    assert not missing, f"RU monograph missing sections: {missing}"


def test_en_monograph_sections(pkg):
    text = (pkg / "01_monographs/en/monograph_en.md").read_text(encoding="utf-8")
    low = text.lower()
    missing = [s for s in SECTIONS_EN if s.lower() not in low]
    assert not missing, f"EN monograph missing sections: {missing}"


def test_honesty_boundary_present(pkg):
    for lang in ("ru", "en"):
        text = (pkg / f"01_monographs/{lang}/monograph_{lang}.md").read_text(encoding="utf-8")
        assert "blocked" in text, f"{lang} monograph lost the blocked verdict"
        assert "не доказыва" in text or "does not prove" in text.lower() or "not prove" in text.lower()


def test_numbers_carry_campaigns(pkg):
    """Every register row must name its campaign."""
    import json
    reg = json.loads((pkg / "02_data/processed/research_registry.json").read_text(encoding="utf-8"))
    for row in reg["numbers_registry"]:
        assert row.get("campaign"), f"registry row {row.get('n')} has no campaign"


def test_max_editions_present(pkg):
    """The MAX editions: ~100k words each, with figures and the honest boundary."""
    import re
    for lang in ("ru", "en"):
        md = pkg / f"01_monographs/{lang}/monograph_{lang}_max.md"
        text = md.read_text(encoding="utf-8")
        words = len(re.findall(r"\S+", text))
        assert words > 80_000, f"{lang} MAX edition too small: {words} words"
        assert "blocked" in text, f"{lang} MAX lost the blocked verdict"
        # уровни нового обогащения
        for section in ("v19", "H5", "T34", "W1"):
            assert section in text, f"{lang} MAX missing enrichment section {section}"
        # фигуры
        imgs = re.findall(r"!\[[^\]]*\]\(([^)]+\.png)\)", text)
        assert len(imgs) >= 15, f"{lang} MAX has too few embedded figures: {len(imgs)}"


def test_max_built(pkg):
    for lang in ("ru", "en"):
        pdf = pkg / f"01_monographs/{lang}/monograph_{lang}_max.pdf"
        assert pdf.stat().st_size > 1_000_000
        assert pdf.read_bytes()[:5] == b"%PDF-"
        docx = pkg / f"01_monographs/{lang}/monograph_{lang}_max.docx"
        assert docx.stat().st_size > 500_000
        assert docx.read_bytes()[:2] == b"PK"


def test_ru_pdf_built(pkg):
    pdf = pkg / "01_monographs/ru/monograph_ru.pdf"
    assert pdf.stat().st_size > 50_000
    assert pdf.read_bytes()[:5] == b"%PDF-"


def test_en_docx_built(pkg):
    docx = pkg / "01_monographs/en/monograph_en.docx"
    assert docx.stat().st_size > 20_000
    assert docx.read_bytes()[:2] == b"PK"
