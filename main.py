import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('AI space')
icon = pygame.image.load('assets\icon.png')
pygame.display.set_icon(icon)

background = pygame.image.load('assets/background.jpg')

playerImg = pygame.image.load('assets\player.png')
playerX = 370
playerY = 480

enemyImg = pygame.image.load('assets\enemy.png')
enemyX = random.randint(10, 660)
enemyY = random.randint(10, 150)

bulletImg = pygame.image.load('assets/bullet.png')

class Bullet():
    def __init__(self, XPos, YPos):
        self.X = XPos
        self.Y = YPos
        
bullets = []

def player_movt(Xpos, Ypos):
    screen.blit(playerImg, (Xpos,Ypos))
    
def enemy_movt(Xpos, Ypos):
    screen.blit(enemyImg, (Xpos,Ypos))
enemyX_change = 0.1   
      
fire_time = 0  
            
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] and playerX<735:
        playerX += 0.5
    if keys[pygame.K_a] and 0<playerX:
        playerX -= 0.5
    if keys[pygame.K_SPACE]:
        if time.time() - fire_time >= 1:
            bullets.append(Bullet(playerX, playerY))
            fire_time = time.time()
        else:
            pass
    
    if enemyX > 735:
        enemyX_change = -0.1
        enemyY += 20
    elif enemyX < 0:
        enemyX_change = 0.1
        enemyY += 20
    enemyX += enemyX_change
        
    screen.fill((54, 69, 79))
    screen.blit(background, (0,0))
    player_movt(playerX, playerY)
    enemy_movt(enemyX, enemyY)
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(enemyX-20, enemyY-20, 40, 40),  2)
    for bullet in bullets:
        if bullet.Y <= 0:
            bullets.remove(bullet)
        else:
            screen.blit(bulletImg, (bullet.X, bullet.Y))
            bullet.Y -= 0.1
            
        if abs(bullet.X - enemyX) <= 20 and abs(bullet.Y - enemyY) <= 20:
            bullets.remove(bullet)
            print('enemy hit')
        
    pygame.display.update()