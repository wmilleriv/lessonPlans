import sys
import pygame
from pygame.locals import *
import random, time


FPS=60

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

PURPLE=(200,0,255)
RED=(255,0,0)
GREEN=(0,255,0)

SPEED=5

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
        if self.rect.width>self.rect.height:
            self.rect.move_ip(0,10)
        else:
            self.rect.move_ip(10,0)

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

    def move(self):

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

all_sprites=pygame.sprite.Group()
enemies=pygame.sprite.Group()

def addEnemy(all_sprites,enemies): 
    eVert=Enemy(GREEN,10,30,0,random.randint(40,SCREEN_WIDTH-40))
    eHorizontal=Enemy(GREEN,30,10,random.randint(40,SCREEN_HEIGHT-40),0)
    
    enemies.add(eVert)
    enemies.add(eHorizontal)
    all_sprites.add(p1)
    all_sprites.add(eVert)
    all_sprites.add(eHorizontal)

INCREASE_SPEED = pygame.USEREVENT+1
pygame.time.set_timer(INCREASE_SPEED,1000)

while True:
    for event in pygame.event.get():
        if event.type==INCREASE_SPEED:
            SPEED+=2
            addEnemy(all_sprites,enemies)
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

    DISPLAY_SURFACE.fill(PURPLE)

    for entity in all_sprites:
        DISPLAY_SURFACE.blit(entity.image, entity.rect)
        entity.move()
        entity.draw(DISPLAY_SURFACE)

    #collision detection
    if pygame.sprite.spritecollideany(p1, enemies):
        DISPLAY_SURFACE.fill(RED)
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
            time.sleep(2)
            pygame.quit()
            sys.exit()


    pygame.display.update()
    pygame.time.Clock().tick(FPS)
