"""
たくさんのハートマーク
"""

if False:
    from lib.Processing3 import *
import util

BACKGROUND_COLOR = color(0, 44, 77)
SIZE_X = 800
SIZE_Y = 600
MARK_TYPE = 'heart'  # heart, leaf


def setup():
    size(SIZE_X, SIZE_Y)
    colorMode(HSB, 360, 100, 100)
    background(BACKGROUND_COLOR)
    for i in range(100):
        p = PVector(random(width), random(height))
        angle = map(random(1), 0, 1, 0, TWO_PI)
        mark_size = random(10, 30)
        draw_mark(p, angle, mark_size, MARK_TYPE)


def draw_mark(p, angle, mark_size, mark_type):
    if mark_type == 'leaf':
        mark_color = random(120, 150)
        vt1 = PVector(mark_size / 2, mark_size)
        vt2 = PVector(mark_size / 4, mark_size * 3 / 4)
        vt3 = PVector(mark_size / 2, 0)
        cp1 = PVector(mark_size * 3 / 8, mark_size)
        cp2 = PVector(mark_size / 4, mark_size * 7 / 8)
        cp3 = PVector(mark_size / 4, mark_size / 2)
        cp4 = PVector(mark_size * 3 / 8, mark_size / 4)
    else:  # heart
        mark_color = random(20)
        vt1 = PVector(mark_size / 2, mark_size)
        vt2 = PVector(mark_size / 4, mark_size * 3 / 4)
        vt3 = PVector(mark_size / 2, mark_size / 4)
        cp1 = PVector(mark_size / 2, mark_size)
        cp2 = PVector(mark_size / 4, mark_size * 3 / 4)
        cp3 = PVector(-mark_size / 4, mark_size / 4)
        cp4 = PVector(mark_size / 4, -mark_size / 4)
    fill(mark_color, 100, 100)
    strokeWeight(1)
    stroke(mark_color, 100, 100)
    pushMatrix()
    translate(p.x, p.y)
    rotate(angle)
    util.draw_bezier_shape(vt1, vt2, vt3, cp1, cp2, cp3, cp4, mark_size)
    popMatrix()


def mirror_x(x, mark_size):
    return mark_size - x
