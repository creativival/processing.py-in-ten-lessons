#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
P3D Util
"""
if False:
    from lib.Processing3 import *


class Cylinder:
    def __init__(self, _radius, _height, _number_of_vertices, _is_corn=0):
        if _number_of_vertices >= 64:
            _number_of_vertices = 64
        self.radius = _radius
        self.height = _height
        self.number_of_vertices = _number_of_vertices
        self.is_corn = _is_corn

    def draw(self):
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
