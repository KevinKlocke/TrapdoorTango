import pygame


class Trap(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('#0e677d')
        self.rect = self.image.get_rect(topleft = pos)