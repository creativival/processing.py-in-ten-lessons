if False:
    from lib.Processing3 import *


def setup():
    colorMode(HSB, 360, 100, 100)
    noStroke()
    size(550, 550)
    for j in range(11):  # 明度（Y軸）
        for i in range(11):  # 彩度（X軸）
            fill(360, 10 * i, 10 * j)
            rect(50 * i, 50 * j, 50, 50)
    print('hello world')
