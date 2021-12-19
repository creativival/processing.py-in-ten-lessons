"""
方眼紙
"""

if False:
    from lib.Processing3 import *

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


def mouseClicked():
    # 画像を保存
    print('save image')
    save('grid.png')
