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
        self.height=randint(200,400)
        self.pipeup=pygame.transform.scale(pygame.image.load("assets/pipe.png").convert(),(52-4,self.height))
        self.pipedown=pygame.transform.scale(pygame.image.load("assets/pipe.png").convert(),(52-4,768-self.height))
  
        
        
        
    def display(self,gameDisplay,pillarlist):
        
        gameDisplay.blit(self.pipeup,(self.x+2, self.y))
        gameDisplay.blit(self.pillarup,(self.x,self.y+self.height))
    
        gameDisplay.blit(self.pillardown,(self.x,self.y+self.height+self.gap))
        gameDisplay.blit(self.pipedown,(self.x+2,self.y+self.height+self.gap+26))
    
        self.x-=2
        
        if(self.x==630):
            pillarlist.append(pillar())
        
        if(self.x<295):
            pillarlist.remove(self)
            
            
class bird(object):
    
    a=9.8
    t=0
    
    def __init__(self):
        
        self.x=400
        self.y=400
        
        bird1=pygame.image.load("assets/bird/bird1.png").convert()
       
        bird2=pygame.image.load("assets/bird/bird2.png").convert()
       
        bird3=pygame.image.load("assets/bird/bird3.png").convert()
       
        bird4=pygame.image.load("assets/bird/bird4.png").convert()
       
        self.birdlist=[bird1,bird2,bird3,bird4]
       
       
    def display(self,gameDisplay):
            
        gameDisplay.blit(self.birdlist[0],(self.x,self.y))
        
    '''    
    def jump():
        
        t+=1
        
        v=10-a*(t/1000)
        self.y-=v
         
    '''     
         
         
        
        
    
        