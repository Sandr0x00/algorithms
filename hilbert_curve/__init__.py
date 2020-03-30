#!/usr/bin/env python3

class HilbertCurve:

    def __init__(self, n):
        self.n = n

    # convert (x,y) to d
    def xy2d (self, x, y):
        s = self.n // 2
        d = 0
        while s > 0:
            rx = (x & s) > 0
            ry = (y & s) > 0
            d += s * s * ((3 * rx) ^ ry)
            x, y = self.rot(self.n, x, y, rx, ry)
            s //= 2
        return d

    # convert d to (x,y)
    def d2xy(self, d):
        x = y = 0
        t = d
        s = 1
        while s < self.n:
            rx = 1 & (t // 2)
            ry = 1 & (t ^ rx)
            x, y = self.rot(s, x, y, rx, ry)
            x += s * rx
            y += s * ry
            t //= 4
            s *= 2
        return y, x

    # rotate/flip a quadrant appropriately
    def rot(self, n, x, y, rx, ry):
        if ry:
            return x, y
        if rx:
            x = n - 1 - x
            y = n - 1 - y
        return y, x
