"""Trace a generated emblem into a clean mark in the family ring frame.

usage: clean.py <image> <outdir> <Label> <factor> [dx=0] [dy=0]
  factor: size relative to the generated ring (1.0 = as generated)
env:   CLEAN_EDIT=<python file>  run on the masks before smoothing (navy, accent, xx, yy, S)
       CLEAN_SIGMA (default 1.1)  smoothing in source pixels
       CLEAN_TOL   (default 1.2)  potrace curve tolerance in source pixels
"""
import sys, re, os, subprocess, numpy as np
from PIL import Image
from scipy import ndimage
src, out, label, f = sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4])
dx = float(sys.argv[5]) if len(sys.argv) > 5 else 0.0
dy = float(sys.argv[6]) if len(sys.argv) > 6 else 0.0
SIGMA = float(os.environ.get('CLEAN_SIGMA', 1.1)); TOL = float(os.environ.get('CLEAN_TOL', 1.2))
os.makedirs(out, exist_ok=True)
S = 4
im = Image.open(src).convert('RGB'); im = im.resize((im.width*S, im.height*S), Image.BICUBIC)
a = np.asarray(im).astype(int); r, g, b = a[..., 0], a[..., 1], a[..., 2]
h, w = r.shape; yy, xx = np.mgrid[0:h, 0:w]

# 1. classify. Bronze by its warmth; navy by the red channel, where bronze and paper lie close together.
#    Beside bronze the threshold is the navy/bronze midpoint, elsewhere the navy/paper midpoint, so a line
#    is equally thick whatever it borders.
bronze = (r-b > 55) & (r > 140) & (g < 200)
near_bronze = ndimage.binary_dilation(bronze, iterations=3*S)
navy = r < np.where(near_bronze, 101, 132)
bronze &= ~navy

if os.environ.get('CLEAN_FRAME'):
    # the source has no ring: centre and the radius that maps to 107 are given in source pixels
    cx, cy, inner = (float(v)*S for v in os.environ['CLEAN_FRAME'].split(','))
    d = np.hypot(xx-cx, yy-cy); accent = bronze
else:
    # 2. the generated ring: largest bronze area. Fit its inner edge, then drop it.
    lab, n = ndimage.label(bronze)
    sizes = ndimage.sum(bronze, lab, range(1, n+1)); ring = lab == (1+int(np.argmax(sizes)))
    ys, xs = np.nonzero(ring); sel = np.random.default_rng(1).choice(len(xs), 40000, replace=False)
    x = xs[sel].astype(float); y = ys[sel].astype(float)
    A = np.c_[2*x, 2*y, np.ones_like(x)]; sol = np.linalg.lstsq(A, x*x+y*y, rcond=None)[0]
    cx, cy = sol[0], sol[1]
    d = np.hypot(xx-cx, yy-cy)
    ang = np.arctan2(yy[ring]-cy, xx[ring]-cx); bins = ((ang+np.pi)/(2*np.pi)*360).astype(int) % 360
    dr = d[ring]; inner = float(np.median([dr[bins == i].min() for i in range(360)]))
    accent = bronze & ~ring & (d < inner)
    navy &= d < inner - 2*S

if os.environ.get('CLEAN_EDIT'): exec(open(os.environ['CLEAN_EDIT']).read())

# 3. smooth: blur each mask and cut it again at one half, which rounds off steps and nicks; then
#    remove specks and fill pinholes.
def smooth(m, sigma):
    m = ndimage.gaussian_filter(m.astype(np.float32), sigma*S) > 0.5
    def drop_small(mask, area):
        l, k = ndimage.label(mask)
        if k == 0: return mask
        sz = ndimage.sum(mask, l, range(1, k+1)); keep = np.concatenate([[False], sz >= area])
        return keep[l]
    m = drop_small(m, 30*S*S)            # specks
    m = ~drop_small(~m, 14*S*S)          # pinholes
    return m
navy = smooth(navy, SIGMA); accent = smooth(accent, SIGMA)
# bronze runs under the navy that borders it, so no paper can show between the two
accent_draw = accent | (ndimage.binary_dilation(accent, iterations=4*S) & ndimage.binary_dilation(navy, iterations=1))

# 4. placement in the frame
k = 107.0/inner * f; tx = 120 + dx - k*cx; ty = 120 + dy - k*cy
m = navy | accent; ys, xs = np.nonzero(m)
free = m & (yy < cy + 0.3*inner)
print(f'{label}: x{f}; top y={ty+k*ys.min():.1f}, bottom y={ty+k*ys.max():.1f}, upper parts reach r={k*d[free].max():.1f}, all r={k*d[m].max():.1f}')

# 5. trace with potrace
def trace(mask, name):
    p = f'{out}/_{name}.pbm'
    Image.fromarray(np.where(mask, 0, 255).astype('uint8')).convert('1').save(p)
    svg = subprocess.run(['potrace', '-b', 'svg', '-a', '1.1', '-O', str(TOL*S), '-t', str(20*S*S), '-u', '1', '--flat', p, '-o', '-'],
                         capture_output=True, text=True, check=True).stdout
    os.remove(p)
    return re.findall(r'<path d="([^"]+)"', svg)
T = f'transform="translate({tx:.4f} {ty:.4f}) scale({k:.7f}) translate(0 {h}) scale(1 -1)"'
np_, ap = trace(navy, 'navy'), trace(accent_draw, 'accent')
nodes = sum(len(re.findall(r'[clm]', p)) for p in np_+ap)
slug = label.lower()
def svg(navyc, bronzec, disc=False):
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 240" role="img" aria-label="{label}">']
    if disc: p.append('<circle cx="120" cy="120" r="117" fill="#FAF9F4"/>')
    p += [f'<clipPath id="{slug}-window"><circle cx="120" cy="120" r="97"/></clipPath>', f'<g clip-path="url(#{slug}-window)">']
    p += [f'<path fill="{bronzec}" fill-rule="evenodd" {T} d="{" ".join(ap)}"/>'] if ap else []
    p += [f'<path fill="{navyc}" fill-rule="evenodd" {T} d="{" ".join(np_)}"/>', '</g>',
          f'<circle cx="120" cy="120" r="112" fill="none" stroke="{bronzec}" stroke-width="10"/>', '</svg>']
    return '\n'.join(p)
for name, s in (('mark', svg('#0E2A4D', '#BC8A45')), ('mark-on-dark', svg('#0E2A4D', '#BC8A45', True)), ('mark-mono', svg('#0E2A4D', '#0E2A4D'))):
    open(f'{out}/{name}.svg', 'w').write(s)
subprocess.run(['npx', '--yes', 'svgo@4', '--multipass', '-p', '2', '-f', out], capture_output=True)
for name in ('mark', 'mark-on-dark', 'mark-mono'):
    p = f'{out}/{name}.svg'; s = open(p).read()
    s = s.replace('<svg xmlns="http://www.w3.org/2000/svg"', '<svg xmlns="http://www.w3.org/2000/svg" role="img"', 1) if 'role=' not in s else s
    s = re.sub(r'id="a"', f'id="{slug}-window"', s); s = s.replace('url(#a)', f'url(#{slug}-window)')
    open(p, 'w').write(s)
print(f'{nodes} curve segments, {os.path.getsize(out+"/mark.svg")} bytes')
