# importing modules and variables
import pygame, sys
from settings import *
from level import Level
from button import Button

# initialize pygame 
pygame.init()

# setup screen and Clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('TrapdoorTango')
clock = pygame.time.Clock()

font = pygame.font.Font(size=24)

def start_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.exit()
                sys.exit()
    
    button = Button((640,200), 'Start Game', font, 'red', 'blue')
    button.draw(screen)
        

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    Level(screen).run()
    # button = Button((640,200), 'Start Game', font, 'red', 'blue')
    # button.draw(screen)
    
    pygame.display.update()
