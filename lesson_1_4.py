"""
虹（分割数を増やす）
"""

if False:
    from lib.Processing3 import *

DIVISION_NUMBER = 5  # 分割数


def setup():
    colorMode(HSB, 360, 100, 100)
    noStroke()
    size(1000, 1000)
    background(0)
    # 虹
    for i in range(int(DIVISION_NUMBER * 12 / 7)):
        if i >= DIVISION_NUMBER:
            fill(0)
        else:
            fill(map(i, 0, DIVISION_NUMBER, 0, 300), 100, 100)
        radius = (350 / DIVISION_NUMBER) * (DIVISION_NUMBER * 12 / 7 - i)
        ellipse(width / 2, height / 2, radius, radius)
    rect(0, height / 2, width, height / 2)
    print('hello world')
