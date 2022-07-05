#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Sonic Jump
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


class welcomescreen:

    def __init__(self, display):
        self.gameDisplay = display
        # Top left corner of the actual game, as it is surrounded by 2 black rectangles
        self.x_start = 350
        self.width = 490
        self.x_end = self.width + self.x_start
        self.height = 768
        # x coordinate and duplicate image x coordinate for 3 skies and land respectively.
        self.x1_x2 = [[self.x_start, self.x_start + self.width] for _ in range(4)]
        self.x_speeds = (0.5, 0.75, 1, 3)
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


    def run(self):
        black = (0, 0, 0)
        white = (255, 255, 255)
        clock = pygame.time.Clock()
        crashed = False
        # image load
        land = pygame.image.load("assets/land.png").convert()
        land1 = pygame.transform.scale(land, (self.width, 150))
        land2 = land1
        skyfill = pygame.image.load("assets/skyfill.png").convert()
        skyfill = pygame.transform.scale(skyfill, (self.width, 500))
        scoreboard = pygame.image.load("assets/scoreboard.png")
        scoreboard = pygame.transform.scale(scoreboard, (360, 450))
        replay = pygame.image.load("assets/replay.png")
        replay = pygame.transform.scale(replay, (150, 90))
        rules = pygame.image.load("assets/splash.png")
        font2 = pygame.font.Font("fonts/Arimo.ttf", 25)
        flag = 1
        birds = bird()
        button = pygame.image.load("assets/button.png")
        logo = pygame.image.load("assets/logo.png")
        logo = pygame.transform.scale(logo, (280, 80))

        # GAME LOOP BEGINS !!!
        while not crashed:
            # Gtk events
            while Gtk.events_pending():
                Gtk.main_iteration()
            for event in pygame.event.get():
                # totaltime+=timer.tick()
                if event.type == pygame.QUIT:
                    crashed = True
                if event.type == pygame.KEYDOWN and event.key == 273:
                    return

            mos_x, mos_y = pygame.mouse.get_pos()
            self.gameDisplay.fill(white)
            self.gameDisplay.blit(skyfill, (self.x_start, 0))
            for i in range(3):
                self.gameDisplay.blit(self.background[i][0], (self.x1_x2[i][0], self.y[i]))
                self.gameDisplay.blit(self.background[i][1], (self.x1_x2[i][1], self.y[i]))

            # Platform blit
            # Land 1 (with x coord x1x2[3][0]) and Land 2 (with x coord x1x2[3][1]) are duplicate images,
            # displayed next to each other and are moved. If one goes out of the screen, other covers for it.
            # y[3] contains the height of land.
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
            # bird display
            birds.display(self.gameDisplay, flag)
            self.gameDisplay.blit(rules, (500, 140))
            self.gameDisplay.blit(button, (700, 330))
            head3 = font2.render(_("Use this button ->"), 1, (white))
            self.gameDisplay.blit(head3, (480, 320))
            head3 = font2.render(_("to play the game"), 1, (white))
            self.gameDisplay.blit(head3, (480, 340))
            self.gameDisplay.blit(logo, (455, 30))
            # left and right black background patches
            pygame.draw.rect(self.gameDisplay, black, (0, 0, self.x_start, self.height))
            pygame.draw.rect(self.gameDisplay, black, (self.x_end, 0, 693, self.height))
            pygame.display.update()
            clock.tick(60)

            if crashed:                        # Game crash or Close check
                pygame.quit()
                sys.exit()

        # Just a window exception check condition
        event1 = pygame.event.get()
        if event1.type == pygame.QUIT:
            crashed = True

        if crashed:
            pygame.quit()
            sys.exit()
