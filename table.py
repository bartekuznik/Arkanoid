import pygame

class Table(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((80,10))
        self.rect = self.image.get_rect(center = (300,580))
        self.image.fill('red')
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= 7
        if keys[pygame.K_RIGHT] and self.rect.x + 50 < 600:
            self.rect.x += 7
    
    def update(self):
        self.player_input()