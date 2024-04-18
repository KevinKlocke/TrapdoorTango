# importing modules and variables
import pygame, sys
from settings import *
from level import Level
from button import Button
from tutorial import Tutorial
from font import getFont

# initialize pygame 
pygame.init()

level_won = []

# setup screen and Clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('TrapdoorTango')
clock = pygame.time.Clock()



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
        play_button = Button(pos=(640, 370), text_input='PLAY', font=getFont(40), base_color='#b68f40', hovering_color='#e8b754')
        
        quit_button = Button(pos=(640, 630), text_input='QUIT', font=getFont(40), base_color='#b68f40', hovering_color='#e8b754')
        
        fullscreen_button = Button(pos=(640, 500), text_input='FULLSCREEN', font=getFont(40), base_color='#b68f40', hovering_color='#e8b754')

        
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
    level_maps = [LEVEL_MAP0, LEVEL_MAP1, LEVEL_MAP2, LEVEL_MAP3, LEVEL_MAP4]
    if len(level_won) < len(level_maps):
        if len(level_won) == 0:
            level = Tutorial(screen, level_maps[len(level_won)])
        else:
            level = Level(screen, level_maps[len(level_won)])
    else:
        start_screen()

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
        
        if len(level_won) == 0:
            level_text = getFont(40).render('Tutorial', True, '#b68f40')
        else:
            level_text = getFont(40).render(f'Level {len(level_won)}', True, '#b68f40')
        level_rect = level_text.get_rect(center=(640, 30))

    
        clock.tick(60)

        level.run()
        
        screen.blit(level_text, level_rect)
        
        if level.checkForGameOver():
            game_over()

        if level.checkForWin():
            level_ending()
        
        pygame.display.update()   

def game_over():
    while True:
        screen.fill('black')

        gameover_text = getFont(80).render('Game Over', True, 'White')
        gameover_rect = gameover_text.get_rect(center=(640, 250))

        continue_text = getFont(30).render('Press Enter To Try Again!', True, 'White')
        continue_rect = continue_text.get_rect(center=(640, 380))

        cancel_text = getFont(30).render('Press ESC To Get To The Title Screen', True, 'White')
        cancel_rect = cancel_text.get_rect(center=(640, 450))

        screen.blit(gameover_text, gameover_rect)
        screen.blit(continue_text, continue_rect)
        screen.blit(cancel_text, cancel_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    play()
                if event.key == pygame.K_ESCAPE:
                    start_screen()

        pygame.display.update()

def level_ending():
    while True:
        screen.fill('#0e677d')

        if len(level_won) == 0:
            success_text = getFont(50).render('Tutorial Completed', True, 'Green')
        else:
            success_text = getFont(50).render(f'Level {len(level_won)} Completed', True, 'Green')
        success_rect = success_text.get_rect(center=(640, 250))

        continue_text = getFont(30).render('Press ENTER For The Next Level!', True, 'White')
        continue_rect = continue_text.get_rect(center=(640, 380))

        cancel_text = getFont(30).render('Press ESC To Get To The Title Screen', True, 'White')
        cancel_rect = cancel_text.get_rect(center=(640, 450))

        screen.blit(success_text, success_rect)
        screen.blit(continue_text, continue_rect)
        screen.blit(cancel_text, cancel_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    level_won.append('1')
                    play()
                if event.key == pygame.K_ESCAPE:
                    start_screen()
        

        pygame.display.update()

start_screen()
