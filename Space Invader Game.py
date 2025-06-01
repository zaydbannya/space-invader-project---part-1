import math
import pygame
import random
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("background.png")
pygame.display.set_caption("space invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
playerlmg = pygame.image.load("player.png")
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0
enemylmg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for _i in range(num_of_enemies):
    enemylmg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)
bulletlmg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = PLAYER_START_Y
bulletX_change = 0
bullet_state = "ready"
