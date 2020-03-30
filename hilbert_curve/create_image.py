#!/usr/bin/env python3

import sys
sys.path.append('..')

from PIL import Image

from hilbert_curve import HilbertCurve

def fade(fr, to, d, n):
    return (
        (fr[0] - (to[0] * int(d/n * 256))) & 0xff,
        (fr[1] - (to[1] * int(d/n * 256))) & 0xff,
        (fr[2] - (to[2] * int(d/n * 256))) & 0xff
    )

if __name__ == "__main__":
    n = 16

    h = HilbertCurve(n)

    curve = []
    for x in range(n):
        for y in range(n):
            d = h.xy2d(x, y)
            curve.append(fade((0,255,255), (255,0,0), d, n * n))


    # for d in range(n * n):
    #     x,y = h.d2xy(d)

    im2 = Image.new("RGB", (n, n))
    im2.putdata(curve)
    im2.save("curve.png")
