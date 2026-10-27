// c17_docx.js — DOCX-версия отчёта «C17: слепая фаза B протокола N7»
// (docx-js, рецепт R1; архитектура audit_docx.js/amap_docx.js).
// Отличия от аудита: парсер <b>/<sub>/<super> → TextRun{bold/subScript/
// superScript}, блок formula, абсолютные пути фигур.
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  ImageRun, Header, Footer, AlignmentType, HeadingLevel, PageNumber,
  BorderStyle, WidthType, ShadingType, TableLayoutType, SectionType,
  NumberFormat, TableOfContents, VerticalAlign,
} = require("docx");

const HERE = __dirname;
const C = JSON.parse(fs.readFileSync(path.join(HERE, "content_c17.json"), "utf-8"));

// ── Палитра MIN-1 (Warm Gold — семейство аудита) ──
const P = {
  bg: "F3F1ED", titleColor: "000000", subtitleColor: "606060",
  metaColor: "707070", footerColor: "A0A0A0", accent: "D6C096",
  tblHeaderBg: "D6C096", tblHeaderText: "1A1A1A",
  tblInnerLine: "DDD8CC", tblSurface: "F5F3ED",
  body: "262522", primary: "000000", muted: "817F77",
};
const BODY_FONT = { ascii: "Times New Roman", hAnsi: "Times New Roman", eastAsia: "SimSun" };
const HEAD_FONT = { ascii: "Arial", hAnsi: "Arial", eastAsia: "SimHei" };

function pngSize(file) {
  const b = fs.readFileSync(file);
  return { w: b.readUInt32BE(16), h: b.readUInt32BE(20) };
}
const noBorders = {
  top: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
  bottom: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
  left: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
  right: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
};
const allNoBorders = { ...noBorders,
  insideHorizontal: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
  insideVertical: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" } };

// ── Парсер <b>/<sub>/<super> → массив TextRun ──
function runs(text, base) {
  const out = [];
  const re = /<(b|sub|super)>([\s\S]*?)<\/\1>/g;
  let last = 0, m;
  const s = String(text);
  while ((m = re.exec(s)) !== null) {
    if (m.index > last) out.push(new TextRun({ ...base, text: s.slice(last, m.index) }));
    if (m[1] === "b") out.push(new TextRun({ ...base, text: m[2], bold: true }));
    else if (m[1] === "sub") out.push(new TextRun({ ...base, text: m[2], subScript: true }));
    else out.push(new TextRun({ ...base, text: m[2], superScript: true }));
    last = m.index + m[0].length;
  }
  if (last < s.length) out.push(new TextRun({ ...base, text: s.slice(last) }));
  if (out.length === 0) out.push(new TextRun({ ...base, text: s }));
  return out;
}

// ── Хелперы обложки (design-system) ──
function splitTitleLines(title, cpl) {
  if (title.length <= cpl) return [title];
  const breakAfter = new Set([..."\u2014\u2013-_/ \t", ...":,·"]);
  const lines = []; let rem = title;
  while (rem.length > cpl) {
    let at = -1;
    for (let i = cpl; i >= Math.floor(cpl * 0.6); i--)
      if (i < rem.length && breakAfter.has(rem[i - 1])) { at = i; break; }
    if (at === -1) at = cpl;
    lines.push(rem.slice(0, at).trim()); rem = rem.slice(at).trim();
  }
  if (rem) lines.push(rem);
  if (lines.length >= 2 && lines[lines.length - 1].length <= 2) {
    const last = lines.pop(); lines[lines.length - 1] += " " + last;
  }
  return lines;
}
function calcTitleLayout(title, maxW, prefPt = 40, minPt = 24) {
  const cplOf = (pt) => Math.floor(maxW / (pt * 20));
  let pt = prefPt, lines;
  while (pt >= minPt) {
    const cpl = cplOf(pt);
    if (cpl < 2) { pt -= 2; continue; }
    lines = splitTitleLines(title, cpl);
    if (lines.length <= 3) break;
    pt -= 2;
  }
  if (!lines || lines.length > 3) { lines = splitTitleLines(title, cplOf(minPt)); pt = minPt; }
  return { titlePt: pt, titleLines: lines };
}
function calcCoverSpacing(q) {
  const { titleLineCount = 1, titlePt = 36, hasSubtitle = false,
    hasEnglishLabel = false, metaLineCount = 0, fixedHeight = 800,
    pageHeight = 16838 } = q;
  const SAFETY = 1200;
  const usable = pageHeight - SAFETY;
  const contentH = titleLineCount * (titlePt * 23 + 200) +
    (hasSubtitle ? (12 * 23 + 600) : 0) + (hasEnglishLabel ? (9 * 23 + 600) : 0) +
    metaLineCount * (10 * 23 + 100) + fixedHeight + 3 * 300;
  const rem = Math.max(usable - contentH, 400);
  const FOOTER_MIN = 800;
  const rawTop = Math.floor(rem * 0.45), rawBottom = Math.floor(rem * 0.45);
  const bottomSpacing = Math.max(rawBottom, FOOTER_MIN);
  const topSpacing = Math.max(rawTop - Math.max(0, FOOTER_MIN - rawBottom), 400);
  return { topSpacing, bottomSpacing };
}

// ── Рецепт R1 (Pure Paragraph Left) ──
function buildCoverR1(config) {
  const padL = 1200, padR = 800;
  const availableWidth = 11906 - padL - padR - 300;
  const { titlePt, titleLines } = calcTitleLayout(config.title, availableWidth, 40, 24);
  const titleSize = titlePt * 2;
  const spacing = calcCoverSpacing({
    titleLineCount: titleLines.length, titlePt,
    hasSubtitle: !!config.subtitle, hasEnglishLabel: !!config.englishLabel,
    metaLineCount: (config.metaLines || []).length, fixedHeight: 400,
  });
  const accentLeft = { style: BorderStyle.SINGLE, size: 8, color: P.accent, space: 12 };
  const children = [];
  children.push(new Paragraph({ spacing: { before: spacing.topSpacing } }));
  if (config.englishLabel) {
    children.push(new Paragraph({
      indent: { left: padL, right: padR }, spacing: { after: 500 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: P.accent, space: 8 } },
      children: [new TextRun({ text: config.englishLabel.split("").join("  "),
        size: 18, color: "8A7B55", font: HEAD_FONT, characterSpacing: 40 })],
    }));
  }
  for (let i = 0; i < titleLines.length; i++) {
    children.push(new Paragraph({
      indent: { left: padL },
      spacing: { after: i < titleLines.length - 1 ? 100 : 300,
                 line: Math.ceil(titlePt * 23), lineRule: "atLeast" },
      children: [new TextRun({ text: titleLines[i], size: titleSize, bold: true,
        color: P.titleColor, font: HEAD_FONT })],
    }));
  }
  if (config.subtitle) {
    children.push(new Paragraph({
      indent: { left: padL, right: padR }, spacing: { after: 800 },
      children: runs(config.subtitle, { size: 24, color: P.subtitleColor, font: BODY_FONT }),
    }));
  }
  for (const line of (config.metaLines || [])) {
    children.push(new Paragraph({
      indent: { left: padL + 200 }, spacing: { after: 80 },
      border: { left: accentLeft },
      children: [new TextRun({ text: line, size: 24, color: P.metaColor, font: BODY_FONT })],
    }));
  }
  children.push(new Paragraph({ spacing: { before: spacing.bottomSpacing } }));
  children.push(new Paragraph({
    indent: { left: padL, right: padR },
    border: { top: { style: BorderStyle.SINGLE, size: 2, color: P.accent, space: 8 } },
    spacing: { before: 200 },
    children: [
      new TextRun({ text: config.footerLeft || "", size: 16, color: P.footerColor, font: HEAD_FONT }),
      new TextRun({ text: "                                        " }),
      new TextRun({ text: config.footerRight || "", size: 16, color: P.footerColor, font: HEAD_FONT }),
    ],
  }));
  return [new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    layout: TableLayoutType.FIXED,
    borders: allNoBorders,
    rows: [new TableRow({
      height: { value: 16838, rule: "exact" },
      children: [new TableCell({
        shading: { type: ShadingType.CLEAR, fill: P.bg }, borders: noBorders,
        children,
      })],
    })],
  })];
}

// ── Компоненты тела ──
function h1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 400, after: 160, line: 312 },
    children: [new TextRun({ text, bold: true, size: 32, color: "58513B", font: HEAD_FONT })],
  });
}
function h2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 280, after: 120, line: 312 },
    children: [new TextRun({ text, bold: true, size: 26, color: P.body, font: HEAD_FONT })],
  });
}
function body(text) {
  return new Paragraph({
    alignment: AlignmentType.JUSTIFIED,
    spacing: { line: 312, after: 120 },
    children: runs(text, { size: 22, color: P.body, font: BODY_FONT }),
  });
}
function bullet(text) {
  return new Paragraph({
    alignment: AlignmentType.LEFT,
    bullet: { level: 0 },
    spacing: { line: 312, after: 100 },
    children: runs(text, { size: 22, color: P.body, font: BODY_FONT }),
  });
}
function formula(text) {
  return new Table({
    width: { size: 8200, type: WidthType.DXA },
    alignment: AlignmentType.CENTER,
    borders: allNoBorders,
    rows: [new TableRow({
      children: [new TableCell({
        shading: { type: ShadingType.CLEAR, fill: P.tblSurface },
        margins: { top: 120, bottom: 120, left: 200, right: 200 },
        children: [new Paragraph({
          alignment: AlignmentType.CENTER, spacing: { line: 312 },
          children: runs(text, { size: 24, color: P.body, font: BODY_FONT }),
        })],
      })],
    })],
  });
}
function quote(text) {
  return new Paragraph({
    alignment: AlignmentType.LEFT,
    indent: { left: 480, right: 240 },
    spacing: { line: 312, before: 120, after: 160 },
    border: { left: { style: BorderStyle.SINGLE, size: 12, color: "907422", space: 12 } },
    shading: { type: ShadingType.CLEAR, fill: P.tblSurface },
    children: runs(text, { italics: true, size: 22, color: P.body, font: BODY_FONT }),
  });
}
function cellPara(text, opts) {
  const o = opts || {};
  return new Paragraph({
    alignment: o.center ? AlignmentType.CENTER : AlignmentType.LEFT,
    spacing: { line: 276 },
    children: runs(text, { size: 19, bold: !!o.bold,
      color: o.color || P.body, font: BODY_FONT }),
  });
}
function tbl(spec) {
  const n = spec.header.length;
  const widths = (spec.ratios || spec.header.map(() => 1 / n))
    .map(r => Math.round(r * 9350));
  const header = new TableRow({
    tableHeader: true, cantSplit: true,
    children: spec.header.map((htxt, i) => new TableCell({
      width: { size: widths[i], type: WidthType.DXA },
      shading: { type: ShadingType.CLEAR, fill: P.tblHeaderBg },
      margins: { top: 80, bottom: 80, left: 120, right: 120 },
      verticalAlign: VerticalAlign.CENTER,
      children: [cellPara(htxt, { bold: true, color: P.tblHeaderText, center: true })],
    })),
  });
  const rows = spec.rows.map((r, ri) => new TableRow({
    cantSplit: true,
    children: r.map((cv, i) => new TableCell({
      width: { size: widths[i], type: WidthType.DXA },
      shading: { type: ShadingType.CLEAR, fill: ri % 2 ? P.tblSurface : "FFFFFF" },
      margins: { top: 60, bottom: 60, left: 120, right: 120 },
      children: [cellPara(cv)],
    })),
  }));
  return [
    new Paragraph({ keepNext: true, spacing: { before: 200, after: 60 },
      alignment: AlignmentType.CENTER,
      children: [new TextRun({ text: spec.caption, italics: true, size: 17,
        color: P.muted, font: BODY_FONT })] }),
    new Table({
      width: { size: 9350, type: WidthType.DXA },
      layout: TableLayoutType.FIXED,
      borders: { ...allNoBorders,
        top: { style: BorderStyle.SINGLE, size: 4, color: P.accent },
        bottom: { style: BorderStyle.SINGLE, size: 4, color: P.accent },
        insideHorizontal: { style: BorderStyle.SINGLE, size: 2, color: P.tblInnerLine } },
      rows: [header, ...rows],
    }),
    new Paragraph({ spacing: { after: 160 } }),
  ];
}
function fig(spec) {
  const file = path.isAbsolute(spec.path) ? spec.path : path.join(HERE, spec.path);
  if (!fs.existsSync(file)) return [body("[фигура недоступна: " + spec.path + "]")];
  const { w, h } = pngSize(file);
  const maxW = 9350, maxH = (spec.max_h || 280) * 15 * 1.33;
  const scale = Math.min(maxW / w, maxH / h, 1.0);
  return [
    new Paragraph({
      alignment: AlignmentType.CENTER, keepNext: true, spacing: { before: 160 },
      children: [new ImageRun({ type: "png", data: fs.readFileSync(file),
        transformation: { width: Math.round(w * scale / 20),
                          height: Math.round(h * scale / 20) } })],
    }),
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 200 },
      children: [new TextRun({ text: spec.caption, italics: true, size: 17,
        color: P.muted, font: BODY_FONT })] }),
  ];
}
function callout(spec) {
  return [new Table({
    width: { size: 6200, type: WidthType.DXA },
    alignment: AlignmentType.CENTER,
    borders: { ...allNoBorders,
      top: { style: BorderStyle.SINGLE, size: 8, color: "907422" },
      bottom: { style: BorderStyle.SINGLE, size: 8, color: "907422" },
      left: { style: BorderStyle.SINGLE, size: 8, color: "907422" },
      right: { style: BorderStyle.SINGLE, size: 8, color: "907422" } },
    rows: [new TableRow({
      children: [new TableCell({
        shading: { type: ShadingType.CLEAR, fill: P.tblSurface },
        margins: { top: 160, bottom: 160, left: 200, right: 200 },
        children: [
          new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 },
            children: runs(spec.big, { bold: true, size: 40,
              color: "907422", font: HEAD_FONT }) }),
          new Paragraph({ alignment: AlignmentType.CENTER,
            children: runs(spec.label, { size: 18,
              color: P.muted, font: BODY_FONT }) }),
        ],
      })],
    })],
  }), new Paragraph({ spacing: { after: 200 } })];
}

// ── Тело ──
const bodyChildren = [];
for (const b of C.blocks) {
  if (b.t === "h1") bodyChildren.push(h1(b.p));
  else if (b.t === "h2") bodyChildren.push(h2(b.p));
  else if (b.t === "p") bodyChildren.push(body(b.p));
  else if (b.t === "bullets") b.p.forEach(x => bodyChildren.push(bullet(x)));
  else if (b.t === "table") bodyChildren.push(...tbl(b.p));
  else if (b.t === "fig") bodyChildren.push(...fig(b.p));
  else if (b.t === "callout") bodyChildren.push(...callout(b.p));
  else if (b.t === "quote") bodyChildren.push(quote(b.p));
  else if (b.t === "formula") bodyChildren.push(formula(b.p));
}
bodyChildren.push(h1("Источники"));
for (const ref of C.biblio) {
  bodyChildren.push(new Paragraph({
    alignment: AlignmentType.LEFT,
    indent: { left: 400, hanging: 400 },
    spacing: { line: 312, after: 80 },
    children: [new TextRun({ text: ref, size: 20, color: P.body, font: BODY_FONT })],
  }));
}

// ── Секции ──
const pgMargin = { top: 1440, bottom: 1440, left: 1701, right: 1417 };
function pageNumFooter() {
  return new Footer({ children: [new Paragraph({
    alignment: AlignmentType.CENTER,
    children: [new TextRun({ children: [PageNumber.CURRENT], size: 18,
      color: P.muted, font: BODY_FONT })],
  })] });
}
function docHeader() {
  return new Header({ children: [new Paragraph({
    alignment: AlignmentType.LEFT,
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: P.accent, space: 4 } },
    children: [new TextRun({ text: "Hilbert Polya Bridge · алгебраическая карта кодировки",
      size: 16, color: P.muted, font: BODY_FONT })],
  })] });
}

const doc = new Document({
  creator: "Z.ai",
  title: C.title,
  subject: C.subtitle,
  styles: { default: { document: {
    run: { font: BODY_FONT, size: 22, color: P.body },
    paragraph: { spacing: { line: 312 } },
  } } },
  features: { updateFields: true },
  sections: [
    { properties: { page: { size: { width: 11906, height: 16838 },
        margin: { top: 0, bottom: 0, left: 0, right: 0 } } },
      children: buildCoverR1({
        title: "Алгебраическая карта якобиевой кодировки",
        subtitle: C.subtitle,
        englishLabel: "RESEARCH NOTE",
        metaLines: [
          "Пакет: Hilbert Polya Bridge v2.0.0+amap",
          "Дата отчёта: 13 октября 2026",
          "Статус: замыкание доказано; протокол N7 уточнён",
        ],
        footerLeft: "HILBERT POLYA BRIDGE",
        footerRight: "13.10.2026",
      }) },
    { properties: { type: SectionType.NEXT_PAGE,
        page: { size: { width: 11906, height: 16838 }, margin: pgMargin,
          pageNumbers: { start: 1, formatType: NumberFormat.UPPER_ROMAN } } },
      headers: { default: docHeader() },
      footers: { default: pageNumFooter() },
      children: [
        new Paragraph({ alignment: AlignmentType.CENTER,
          spacing: { before: 480, after: 360 },
          children: [new TextRun({ text: "Содержание", bold: true, size: 32,
            color: "58513B", font: HEAD_FONT })] }),
        new TableOfContents("Table of Contents", { hyperlink: true,
          headingStyleRange: "1-2" }),
        new Paragraph({ spacing: { before: 200 },
          children: [new TextRun({
            text: "Примечание: оглавление построено на кодах полей Word. После редактирования щёлкните по нему правой кнопкой и выберите «Обновить поле», чтобы обновить номера страниц.",
            italics: true, size: 18, color: "888888", font: BODY_FONT })] }),
      ] },
    { properties: { type: SectionType.NEXT_PAGE,
        page: { size: { width: 11906, height: 16838 }, margin: pgMargin,
          pageNumbers: { start: 1, formatType: NumberFormat.DECIMAL } } },
      headers: { default: docHeader() },
      footers: { default: pageNumFooter() },
      children: bodyChildren },
  ],
});

Packer.toBuffer(doc).then(buf => {
  const out = process.argv[2] || path.join(HERE, "..", "HPB_C17_blind_phaseB_2026-10-13_ru.docx");
  fs.writeFileSync(out, buf);
  console.log("DOCX OK:", out, Math.round(buf.length / 1024) + " KB");
});
