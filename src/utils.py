import pygame
import os

WIN_WIDTH = 500
WIN_HEIGHT = 800
IMAGES_DIR = "data\\imgs\\"
pygame.font.init()
BIRD_IMAGES = [pygame.transform.scale2x(
    pygame.image.load(os.path.join(IMAGES_DIR, "bird1.png"))),
    pygame.transform.scale2x(
        pygame.image.load(os.path.join(IMAGES_DIR, "bird2.png"))),
    pygame.transform.scale2x(
        pygame.image.load(os.path.join(IMAGES_DIR, "bird3.png")))
]
PIPE_IMAGES = [pygame.transform.scale2x(
    pygame.image.load(os.path.join(IMAGES_DIR, "pipe.png"))), ]
BASE_IMAGES = [pygame.transform.scale2x(
    pygame.image.load(os.path.join(IMAGES_DIR, "base.png"))), ]
BACKGROUND_IMAGES = [pygame.transform.scale2x(
    pygame.image.load(os.path.join(IMAGES_DIR, "bg.png"))), ]

STAT_FONT = pygame.font.SysFont("comicsans", 50)
