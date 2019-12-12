# -*- coding:utf-8 -*-

import pygame
from pygame.locals import *  #pygame使用的各种常量
import time,random

# 显示敌机。

class HeroPlane:
    ''' 玩家飞机类（英雄） '''
    def __init__(self, screen_temp):
        self.x = 200
        self.y = 400
        self.screen = screen_temp
        self.image = pygame.image.load("./images/me.png")
        self.bullet_list = [] #存储发射出去的子弹对象引用

    def display(self):
        ''' 绘制玩家到窗口中 '''
        
        #遍历移动子弹
        for bullet in self.bullet_list:
            bullet.display()
            #移动子弹，并判断是否越界。
            if bullet.move():
                self.bullet_list.remove(bullet)

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
    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))
        print(len(self.bullet_list))

class Bullet:
    ''' 玩家子弹类 '''
    def __init__(self, screen_temp, x, y):
        self.x = x+51
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load("./images/pd.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y-=10
        if self.y<-20:
            return True

class EnemyPlane:
    """敌机的类"""
    def __init__(self, screen_temp):
        self.x = random.choice(range(408))
        self.y = -75
        self.screen = screen_temp
        self.image = pygame.image.load("./images/e"+str(random.choice(range(3)))+".png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self,hero):
        self.y += 4
        #遍历玩家的子弹，并做碰撞检测
        for bo in hero.bullet_list:
            if bo.x>self.x+12 and bo.x<self.x+92 and bo.y>self.y+20 and bo.y<self.y+60:
                hero.bullet_list.remove(bo)
                return True
        #判断敌机是否越界
        if self.y>512:
            return True;

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
        hero_temp.fire()

def main():
    '''游戏的主程序执行函数'''

    #1. 创建窗口:set_mode(分辨率=(0,0),标志=0,深度=0)
    screen = pygame.display.set_mode((512,568),0,0)

    #2. 创建一个游戏背景图片(512*1536)
    background = pygame.image.load("./images/bg2.jpg")
    m=-968 #初始化游戏背景图片标轴y的值

    #3. 创建一个玩家飞机对象
    hero = HeroPlane(screen)

    #4.定义用于存放敌机列表
    enemylist = []

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

        #随机输出敌机
        if random.choice(range(50))==10:
            enemylist.append(EnemyPlane(screen))
        
        #遍历所有敌机，显示敌机，移动敌机，并与玩家子弹碰撞检测
        for em in enemylist:
            em.display()
            if em.move(hero):
                enemylist.remove(em)

        #更新屏幕显示
        pygame.display.update()

        # 定时睡眠（时钟）
        time.sleep(0.04)

# 判断当前是否是主程序，若是就执行主程序。
if __name__ == "__main__":
    main()
