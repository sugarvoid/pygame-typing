
import pygame
from os import path
from pygame.font import Font

pygame.font.init()


_font = pygame.font.Font('./font/monogram.ttf', 16)

class Text(pygame.sprite.Sprite):
    def __init__(self, font_name, size, text, color, pos=(0,0)):
        super().__init__() 
        _font = pygame.font.Font(f'./font/{font_name}.ttf', size)
        self.text = text
        self.font = _font
        self.color = color
        self.image = self.font.render(self.text, False, self.color).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
    
    def change_text(self, new_text: str):
        if new_text == self.text:
            return
        self.text = new_text
        self.image = self.font.render(self.text, False, self.color).convert_alpha()
        self.rect = self.image.get_rect()
    
    def change_location(self, pos:tuple):
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    


@staticmethod
def draw_text(surface:pygame.Surface, text:str, size:int, font_file:str, color, x:int, y:int):
    #text_font = font.Font(font_file, size)

    img = _font.render(text, False, color)
    surface.blit(img, (x,y))



@staticmethod
def get_font_by_name(font_name: str, font_size: int) -> Font:
    match font_name:
        case 'thaleah':
            return Font('./font/ThaleahFat.ttf', font_size)
        case 'smart_basic':
            return Font('./font/smart_basic_9h.ttf', font_size)
        case 'monogram':
            return Font('./font/monogram.ttf', font_size)
        case _:
            raise Exception('Please add a valid font name.') 