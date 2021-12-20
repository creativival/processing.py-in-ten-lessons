"""
たくさんのハートマーク
"""

if False:
    from lib.Processing3 import *

BACKGROUND_COLOR = color(0, 44, 77)
SIZE_X = 800
SIZE_Y = 600


def setup():
    size(SIZE_X, SIZE_Y)
    colorMode(HSB, 360, 100, 100)
    background(BACKGROUND_COLOR)
    for i in range(100):
        p = PVector(random(width), random(height))
        angle = map(random(1), 0, 1, 0, TWO_PI)
        mark_size = random(10, 30)
        heart_color = random(20)
        draw_mark(p, angle, mark_size, heart_color)


def draw_mark(p, angle, mark_size, heart_color):
    fill(heart_color, 100, 100)
    strokeWeight(1)
    stroke(heart_color, 100, 100)
    pushMatrix()
    translate(p.x, p.y)
    rotate(angle)
    vt1 = PVector(mark_size / 2, mark_size)
    vt2 = PVector(mark_size / 4, mark_size * 3 / 4)
    vt3 = PVector(mark_size / 2, mark_size / 4)
    cp1 = PVector(-mark_size / 4, mark_size / 4)
    cp2 = PVector(mark_size / 4, -mark_size / 4)
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
        mirror_x(vt2.x, mark_size),
        vt2.y,
        mirror_x(cp1.x, mark_size),
        cp1.y,
        mirror_x(cp2.x, mark_size),
        cp2.y,
        mirror_x(vt3.x, mark_size),
        vt3.y
    )
    quad(
        vt1.x,
        vt1.y,
        vt2.x,
        vt2.y,
        vt3.x,
        vt3.y,
        mirror_x(vt2.x, mark_size),
        vt2.y
    )
    popMatrix()


def mirror_x(x, mark_size):
    return mark_size - x
