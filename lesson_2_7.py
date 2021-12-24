"""
ベジェ曲線による方眼紙の変形
"""

if False:
    from lib.Processing3 import *
import util


BACKGROUND_COLOR = color(0, 44, 77)
SIZE_X = 1000
SIZE_Y = 1000


def setup():
    size(SIZE_X, SIZE_Y)
    colorMode(HSB, 360, 100, 100)
    noFill()
    stroke(127)


def draw():
    background(BACKGROUND_COLOR)
    for i in range(101):
        # # 方眼紙
        # line(i * 10, 0, i * 10, height)
        # line(0, i * 10, width, i * 10)
        # ベジェ曲線
        vertex_point_1 = PVector(i * 10, 0)
        vertex_point_2 = PVector(i * 10, height)
        if i <= 50:
            add_value = i * frameCount / 2.0
        else:
            add_value = -(101 - i) * frameCount / 2.0
        control_point_1 = PVector.add(
            vertex_point_1,
            PVector(add_value, -100)
        )
        control_point_2 = PVector.add(
            vertex_point_2,
            PVector(add_value, 100)
        )
        print(control_point_1, control_point_2)
        bezier(
            vertex_point_1.x, vertex_point_1.y,
            control_point_1.x, control_point_1.y,
            control_point_2.x, control_point_2.y,
            vertex_point_2.x, vertex_point_2.y
        )
        bezier(
            vertex_point_1.y, vertex_point_1.x,
            control_point_1.y, control_point_1.x,
            control_point_2.y, control_point_2.x,
            vertex_point_2.y, vertex_point_2.x
        )
