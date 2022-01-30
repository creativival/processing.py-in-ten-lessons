"""
RGBの理解
"""

if False:
    from lib.Processing3 import *
import os


def setup():
    noStroke()
    size(1024, 1024)
    for k in range(0, 256, 32):
        for j in range(0, 256, 32):
            for i in range(0, 256, 32):
                print(i, j, k)
                fill(i, j, k)
                rect(i * 4 + k / 2, j * 4, 16, 128)


def draw():
    pass


def keyPressed():
    if key == 's':
        file_name = os.path.basename(__file__).split('.')[0]
        print('{}.png'.format(file_name))
        save('output_images/{}.png'.format(file_name))
