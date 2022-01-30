"""
ダンシングとマーク（動画で書き出し）
"""

if False:
    from lib.Processing3 import *
import os
import util

add_library("sound")

DANCER_SETTINGS = {
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
MARK_SETTINGS = {
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
dancer = None
marks = []
MIN_FRAME = 1
MAX_FRAME = 180


def setup():
    global dancer
    size(SIZE_X, SIZE_Y)
    colorMode(HSB, 360, 100, 100)
    dancer = util.Dancer(DANCER_SETTINGS)
    blendMode(ADD)
    for i in range(MARK_SETTINGS['number_of_marks']):
        p = PVector(random(width), random(height))
        angle = map(random(1), 0, 1, 0, TWO_PI)
        mark_size = random(MARK_SETTINGS['min_size'], MARK_SETTINGS['max_size'])
        mark_color = random(MARK_SETTINGS['min_color'], MARK_SETTINGS['max_color'])
        mark = util.Mark(p, angle, mark_size, mark_color, MARK_SETTINGS)
        marks.append(mark)

    global soundfile
    soundfile = SoundFile(this, "sound.aiff")
    soundfile.loop()


def draw():
    background(BACKGROUND_COLOR)
    dancer.draw()
    for m in marks:
        m.draw()
        m.update()
        m.through_walls()

    util.save_frame(MIN_FRAME, MAX_FRAME)


def keyPressed():
    if key == 's':
        file_name = os.path.basename(__file__).split('.')[0]
        print('{}.png'.format(file_name))
        save('output_images/{}.png'.format(file_name))
