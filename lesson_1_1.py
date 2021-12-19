"""
彩度、明度の理解
"""

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
    word = 'world'
    print('hello {}'.format(word))
    # print(f'hello {word}')  # 未対応
    hello = u'こんにちは'
    world = u'世界'
    print(hello)
    print(world)
    print(hello, world)
    print(hello + world)
    # print('hello {}'.format(world))  # 未対応
