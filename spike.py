import pygame

class Spike(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('./assets/spike64.png').convert_alpha()
        self.rect = self.image.get_rect(bottomleft = pos)
        self.rect.height = 32
    