"""
ボックスにテキスチャーを貼り付け
"""
if False:
    from lib.Processing3 import *
import os

SIZE_X = 1200
SIZE_Y = 700
MIN_CRYSTAL = 20
MAX_CRYSTAL = 50
CAMERA_DISTANCE = 600
crystals = []


def setup():
    size(SIZE_X, SIZE_Y, P3D)
    frameRate(60)
    create_crystals()


def draw():
    global crystals
    img = loadImage('lerp_color.png')
    background(0)
    lights()
    camera_x = CAMERA_DISTANCE * sin(frameCount * 0.01)
    camera_z = CAMERA_DISTANCE * cos(frameCount * 0.01)
    camera(width / 2 + camera_x, height / 2, camera_z, width / 2, height / 2, 0, 0, 1, 0)

    translate(width / 2, height / 2, 0)
    for crystal in crystals:
        crystal.draw(img)

    if frameCount % (3 * 60) == 0:
        crystals = []
        create_crystals()


def mousePressed():
    global crystals
    crystals = []
    create_crystals()


def create_crystals():
    num = int(random(MIN_CRYSTAL, MAX_CRYSTAL))
    for i in range(num):
        crystals.append(Crystal())


class Crystal:
    def __init__(self):
        self.width = random(25, 50)
        self.height = random(250, 500)
        self.depth = self.width
        self.rotate = PVector(
            random(TWO_PI),
            random(TWO_PI),
            random(TWO_PI)
        )

    def draw(self, _img):
        pushMatrix()
        rotateX(self.rotate.x)
        rotateY(self.rotate.y)
        rotateZ(self.rotate.z)
        b = createShape(
            BOX,
            self.width,
            self.height,
            self.depth
        )
        b.setTexture(_img)
        shape(b)
        popMatrix()


def keyPressed():
    if key == 's':
        file_name = os.path.basename(__file__).split('.')[0]
        print('{}.png'.format(file_name))
        save('output_images/{}.png'.format(file_name))
