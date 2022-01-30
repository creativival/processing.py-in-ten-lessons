"""
絵文字
"""
if False:
    from lib.Processing3 import *
import os

SIZE_X = 1200
SIZE_Y = 750


def setup():
    size(SIZE_X, SIZE_Y, P3D)

    # my_font = createFont(u'メイリオ', 30)
    # textFont(my_font)

    # num = '123'
    # url = 'http://localhost:18080/kabusapi/board/{}'.format(num)
    #
    # print(url)
    #
    # s1 = '日本語文字列(s1)'
    # s2 = u'日本語文字列(s2)'
    #
    # print(s1)  # 文字化け
    # print(s2)  # 文字化けしない
    #
    # print(type(s1))  # str
    # print(type(s2))  # unicode
    #
    # print(s1.decode('utf-8'))  # str -> unicode に変換. 文字化けしない
    # print(s2.encode('utf-8'))  # unicode -> str に変換. 文字化けする
    #
    # print(s2.encode('utf-8').decode('utf-8'))  # unicode -> str -> unicode　文字化けしない

    fill(0)
    textSize(100)
    text(u'あいうえお', 100, 100)
    text(u"💙", 100, 200)  # x, y = 100, 100 test
    text("💙", 100, 300)  # x, y = 100, 100 test
    text(u"🍭💡💦", 100, 400)
    # grinning face
    text(u"\U0001F600", 100, 500)
    # beaming face with smiling eyes
    text("\U0001F601", 100, 600)
    # grinning face with sweat
    text("U0001F605", 100, 700)

    # grinning face
    print(u"\U0001F600")
    # beaming face with smiling eyes
    print("\U0001F601")
    # grinning face with sweat
    print("U0001F605")
    # rolling on the floor laughing
    print("U0001F923")
    # face with tears of joy
    print("U0001F602")
    # slightly smiling face
    print("U0001F642")
    # smiling face with halo
    print("U0001F607")
    # smiling face with heart-eyes
    print("U0001F60D")
    # zipper-mouth face
    print("U0001F910")
    # unamused face
    print("U0001F612")
    print('\U0001f604'.decode('utf-8'))
    print("🍭💡💦".decode('utf-8'))
    print(":door: Nite, nite")
    print(u"\U0001f6aa Nite, nite")


def draw():
    pass
