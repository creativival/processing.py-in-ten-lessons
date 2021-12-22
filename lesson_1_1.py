"""
RGBの理解
"""

if False:
    from lib.Processing3 import *


def setup():
    noStroke()
    size(1024, 1024)
    for k in range(0, 256, 32):
        for j in range(0, 256, 32):
            for i in range(0, 256, 32):
                print(i, j, k)
                fill(i, j, k)
                rect(i * 4 + k / 2, j * 4, 16, 128)
