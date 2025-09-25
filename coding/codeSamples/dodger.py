import sys
import pygame
from pygame.locals import *
import random


FPS=60

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

PURPLE=(200,0,255)
RED=(255,0,0)

DISPLAY_SURFACE = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAY_SURFACE.fill(PURPLE)
pygame.display.set.caption("Dodger")

class Player(ipygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((80,80))
        self.pos=pygame.Vector2(self.window.get_width()/2, self.window.get_height()/2)
        pygame.draw.circle(self.image,PURPLE,self.pos, 40)

    def update(self):

        keys=pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.pos.y-=5
        if keys[pygame.K_s]:
            self.pos.y+=5
        if keys[pygame.K_a]:
            self.pos.x-=5
        if keys[pygame.K_d]:
            self.pos.x+=5



class Dodger():

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1280,720))
        self.clock=pygame.time.Clock()
        self.running=True
        self.dt=0
        self.player_pos=pygame.Vector2(self.window.get_width()/2, self.window.get_height()/2)

    def processInput(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running=False




    def update(Self):
        pass

    def render(self):
        self.window.fill("purple")
        pygame.draw.circle(self.window, "red", self.player_pos, 40)
        pygame.display.update()

    def run(self):
        while self.running:
            self.processInput()
            self.update()
            self.render()
            self.dt=self.clock.tick(60)/1000

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.draw.rect(surface, "green", pygame.Rect(0,0,5,10))

    def move(self):
        self.rect.move_ip(0,10)
        if self.rect.bottom > 600):
            self.rect

    def draw(self, surface):
        surface.blit(self.image, self.rect)
game=Dodger()
game.run()
pygame.quit()
