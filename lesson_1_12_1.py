"""
スピログラフ（玩具）実行が遅くなるので改良
"""

if False:
    from lib.Processing3 import *
import util

BACKGROUND_COLOR = color(0, 44, 77)
BASE_CIRCLE_RADIUS = 300
RADIUS = 105
DRAW_RADIUS = 90
draw_points = []


def setup():
    size(1000, 1000)
    # textAlign(CENTER, CENTER)
    textSize(20)
    background(BACKGROUND_COLOR)
    translate(width / 2, height / 2)
    noFill()
    stroke(0, 255, 0)
    line(-2000, 0, 2000, 0)
    line(0, -2000, 0, 2000)
    stroke(127)
    ellipse(0, 0, BASE_CIRCLE_RADIUS * 2, BASE_CIRCLE_RADIUS * 2)
    # # スピログラフ（アニメーションなし）
    # for i in range(10000):
    #     base_circle_angle = i / 60.0
    #     circle_angle = -base_circle_angle * BASE_CIRCLE_RADIUS / RADIUS + PI
    #     circle_center = PVector(
    #         (BASE_CIRCLE_RADIUS - RADIUS) * cos(base_circle_angle),
    #         (BASE_CIRCLE_RADIUS - RADIUS) * sin(base_circle_angle),
    #     )
    #     draw_point = PVector.add(
    #         circle_center,
    #         PVector(DRAW_RADIUS * cos(circle_angle), DRAW_RADIUS * sin(circle_angle))
    #     )
    #     _base_circle_angle = (i - 1) / 60.0
    #     _circle_angle = -_base_circle_angle * BASE_CIRCLE_RADIUS / RADIUS + PI
    #     _circle_center = PVector(
    #         (BASE_CIRCLE_RADIUS - RADIUS) * cos(_base_circle_angle),
    #         (BASE_CIRCLE_RADIUS - RADIUS) * sin(_base_circle_angle),
    #     )
    #     _draw_point = PVector.add(
    #         _circle_center,
    #         PVector(DRAW_RADIUS * cos(_circle_angle), DRAW_RADIUS * sin(_circle_angle))
    #     )
    #     noFill()
    #     stroke(255, 0, 0)
    #     line(_draw_point.x, _draw_point.y, draw_point.x, draw_point.y)


def draw():
    background(BACKGROUND_COLOR)
    translate(width / 2, height / 2)
    noFill()
    stroke(0, 255, 0)
    line(-2000, 0, 2000, 0)
    line(0, -2000, 0, 2000)
    stroke(127)
    ellipse(0, 0, BASE_CIRCLE_RADIUS * 2, BASE_CIRCLE_RADIUS * 2)
    # スピログラフ（アニメーション）
    base_circle_angle = frameCount / 20.0
    circle_angle = -base_circle_angle * BASE_CIRCLE_RADIUS / RADIUS + PI
    circle_center = PVector(
        (BASE_CIRCLE_RADIUS - RADIUS) * cos(base_circle_angle),
        (BASE_CIRCLE_RADIUS - RADIUS) * sin(base_circle_angle),
    )
    draw_point = PVector.add(
        circle_center,
        PVector(DRAW_RADIUS * cos(circle_angle), DRAW_RADIUS * sin(circle_angle))
    )
    draw_points.append(draw_point)

    noFill()
    stroke(255, 0, 0)
    if len(draw_points) >= 2:
        for i in range(len(draw_points) - 1):
            print(i)
            print(draw_points[i])
            line(draw_points[i].x, draw_points[i].y, draw_points[i + 1].x, draw_points[i + 1].y)
    stroke(255)
    ellipse(circle_center.x, circle_center.y, RADIUS * 2, RADIUS * 2)
    stroke(255, 255, 0)
    line(circle_center.x, circle_center.y, draw_point.x, draw_point.y)
    fill(255, 0, 0)
    noStroke()
    ellipse(draw_point.x, draw_point.y, 4, 4)

    # MIN_FRAME = 360
    # MAX_FRAME = 540
    # util.save_frame(MIN_FRAME, MAX_FRAME)
