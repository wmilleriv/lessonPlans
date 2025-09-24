import os
import pygame

os.environ['SDL_VIDEO_CENTERED'] = '1'

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


    

        keys=pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player_pos.y-=300*self.dt
        if keys[pygame.K_s]:
            self.player_pos.y+=300*self.dt
        if keys[pygame.K_a]:
            self.player_pos.x-=300*self.dt
        if keys[pygame.K_d]:
            self.player_pos.x+=300*self.dt

        #pygame.display.flip()

        #dt=clock.tick(60)/1000

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

    def draw(self, surface):
        surface.blit(self.image, self.rect)
game=Dodger()
game.run()
pygame.quit()
