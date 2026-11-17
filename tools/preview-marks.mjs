// Render marks side by side to judge a new one against the family.
// usage: NODE_PATH=$(npm root -g) node tools/preview-marks.mjs out.png mark1.svg mark2.svg ...
// Each mark is shown at 280 px with a dashed guide at the top limit (y = 38), and at 32 px below it.
// With --reference as the first argument the marks are shown large and plain, without guide and
// small copies: that picture is the style reference to attach to an image model's prompt.
import { createRequire } from "node:module"
import fs from "node:fs"
const { chromium } = createRequire(import.meta.url)("playwright")
const args = process.argv.slice(2)
const reference = args[0] === "--reference"
if (reference) args.shift()
const [out, ...files] = args
if (!out || files.length === 0) {
  console.error("usage: preview-marks.mjs out.png mark.svg [more.svg ...]")
  process.exit(1)
}
// Each inlined copy needs its own clip-path id, or all marks would use the first one's.
const inline = (file, index, size) =>
  fs
    .readFileSync(file, "utf8")
    .replace("<svg ", `<svg width="${size}" height="${size}" `)
    .replaceAll("-window", `-window-${index}-${size}`)
const plain = (file, index) => `<div>${inline(file, index, 520)}</div>`
const cell = (file, index) => `
  <div>
    <div style="position:relative;width:280px;height:280px">
      ${inline(file, index, 280)}
      <div style="position:absolute;left:0;right:0;top:${(38 / 240) * 280}px;border-top:1px dashed #d33"></div>
    </div>
    <div style="margin-top:12px">${inline(file, index, 32)}</div>
  </div>`
const browser = await chromium.launch()
const page = await browser.newPage({
  viewport: reference
    ? { width: files.length * 560 + 40, height: 600 }
    : { width: files.length * 300 + 40, height: 380 },
})
await page.setContent(
  `<body style="margin:${reference ? 40 : 20}px;background:#FAF9F4;display:flex;gap:${reference ? 40 : 20}px">${files
    .map(reference ? plain : cell)
    .join("")}</body>`,
)
await page.screenshot({ path: out })
await browser.close()
