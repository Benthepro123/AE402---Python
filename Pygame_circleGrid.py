# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 19:14:31 2020

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
    
    for i in range (140,341,40):
        for a in range (140,341,40):
            pygame.draw.circle(screen,ORANGE,(a,i),20)
       
    pygame.display.flip()

pygame.quit()