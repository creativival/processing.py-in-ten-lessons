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


def draw():
    background(255)
    p3d_util.test_drawing_cylinder(RADIUS, HEIGHT, NUMBER_OF_VERTICES)
