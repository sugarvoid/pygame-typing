import pygame
from csv import reader

#font = pygame.font.Font('./font/monogram.ttf', 24)

class Text(pygame.sprite.Sprite):
    def __init__(self, text, color, center_pos=(0,0)):
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



