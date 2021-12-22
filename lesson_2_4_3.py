"""
曲線 ダイア
"""

if False:
    from lib.Processing3 import *
import util

MARK_COLOR = color(0, 0, 255)
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
    vt2 = PVector(SIZE / 4, SIZE / 2)
    vt3 = PVector(SIZE / 2, 0)
    vt4 = util.mirror_x(vt2, SIZE)
    cp1 = vt1
    cp2 = vt2
    cp3 = vt2
    cp4 = vt3
    cp5 = util.mirror_x(cp4, SIZE)
    cp6 = util.mirror_x(cp3, SIZE)
    cp7 = util.mirror_x(cp2, SIZE)
    cp8 = util.mirror_x(cp1, SIZE)
    vertices = [vt1, vt2, vt3, vt4]
    control_points = [cp1, cp2, cp3, cp4, cp5, cp6, cp7, cp8]
    util.draw_bezier_shape(vertices, control_points)
    util.draw_check_point(vertices, control_points)
