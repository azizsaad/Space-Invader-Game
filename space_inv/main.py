
import pygame
import random
import math

pygame.init()

# clock=pygame.time.Clock()
# FPS = 60

screen = pygame.display.set_mode((800,600))

background = pygame.image.load('bg.png')

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

ship = pygame.image.load('ship.png')
ship2 = pygame.transform.scale(ship, (64, 95))

enemy = pygame.image.load('enemy.png')
enemy2 = pygame.transform.scale(enemy, (64, 90))
enemy3 = enemy2
enemy3 = []

bull = pygame.image.load('bullet.png')
bullet = pygame.transform.scale(bull, (32, 32))

playerX = 370
playerY = 480
playerX_change = 0

enemX = []
enemY = []
enemX_change = []
enemY_change = []

num_of_enemies = 4

for i in range(num_of_enemies):
    enemy3.append(enemy2)
    enemX.append(random.randint(0,800))
    enemY.append(random.randint(60,160))
    enemX_change.append(25)
    enemY_change.append(0)


bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = -50
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('Comic Sans MS.ttf',40)
textX = 10
textY = 10

over_font = pygame.font.Font('Comic Sans MS.ttf',300)


def show_score(x,y):
    score = font.render("Score:" + str(score_value), True, (0,255,255))
    screen.blit(score,(x,y))

def game_over_text():
    over_text = font.render("GAME OVER! Score: " + str(score_value), True, (0,0,255))
    screen.blit(over_text,(100,250))



def player(x,y):
    screen.blit(ship2,(x,y))

def enem(x,y,i):
    screen.blit(enemy3[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet,(x+16,y+10))



def isCollision(enemX,enemY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemX-bulletX,2))+(math.pow(enemY-bulletY,2)))
    if distance < 40:
        return True
    else:
        return False



running = True
while running:

    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerX_change = -25



            if event.key == pygame.K_RIGHT:
                playerX_change = 25

            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736

    for i in range(num_of_enemies):

        if enemY[i] > 400:
            for j in range(num_of_enemies):
                enemY[j] = 2000
            game_over_text()
            break


        enemX[i] += enemX_change[i]
        enemY[i]  += enemY_change[i]

        if enemX[i]  <= 0:
            enemX_change[i]  = 25
            enemY_change[i]  = 3
        elif enemX[i]  >= 736:
            enemX_change[i]  = -25
            enemY_change[i]  = 3

        collision = isCollision(enemX[i],enemY[i],bulletX,bulletY)

        if collision:
            bulletY = 480
            bullet_state = 'ready'
            score_value += 1
            enemX[i] = random.randint(0,735)
            enemY[i] = random.randint(60,140)

        enem(enemX[i],enemY[i],i)


    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'

    if bullet_state is 'fire':
        fire_bullet(bulletX,bulletY)
        bulletY += bulletY_change


    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()






#
