"""
落下するマーク
"""

if False:
    from lib.Processing3 import *
import util

"""
heart
leaf
diamond
shine
five_pointed_star
six_pointed_star
gear
"""
SETTINGS = {
    'type': 'gear',
    'number_of_marks': 50,
    'min_size': 10,
    'max_size': 30,
    'min_color': 0,
    'max_color': 360,
    'fall_speed': PVector(0, 0.1)
}
BACKGROUND_COLOR = color(0, 44, 77)
SIZE_X = 800
SIZE_Y = 600
marks = []


def setup():
    size(SIZE_X, SIZE_Y)
    colorMode(HSB, 360, 100, 100)
    blendMode(ADD)
    for i in range(SETTINGS['number_of_marks']):
        p = PVector(random(width), random(height))
        angle = map(random(1), 0, 1, 0, TWO_PI)
        mark_size = random(SETTINGS['min_size'], SETTINGS['max_size'])
        mark_color = random(SETTINGS['min_color'], SETTINGS['max_color'])
        mark = util.Mark(p, angle, mark_size, mark_color, SETTINGS)
        marks.append(mark)


def draw():
    background(BACKGROUND_COLOR)
    for m in marks:
        m.draw()
        m.update()
        m.through_walls()
