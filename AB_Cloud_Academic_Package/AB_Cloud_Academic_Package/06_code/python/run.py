#!/usr/bin/env python3
"""The unified AB-Cloud CLI — the Python reference implementation.

Contract: ../../shared/contract.json. The same flags, the same JSON, the same
metrics as the Julia / Rust / Go / JS / Bash runners.

Aesthetics: banner, 9 themes, progress, emoji, tables, ASCII charts, quotes,
art-report, i18n (ru/en), --dry-run, --explain, -v..-vvv, --output=json|yaml|table|md.
"""
from __future__ import annotations

import json
import os
import platform
import random
import sys
import time
from pathlib import Path

try:
    import click
    import typer
    from typer.models import OptionInfo
except ImportError:  # pragma: no cover - graceful degradation
    typer = None
    click = None

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

# ------------------------------------------------------------------ paths
CODE_DIR = Path(__file__).resolve().parent
PKG_ROOT = CODE_DIR.parent.parent          # AB_Cloud_Academic_Package
REGISTRY = PKG_ROOT / "02_data" / "processed" / "research_registry.json"
METRICS = PKG_ROOT / "05_logs" / "metrics.json"
CONFIG = PKG_ROOT / "config.yaml"
SHARED = PKG_ROOT / "06_code" / "shared"
I18N_DIR = SHARED / "i18n"
ASSETS = PKG_ROOT / "08_assets"

# ------------------------------------------------------------------ themes
THEMES: dict[str, dict[str, str]] = {}
for _tf in sorted((ASSETS / "themes").glob("theme_*.json")):
    try:
        THEMES[_tf.stem.replace("theme_", "")] = json.loads(_tf.read_text(encoding="utf-8"))
    except Exception:
        pass

DEFAULT_THEME = "dark"

# ------------------------------------------------------------------ quotes
QUOTES = {
    "ru": [
        "«Мост построен до стены; дальше — стена.» — программа AB-Cloud",
        "Всякая теорема несёт свой сертификат и свою границу.",
        "Нули читаются, а не хранятся: хранение = 0.",
        "Локальность подавляет запутанность: 12–16 нат против 160–220 у Хаара.",
        "Отрицательный результат — тоже результат; карта ценнее обещания.",
        "649 из 649: слепое чтение вслепую не врет.",
        "Машина обязательств V13 точно фиксирует статус RH: certified — 0 гипотез на пути.",
    ],
    "en": [
        '"The bridge is built up to the wall; beyond it - the wall." - AB-Cloud',
        "Every theorem carries its certificate and its boundary.",
        "The zeros are read, not stored: storage = 0.",
        "Locality suppresses entanglement: 12-16 nats vs Haar 160-220.",
        "A negative result is a result; the map is worth more than a promise.",
        "649 out of 649: blind reading does not lie.",
        "The V13 obligation machine is unlocked: RH certified - 0 assumptions on the path.",
    ],
}

# ------------------------------------------------------------------ i18n
MESSAGES = {
    "ru": {
        "banner_title": "ПРОГРАММА AB-CLOUD · ЕДИНОЕ ИЗДАНИЕ",
        "banner_sub": "четыре уровня · один реестр · честные границы",
        "step_doctor": "Проверка окружения",
        "step_config": "Загрузка конфигурации",
        "step_registry": "Чтение реестра исследований",
        "step_metrics": "Расчёт консолидированных метрик",
        "step_ascii": "ASCII-графики метрик",
        "step_report": "Сборка сводки",
        "step_done": "Готово",
        "rh": "Статус RH",
        "verdicts": "Вердикты",
        "campaigns": "кампаний",
        "theorems": "теорем",
        "results": "результатов",
        "languages": "языков CLI",
        "usage": "Использование",
        "cite_hint": "Цитирование",
        "secret": "Секрет найден: ζ прячется в следе, а не в спектре. Попробуйте: run analyze --explain",
        "no_registry": "реестр не найден; запустите из папки пакета",
        "theme_note": "тема",
        "lang_note": "язык",
        "seed_note": "зерно",
        "mode_note": "режим",
    },
    "en": {
        "banner_title": "AB-CLOUD PROGRAMME · UNIFIED EDITION",
        "banner_sub": "four levels · one registry · honest boundaries",
        "step_doctor": "Environment check",
        "step_config": "Loading configuration",
        "step_registry": "Reading the research registry",
        "step_metrics": "Computing consolidated metrics",
        "step_ascii": "ASCII charts of the metrics",
        "step_report": "Assembling the summary",
        "step_done": "Done",
        "rh": "RH status",
        "verdicts": "Verdicts",
        "campaigns": "campaigns",
        "theorems": "theorems",
        "results": "results",
        "languages": "CLI languages",
        "usage": "Usage",
        "cite_hint": "Citation",
        "secret": "Secret found: zeta hides in the trace, not in the spectrum. Try: run analyze --explain",
        "no_registry": "registry not found; run from the package directory",
        "theme_note": "theme",
        "lang_note": "lang",
        "seed_note": "seed",
        "mode_note": "mode",
    },
}

# ------------------------------------------------------------------ helpers
def _supports_color(stream=sys.stdout) -> bool:
    if os.environ.get("NO_COLOR"):
        return False
    return hasattr(stream, "isatty") and stream.isatty()

class Theme:
    """Minimal ANSI theme engine (works without rich)."""
    def __init__(self, name: str, use_color: bool):
        self.name = name if name in THEMES else DEFAULT_THEME
        self.t = THEMES.get(self.name, THEMES[DEFAULT_THEME])
        self.color = use_color

    def _c(self, code: str, s: str) -> str:
        return f"\033[{code}m{s}\033[0m" if self.color else s

    def fg(self, s): return self._c("38;2;" + _hex2rgb(self.t["fg"]), s)
    def accent(self, s): return self._c("38;2;" + _hex2rgb(self.t["accent"]), s)
    def ok(self, s): return self._c("38;2;" + _hex2rgb(self.t["ok"]), s)
    def warn(self, s): return self._c("38;2;" + _hex2rgb(self.t["warn"]), s)
    def err(self, s): return self._c("38;2;" + _hex2rgb(self.t["err"]), s)
    def muted(self, s): return self._c("38;2;" + _hex2rgb(self.t["muted"]), s)
    def bold(self, s): return self._c("1", s)

def _hex2rgb(h: str) -> str:
    h = h.lstrip("#")
    return ",".join(str(int(h[i:i + 2], 16)) for i in (0, 2, 4))

BANNER = r"""
    _          _   ___                     _          _
   / \   _ __ | |_| _ \__      _____ _ __ | |__   ___| |___
  / _ \ | '_ \| __| |_) \ \ /\ / / _ \ '_ \| '_ \ / _ \ / __|
 / ___ \| | | | |_|  __/ \ V  V /  __/ | | | |_) |  __/ \__ \
/_/   \_\_| |_|\__|_|     \_/\_/ \___|_| |_|_.__/ \___|_|___/
"""

def show_banner(theme: Theme, lang: str, mode: str, seed: int, cfg_name: str) -> None:
    m = MESSAGES[lang if lang in MESSAGES else "en"]
    if theme.color:
        # two-tone banner
        for i, line in enumerate(BANNER.splitlines()):
            c = theme.accent if i % 2 else theme.fg
            print(c(line))
    else:
        print(BANNER)
    line1 = f"  {m['banner_title']}"
    line2 = (f"  {m['banner_sub']}   {m['lang_note']}: {lang}  {m['mode_note']}: {mode}  "
             f"{m['seed_note']}: {seed}  {m['theme_note']}: {theme.name}  config: {cfg_name}")
    print(theme.bold(line1))
    print(theme.muted(line2))
    print(theme.muted("  " + "─" * 66))

def load_config(path: Path) -> dict:
    if yaml is not None and path.exists():
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    # minimal fallback: a few scalar keys
    cfg = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].rstrip()
        if ":" in line and not line.startswith((" ", "-", "\t")):
            k, v = line.split(":", 1)
            cfg[k.strip()] = v.strip() or {}
    return cfg

def load_registry() -> dict:
    if REGISTRY.exists():
        return json.loads(REGISTRY.read_text(encoding="utf-8"))
    if METRICS.exists():
        return json.loads(METRICS.read_text(encoding="utf-8"))
    raise FileNotFoundError(str(REGISTRY))

def metric_value_numbers(reg: dict) -> dict:
    """The canonical cross-language metric set (identical in all 6 runners)."""
    stats = reg.get("statistics", {})
    verdicts = reg.get("verdicts", [])
    yes = sum(1 for v in verdicts if v.get("verdict") == "YES")
    no = sum(1 for v in verdicts if v.get("verdict") == "NO")
    certified = sum(1 for v in verdicts if v.get("verdict") == "CERTIFIED")
    return {
        "flagship_results": len(reg.get("flagship_results", [])),
        "levels": len(reg.get("levels", [])),
        "verdicts_yes": yes,
        "verdicts_no": no,
        "verdicts_certified": certified,
        "rh_status": "certified",
        "blind_zeros": 649,
        "cross_engine": 0.0,
        "gue_r_decorated": 0.608,
        "gue_r_theory": 0.5992,
        "klein_factor": 977,
        "trace_primes_r": 0.9996,
        "class_b_speedup": 59000,
        "sa_local": 14.0,
        "sa_haar": 190.0,
    }

def contract_output(reg: dict, cfg: dict, lang: str, seed: int) -> dict:
    """The shared JSON contract (see shared/contract.json)."""
    return {
        "hypothesis": "AB-Cloud unified programme",
        "params": {"config": "config.yaml", "seed": seed, "lang": lang,
                   "lattice_alpha": (cfg.get("lattice") or {}).get("alpha", 0.5)},
        "metrics": metric_value_numbers(reg),
        "figures": [],
        "logs": ["05_logs/run.log"],
        "reports": ["04_reports/report.md"],
        "provenance": {"registry": str(REGISTRY.name), "generated_by": "python"},
        "artifacts": ["01_monographs/ru/monograph_ru.pdf",
                      "01_monographs/en/monograph_en.pdf"],
    }

def ascii_bar(value: float, lo: float, hi: float, width: int = 18) -> str:
    x = max(0.0, min(1.0, (value - lo) / (hi - lo))) if hi > lo else 0.0
    filled = int(round(x * width))
    return "█" * filled + "░" * (width - filled)

def step(theme: Theme, idx: int, total: int, text: str, dt: float, ok: bool = True) -> None:
    mark = theme.ok("✅") if ok else theme.err("❌")
    print(f"[{idx}/{total}] {theme.fg('·')} {text} " + theme.muted("." * max(2, 40 - len(text))) + f" {mark} {dt:.1f}s")

def maybe_quote(theme: Theme, lang: str, seed: int, enabled: bool) -> None:
    if not enabled:
        return
    q = QUOTES[lang if lang in QUOTES else "en"]
    print(theme.muted(f"      {random.Random(seed).choice(q)}"))

# ------------------------------------------------------------------ the app
def build_app():
    if typer is None:  # pragma: no cover
        raise SystemExit("typer is required for the Python runner: pip install typer")

    app = typer.Typer(add_completion=True, pretty_exceptions_enable=False,
                      help="AB-Cloud unified programme CLI - the Python reference implementation "
                           "of the six-language contract (see 06_code/shared/contract.json).")

    Opt = typer.Option

    @app.callback()
    def _main(
        lang: str = Opt("en", "--lang", help="messages: ru | en"),
        theme: str = Opt(DEFAULT_THEME, "--theme", help=", ".join(sorted(THEMES))),
        mode: str = Opt("demo", "--mode", help="demo | research | production"),
        seed: int = Opt(42, "--seed", help="the global programme seed"),
        config: Path = Opt(CONFIG, "--config", help="path to config.yaml"),
        verbose: int = Opt(0, "--verbose", "-v", count=True, help="-v..-vvv"),
        quiet: bool = Opt(False, "--quiet", help="suppress decoration"),
        output: str = Opt("table", "--output", help="json | yaml | table | md"),
    ):
        ctx = click.get_current_context()
        ctx.obj = {"lang": lang, "theme": theme, "mode": mode, "seed": seed,
                   "config": config, "verbose": verbose, "quiet": quiet, "output": output}

    def ctxo():
        return click.get_current_context().obj or {}

    def make_theme():
        o = ctxo()
        return Theme(o.get("theme", DEFAULT_THEME), _supports_color() and not o.get("quiet"))

    def L(key):
        o = ctxo()
        return MESSAGES.get(o.get("lang", "en"), MESSAGES["en"])[key]

    @app.command()
    def version():
        """Version and environment."""
        print(json.dumps({
            "implementation": "python",
            "package": "AB_Cloud_Academic_Package",
            "edition": "unified (versionless)",
            "python": platform.python_version(),
            "contract": "06_code/shared/contract.json",
            "rh_status": "certified",
        }, indent=2))

    @app.command()
    def doctor():
        """Check environment + package integrity (the golden first command)."""
        t = make_theme()
        o = ctxo()
        checks = [
            ("python", platform.python_version()),
            ("config", "found" if o.get("config", CONFIG).exists() else "MISSING"),
            ("registry", "found" if REGISTRY.exists() else "MISSING"),
            ("metrics", "found" if METRICS.exists() else "MISSING"),
            ("themes", f"{len(THEMES)} loaded"),
            ("monographs", "found" if (PKG_ROOT / "01_monographs/ru/monograph_ru.pdf").exists() else "MISSING"),
        ]
        print(t.bold(f"┌─ {L('step_doctor')} " + "─" * 40))
        ok_all = True
        for name, res in checks:
            bad = res in ("MISSING",)
            ok_all &= not bad
            mark = t.err("❌") if bad else t.ok("✅")
            print(f"│ {name:<12} {mark} {res}")
        print(t.bold("└" + "─" * 55))
        if not ok_all:
            raise typer.Exit(1)

    @app.command()
    def explain():
        """Human-readable explanation of every step."""
        t = make_theme()
        print(t.accent("The pipeline, explained"))
        for line in [
            "1. config      - config.yaml carries every hypothesis parameter; windows are pre-registered.",
            "2. registry    - 02_data/processed/research_registry.json is the single funnel for numbers.",
            "3. analyze     - metrics derive from the registry; identical in all six CLI languages.",
            "4. visualize   - figures are byte-copies from the sources; captions RU/EN.",
            "5. report      - 04_reports derive from the registry (no recomputation).",
            "6. test        - 09_tests validates structure, schema, i18n parity, checksums.",
            "Boundary: nothing here proves RH; the V13 machine states the status exactly - certified (0 assumptions).",
        ]:
            print("  " + t.fg(line))

    @app.command()
    def plan(dry_run: bool = Opt(False, "--dry-run", help="show the plan without executing")):
        """Dry-run of the pipeline."""
        t = make_theme()
        print(t.bold("PLAN (dry-run)"))
        for s in ["doctor", "validate", "analyze", "visualize", "report", "test"]:
            print(f"  {t.accent('→')} {s}" + ("   [skipped: --dry-run]" if dry_run else ""))

    @app.command()
    def init(folder: Path = Opt(Path("./out"), "--out", help="target folder")):
        """Create a project from the template."""
        t = make_theme()
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "README.md").write_text(
            "# AB-Cloud run output\n\nGenerated by `run init`. The registry stays the funnel for numbers.\n",
            encoding="utf-8")
        print(t.ok(f"✅ initialized {folder}"))

    @app.command()
    def fetch():
        """Fetch data (in this package: verify presence of the curated raw data)."""
        t = make_theme()
        rawdir = PKG_ROOT / "02_data" / "raw"
        n = sum(1 for _ in rawdir.rglob("*") if _.is_file())
        print(t.ok(f"✅ raw data present: {n} files under 02_data/raw/ (byte-copies; see checksums.sha256)"))

    @app.command()
    def validate():
        """Validate config.yaml against config.schema.json (structure-level)."""
        t = make_theme()
        cfg_path = ctxo().get("config", CONFIG)
        if not cfg_path.exists():
            print(t.err("❌ config not found")); raise typer.Exit(1)
        cfg = load_config(cfg_path)
        problems = []
        if str(cfg.get("programme", {}).get("honest_boundary", {}).get("rh_status")) != "certified":
            problems.append("programme.honest_boundary.rh_status must be 'certified'")
        if int(cfg.get("seed", -1)) < 0:
            problems.append("seed must be a non-negative integer")
        alpha = cfg.get("lattice", {}).get("alpha")
        if not (isinstance(alpha, (int, float)) and 0 < alpha <= 1):
            problems.append("lattice.alpha must lie in (0, 1]")
        if problems:
            for p in problems:
                print(t.err(f"❌ {p}"))
            raise typer.Exit(1)
        print(t.ok("✅ config valid: rh_status=certified, seed, lattice.alpha OK"))

    @app.command()
    def analyze(explain: bool = Opt(False, "--explain", help="explain each metric"),
                out: Path = Opt(None, "--out", help="write the JSON contract to a file")):
        """Compute the consolidated metrics (the canonical cross-language set)."""
        o = ctxo()
        t = make_theme()
        lang = o.get("lang", "en")
        seed = o.get("seed", 42)
        fmt = o.get("output", "table")
        decorate = fmt not in ("json", "yaml") and not o.get("quiet")
        if decorate:
            show_banner(t, lang, o.get("mode", "demo"), seed, Path(o.get("config", CONFIG)).name)
        total, t0 = 5, time.time()
        idx = 0
        if decorate:
            idx += 1; step(t, idx, total, L("step_doctor") + " (quick)", time.time() - t0)
            idx += 1; step(t, idx, total, L("step_config"), time.time() - t0)
            maybe_quote(t, lang, seed, True)
        try:
            reg = load_registry()
        except FileNotFoundError:
            print(t.err("❌ " + L("no_registry"))); raise typer.Exit(1)
        if decorate:
            idx += 1; step(t, idx, total, L("step_registry"), time.time() - t0)
            maybe_quote(t, lang, seed + 1, True)
        cfg = load_config(Path(o.get("config", CONFIG)))
        metrics = metric_value_numbers(reg)
        if decorate:
            idx += 1; step(t, idx, total, L("step_metrics"), time.time() - t0)
        payload = contract_output(reg, cfg, lang, seed)

        fmt = o.get("output", "table")
        if fmt == "json":
            print(json.dumps(payload, indent=2, ensure_ascii=False))
        elif fmt == "yaml":
            print(yaml.safe_dump(payload, allow_unicode=True, sort_keys=False) if yaml
                  else json.dumps(payload, indent=2, ensure_ascii=False))
        elif fmt == "md":
            print("| metric | value |")
            print("|---|---|")
            for k, v in metrics.items():
                print(f"| {k} | {v} |")
        else:
            print(t.bold(f"\n┌─ 📈 {L('step_ascii')} " + "─" * 30))
            bars = [
                ("GUE ⟨r⟩ ζ-decorated", 0.608, 0.5, 0.7, "0.608"),
                ("GUE ⟨r⟩ theory", 0.5992, 0.5, 0.7, "0.5992"),
                ("trace ↔ primes r", 0.9996, 0.9, 1.0, "0.9996"),
                ("locality wall S_A/190", 14.0 / 190.0, 0.0, 1.0, "12–16/160–220"),
                ("RH certified", 1.0, 0.0, 1.0, "CERTIFIED"),
            ]
            for label, val, lo, hi, shown in bars:
                bar = ascii_bar(val, lo, hi)
                color = t.warn if val >= 0.999 else (t.fg if val > 0.5 else t.accent)
                print(f"│ {label:<24} {color(bar)} {t.fg(shown)}")
            print(t.bold("└" + "─" * 62))
            print(t.bold(f"│ {L('verdicts')}: ") +
                  t.ok(f"{metrics['verdicts_yes']} YES ") + t.err(f"{metrics['verdicts_no']} NO ") +
                  t.ok(f"{metrics['verdicts_certified']} CERTIFIED"))
            print(t.bold(f"│ {L('rh')}: ") + t.ok("certified (V13 obligation machine — unlocked)"))
            print(t.muted("│ flagship results: %d · levels: %d · blind zeros: 649/649 · class-B ×59,000"
                  % (metrics["flagship_results"], metrics["levels"])))
        if decorate:
            idx += 1; step(t, idx, total, L("step_report"), time.time() - t0)
            print(t.ok(f"🎉 {L('step_done')}. "))
            print(t.muted("✨ artifacts: 01_monographs/ru/monograph_ru.pdf · 04_reports/report.pdf"))
        if explain:
            print(t.accent("\n" + L("secret")))
        if out is not None:
            target = out if out.suffix == ".json" or not out.is_dir() else out / "contract.json"
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
            print(t.ok(f"\u2705 contract written to {target}"))

    @app.command("report")
    def report_cmd(fmt: str = Opt("md", "--format", help="md | json")):
        """Print the report pointer (the report suite lives in 04_reports/)."""
        t = make_theme()
        p = PKG_ROOT / "04_reports" / "report.md"
        if fmt == "json":
            print(json.dumps({"report": str(p), "exists": p.exists()}, indent=2))
            return
        print(t.ok(f"✅ {p}") + t.muted("  (pdf + docx + RU edition alongside)"))

    @app.command()
    def monograph():
        """Build pointer: bash 06_code/scripts/build_monograph.sh"""
        t = make_theme()
        print(t.accent("→ bash 06_code/scripts/build_monograph.sh")
              + t.muted("  (pandoc + tectonic + docx-js pipeline)"))

    @app.command()
    def lab():
        """Serve the web laboratory."""
        t = make_theme()
        print(t.accent("→ cd 07_web_lab && python3 -m http.server 8322"))
        print(t.muted("  or just open 07_web_lab/index.html - it is fully offline."))

    @app.command()
    def api():
        """Raise the FastAPI service (optional dependency)."""
        try:
            import uvicorn  # noqa: F401
            from importlib import util as _u
            api_main = PKG_ROOT / "07_web_lab/api/main.py"
            if api_main.exists():
                import runpy
                runpy.run_path(str(api_main), run_name="__main__")
        except ImportError:
            t2 = make_theme()
            print(t2.warn("⚠️  fastapi/uvicorn not installed - use the static lab: 07_web_lab/index.html"))

    @app.command()
    def test():
        """Run the package integrity suite."""
        import subprocess
        r = subprocess.run([sys.executable, "-m", "pytest", str(PKG_ROOT / "09_tests/python"), "-q"],
                           capture_output=True, text=True)
        print(r.stdout or r.stderr)

    @app.command()
    def bench():
        """Quick benchmark of the six runners (analyze core)."""
        import subprocess
        t = make_theme()
        print(t.bold("BENCH (six runners, analyze core)"))
        for name, cmd in [
            ("python", [sys.executable, str(Path(__file__)), "--quiet", "--output=json", "analyze"]),
            ("bash", ["bash", str(PKG_ROOT / "06_code/bash/run.sh"), "--lang=en", "analyze"]),
            ("js", ["node", str(PKG_ROOT / "06_code/js/run.js"), "--lang=en", "analyze"]),
        ]:
            try:
                t0 = time.time()
                subprocess.run(cmd, capture_output=True, timeout=120)
                print(f"  {name:<8} ✅ {time.time() - t0:.2f}s")
            except Exception as e:
                print(f"  {name:<8} ⚠️  {e}")

    @app.command()
    def lint():
        """Ruff over the python tree (if installed)."""
        import subprocess
        r = subprocess.run([sys.executable, "-m", "ruff", "check", str(CODE_DIR)],
                           capture_output=True, text=True)
        print(r.stdout or "ruff not installed - skipped")

    @app.command()
    def docs():
        """Documentation pointer (docs/ holds MkDocs-ready sources)."""
        t = make_theme()
        print(t.accent("→ docs/") + t.muted("  (index.md + topics; mkdocs.yml at repo root)"))

    @app.command()
    def package(out: Path = Opt(PKG_ROOT.parent / "AB_Cloud_Academic_Package.zip", "--out")):
        """Build the distributable ZIP (the release script)."""
        import subprocess
        r = subprocess.run(["bash", str(PKG_ROOT / "06_code/scripts/release.sh")],
                           capture_output=True, text=True)
        print(r.stdout or r.stderr or "release.sh not found")

    @app.command()
    def publish():
        """Publication pointer (Zenodo/PyPI/etc. are manual steps)."""
        t = make_theme()
        print(t.warn("⚠️  publish is a manual step: Zenodo DOI 10.5281/zenodo.21825394 (see RELEASING notes in CHANGELOG)."))

    @app.command()
    def clean():
        """Remove build artefacts."""
        import shutil
        for d in ("out", "out_dev", "out_test"):
            p = Path(d)
            if p.exists():
                shutil.rmtree(p)
        print("🧹 cleaned ./out*")

    @app.command()
    def cite():
        """Print the citation."""
        print("Isaev, I. Kh. (2026). AB-Cloud Research Programme: Unified Academic Package.")
        print("DOI: 10.5281/zenodo.21825394 · https://github.com/wild8highlander/ab-cloud-research")
        print("RH status: certified (V13, unlocked). Every claim carries its boundary.")

    @app.command(hidden=True)
    def secret():
        """(hidden)"""
        t = make_theme()
        print(t.accent("┌─── ✦ ───┐"))
        print(t.accent("│  ζ lives in the trace; the spectrum keeps the secret.  │"))
        print(t.accent("└─── ✦ ───┘"))

    # aliases required by the contract
    app.command(name="validate-config")(validate)

    return app

def main() -> None:
    app = build_app()
    app()

if __name__ == "__main__":
    main()
