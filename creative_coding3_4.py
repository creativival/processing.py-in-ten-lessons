"""
円柱
"""
if False:
    from lib.Processing3 import *
import p3d_util

SIZE_X = 1200
SIZE_Y = 750
RADIUS = 300
HEIGHT = 100
NUMBER_OF_VERTICES = 64  # 64以上は円柱に変換


def setup():
    size(SIZE_X, SIZE_Y, P3D)


def draw():
    background(255)
    # 錐
    pushMatrix()
    fill(0, 255, 0)
    translate(width / 2, height / 3)
    rotateX(map(mouseY, 0, height, -PI, PI))
    rotateY(map(mouseX, 0, width, -PI, PI))
    cylinder = p3d_util.Cylinder(RADIUS, HEIGHT, NUMBER_OF_VERTICES, 1)
    cylinder.draw()
    popMatrix()
    # 柱
    pushMatrix()
    fill(255, 0, 0)
    translate(width / 2, height * 3 / 4)
    rotateX(map(mouseY, 0, height, -PI, PI))
    rotateY(map(mouseX, 0, width, -PI, PI))
    cylinder = p3d_util.Cylinder(RADIUS, HEIGHT, NUMBER_OF_VERTICES, 0)
    cylinder.draw()
    popMatrix()
