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
    def __init__(self):
        super.__init_()
        self.image = pygame.draw.rect(DISPLAY_SURFACE, GREEN, (50,50,100,75))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((80,80))
        self.rect = self.image.get_rect()
        self.pos=pygame.Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        pygame.draw.circle(self.image,PURPLE,self.pos, 40)
        self.dt=0

    def update(self):

        keys=pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.pos.y-=300*self.dt
        if keys[pygame.K_s]:
            self.pos.y+=300*self.dt
        if keys[pygame.K_a]:
            self.pos.x-=300*self.dt
        if keys[pygame.K_d]:
            self.pos.x+=300*self.dt
    
    def draw(self, surface):
        surface.blit(self.image,self.rect)


#class Dodger():

#    def __init__(self):
#        pygame.init()
#        self.window = pygame.display.set_mode((1280,720))
#        self.clock=pygame.time.Clock()
#        self.running=True
#        self.dt=0
#        self.player_pos=pygame.Vector2(self.window.get_width()/2, self.window.get_height()/2)

#    def processInput(self):

#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                self.running=False




#    def update(Self):
#        pass

#    def render(self):
#        self.window.fill("purple")
#        pygame.draw.circle(self.window, "red", self.player_pos, 40)
#       pygame.display.update()

#    def run(self):
#        while self.running:
#           self.processInput()
#            self.update()
#            self.render()
#            self.dt=self.clock.tick(60)/1000

p1=Player()

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    p1.update()

    DISPLAY_SURFACE.fill(PURPLE)
    p1.draw(DISPLAY_SURFACE)

    pygame.display.update()
    pygame.time.Clock().tick(FPS)
