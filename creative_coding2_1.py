"""
無限大
"""

if False:
    from lib.Processing3 import *

SIZE_X = 1200
SIZE_Y = 750
BASE_LENGTH = 300


def setup():
    size(SIZE_X, SIZE_Y)


def draw():
    background(255)
    translate(width / 2, height / 2)
    for i in range(360):
        angle = radians(i)
        x = BASE_LENGTH * sqrt(2) * cos(angle) / (sq(sin(angle)) + 1)
        y = BASE_LENGTH * sqrt(2) * cos(angle) * sin(angle) / (sq(sin(angle)) + 1)
        ellipse(x, y, 10, 10)
