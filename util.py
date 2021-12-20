# coding=utf-8
if False:
    from lib.Processing3 import *


def draw_bezier_shape(vt1, vt2, vt3, cp1, cp2, cp3, cp4, mark_size):
    # ベジェ曲線で囲まれた図形
    bezier(
        vt1.x,
        vt1.y,
        cp1.x,
        cp1.y,
        cp2.x,
        cp2.y,
        vt2.x,
        vt2.y
    )
    bezier(
        mirror_x(vt1.x, mark_size),
        vt1.y,
        mirror_x(cp1.x, mark_size),
        cp1.y,
        mirror_x(cp2.x, mark_size),
        cp2.y,
        mirror_x(vt2.x, mark_size),
        vt2.y
    )
    bezier(
        vt2.x,
        vt2.y,
        cp3.x,
        cp3.y,
        cp4.x,
        cp4.y,
        vt3.x,
        vt3.y
    )
    bezier(
        mirror_x(vt2.x, mark_size),
        vt2.y,
        mirror_x(cp3.x, mark_size),
        cp3.y,
        mirror_x(cp4.x, mark_size),
        cp4.y,
        mirror_x(vt3.x, mark_size),
        vt3.y
    )
    quad(
        vt1.x,
        vt1.y,
        vt2.x,
        vt2.y,
        vt3.x,
        vt3.y,
        mirror_x(vt2.x, mark_size),
        vt2.y
    )

def draw_check_point(vt1, vt2, vt3, cp1, cp2, cp3, cp4, mark_size):
    stroke(255, 255, 0)
    strokeWeight(3)
    line(vt1.x, vt1.y, cp1.x, cp1.y)
    line(vt2.x, vt2.y, cp2.x, cp2.y)
    line(
        mirror_x(vt1.x, mark_size),
        vt1.y,
        mirror_x(cp1.x, mark_size),
        cp1.y)
    line(
        mirror_x(vt2.x, mark_size),
        vt2.y,
        mirror_x(cp2.x, mark_size),
        cp2.y)
    line(vt2.x, vt2.y, cp3.x, cp3.y)
    line(vt3.x, vt3.y, cp4.x, cp4.y)
    line(
        mirror_x(vt2.x, mark_size),
        vt2.y,
        mirror_x(cp3.x, mark_size),
        cp3.y)
    line(
        mirror_x(vt3.x, mark_size),
        vt3.y,
        mirror_x(cp4.x, mark_size),
        cp4.y
    )


def mirror_x(x, mark_size):
    return mark_size - x
