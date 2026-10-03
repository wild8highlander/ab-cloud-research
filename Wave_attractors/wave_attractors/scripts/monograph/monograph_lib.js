/**
 * monograph_lib.js — shared builders for the W1 monographs (RU/EN).
 *
 * Implements the docx-skill rules:
 *  - R5 Clean White academic cover (16838 exact wrapper, allNoBorders,
 *    width-aware calcTitleLayout, adaptive meta table, no margins.top)
 *  - 3-section architecture: cover (no numbers) / front matter (Roman) /
 *    body (Arabic from 1)
 *  - academic Profile A: Times New Roman, pure black, justified,
 *    first-line indent, 1.5 line spacing, HeadingLevel for TOC
 *  - three-line tables (tableHeader + cantSplit + keepNext caption above)
 *  - figures: block ImageRun (aspect preserved) + caption below
 *  - formulas: centered + right-aligned number (tab stops)
 */

const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  ImageRun, PageBreak, Header, Footer, PageNumber, NumberFormat,
  AlignmentType, HeadingLevel, WidthType, BorderStyle, ShadingType,
  TabStopType, TableOfContents, SectionType, TableLayoutType,
} = require("docx");

// ---------------------------------------------------------------- constants
const NB = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const noBorders = { top: NB, bottom: NB, left: NB, right: NB };
const allNoBorders = {
  top: NB, bottom: NB, left: NB, right: NB,
  insideHorizontal: NB, insideVertical: NB,
};
const FONT = "Times New Roman";
const CONTENT_W_TW = 11906 - 1701 - 1417;      // 8788 twips
const CONTENT_W_PX = Math.floor(CONTENT_W_TW / 15); // ~585 px @96dpi

// ------------------------------------------------------------ png geometry
function pngSize(path) {
  const b = fs.readFileSync(path);
  return { w: b.readUInt32BE(16), h: b.readUInt32BE(20) };
}

// ------------------------------------------------------- inline markup runs
/**
 * Mini markup: *italic*, **bold**, ^{sup}, _{sub}.
 * Parses sequentially; returns TextRun[] (document default font applies).
 */
function runs(text0, base = {}) {
  const text = String(text0).replace(/ — /g, "\u00A0— ");
  const out = [];
  let i = 0;
  let plain = "";
  const flush = () => {
    if (plain) { out.push(new TextRun({ text: plain, ...base })); plain = ""; }
  };
  while (i < text.length) {
    if (text.startsWith("**", i)) {
      const j = text.indexOf("**", i + 2);
      if (j > -1) {
        flush();
        out.push(new TextRun({ text: text.slice(i + 2, j), bold: true, ...base }));
        i = j + 2; continue;
      }
    }
    const ch = text[i];
    if (ch === "*") {
      const j = text.indexOf("*", i + 1);
      if (j > -1) {
        flush();
        out.push(new TextRun({ text: text.slice(i + 1, j), italics: true, ...base }));
        i = j + 1; continue;
      }
    }
    if (ch === "^" && text[i + 1] === "{") {
      const j = text.indexOf("}", i + 2);
      if (j > -1) {
        flush();
        out.push(new TextRun({ text: text.slice(i + 2, j), superScript: true, ...base }));
        i = j + 1; continue;
      }
    }
    if (ch === "_" && text[i + 1] === "{") {
      const j = text.indexOf("}", i + 2);
      if (j > -1) {
        flush();
        out.push(new TextRun({ text: text.slice(i + 2, j), subScript: true, ...base }));
        i = j + 1; continue;
      }
    }
    plain += ch; i += 1;
  }
  flush();
  return out;
}

// ---------------------------------------------------------------- headings
function h1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    alignment: AlignmentType.CENTER,
    spacing: { before: 480, after: 360, line: 360 },
    children: [new TextRun({ text, bold: true, size: 32, color: "000000", font: FONT })],
  });
}
function h2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 360, after: 240, line: 360 },
    children: [new TextRun({ text, bold: true, size: 30, color: "000000", font: FONT })],
  });
}
function h3(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_3,
    spacing: { before: 240, after: 120, line: 360 },
    children: [new TextRun({ text, bold: true, size: 28, color: "000000", font: FONT })],
  });
}

// ------------------------------------------------------------------ body
function p(text, opts = {}) {
  return new Paragraph({
    alignment: AlignmentType.JUSTIFIED,
    indent: { firstLine: 567 },
    spacing: { line: 360, after: opts.after !== undefined ? opts.after : 0 },
    children: runs(text),
  });
}
/** paragraph without first-line indent (continuations, list-like lines) */
function pFlat(text, opts = {}) {
  return new Paragraph({
    alignment: AlignmentType.JUSTIFIED,
    spacing: { line: 360, after: opts.after !== undefined ? opts.after : 0 },
    indent: opts.left ? { left: opts.left } : undefined,
    children: runs(text),
  });
}
/** hanging-indent list line (monograph style) */
function pList(text) {
  return new Paragraph({
    alignment: AlignmentType.JUSTIFIED,
    indent: { left: 851, hanging: 284 },
    spacing: { line: 360 },
    children: runs(text),
  });
}

// ---------------------------------------------------------------- figures
function figure(path, caption, widthPx) {
  const { w, h } = pngSize(path);
  const displayW = Math.min(widthPx || 560, CONTENT_W_PX);
  const displayH = Math.round(displayW * h / w);
  return [
    new Paragraph({
      alignment: AlignmentType.CENTER,
      keepNext: true,
      spacing: { before: 200 },
      children: [new ImageRun({
        data: fs.readFileSync(path),
        transformation: { width: displayW, height: displayH },
        type: "png",
      })],
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 60, after: 240, line: 280 },
      children: runs(caption, { size: 21 }),
    }),
  ];
}

// ----------------------------------------------------------------- tables
function tableCaption(text) {
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    keepNext: true,
    spacing: { before: 240, after: 80, line: 280 },
    children: runs(text, { size: 21 }),
  });
}
/** three-line academic table; cells accept the mini markup */
function threeLineTable(headers, rowsData, colPct) {
  const cell = (text, bold, idx) => new TableCell({
    width: { size: colPct[idx], type: WidthType.PERCENTAGE },
    borders: bold
      ? { bottom: { style: BorderStyle.SINGLE, size: 2, color: "000000" }, top: NB, left: NB, right: NB }
      : noBorders,
    margins: { top: 60, bottom: 60, left: 100, right: 100 },
    children: [new Paragraph({
      alignment: idx === 0 ? AlignmentType.LEFT : AlignmentType.CENTER,
      spacing: { line: 280 },
      children: runs(text, { size: 21, bold }),
    })],
  });
  return new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    layout: TableLayoutType.FIXED,
    borders: {
      top: { style: BorderStyle.SINGLE, size: 4, color: "000000" },
      bottom: { style: BorderStyle.SINGLE, size: 4, color: "000000" },
      left: NB, right: NB, insideHorizontal: NB, insideVertical: NB,
    },
    rows: [
      new TableRow({
        tableHeader: true, cantSplit: true,
        children: headers.map((t, i) => cell(t, true, i)),
      }),
      ...rowsData.map(r => new TableRow({
        cantSplit: true,
        children: r.map((t, i) => cell(t, false, i)),
      })),
    ],
  });
}

// --------------------------------------------------------------- formulas
/** centered formula with right-aligned number */
function formula(markup, num) {
  return new Paragraph({
    spacing: { before: 120, after: 120, line: 360 },
    tabStops: [
      { type: TabStopType.CENTER, position: Math.round(CONTENT_W_TW / 2) },
      { type: TabStopType.RIGHT, position: CONTENT_W_TW },
    ],
    children: [
      new TextRun({ text: "\t" }),
      ...runs(markup),
      new TextRun({ text: "\t(" + num + ")" }),
    ],
  });
}

// ------------------------------------------------------------ cover (R5)
function estimateTextWidth(text, pt) {
  let width = 0;
  for (const ch of text) {
    const code = ch.codePointAt(0);
    const isWide = (code >= 0x4E00 && code <= 0x9FFF) ||
      (code >= 0x3000 && code <= 0x303F) || (code >= 0xFF00 && code <= 0xFFEF);
    width += isWide ? pt * 20 : pt * 11;   // Latin/Cyrillic ~55% width
  }
  return width;
}
function splitTitleLinesW(title, maxWidthTw, pt) {
  const words = title.split(" ");
  const lines = [];
  let cur = "";
  for (const w of words) {
    const probe = cur ? cur + " " + w : w;
    if (estimateTextWidth(probe, pt) <= maxWidthTw || !cur) cur = probe;
    else { lines.push(cur); cur = w; }
  }
  if (cur) lines.push(cur);
  if (lines.length > 1 && lines[lines.length - 1].length <= 4) {
    const last = lines.pop();
    lines[lines.length - 1] += " " + last;
  }
  return lines;
}
function calcTitleLayoutMixed(title, maxWidthTw, preferredPt, minPt) {
  let titlePt = preferredPt || 36, lines;
  const min = minPt || 24;
  while (titlePt >= min) {
    lines = splitTitleLinesW(title, maxWidthTw, titlePt);
    if (lines.length <= 3) break;
    titlePt -= 2;
  }
  if (!lines || lines.length > 3) {
    lines = splitTitleLinesW(title, maxWidthTw, min);
    titlePt = min;
  }
  return { titlePt, titleLines: lines };
}
function calcR5MetaLayout(metaEntries, fontPt) {
  const pt = fontPt || 12;
  const maxLabelLen = Math.max(...metaEntries.map(e => [...e.label].length));
  const labelNeedTw = (maxLabelLen + 2) * pt * 11;
  const valueNeedTw = 6800;
  const totalNeedTw = labelNeedTw + valueNeedTw;
  const tablePct = Math.min(75, Math.max(55, Math.ceil(totalNeedTw / 11906 * 100)));
  const rawLabelPct = Math.ceil(labelNeedTw / (tablePct / 100 * 11906) * 100);
  return { tablePct, labelPct: Math.max(25, Math.min(45, rawLabelPct)) };
}
function buildR5MetaTable(metaEntries) {
  const { tablePct, labelPct } = calcR5MetaLayout(metaEntries);
  const valuePct = 100 - labelPct;
  const bottomBorder = { style: BorderStyle.SINGLE, size: 4, color: "000000" };
  const rows = metaEntries.map(entry => new TableRow({
    cantSplit: true,
    children: [
      new TableCell({
        width: { size: labelPct, type: WidthType.PERCENTAGE },
        borders: noBorders,
        margins: { top: 60, bottom: 60, left: 0, right: 0 },
        children: [new Paragraph({
          alignment: AlignmentType.LEFT,
          spacing: { before: 60, after: 60, line: 400 },
          children: [new TextRun({ text: entry.label + ":", size: 24, font: FONT })],
        })],
      }),
      new TableCell({
        width: { size: valuePct, type: WidthType.PERCENTAGE },
        borders: { top: NB, left: NB, right: NB, bottom: bottomBorder },
        margins: { top: 60, bottom: 60, left: 80, right: 0 },
        children: [new Paragraph({
          alignment: AlignmentType.LEFT,
          spacing: { before: 60, after: 60, line: 400 },
          children: [new TextRun({ text: entry.value, size: 24, font: FONT })],
        })],
      }),
    ],
  }));
  return new Table({
    width: { size: tablePct, type: WidthType.PERCENTAGE },
    alignment: AlignmentType.CENTER,
    layout: TableLayoutType.FIXED,
    borders: allNoBorders,
    rows,
  });
}
/** R5 Clean White academic cover — margin:0 section, 16838 exact wrapper */
function buildCoverR5(config) {
  const PAGE_H = 16838, SAFETY = 1200;
  const safeH = PAGE_H - SAFETY;
  const simMarginLR = 1701, simMarginT = 1200;
  const contentW = 11906 - simMarginLR * 2;

  const { titlePt, titleLines } = calcTitleLayoutMixed(config.title, contentW, 36, 24);
  const titleSize = titlePt * 2;
  const metaEntries = (config.metaLines || []).map(line => {
    const idx = line.indexOf(":");
    if (idx === -1) return { label: line, value: "" };
    return { label: line.slice(0, idx).trim(), value: line.slice(idx + 1).trim() };
  });

  const schoolNameH = config.schoolName ? (20 * 23 + 400) : 0;
  const docTypeH = config.docType ? (15 * 23 + 500) : 0;
  const titleTotalH = titleLines.length * (titlePt * 23 + 200);
  const subtitleH = config.subtitle ? 2 * (13 * 23 + 300) : 0;
  const metaTableH = metaEntries.length * 520;
  const footerH = config.footerRight ? (12 * 23 + 200) : 0;
  const fixedH = schoolNameH + docTypeH + titleTotalH + subtitleH +
    metaTableH + footerH + 3 * 350;
  const remaining = Math.max(safeH - fixedH, 600);
  const topSpacing = Math.min(Math.floor(remaining * 0.28) + simMarginT, 4200);
  const midSpacing = Math.min(Math.floor((remaining - simMarginT) * 0.18), 2000);
  const bottomSpacing = Math.max(
    Math.min(remaining - topSpacing + simMarginT - midSpacing, 5500), 800);

  const children = [];
  children.push(new Paragraph({ spacing: { before: topSpacing } }));
  if (config.schoolName) {
    children.push(new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 200, line: Math.ceil(20 * 23), lineRule: "atLeast" },
      children: [new TextRun({ text: config.schoolName, size: 40,
        characterSpacing: 40, font: FONT })],
    }));
  }
  if (config.docType) {
    children.push(new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 500, line: Math.ceil(15 * 23), lineRule: "atLeast" },
      children: [new TextRun({ text: config.docType, size: 30,
        color: "404040", font: FONT })],
    }));
  }
  for (let i = 0; i < titleLines.length; i++) {
    children.push(new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: {
        after: i < titleLines.length - 1 ? 120 : 300,
        line: Math.ceil(titlePt * 23), lineRule: "atLeast",
      },
      children: [new TextRun({ text: titleLines[i], size: titleSize,
        bold: true, font: FONT })],
    }));
  }
  if (config.subtitle) {
    children.push(new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 120, line: Math.ceil(13 * 23), lineRule: "atLeast" },
      children: [new TextRun({ text: config.subtitle, size: 26,
        color: "202020", font: FONT })],
    }));
    if (config.subtitle2) {
      children.push(new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 200, line: Math.ceil(13 * 23), lineRule: "atLeast" },
        children: [new TextRun({ text: config.subtitle2, size: 26,
          color: "202020", font: FONT })],
      }));
    }
  }
  children.push(new Paragraph({ spacing: { before: midSpacing } }));
  if (metaEntries.length > 0) children.push(buildR5MetaTable(metaEntries));
  children.push(new Paragraph({ spacing: { before: bottomSpacing } }));
  if (config.footerRight) {
    children.push(new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [new TextRun({ text: config.footerRight, size: 24,
        color: "404040", font: FONT })],
    }));
  }
  return [new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    layout: TableLayoutType.FIXED,
    borders: allNoBorders,
    rows: [new TableRow({
      height: { value: PAGE_H, rule: "exact" },
      children: [new TableCell({
        shading: { type: ShadingType.CLEAR, fill: "FFFFFF" },
        borders: noBorders, verticalAlign: "top",
        margins: { left: simMarginLR, right: simMarginLR },
        children,
      })],
    })],
  })];
}

// ------------------------------------------------------- header / footers
function buildHeader(title) {
  return new Header({ children: [
    new Paragraph({
      alignment: AlignmentType.CENTER,
      border: { bottom: { style: BorderStyle.SINGLE, size: 1, color: "000000" } },
      children: [new TextRun({ text: title, size: 18, color: "333333", font: FONT })],
    }),
  ] });
}
function buildPageNumberFooter() {
  return new Footer({ children: [
    new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [
        new TextRun({ text: "- ", size: 21, font: FONT }),
        new TextRun({ children: [PageNumber.CURRENT], size: 21, font: FONT }),
        new TextRun({ text: " -", size: 21, font: FONT }),
      ],
    }),
  ] });
}

// ---------------------------------------------------------------- assemble
function buildDocument(cfg) {
  const bodyChildren = [];
  for (const b of cfg.body) {
    switch (b.type) {
      case "h1": bodyChildren.push(h1(b.text)); break;
      case "h2": bodyChildren.push(h2(b.text)); break;
      case "h3": bodyChildren.push(h3(b.text)); break;
      case "p": bodyChildren.push(p(b.text, b.opts)); break;
      case "pFlat": bodyChildren.push(pFlat(b.text, b.opts)); break;
      case "pList": bodyChildren.push(pList(b.text)); break;
      case "fig": bodyChildren.push(...figure(b.path, b.caption, b.width)); break;
      case "table":
        bodyChildren.push(tableCaption(b.caption));
        bodyChildren.push(threeLineTable(b.headers, b.rows, b.colPct));
        break;
      case "formula": bodyChildren.push(formula(b.markup, b.num)); break;
      case "spacer": bodyChildren.push(new Paragraph({ spacing: { before: b.h || 120 } })); break;
      default: throw new Error("unknown block type: " + b.type);
    }
  }

  const front = [];
  front.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 240, after: 360, line: 360 },
    children: [new TextRun({ text: cfg.abstractTitle, bold: true, size: 32, font: FONT })],
  }));
  for (const t of cfg.abstract) front.push(p(t, { after: 120 }));
  front.push(new Paragraph({
    alignment: AlignmentType.JUSTIFIED,
    spacing: { before: 240, line: 360 },
    children: [
      new TextRun({ text: cfg.keywordsLabel + " ", bold: true, size: 24, font: FONT }),
      ...runs(cfg.keywords, { size: 24 }),
      new PageBreak(),
    ],
  }));
  // TOC on its own page (page break attached to the keywords paragraph above)
  front.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 240, after: 360, line: 360 },
    children: [new TextRun({ text: cfg.tocTitle, bold: true, size: 32, font: FONT })],
  }));
  front.push(new TableOfContents("Table of Contents", {
    hyperlink: true,
    headingStyleRange: "1-3",
  }));
  front.push(new Paragraph({
    spacing: { before: 200 },
    children: [new TextRun({
      text: cfg.tocHint,
      italics: true, size: 18, color: "888888", font: FONT,
    })],
  }));

  const doc = new Document({
    creator: "AB-Cloud Research",
    title: cfg.docTitle,
    subject: cfg.docSubject,
    description: cfg.docSubject,
    styles: {
      default: {
        document: {
          run: { font: FONT, size: 24, color: "000000" },
          paragraph: { spacing: { line: 360 } },
        },
        heading1: {
          run: { font: FONT, size: 32, bold: true, color: "000000" },
          paragraph: { alignment: AlignmentType.CENTER, spacing: { before: 480, after: 360, line: 360 }, outlineLevel: 0 },
        },
        heading2: {
          run: { font: FONT, size: 30, bold: true, color: "000000" },
          paragraph: { spacing: { before: 360, after: 240, line: 360 }, outlineLevel: 1 },
        },
        heading3: {
          run: { font: FONT, size: 28, bold: true, color: "000000" },
          paragraph: { spacing: { before: 240, after: 120, line: 360 }, outlineLevel: 2 },
        },
      },
    },
    sections: [
      { // Section 1: cover — margin 0, no numbers, no footer
        properties: {
          page: {
            size: { width: 11906, height: 16838 },
            margin: { top: 0, bottom: 0, left: 0, right: 0 },
          },
        },
        children: buildCoverR5(cfg.cover),
      },
      { // Section 2: front matter — Roman numerals
        properties: {
          type: SectionType.NEXT_PAGE,
          page: {
            size: { width: 11906, height: 16838 },
            margin: { top: 1440, bottom: 1440, left: 1701, right: 1417, header: 850, footer: 700 },
            pageNumbers: { start: 1, formatType: NumberFormat.UPPER_ROMAN },
          },
        },
        headers: { default: buildHeader(cfg.headerTitle) },
        footers: { default: buildPageNumberFooter() },
        children: front,
      },
      { // Section 3: body — Arabic from 1
        properties: {
          type: SectionType.NEXT_PAGE,
          page: {
            size: { width: 11906, height: 16838 },
            margin: { top: 1440, bottom: 1440, left: 1701, right: 1417, header: 850, footer: 700 },
            pageNumbers: { start: 1, formatType: NumberFormat.DECIMAL },
          },
        },
        headers: { default: buildHeader(cfg.headerTitle) },
        footers: { default: buildPageNumberFooter() },
        children: bodyChildren,
      },
    ],
  });
  return Packer.toBuffer(doc);
}

module.exports = { buildDocument, runs };
