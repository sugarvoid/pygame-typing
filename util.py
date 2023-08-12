import pygame
from csv import reader

#font = pygame.font.Font('./font/monogram.ttf', 24)

class Text(pygame.sprite.Sprite):
    def __init__(self, text:str, color:str, center_pos=(0,0)):
        super().__init__() 
        self.font = pygame.font.Font('./font/monogram.ttf', 16)
        self.image = self.font.render(text, False, color)
        self.rect = self.image.get_rect(topleft = center_pos)
    


def import_cvs_layout(cvs_path:str) -> list:
    layer_data: list = []
    with open(cvs_path) as map:
        level = reader(map,delimiter=',')
        for row in level:
            layer_data.append(list(row))
        return layer_data

class ProgressBar():

    def __init__(self, surface, color, max_val, pos:tuple) -> None:
        self.surface = surface
        self.color = color
        self.under_color = pygame.Color('gray')
        self.pos = pos
        
        self.max_val = max_val
        self.current_val = max_val
        self.bar_length = 50
        self.bar_ratio = self.max_val / self.bar_length
        self.rect = pygame.Rect(pos[0], pos[1], self.bar_length, 4)
        self.rect_under = pygame.Rect(pos[0], pos[1], self.bar_length, 4)
    
    def update(self, dt):
        self.bar_length -= 1 * dt
        self.rect.width = self.bar_length
        # print(int(self.bar_length))
    
    def draw(self):
        pygame.draw.rect(self.surface, self.under_color, self.rect_under)
        pygame.draw.rect(self.surface, self.color, self.rect)
        
class Button():
    pass