/* Dirac Laboratory monograph generator (EN/RU) — docx-js, R5 academic cover */
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  ImageRun, PageBreak, Header, Footer, PageNumber, NumberFormat,
  AlignmentType, HeadingLevel, WidthType, BorderStyle, ShadingType,
  TableOfContents, TableLayoutType,
} = require("docx");
const fs = require("fs");

/* PNG dimension reader — parse IHDR (width @16, height @20), no deps */
function pngSize(buf) {
  return { width: buf.readUInt32BE(16), height: buf.readUInt32BE(20) };
}

const lang = process.argv[2] || "en";
const content = JSON.parse(fs.readFileSync(`${__dirname}/monograph_${lang}.json`, "utf8"));
const figDir = `${__dirname}/../figures`;
const outFile = `${__dirname}/../monographs/${lang}/Dirac_Lab_Monograph_${lang.toUpperCase()}.docx`;

const NB = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const noBorders = { top: NB, bottom: NB, left: NB, right: NB };
const allNoBorders = { top: NB, bottom: NB, left: NB, right: NB, insideHorizontal: NB, insideVertical: NB };

const isRu = lang === "ru";
const T = isRu ? {
  tocTitle: "Содержание", abstract: "Аннотация", refs: "Литература",
  refreshHint: "Примечание: обновите поле оглавления (правый клик → «Обновить поле») для актуальных номеров страниц.",
} : {
  tocTitle: "Table of Contents", abstract: "Abstract", refs: "References",
  refreshHint: "Note: refresh the TOC field (right-click → \u201cUpdate Field\u201d) to obtain current page numbers.",
};

/* Latin/Cyrillic-aware title layout (R5 adapted): char width ~ pt*11 twips */
function calcTitleLayout(title, maxWidthTwips, preferredPt = 34, minPt = 22) {
  const charsPerLine = (pt) => Math.floor(maxWidthTwips / (pt * 11));
  const split = (text, cpl) => {
    const words = text.split(" ");
    const lines = []; let cur = "";
    for (const w of words) {
      if ((cur + " " + w).trim().length > cpl && cur) { lines.push(cur.trim()); cur = w; }
      else cur = (cur + " " + w).trim();
    }
    if (cur) lines.push(cur.trim());
    return lines;
  };
  let pt = preferredPt, lines;
  while (pt >= minPt) {
    lines = split(title, charsPerLine(pt));
    if (lines.length <= 3) break;
    pt -= 2;
  }
  return { titlePt: pt, titleLines: lines };
}

function buildCoverR5(cfg) {
  const PAGE_H = 16838, SAFETY = 1200, simMarginLR = 1701, simMarginT = 1200;
  const contentW = 11906 - simMarginLR * 2;
  const { titlePt, titleLines } = calcTitleLayout(cfg.title, contentW);
  const titleSize = titlePt * 2;
  const metaEntries = cfg.metaLines.map(line => {
    const idx = line.indexOf(":");
    return { label: line.slice(0, idx).trim(), value: line.slice(idx + 1).trim() };
  });
  const metaTableH = metaEntries.length * 520;
  const titleTotalH = titleLines.length * (titlePt * 23 + 200);
  const subtitleH = cfg.subtitle ? (13 * 23 + 600) : 0;
  const fixedH = titleTotalH + subtitleH + metaTableH + 3 * 350 + 900;
  const remaining = Math.max(PAGE_H - SAFETY - fixedH, 600);
  const topSpacing = Math.min(Math.floor(remaining * 0.30) + simMarginT, 4200);
  const midSpacing = Math.min(Math.floor((remaining - simMarginT) * 0.20), 2000);
  const bottomSpacing = Math.max(Math.min(remaining - topSpacing + simMarginT - midSpacing, 5500), 600);

  const children = [new Paragraph({ spacing: { before: topSpacing } })];
  for (let i = 0; i < titleLines.length; i++) {
    children.push(new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: i < titleLines.length - 1 ? 120 : 300, line: Math.ceil(titlePt * 23), lineRule: "atLeast" },
      children: [new TextRun({ text: titleLines[i], size: titleSize, bold: true, font: { ascii: "Times New Roman", eastAsia: "Times New Roman" } })],
    }));
  }
  if (cfg.subtitle) children.push(new Paragraph({
    alignment: AlignmentType.CENTER, spacing: { after: 200, line: 340, lineRule: "atLeast" },
    children: [new TextRun({ text: cfg.subtitle, size: 26, italics: true, color: "404040", font: { ascii: "Times New Roman" } })],
  }));
  children.push(new Paragraph({ spacing: { before: midSpacing } }));
  const bottomBorder = { style: BorderStyle.SINGLE, size: 4, color: "000000" };
  children.push(new Table({
    width: { size: 62, type: WidthType.PERCENTAGE }, alignment: AlignmentType.CENTER,
    layout: TableLayoutType.FIXED, borders: allNoBorders,
    rows: metaEntries.map(e => new TableRow({
      children: [
        new TableCell({
          width: { size: 34, type: WidthType.PERCENTAGE }, borders: noBorders,
          margins: { top: 60, bottom: 60, left: 0, right: 0 },
          children: [new Paragraph({ spacing: { line: 400, lineRule: "atLeast" }, children: [new TextRun({ text: e.label + ":", size: 24, font: { ascii: "Times New Roman" } })] })],
        }),
        new TableCell({
          width: { size: 66, type: WidthType.PERCENTAGE },
          borders: { top: NB, left: NB, right: NB, bottom: bottomBorder },
          margins: { top: 60, bottom: 60, left: 80, right: 0 },
          children: [new Paragraph({ spacing: { line: 400, lineRule: "atLeast" }, children: [new TextRun({ text: e.value, size: 24, font: { ascii: "Times New Roman" } })] })],
        }),
      ],
    })),
  }));
  children.push(new Paragraph({ spacing: { before: bottomSpacing } }));
  children.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: cfg.footer, size: 24, color: "404040", font: { ascii: "Times New Roman" } })],
  }));
  return [new Table({
    width: { size: 100, type: WidthType.PERCENTAGE }, layout: TableLayoutType.FIXED,
    borders: allNoBorders,
    rows: [new TableRow({
      height: { value: PAGE_H, rule: "exact" },
      children: [new TableCell({
        shading: { type: ShadingType.CLEAR, fill: "FFFFFF" }, borders: noBorders,
        verticalAlign: "top", margins: { left: simMarginLR, right: simMarginLR },
        children,
      })],
    })],
  })];
}

function body(text) {
  return new Paragraph({
    alignment: AlignmentType.JUSTIFIED,
    indent: { firstLine: 425 },
    spacing: { line: 312, after: 80 },
    children: [new TextRun({ text, size: 23, font: { ascii: "Times New Roman", eastAsia: "Times New Roman" } })],
  });
}
function h1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1, spacing: { before: 360, after: 160, line: 312 },
    children: [new TextRun({ text, bold: true, size: 30, color: "0B1220", font: { ascii: "Times New Roman" } })],
  });
}
function figureBlock(src, caption) {
  const p = `${figDir}/${src}`;
  const buf = fs.readFileSync(p);
  const d = pngSize(buf);
  const displayW = 620;
  const displayH = Math.round(displayW * d.height / d.width);
  return [
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 160, after: 60 }, keepNext: true,
      children: [new ImageRun({ data: buf, transformation: { width: displayW, height: displayH }, type: "png" })] }),
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 200 },
      children: [new TextRun({ text: caption, size: 19, italics: true, color: "444444", font: { ascii: "Times New Roman" } })] }),
  ];
}
function tableBlock(caption, header, rows) {
  return [
    new Paragraph({ keepNext: true, spacing: { before: 160, after: 80 },
      children: [new TextRun({ text: caption, bold: true, size: 21, font: { ascii: "Times New Roman" } })] }),
    new Table({
      width: { size: 100, type: WidthType.PERCENTAGE },
      borders: {
        top: { style: BorderStyle.SINGLE, size: 6, color: "000000" },
        bottom: { style: BorderStyle.SINGLE, size: 6, color: "000000" },
        left: NB, right: NB,
        insideHorizontal: { style: BorderStyle.SINGLE, size: 2, color: "BBBBBB" },
        insideVertical: NB,
      },
      rows: [
        new TableRow({ tableHeader: true, cantSplit: true,
          children: header.map((t, i) => new TableCell({
            children: [new Paragraph({ children: [new TextRun({ text: t, bold: true, size: 20, font: { ascii: "Times New Roman" } })] })],
            shading: { type: ShadingType.CLEAR, fill: "F1F5F9" },
            margins: { top: 60, bottom: 60, left: 120, right: 120 },
            width: { size: i === 1 ? 52 : 16, type: WidthType.PERCENTAGE },
          })) }),
        ...rows.map(r => new TableRow({ cantSplit: true,
          children: r.map((t, i) => new TableCell({
            children: [new Paragraph({ children: [new TextRun({ text: t, size: 20, font: { ascii: "Times New Roman" } })] })],
            margins: { top: 50, bottom: 50, left: 120, right: 120 },
            width: { size: i === 1 ? 52 : 16, type: WidthType.PERCENTAGE },
          })) })),
      ],
    }),
  ];
}

/* ── assemble ── */
const children = [];
children.push(h1(T.abstract));
children.push(body(content.abstract));
children.push(new Paragraph({
  children: [new TextRun({ text: isRu ? "Ключевые слова: уравнение Дирака, модель Хофштадтера, нули дзета-функции, программа Гильберта–Пойа, GUE, фаза Берри, туннелирование Клейна, цвиттербевегунг, киральная симметрия, нулевые моды Джекива–Росси, парная корреляция Монтгомери, индекс-восстанавливающая декорация." : "Keywords: Dirac equation, Hofstadter model, Riemann zeta zeros, Hilbert-Polya programme, GUE, Berry phase, Klein tunneling, Zitterbewegung, chiral symmetry, Jackiw-Rossi zero modes, Montgomery pair correlation, index-restoring decoration.", size: 21, italics: true }), new PageBreak()],
}));
children.push(new Paragraph({
  alignment: AlignmentType.CENTER, spacing: { before: 240, after: 240 },
  children: [new TextRun({ text: T.tocTitle, bold: true, size: 30, font: { ascii: "Times New Roman" } })],
}));
children.push(new TableOfContents("Contents", { hyperlink: true, headingStyleRange: "1-2" }));
children.push(new Paragraph({ spacing: { before: 120 },
  children: [new TextRun({ text: T.refreshHint, italics: true, size: 18, color: "888888", font: { ascii: "Times New Roman" } })] }));
children.push(new Paragraph({
  spacing: { before: 60 },
  children: [new TextRun({ text: isRu ? "Переход к основному тексту." : "The main text follows.", size: 2, color: "FFFFFF" }), new PageBreak()],
}));

for (const sec of content.sections) {
  children.push(h1(sec.title));
  for (const b of sec.blocks) {
    if (b.t === "p") children.push(body(b.text));
    else if (b.t === "figure") children.push(...figureBlock(b.src, b.caption));
    else if (b.t === "table") children.push(...tableBlock(b.caption, b.header, b.rows));
  }
}
children.push(h1(T.refs));
for (const r of content.references) {
  children.push(new Paragraph({
    alignment: AlignmentType.LEFT, spacing: { line: 312, after: 60 },
    indent: { left: 400, hanging: 400 },
    children: [new TextRun({ text: r, size: 20, font: { ascii: "Times New Roman" } })],
  }));
}

const doc = new Document({
  creator: "AB-Cloud Dirac Laboratory",
  title: content.title,
  description: content.subtitle,
  styles: { default: { document: {
    run: { font: { ascii: "Times New Roman", eastAsia: "Times New Roman" }, size: 23, color: "000000" },
    paragraph: { spacing: { line: 312 } },
  }}},
  features: { updateFields: true },
  sections: [
    { properties: { page: { margin: { top: 0, bottom: 0, left: 0, right: 0 } } },
      children: buildCoverR5({
        title: content.title, subtitle: content.subtitle,
        metaLines: [
          (isRu ? "Автор: " : "Author: ") + content.author,
          (isRu ? "Идентификатор: " : "Identifier: ") + content.orcid,
          (isRu ? "Организация: " : "Affiliation: ") + content.affiliation,
          (isRu ? "Дата: " : "Date: ") + content.date,
        ],
        footer: "AB-Cloud Research — Dirac Laboratory (D1–D10, v1.1)",
      }) },
    { properties: { page: { margin: { top: 1440, bottom: 1440, left: 1560, right: 1440 } } },
      headers: { default: new Header({ children: [new Paragraph({ alignment: AlignmentType.RIGHT,
        children: [new TextRun({ text: content.title, size: 16, color: "888888", italics: true, font: { ascii: "Times New Roman" } })] })] }) },
      footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER,
        children: [new TextRun({ children: [PageNumber.CURRENT], size: 18, color: "666666", font: { ascii: "Times New Roman" } })] })] }) },
      children },
  ],
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(outFile, buf);
  console.log("written:", outFile, buf.length, "bytes");
});
