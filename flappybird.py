import pygame
import random
pygame.init()
HEIGHT = 900
WIDTH = 864
screen = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("flappy bird")
background = pygame.image.load(r"flappy bird\images\fb_background.png")
fbdown = pygame.image.load(r"flappy bird\images\fb_down.png")
fbup = pygame.image.load(r"flappy bird\images\fb_up.png")
fbmid = pygame.image.load(r"flappy bird\images\fb_mid.png")
floor = pygame.image.load(r"flappy bird\images\fb_floor.png")
pillar = pygame.image.load(r"flappy bird\images\fb_pillar.png")
floorx = 0 
pipe_delay = 1710
last_pipe = pygame.time.get_ticks()-pipe_delay
class Bird(pygame.sprite.Sprite):
    def __init__(self , x , y):
        super().__init__()
        self.images = [fbup , fbmid , fbdown]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
class Pipe(pygame.sprite.Sprite):
    def __init__(self , x , y , pos):
        super().__init__()
        self.image = pillar
        self.rect = self.image.get_rect()
        if pos == 1 :
            self.image = pygame.transform.rotate(self.image,angle= 180)
            self.rect.bottomleft = x , y 
            
        else:
            self.rect.topleft = x, y 
            


    def update(self):
        self.rect.x = self.rect.x - 1
        if self.rect.x < -70:
            self.kill()


pipegroup = pygame.sprite.Group()

bird = Bird(100 , HEIGHT/2)
birdgroup = pygame.sprite.Group()
birdgroup.add(bird)
run = True
while run == True:
    screen.blit(background , (0,0))
  
    floorx=floorx-1
    if floorx < -36:
        floorx = 0

    if pygame.time.get_ticks()-last_pipe > pipe_delay:
        toppipe = Pipe(750 , 760//2-100,1)
        botpipe = Pipe(750 , 760//2 +100, 2  )
        pipegroup.add(toppipe )
        pipegroup.add(botpipe)
        last_pipe = pygame.time.get_ticks()
  

    birdgroup.draw(screen)
    pipegroup.update()
    pipegroup.draw(screen)
    screen.blit(floor , (floorx,760))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
  