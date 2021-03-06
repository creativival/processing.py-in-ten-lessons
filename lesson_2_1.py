"""
方眼紙
"""

if False:
    from lib.Processing3 import *
import os

BACKGROUND_COLOR = color(0, 44, 77)


def setup():
    size(1000, 1000)
    background(BACKGROUND_COLOR)
    stroke(127)
    textSize(20)
    textAlign(LEFT, TOP)
    text(str(0), 0, 0)
    # 方眼紙
    for i in range(1, 11):
        # 縦線
        line(i * 100, 0, i * 100, 1000)
        textAlign(CENTER, TOP)
        text(str(i * 100), i * 100, 0)
        # 横線
        line(0, i * 100, 1000, i * 100)
        textAlign(LEFT, CENTER)
        text(str(i * 100), 0, i * 100)


def draw():
    pass


def mousePressed():
    # 画像を保存
    print('save image')
    save('output_images/grid.png')


def keyPressed():
    if key == 's':
        file_name = os.path.basename(__file__).split('.')[0]
        print('{}.png'.format(file_name))
        save('output_images/{}.png'.format(file_name))
