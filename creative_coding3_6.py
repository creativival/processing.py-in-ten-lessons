"""
たくさんのシリンダー
"""
import p3d_util

if False:
    from lib.Processing3 import *
import os

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
        cylinder.draw()


def keyPressed():
    if key == 's':
        file_name = os.path.basename(__file__).split('.')[0]
        print('{}.png'.format(file_name))
        save('output_images/{}.png'.format(file_name))
