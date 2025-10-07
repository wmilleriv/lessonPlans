import sys
import pygame
from pygame.locals import *
import random


FPS=60

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

PURPLE=(200,0,255)
RED=(255,0,0)
GREEN=(0,255,0)

DISPLAY_SURFACE = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAY_SURFACE.fill(PURPLE)
pygame.display.set_caption("Dodger")

class Enemy(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height],pygame.SRCALPHA)
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)

    def move(self):
        self.rect.move_ip(0,10)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self, color, radius, x, y):
        super().__init__()
        self.color=color
        self.radius=radius
        self.image=pygame.Surface((radius*2,radius*2),pygame.SRCALPHA)
        pygame.draw.circle(self.image,self.color, (radius,radius),self.radius)
        self.rect=self.image.get_rect(center=(x,y))

    def update(self):

        keys=pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.move_ip(0,-5)
        if keys[pygame.K_s]:
            self.rect.move_ip(0,5)
        if keys[pygame.K_a]:
            self.rect.move_ip(-5,0)
        if keys[pygame.K_d]:
            self.rect.move_ip(5,0)
    
    def draw(self, surface):
        surface.blit(self.image,self.rect)

p1=Player(RED,20,SCREEN_WIDTH//2,SCREEN_HEIGHT//2)

e=Enemy(GREEN,10,30,SCREEN_WIDTH//3,SCREEN_HEIGHT//3)
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    p1.update()
    e.move()

    DISPLAY_SURFACE.fill(PURPLE)
    p1.draw(DISPLAY_SURFACE)
    e.draw(DISPLAY_SURFACE)

    pygame.display.update()
    pygame.time.Clock().tick(FPS)
