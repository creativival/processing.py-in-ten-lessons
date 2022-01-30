"""
ダンシング
"""

if False:
    from lib.Processing3 import *
import os
import util

SETTINGS = {
    'min_img_num': 1,
    'max_img_num': 31,
    'base_file_name': 'action',
    'speed': 10,
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
images = []
img_num = 0


def setup():
    size(SIZE_X, SIZE_Y)
    colorMode(HSB, 360, 100, 100)
    # blendMode(ADD)
    for i in range(SETTINGS['min_img_num'], SETTINGS['max_img_num'] + 1):
        # if i <= 9:
        #     num = '00' + str(i)
        # elif i <= 99:
        #     num = '0' + str(i)
        # else:
        #     num = str(i)
        num = '{0:03d}'.format(i)
        file_name = '{}_{}.png'.format(SETTINGS['base_file_name'], num)
        img = loadImage(file_name)
        images.append(img)
        print(file_name)


def draw():
    global img_num
    background(BACKGROUND_COLOR)
    if frameCount % int(20.0 / SETTINGS['speed']) == 0:
        img_num = int(random(len(images)))
        print(img_num)

    for dancer in SETTINGS['dancers']:
        img_size = PVector(
            width * dancer['ratio'],
            height * dancer['ratio']
        )
        dancer_position = PVector(
            (1 - dancer['ratio']) * width / 2.0 + dancer['x'],
            (1 - dancer['ratio']) * height / 2.0 + dancer['y'],
        )
        image(images[img_num], dancer_position.x, dancer_position.y, img_size.x, img_size.y)


def keyPressed():
    if key == 's':
        file_name = os.path.basename(__file__).split('.')[0]
        print('{}.png'.format(file_name))
        save('output_images/{}.png'.format(file_name))
