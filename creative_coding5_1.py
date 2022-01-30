"""
leapColor
"""
if False:
    from lib.Processing3 import *
import os

SIZE_X = 300
SIZE_Y = 500


def setup():
    size(SIZE_X, SIZE_Y)
    noStroke()
    color1 = color(0xff, 0xff, 0xff)
    color2 = color(0x0b, 0xba, 0xcc)
    color3 = color(0x01, 0x1b, 0x42)
    for i in range(0, height, 5):
        if i <= height / 2:
            c = lerpColor(color1, color2, i * 2.0 / height)
        else:
            print(i)
            c = lerpColor(color2, color3, (i - height / 2) * 2.0 / height)
        fill(c)
        rect(0, i, width, 5)
    save('output_images/lerp_color.png')


def keyPressed():
    if key == 's':
        file_name = os.path.basename(__file__).split('.')[0]
        print('{}.png'.format(file_name))
        save('output_images/{}.png'.format(file_name))
