"""
曲線 ハートマーク
"""

if False:
    from lib.Processing3 import *

HEART_COLOR = color(255, 0, 0)
BACKGROUND_COLOR = color(0, 44, 77)
SIZE = 400


def setup():
    size(SIZE, SIZE)
    grid = loadImage('grid.png')
    image(grid, 0, 0)
    # background(BACKGROUND_COLOR)
    fill(HEART_COLOR)
    strokeWeight(1)
    stroke(HEART_COLOR)
    # noStroke()
    vt1 = PVector(SIZE / 2, SIZE)
    vt2 = PVector(SIZE / 4, SIZE * 3 / 4)
    vt3 = PVector(SIZE / 2, SIZE / 4)
    cp1 = PVector(-SIZE / 4, SIZE / 4)
    cp2 = PVector(SIZE / 4, -SIZE / 4)
    bezier(
        vt2.x,
        vt2.y,
        cp1.x,
        cp1.y,
        cp2.x,
        cp2.y,
        vt3.x,
        vt3.y
    )
    bezier(
        mirror_x(vt2.x, SIZE),
        vt2.y,
        mirror_x(cp1.x, SIZE),
        cp1.y,
        mirror_x(cp2.x, SIZE),
        cp2.y,
        mirror_x(vt3.x, SIZE),
        vt3.y
    )
    quad(
        vt1.x,
        vt1.y,
        vt2.x,
        vt2.y,
        vt3.x,
        vt3.y,
        mirror_x(vt2.x, SIZE),
        vt2.y
    )
    stroke(255, 255, 0)
    line(vt2.x, vt2.y, cp1.x, cp1.y)
    line(vt3.x, vt3.y, cp2.x, cp2.y)
    line(
        mirror_x(vt2.x, SIZE),
        vt2.y,
        mirror_x(cp1.x, SIZE),
        cp1.y)
    line(
        mirror_x(vt3.x, SIZE),
        vt3.y,
        mirror_x(cp2.x, SIZE),
        cp2.y
    )


def mirror_x(x, mark_size):
    return mark_size - x
