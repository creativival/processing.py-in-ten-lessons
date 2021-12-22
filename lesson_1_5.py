"""
角度（度）
"""

if False:
    from lib.Processing3 import *

BACKGROUND_COLOR = color(0, 44, 77)
# DEGREE_ANGLES = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 360]
# RADIAN_ANGLES = [PI / 6, PI / 3, PI / 2, PI * 2 / 3, PI * 5 / 6, PI, PI * 7 / 6, PI * 4 / 3, PI * 3 / 2, PI * 5 / 3,
#                  PI * 11 / 6, PI * 2]
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
    # 角度（度）
    for i, a in enumerate(DEGREE_ANGLES):
        angle = radians(a)
        noFill()
        stroke(255)
        strokeWeight(2)
        radius = RADIUS + i * 20
        arc(0, 0, radius, radius, 0, angle)
        fill(255, 0, 0)
        noStroke()
        text(str(a), radius * cos(angle) / 2.0, radius * sin(angle) / 2.0)
