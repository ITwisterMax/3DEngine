import pygame as pg
from config import *
from models.camera import *
from services.projection import *
from services.reader import *


class Engine3D:
    def __init__(self):
        pg.init()

        self.RES = self.WIDTH, self.HEIGHT = WINDOW_WIDTH, WINDOW_HEIGHT
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = WINDOW_FPS

        pg.display.set_caption(WINDOW_CAPTION)
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()

        self.create_models()

    def create_models(self):
        self.camera = Camera(self, CAMERA_POSITON)
        self.projection = Projection(self)
        self.object = get_object_from_file(self, PATH_TO_OBJECT)

    def draw(self):
        self.screen.fill(pg.Color(WINDOW_COLOR))
        self.object.draw()

    def run(self):
        while True:
            self.draw()
            self.camera.control()

            [exit() for i in pg.event.get() if i.type == pg.QUIT]

            pg.display.flip()
            self.clock.tick(self.FPS)

if __name__ == '__main__':
    app = Engine3D()
    app.run()