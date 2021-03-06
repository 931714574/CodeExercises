#!/usr/bin/env python3
# 绘制世界
# 添加玩家和玩家控制
# 添加玩家移动控制

# GNU All-PermissiveLicense
# Copyingand distribution of thisfile,withor without modification,
# are permitted in any medium without royalty provided the copyright
# notice andthis notice are preserved.Thisfileis offered as-is,
# without any warranty.

import pygame
import sys
import os



class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        for i in range(1, 5):
            img = pygame.image.load(os.path.join('images', 'hero' + str(i) + '.png')).convert()
        img.convert_alpha()
        img.set_colorkey(ALPHA)
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()


        def control(self, x, y):
            '''
            控制玩家移动
            '''


            self.movex += x
            self.movey += y


        def update(self):
            '''
            更新妖精位置
            '''


        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

        # 向左移动
        if self.movex < 0:
            self.frame += 1
        if self.frame > 3 * ani:
            self.frame = 0
            self.image = self.images[self.frame // ani]

        # 向右移动
        if self.movex > 0:
            self.frame += 1
        if self.frame > 3 * ani:
            self.frame = 0
            self.image = self.images[(self.frame // ani) + 4]

'''
设置
'''
worldx = 960
worldy = 720

fps = 40  # 帧刷新率
ani = 4  # 动画循环
clock = pygame.time.Clock()
pygame.init()
main = True

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)

world = pygame.display.set_mode([worldx, worldy])
backdrop = pygame.draw.circle(world, (0, 0, 0), [worldx, worldy], 5, 0)
backdropbox = world.get_rect()
player = Player()  # 生成玩家
player.rect.x = 0
player.rect.y = 0
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10  # 移动速度

'''
主循环
'''
while main == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit()
            main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps, 0)
        if event.key == pygame.K_RIGHT or event.key == ord('d'):
            player.control(steps, 0)
        if event.key == pygame.K_UP or event.key == ord('w'):
            print('jump')

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps, 0)
        if event.key == pygame.K_RIGHT or event.key == ord('d'):
            player.control(-steps, 0)
        if event.key == ord('q'):
            pygame.quit()
            sys.exit()
            main = False

# world.fill(BLACK)
world.blit(backdrop, backdropbox)
player.update()
player_list.draw(world)  # 更新玩家位置
pygame.display.flip()
clock.tick(fps)
