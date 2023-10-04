import pygame
import sys
from level import *
from table import *
from ball import *
from functions import *


pygame.init()
scr_w, scr_h = 600,600
screen = pygame.display.set_mode((scr_w,scr_h))
table = Table()
tables = pygame.sprite.GroupSingle()
tables.add(table)


clock = pygame.time.Clock()

text_font = pygame.font.Font('font/Inconsolata-Medium.ttf', 50)

level = Level(level_date, screen)

ball = Ball()
#ball = pygame.Rect(348,198,5,5)
#x_speed, y_speed = 4, 5

isActive = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and isActive == False:
                isActive = True

    if isActive:
        screen.fill('black')
        tables.draw(screen)
        tables.update()

        pygame.draw.rect(screen, 'white', ball)
        level.update()
        bouncing(ball, scr_w, scr_h, tables, table, level)
    else:
        starting_screen(screen, scr_w, text_font)
          
    pygame.display.update()
    clock.tick(60)