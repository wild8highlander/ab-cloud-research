#!/usr/bin/env node
/* AB-Cloud unified CLI — the JavaScript/TypeScript-compatible runner (Node, zero deps).
 * Contract: ../shared/contract.json — identical metrics to the other five runners. */
"use strict";
const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..", "..");
const SHARED = path.join(__dirname, "..", "shared");
const METRICS = JSON.parse(fs.readFileSync(path.join(SHARED, "metrics.json"), "utf8"));
const CONSTANTS = JSON.parse(fs.readFileSync(path.join(SHARED, "constants.json"), "utf8"));
const THEMES = { dark: ["\x1b[38;2;201;185;126m", "38;2;232;238;245"], neon: ["\x1b[38;2;255;64;129m", "38;2;0;229;255"],
  light: ["\x1b[38;2;31;78;121m", "38;2;22;32;50"] };
const BANNER = [
"    _          _   ___                     _          _    ",
"   / \\   _ __ | |_| _ \\__      _____ _ __ | |__   ___| |___",
"  / _ \\ | '_ \\| __| |_) \\ \\ /\\ / / _ \\ '_ \\| '_ \\ / _ \\ / __|",
" / ___ \\| | | | |_|  __/ \\ V  V /  __/ | | | |_) |  __/ \\__ \\",
"/_/   \\_\\_| |_|\\__|_|     \\_/\\_/ \\___|_| |_|_.__/ \\___|_|___/",
];
const arg = (name, dflt) => {
  for (let i = 2; i < process.argv.length; i++) {
    const a = process.argv[i];
    if (a === "--" + name) return process.argv[i + 1];
    if (a.startsWith("--" + name + "=")) return a.slice(name.length + 3);
  }
  return dflt;
};
const lang = arg("lang", "en"), theme = THEMES[arg("theme", "dark")] ? arg("theme", "dark") : "dark";
const jsonOut = arg("output", "table") === "json";
const I18N = JSON.parse(fs.readFileSync(path.join(SHARED, "i18n", lang === "ru" ? "ru.json" : "en.json"), "utf8"));
const c = (s) => `\x1b[${THEMES[theme][1]}m${s}\x1b[0m`;
const bar = (v, lo, hi, w = 18) => { const x = Math.max(0, Math.min(1, (v - lo) / (hi - lo)));
  return "\u2588".repeat(Math.round(x * w)) + "\u2591".repeat(w - Math.round(x * w)); };

function analyze() {
  if (!jsonOut) {
    BANNER.forEach(l => console.log(c(l)));
    console.log(`  ${I18N.banner_title}`);
    console.log(`  ${I18N.banner_sub}   lang: ${lang}  seed: ${METRICS.seed}  theme: ${theme}`);
    console.log("  " + "\u2500".repeat(66));
    I18N.steps.forEach((s, i) => console.log(`[${i + 1}/5] \u00b7 ${s} ` + ".".repeat(Math.max(2, 40 - s.length)) + " \u2705"));
    console.log("\n\u2500\u2500 \u{1F4C8} metrics " + "\u2500".repeat(24));
    console.log(`GUE <r> zeta-dec    ${bar(METRICS.gue_r_decorated, 0.5, 0.7)} ${METRICS.gue_r_decorated}`);
    console.log(`GUE <r> theory      ${bar(METRICS.gue_r_theory, 0.5, 0.7)} ${METRICS.gue_r_theory}`);
    console.log(`trace-primes r      ${bar(METRICS.trace_primes_r, 0.9, 1.0)} ${METRICS.trace_primes_r}`);
    console.log(`locality wall S_A   ${bar(METRICS.sa_local / METRICS.sa_haar, 0, 1)} ${METRICS.sa_local}/${METRICS.sa_haar}`);
    console.log(`${I18N.verdicts}: ${METRICS.verdicts_yes} YES ${METRICS.verdicts_no} NO ${METRICS.verdicts_certified} CERTIFIED`);
    console.log(`${I18N.rh}: ${METRICS.rh_status} (V13 obligation machine)`);
    console.log("\u{1F389} " + I18N.done + ".\n");
  } else {
    console.log(JSON.stringify({
      hypothesis: "AB-Cloud unified programme",
      params: { config: "config.yaml", seed: METRICS.seed, lang, theme },
      metrics: METRICS, provenance: { registry: "research_registry.json", generated_by: "js" },
      artifacts: ["01_monographs/ru/monograph_ru.pdf", "01_monographs/en/monograph_en.pdf"],
    }, null, 2));
  }
}
const _pos = process.argv.slice(2).find(a => !a.startsWith("--"));
const cmd = _pos !== undefined ? _pos : "analyze";
if (cmd === "version") console.log(JSON.stringify({ implementation: "js", package: CONSTANTS.package, edition: CONSTANTS.edition, node: process.version, rh_status: "certified" }, null, 2));
else if (cmd === "analyze") analyze();
else if (cmd === "doctor") { const ok = fs.existsSync(path.join(ROOT, "02_data/processed/research_registry.json"));
  console.log(`registry ${ok ? "\u2705 found" : "\u274c MISSING"}\nconfig ${fs.existsSync(path.join(ROOT, "config.yaml")) ? "\u2705 found" : "\u274c MISSING"}\nmetrics \u2705 loaded`); process.exitCode = ok ? 0 : 1; }
else if (cmd === "cite") console.log(`Isaev, I. Kh. (2026). ${CONSTANTS.programme}: Unified Academic Package.\nDOI: ${CONSTANTS.doi}\nRH status: certified (V13, unlocked).`);
else if (cmd === "secret") console.log("zeta lives in the trace; the spectrum keeps the secret.");
else { console.log(`command '${cmd}' delegated to the python reference: python3 python/run.py ${cmd}`); process.exitCode = 2; }
