import neat
import os
import random
from bird import Bird
from pipe import Pipe
from base import Base
from utils import *

gen = 0
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))


def draw_window(win, birds, pipes, base, score, gen):
    win.blit(BACKGROUND_IMAGES[0], (0, 0))

    for pipe in pipes:
        pipe.draw(win)

    for bird in birds:
        bird.draw(win)

    base.draw(win)

    text = STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))

    textg = STAT_FONT.render("Gen: " + str(gen), 1, (255, 255, 255))
    win.blit(textg, (10, 10))
    pygame.display.update()


def eval_gen(genomes, config):
    global win
    birds = []
    ge = []
    nets = []
    global gen
    gen += 1
    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        birds.append(Bird(230, 350))
        g.fitness = 0
        ge.append(g)
        pass

    base = Base(730)
    pipes = [Pipe(600)]

    # Entity which creates virtual clock
    clock = pygame.time.Clock()
    score = 0
    run = True

    while run:
        # virtual clock ticks manually
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        pipe_ind = 0
        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > pipes[0].PIPE_TOP.get_width():
                pipe_ind = 1
        else:
            run = False
            break

        for x, bird in enumerate(birds):
            bird.move()
            ge[x].fitness += 0.1

            output = nets[birds.index(bird)].activate(
                (bird.y, abs(bird.y - pipes[pipe_ind].top), abs(bird.y - pipes[pipe_ind].bottom),
                 abs(bird.x - pipes[pipe_ind].x)))

            if output[0] > 0.5:
                bird.jump()
        # move the pipes as well as add more random pipes
        rem = []
        add_pipe = False
        for pipe in pipes:

            for x, bird in enumerate(birds):

                if pipe.collide(bird):
                    # encourages to stay in-between the pipe
                    ge[x].fitness -= 0.75
                    birds.pop(x)
                    nets.pop(x)
                    ge.pop(x)

                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    add_pipe = True

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)

            pipe.move()

        if add_pipe:
            score += 1
            for g in ge:
                g.fitness += 5
            pipes.append(Pipe(random.randrange(450, 750)))

        for r in rem:
            pipes.remove(r)

        for x, bird in enumerate(birds):
            if bird.y + bird.img.get_height() > 730 or bird.y < 0:
                birds.pop(x)
                nets.pop(x)
                ge.pop(x)
        # move background image
        base.move()
        draw_window(win, birds, pipes, base, score, gen)


def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet,
                                neat.DefaultStagnation, config_path)
    p = neat.Population(config)
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    winner = p.run(eval_gen, 50)
    print('\nBest genome:\n{!s}'.format(winner))


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")
    run(config_path)
