"""
虹（分割数を指定する）
"""

if False:
    from lib.Processing3 import *
import os

BACKGROUND_COLOR = color(0,44,77)
DIVISION_NUMBER = 5  # 分割数


def setup():
    colorMode(HSB, 360, 100, 100)
    noStroke()
    size(1000, 1000)
    background(BACKGROUND_COLOR)
    # 虹
    for i in range(int(DIVISION_NUMBER * 12 / 7)):
        if i >= DIVISION_NUMBER:
            fill(BACKGROUND_COLOR)
        else:
            fill(map(i, 0, DIVISION_NUMBER, 0, 300), 100, 100)
        radius = (350 / DIVISION_NUMBER) * (DIVISION_NUMBER * 12 / 7 - i)
        ellipse(width / 2, height / 2, radius, radius)
    rect(0, height / 2, width, height / 2)
    print('hello world')


def draw():
    pass


def keyPressed():
    if key == 's':
        file_name = os.path.basename(__file__).split('.')[0]
        print('{}.png'.format(file_name))
        save('output_images/{}.png'.format(file_name))
