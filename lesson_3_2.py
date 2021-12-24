"""
ダンシング（クラスを使用）
"""

if False:
    from lib.Processing3 import *
import util

SETTINGS = {
    'min_img_num': 1,
    'max_img_num': 31,
    'base_file_name': 'action',
    'speed': 5,
    'dancers': [
        {
            'ratio': 1.0 / 2.0,
            'x': -300,
            'y': -200,
        },
        {
            'ratio': 1.0 / 2.0,
            'x': 0,
            'y': -200,
        },
        {
            'ratio': 1.0 / 2.0,
            'x': 300,
            'y': -200,
        },
        {
            'ratio': 2.0 / 3.0,
            'x': -150,
            'y': -100,
        },
        {
            'ratio': 2.0 / 3.0,
            'x': 150,
            'y': -100,
        },
        {
            'ratio': 1,
            'x': 0,
            'y': 0,
        },
    ],
}
BACKGROUND_COLOR = color(0, 44, 77)
SIZE_X = 800
SIZE_Y = 600
dancer = None


def setup():
    global dancer
    size(SIZE_X, SIZE_Y)
    colorMode(HSB, 360, 100, 100)
    dancer = util.Dancer(SETTINGS)


def draw():
    background(BACKGROUND_COLOR)
    dancer.draw()
