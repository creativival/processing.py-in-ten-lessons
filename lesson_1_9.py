"""
サイクロイド曲線
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
    # 三角関数
    for i in range(frameCount):
        angle = i / 60.0
        draw_point_angle = -angle - PI / 2.0
        circle_center = PVector(angle * RADIUS, RADIUS)
        draw_point = PVector.add(circle_center,
                                 PVector(RADIUS * cos(draw_point_angle), RADIUS * sin(draw_point_angle)))
        _angle = (i - 1) / 60.0
        _draw_point_angle = -_angle - PI / 2.0
        _circle_center = PVector(_angle * RADIUS, RADIUS)
        _draw_point = PVector.add(_circle_center,
                                 PVector(RADIUS * cos(_draw_point_angle), RADIUS * sin(_draw_point_angle)))
        noFill()
        stroke(255, 0, 0)
        line(_draw_point.x, _draw_point.y, draw_point.x, draw_point.y)

        if i >= frameCount - 1:
            noFill()
            stroke(255)
            ellipse(circle_center.x, circle_center.y, RADIUS * 2, RADIUS * 2)
            stroke(255, 255, 0)
            line(circle_center.x, circle_center.y, draw_point.x, draw_point.y)
            fill(255, 0, 0)
            noStroke()
            ellipse(draw_point.x, draw_point.y, 4, 4)
            print(degrees(angle))
            print(circle_center)
