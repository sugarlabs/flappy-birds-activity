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


from pygame.locals import *


from scorescreen import *
from welcomescreen import *









class game:
    
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
            
            
            pygame.display.set_caption("Stick Hero")
            #gameicon=pygame.image.load('images/icon.png')
            #pygame.display.set_icon(gameicon)
            
            
        sprite=pygame.image.load("images/sprite.png")
        
        
        
        # Variable Initialization
        
        
        font_path = "fonts/comicsans.ttf"
        font_size = 40
        font1= pygame.font.Font(font_path, font_size)
        font2=pygame.font.Font("fonts/sans.ttf",25)
        font3=pygame.font.Font("fonts/sans.ttf",40)
        font4=pygame.font.Font("fonts/sans.ttf",20)
        
        
        
        color=[(153,50,204),(255,105,180),(255,215,0),\
                (0,255,127),(30,144,255),(255,69,0)]
        
        
        
        
        # VARIABLE INITIALIZATION
        
        
        herod=33
        
        fruitscore=0
        score=0
        
        
        #running  7 sprites
        
        running=[[8,11],[50,7],[93,9],[137,9]]
        
        runningwd=[[40,33],[41,37],[39,36],[40,33]]
        
        
        stops=   [10,55]
        stopwd= [23,38]
        
        
        #jumping 15 sprites
        
        jumping=[[39,59],[64,54],[95,58],[122,57],[156,57],[187,57],\
            [218,58],[249,57]]
        
        jumpingwd=[[23,22],[26,32],[24,25],\
            [29,26],[26,27],[26,29],[24,24],[30,26]]
        
        falls=[[284,54],[321,51],[355,51]]
        
        fallswd=[[26,32],[26,37],[30,37]]
        
        touchs=[[390,63],[427,65],[473,67]]
        touchswd=[[29,32],[28,29],[24,26]]
        
        
        
    
                    
        
        
        
        
        
        score=0
        maxscore=0
        
        
        
        
        if os.path.getsize("score.pkl") == 0:
            
            with open('score.pkl', 'wb') as output:
                pickle.dump(0, output, pickle.HIGHEST_PROTOCOL)
        
        
        with open('score.pkl', 'rb') as input:    #REading
            maxscore = pickle.load(input)
        
        
        i=0
        
        j=0
        k=0
        
        keyinit=0
        
        
        run=1
        jump=stop=0
        
        fall=touch=0
        
        r=s=j=0
        
        frame=5     # FRame rate
        
        
        sonicy=410
        
        inity=410
        velocity=0
        distance=150
        
        time=0
        fall=0
        down=0
        flag1=0
        
        
        f=t=0
        scoreflag=0
        
        
        
        jumpf=fallf=stopf=0   
        
        accf=0.21
        
        
        
        initialvelocity=8
        
        #distance=(initialvelocity**2)/(2*10)
        
        timefactor=0.02
        
        step=0
        
        velocity=10
        
        
        
        
        
        #pillar coordinte x
        
        time1=0
        
        
        chk=False
        factor=-1
        
        
        gap=150             # GAp for passage
        array=[230,300,230,300]
        pillardist=array[randint(0,1)]     #Distance between pillars
        
        
        thick1=200          #Thicknesss of the pillars
        
        thick2=180  
        
        thick3=250
        
        
        platx=350
        pillar1x=840+pillardist
        pillar2x=(pillar1x+thick1)+pillardist
        
        pillardist=array[randint(0,1)] 
        
        pillar3x=(pillar2x+thick2)+pillardist
        
        height1=200
        height2=350
        height3=400
        
        speed=4
        
        
        
        
        colorp=color[randint(0,5)]
        color1=color[randint(0,5)]
        while(color1==colorp):
            color1=color[randint(0,5)]
        
        color2=color[randint(0,5)]
        while(color2==color1):
            color2=color[randint(0,5)]
         
        
        color3=color[randint(0,5)]
        while(color3==color2):
            color3=color[randint(0,5)]
        
        
        
        pillarcolor=color1
        pillar2nd=pillar1x
        pillar2ndthick=thick1
        pillar2ndheight=height1
        lastheight=height1
            
        platformdrop=False
        
        
        pillartouch=pillar2nd
        pillartouchthick=pillar2ndthick
        
        
        
        pillarbegin=platx
        pillarbeginthick=490
        
        
        
        flag2=False
        sonicx=450
        basetouch=False
        fallflag=False
        
        
        
        heightlist=[200,250,300,350,400]
        
        
        font_path = "fonts/sans.ttf"
        font_size = 55
        font1= pygame.font.Font(font_path, font_size)
        font2=pygame.font.Font("fonts/sans.ttf",30)
        font3=pygame.font.Font("fonts/sans.ttf",40)
        font4=pygame.font.Font("fonts/sans.ttf",23)
        
        
        homef=1
        replay=0
        
        
        
        
        
        # Sound loads
        
        jumpsound=pygame.mixer.Sound("sound/sound-jump.ogg")
        bumpsound=pygame.mixer.Sound("sound/sound-bump.ogg")
        coinsound=pygame.mixer.Sound("sound/sound-coin.ogg")
        
        scoref=0
        
        
        
        
        
        
        
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
            
                
            
            
                    
            # HOme call
            
            if(homef==1):
                a=welcomescreen()
                a.run(gameDisplay)
                homef=0
            
            
            gameDisplay.fill(white)
            
            
            i+=1
            
            if(i>50):
                i=0
                
            
            
            
                
            if(run==1):
                if(i%frame==0):    
                    r+=1
                    if(r>=4):
                        r=0
            
            
                
            elif(jump==1):
                if(i%frame==0):
                    j+=1
                    if(j>=8):
                        j=0
                        
                        
            elif(fall==1):
                if(i%frame==0):
                    if(f<2):
                        f+=1
                        
                        
            elif(touch==1):
                if(i%frame==0):
                    if(t<2):
                        t+=1
                    
                        
                        
                        
                        
                        
            
            #print str(jump)+str(fall)
            
            #print velocity
            
            
            if((jumpf==1) and run!=1):
                
                #if(time<):          
                time+=1
                time1+=1
                
                if(velocity<=0 and chk==False):
                    chk=not chk
                    time=0
                    
                    factor*=-1
                    
                
                    
                if(time1<=40):       #jump sprite show
                    jump=1
                    stop=0
                    #keyinit=0
                if(time1>40):               #fall sprite display
                    fall=1
                    jump=0  
                    
                
                
                
                
                #velocity=initialvelocity+factor*(accf*(time/22))
                velocity=initialvelocity+(factor*accf*(time))
                
                #print (accf*(time/100))
                #sonicy+=factor*velocity
                sonicy=sonicy+factor*velocity
                
                
                
            elif(fallf==1):
                
                #print "help"
                time+=1
                fall=1
                jump=0
                stop=0
                run=0
                
                
            
                #velocity=initialvelocity+factor*(accf*(time/22))
                velocity=2+accf*(time)
                
                
                #print (accf*(time/100))
                #sonicy+=factor*velocity
                sonicy=sonicy+velocity
            
            
            
            
            
            
            
                
            #Keyboard Hit check
            
            
            if event.type==pygame.KEYDOWN and event.key==273 and keyinit==0 and step<2 :
                
                keyinit=1
                jumpsound.play(0)
               
                #print "hl"
                #print step
                
                
                if(step==0):    #First jump     
                    run=0
                    stopf=0
                    stop=0
                    jumpf=jump=1
                    fall=0
                    fallf=0
                    factor=-1
                    initialvelocity=8
                    time=time1=0
                    
                    
                elif(step==1):      #Second Jump
                    jump=1
                    
                    initialvelocity=7
                    time=0
                    time1=0
                    chk=False
                    
                    #jumpf=1
                    factor=-1
                    #fallf=0
                    #flag1=0
                    #time=0
                    #inity=sonicy
                    #initialvelocity=-velocity
                    #distance=distance/2
                    
                
                step+=1
                
                
                
                
                
                
                #print "help"
                
                
                            
            if event.type==pygame.KEYUP  and event.key==273 and keyinit==1:
                keyinit=0
                    
                #stickgrow.stop()
                #kick.stop()
                #kick.play()
                
            
            #print stop
                    
            
            
            if(run==1):
                
                sprite.set_clip(pygame.Rect(running[r][0], running[r][1],\
                    runningwd[r][0], runningwd[r][1])) 
            
            
            
            elif(stop==1):
                sprite.set_clip(pygame.Rect(stops[0], stops[1],\
                stopwd[0], stopwd[1])) 
            
            
              
            
            elif(jump==1):
                sprite.set_clip(pygame.Rect(jumping[j][0], jumping[j][1],\
                jumpingwd[j][0], jumpingwd[j][1]))
                
                
                
            elif(fall==1):
                sprite.set_clip(pygame.Rect(falls[f][0], falls[f][1],\
                fallswd[f][0], fallswd[f][1]))     
                
            
            elif(touch==1):
                sprite.set_clip(pygame.Rect(touchs[t][0], touchs[t][1],\
                touchswd[t][0], touchswd[t][1])) 
                
                
                
                
            # Colored Pillars Disp    
            
            if(pillar3x>700):
                pillar3rd=pillar3x
                pillar3thick=thick3
                lastcolor=color3
                lastheight=height3
                
            elif(pillar2x>700):
                pillar3rd=pillar2x
                pillar3thick=thick2
                lastcolor=color2
                lastheight=height2
                
            elif(pillar1x>700):
                pillar3rd=pillar1x
                pillar3thick=thick1
                lastcolor=color1
                lastheight=height1
                
                
                
            
                
                
            if(pillar1x<350-thick1):
                pillar1x=pillar3rd+pillar3thick+array[randint(0,3)]
                
                thick1=randint(180,250)
                color1=color[randint(0,5)]
                while(color1==lastcolor):
                    color1=color[randint(0,5)]
                
                height1=heightlist[randint(0,4)]
                while(height1==lastheight or (lastheight==400 and height1==200) or (lastheight==200 and height1==400) ):
                    height1=heightlist[randint(0,4)]
                    
                    
                
                
                
                    
            if(pillar2x<=350-thick2):
                pillar2x=pillar3rd+pillar3thick+array[randint(0,3)]
                #height2=heightlist[randint(0,4)]
                thick2=randint(180,250)
                color2=color[randint(0,5)]
                while(color2==lastcolor):
                    color2=color[randint(0,5)]
                
                height2=heightlist[randint(0,4)]
                while(height2==lastheight or (lastheight==400 and height2==200) or (lastheight==200 and height2==400)):
                    height2=heightlist[randint(0,4)]
                    
                    
                    
            
            if(pillar3x<=350-thick3):
                pillar3x=pillar3rd+pillar3thick+array[randint(0,3)]
                #height3=heightlist[randint(0,4)]
                thick3=randint(180,250)
                color3=color[randint(0,5)]
                while(color3==lastcolor):
                    color3=color[randint(0,5)]
                    
                height3=heightlist[randint(0,4)]
                while(height3==lastheight or (lastheight==400 and height3==200) or  (lastheight==200 and height3==400) ):
                    height3=heightlist[randint(0,4)]    
            
            
            if(platx+490<sonicx-90):
                platx=900
                pillarbegin=900
            
            if(platx>=-490 and platx<840):
                platx-=speed        
            
            pillar1x-=speed
            
            pillar2x-=speed
            
            pillar3x-=speed
            
            
            #print pillar1x
            
            
            
            pygame.draw.rect(gameDisplay,colorp,(platx,454,490,768))
            
            pygame.draw.rect(gameDisplay,color1,(pillar1x,0,thick1,height1))
            pygame.draw.rect(gameDisplay,color1,(pillar1x,height1+gap,thick1,768))
            
            pygame.draw.rect(gameDisplay,color2,(pillar2x,0,thick2,height2))
            pygame.draw.rect(gameDisplay,color2,(pillar2x,height2+gap,thick2,768))
            
            pygame.draw.rect(gameDisplay,color3,(pillar3x,0,thick3,height3))
            pygame.draw.rect(gameDisplay,color3,(pillar3x,height3+gap,thick3,768))
            
            rect1a=pygame.Rect(pillar1x,0,thick1,height1)
            rect1b=pygame.Rect(pillar1x,height1+gap,thick1,768)
            
            rect2a=pygame.Rect(pillar2x,0,thick2,height2)
            rect2b=pygame.Rect(pillar2x,height2+gap,thick2,768)
            
            rect3a=pygame.Rect(pillar3x,0,thick3,height3)
            rect3b=pygame.Rect(pillar3x,height3+gap,thick3,768)
            
            
            
            
            
            
                
            
            # Pillar Touch test
            
                
            #  Sonic Display
            
            

            draw_me = sprite.subsurface(sprite.get_clip()) #Extract the sprite you want

            #backdrop = pygame.Rect(0,0,350,768) #Create the whole screen so you can draw on it
            
            draw_me=pygame.transform.scale(draw_me,(draw_me.get_width()+10,draw_me.get_height()+10))
            
            
            gameDisplay.blit(draw_me,(sonicx,sonicy)) #'Blit' on the backdrop
            
            a=sonicx+(draw_me.get_width()/2)
            b=sonicy+(draw_me.get_height()/2)
            center=(a,b)
            
            sonic_rect=draw_me.get_rect(center=(a,b))
            
            
            
            
            # Current Scores Display
            
            
            scores=font4.render(str(score),1,black)
            gameDisplay.blit(scores,(790,20))
            
            
            
            # 2nd pillar test
            
            if(pillar1x<650 and pillar1x>=-thick1 ):
                pillarcolor=color1
                pillar2nd=pillar1x
                pillar2ndthick=thick1
                pillar2ndheight=height1
                
            
            if(pillar2x<650 and pillar2x>=-thick2):
                pillarcolor=color2
                pillar2nd=pillar2x
                pillar2ndthick=thick2
                pillar2ndheight=height2
                
                
            
            
            
            if(pillar3x<650 and pillar3x>=-thick3):
                pillarcolor=color3
                pillar2nd=pillar3x
                pillar2ndthick=thick3
                pillar2ndheight=height3
                
            
            
            
            # TRACKER DOTS 
            
            topleft=(sonicx,int(sonicy))
            topright=(int(sonicx+draw_me.get_width()),int(sonicy))
            
            bottomleft=(sonicx,int(sonicy+draw_me.get_height()))
            bottomright=(int(sonicx+draw_me.get_width()),int(sonicy+draw_me.get_height()))
            
                
            
            #pygame.draw.circle(gameDisplay,black,topleft ,3, 2)
            #pygame.draw.circle(gameDisplay,black, topright ,3, 2)
            #pygame.draw.circle(gameDisplay,black, bottomleft ,3, 2)
            #epygame.draw.circle(gameDisplay,black, bottomright ,3, 2)
            
            
            #Collision Test
            
            
            
            pillar_rect1=pygame.Rect(pillar2nd,0,pillar2ndthick,pillar2ndheight)
            pillar_rect2=pygame.Rect(pillar2nd,pillar2ndheight+gap, \
                                    pillar2ndthick,768)
            
            
            # Pillar side front upper collision
            
            
            if(sonicy+draw_me.get_height()>768  or (sonic_rect.colliderect(pillar_rect1)==True) or \
                 
                    ( sonic_rect.colliderect(pillar_rect2)==True and \
                    bottomright[0]<=pillar2nd+5 )  ):
                 
                 
                bumpsound.play(0) 
                 
                if(score>maxscore):
                    scoreflag=1
                    with open('score.pkl', 'wb') as output:
                        pickle.dump(score, output, pickle.HIGHEST_PROTOCOL)
                 
                
                #scorescreen call
                
                a=scorescreen()
                a=a.run(gameDisplay,score,scoreflag)
                
                
                if(a==1 or a==0):
                    
                    # Variables reinitialization
                    if(a==0):
                        homef=1
                    
                    score=0
        
                    maxscore=0
        
        
        
        
                    if os.path.getsize("score.pkl") == 0:
            
                        with open('score.pkl', 'wb') as output:
                            pickle.dump(0, output, pickle.HIGHEST_PROTOCOL)
        
        
                    with open('score.pkl', 'rb') as input:    #REading
                        maxscore = pickle.load(input)
        
        
                    i=0
        
                    j=0
                    k=0
        
                    keyinit=0
        
        
                    run=1
                    jump=stop=0
        
                    fall=touch=0
        
                    r=s=j=0
        
                    frame=5     # FRame rate
        
        
                    sonicy=410
        
                    inity=410
                    velocity=0
                    distance=150
        
                    time=0
                    fall=0
                    down=0
                    flag1=0
        
        
                    f=t=0
        
        
        
        
                    jumpf=fallf=stopf=0   
        
                    accf=0.21
        
        
        
                    initialvelocity=8
        
                    #distance=(initialvelocity**2)/(2*10)
        
                    timefactor=0.02
        
                    step=0
        
                    velocity=10
        
        
        
        
        
                    #pillar coordinte x
        
                    time1=0
        
        
                    chk=False
                    factor=-1
        
        
                    gap=150             # GAp for passage
                    array=[230,300,230,300]
                    pillardist=array[randint(0,1)]     #Distance between pillars
        
        
                    thick1=200          #Thicknesss of the pillars
        
                    thick2=180  
        
                    thick3=250
        
        
                    platx=350
                    pillar1x=840+pillardist
                    pillar2x=(pillar1x+thick1)+pillardist
        
                    pillardist=array[randint(0,1)] 
        
                    pillar3x=(pillar2x+thick2)+pillardist
        
                    height1=200
                    height2=350
                    height3=400
        
                    speed=4
        
        
        
        
                    colorp=color[randint(0,5)]
                    color1=color[randint(0,5)]
                    while(color1==colorp):
                        color1=color[randint(0,5)]
        
                    color2=color[randint(0,5)]
                    while(color2==color1):
                        color2=color[randint(0,5)]
         
        
                    color3=color[randint(0,5)]
                    while(color3==color2):
                        color3=color[randint(0,5)]
        
        
        
                    pillarcolor=color1
                    pillar2nd=pillar1x
                    pillar2ndthick=thick1
                    pillar2ndheight=height1
                    lastheight=height1
            
                    platformdrop=False
        
        
                    pillartouch=pillar2nd
                    pillartouchthick=pillar2ndthick
        
        
        
                    pillarbegin=platx
                    pillarbeginthick=490
        
        
        
                    flag2=False
                    sonicx=450
                    basetouch=False
                    fallflag=False
        
        
        
                    heightlist=[200,250,300,350,400]
        
        
                    scoref=0
                    scoreflag=0
                    replay=0
                
            
            
            # Pillar base touch
            
            if( sonic_rect.colliderect(pillar_rect2)==True and \
                        pillar2nd+5<bottomright[0] and basetouch==False ):
                 
                #print "helo"
                #print "hello"
                #if(platx==900):
                #    score+=1
                #    coinsound.play(0)
                
                run=1
                step=0
                fallf=stopf=jumpf=stop=jump=fall=0
                time=0
                time1=0
                chk=False
                fallflag=False
                    
                initialvelocity=8
                basetouch=True
                factor=-1
                    
                sonicy=pillar2ndheight+gap-draw_me.get_height()
            
            
            
            # Platform condition
            
            if( bottomleft[0]>platx and bottomleft[0]<=platx+490):
                
                if(bottomleft[1]>454):
                    
                    run=1
                    step=0
                    fallf=stopf=jumpf=stop=jump=fall=0
                    time=0
                    time1=0
                    chk=False
                    fallflag=False
                    
                    initialvelocity=8
                    #basetouch=True
                    factor=-1
                    
                    sonicy=454-draw_me.get_height()
                    
            
            
            if(basetouch==True and pillar2nd<sonicx):
                basetouch=False
            
            
            #Fall from platform
            
            if( fallflag==False and (pillar2nd+pillar2ndthick<sonicx or\
                platx+490<sonicx) and run==1):
                
                fallf=1
                fall=1
                run=stopf=stop=jump=jumpf=0
                time=0 
                time1=0
                factor=1
                basetouch=False
                
                
                
                fallflag=True
                
                #print "hello"
                
                
            
            
            #print str(fallflag)+str(run)c
            
            if(pillar2nd+5<sonicx and scoref==0):
                score+=1
                scoref=1
                coinsound.play(0)
                
            if(pillar2nd+5>sonicx and scoref==1):
                scoref=0
            
            
            
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

            