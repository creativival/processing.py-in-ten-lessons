"""
曲線 ハートマーク
"""

if False:
    from lib.Processing3 import *

HEART_COLOR = color(255, 0, 0)
BACKGROUND_COLOR = color(0, 44, 77)
SIZE = 50


def setup():
    size(SIZE, SIZE)
    # grid = loadImage('grid.png')
    # image(grid, 0, 0)
    background(BACKGROUND_COLOR)
    fill(HEART_COLOR)
    strokeWeight(1)
    stroke(HEART_COLOR)
    vt1 = PVector(SIZE / 2, SIZE)
    vt2 = PVector(SIZE / 4, SIZE * 3 / 4)
    vt3 = PVector(SIZE / 2, SIZE / 4)
    cp3 = PVector(-SIZE / 4, SIZE / 4)
    cp4 = PVector(SIZE / 4, -SIZE / 4)
    bezier(
        vt2.x,
        vt2.y,
        cp3.x,
        cp3.y,
        cp4.x,
        cp4.y,
        vt3.x,
        vt3.y
    )
    bezier(
        mirror_x(vt2.x),
        vt2.y,
        mirror_x(cp3.x),
        cp3.y,
        mirror_x(cp4.x),
        cp4.y,
        mirror_x(vt3.x),
        vt3.y
    )
    quad(
        vt1.x,
        vt1.y,
        vt2.x,
        vt2.y,
        vt3.x,
        vt3.y,
        mirror_x(vt2.x),
        vt2.y
    )


def mirror_x(x):
    return SIZE - x
