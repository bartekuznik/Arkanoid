import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((5,5))
        self.rect = self.image.get_rect(center = (348,198))
        self.x_speed = 4
        self.y_speed = 5

    def movement(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

    def update(self):
        self.movement()