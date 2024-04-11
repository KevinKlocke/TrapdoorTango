import pygame

class Button():
    def __init__(self, pos, text_input, font, base_color, hovering_color):
        pygame.init()
        # creating the Button Surface
        self.image = pygame.Surface((530, 100))
        self.image.fill('#735a28')
        
        # getting the position x,y of the button
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        
        # setting the font for the Text, colors and the display text
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center = (self.x_pos, self.y_pos))
    
    # function for drawing the button on screen
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)
    
    def getMousePos(self, position):
        return position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom)
    
    # check if the mouse is colliding with the Button
    def checkForMouseCollision(self, position):
        if self.getMousePos(position):
            return True
        return False
    
    # Updating font color when colliding
    def changeColor(self, position):
        if self.getMousePos(position):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)