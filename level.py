import pygame
from block import *

level_date = [["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
         ["w", "w", "w", "p", "p", "w", "w", "w", "w", "w", "w", "w", "p", "w", "w", "w", "w", "w", "w", "w"],
         ["w", "w", "w", "p", "w", "w", "w", "w", "p", "w", "w", "w", "w", "p", "w", "w", "w", "w", "w", "w"],
         ["w", "w", "w", "w", "w", "w", "w", "p", "w", "w", "p", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
         ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
         ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
         ["w", "w", "w", "w", "w", "p", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
         ["w", "w", "w", "w", "w", "w", "w", "w", "w", "p", "w", "w", "w", "p", "w", "w", "w", "w", "w", "w"],
         ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
         ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
         ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
         ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
         ]

t_size = 20

class Level:
    def __init__(self, level_date, screen):
        self.level_date = level_date
        self.screen = screen
        self.init_surface(self.level_date)

    def init_surface(self, level_date):
        self.blocks = pygame.sprite.Group()
        for row_index, row in enumerate(level_date):
            for col_index, cell in enumerate(row):
                if cell == "w":
                    pass
                if cell == "p":
                    x = col_index*t_size
                    y = row_index*t_size

                    block = Block((x,y), t_size)
                    self.blocks.add(block)
                    
    def update(self):
        self.blocks.draw(self.screen)
