"""
虹（分割数を増やす）
"""

if False:
    from lib.Processing3 import *

MAGNIFICATION = 10  # 倍率（数字）


def setup():
    colorMode(HSB, 360, 100, 100)
    noStroke()
    size(1000, 1000)
    background(0)
    # 虹
    for i in range(12 * MAGNIFICATION):
        if i >= 7 * MAGNIFICATION:
            fill(0)
        else:
            fill(map(i, 0, 7 * MAGNIFICATION, 0, 300), 100, 100)
        radius = (50 / MAGNIFICATION) * (12 * MAGNIFICATION - i)
        ellipse(width / 2, height / 2, radius, radius)
    rect(0, height / 2, width, height / 2)
    print('hello world')
