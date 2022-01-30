"""
S字カーブ
"""

if False:
    from lib.Processing3 import *
import os
import util

BACKGROUND_COLOR = color(0, 44, 77)
SIZE_X = 1000
SIZE_Y = 1000
SPEED = 5
count = 0
is_countable = True


def setup():
    size(SIZE_X, SIZE_Y)
    noFill()


def draw():
    global count
    background(BACKGROUND_COLOR)
    if is_countable:
        count += SPEED
    for i in range(101):
        # 方眼紙
        stroke(63)
        line(i * 10, 0, i * 10, height)
        line(0, i * 10, width, i * 10)
    # ベジェ曲線
    translate(250, 250)
    stroke(255)
    vertex_point_1 = PVector(250, 0)
    vertex_point_2 = PVector(250, 500)
    add_value = count
    control_point_1 = PVector.add(
        vertex_point_1,
        PVector(add_value, add_value)
    )
    control_point_2 = PVector.add(
        vertex_point_2,
        PVector(-add_value, -add_value)
    )
    bezier(
        vertex_point_1.x, vertex_point_1.y,
        control_point_1.x, control_point_1.y,
        control_point_2.x, control_point_2.y,
        vertex_point_2.x, vertex_point_2.y
    )
    stroke(255, 255, 0)
    line(vertex_point_1.x, vertex_point_1.y, control_point_1.x, control_point_1.y)
    line(vertex_point_2.x, vertex_point_2.y, control_point_2.x, control_point_2.y)
    print('control point length:' + str(add_value))


def mousePressed():
    global is_countable
    is_countable = not is_countable


def keyPressed():
    if key == 's':
        file_name = os.path.basename(__file__).split('.')[0]
        print('{}.png'.format(file_name))
        save('output_images/{}.png'.format(file_name))
