"""
軸の回転
"""
import p3d_util

if False:
    from lib.Processing3 import *
import os

SIZE_X = 1200
SIZE_Y = 750
rotate = PVector(0, 0, 0)


def setup():
    size(SIZE_X, SIZE_Y, P3D)
    camera(0, 0, 1000, width / 2, height / 2, 0, 0, 1, 0)


def draw():
    background("#E7ECF2")
    fill(0)
    text(str(degrees(rotate.x)), 20, 100)
    text(str(degrees(rotate.y)), 20, 140)
    text(str(degrees(rotate.z)), 20, 180)
    noFill()
    pushMatrix()
    translate(width / 2, height / 2, 0)
    p3d_util.draw_axes(4)
    rotateX(rotate.x)
    rotateY(rotate.y)
    rotateZ(rotate.z)
    p3d_util.draw_axes(2)
    popMatrix()


def keyPressed():
    if key == 'x':
        rotate.x += 0.01
    elif key == 'y':
        rotate.y += 0.01
    elif key == 'z':
        rotate.z += 0.01
    elif key == 'r':
        rotate.x = 0
        rotate.y = 0
        rotate.z = 0
    if key == 's':
        file_name = os.path.basename(__file__).split('.')[0]
        print('{}.png'.format(file_name))
        save('output_images/{}.png'.format(file_name))
