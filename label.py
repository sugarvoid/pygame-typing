#import pygame
from pygame import Rect
from pygame.font import SysFont
from pygame.sprite import Group



class Label:
    
    def __init__(self, screen, text, x, y, size, color="white", group=Group):
        
        self.font = SysFont("Arial", size)
        self.color = color
        self.image = self.font.render(text, 1, self.color).convert_alpha()
        _, _, w, h = self.image.get_rect()
        self.rect = Rect(x, y, w, h)
        self.screen = screen
        self.text = text
        #group.append(self)

    def change_text(self, new_text):
        self.image = self.font.render(new_text, 1, self.color).convert_alpha()

    def change_font(self, font, size):
        self.font = SysFont(font, size)
        self.change_text(self.text)

    def draw(self):
        self.screen.blit(self.image, (self.rect))


'''     when you import this module
text1 = Text(win, "Ciao a tutti", 100, 100) # out of loop
text.draw() # into the loop
'''

