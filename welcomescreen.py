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




import os
import gtk
import pickle
import pygame
import sys

from math import *

from random import *

from elements import *







  
pygame.init()
sound=True
        
try:
    pygame.mixer.init()
except Exception, err:
    sound=False
    print 'error with sound', error
            
black=(0,0,0)
white=(255,255,255)
clock=pygame.time.Clock()
timer=pygame.time.Clock()
            
crashed=False   
disp_width = 600
disp_height = 600
            
press=0    
            
gameDisplay=pygame.display.get_surface()
        
if not(gameDisplay):
    info=pygame.display.Info()
    gameDisplay = pygame.display.set_mode((info.current_w,info.current_h))
            
    #pygame.display.set_caption("Make Them Fall")
    #gameicon=pygame.image.load('data/images/icon.png')
    #pygame.display.set_icon(gameicon)

#back=pygame.image.load('background/back6.jpg')
fruitscore=0
score=0








class welcomescreen:

    def run(self,gameDisplay,score):
        
        pygame.init()
        sound=True
        
        try:
            pygame.mixer.init()
        except Exception, err:
            sound=False
            print 'error with sound', err
            
        black=(0,0,0)
        white=(255,255,255)
        clock=pygame.time.Clock()
        timer=pygame.time.Clock()
            
        crashed=False   
        disp_width = 600
        disp_height = 600
            
        press=0    
        
        info=pygame.display.Info()
        gameDisplay=pygame.display.get_surface()
        
        
        if not(gameDisplay):
            
            gameDisplay = pygame.display.set_mode((info.current_w,info.current_h))
            
            
        #image load    
        
        land=pygame.image.load("assets/land.png").convert()
        land1=pygame.transform.scale(land,(490,120))
        land2=land1
        
        sky=pygame.image.load("assets/sky.png").convert()
        sky=pygame.transform.scale(sky,(490,200))
            
        
        skyfill=pygame.image.load("assets/skyfill.png").convert()
        skyfill=pygame.transform.scale(skyfill,(490,500))
        
        
        scoreboard=pygame.image.load("assets/scoreboard.png")
        scoreboard=pygame.transform.scale(scoreboard,(360,450))
        
        land1x=350
        land2x=840
        
        
        replay=pygame.image.load("assets/replay.png")
        replay=pygame.transform.scale(replay,(150,90))
        
        
        rules=pygame.image.load("assets/splash.png")
            
        
        
        
        #font load
        
        '''
        font_path = "fonts/sans.ttf"
        font_size = 55
        font1= pygame.font.Font(font_path, font_size)
        font2=pygame.font.Font("fonts/sans.ttf",30)
        font3=pygame.font.Font("fonts/sans.ttf",30)
        font4=pygame.font.Font("fonts/sans.ttf",20)
        '''
       
        '''
        
        with open('score.pkl', 'rb') as input:    #REading
            maxscore = pickle.load(input)
        '''    
        
        
        buttonsound=pygame.mixer.Sound("sound/sound-button.ogg")
        
        birds=bird()
        
        button=pygame.image.load("assets/button.png")
        
        
        
        # GAME LOOP BEGINS !!!
        
        while not crashed:
        #Gtk events
            
            while gtk.events_pending():
                gtk.main_iteration()
            for event in pygame.event.get():
            #totaltime+=timer.tick()
                if event.type == pygame.QUIT:
                    crashed=True
                    
                if event.type==pygame.KEYDOWN and event.key==273:
                    return 1
                    
                
            #print "help"
            mos_x,mos_y=pygame.mouse.get_pos() 
            
            #print event
            
            
                
            gameDisplay.fill(white)
           
            gameDisplay.blit(skyfill,(350,0))
            gameDisplay.blit(sky,(350,400))
            
             # Platform blit
            gameDisplay.blit(land1,(land1x,600))
            gameDisplay.blit(land2,(land2x,600))
            
            land1x-=3
            land2x-=3
            
            if(land1x<=-140):
                land1x=837
                
            if(land2x<=-140):
                land2x=837
            
            
                           
            birds.display(gameDisplay)
            
            gameDisplay.blit(rules,(500,150))
            gameDisplay.blit(button,(500,450))
            
           
           
            #left and right black background patches
                      
            pygame.draw.rect(gameDisplay,black,(0,0,350,768))    
                    
            pygame.draw.rect(gameDisplay,black,(840,0,693,768))
            
            
            
            
            
            
            
            
            
            pygame.display.update()
            clock.tick(60)
     
            if crashed==True:                                   # Game crash or Close check
                pygame.quit()
                sys.exit()
     
     
     
     
        # Just a window exception check condition

        event1=pygame.event.get()                                 
        if event1.type == pygame.QUIT:
            crashed=True
   
        if crashed==True:
            pygame.quit()
            sys.exit()






if __name__ == "__main__":
    g = welcomescreen()
    g.run(gameDisplay,score)         


