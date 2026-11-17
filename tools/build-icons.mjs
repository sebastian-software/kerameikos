// Renders the raster files of every mark from its SVG files and writes them next to them:
//
//   marks/<product>/icons/favicon.ico           16, 32 and 48 px, small mark with paper disc
//   marks/<product>/icons/apple-touch-icon.png  180 px opaque paper square, small mark at 148 px
//   marks/<product>/icons/icon-192.png          web app manifest, small mark with paper disc
//   marks/<product>/icons/icon-512.png          the same at 512 px
//   marks/<product>/png/mark.png                1024 px full mark, transparent, for documents
//   marks/<product>/png/mark-on-dark.png        1024 px full mark with paper disc
//   marks/<product>/png/lockup.png              lockup, mark 256 px high
//   marks/<product>/png/lockup-on-dark.png      the same for dark surfaces
//
// Icons are shown at icon size even when the file is larger, so they use the small mark
// (DESIGN.md, "Which version at which size"). Browser tabs and launchers are light or dark, so
// icons carry the paper disc. The outputs are committed; run this after changing a mark:
//
//   NODE_PATH=$(npm root -g) node tools/build-icons.mjs [product ...]
//
// It needs Playwright with Chromium and no other tool.
import { mkdirSync, readdirSync, readFileSync, writeFileSync, existsSync } from "node:fs"
import { dirname, join } from "node:path"
import { fileURLToPath } from "node:url"
import { createRequire } from "node:module"

const require = createRequire(import.meta.url)
const { chromium } = require("playwright")

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..")
const MARKS = join(ROOT, "marks")
const PAPER = "#faf9f4"

/** An ICO file holding one PNG per size, which every current browser reads. */
function ico(images) {
  const header = Buffer.alloc(6 + 16 * images.length)
  header.writeUInt16LE(0, 0)
  header.writeUInt16LE(1, 2)
  header.writeUInt16LE(images.length, 4)
  let offset = header.length
  images.forEach(({ png, size }, index) => {
    const entry = 6 + 16 * index
    header.writeUInt8(size % 256, entry)
    header.writeUInt8(size % 256, entry + 1)
    header.writeUInt16LE(1, entry + 4)
    header.writeUInt16LE(32, entry + 6)
    header.writeUInt32LE(png.length, entry + 8)
    header.writeUInt32LE(offset, entry + 12)
    offset += png.length
  })
  return Buffer.concat([header, ...images.map((image) => image.png)])
}

/** The SVG's markup with a fixed pixel size. */
function sized(markup, width, height) {
  return markup.replace("<svg ", `<svg width="${width}" height="${height}" `)
}

function viewBox(markup) {
  const [, , w, h] = markup.match(/viewBox="([^"]+)"/)[1].split(/\s+/).map(Number)
  return { w, h }
}

function write(path, content) {
  mkdirSync(dirname(path), { recursive: true })
  writeFileSync(path, content)
  console.log(`wrote ${path.slice(ROOT.length + 1)}`)
}

const wanted = process.argv.slice(2)
const products = readdirSync(MARKS)
  .filter((name) => existsSync(join(MARKS, name, "mark-small.svg")))
  .filter((name) => wanted.length === 0 || wanted.includes(name))
  .sort()

const browser = await chromium.launch()
try {
  const page = await browser.newPage()
  const shoot = async (body, width, height, background = "transparent") => {
    await page.setViewportSize({ width, height })
    await page.setContent(
      `<!doctype html><body style="margin:0;width:${width}px;height:${height}px;display:grid;place-items:center;background:${background}">${body}</body>`,
    )
    return page.screenshot({ type: "png", omitBackground: background === "transparent" })
  }

  for (const product of products) {
    const dir = join(MARKS, product)
    const read = (name) => readFileSync(join(dir, `${name}.svg`), "utf8").trim()
    const small = read("mark-small")
    const smallOnDark = read("mark-small-on-dark")

    const favicons = []
    for (const size of [16, 32, 48]) {
      favicons.push({ size, png: await shoot(sized(smallOnDark, size, size), size, size) })
    }
    write(join(dir, "icons/favicon.ico"), ico(favicons))
    write(join(dir, "icons/apple-touch-icon.png"), await shoot(sized(small, 148, 148), 180, 180, PAPER))
    for (const size of [192, 512]) {
      write(join(dir, `icons/icon-${size}.png`), await shoot(sized(smallOnDark, size, size), size, size))
    }

    for (const name of ["mark", "mark-on-dark"]) {
      write(join(dir, `png/${name}.png`), await shoot(sized(read(name), 1024, 1024), 1024, 1024))
    }
    for (const name of ["lockup", "lockup-on-dark"]) {
      const markup = read(name)
      const { w, h } = viewBox(markup)
      const width = Math.round((w / h) * 256)
      write(join(dir, `png/${name}.png`), await shoot(sized(markup, width, 256), width, 256))
    }
  }
} finally {
  await browser.close()
}
