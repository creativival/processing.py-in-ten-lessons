"""
円柱
"""
if False:
    from lib.Processing3 import *
import os
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
    p3d_util.test_drawing_cylinder(RADIUS, HEIGHT, NUMBER_OF_VERTICES)


def keyPressed():
    if key == 's':
        file_name = os.path.basename(__file__).split('.')[0]
        print('{}.png'.format(file_name))
        save('output_images/{}.png'.format(file_name))
