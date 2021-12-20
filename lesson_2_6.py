"""
落下するハートマーク
"""

if False:
    from lib.Processing3 import *

BACKGROUND_COLOR = color(0, 44, 77)
SIZE_X = 800
SIZE_Y = 600
FALL_SPEED = PVector(0, 0.1)
marks = []


def setup():
    size(SIZE_X, SIZE_Y)
    colorMode(HSB, 360, 100, 100)
    blendMode(ADD)
    for i in range(100):
        p = PVector(random(width), random(height))
        angle = map(random(1), 0, 1, 0, TWO_PI)
        mark_size = random(10, 30)
        mark_color = random(20)
        mark = HeartMark(p, angle, mark_size, mark_color)
        marks.append(mark)


def draw():
    background(BACKGROUND_COLOR)
    for m in marks:
        m.draw()
        m.update()
        m.through_walls()


class HeartMark:
    def __init__(self, p, angle, mark_size, mark_color):
        self.position = p
        self.angle = angle
        self.mark_size = mark_size
        self.mark_color = mark_color

    def draw(self):
        fill(self.mark_color, 100, 100)
        # strokeWeight(1)
        # stroke(self.mark_color, 100, 100)
        noStroke()
        pushMatrix()
        translate(self.position.x, self.position.y)
        rotate(self.angle)
        vt1 = PVector(self.mark_size / 2, self.mark_size)
        vt2 = PVector(self.mark_size / 4, self.mark_size * 3 / 4)
        vt3 = PVector(self.mark_size / 2, self.mark_size / 4)
        cp1 = PVector(-self.mark_size / 4, self.mark_size / 4)
        cp2 = PVector(self.mark_size / 4, -self.mark_size / 4)
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
            mirror_x(vt2.x, self.mark_size),
            vt2.y,
            mirror_x(cp1.x, self.mark_size),
            cp1.y,
            mirror_x(cp2.x, self.mark_size),
            cp2.y,
            mirror_x(vt3.x, self.mark_size),
            vt3.y
        )
        quad(
            vt1.x,
            vt1.y,
            vt2.x,
            vt2.y,
            vt3.x,
            vt3.y,
            mirror_x(vt2.x, self.mark_size),
            vt2.y
        )
        popMatrix()

    def update(self):
        speed = PVector.mult(FALL_SPEED, self.mark_size)
        speed.y += noise(1)
        self.position = PVector.add(self.position, speed)
        self.angle += random(PI/180)
        self.mark_size *= random(1 / 1.01, 1.01)

    def reset_size(self):
        if self.mark_size < 5 or 40 < self.mark_size:
            self.mark_size = random(10,20)

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
