// Render all marks on one sheet, to hand to an image model in one request.
// usage: NODE_PATH=$(npm root -g) node tools/sheet.mjs out.png [mark-file]
// The marks stand in a 4 x 2 grid in the order of SHEET_ORDER, without labels, each 560 px wide.
// mark-file is mark.svg by default; mark-small.svg renders the small versions for review.
import { createRequire } from "node:module"
import fs from "node:fs"
import path from "node:path"
import { fileURLToPath } from "node:url"
const { chromium } = createRequire(import.meta.url)("playwright")
export const SHEET_ORDER = [
  "palamedes",
  "tereon",
  "stentaro",
  "terminaro",
  "gramano",
  "curano",
  "agoros",
  "naos",
]
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..")
const [, , out, file = "mark.svg"] = process.argv
if (!out) {
  console.error("usage: sheet.mjs out.png [mark-file]")
  process.exit(1)
}
const cell = (product, index) => {
  const svg = fs
    .readFileSync(path.join(root, "marks", product, file), "utf8")
    .replace("<svg ", '<svg width="560" height="560" ')
    .replaceAll("-window", `-window-${index}`)
  return `<div>${svg}</div>`
}
const browser = await chromium.launch()
const page = await browser.newPage({
  viewport: { width: 4 * 560 + 5 * 80, height: 2 * 560 + 3 * 80 },
})
await page.setContent(
  `<body style="margin:0;padding:80px;background:#FAF9F4;display:grid;grid-template-columns:repeat(4,560px);gap:80px">${SHEET_ORDER.map(cell).join("")}</body>`,
)
await page.screenshot({ path: out })
await browser.close()
