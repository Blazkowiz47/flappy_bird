from utils import *


class Base:
    VEL = 5
    WIDTH = BASE_IMAGES[0].get_width()
    IMG = BASE_IMAGES[0]

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):
        # moves background images to left
        self.x1 -= self.VEL
        self.x2 -= self.VEL
        # moves background image in sort of circular loop
        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH
        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))