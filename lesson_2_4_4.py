"""
曲線 ダイア
"""

if False:
    from lib.Processing3 import *
import util

MARK_COLOR = color(255, 0, 255)
BACKGROUND_COLOR = color(0, 44, 77)
SIZE = 400


def setup():
    size(SIZE, SIZE)
    grid = loadImage('grid.png')
    image(grid, 0, 0)
    # background(BACKGROUND_COLOR)
    fill(MARK_COLOR)
    noStroke()
    vt1 = PVector(SIZE / 2, SIZE)
    vt2 = PVector(0, SIZE / 2)
    vt3 = PVector(SIZE / 2, 0)
    cp1 = PVector(SIZE / 2, SIZE * 3 / 4)
    cp2 = PVector(SIZE / 4, SIZE / 2)
    cp3 = PVector(SIZE / 4, SIZE / 2)
    cp4 = PVector(SIZE / 2, SIZE / 4)
    util.draw_bezier_shape(vt1, vt2, vt3, cp1, cp2, cp3, cp4, SIZE)
    util.draw_check_point(vt1, vt2, vt3, cp1, cp2, cp3, cp4, SIZE)
