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

        if(self.x<295):
            pillarlist.remove(self)
    
        