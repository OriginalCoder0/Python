# -*- coding:utf-8 -*-

import pygame
from pygame.locals import *  #pygame使用的各种常量
import time

# 放置玩家英雄飞机，并绑定键盘事件，实现飞机移动

class HeroPlane:
    ''' 玩家飞机类（英雄） '''
    def __init__(self, screen_temp):
        self.x = 200
        self.y = 400
        self.screen = screen_temp
        self.image = pygame.image.load("./images/me.png")

    def display(self):
        ''' 绘制玩家到窗口中 '''
        self.screen.blit(self.image, (self.x, self.y))

    def move_left(self):
        ''' 左移动,并判断防止越界 '''
        self.x -= 5
        if self.x<0:
            self.x=0

    def move_right(self):
        ''' 右移动,并判断防止越界 '''
        self.x += 5
        if self.x > 406:
            self.x = 406

def key_control(hero_temp):
    ''' 键盘控制函数 '''

    #获取事件，比如按键等
    for event in pygame.event.get():
        #判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()

    #获取按下的键(返回的是元组值)
    pressed_keys = pygame.key.get_pressed()
    #检测是否按下a或者left键
    if pressed_keys[K_LEFT] or pressed_keys[K_a]:
        print('left')
        hero_temp.move_left()
    
    #检测是否按下d或者right键
    elif pressed_keys[K_RIGHT] or pressed_keys[K_d]:
        print('right')
        hero_temp.move_right()
    
    #检查是否是空格键
    if pressed_keys[K_SPACE]:
        print('space')

def main():
    '''游戏的主程序执行函数'''

    #1. 创建窗口:set_mode(分辨率=(0,0),标志=0,深度=0)
    screen = pygame.display.set_mode((512,568),0,0)

    #2. 创建一个游戏背景图片(512*1536)
    background = pygame.image.load("./images/bg2.jpg")
    m=-968 #初始化游戏背景图片标轴y的值

    #3. 创建一个玩家飞机对象
    hero = HeroPlane(screen)

    while True:
        #绘制位图
        screen.blit(background,(0,m))
        m+=2
        if m>=-200:
            m = -968

         #显示英雄玩家
        hero.display()
        # 键盘控制（负责移动玩家）
        key_control(hero)

        #更新屏幕显示
        pygame.display.update()

        # 定时睡眠（时钟）
        time.sleep(0.04)

# 判断当前是否是主程序，若是就执行主程序。
if __name__ == "__main__":
    main()
