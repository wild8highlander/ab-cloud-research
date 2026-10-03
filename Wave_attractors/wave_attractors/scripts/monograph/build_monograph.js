/**
 * build_monograph.js — entry point: assembles the W1 monograph DOCX.
 *
 * Usage:  NODE_PATH=<global node_modules> node build_monograph.js --lang ru|en
 * Output: wave_attractors/monograph/<lang>/text/AB_Cloud_Monograph_W1_<LANG>.docx
 */

const fs = require("fs");
const path = require("path");
const { buildDocument } = require("./monograph_lib.js");

const lang = process.argv.includes("--lang")
  ? process.argv[process.argv.indexOf("--lang") + 1]
  : "ru";
if (lang !== "ru" && lang !== "en") throw new Error("--lang ru|en");

const meta = require("./content_meta_" + lang + ".js");
const body = [
  ...require("./content_a_" + lang + ".js"),
  ...require("./content_b_" + lang + ".js"),
];

const cfg = { ...meta, body };
const ROOT = path.resolve(__dirname, "..", "..");
const outDir = path.join(ROOT, "monograph", lang, "text");
fs.mkdirSync(outDir, { recursive: true });
const outFile = path.join(outDir, meta.fileName);

buildDocument(cfg).then(buf => {
  fs.writeFileSync(outFile, buf);
  console.log("written:", outFile, buf.length, "bytes");
}).catch(e => { console.error(e); process.exit(1); });
