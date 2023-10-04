import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size-1, size/2))
        self.rect = self.image.get_rect(topleft = pos)
        self.image.fill('green')
