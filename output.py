#-*-coding:utf-8-*-
import pygame
from sys import exit
from pygame.locals import *
import random
import time

class LabelSprite(pygame.sprite.Sprite):
    
    def __init__(self, label, topleft,n):
        pygame.sprite.Sprite.__init__(self)
        self.label = label
        self.rect = label.get_rect()
        self.rect.topleft = topleft
        self.listsize = n
        
    


    def UpRun(self,screen):
        self.rect.top -= 36
        if(self.rect.top < SCREEN_HEIGHT//2):
            self.rect.top = SCREEN_HEIGHT//2 + 36*(self.listsize-1)
      

# 设置游戏屏幕大小
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800


# 初始化 pygame
pygame.init()

# 设置游戏界面大小、背景图片及标题
# 游戏界面像素大小
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load('resources/image/background.png').convert()

foods =[u'最得意',u'二细牛肉面',u'早晚见面粥',u'兴隆街选一家',u'他伟哥决定',u'听粗鲁哥建议',u'庆丰包子',u'德克士',u'晋味面馆特别甜',u'建议不吃',u'再来一次']

animals = []
ask = pygame.image.load('resources/image/ask.png').convert_alpha()
animals.append(ask)
answer = pygame.image.load('resources/image/answer.png').convert_alpha()
animals.append(answer)
answer2 = pygame.image.load('resources/image/answer2.png').convert_alpha()
animals.append(answer2)
answer3 = pygame.image.load('resources/image/answer3.png').convert_alpha()
animals.append(answer3)

happy = pygame.image.load('resources/image/happy.png').convert_alpha()

answer_rect = answer.get_rect()
answer_rect.topleft = [SCREEN_WIDTH- answer_rect.width, 0]

tips = []
m = 0
for i in foods:
    score_font = pygame.font.SysFont('stsong', 36)
    score_text = score_font.render(i, True, (0, 0, 0))
    text_rect = score_text.get_rect()
    text_rect.topleft = [100, SCREEN_HEIGHT//2 + 36 *m]
    m = m+1
    labelSprite = LabelSprite(score_text,text_rect.topleft, len(foods) )
    
    #screen.blit(score_text, text_rect)
    tips.append(labelSprite)



# 游戏界面标题
pygame.display.set_caption('中午吃什么')
clock = pygame.time.Clock()

running = True

animalfrequence = 0
animalindex = 0



def run():
    
    def result():
        global running
        tipstr = u'午饭： '
        index = random.randint(0,len(foods)-1 )
        score_font = pygame.font.SysFont('stsong', 36)
        score_text = score_font.render(tipstr + foods[index], True, (128, 128, 128))
        text_rect = score_text.get_rect()
        text_rect.topleft = [100, SCREEN_HEIGHT//2 ]
        screen.fill((0,0,0))
        screen.blit(background, (0,0))
        screen.blit(score_text, text_rect.topleft)
        screen.blit(happy, (100,0))
        pygame.display.update() 
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        running = True
                        run()
                        
    while running:
        global running
        global animalfrequence
        global animalindex
        clock.tick(60);
        time.sleep(0.05)
        animalfrequence+=1
        if animalfrequence >15:
            animalfrequence = 0
        if animalfrequence  == 0:
            animalindex+=1
        if animalindex > 3:
            animalindex = 0
        #print("animalfrequence is  %d" %(animalfrequence))
        #print("animalindex is  %d" %(animalindex))
        screen.fill((0,0,0))
        screen.blit(background, (0,0))
        screen.blit(animals[animalindex],(150,180))
    
        for i in tips:
            i.UpRun(screen)
            screen.blit(i.label, i.rect)
       
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    result()
                    running = False
                
                    
     

run()




while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        

    



