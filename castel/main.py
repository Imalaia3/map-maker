from platform import python_branch
from time import pthread_getcpuclockid
import pygame
from pygame.locals import *
import os
import sys
import math
import textureloader
import csv
from settings import *

SCREEN = pygame.display.set_mode((800,800))
LAYERS = [None,None,None] #3 Empty Layers

def setup():
    global GLOBAL_TLIST
    pygame.init()
    GLOBAL_TLIST = textureloader.setup_texture('/data/textures')
    
def myround(x, base=32):
    return base * round(x/base)


MAPDATA = "0"*(50)
MAPDATA+=","
MAPDATA = MAPDATA*(50)
def read_map(TMAP):
	n = 50
	DATA = TMAP.split(",")
	MAP=[]

	for row in DATA:
		MAP.append(list(row))
	return MAP






def savemap(MD,sp):
    mp = MD
    tos=""
    for line in mp:
        for char in line:
            tos+=char
        tos+=","

    with open(sp,"w+") as data:
        data.write(tos)
        data.close()






def main():
    global monedown,mthreedown
    monedown = False
    mthreedown = False
    maps=read_map(MAPDATA)
    while True:
        #maps=read_map(MAPDATA)
        SCREEN.fill(WHITE)

        x,y=0,0
        for row in maps:
            x=0
            for tile in row:
                if tile == "0":
                    pass
                if tile == "1":
                    SCREEN.blit(GLOBAL_TLIST["brick"],(x*32,y*32))

                x+=1

            y+=1
                
        
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    font = pygame.font.Font('freesansbold.ttf', 14)
                    green = (0, 255, 0)
                    blue = (0, 0, 128)
                    savepath = "/home/imalaia3/Desktop/castel/demo.ms"
                    running=True
                    while running:
                        SCREEN.fill(WHITE)

                        text = font.render('Save as...', True, (0,0,0))
                        textRect = text.get_rect()
                        textRect.center = (800 // 2, 800 // 2-100)
                        SCREEN.blit(text, textRect)
                        sp_text = font.render(savepath, True, (0,0,0))
                        spRect = sp_text.get_rect()
                        spRect.center = (800 // 2, 800 // 2-50)
                        SCREEN.blit(sp_text, spRect)



                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit(0)

                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    running=False
                                elif event.key == pygame.K_BACKSPACE:
                                    savepath = savepath[:-1]
                                elif event.key == pygame.K_RETURN:
                                    print("Saving...")
                                    savemap(maps,savepath)
                                else:
                                    savepath += event.unicode



                        

                        pygame.display.flip()

                if event.key == K_l:
                    with open("demo.ms") as fl:
                        maps=read_map(fl.read())
                        #print(fl.read())
                        fl.close()









            if event.type == MOUSEBUTTONDOWN:
                pos =  pygame.mouse.get_pos()
                if event.button == 1:
                    monedown=True
                if event.button == 3:
                    mthreedown=True
            if event.type == MOUSEBUTTONUP:
                pos =  pygame.mouse.get_pos()
                if event.button == 1:
                    monedown=False
                if event.button == 3:
                    mthreedown=False




                
                
        if monedown:
            pos =  pygame.mouse.get_pos()
            mx = myround(pos[0])
            my = myround(pos[1])     
            maps[my//32][mx//32] = "1"

        if mthreedown:
            pos =  pygame.mouse.get_pos()
            mx = myround(pos[0])
            my = myround(pos[1])     
            maps[my//32][mx//32] = "0"
         
         
                #SCREEN.blit(GLOBAL_TLIST["brick"],(mx,my))

        pygame.display.flip()






if __name__ == "__main__":
    setup()
    main()