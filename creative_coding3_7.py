"""
たくさんのシリンダー（アニメーション）
"""
import p3d_util

if False:
    from lib.Processing3 import *

SIZE_X = 1200
SIZE_Y = 750
details = [3, 4, 6]
cylinders = []


def setup():
    global globe
    size(SIZE_X, SIZE_Y, P3D)
    colorMode(HSB, 360, 100, 100)
    for i in range(50):
        cylinder_radius = random(50, 100)
        cylinder_height = cylinder_radius / 2
        cylinder_color = color(random(360), 100, 100)
        cylinder_detail = details[int(random(len(details)))]
        cylinder_position = PVector(
            random(width),
            random(height),
            random(-100)
        )
        cylinder_rotate = PVector(
            random(TWO_PI),
            random(TWO_PI),
            random(TWO_PI)
        )
        cylinder = p3d_util.Cylinder(
            cylinder_position,
            cylinder_rotate,
            cylinder_radius,
            cylinder_height,
            cylinder_detail,
            cylinder_color,
            0
        )
        cylinders.append(cylinder)


def draw():
    background("#E7ECF2")
    lights()
    for cylinder in cylinders:
        # cylinder.rotate.y += frameCount * 0.0001
        cylinder.update()
        cylinder.draw()


