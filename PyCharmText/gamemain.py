# -*- coding: utf-8 -*-
import time

import pygame as pg
import sys
import os
import random
from pygame.locals import *


def main():
    # 初始化pygame模块
    pg.init()
    # 创建窗口并设置窗口大小、标题、背景颜色
    window = pg.display.set_mode((1200, 450), RESIZABLE)
    pg.display.set_caption("勇士的信仰")
    window.fill((250, 250, 250))
    # 小球生成
    for i in range(1, 500):
        ball(window, 2)
    # 大球生成
    rollballX = 600
    rollballY = 250
    pg.draw.circle(window, (0, 0, 0), [rollballX, rollballY], 5, 0)
    pg.display.update()

    # 创建一个变量储存改动值
    move_x = 0
    move_y = 0

    # 设置循环让窗口可以一直显示
    while True:
        for event in pg.event.get():
            # print(event)
            if event.type == pg.QUIT:
                exit()
            # 控制按键按下
            if event.type == pg.KEYDOWN:
                if event.key == K_w:
                    move_y = -1
                elif event.key == K_a:
                    move_x = -1
                elif event.key == K_s:
                    move_y = 1
                elif event.key == K_d:
                    move_x = 1
                elif event.key == K_ESCAPE:
                    exit()
            # 控制按键松开
            if event.type == pg.KEYUP:
                if event.key == K_w:
                    move_y = 0
                elif event.key == K_a:
                    move_x = 0
                elif event.key == K_s:
                    move_y = 0
                elif event.key == K_d:
                    move_x = 0
        rollballX += move_x
        rollballY += move_y
        pg.draw.circle(window, (0, 0, 0), [rollballX, rollballY], 5, 0)
        pg.display.update()
        time.sleep(0.01)

# 生成随机球
def ball(window,size):
    # 画一个圆形
    colour = random.randint(0, 255)
    colour2 = random.randint(0, 255)
    colour3 = random.randint(0, 255)
    coordinateX = random.randint(0, 1200)
    coordinateY = random.randint(0, 450)
    pg.draw.circle(window, (colour, colour2, colour3), [coordinateX, coordinateY], size, 0)

# 控制球的移动事件
def rollball():
    print()









if __name__ == '__main__':
    main()
