# coding=utf-8
if False:
    from lib.Processing3 import *


def draw_bezier_shape(vt1, vt2, vt3, cp1, cp2, cp3, cp4, mark_size):
    # ベジェ曲線で囲まれた図形
    beginShape()
    vertex(vt1.x, vt1.y)
    bezierVertex(
        cp1.x,
        cp1.y,
        cp2.x,
        cp2.y,
        vt2.x,
        vt2.y
    )
    bezierVertex(
        cp3.x,
        cp3.y,
        cp4.x,
        cp4.y,
        vt3.x,
        vt3.y
    )
    bezierVertex(
        mirror_x(cp4.x, mark_size),
        cp4.y,
        mirror_x(cp3.x, mark_size),
        cp3.y,
        mirror_x(vt2.x, mark_size),
        vt2.y,
    )
    bezierVertex(
        mirror_x(cp2.x, mark_size),
        cp2.y,
        mirror_x(cp1.x, mark_size),
        cp1.y,
        vt1.x,
        vt1.y,
    )
    endShape()
    # quad(
    #     vt1.x,
    #     vt1.y,
    #     vt2.x,
    #     vt2.y,
    #     vt3.x,
    #     vt3.y,
    #     mirror_x(vt2.x, mark_size),
    #     vt2.y
    # )

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


def draw_mark(p, angle, mark_size, mark_type):
    if mark_type == 'star':
        mark_color = random(30, 60)
        vt1 = PVector(mark_size / 2, mark_size)
        vt2 = PVector(0, mark_size / 2)
        vt3 = PVector(mark_size / 2, 0)
        cp1 = PVector(mark_size / 2, mark_size * 3 / 4)
        cp2 = PVector(mark_size / 4, mark_size / 2)
        cp3 = PVector(mark_size / 4, mark_size / 2)
        cp4 = PVector(mark_size / 2, mark_size / 4)
    elif mark_type == 'diamond':
        mark_color = random(240, 270)
        vt1 = PVector(mark_size / 2, mark_size)
        vt2 = PVector(mark_size / 4, mark_size / 2)
        vt3 = PVector(mark_size / 2, 0)
        cp1 = PVector(mark_size / 2, mark_size)
        cp2 = PVector(mark_size / 4, mark_size / 2)
        cp3 = PVector(mark_size / 4, mark_size /2)
        cp4 = PVector(mark_size / 2, 0)
    elif mark_type == 'leaf':
        mark_color = random(120, 150)
        vt1 = PVector(mark_size / 2, mark_size)
        vt2 = PVector(mark_size / 4, mark_size * 3 / 4)
        vt3 = PVector(mark_size / 2, 0)
        cp1 = PVector(mark_size * 3 / 8, mark_size)
        cp2 = PVector(mark_size / 4, mark_size * 7 / 8)
        cp3 = PVector(mark_size / 4, mark_size / 2)
        cp4 = PVector(mark_size * 3 / 8, mark_size / 4)
    else:  # heart
        mark_color = random(20)
        vt1 = PVector(mark_size / 2, mark_size)
        vt2 = PVector(mark_size / 4, mark_size * 3 / 4)
        vt3 = PVector(mark_size / 2, mark_size / 4)
        cp1 = PVector(mark_size / 2, mark_size)
        cp2 = PVector(mark_size / 4, mark_size * 3 / 4)
        cp3 = PVector(-mark_size / 4, mark_size / 4)
        cp4 = PVector(mark_size / 4, -mark_size / 4)
    fill(mark_color, 100, 100)
    strokeWeight(1)
    stroke(mark_color, 100, 100)
    pushMatrix()
    translate(p.x, p.y)
    rotate(angle)
    draw_bezier_shape(vt1, vt2, vt3, cp1, cp2, cp3, cp4, mark_size)
    popMatrix()
