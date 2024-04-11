import pygame
from tiles import Tile
from door import Door
from settings import *
from player import Player

class Level():
    def __init__(self, surface, level_data):
        self.display_surface = surface
        self.isGameOver = False
        self.level_data = level_data
        self.setup_level(self.level_data)

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.door = pygame.sprite.GroupSingle()

        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                x = col_index * TIlE_SIZE
                y = row_index * TIlE_SIZE
                
                if cell == 'X':
                    tile = Tile((x, y), TIlE_SIZE)
                    self.tiles.add(tile)
                if cell == 'P':
                    player = Player((x,y))
                    self.player.add(player)
                if cell == 'D':
                    door = Door((x ,y))
                    self.door.add(door)


    def horizontal_movement_collision(self):
        player = self.player.sprite

        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.jumping = False
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
    
    def checkForWin(self):
        player = self.player.sprite
        door = self.door.sprite
        if player.rect.colliderect(door.rect):
            self.isGameOver = True
            return self.isGameOver

    def checkForGameOver(self):
        player = self.player.sprite
        if player.rect.bottom > 768:
            self.isGameOver = True
            return self.isGameOver

    def run(self):
        # level tiles
        self.tiles.draw(self.display_surface)
        self.door.draw(self.display_surface)

        # player
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.checkForWin()
        self.player.draw(self.display_surface)
        self.checkForGameOver()
    
        