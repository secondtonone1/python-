#name : HACKER EMPIRE CAPTION RAIN
#import modules
try :
    import pygame
    import sys
    from pygame.locals import *
    from random import randint
    import random
except :
    print("Load modules error!!")
    exit()
#define some datas
SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768
LOW_SPEED = 5
HIGH_SPEED = 10
LOW_SIZE = 5
HIGH_SIZE = 30
FONT_SIZE = 25
FONT_NAME = "arial"
FREQUENCE = 50
times = 0
#def random color
def randomcolor() :
    #return (randint(0,255),randint(0,255),randint(0,255))
    return(50, 205, 50)
def randomspeed() :
    return randint(LOW_SPEED,HIGH_SPEED)
def randomposition() :
    return (randint(0,SCREEN_WIDTH),randint(0,SCREEN_HEIGHT))
def randomsize() :
    return randint(LOW_SIZE,HIGH_SIZE)
def randomoname() :
    array=[1,0,2,4]
    return random.choice(array)
def randomvalue() :
    array=[1,0,2,4]
    return random.choice(array)
#class of sprite
class Word(pygame.sprite.Sprite) :
    def __init__(self,bornposition) :
        pygame.sprite.Sprite.__init__(self)
        self.value = randomvalue()
        self.font = pygame.font.SysFont(FONT_NAME,FONT_SIZE)
        self.image = self.font.render(str(self.value),True,randomcolor())
        self.speed = randomspeed()
        self.rect = self.image.get_rect()
        self.rect.topleft = bornposition
    def update(self) :
        self.rect = self.rect.move(0,self.speed)
        if self.rect.top > SCREEN_HEIGHT :
            self.kill()
#init the available modules
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("HACKER EMPIRE CAPTION RAIN")
clock = pygame.time.Clock()
group = pygame.sprite.Group()
group_count = SCREEN_WIDTH // FONT_SIZE
#mainloop
while True :
    time = clock.tick(FREQUENCE)
    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit()
            exit()
    screen.fill((0,0,0))
    for i in range(0,group_count) :
        group.add(Word((i * FONT_SIZE,-FONT_SIZE)))
    group.update()
    group.draw(screen)
    pygame.display.update()


