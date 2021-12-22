"""
曲線 ダイア
"""

if False:
    from lib.Processing3 import *
import util

MARK_COLOR = color(0, 0, 255)
BACKGROUND_COLOR = color(0, 44, 77)
MARK_SIZE = 400


def setup():
    size(MARK_SIZE, MARK_SIZE)
    grid = loadImage('grid.png')
    image(grid, 0, 0)
    # background(BACKGROUND_COLOR)
    fill(MARK_COLOR)
    noStroke()
    vt1 = PVector(MARK_SIZE / 2, MARK_SIZE)
    vt2 = PVector(MARK_SIZE / 4, MARK_SIZE / 2)
    vt3 = PVector(MARK_SIZE / 2, 0)
    vt4 = util.mirror_x(vt2, MARK_SIZE)
    cp1 = vt1
    cp2 = vt2
    cp3 = vt2
    cp4 = vt3
    cp5 = util.mirror_x(cp4, MARK_SIZE)
    cp6 = util.mirror_x(cp3, MARK_SIZE)
    cp7 = util.mirror_x(cp2, MARK_SIZE)
    cp8 = util.mirror_x(cp1, MARK_SIZE)
    vertices = [vt1, vt2, vt3, vt4]
    control_points = [cp1, cp2, cp3, cp4, cp5, cp6, cp7, cp8]
    util.draw_bezier_shape(vertices, control_points)
    util.draw_check_point(vertices, control_points)