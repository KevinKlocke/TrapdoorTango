import pygame
from tiles import Tile
from settings import TIlE_SIZE, LEVEL_MAP1

class Level():
    def __init__(self, surface):
        self.display_surface = surface
        self.isGameOver = False
        self.level_data = LEVEL_MAP1
        self.setup_level(self.level_data)
        
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * TIlE_SIZE
                y = row_index * TIlE_SIZE
                
                if cell == 'X':
                    tile = Tile((x, y), TIlE_SIZE)
                    self.tiles.add(tile)
    
    
    def run(self):
        self.tiles.draw(self.display_surface)
        