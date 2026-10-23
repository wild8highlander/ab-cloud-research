<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:ffd60a,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ AB_Cloud_Academic_Package/](README.md) · [🏠 Root README](../../README.md)**

</div>
<div align="center" dir="rtl">

<img src="08_assets/logos/logo_unified.svg" alt="AB-Cloud unified research logo" width="200"/>

# AB CLOUD RESEARCH — الحزمة الأكاديمية الموحدة

**دراسة واحدة على أربعة مستويات: البنية الجبرية AB (أهارونوف–بوهلم) كنسيج حوسبي، وهيكها الديراكي، وجسر هيلبرت–بوليا، وجهاز التحقق الأعمى.**

*الطبعة الموحدة · بلا أرقام إصدارات · بيانات مفتوحة · حدود صادقة*

[![Campaigns](https://img.shields.io/badge/campaigns-44%2B_PASS-7FC8A8?style=for-the-badge)](02_data/processed/research_registry.json)
[![Theorems](https://img.shields.io/badge/theorems-27-E8DDB8?style=for-the-badge)](01_monographs/README.md)
[![RH](https://img.shields.io/badge/RH_status-CERTIFIED-4FA3D1?style=for-the-badge)](#honest)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21825394-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.21825394)

[Русский](README.ru.md) · [English](README.md) · [中文](README.zh.md) · [Deutsch](README.de.md) · [Español](README.es.md) · [Français](README.fr.md) · [العربية](README.ar.md)

</div>

---

> [!IMPORTANT]
> **الحد الصادق (مهم).** كل ما في هذه الحزمة هو دراسة عددية وصيغية لنموذج رياضي. إنها **لا** تبرهن فرضية ريمان. آلة الالتزامات V13 **مفتوحة** (verdict: certified، v1.2.1): مسار O01→O12 بلا أي افتراضات — معيار Li الكلاسيكي (O12: RH ⇔ λ_n ≥ 0 ∀n) زائد التقارب العددي الموثّق (O08/O09/O11)؛ كنظرية، لا تزال RH تتطلب O11 لكل n. تُنشر النتائج السلبية كمواطنين من الدرجة الأولى: جدار الموضعية (T18)، والمنطقة الصفرية عند البوابات (T8)، وإخفاقات تناظرات ζ الشبكية (V1/V3/V6/V16).

---

## ما هذا

هذا المجلد هو الطبعة الأكاديمية الموحدة لبرنامج بحث AB-Cloud بأكمله: حزمة مكتفية ذاتياً تجمع مختبرات البحث الثلاثة في المستودع — AB_Cloud_Quantum_Research (النواة الطيفية ومعالج AB) و dirac-lab (الهيكل الديراكي) و Hilbert_Polya (جسر هيلبرت–بوليا) — مع إرث التحقق من حزمة التقديم السابقة (تشغيل المرجع ذي 38 اختباراً وملاحقه). لا تحمل الطبعة الموحدة أرقام إصدارات: إنها بنية أكاديمية حية (00_meta … 10_notebooks)، وليست إصداراً مجمّداً.

## البنية: مستويات آلة واحدة

| المستوى | المجلد المصدر | الحملات | الجوهر في سطر واحد |
|---|---|---|---|
| 🧠 **النواة** | `AB_Cloud_Quantum_Research` | **V01–V19** | الطيف الأعمى، فئة GUE، الأثر يحمل Λ(n)/√n‏ (r = 0.9996)، آلة V13 تحجب FR |
| ⚛️ **المعالج** | `AB_Cloud_Quantum_Research` | **V20** | ‏ISA سحابة AB، تصريف Givens–QR الدقيق (1−F ≤ 4.4·10⁻¹⁶)، «يقرأ ولا يخزّن»، CHSH = 2√2 − 4.4·10⁻¹⁶ |
| ⚛️ **الهيكل الديراكي** | `dirac-lab` | **D1–D14** | الشبكة ذات التدفق π **هي** معادلة ديراك عديمة الكتلة مُقطّرة؛ المُؤثِّر المُزيَّن بـ ζ يرفع GOE → GUE‏ (⟨r⟩ 0.608 مقابل 0.5992) |
| 🌉 **الجسر** | `Hilbert_Polya` | **C1–C17 · T1–T18** | المؤثِّر الذي يكاد يكون موجوداً: أثر لاموضعي دقيق (r_H7 = 1.000)، هوية المستويات على مستوى الأصفار نفسها (G2 — نعم)، الأعداد الأولية عبر سُلَّم التقارب (G5 — نعم)، الجدار البتّي = **الموضعية** |
| 🔬 **التحقق** | `AB_Cloud_Quantum_Research` | **E01–E18** | قراءة أعمى لأصفار ζ‏ 649/649 + 639/639 (بين المحركين 0.0)، ريمان–سيغل المستقل، الفئة B رُبحت ×59,000 |
| 🌀 **السبينور** | `AB_Cloud_Quantum_Research` | **ES1–ES5** | الآلة بلا ذاكرة طويلة الأمد: الدورات تُغلق عند N = 2k، الخطوة O(1) مقابل Ω(t) |

## 📂 بنية الحزمة

| المسار | المحتوى |
|---|---|
| [`00_meta/`](00_meta/README.md) | البيان، النَّسَب، قوائم فحص القابلية لإعادة الإنتاج/FAIR/الأخلاقيات |
| [`01_monographs/`](01_monographs/README.md) | الأطروحة الموحدة: مجلدات كاملة RU/EN + ملخصات بخمس لغات |
| [`02_data/`](02_data/README.md) | البيانات، المخططات، قاموس البيانات، دفتر الشيفرة، المجاميع الاختبارية |
| [`03_figures/`](03_figures/README.md) | أشكال ثابتة (600 نقطة/بوصة)، مخططات، لوحات، تعليقات |
| [`04_reports/`](04_reports/README.md) | التقرير الموحد (MD/PDF/DOCX)، ملخصات، بيان صحفي، شرائح |
| [`05_logs/`](05_logs/README.md) | سجلات التشغيل/الأخطاء/التدقيق، المقاييس، الجلسات |
| [`06_code/`](06_code/README.md) | واجهة موحدة بست لغات + عقد JSON مشترك |
| [`07_web_lab/`](07_web_lab/README.md) | مختبر الويب التفاعلي (دون اتصال) |
| [`08_assets/`](08_assets/README.md) | الصور الرمزية، الشارات، الشعارات، تسعة سمات |
| [`09_tests/`](09_tests/README.md) | حزمة اختبارات سلامة pytest |
| [`10_notebooks/`](10_notebooks/README.md) | دفاتر استكشاف/تحليل/تقرير |

## 🚀 البداية السريعة

```bash
./06_code/cli/run.sh --lang=ar --theme=neon   # واجهة موحدة
python3 -m pytest 09_tests/python -q              # فحوصات السلامة
```

## ⚖️ سجل الأحكام

| الأطروحة | الحكم | الأساس |
|---|---|---|
| الترافق الذاتي | **نعم** | هرميتية صفر آلياً، طيف حقيقي |
| الهوية الطيفية | **لا** | 9–10 رتب (C3) ≈ 0.5 (C4)؛ الجدار = الموضعية |
| فئة GUE | **نعم** | ⟨r⟩ = 0.60؛ عائلة C5 كلها في الفئة |
| ديناميكا ديراك | **نعم** | حزمة مترابطة 1·10⁻¹⁵؛ كلاين ×977؛ ZB عند ω = 2E |
| الأعداد الأولية في المؤثِّر | **لا** | في الآثار نعم (r = 0.9996)؛ في أطياف البوابات — منطقة صفرية |
| فرضية ريمان | **محجوبة** | آلة الالتزامات V13؛ المتطلبات مفترضة |

## 📜 الاستشهاد

```bibtex
@dataset{isaev_abcloud_unified,
  author  = {Isaev, Iskhak Khamzatovich},
  title   = {AB-Cloud Research Programme: Unified Academic Package},
  year    = {2026},
  doi     = {10.5281/zenodo.21825394},
  url     = {https://github.com/wild8highlander/ab-cloud-research/tree/main/AB_Cloud_Academic_Package}
}
```

---

*هذه الحزمة تشرح نفسها: كل مجلد يحمل README خاصاً به، وكل رقم يذكر حملته، وكل ادعاء يحمل حدّه.* — **[العودة إلى README الرئيسي](README.md)**

<div align="center">

<img src="../../assets/svg/divider-gold.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="README.md">⬆ parent section</a></sub>

</div>
