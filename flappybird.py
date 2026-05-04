import pygame
import random
pygame.init()
HEIGHT = 900
WIDTH = 864

screen = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("flappy bird")
background = pygame.image.load(r"images\fb_background.png")
fbdown = pygame.image.load(r"images\fb_down.png")
fbup = pygame.image.load(r"images\fb_up.png")
fbmid = pygame.image.load(r"images\fb_mid.png")
floor = pygame.image.load(r"images\fb_floor.png")
pillar = pygame.image.load(r"images\fb_pillar.png")
floorx = 0 
pipe_delay = 1710
score = 0
game_over = False
font = pygame.font.SysFont("jokerman", 25 )
passedpipe = False
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
        self.vy = 0
    def update(self):
        key_press = pygame.key.get_pressed()
        if key_press[pygame.K_SPACE] and game_over == False:
            self.vy = -1
        if self.vy < 5:
            self.vy = self.vy + 0.005
        self.rect.y = self.rect.y + self.vy
        self.index= (self.index+1)%3
        self.image = self.images[self.index]
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
        global passedpipe
        if game_over == False:
            self.rect.x = self.rect.x  - 1                
            if self.rect.x < -70 :
                self.kill()
                passedpipe = False


pipegroup = pygame.sprite.Group()

bird = Bird(100 , HEIGHT/2)
birdgroup = pygame.sprite.Group()
birdgroup.add(bird)
run = True
while run == True:
    screen.blit(background , (0,0))
    if bird.rect.bottom >  760:
        game_over=True
        bird.rect.bottom = 760
    if len(pipegroup)>0:
        if bird.rect.x > pipegroup.sprites()[0].rect.right and passedpipe==False:
            score = score+1
            passedpipe = True
        if pygame.sprite.groupcollide(birdgroup,pipegroup,False , False):
            game_over=True   
   
    
    birdgroup.update()
    if game_over==False:
        floorx=floorx-1
    if floorx < -36:
        floorx = 0
    if game_over == True:
        text = font.render("GAME OVER " , True , "black")
        screen.blit(text , (WIDTH/2-50,HEIGHT/2-100))
    
    if pygame.time.get_ticks()-last_pipe > pipe_delay and game_over==False:
        pipey = random.randint(-150,150)
        toppipe = Pipe(750 , 760//2-100+pipey,1)
        botpipe = Pipe(750 , 760//2 +100+pipey, 2  )
        pipegroup.add(toppipe )
        pipegroup.add(botpipe)
        last_pipe = pygame.time.get_ticks()
    

    birdgroup.draw(screen)
    pipegroup.update()
    pipegroup.draw(screen)
    text = font.render(f"score:{score}" , True , "black")
    screen.blit(text , (100,100)) 
    screen.blit(floor , (floorx,760))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    