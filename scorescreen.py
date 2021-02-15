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

import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import pickle
import pygame
import sys
from gettext import gettext as _


class scorescreen:

    def run(self, gameDisplay, scores, sound):
        black = (0, 0, 0)
        white = (255, 255, 255)
        red = (255, 0, 0)
        clock = pygame.time.Clock()
        crashed = False
        press = 0
        # image load
        land = pygame.image.load("assets/land.png").convert()
        land1 = pygame.transform.scale(land, (490, 150))
        sky = pygame.image.load("assets/sky.png").convert()
        sky = pygame.transform.scale(sky, (490, 200))
        skyfill = pygame.image.load("assets/skyfill.png").convert()
        skyfill = pygame.transform.scale(skyfill, (490, 500))
        scoreboard = pygame.image.load("assets/scoreboard.png")
        scoreboard = pygame.transform.scale(scoreboard, (360, 450))
        land1x = 350
        replay = pygame.image.load("assets/replay.png")
        replay = pygame.transform.scale(replay, (150, 90))

        # font load
        font2 = pygame.font.Font("fonts/Arimo.ttf", 30)

        # Scores load
        if not os.path.exists("score.pkl"):
            open('score.pkl', 'w+')
        if os.path.getsize("score.pkl") == 0:
            with open('score.pkl', 'wb') as output:
                pickle.dump(0, output, pickle.HIGHEST_PROTOCOL)
        with open('score.pkl', 'rb') as input:  # REading
            maxscore = pickle.load(input)

        newflag = 0

        if(scores > maxscore):
            with open('score.pkl', 'wb') as output:
                pickle.dump(scores, output, pickle.HIGHEST_PROTOCOL)
            maxscore = scores
            newflag = 1

        swoosh = pygame.mixer.Sound("assets/sounds/swoosh.ogg")

        # GAME LOOP BEGINS !!!
        while not crashed:
            # Gtk events
            while Gtk.events_pending():
                Gtk.main_iteration()
            for event in pygame.event.get():
                # totaltime+=timer.tick()
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if sound:
                        swoosh.play(0)
                    return 1

            # print "help"
            mos_x, mos_y = pygame.mouse.get_pos()
            gameDisplay.fill(white)
            gameDisplay.blit(skyfill, (350, 0))
            gameDisplay.blit(sky, (350, 400))

            # Platform blit
            gameDisplay.blit(land1, (land1x, 600))
            gameDisplay.blit(scoreboard, (420, 100))
            gameDisplay.blit(replay, (530, 450))

            if replay.get_rect(
                    center=(530 + (replay.get_width() / 2),
                            450 + (replay.get_height() / 2))
            ).collidepoint(mos_x, mos_y):
                gameDisplay.blit(
                        pygame.transform.scale(
                            replay, (
                                replay.get_width() + 4,
                                replay.get_height() + 4)
                            ),
                        (530 - 2, 450 - 2)
                )
                if(pygame.mouse.get_pressed())[0] == 1 and press == 0:
                    return
            # print scores
            scoress = font2.render(str(scores), 2, black)
            gameDisplay.blit(scoress, (630, 265))

            if(newflag == 1):
                maxscores = font2.render(
                    str(maxscore) + _("  NEW!"), 2, red)
            else:
                maxscores = font2.render(str(maxscore), 2, black)

            gameDisplay.blit(maxscores, (630, 330))
            # left and right black background patches
            pygame.draw.rect(gameDisplay, black, (0, 0, 350, 768))
            pygame.draw.rect(gameDisplay, black, (840, 0, 693, 768))
            pygame.display.update()
            clock.tick(60)
