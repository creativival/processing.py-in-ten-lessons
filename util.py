# coding=utf-8
if False:
    from lib.Processing3 import *


def draw_bezier_shape(vertices, control_points):
    # ベジェ曲線で囲まれた図形
    beginShape()
    vertex(vertices[0].x, vertices[0].y)
    for i in range(len(vertices)):
        if i >= len(vertices) - 1:
            bezierVertex(
                control_points[i * 2].x,
                control_points[i * 2].y,
                control_points[i * 2 + 1].x,
                control_points[i * 2 + 1].y,
                vertices[0].x,
                vertices[0].y
            )
        else:
            bezierVertex(
                control_points[i * 2].x,
                control_points[i * 2].y,
                control_points[i * 2 + 1].x,
                control_points[i * 2 + 1].y,
                vertices[i + 1].x,
                vertices[i + 1].y
            )
    endShape()


def draw_check_point(vertices, control_points):
    stroke(255, 255, 0)
    strokeWeight(3)
    for i in range(len(vertices)):
        if i == 0:
            line(
                vertices[i].x,
                vertices[i].y,
                control_points[i * 2].x,
                control_points[i * 2].y
            )
            line(
                vertices[i].x,
                vertices[i].y,
                control_points[len(control_points) - 1].x,
                control_points[len(control_points) - 1].y
            )
        else:
            line(
                vertices[i].x,
                vertices[i].y,
                control_points[i * 2 - 1].x,
                control_points[i * 2 - 1].y
            )
            line(
                vertices[i].x,
                vertices[i].y,
                control_points[i * 2].x,
                control_points[i * 2].y
            )


def mirror_x(p, mark_size):
    return PVector(mark_size - p.x, p.y)


def mirror_y(p, mark_size):
    return PVector(p.x, mark_size - p.y)


def draw_mark(p, angle, mark_size, mark_type):
    if mark_type == 'star':
        mark_color = random(30, 60)
        vt1 = PVector(mark_size / 2, mark_size)
        vt2 = PVector(0, mark_size / 2)
        vt3 = PVector(mark_size / 2, 0)
        vt4 = mirror_x(vt2, mark_size)
        cp1 = PVector(mark_size / 2, mark_size * 3 / 4)
        cp2 = PVector(mark_size / 4, mark_size / 2)
        cp3 = PVector(mark_size / 4, mark_size / 2)
        cp4 = PVector(mark_size / 2, mark_size / 4)
        cp5 = mirror_x(cp4, mark_size)
        cp6 = mirror_x(cp3, mark_size)
        cp7 = mirror_x(cp2, mark_size)
        cp8 = mirror_x(cp1, mark_size)
        vertices = [vt1, vt2, vt3, vt4]
        control_points = [cp1, cp2, cp3, cp4, cp5, cp6, cp7, cp8]
    elif mark_type == 'diamond':
        mark_color = random(240, 270)
        vt1 = PVector(mark_size / 2, mark_size)
        vt2 = PVector(mark_size / 4, mark_size / 2)
        vt3 = PVector(mark_size / 2, 0)
        vt4 = mirror_x(vt2, mark_size)
        cp1 = vt1
        cp2 = vt2
        cp3 = vt2
        cp4 = vt3
        cp5 = mirror_x(cp4, mark_size)
        cp6 = mirror_x(cp3, mark_size)
        cp7 = mirror_x(cp2, mark_size)
        cp8 = mirror_x(cp1, mark_size)
        vertices = [vt1, vt2, vt3, vt4]
        control_points = [cp1, cp2, cp3, cp4, cp5, cp6, cp7, cp8]
    elif mark_type == 'leaf':
        mark_color = random(120, 150)
        vt1 = PVector(mark_size / 2, mark_size)
        vt2 = PVector(mark_size / 4, mark_size * 3 / 4)
        vt3 = PVector(mark_size / 2, 0)
        vt4 = mirror_x(vt2, mark_size)
        cp1 = PVector(mark_size * 3 / 8, mark_size)
        cp2 = PVector(mark_size / 4, mark_size * 7 / 8)
        cp3 = PVector(mark_size / 4, mark_size / 2)
        cp4 = PVector(mark_size * 3 / 8, mark_size / 4)
        cp5 = mirror_x(cp4, mark_size)
        cp6 = mirror_x(cp3, mark_size)
        cp7 = mirror_x(cp2, mark_size)
        cp8 = mirror_x(cp1, mark_size)
        vertices = [vt1, vt2, vt3, vt4]
        control_points = [cp1, cp2, cp3, cp4, cp5, cp6, cp7, cp8]
    else:  # heart
        mark_color = random(20)
        vt1 = PVector(mark_size / 2, mark_size)
        vt2 = PVector(mark_size / 4, mark_size * 3 / 4)
        vt3 = PVector(mark_size / 2, mark_size / 4)
        vt4 = mirror_x(vt2, mark_size)
        cp1 = vt1
        cp2 = vt2
        cp3 = PVector(-mark_size / 4, mark_size / 4)
        cp4 = PVector(mark_size / 4, -mark_size / 4)
        cp5 = mirror_x(cp4, mark_size)
        cp6 = mirror_x(cp3, mark_size)
        cp7 = mirror_x(cp2, mark_size)
        cp8 = mirror_x(cp1, mark_size)
        vertices = [vt1, vt2, vt3, vt4]
        control_points = [cp1, cp2, cp3, cp4, cp5, cp6, cp7, cp8]
    fill(mark_color, 100, 100)
    strokeWeight(1)
    stroke(mark_color, 100, 100)
    pushMatrix()
    translate(p.x, p.y)
    rotate(angle)
    draw_bezier_shape(vertices, control_points)
    popMatrix()
