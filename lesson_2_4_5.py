"""
曲線 五芒星
"""

if False:
    from lib.Processing3 import *
import util

MARK_COLOR = color(255, 0, 255)
BACKGROUND_COLOR = color(0, 44, 77)
MARK_SIZE = 400


def setup():
    size(MARK_SIZE, MARK_SIZE)
    grid = loadImage('grid.png')
    image(grid, 0, 0)
    # background(BACKGROUND_COLOR)
    fill(MARK_COLOR)
    noStroke()
    radius = MARK_SIZE / 2
    pushMatrix()
    translate(radius, radius)
    # vt1 = PVector(radius * cos(PI * 0 / 10), radius * sin(PI * 0 / 10))
    # vt2 = PVector(radius * cos(PI * 4 / 10), radius * sin(PI * 4 / 10))
    # vt3 = PVector(radius * cos(PI * 8 / 10), radius * sin(PI * 8 / 10))
    # vt4 = PVector(radius * cos(PI * 12 / 10), radius * sin(PI * 12 / 10))
    # vt5 = PVector(radius * cos(PI * 16 / 10), radius * sin(PI * 16 / 10))
    # cp1 = PVector(radius * cos(PI * 2 / 10) / 3, radius * sin(PI * 2 / 10) / 3)
    # cp2 = PVector(radius * cos(PI * 2 / 10) / 3, radius * sin(PI * 2 / 10) / 3)
    # cp3 = PVector(radius * cos(PI * 6 / 10) / 3, radius * sin(PI * 6 / 10) / 3)
    # cp4 = PVector(radius * cos(PI * 6 / 10) / 3, radius * sin(PI * 6 / 10) / 3)
    # cp5 = PVector(radius * cos(PI * 10 / 10) / 3, radius * sin(PI * 10 / 10) / 3)
    # cp6 = PVector(radius * cos(PI * 10 / 10) / 3, radius * sin(PI * 10 / 10) / 3)
    # cp7 = PVector(radius * cos(PI * 14 / 10) / 3, radius * sin(PI * 14 / 10) / 3)
    # cp8 = PVector(radius * cos(PI * 14 / 10) / 3, radius * sin(PI * 14 / 10) / 3)
    # cp9 = PVector(radius * cos(PI * 18 / 10) / 3, radius * sin(PI * 18 / 10) / 3)
    # cp10 = PVector(radius * cos(PI * 18 / 10) / 3, radius * sin(PI * 18 / 10) / 3)
    # vertices = [vt1, vt2, vt3, vt4, vt5]
    # control_points = [cp1, cp2, cp3, cp4, cp5, cp6, cp7, cp8, cp9, cp10]
    vertices = []
    control_points = []
    for i in range(5):
        vertices.append(
            PVector(radius * cos(PI * i * 4 / 10), radius * sin(PI * i * 4 / 10))
        )
        control_points.append(
            PVector(radius * cos(PI * (2 + i * 4) / 10) / 3, radius * sin(PI * (2 + i * 4) / 10) / 3)
        )
        control_points.append(
            PVector(radius * cos(PI * (2 + i * 4) / 10) / 3, radius * sin(PI * (2 + i * 4) / 10) / 3)
        )
    util.draw_bezier_shape(vertices, control_points)
    util.draw_check_point(vertices, control_points)
    popMatrix()
