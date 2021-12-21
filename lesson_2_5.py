"""
たくさんのハートマーク
"""

if False:
    from lib.Processing3 import *
import util

BACKGROUND_COLOR = color(0, 44, 77)
mark_size_X = 800
mark_size_Y = 600
MARK_TYPE = 'star'  # heart, leaf, diamond or star
MIN_MARK_mark_size = 20
MAX_MARK_mark_size = 40


def setup():
    size(mark_size_X, mark_size_Y)
    colorMode(HSB, 360, 100, 100)
    background(BACKGROUND_COLOR)
    for i in range(100):
        p = PVector(random(width), random(height))
        angle = map(random(1), 0, 1, 0, TWO_PI)
        mark_size = random(MIN_MARK_mark_size, MAX_MARK_mark_size)
        util.draw_mark(p, angle, mark_size, MARK_TYPE)


def mirror_x(x, mark_size):
    return mark_size - x
