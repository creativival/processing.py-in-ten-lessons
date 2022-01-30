"""
曲線 ベジェ曲線
"""

if False:
    from lib.Processing3 import *
import os


def setup():
    size(1000, 1000)
    grid = loadImage('grid.png')
    image(grid, 0, 0)
    noFill()
    strokeWeight(3)
    cp1 = PVector(250, 250)
    cp2 = PVector(250, 250)
    # 直線
    stroke(255, 0, 0)
    # line(100, 100, 400, 400)
    bezier(100, 100, cp1.x, cp1.y, cp2.x, cp2.y, 400, 400)
    # 曲線
    stroke(255, 255, 0)
    cp1.y = 200
    cp2.x = 180
    cp2.y = 350
    bezier(100, 100, cp1.x, cp1.y, cp2.x, cp2.y, 400, 400)
    # コントロールポイントの視覚化
    stroke(255, 99, 0)
    line(100, 100, cp1.x, cp1.y)
    line(400, 400, cp2.x, cp2.y)


def draw():
    pass


def keyPressed():
    if key == 's':
        file_name = os.path.basename(__file__).split('.')[0]
        print('{}.png'.format(file_name))
        save('output_images/{}.png'.format(file_name))
