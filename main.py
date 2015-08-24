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
import gtk
import pickle
import pygame
import sys

from math import *

from random import *

from elements import *







class game:
  
  
    def initialize(self):
      
        self.flag=0
      
    
    
    
    def make(self):
        
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
            
            
            pygame.display.set_caption("Flappy Birds")
            #gameicon=pygame.image.load('images/icon.png')
            #pygame.display.set_icon(gameicon)
            
            
        
        
        
        # Variable Initialization
        
        
        font_path = "fonts/comicsans.ttf"
        font_size = 40
        font1= pygame.font.Font(font_path, font_size)
        font2=pygame.font.Font("fonts/sans.ttf",25)
        font3=pygame.font.Font("fonts/sans.ttf",40)
        font4=pygame.font.Font("fonts/sans.ttf",20)
        
        
        
        
        
        
        
        
        font_path = "fonts/sans.ttf"
        font_size = 55
        font1= pygame.font.Font(font_path, font_size)
        font2=pygame.font.Font("fonts/sans.ttf",30)
        font3=pygame.font.Font("fonts/sans.ttf",40)
        font4=pygame.font.Font("fonts/sans.ttf",23)
        
        
        
        
        
        
        
        
        # Sound loads
        
        jumpsound=pygame.mixer.Sound("sound/sound-jump.ogg")
        bumpsound=pygame.mixer.Sound("sound/sound-bump.ogg")
        coinsound=pygame.mixer.Sound("sound/sound-coin.ogg")
        
        
        
        
        #image loads
        
        
        land=pygame.image.load("assets/land.png").convert()
        land1=pygame.transform.scale(land,(490,120))
        land2=land1
        
        sky=pygame.image.load("assets/sky.png").convert()
        sky=pygame.transform.scale(sky,(490,200))
            
        
        skyfill=pygame.image.load("assets/skyfill.png").convert()
        skyfill=pygame.transform.scale(skyfill,(490,500))
        
        
        land1x=350
        land2x=840
        
        
        pillarlist=[]
        a=pillar()
        pillarlist.append(a)
        
        
        birds=bird()
        
        keyinit=0
        keytest=0
        
        
        
        # GAME LOOP BEGINS !!!
        
        while not crashed:
        #Gtk events
            
            while gtk.events_pending():
                gtk.main_iteration()
            for event in pygame.event.get():
            #totaltime+=timer.tick()
                if event.type == pygame.QUIT:
                    crashed=True
                
            
            mos_x,mos_y=pygame.mouse.get_pos() 
            
            #print "hello"
            
                
            
            
                    
            
            
            
            gameDisplay.fill(white)
            
            
            gameDisplay.blit(skyfill,(350,0))
            gameDisplay.blit(sky,(350,400))
            
            
            
            # Pillar Display
            for i in pillarlist:
                i.display(gameDisplay,pillarlist)
            
            
            
            
            
            # Platform blit
            gameDisplay.blit(land1,(land1x,600))
            gameDisplay.blit(land2,(land2x,600))
            
            land1x-=2
            land2x-=2
            
            if(land1x<=-140):
                land1x=840
                
            if(land2x<=-140):
                land2x=840
            
            
            
            if(keyinit==1):
                birds.jump(land1,land2)
            
            
            if event.type==pygame.KEYDOWN and event.key==273 and keytest==0:
                
                keyinit=keytest=1
                birds.t=0
                birds.angle=0
                #birds.u=birds.v
                
               
                            
            if event.type==pygame.KEYUP  and event.key==273 :
                
                keytest=0
                
            
            
            
            
            # bird display
            
            birds.display(gameDisplay)
            
            
            
            
            
            
            
            
            
            
            # BLACK RECTANGLES DISPLAY
                      
            pygame.draw.line(gameDisplay,black,(350,0),(350,768), 1)          
            pygame.draw.line(gameDisplay,black,(840,0),(840,768), 1)           
                      
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
    g = game()
    g.make()         

            