import pygame
from gettext import gettext as _
from random import randint
from scorescreen import scorescreen


def load_elements_images():

    global pillarup, pillarup, pillardown, pipe, bird1, bird2, bird3, bird4
    global pillarup_width, pillarup_height, pillardown_width, pillardown_height
    pillarup = pygame.image.load("assets/pipe-down.png").convert()
    pillarup_width = pillarup.get_width()
    pillarup_height = pillarup.get_height()
    pillardown = pygame.image.load("assets/pipe-up.png").convert()
    pillardown_width = pillardown.get_width()
    pillardown_height = pillardown.get_height()
    pipe = pygame.image.load("assets/pipe.png").convert()

    bird1 = pygame.image.load("assets/bird/bird1.png").convert()
    bird2 = pygame.image.load("assets/bird/bird2.png").convert()
    bird3 = pygame.image.load("assets/bird/bird3.png").convert()
    bird4 = pygame.image.load("assets/bird/bird4.png").convert()


class pillar(object):

    def __init__(self):
        self.gap = 160
        self.x = 840
        self.y = 0
        self.height = randint(60, 300)
        self.pipeup = pygame.transform.scale(pipe, (52 - 4, self.height))
        self.pipeup_width = self.pipeup.get_width()
        self.pipeup_height = self.pipeup.get_height()
        self.pipedown = pygame.transform.scale(
            pipe, (52 - 4, 768 - self.height))
        self.pipedown_width = self.pipedown.get_width()
        self.pipedown_height = self.pipedown.get_height()

    def display(self, gameDisplay, pillarlist, birds, g):

        gameDisplay.blit(self.pipeup, (self.x + 2, self.y))
        gameDisplay.blit(pillarup, (self.x, self.y + self.height))

        gameDisplay.blit(pillardown, (self.x, self.y + self.height + self.gap))
        gameDisplay.blit(self.pipedown, (self.x + 2,
                                         self.y + self.height + self.gap + 26))

        self.x -= 3

        if(self.x == 618):
            pillarlist.append(pillar())
        # original 295
        if(self.x < 0):
            pillarlist.remove(self)

        # collision check

        bird_rect = birds.bird.get_rect(center=(birds.x + birds.bird.get_width() / 2,

                                                birds.y + birds.bird.get_height() / 2))

        pipe1_rect = self.pipeup.get_rect(center=(self.x + 2 + self.pipeup_width / 2,
                                                  self.y + self.pipeup_height / 2))

        pillar1_rect = pillarup.get_rect(center=(self.x + pillarup_width / 2,
                                                 self.y + self.height + pillarup_height / 2))

        pillar2_rect = pillardown.get_rect(center=(self.x + pillardown_width / 2,
                                                   self.y + self.height + self.gap + pillardown_height / 2))

        pipe2_rect = self.pipedown.get_rect(center=(self.x + 2 + self.pipedown.get_width() / 2,
                                                    self.y + self.height + self.gap + 26 + self.pipedown.get_height() / 2))

        if bird_rect.colliderect(pipe1_rect) or bird_rect.colliderect(pipe2_rect) or \
                bird_rect.colliderect(pillar1_rect) or bird_rect.colliderect(pillar2_rect):

            g.hit.play(0)

            b = scorescreen()
            b.run(g.gameDisplay, g.scores)
            g.initialize()
            g.welcomeflag = 1
            return

        # scores increment
        if(self.x == 399):
            g.scores += 1
            g.point.play(0)


class bird(object):

    def __init__(self):

        self.x = 400
        self.y = 400
        self.t = 0
        self.a = 9.6
        self.u = 8.0
        self.v = 10
        self.frame = 0
        self.angle = 0
        self.count = 0
        self.up = True
        self.bird = bird1

        self.birdlist = [bird1, bird2, bird3, bird4]

    def display(self, gameDisplay, flag):

        self.bird = pygame.transform.rotate(
            self.birdlist[int(self.frame / 8)], self.angle)
        gameDisplay.blit(self.bird, (self.x, self.y))
        self.frame += 1
        if(int(self.frame / 8) == 4):
            self.frame = 0

        if(flag == 1):

            self.count += 1
            if(self.count == 25):
                self.count = 0
                self.up = not self.up

            if self.up:
                self.y -= 1
            else:
                self.y += 1

    def jump(self, land1, land2, land1x, land2x, g):

        self.t += 1

        if(self.v > 0 and self.t > 0 and self.t < 25 and self.angle <= 20):
            self.angle += 2

        if(self.t > 25 and self.angle > -80):
            self.angle -= 2

        # motion equation v=u-at

        self.v = self.u - (self.a / 24) * (self.t)

        self.y -= self.v

        if(self.y < 0):
            self.y = 0

        # bird platform fall check

        bird_rect = self.bird.get_rect(center=(
            self.x + self.bird.get_width() / 2, self.y + self.bird.get_height() / 2))

        platform_rect1 = land1.get_rect(
            center=(land1x + land1.get_width() / 2, 600 + land1.get_height() / 2))
        platform_rect2 = land2.get_rect(
            center=(land2x + land2.get_width() / 2, 600 + land2.get_height() / 2))

        if bird_rect.colliderect(platform_rect1) or bird_rect.colliderect(platform_rect2):

            g.hit.play(0)

            b = scorescreen()
            b.run(g.gameDisplay, g.scores)
            g.initialize()
            g.welcomeflag = 1
