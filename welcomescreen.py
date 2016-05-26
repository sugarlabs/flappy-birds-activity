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


import gtk
import pygame
import sys
from gettext import gettext as _

from elements import bird


class welcomescreen:

    def __init__(self, display):
        self.gameDisplay = display

    def run(self):

        black = (0, 0, 0)
        white = (255, 255, 255)
        clock = pygame.time.Clock()

        crashed = False

        # image load

        land = pygame.image.load("assets/land.png").convert()
        land1 = pygame.transform.scale(land, (490, 150))
        land2 = land1

        sky = pygame.image.load("assets/sky.png").convert()
        sky = pygame.transform.scale(sky, (490, 200))

        skyfill = pygame.image.load("assets/skyfill.png").convert()
        skyfill = pygame.transform.scale(skyfill, (490, 500))

        scoreboard = pygame.image.load("assets/scoreboard.png")
        scoreboard = pygame.transform.scale(scoreboard, (360, 450))

        land1x = 350
        land2x = 840

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

            while gtk.events_pending():
                gtk.main_iteration()
            for event in pygame.event.get():
                # totaltime+=timer.tick()
                if event.type == pygame.QUIT:
                    crashed = True

                if event.type == pygame.KEYDOWN and event.key == 273:
                    return

            # print "help"
            mos_x, mos_y = pygame.mouse.get_pos()

            self.gameDisplay.fill(white)

            self.gameDisplay.blit(skyfill, (350, 0))
            self.gameDisplay.blit(sky, (350, 400))

            # Platform blit
            self.gameDisplay.blit(land1, (land1x, 600))
            self.gameDisplay.blit(land2, (land2x, 600))

            land1x -= 3
            land2x -= 3

            if(land1x <= -140):
                land1x = 837

            if(land2x <= -140):
                land2x = 837

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

            pygame.draw.rect(self.gameDisplay, black, (0, 0, 350, 768))

            pygame.draw.rect(self.gameDisplay, black, (840, 0, 693, 768))

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


'''


if __name__ == "__main__":
    g = welcomescreen()
    g.run(gameDisplay,score)         

'''
