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
    for i in range(8):
        if i >= 7:
            fill('#00000')
        else:
            fill(map(i, 0, 7, 0, 300), 100, 100)
        ellipse(width / 2, height / 2, 50 * (12 - i), 50 * (12 - i))
    # # 70 color
    # for i in range(80):
    #     if i >= 70:
    #         fill('#00000')
    #     else:
    #         fill(map(i, 0, 70, 0, 300), 100, 100)
    #     ellipse(width / 2, height / 2, 5 * (120 - i), 5 * (120 - i))
    # # 700 color
    # for i in range(800):
    #     if i >= 700:
    #         fill('#00000')
    #     else:
    #         fill(map(i, 0, 700, 0, 300), 100, 100)
    #     ellipse(width / 2, height / 2, 0.5 * (1200 - i), 0.5 * (1200 - i))
    rect(0, height / 2, width, height / 2)
    print('hello world')
