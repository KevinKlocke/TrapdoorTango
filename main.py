# importing modules and variables
import pygame, sys
from settings import *

# initialize pygame 
pygame.init()

# setup screen and Clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('TrapdoorTango')
clock = pygame.time.Clock()
