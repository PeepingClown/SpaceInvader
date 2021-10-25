import pygame
import random

#Initialize the pygame
pygame.init()

#Create the screen
screenWidth = 800
screenHeight = 600
screen=pygame.display.set_mode((screenWidth, screenHeight))

#Title and logo
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("./image/spaceship_bordered.png")
pygame.display.set_icon(icon)


#player
playerImg = pygame.image.load('./image/player.png')
playerX = 370
playerY = 480
playerxChange = 0
playeryChange = 0
moveStep = 0.3

#enemy
enemyImg = pygame.image.load("./image/enemy.png")
enemyX = random.randint(0,screenWidth)
enemyY = random.randint(50,150)
enemyxChange = 0.2
enemyyChange = 20

def player(x,y):
    screen.blit(playerImg, (x,y))

def enemy(x,y):
    screen.blit(enemyImg, (x,y))
#game Loop
running = True
while running:

    screen.fill((0,0,0))
    enemyX += 0.1

    # player boundary
    if playerX >= (screenWidth-32):
        playerX=(screenWidth-32)
    elif playerX <=0 :
        playerX = 0

    if playerY <= 0:
        playerY = 0
    elif playerY >= screenHeight-32:
        playerY = screenHeight-32

    #enemy boundary
    if enemyX >= (screenWidth-32):
        enemyxChange = -0.2
        enemyY += enemyyChange
    elif enemyX <=0 :
        enemyxChange = 0.2
        enemyY += enemyyChange


    if enemyY <= 0:
        enemyY = 0
    elif enemyY >= screenHeight-32:
        enemyY = screenHeight-32


    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerxChange = -moveStep
            if event.key == pygame.K_RIGHT:
                playerxChange = moveStep
            if event.key == pygame.K_UP:
                playeryChange = -moveStep
            if event.key == pygame.K_DOWN:
                playeryChange = moveStep
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerxChange = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playeryChange = 0

    playerX += playerxChange
    playerY += playeryChange

    enemyX += enemyxChange
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
