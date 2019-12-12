# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *  #pygame使用的各种常量
import time

# 添加键盘事件处理函数。

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
    
    #检测是否按下d或者right键
    elif pressed_keys[K_RIGHT] or pressed_keys[K_d]:
        print('right')
    
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

    while True:
        #绘制位图
        screen.blit(background,(0,m))
        m+=2
        if m>=-200:
            m = -968

        # 调用键盘控制函数
        key_control(None)

        #更新屏幕显示
        pygame.display.update()

        # 定时睡眠（时钟）
        time.sleep(0.04)

# 判断当前是否是主程序，若是就执行主程序。
if __name__ == "__main__":
    main()


