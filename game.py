# noinspection PyInterpreter
import pygame
from pygame.locals import *
from sys import exit


SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640

#计数ticks
ticks = 0


#初始化游戏mysql-connector
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
pygame.display.set_caption('This is my first pygame-project')

#载入背景图片
background = pygame.image.load('resources/image/hua.jpg')

#载入飞机
shoot_img = pygame.image.load('resources/image/fly.png')
#用subsurface剪切读入的图片
hero1_rect = pygame.Rect(0,99,102,126)
hero2_rect = pygame.Rect(165,360,102,126)
hero1 = shoot_img.subsurface(hero1_rect)
hero2 = shoot_img.subsurface(hero2_rect)
hero_pos = [200,500]



while True:

    #绘制背景
    screen.blit(background,(0,0))

    #绘制飞机
    if ticks % 50 < 25:
        screen.blit(hero1,hero_pos)
    else:
        screen.blit(hero2,hero_pos)
    ticks+=1

    #更新屏幕
    pygame.display.update()

    #处理游戏退出
    #从消息队列中循环取
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
