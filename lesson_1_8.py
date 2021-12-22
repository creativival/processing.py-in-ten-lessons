"""
三角関数（サイン, コサイン、タンジェント）
"""

if False:
    from lib.Processing3 import *

BACKGROUND_COLOR = color(0, 44, 77)
RADIUS = 100


def setup():
    size(1800, 1000)
    # textAlign(CENTER, CENTER)
    textSize(20)


def draw():
    background(BACKGROUND_COLOR)
    translate(100, height / 2)
    noFill()
    stroke(0, 255, 0)
    line(-2000, 0, 2000, 0)
    line(0, -2000, 0, 2000)
    stroke(127)
    ellipse(0, 0, RADIUS * 2, RADIUS * 2)
    # 三角関数
    repeat_num = int(frameCount / 60)
    for i in range(repeat_num):
        x = i * 8
        angle = i * PI / 60
        y_sin = RADIUS * sin(angle)
        y_cos = RADIUS * cos(angle)
        y_tan = RADIUS * tan(angle)
        _x = (i - 1) * 8
        _angle = (i - 1) * PI / 60
        _y_sin = RADIUS * sin(_angle)
        _y_cos = RADIUS * cos(_angle)
        _y_tan = RADIUS * tan(_angle)
        stroke(255, 0, 0)
        fill(255, 0, 0)
        ellipse(x, y_sin, 2, 2)
        line(_x, _y_sin, x, y_sin)
        stroke(255, 255, 0)
        fill(255, 255, 0)
        ellipse(x, y_cos, 2, 2)
        line(_x, _y_cos, x, y_cos)
        # stroke(0, 255, 255)
        # fill(0, 255, 255)
        # ellipse(x, y_tan, 2, 2)
        # if y_tan < 1000 and _y_tan < 1000:
        #     line(_x, _y_tan, x, y_tan)

        if i >= repeat_num - 1:
            noFill()
            stroke(255)
            arc(0, 0, RADIUS * 2, RADIUS * 2, 0, angle, PIE)
            stroke(255, 0, 0)
            line(y_cos, y_sin, y_cos, 0)
            line(x - 1, 0, x - 1, y_sin)
            stroke(255, 255, 0)
            line(y_cos, y_sin, 0, y_sin)
            line(x + 1, 0, x + 1, y_cos)
