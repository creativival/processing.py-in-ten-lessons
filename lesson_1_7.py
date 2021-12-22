"""
三角関数（サイン, コサイン、タンジェント）
"""

if False:
    from lib.Processing3 import *

BACKGROUND_COLOR = color(0, 44, 77)
RADIUS = 100


def setup():
    size(1000, 1000)
    # textAlign(CENTER, CENTER)
    textSize(20)
    background(BACKGROUND_COLOR)
    translate(width / 2, height / 2)
    stroke(0, 255, 0)
    line(-2000, 0, 2000, 0)
    line(0, -2000, 0, 2000)
    # 三角関数
    for i in range(-64, 65):
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
        stroke(0, 255, 255)
        fill(0, 255, 255)
        ellipse(x, y_tan, 2, 2)
        if y_tan < 1000 and _y_tan < 1000:
            line(_x, _y_tan, x, y_tan)
        # text(str(a), radius * cos(angle) / 2.0, radius * sin(angle) / 2.0)
