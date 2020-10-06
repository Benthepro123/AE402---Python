# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 20:18:15 2020

@author: edric
"""

import pygame,random

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

pygame.init()

size = (400, 300)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("走動的方塊")

done = False
click = False
def randomColor():
    R = random.randint(0,255)
    G = random.randint(0,255)
    B = random.randint(0,255)


    return(R,G,B)


clock = pygame.time.Clock()
r = 0
rmax = 50
x = 0
y = 0
COLOR = BLACK
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            click = True
            r = 0
            Color = randomColor()
    

    screen.fill(WHITE)
    if click and r < rmax:
        pygame.draw.circle(screen,Color,pos,r)
        r+=1
    if r >= rmax:
           click = False
        
    pygame.display.flip()

    clock.tick(60)
pygame.quit()
