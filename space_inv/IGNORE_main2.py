import pygame
import random
import math

pygame.init()




screen = pygame.display.set_mode((800,600))
ship = pygame.image.load('ship.png')
ship2 = pygame.transform.scale(ship, (64, 95))

playerX = 370
playerY = 480
playerX_change = 0

def player(x,y):
    screen.blit(ship2,(x,y))
clock = pygame.time.Clock()


walkcount = 0

def redraw():
    global walkcount
    screen.fill((0,0,0))

    if walkcount+1 >= 27:
        walkcount = 0
    if event.key == pygame.K_LEFT:
        screen.blit(ship2,(x,y))
        walkcount += 1
    elif event.key == pygame.K_RIGHT:
        screen.blit(ship2,(x,y))
        walkcount += 1
    else:
        screen.blit(ship2,(x,y))

    pygame.display.update()






running = True
while running:

    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerX_change = -25

            if event.key == pygame.K_RIGHT:
                playerX_change = 25

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736

    player(playerX,playerY)
    redraw()





#
