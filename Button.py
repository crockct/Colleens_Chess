from pygame import sprite, Rect
import pygame.font
import enum
from enum import Enum



class ButtonType(Enum):
    Quit = 1
    PlayAgain = 2
    Castle = 3

class Button(sprite.Sprite):
    def __init__(self, screen, message, bType, color, textColor, textFont, buttonCount):
        sprite.Sprite.__init__(self)
        if (textFont==None):
            self.font = pygame.font.Font(None, 30)
        else:
            self.font = textFont
        self.text = self.font.render(message, True, textColor, color)
        self.rect = self.text.get_rect()

        #upper right corner
        self.rect.centerx = 950
        self.rect.centery = 20 + 30 * buttonCount #stack buttons under one another

        
        self.color = color
        self.image = self.rect
        #self.image.fill(color)
        self.screen = screen
        self.ButtonType = bType
        screen.blit(self.text, self.rect)


def makeButton(buttons, screen, message, bType, color, textColor, textFont=None):
    buttons.add(Button(screen, message, bType, color, textColor, textFont, len(buttons)))
    return buttons

"""
Returns button (if any), that intersects with the point given by position
ASSUMES BUTTONS DON'T OVERLAP
Returns False if no buttons intersect with given point
"""
def clicked(buttons, position):
    iterator = iter(buttons)
    hasNext = True
    while hasNext:
        try:
            b = iterator.next()
            if (b.rect.collidepoint(position)):
                return b
        except (StopIteration):
            hasNext = False
    return False
        
    
        
    
