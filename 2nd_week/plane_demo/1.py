# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *  #pygame使用的各种常量
import time

# 创建游戏主页面窗口，并添加滚动背景。

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

        #更新屏幕显示
        pygame.display.update()

        # 定时睡眠（时钟）
        time.sleep(0.04)

# 判断当前是否是主程序，若是就执行主程序。
if __name__ == "__main__":
    main()
