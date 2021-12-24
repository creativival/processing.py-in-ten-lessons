"""
ベジェ曲線による方眼紙の変形（S字カーブ）
"""

if False:
    from lib.Processing3 import *
import util


BACKGROUND_COLOR = color(0, 44, 77)
SIZE_X = 1000
SIZE_Y = 1000
count = 0
is_addable = True


def setup():
    size(SIZE_X, SIZE_Y)
    colorMode(HSB, 360, 100, 100)
    noFill()
    stroke(127)


def draw():
    global count
    background(BACKGROUND_COLOR)
    if is_addable:
        count += 1
    for i in range(501):
        # # 方眼紙
        # line(i * 10, 0, i * 10, height)
        # line(0, i * 10, width, i * 10)
        # ベジェ曲線
        vertex_point_1 = PVector(i * 10 - 2000, 0)
        vertex_point_2 = PVector(i * 10 - 2000, height)
        if is_addable:
            count += 1
        # if i <= 250:
        #     add_value = i * count / 20.0
        # else:
        #     add_value = -(501 - i) * count / 20.0
        add_value = count / 20.0
        control_point_1 = PVector.add(
            vertex_point_1,
            PVector(add_value, add_value)
        )
        control_point_2 = PVector.add(
            vertex_point_2,
            PVector(-add_value, -add_value)
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


def mouseClicked():
    global is_addable
    is_addable = not is_addable
