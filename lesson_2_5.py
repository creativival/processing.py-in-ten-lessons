"""
たくさんのマーク
"""

if False:
    from lib.Processing3 import *
import os
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
MARK_TYPE = 'gear'
MIN_COLOR = 0
MAX_COLOR = 360
BACKGROUND_COLOR = color(0, 44, 77)
mark_size_X = 800
mark_size_Y = 600
MIN_MARK_SIZE = 20
MAX_MARK_SIZE = 40


def setup():
    size(mark_size_X, mark_size_Y)
    colorMode(HSB, 360, 100, 100)
    background(BACKGROUND_COLOR)
    for i in range(100):
        p = PVector(random(width), random(height))
        angle = map(random(1), 0, 1, 0, TWO_PI)
        mark_size = random(MIN_MARK_SIZE, MAX_MARK_SIZE)
        mark_color = random(MIN_COLOR, MAX_COLOR)
        util.draw_mark(p, angle, mark_size, mark_color, MARK_TYPE)
        print(p, angle, mark_size, MARK_TYPE)


def draw():
    pass


def keyPressed():
    if key == 's':
        file_name = os.path.basename(__file__).split('.')[0]
        print('{}.png'.format(file_name))
        save('output_images/{}.png'.format(file_name))
