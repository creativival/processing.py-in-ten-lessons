"""
曲線 Catmull-Romスプライン
"""

if False:
    from lib.Processing3 import *

TIGHTNESS = 0.5  # 曲率を変える（弾力性）


def setup():
    size(1000, 1000)
    grid = loadImage('grid.png')
    image(grid, 0, 0)
    stroke(127)
    textSize(20)
    textAlign(LEFT, TOP)
    text('Tightness: ' + str(TIGHTNESS), 20, 20)
    noFill()
    strokeWeight(3)
    curveTightness(TIGHTNESS)
    # 直線
    stroke(255, 0, 0)
    # line(100, 100, 400, 400)
    curve(0, 0, 100, 100, 400, 400, 500, 500)
    # 曲線
    stroke(255, 255, 0)
    curve(0, 250, 100, 100, 400, 400, 500, 250)
    # コントロールポイントの視覚化
    stroke(255, 99, 0)
    curve(0, 250, 0, 250, 100, 100, 400, 400)
    curve(100, 100, 400, 400, 500, 250, 500, 250)
