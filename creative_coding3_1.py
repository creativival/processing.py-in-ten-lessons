"""
三角柱
"""
if False:
    from lib.Processing3 import *
import p3d_util

SIZE_X = 1200
SIZE_Y = 750
RADIUS = 300
HEIGHT = 100
NUMBER_OF_VERTICES = 3


def setup():
    size(SIZE_X, SIZE_Y, P3D)
    stroke(127)


def draw():
    background(255)
    pushMatrix()
    fill(255, 0, 0, 127)
    translate(width / 2, height / 4)
    rotateY(frameCount * 0.01)
    # box(150, 150, 150)
    cylinder = p3d_util.Cylinder(RADIUS, HEIGHT, NUMBER_OF_VERTICES, 0)
    cylinder.draw()
    popMatrix()
    pushMatrix()
    fill(0, 255, 0, 127)
    translate(width / 2, height * 3/ 4)
    rotateY(frameCount * 0.01)
    # box(150, 150, 150)
    cylinder = p3d_util.Cylinder(RADIUS, HEIGHT, NUMBER_OF_VERTICES, 1)
    cylinder.draw()
    popMatrix()