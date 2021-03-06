if False:
    from lib.Processing3 import *


def draw_bezier_shape(vertices, control_points):
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


def draw_mark(p, angle, mark_size, mark_color, mark_type):
    if mark_type == 'gear':
        number_of_vertices = int(random(8, 14))
        ratio = 8.0 / 10
        radius = mark_size / 2
        pushMatrix()
        translate(radius, radius)
        vertices = []
        control_points = []
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
        popMatrix()
    elif mark_type == 'six_pointed_star':
        number_of_vertices = 6
        ratio = 1.0 / 2
        radius = mark_size / 2
        pushMatrix()
        translate(radius, radius)
        vertices = []
        control_points = []
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
        popMatrix()
    elif mark_type == 'five_pointed_star':
        number_of_vertices = 5
        ratio = 1.0 / 3
        radius = mark_size / 2
        pushMatrix()
        translate(radius, radius)
        vertices = []
        control_points = []
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
        popMatrix()
    elif mark_type == 'shine':
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


class Mark:
    def __init__(self, p, angle, mark_size, mark_color, settings):
        self.position = p
        self.angle = angle
        self.size = mark_size
        self.color = mark_color
        self.type = settings['type']
        self.fall_speed = settings['fall_speed']
        self.min_size = settings['min_size']
        self.max_size = settings['max_size']

    def draw(self):
        draw_mark(self.position, self.angle, self.size, self.color, self.type)

    def update(self):
        speed = PVector.mult(self.fall_speed, self.size)
        speed.y += noise(1)
        self.position = PVector.add(self.position, speed)
        self.angle += random(-PI / 90, PI / 90)
        self.size *= random(1 / 1.01, 1.01)

    def reset_size(self):
        if self.size < self.min_size / 2 or self.max_size * 1.5 < self.size:
            self.size = random(10, 20)

    def through_walls(self):
        if self.position.x < 0:
            self.position.x = width
            self.reset_size()
        if width < self.position.x:
            self.position.x = 0
            self.reset_size()
        if self.position.y < 0:
            self.position.x = random(width)
            self.position.y = height
            self.reset_size()
        if height < self.position.y:
            self.position.x = random(width)
            self.position.y = 0
            self.reset_size()


def save_frame(min_frame, max_frame):
    if min_frame <= frameCount <= max_frame:
        saveFrame('frames/######.png')


class Dancer:
    def __init__(self, settings):
        self.settings = settings
        self.img_num = 0
        self.images = []
        for i in range(settings['min_img_num'], settings['max_img_num'] + 1):
            num = '{0:03d}'.format(i)
            file_name = '{}_{}.png'.format(settings['base_file_name'], num)
            img = loadImage(file_name)
            self.images.append(img)

    def draw(self):
        if frameCount % int(20.0 / self.settings['speed']) == 0:
            self.img_num = int(random(len(self.images)))
            print(self.img_num)

        for dancer in self.settings['dancers']:
            img_size = PVector(
                width * dancer['ratio'],
                height * dancer['ratio']
            )
            dancer_position = PVector(
                (1 - dancer['ratio']) * width / 2.0 + dancer['x'],
                (1 - dancer['ratio']) * height / 2.0 + dancer['y'],
            )
            image(self.images[self.img_num], dancer_position.x, dancer_position.y, img_size.x, img_size.y)
