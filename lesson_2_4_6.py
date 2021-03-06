"""
曲線 六芒星
"""

if False:
    from lib.Processing3 import *
import os
import util

MARK_COLOR = color(255, 0, 255)
BACKGROUND_COLOR = color(0, 44, 77)
MARK_SIZE = 400
NUMBER_OF_VERTICES = 6
RATIO = 1.0 / 2


def setup():
    size(MARK_SIZE, MARK_SIZE)
    grid = loadImage('grid.png')
    image(grid, 0, 0)
    # background(BACKGROUND_COLOR)
    fill(MARK_COLOR)
    noStroke()
    radius = MARK_SIZE / 2
    pushMatrix()
    translate(radius, radius)
    vertices = []
    control_points = []
    number_of_vertices = NUMBER_OF_VERTICES
    ratio = RATIO
    for i in range(number_of_vertices):
        vertex_angle = PI * i * 4 / (2 * number_of_vertices)
        control_point_angle = PI * (2 + i * 4) / (2 * number_of_vertices)
        vertices.append(
            PVector(radius * cos(vertex_angle), radius * sin(vertex_angle))
        )
        control_points.append(
            PVector(radius * cos(control_point_angle) * ratio, radius * sin(control_point_angle) * ratio)
        )
        control_points.append(
            PVector(radius * cos(control_point_angle) * ratio, radius * sin(control_point_angle) * ratio)
        )
    util.draw_bezier_shape(vertices, control_points)
    util.draw_check_point(vertices, control_points)
    popMatrix()


def draw():
    pass


def keyPressed():
    if key == 's':
        file_name = os.path.basename(__file__).split('.')[0]
        print('{}.png'.format(file_name))
        save('output_images/{}.png'.format(file_name))
