# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2017-06-25 00:53:06
# @Last Modified by:   Marte
# @Last Modified time: 2017-06-25 08:50:16

import pygame

if __name__ == '__main__':
    screen = pygame.display.set_mode((480,890),0,32)
    bgImageFile='./feiji/background.png'
    background = pygame.image.load(bgImageFile).convert()
    while True:
        screen.blit(background,(0,0))
        pygame.display.update()