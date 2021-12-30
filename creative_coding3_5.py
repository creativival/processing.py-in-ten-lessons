"""
地球儀（テキスチャースフィア）
"""
if False:
    from lib.Processing3 import *

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
    translate(width / 2, height / 2)
    rotateX(map(mouseY, 0, height, -PI, PI))
    rotateY(map(mouseX, 0, width, -PI, PI))
    shape(globe, 0, 0)
