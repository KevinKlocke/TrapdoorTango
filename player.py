import pygame
import time

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('./assets/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        # player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -15

        self.jumping = False


    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT] or keys [pygame.K_a]:
            self.direction.x = -1
        else: 
            self.direction.x = 0

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.jump()
            self.jumping = True
    
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        if not self.jumping:
            self.direction.y = self.jump_speed
    
    def update(self):
        self.get_input()
    