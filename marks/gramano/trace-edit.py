# Gramano: the open sheet is paper, only the two rolls stay bronze; the shoulder clasp is a bronze disc.
lab_a, _ = ndimage.label(accent)
comp = lab_a == lab_a[750*S, 800*S]
(x1, y1), (x2, y2) = (983*S, 603*S), (907*S, 833*S)
side = (xx-x1)*(y2-y1) - (yy-y1)*(x2-x1)
accent &= ~(comp & (side < 0))
ccx, ccy, cr = 341.7*S, 588.5*S, 31.5*S
disc = np.hypot(xx-ccx, yy-ccy) <= cr
accent |= disc; navy &= ~disc
