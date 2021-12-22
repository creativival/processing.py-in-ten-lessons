"""
角度（ラジアン）
"""

if False:
    from lib.Processing3 import *

BACKGROUND_COLOR = color(0, 44, 77)
DEGREE_ANGLES = []
RADIAN_ANGLES = []
for i in range(13):
    DEGREE_ANGLES.append(i * 30)
    RADIAN_ANGLES.append(i * PI / 6)
RADIUS = 300


def setup():
    size(1000, 1000)
    # textAlign(CENTER, CENTER)
    textSize(20)
    background(BACKGROUND_COLOR)
    translate(width / 2, height / 2)
    stroke(0, 255, 0)
    line(-500, 0, 500, 0)
    line(0, -500, 0, 500)
    # 角度（ラジアン）
    for i, a in enumerate(RADIAN_ANGLES):
        angle = a
        noFill()
        stroke(255)
        strokeWeight(2)
        radius = RADIUS + i * 20
        arc(0, 0, radius, radius, 0, angle)
        fill(255, 0, 0)
        noStroke()
        text(str(a), radius * cos(angle) / 2.0, radius * sin(angle) / 2.0)
