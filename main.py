#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Flappy Birds
# Copyright (C) 2015  Utkarsh Tiwari
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Contact information:
# Utkarsh Tiwari    iamutkarshtiwari@gmail.com


import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import pygame
import sys
from gettext import gettext as _

from elements import bird
from elements import pillar
from elements import load_elements_images
from welcomescreen import welcomescreen


class game:

    def __init__(self):
        pass

    def initialize(self):
        self.flag = 0
        self.scores = 0
        # Top left corner of the actual game, as it is surrounded by 2 black rectangles
        self.x_start = 350
        self.width = 490
        self.x_end = self.width + self.x_start
        self.height = 768
        # x coordinate and duplicate image x coordinate for 3 skies and land respectively.
        self.x1_x2 = [[self.x_start, self.x_start + self.width] for _ in range(4)]
        self.x_speeds = (0.5, 0.75, 1, 3)

        self.keyinit = 0
        self.keytest = 0
        self.flag = 0
        self.welcomeflag = 1
        self.musicflag = False
        pygame.init()
        self.sound = True
        try:
            pygame.mixer.init()
        except Exception as err:
            self.sound = False
            print('error with sound', err)
        self.info = pygame.display.Info()
        self.gameDisplay = pygame.display.get_surface()

        if not(self.gameDisplay):
            self.gameDisplay = pygame.display.set_mode(
                (self.info.current_w, self.info.current_h))
            pygame.display.set_caption(_("Flappy Birds"))

        self.hit = pygame.mixer.Sound("assets/sounds/hit.ogg")
        self.point = pygame.mixer.Sound("assets/sounds/point.ogg")
        self.wing = pygame.mixer.Sound("assets/sounds/wing.ogg")
        self.swoosh = pygame.mixer.Sound("assets/sounds/swoosh.ogg")
        self.die = pygame.mixer.Sound("assets/sounds/die.ogg")

        self.font_path = "fonts/Arimo.ttf"
        self.font_size = 55
        self.font1 = pygame.font.Font(self.font_path, self.font_size)
        self.font2 = pygame.font.Font("fonts/Arimo.ttf", 30)
        self.font3 = pygame.font.Font("fonts/Arimo.ttf", 40)
        self.font4 = pygame.font.Font("fonts/Arimo.ttf", 23)

        self.background_actual_height = pygame.image.load("assets/sky.png").get_height()
        self.background_scaled_height = 200
        # Overlapped image for the combined background should be scaled to 200.
        self.scaling_factor = self.background_scaled_height / self.background_actual_height

        background = [
            pygame.image.load("assets/sky3.png").convert(),
            pygame.image.load("assets/sky2.png").convert(),
            pygame.image.load("assets/sky1.png").convert_alpha()
        ]
        background = list(
            map(lambda img: pygame.transform.scale(
                img, (self.width, int(img.get_height() * self.scaling_factor))
            ), background)
        )

        # Y coodinates of 3 skies and land respectively.
        self.y = (
            400,
            400 + background[0].get_height(),
            400 + self.background_scaled_height - background[2].get_height(),
            400 + self.background_scaled_height,
        )
        # Duplicate each image so images can be moved, if one goes out of screen, other covers for it.
        self.background = [(i, i) for i in background]

        # Load the images for elements
        load_elements_images()
        self.birds = bird()
        self.pillarlist = []
        a = pillar()
        self.pillarlist.append(a)

    def make(self):
        self.initialize()
        # Variable Initialization
        black = (0, 0, 0)
        white = (255, 255, 255)
        clock = pygame.time.Clock()
        crashed = False

        # Sound loads
        self.hit = pygame.mixer.Sound("assets/sounds/hit.ogg")
        self.point = pygame.mixer.Sound("assets/sounds/point.ogg")

        # image loads
        land1 = land2 = pygame.transform.scale(pygame.image.load("assets/land.png").convert(), (self.width, 150))
        skyfill = pygame.transform.scale(pygame.image.load("assets/skyfill.png").convert(), (self.width, 500))

        # GAME LOOP BEGINS !!!
        while not crashed:
            # Gtk events
            while Gtk.events_pending():
                Gtk.main_iteration()
            for event in pygame.event.get():
                # totaltime+=timer.tick()
                if event.type == pygame.QUIT:
                    crashed = True
            mos_x, mos_y = pygame.mouse.get_pos()
            if self.welcomeflag == 1:
                a = welcomescreen(self.gameDisplay)
                a.run()
                self.welcomeflag = 0
                self.keyinit = 1

            self.gameDisplay.fill(white)
            self.gameDisplay.blit(skyfill, (self.x_start, 0))
            for i in range(3):
                self.gameDisplay.blit(self.background[i][0], (self.x1_x2[i][0], self.y[i]))
                self.gameDisplay.blit(self.background[i][1], (self.x1_x2[i][1], self.y[i]))

            # Pillar Display
            for i in self.pillarlist:
                i.display(self.gameDisplay, self.pillarlist, self.birds, self)
                if(self.welcomeflag == 1):
                    a = welcomescreen(self.gameDisplay)
                    a.run()
                    self.welcomeflag = 0
                    self.keyinit = 1
                    break

            # Platform blit
            # Land 1 (with x coord x1x2[3][0]) and Land 2 (with x coord x1x2[3][1]) are displayed next to each 
            # other and are moved such that if one goes out of the screen, it is moved to the other side of the 
            # screen. y[3] contains the height of land.
            self.gameDisplay.blit(land1, (self.x1_x2[3][0], self.y[3]))
            self.gameDisplay.blit(land2, (self.x1_x2[3][1], self.y[3]))
            
            # Similar logic to move the 3 sky background for parallax effect.
            for i, speed in enumerate(self.x_speeds):
                self.x1_x2[i][0] -= speed
                self.x1_x2[i][1] -= speed
                if(self.x1_x2[i][0] <= -140):
                    self.x1_x2[i][0] = 837
                if(self.x1_x2[i][1] <= -140):
                    self.x1_x2[i][1] = 837

            if(self.keyinit == 1):
                self.birds.jump(land1, land2, self.x1_x2[0][0], self.x1_x2[0][1], self)
            if(self.welcomeflag == 1):
                a = welcomescreen(self.gameDisplay)
                a.run()
                self.welcomeflag = 0
                self.keyinit = 1
                continue
            if event.type == pygame.KEYDOWN and event.key == 273 and self.keytest == 0:
                self.keyinit = self.keytest = 1
                if(self.birds.t > 25):
                    self.birds.angle = 0
                self.birds.t = 0
            if event.type == pygame.KEYUP and event.key == 273 and self.musicflag:
                self.keytest = 0
                self.musicflag = False
            if not(self.musicflag) and event.type == pygame.KEYDOWN and event.key == 273:
                pygame.mixer.music.load("assets/sounds/wing.ogg")
                pygame.mixer.music.play(0, 0)
                self.musicflag = True

            # bird display
            self.birds.display(self.gameDisplay, self.flag)
            head3 = self.font3.render(str(self.scores), 1, (white))
            self.gameDisplay.blit(head3, (580, 30))

            # BLACK RECTANGLES DISPLAY
            pygame.draw.line(self.gameDisplay, black, (self.x_start, 0), (self.x_start, self.height), 1)
            pygame.draw.line(self.gameDisplay, black, (self.x_end, 0), (self.x_end, self.height), 1)
            pygame.draw.rect(self.gameDisplay, black, (0, 0, self.x_start, self.height))
            pygame.draw.rect(self.gameDisplay, black, (self.x_end, 0, 693, self.height))
            pygame.display.update()
            clock.tick(60)

            if crashed:                                   # Game crash or Close check
                pygame.quit()
                sys.exit()

        # Just a window exception check condition
        event1 = pygame.event.get()
        if event1.type == pygame.QUIT:
            crashed = True

        if crashed:
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    g = game()
    g.make()
