import pygame

class Door(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((64, 64))
        self.image.fill('green')
        self.rect = self.image.get_rect(topleft = pos)
    
    