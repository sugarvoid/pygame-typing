import pygame
from csv import reader

from typing import Callable

#font = pygame.font.Font('./font/monogram.ttf', 24)

# TODO: Move to its' own file
def clamp(n, min, max):
    if n < min:
        return min
    elif n > max:
        return max
    else:
        return n

class Text(pygame.sprite.Sprite):
    #TODO: Remove the 4 variable part and replace with rect
    def __init__(self, text:str, color:str, size:int, center_pos=(0,0)):
        super().__init__() 
        self.color = color
        self.text = text
        self.font = pygame.font.Font('./font/monogram.ttf', size)

        
        self.image = self.font.render(self.text, True, self.color).convert_alpha()
        _, _, self.w, self.h = self.image.get_rect()
        self.rect = self.image.get_rect()


        self.rect = self.image.get_rect(topleft = center_pos)

    def change_text(self, new_text):
        if self.text == new_text:
            return
        self.text = new_text
        self.image = self.font.render(self.text, 1, self.color).convert_alpha()
        self.rect = self.image.get_rect()
        _, _, self.w, self.h = self.image.get_rect()
    
    def update_pos(self):
        pass
    
    def update_text(self, new_text):
        self.image = self.font.render(new_text, True, self.color).convert_alpha()
    
    def change_location(self, pos:tuple):
        _, _, w, h = self.image.get_rect()
        self.rect = pygame.Rect(pos[0],pos[1], self.w, self.h)
    



        


