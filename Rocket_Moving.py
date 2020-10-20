
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 20:14:02 2020

@author: edric
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pygame

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

pygame.init()

size = (400, 300)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("走動的方塊")

clock = pygame.time.Clock()
bg_position = [0,0]
bg_image = pygame.image.load("saturn_family1.jpg")
bg_image_SMALL = pygame.transform.scale(bg_image, (400, 300))
spaceship_image = pygame.image.load("playerShip1_orange.png")
done = False
    

x = 0
y = 0

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
            
    screen.blit(bg_image_SMALL,bg_position)
    player_pos = pygame.mouse.get_pos()
    x = player_pos[0]
    y = player_pos[1]

    screen.blit(spaceship_image,[x,y])


    pygame.display.flip()

    clock.tick(60)
pygame.quit()
