"""
虹
"""

if False:
    from lib.Processing3 import *


def setup():
    colorMode(HSB, 360, 100, 100)
    noStroke()
    size(1000, 1000)
    background(0)
    # 7 color
    for i in range(12):
        if i >= 7:
            fill('#00000')
        else:
            fill(map(i, 0, 7, 0, 300), 100, 100)
        radius = 50 * (12 - i)
        ellipse(width / 2, height / 2, radius, radius)
    # # 70 color
    # for i in range(120):
    #     if i >= 70:
    #         fill('#00000')
    #     else:
    #         fill(map(i, 0, 70, 0, 300), 100, 100)
    #     radius = radius = 5 * (120 - i)
    #     ellipse(width / 2, height / 2, radius, radius)
    #     rect(0, height / 2, width, height / 2)
    print('hello world')
