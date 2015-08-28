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

from welcomescreen import *

from scorescreen import *


pygame.init()


sound=True
        
try:
    pygame.mixer.init()
except Exception, err:
    sound=False
    print 'error with sound', err

wing=pygame.mixer.Sound("assets/sounds/wing.ogg")





class game:
    
    
        
    
  
    def initialize(self):
        
        
        sound=True
        
        try:
            pygame.mixer.init()
        except Exception, err:
            sound=False
            print 'error with sound', err
            
        
        
        info=pygame.display.Info()
        self.gameDisplay=pygame.display.get_surface()
        
        
        
        
        
        if not(self.gameDisplay):
            
            self.gameDisplay = pygame.display.set_mode((info.current_w,info.current_h))
            
            
            pygame.display.set_caption("Flappy Birds")
            #gameicon=pygame.image.load('images/icon.png')
            #pygame.display.set_icon(gameicon)
            
            
        
        
        
      
        self.flag=0
        self.scores=0
        
        self.land1x=350
        self.land2x=840
        
        
        self.pillarlist=[]
        a=pillar()
        self.pillarlist.append(a)
        
        
        self.birds=bird()
        
        self.keyinit=0
        self.keytest=0
        
        self.flag=0
        self.welcomeflag=1
        self.musicflag=False
    
    
    def make(self):
        
        
        
        
        black=(0,0,0)
        white=(255,255,255)
        clock=pygame.time.Clock()
        timer=pygame.time.Clock()
            
        crashed=False   
        disp_width = 600
        disp_height = 600
            
        press=0    
        
        
        
        
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
        
        hit=pygame.mixer.Sound("assets/sounds/hit.ogg")
        wing=pygame.mixer.Sound("assets/sounds/wing.ogg")
        point=pygame.mixer.Sound("assets/sounds/point.ogg")
        swoosh=pygame.mixer.Sound("assets/sounds/swoosh.ogg")
        die=pygame.mixer.Sound("assets/sounds/die.ogg")
        
        
        
        
        #image loads
        
        
        land=pygame.image.load("assets/land.png").convert()
        land1=pygame.transform.scale(land,(490,150))
        land2=land1
        
        sky=pygame.image.load("assets/sky.png").convert()
        sky=pygame.transform.scale(sky,(490,200))
            
        
        skyfill=pygame.image.load("assets/skyfill.png").convert()
        skyfill=pygame.transform.scale(skyfill,(490,500))
        
        
        
        
        
        
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
            
            
            if(self.welcomeflag==1):
                a=welcomescreen()
                a.run(self.gameDisplay)
                self.welcomeflag=0
                self.keyinit=1
            
            
                    
            
            
            
            self.gameDisplay.fill(white)
            
            
            self.gameDisplay.blit(skyfill,(350,0))
            self.gameDisplay.blit(sky,(350,400))
            
            
            
            # Pillar Display
            for i in self.pillarlist:
                i.display(self.gameDisplay,self.pillarlist,self.birds,self)
                
                
                if(self.welcomeflag==1):
                    a=welcomescreen()
                    a.run(self.gameDisplay)
                    self.welcomeflag=0
                    self.keyinit=1
                    
                    break
		    #pygame.display.update()
            	    #clock.tick(60)
            
            
            
            
            
            # Platform blit
            self.gameDisplay.blit(land1,(self.land1x,600))
            self.gameDisplay.blit(land2,(self.land2x,600))
            
            self.land1x-=3
            self.land2x-=3
            
            if(self.land1x<=-140):
                self.land1x=837
                
            if(self.land2x<=-140):
                self.land2x=837
            
            
            
            if(self.keyinit==1):
                self.birds.jump(land1,land2,self.land1x,self.land2x,self)
            
            if(self.welcomeflag==1):
                a=welcomescreen()
                a.run(self.gameDisplay)
                self.welcomeflag=0
                self.keyinit=1
		continue
		#pygame.display.update()
            	#clock.tick(60)
		
            
            
            
                
            
            
                #pygame.mixer.music.load("assets/sounds/wing.ogg")
                #pygame.mixer.music.play(0,0)
                #self.musicflag=not self.musicflag
            
            #print event
            
            if event.type==pygame.KEYDOWN and event.key==273 and self.keytest==0:
                #print "hellp"
                #self.musicflag=True
                #pygame.mixer.music.fadeout(10)
                
                
                
                #wing.fadeout(5)
                #wing.play(0)
                self.keyinit=self.keytest=1
                if(self.birds.t>25):
                    self.birds.angle=0
                
                self.birds.t=0
                #birds.u=birds.v
                
               
                            
            if event.type==pygame.KEYUP  and event.key==273 and self.musicflag==True:
                
                self.keytest=0
                self.musicflag=False
                
            
            
            if self.musicflag==False and event.type==pygame.KEYDOWN  and event.key==273: 
                pygame.mixer.music.load("assets/sounds/wing.ogg")
                pygame.mixer.music.play(0,0)
                self.musicflag=not self.musicflag
            
            
            
            
            
            # bird display
            
            self.birds.display(self.gameDisplay,self.flag)
            
            
            head3=font3.render(str(self.scores),1,(white))
            self.gameDisplay.blit(head3,(580,30))
            
            
            #print self.scores
            
            
            
            
            
            
            
            
            
            
            
            
            # BLACK RECTANGLES DISPLAY
                      
            pygame.draw.line(self.gameDisplay,black,(350,0),(350,768), 1)          
            pygame.draw.line(self.gameDisplay,black,(840,0),(840,768), 1)           
                      
            pygame.draw.rect(self.gameDisplay,black,(0,0,350,768))    
                    
            pygame.draw.rect(self.gameDisplay,black,(840,0,693,768))
            
            
            
            
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
    g.initialize()
    g.make()         

            
