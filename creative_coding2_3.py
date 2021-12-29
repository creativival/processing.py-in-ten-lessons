"""
無限大（アニメーション）カラー
"""
if False:
    from lib.Processing3 import *

SIZE_X = 1200
SIZE_Y = 750
BASE_LENGTH = 300
NUMBER_OF_PARTICLES = 500
particles = []
palette = ["#04E762", "#F5B700", "#DC0073", "#008BF8"]



def setup():
    size(SIZE_X, SIZE_Y)
    for i in range(NUMBER_OF_PARTICLES):
        particles.append(Particle())


def draw():
    background(255)
    translate(width / 2, height / 2)
    for particle in particles:
        particle.draw()
        particle.update()


class Particle:
    def __init__(self):
        self.angle = radians(random(0, 360))
        self.step_angle = radians(random(0.25, 2))
        self.length = BASE_LENGTH + random(-70,70)
        self.color_id = int(random(len(palette)))
        self.diameter = random(5, 20)


    def draw(self):
        noStroke()
        fill(palette[self.color_id])
        x = self.length * sqrt(2) * cos(self.angle) / (sq(sin(self.angle)) + 1)
        y = self.length * sqrt(2) * cos(self.angle) * sin(self.angle) / (sq(sin(self.angle)) + 1)
        ellipse(x, y, self.diameter, self.diameter)

    def update(self):
        self.angle += self.step_angle



