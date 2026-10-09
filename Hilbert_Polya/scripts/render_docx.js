// render_docx.js — рендер монографий серии в DOCX (docx-js).
// Правила скилла: обложка-рецепт R1 (обёртка 16838 exact, allNoBorders,
// margin 0 секция), 3-секционная нумерация (обложка / TOC-римские / тело —
// арабские с 1), заголовки HeadingLevel, таблицы в процентах с CLEAR-заливкой,
// картинки с сохранением пропорций, TOC + подсказка + PageBreak.
// Использование: node render_docx.js <content.json> <out.docx> [lang]
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, ImageRun,
  PageBreak, Header, Footer, PageNumber, NumberFormat, AlignmentType,
  HeadingLevel, WidthType, BorderStyle, ShadingType, TableOfContents,
  SectionType, TableLayoutType,
} = require("docx");
const fs = require("fs");
const path = require("path");

const ROOT = path.dirname(path.dirname(path.resolve(__filename)));
const [contentPath, outPath, langArg] = process.argv.slice(2);
const lang = langArg || "ru";
const doc = JSON.parse(fs.readFileSync(contentPath, "utf8"));

// ━━ палитра серии ━━
const P = {
  bg: "2E3F49", titleColor: "F0F4F5", subtitleColor: "B7C6CC",
  metaColor: "D7E2E6", footerColor: "93A7AE", accent: "298BBC",
  copper: "C96F4A", ink: "222526", muted: "777E81", header: "3B4F58",
  surface: "EBEDEE", grid: "C7D3D9",
};
const NB = { style: BorderStyle.NONE, size: 0, color: "auto" };
const allNoBorders = { top: NB, bottom: NB, left: NB, right: NB,
  insideHorizontal: NB, insideVertical: NB };
const noBorders = { top: NB, bottom: NB, left: NB, right: NB };

const FONT = { ascii: "Times New Roman", eastAsia: "Times New Roman",
  hAnsi: "Times New Roman" };
const HFONT = { ascii: "Arial", eastAsia: "Arial", hAnsi: "Arial" };

// ━━ оценка ширины текста (кириллица/латиница) в twips ━━
function textWidth(text, pt) {
  let w = 0;
  for (const ch of text) {
    const c = ch.codePointAt(0);
    if (c >= 0x400 && c <= 0x4FF) w += pt * 12;       // кириллица
    else if (ch === " ") w += pt * 6;
    else if (c < 128) w += pt * 11;                    // латиница
    else w += pt * 14;
  }
  return w;
}

function splitTitleLines(title, maxWidthTwips, pt) {
  const words = title.split(/\s+/);
  const lines = [];
  let cur = "";
  for (const w of words) {
    const cand = cur ? cur + " " + w : w;
    if (textWidth(cand, pt) <= maxWidthTwips || !cur) cur = cand;
    else { lines.push(cur); cur = w; }
  }
  if (cur) lines.push(cur);
  if (lines.length > 1 && lines[lines.length - 1].split(/\s+/).length === 1
      && lines[lines.length - 1].length <= 8) {
    const last = lines.pop();
    lines[lines.length - 1] += " " + last;
  }
  return lines;
}

function calcTitleLayout(title, maxWidthTwips, preferredPt = 34, minPt = 22) {
  let pt = preferredPt, lines;
  while (pt >= minPt) {
    lines = splitTitleLines(title, maxWidthTwips, pt);
    if (lines.length <= 3) break;
    pt -= 2;
  }
  if (!lines || lines.length > 3) { pt = minPt; lines = splitTitleLines(title, maxWidthTwips, pt); }
  return { titlePt: pt, titleLines: lines };
}

// ━━ обложка — рецепт R1 (Pure Paragraph, тёмный фон) ━━
function buildCoverR1(cfg) {
  const padL = 1100, padR = 900;
  const availableWidth = 11906 - padL - padR - 300;
  const { titlePt, titleLines } = calcTitleLayout(cfg.title, availableWidth, 34, 22);
  const titleSize = titlePt * 2;
  const metaLines = cfg.metaLines || [];
  const SAFETY = 1200;
  const usable = 16838 - SAFETY;
  const titleH = titleLines.length * (titlePt * 23 + 200);
  const subH = cfg.subtitle ? (13 * 23 + 500) : 0;
  const labelH = cfg.englishLabel ? (10 * 23 + 500) : 0;
  const metaH = metaLines.length * (10.5 * 23 + 110);
  const fixedH = 400;
  const contentH = titleH + subH + labelH + metaH + fixedH + 3 * 300;
  const remaining = Math.max(usable - contentH, 400);
  const FOOTER_MIN = 800;
  const rawTop = Math.floor(remaining * 0.45);
  const rawBottom = Math.floor(remaining * 0.45);
  const bottomSpacing = Math.max(rawBottom, FOOTER_MIN);
  const topSpacing = Math.max(rawTop - Math.max(0, FOOTER_MIN - rawBottom), 400);
  const accentLeft = { style: BorderStyle.SINGLE, size: 8, color: P.accent, space: 12 };
  const children = [];
  children.push(new Paragraph({ spacing: { before: topSpacing } }));
  children.push(new Paragraph({
    indent: { left: padL, right: padR }, spacing: { after: 500 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: P.accent, space: 8 } },
    children: [new TextRun({ text: cfg.englishLabel, size: 19, color: P.accent,
      font: HFONT, characterSpacing: 40 })],
  }));
  for (let i = 0; i < titleLines.length; i++) {
    children.push(new Paragraph({
      indent: { left: padL, right: 400 },
      spacing: { after: i < titleLines.length - 1 ? 100 : 300,
                 line: Math.ceil(titlePt * 23), lineRule: "atLeast" },
      children: [new TextRun({ text: titleLines[i], size: titleSize, bold: true,
        color: P.titleColor, font: HFONT })],
    }));
  }
  if (cfg.subtitle) {
    children.push(new Paragraph({
      indent: { left: padL, right: 600 }, spacing: { after: 700, line: 340, lineRule: "atLeast" },
      children: [new TextRun({ text: cfg.subtitle, size: 25, color: P.subtitleColor, font: HFONT })],
    }));
  }
  for (const line of metaLines) {
    children.push(new Paragraph({
      indent: { left: padL + 200 }, spacing: { after: 80 },
      border: { left: accentLeft },
      children: [new TextRun({ text: line, size: 21, color: P.metaColor, font: HFONT })],
    }));
  }
  children.push(new Paragraph({ spacing: { before: bottomSpacing } }));
  children.push(new Paragraph({
    indent: { left: padL, right: padR },
    border: { top: { style: BorderStyle.SINGLE, size: 2, color: P.accent, space: 8 } },
    spacing: { before: 200 },
    children: [
      new TextRun({ text: cfg.footerLeft || "", size: 16, color: P.footerColor, font: HFONT }),
      new TextRun({ text: "                                        " }),
      new TextRun({ text: cfg.footerRight || "", size: 16, color: P.footerColor, font: HFONT }),
    ],
  }));
  return [new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    layout: TableLayoutType.FIXED,
    borders: allNoBorders,
    rows: [new TableRow({
      height: { value: 16838, rule: "exact" },
      children: [new TableCell({
        shading: { type: ShadingType.CLEAR, fill: P.bg },
        borders: noBorders, verticalAlign: "top",
        children,
      })],
    })],
  })];
}

// ━━ PNG-размеры (IHDR) ━━
function pngSize(file) {
  const b = fs.readFileSync(file);
  return { w: b.readUInt32BE(16), h: b.readUInt32BE(20) };
}

function figureParas(fig, bodyW) {
  const p = path.join(ROOT, fig.path.replace(/\{lang\}/g, lang));
  if (!fs.existsSync(p)) return [];
  const { w, h } = pngSize(p);
  const displayW = Math.min(bodyW, 500);
  const displayH = Math.round(displayW * h / w);
  return [
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 120 },
      children: [new ImageRun({ data: fs.readFileSync(p),
        transformation: { width: displayW, height: displayH }, type: "png" })] }),
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 160 },
      children: [new TextRun({ text: fig.caption, size: 17, italics: true,
        color: P.muted, font: FONT })] }),
  ];
}

function tableElements(tbl) {
  const out = [];
  out.push(new Paragraph({ keepNext: true, spacing: { before: 140, after: 60 },
    children: [new TextRun({ text: tbl.caption, bold: true, size: 19,
      color: P.header, font: FONT })] }));
  const n = tbl.header.length;
  const ratios = tbl.ratios && tbl.ratios.length === n
    ? tbl.ratios : Array(n).fill(1 / n);
  const headerRow = new TableRow({
    tableHeader: true, cantSplit: true,
    children: tbl.header.map((h, i) => new TableCell({
      width: { size: Math.round(ratios[i] * 100), type: WidthType.PERCENTAGE },
      shading: { type: ShadingType.CLEAR, fill: P.header },
      margins: { top: 60, bottom: 60, left: 110, right: 110 },
      children: [new Paragraph({ alignment: AlignmentType.CENTER,
        children: [new TextRun({ text: String(h), bold: true, size: 17,
          color: "FFFFFF", font: FONT })] })],
    })),
  });
  const dataRows = tbl.rows.map((r, ri) => new TableRow({
    cantSplit: true,
    children: r.map((c, i) => new TableCell({
      width: { size: Math.round(ratios[i] * 100), type: WidthType.PERCENTAGE },
      shading: { type: ShadingType.CLEAR, fill: ri % 2 ? P.surface : "FFFFFF" },
      margins: { top: 50, bottom: 50, left: 110, right: 110 },
      children: [new Paragraph({ spacing: { line: 240 },
        children: [new TextRun({ text: String(c), size: 17, color: P.ink, font: FONT })] })],
    })),
  }));
  out.push(new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    borders: {
      top: { style: BorderStyle.SINGLE, size: 4, color: P.header },
      bottom: { style: BorderStyle.SINGLE, size: 4, color: P.header },
      left: NB, right: NB,
      insideHorizontal: { style: BorderStyle.SINGLE, size: 1, color: P.grid },
      insideVertical: NB,
    },
    rows: [headerRow, ...dataRows],
  }));
  out.push(new Paragraph({ spacing: { after: 120 }, children: [] }));
  return out;
}

const L = lang === "ru"
  ? { toc: "Содержание", hint: "Примечание: оглавление построено на полях Word. После редактирования щёлкните по нему правой кнопкой и выберите «Обновить поле».",
      proof: "Доказательство.", vol: "том" }
  : { toc: "Contents", hint: "Note: this table of contents is built on Word field codes. After editing, right-click it and choose \"Update Field\".",
      proof: "Proof.", vol: "volume" };

// ━━ тело ━━
function buildBody() {
  const els = [];
  const m = doc.meta;
  els.push(new Paragraph({ spacing: { before: 120, after: 60 },
    children: [new TextRun({ text: m.title, bold: true, size: 40,
      color: P.header, font: HFONT })] }));
  els.push(new Paragraph({ spacing: { after: 200 },
    children: [new TextRun({ text: `${m.author} · ${m.affil} · ${m.series} · ${m.volume}`, size: 19, color: P.muted, font: FONT })] }));
  for (const sec of doc.sections) {
    els.push(new Paragraph({ heading: HeadingLevel.HEADING_1,
      spacing: { before: 320, after: 140 },
      children: [new TextRun({ text: sec.h1, bold: true, size: 30,
        color: P.header, font: HFONT })] }));
    const thmKeys = ["theorem", "theorem2", "theorem3", "theorem4"];
    if (sec.theorem) {
      const t = sec.theorem;
      els.push(new Paragraph({ keepNext: true, spacing: { before: 120, after: 40 },
        border: { left: { style: BorderStyle.SINGLE, size: 10, color: P.copper, space: 10 } },
        indent: { left: 200 },
        children: [new TextRun({ text: t.label, bold: true, size: 21,
          color: P.copper, font: FONT })] }));
      els.push(new Paragraph({ indent: { left: 200 }, spacing: { after: 40 },
        alignment: AlignmentType.JUSTIFIED,
        children: [new TextRun({ text: t.text, size: 20, font: FONT, color: P.ink })] }));
      els.push(new Paragraph({ indent: { left: 200 }, spacing: { after: 140 },
        alignment: AlignmentType.JUSTIFIED,
        children: [new TextRun({ text: `${L.proof} ${t.proof}`, italics: true, size: 19, font: FONT, color: P.ink })] }));
    }
    for (const p of (sec.paras || [])) {
      els.push(new Paragraph({ alignment: AlignmentType.JUSTIFIED,
        spacing: { line: 312, after: 120 },
        children: [new TextRun({ text: p, size: 21, font: FONT, color: P.ink })] }));
    }
    for (const k of thmKeys.slice(1)) {
      const t = sec[k];
      if (!t) continue;
      els.push(new Paragraph({ keepNext: true, spacing: { before: 120, after: 40 },
        border: { left: { style: BorderStyle.SINGLE, size: 10, color: P.copper, space: 10 } },
        indent: { left: 200 },
        children: [new TextRun({ text: t.label, bold: true, size: 21, color: P.copper, font: FONT })] }));
      els.push(new Paragraph({ indent: { left: 200 }, spacing: { after: 40 },
        alignment: AlignmentType.JUSTIFIED,
        children: [new TextRun({ text: t.text, size: 20, font: FONT, color: P.ink })] }));
      els.push(new Paragraph({ indent: { left: 200 }, spacing: { after: 140 },
        alignment: AlignmentType.JUSTIFIED,
        children: [new TextRun({ text: `${L.proof} ${t.proof}`, italics: true, size: 19, font: FONT, color: P.ink })] }));
    }
    if (sec.table) els.push(...tableElements(sec.table));
    for (const k of ["figure", "figure2", "figure3"]) {
      if (sec[k]) els.push(...figureParas(sec[k], 460));
    }
    for (const p of (sec.conclusion || [])) {
      els.push(new Paragraph({ alignment: AlignmentType.JUSTIFIED,
        spacing: { line: 312, after: 120 },
        children: [new TextRun({ text: p, size: 21, font: FONT, color: P.ink })] }));
    }
  }
  return els;
}

function pageFooter(fmt) {
  return new Footer({ children: [new Paragraph({
    alignment: AlignmentType.CENTER,
    children: [new TextRun({ children: [PageNumber.CURRENT], size: 18,
      color: P.muted, font: FONT })],
  })] });
}

const pgSize = { width: 11906, height: 16838 };
const pgMargin = { top: 1440, bottom: 1440, left: 1701, right: 1417 };
const m = doc.meta;
const coverCfg = {
  title: m.title, subtitle: m.subtitle,
  englishLabel: (lang === "ru" ? "HILBERT POLYA BRIDGE · СЕРИЯ МОНОГРАФИЙ"
                                : "HILBERT POLYA BRIDGE · MONOGRAPH SERIES"),
  metaLines: [m.author, m.affil, `${m.series} · ${lang === "ru" ? "том" : "volume"} ${m.volume}`],
  footerLeft: `v${m.version}`, footerRight: m.date,
};

const d = new Document({
  creator: m.author, title: m.title, description: m.subtitle,
  styles: { default: { document: {
    run: { font: FONT, size: 21, color: P.ink },
    paragraph: { spacing: { line: 312 } },
  },
  heading1: { run: { font: HFONT, size: 30, bold: true, color: P.header },
    paragraph: { spacing: { before: 320, after: 140 }, outlineLevel: 0 } },
  }},
  sections: [
    { properties: { page: { size: pgSize, margin: { top: 0, bottom: 0, left: 0, right: 0 } } },
      children: buildCoverR1(coverCfg) },
    { properties: { type: SectionType.NEXT_PAGE,
        page: { size: pgSize, margin: pgMargin,
          pageNumbers: { start: 1, formatType: NumberFormat.UPPER_ROMAN } } },
      footers: { default: pageFooter() },
      children: [
        new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 480, after: 360 },
          children: [new TextRun({ text: L.toc, bold: true, size: 32, font: HFONT, color: P.header })] }),
        new TableOfContents("TOC", { hyperlink: true, headingStyleRange: "1-1" }),
        new Paragraph({ spacing: { before: 200 },
          children: [new TextRun({ text: L.hint, italics: true, size: 17, color: "888888", font: FONT })] }),
        new Paragraph({ children: [new PageBreak()] }),
      ] },
    { properties: { type: SectionType.NEXT_PAGE,
        page: { size: pgSize, margin: pgMargin,
          pageNumbers: { start: 1, formatType: NumberFormat.DECIMAL } } },
      footers: { default: pageFooter() },
      children: buildBody() },
  ],
});

Packer.toBuffer(d).then((buf) => {
  fs.writeFileSync(outPath, buf);
  console.log(`DOCX OK: ${outPath}`);
});
