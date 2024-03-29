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

def getFont(size):
    return pygame.font.Font('assets/font.ttf', size)

def start_screen():
    while True:
        screen.fill('#0e677d')

        # Getting the Mouse Position in the Title Screen
        menu_mouse_pos = pygame.mouse.get_pos()

        # Setting up the Text for the Title Screen
        menu_text = getFont(80).render('TrapdoorTango', True, '#b68f40')
        menu_rect = menu_text.get_rect(center=(640, 200))

        screen.blit(menu_text, menu_rect)

        # Creating the Button Objects for the Title Screen
        play_button = Button(pos=(640, 400), text_input='PLAY', font=getFont(70), base_color='#b68f40', hovering_color='#e8b754')
        
        quit_button = Button(pos=(640, 700), text_input='QUIT', font=getFont(70), base_color='#b68f40', hovering_color='#e8b754')
        
        fullscreen_button = Button(pos=(640, 550), text_input='FSCREEN', font=getFont(70), base_color='#b68f40', hovering_color='#e8b754')

        
        # draw buttons on screen and change Color on Hover
        for button in [play_button, quit_button, fullscreen_button]:
            button.changeColor(menu_mouse_pos)
            button.draw(screen)
        
        # Game Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                pygame.display.toggle_fullscreen()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForMouseCollision(menu_mouse_pos):
                    play()
                if fullscreen_button.checkForMouseCollision(menu_mouse_pos):
                    pygame.display.toggle_fullscreen()
                if quit_button.checkForMouseCollision(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
     
def play():
    # creating the level object
    level = Level(screen)

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    start_screen()
        
        screen.fill('#d6d0b8')

        clock.tick(60)

        level.run()
        
        if level.checkForGameOver():
            pass

        if level.checkForWin():
            pass
        
        pygame.display.update()   

start_screen()
