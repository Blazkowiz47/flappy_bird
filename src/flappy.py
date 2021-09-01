import pygame
import os
import neat
import random
import time

from bird import Bird
from pipe import Pipe
from base import Base
from utils import *


def crash(win, score):
    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        text = STAT_FONT.render(
            "Game over\n Score: " + str(score), 1, (255, 255, 255))
        win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))
        pygame.display.update()
        pygame.display.update()
        pygame.time.Clock().tick(15)


def draw_window(win, bird, pipes, base, score):
    win.blit(BACKGROUND_IMAGES[0], (0, 0))
    for pipe in pipes:
        pipe.draw(win)
    base.draw(win)
    bird.draw(win)
    text = STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))
    pygame.display.update()


def main():
    bird = Bird(230, 350)
    run = True
    base = Base(700)
    pipes = [Pipe(700)]
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    # Entity which creates virtual clock
    clock = pygame.time.Clock()
    score = 0
    while run:
        # virtual clock ticks manually
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                bird.jump()
        # move background image
        base.move()
        # move the pipes as well as add more random pipes
        rem = []
        add_pipe = False
        for pipe in pipes:
            if pipe.collide(bird):
                run = False
                crash(win, score)
            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)
            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe = True
            pipe.move()

        if add_pipe:
            score += 1
            pipes.append(Pipe(random.randrange(600, 950)))
        for r in rem:
            pipes.remove(r)
        if bird.y + bird.img.get_height() > 730:
            pass
        bird.move()
        draw_window(win, bird, pipes, base, score)


if __name__ == "__main__":
    main()
