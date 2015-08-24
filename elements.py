import pygame

import sys

from random import *


class pillar(object):
    
    
    def __init__(self):
        self.gap=150
        self.x=840
        self.y=0   
        self.pillarup=pygame.image.load("assets/pipe-down.png").convert()
        self.pillardown=pygame.image.load("assets/pipe-up.png").convert()
        self.height=randint(100,400)
        self.pipeup=pygame.transform.scale(pygame.image.load("assets/pipe.png").convert(),(52-4,self.height))
        self.pipedown=pygame.transform.scale(pygame.image.load("assets/pipe.png").convert(),(52-4,768-self.height))
  
        
        
        
    def display(self,gameDisplay,pillarlist):
        
        gameDisplay.blit(self.pipeup,(self.x+2, self.y))
        gameDisplay.blit(self.pillarup,(self.x,self.y+self.height))
    
        gameDisplay.blit(self.pillardown,(self.x,self.y+self.height+self.gap))
        gameDisplay.blit(self.pipedown,(self.x+2,self.y+self.height+self.gap+26))
    
        self.x-=3
        
        if(self.x==630):
            pillarlist.append(pillar())
        
        if(self.x<295):
            pillarlist.remove(self)
            
            
class bird(object):
    
    
    
    
    def __init__(self):
        
        self.x=400
        self.y=400
        self.t=0
        self.a=9.8
        self.u=10
        self.v=10
        self.frame=0
        self.angle=0
        
        self.bird=bird1=pygame.image.load("assets/bird/bird1.png").convert()
       
        bird2=pygame.image.load("assets/bird/bird2.png").convert()
       
        bird3=pygame.image.load("assets/bird/bird3.png").convert()
       
        bird4=pygame.image.load("assets/bird/bird4.png").convert()
       
        self.birdlist=[bird1,bird2,bird3,bird4]
       
       
    def display(self,gameDisplay):
        
        self.bird=pygame.transform.rotate(self.birdlist[int(self.frame/8)],self.angle)
        gameDisplay.blit(self.bird,(self.x,self.y))
        self.frame+=1
        if(int(self.frame/8)==4):
            self.frame=0
        
        
      
    def jump(self,land1,land2):
        
        self.t+=1
        
        if(self.v>0):
            self.angle+=1
        
        # motion equation v=u-at
        
        self.v=self.u-(self.a/24)*(self.t)
        
            
        self.y-=self.v
        
        
        #bird platform fall check
        
        bird_rect=self.bird.get_rect(center=(self.x+self.bird.get_width(),self.y+self.bird.get_height()))
        
        platform_rect1=land1.get_rect(center=(land1.get_width(),land1.get_height()))
        platform_rect2=land2.get_rect(center=(land2.get_width(),land2.get_height()))
        
        if (bird_rect.colliderect(platform_rect1)==True or \
            bird_rect.colliderect(platform_rect2)==True):
            sys.exit()
        
            
        
         
        
        
    
        