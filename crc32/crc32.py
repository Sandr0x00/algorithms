#!/usr/bin/env python3

import time
import sys

polynomial = 0xEDB88320

def crc32(data):
    crc = 0xFFFFFFFF
    for i in data:
        crc ^= i
        for _ in range(8):
            t = ((crc & 1) - 1) ^ 0xffffffff
            crc = (crc >> 1) ^ (t & polynomial)

    return crc ^ 0xFFFFFFFF

print(hex(crc32(sys.argv[1].encode())))