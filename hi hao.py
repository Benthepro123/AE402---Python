# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 19:23:31 2020

@author: edric
"""

import pygame
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

pygame.init()
size = (400,300)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("I hate Shawn")
done = False
clock = pygame.clock
x = 0
y = 0
while not done:
    for event in pygame.get():
        if event.type == pygame.QUIT:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                x+1
            elif keys[pygame.K_LEFT]:
                x-1
            elif keys[pygame.K_DOWN]:
                y+1
            elif keys[pygame.K_UP]:
                y-1
                
clock.tick(60)
        
pygame.draw.circle(screen,RED,(x,y),10)
pygame.QUIT()

                                