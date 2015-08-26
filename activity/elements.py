import pygame

import sys

from random import *


class pillar(object):
    
    
    def __init__(self):
        self.gap=160
        self.x=840
        self.y=0   
        self.pillarup=pygame.image.load("assets/pipe-down.png").convert()
        self.pillardown=pygame.image.load("assets/pipe-up.png").convert()
        self.height=randint(80,350)
        self.pipeup=pygame.transform.scale(pygame.image.load("assets/pipe.png").convert(),(52-4,self.height))
        self.pipedown=pygame.transform.scale(pygame.image.load("assets/pipe.png").convert(),(52-4,768-self.height))
  
        
        
        
    def display(self,gameDisplay,pillarlist,birds):
        
        gameDisplay.blit(self.pipeup,(self.x+2, self.y))
        gameDisplay.blit(self.pillarup,(self.x,self.y+self.height))
    
        gameDisplay.blit(self.pillardown,(self.x,self.y+self.height+self.gap))
        gameDisplay.blit(self.pipedown,(self.x+2,self.y+self.height+self.gap+26))
    
        self.x-=3
        
        if(self.x==603):
            pillarlist.append(pillar())
        
        if(self.x<295):
            pillarlist.remove(self)
            
        
        
        #collision check
        
        
        bird_rect=birds.bird.get_rect(center=(birds.x+birds.bird.get_width()/2, \
                                        
                                            birds.y+birds.bird.get_height()/2))
        
        
        
        
        pipe1_rect=self.pipeup.get_rect(center=(self.x+2+self.pipeup.get_width()/2, \
                                               self.y+self.pipeup.get_height()/2))
        
        pillar1_rect=self.pillarup.get_rect(center=(self.x+self.pillarup.get_width()/2, \
                                            self.y+self.height+self.pillarup.get_height()/2))
        
        
        pillar2_rect=self.pillardown.get_rect(center=(self.x+self.pillardown.get_width()/2, \
            self.y+self.height+self.gap+self.pillardown.get_height()/2))
        
        
        pipe2_rect=self.pipedown.get_rect(center=(self.x+2+self.pipedown.get_width()/2, \
                    self.y+self.height+self.gap+26+self.pipedown.get_height()/2))
        
        
        if(bird_rect.colliderect(pipe1_rect) or bird_rect.colliderect(pipe2_rect) or \
            bird_rect.colliderect(pillar1_rect) or \
                bird_rect.colliderect(pillar2_rect)):
            sys.exit()
                                       
                                       
        
        
            
            
            
            
            
class bird(object):
    
    
    
    
    def __init__(self):
        
        self.x=400
        self.y=400
        self.t=0
        self.a=9.4
        self.u=9.2
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
        
        
      
    def jump(self,land1,land2,land1x,land2x):
        
        self.t+=1
        
        #if(self.v==0)
        
        if(self.v>0 and self.t>0 and self.t<25 and self.angle<=30):
            self.angle+=2
            
        if(self.t>25 and self.angle>-80):
            self.angle-=2
            
           
        
        # motion equation v=u-at
        
        self.v=self.u-(self.a/24)*(self.t)
        
            
        self.y-=self.v
        
        if(self.y<0):
            self.y=0
        
        
        
        #bird platform fall check
        
        bird_rect=self.bird.get_rect(center=(self.x+self.bird.get_width()/2,self.y+self.bird.get_height()/2))
        
        platform_rect1=land1.get_rect(center=(land1x+land1.get_width()/2,600+land1.get_height()/2))
        platform_rect2=land2.get_rect(center=(land2x+land2.get_width()/2,600+land2.get_height()/2))
        
        if (bird_rect.colliderect(platform_rect1)==True or \
            bird_rect.colliderect(platform_rect2)==True):
            sys.exit()
        
            
        
         
        
        
    
        