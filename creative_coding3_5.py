"""
地球儀（テキスチャースフィア）
"""
import p3d_util

if False:
    from lib.Processing3 import *
import os

SIZE_X = 1200
SIZE_Y = 750
RADIUS = 300
HEIGHT = 100
globe = None


def setup():
    global globe
    size(SIZE_X, SIZE_Y, P3D)
    noStroke()
    img = loadImage("earth.png")
    globe = createShape(SPHERE, RADIUS)
    globe.setTexture(img)


def draw():
    p3d_util.test_lighting()
    translate(width / 2, height / 2)
    rotateX(map(mouseY, 0, height, -PI, PI))
    rotateY(map(mouseX, 0, width, -PI, PI))
    shape(globe, 0, 0)


def keyPressed():
    if key == 's':
        file_name = os.path.basename(__file__).split('.')[0]
        print('{}.png'.format(file_name))
        save('output_images/{}.png'.format(file_name))
