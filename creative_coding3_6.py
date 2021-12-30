"""
地球儀（テキスチャースフィア）
"""
import p3d_util

if False:
    from lib.Processing3 import *

SIZE_X = 1200
SIZE_Y = 750
details = [3, 4, 6]


def setup():
    global globe
    size(SIZE_X, SIZE_Y, P3D)
    colorMode(HSB, 360, 100, 100)
    background("#E7ECF2")
    draw_cylinders()


def draw():
    pass


def mousePressed():
    background("#E7ECF2")
    draw_cylinders()


def draw_cylinders():
    lights()

    for i in range(50):
        cylinder_radius = random(50, 100)
        cylinder_height = cylinder_radius / 2
        cylinder_color = color(random(360), 100, 100)
        cylinder_detail = details[int(random(len(details)))]
        pushMatrix()
        translate(random(width), random(height), random(-100))
        rotateX(random(TWO_PI))
        rotateY(random(TWO_PI))
        rotateZ(random(TWO_PI))
        cylinder = p3d_util.Cylinder(
            cylinder_radius,
            cylinder_height,
            cylinder_detail,
            cylinder_color,
            0
        )
        cylinder.draw()
        popMatrix()
