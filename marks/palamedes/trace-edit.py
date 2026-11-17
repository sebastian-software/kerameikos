# Palamedes: remove the supporting hand that pokes out under the tablet. Its forearm could not
# fit between the tablet and his body, so it read as an impossibly short arm. Without it the
# tablet rests against his body, held by a hand hidden behind it.
from PIL import Image as _I, ImageDraw as _D
poly = [(706, 949), (803, 928), (812, 940), (800, 962), (760, 985), (722, 1004), (706, 1006)]
_m = _I.new("L", (navy.shape[1], navy.shape[0]), 0)
_D.Draw(_m).polygon([(x*S, y*S) for x, y in poly], fill=255)
hand = np.asarray(_m) > 0
navy &= ~hand
accent &= ~hand
