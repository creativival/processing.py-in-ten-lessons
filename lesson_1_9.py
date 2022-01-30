"""
サイクロイド曲線
"""

if False:
    from lib.Processing3 import *
import os

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
    # サイクロイド曲線
    for i in range(frameCount):
        angle = i / 60.0
        circle_angle = -angle - PI / 2.0
        circle_center = PVector(angle * RADIUS, RADIUS)
        draw_point = PVector.add(circle_center,
                                 PVector(RADIUS * cos(circle_angle), RADIUS * sin(circle_angle)))
        _angle = (i - 1) / 60.0
        _circle_angle = -_angle - PI / 2.0
        _circle_center = PVector(_angle * RADIUS, RADIUS)
        _draw_point = PVector.add(_circle_center,
                                 PVector(RADIUS * cos(_circle_angle), RADIUS * sin(_circle_angle)))
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


def keyPressed():
    if key == 's':
        file_name = os.path.basename(__file__).split('.')[0]
        print('{}.png'.format(file_name))
        save('output_images/{}.png'.format(file_name))
