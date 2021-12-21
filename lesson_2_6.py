"""
落下するマーク
"""

if False:
    from lib.Processing3 import *
import util

BACKGROUND_COLOR = color(0, 44, 77)
SIZE_X = 800
SIZE_Y = 600
MARK_TYPE = 'star'  # heart, leaf, diamond or star
MIN_MARK_SIZE = 10
MAX_MARK_SIZE = 30
FALL_SPEED = PVector(0, 0.1)
marks = []


def setup():
    size(SIZE_X, SIZE_Y)
    colorMode(HSB, 360, 100, 100)
    blendMode(ADD)
    for i in range(100):
        p = PVector(random(width), random(height))
        angle = map(random(1), 0, 1, 0, TWO_PI)
        mark_size = random(MIN_MARK_SIZE, MAX_MARK_SIZE)
        mark = HeartMark(p, angle, mark_size, MARK_TYPE)
        marks.append(mark)


def draw():
    background(BACKGROUND_COLOR)
    for m in marks:
        m.draw()
        m.update()
        m.through_walls()


class HeartMark:
    def __init__(self, p, angle, mark_size, mark_type):
        self.position = p
        self.angle = angle
        self.mark_size = mark_size
        self.mark_type = mark_type

    def draw(self):
        util.draw_mark(self.position, self.angle, self.mark_size, MARK_TYPE)

    def update(self):
        speed = PVector.mult(FALL_SPEED, self.mark_size)
        speed.y += noise(1)
        self.position = PVector.add(self.position, speed)
        self.angle += random(-PI / 90, PI / 90)
        self.mark_size *= random(1 / 1.01, 1.01)

    def reset_size(self):
        if self.mark_size < MIN_MARK_SIZE / 2 or MAX_MARK_SIZE * 1.5 < self.mark_size:
            self.mark_size = random(10, 20)

    def through_walls(self):
        if self.position.x < 0:
            self.position.x = SIZE_X
            self.reset_size()
        if SIZE_X < self.position.x:
            self.position.x = 0
            self.reset_size()
        if self.position.y < 0:
            self.position.x = random(width)
            self.position.y = SIZE_Y
            self.reset_size()
        if SIZE_Y < self.position.y:
            self.position.x = random(width)
            self.position.y = 0
            self.reset_size()


def mirror_x(x, mark_size):
    return mark_size - x
