"""
ベジェ曲線による円弧の近似
半径1の円の時、0.55228474983
https://cat-in-136.github.io/2014/03/bezier-1-kappa.html
半径500の円の時、276.142374915
"""

if False:
    from lib.Processing3 import *
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
        ellipse(750, 250, 1000, 1000)
    # ベジェ曲線
    translate(250, 250)
    stroke(255)
    vertex_point_1 = PVector(0, 0)
    vertex_point_2 = PVector(500, 500)
    add_value = count
    control_point_1 = PVector.add(
        vertex_point_1,
        PVector(0, add_value)
    )
    control_point_2 = PVector.add(
        vertex_point_2,
        PVector(-add_value, 0)
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
