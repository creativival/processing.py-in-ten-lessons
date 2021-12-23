"""
ダンシング
"""

if False:
    from lib.Processing3 import *
import util

BACKGROUND_COLOR = color(0, 44, 77)
SIZE_X = 800
SIZE_Y = 600
MIN_IMG_NUM = 1
MAX_IMG_NUM = 31
BASE_FILE_NAME = 'action'
DANCE_SPEED = 10
images = []
img_num = 0
dancers = [
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
]


def setup():
    size(SIZE_X, SIZE_Y)
    colorMode(HSB, 360, 100, 100)
    # blendMode(ADD)
    for i in range(MIN_IMG_NUM, MAX_IMG_NUM + 1):
        if i <= 9:
            num = '00' + str(i)
        elif i <= 99:
            num = '0' + str(i)
        else:
            num = str(i)
        file_name = '{}_{}.png'.format(BASE_FILE_NAME, num)
        img = loadImage(file_name)
        images.append(img)
        print(file_name)


def draw():
    global img_num
    background(BACKGROUND_COLOR)
    if frameCount % int(20.0 / DANCE_SPEED) == 0:
        img_num = int(random(len(images)))
        print(img_num)

    for dancer in dancers:
        img_size = PVector(
            width * dancer['ratio'],
            height * dancer['ratio']
        )
        dancer_position = PVector(
            (1 - dancer['ratio']) * width / 2.0 + dancer['x'],
            (1 - dancer['ratio']) * height / 2.0  + dancer['y'],
        )
        image(images[img_num], dancer_position.x, dancer_position.y, img_size.x, img_size.y)
