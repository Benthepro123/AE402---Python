# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 19:53:56 2020

@author: edric
"""

import pygame
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
ORANGE = (255,165,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

pygame.init()
size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)
    pygame.draw.circle(screen,RED,(100,100),20)
    pygame.draw.circle(screen,YELLOW,(100,140),20)
    pygame.draw.circle(screen,ORANGE,(140,100),20)
    pygame.draw.circle(screen,GREEN,(140,140),20)
    pygame.display.flip()
pygame.quit()
