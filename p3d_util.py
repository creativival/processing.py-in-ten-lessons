#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
P3D Util
"""
if False:
    from lib.Processing3 import *


class Cylinder:
    def __init__(self, _radius, _height, _number_of_vertices, _color, _is_corn=0):
        if _number_of_vertices >= 64:
            _number_of_vertices = 64
        self.radius = _radius
        self.height = _height
        self.number_of_vertices = _number_of_vertices
        self.color = _color
        self.is_corn = _is_corn

    def draw(self):
        fill(self.color)
        angle = TWO_PI / self.number_of_vertices

        # 底面
        if self.number_of_vertices >= 64:
            # 円錐
            stroke(0)
            pushMatrix()
            rotateX(-PI / 2)
            translate(0, 0, -self.height / 2)
            ellipse(0, 0, self.radius * 2, self.radius * 2)
            translate(0, 0, self.height)
            if self.is_corn:
                ellipse(0, 0, 1, 1)  # 頂点
            else:
                ellipse(0, 0, self.radius * 2, self.radius * 2)
            popMatrix()
        else:
            noStroke()
            beginShape(TRIANGLE_STRIP)
            for i in range(self.number_of_vertices):
                vertex(0, -self.height / 2, 0)
                vertex(
                    self.radius * sin(angle * i),
                    -self.height / 2,
                    self.radius * cos(angle * i),
                )
                vertex(
                    self.radius * sin(angle * (i + 1)),
                    -self.height / 2,
                    self.radius * cos(angle * (i + 1)),
                )
                if not self.is_corn:
                    vertex(0, self.height / 2, 0)
                    vertex(
                        self.radius * sin(angle * i),
                        self.height / 2,
                        self.radius * cos(angle * i),
                    )
                    vertex(
                        self.radius * sin(angle * (i + 1)),
                        self.height / 2,
                        self.radius * cos(angle * (i + 1)),
                    )
            endShape()

        # 側面
        if self.number_of_vertices >= 64:
            # 円錐
            noStroke()
        else:
            stroke(0)

        if self.is_corn:
            beginShape(TRIANGLE_STRIP)
        else:
            beginShape(QUADS)
        for i in range(self.number_of_vertices):
            vertex(
                self.radius * sin(angle * i),
                -self.height / 2,
                self.radius * cos(angle * i),
            )
            vertex(
                self.radius * sin(angle * (i + 1)),
                -self.height / 2,
                self.radius * cos(angle * (i + 1)),
            )
            if self.is_corn:
                vertex(
                    0,
                    self.height / 2,
                    0,
                )
            else:
                vertex(
                    self.radius * sin(angle * (i + 1)),
                    self.height / 2,
                    self.radius * cos(angle * (i + 1)),
                )
                vertex(
                    self.radius * sin(angle * i),
                    self.height / 2,
                    self.radius * cos(angle * i),
                )
        endShape()


def draw_axes():
    stroke(255, 0, 0)
    line(0, 0, 0, 1000, 0, 0)
    stroke(0, 255, 0)
    line(0, 0, 0, 0, 1000, 0)
    stroke(0, 0, 255)
    line(0, 0, 0, 0, 0, 1000)


def test_lighting():
    # ライト
    if keyPressed:
        if key == 'l':
            lights()
        elif key == 'd':
            directionalLight(0, 255, 0, 0, -1, 0)
        elif key == 'a':
            ambientLight(0, 0, 255)
        elif key == 'p':
            pointLight(255, 0, 0, width / 2, height / 2, 400)
        elif key == 's':
            spotLight(255, 0, 0, width / 2, height / 2, 400, 0, 0, -1, PI / 4, 2)


def test_drawing_cylinder(_radius, _height, _number_of_vertices):
    test_lighting()
    # 錐
    pushMatrix()
    c = color(0, 255, 0)
    translate(width / 2, height / 3)
    rotateX(map(mouseY, 0, height, -PI, PI))
    rotateY(map(mouseX, 0, width, -PI, PI))
    draw_axes()
    cylinder = Cylinder(_radius, _height, _number_of_vertices, c, 1)
    cylinder.draw()
    popMatrix()
    # 柱
    pushMatrix()
    c = color(255, 0, 0)
    translate(width / 2, height * 3 / 4)
    rotateX(map(mouseY, 0, height, -PI, PI))
    rotateY(map(mouseX, 0, width, -PI, PI))
    draw_axes()
    cylinder = Cylinder(_radius, _height, _number_of_vertices, c, 0)
    cylinder.draw()
    popMatrix()
