# text.py 0.2.0

from os import path
from pygame.font import Font, init
from pygame.sprite import Sprite

init()


class Text(Sprite):
    def __init__(self, font_name, size, text, color, pos=(0, 0)):
        super().__init__()
        _font = Font(f"./asset/font/{font_name}.ttf", size)
        self.text = text
        self.font = _font
        self.color = color
        self.image = self.font.render(self.text, False, self.color).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

    def change_text(self, new_text: str):
        if new_text == self.text:
            return
        self.text = new_text
        self.image = self.font.render(self.text, False, self.color).convert_alpha()
        self.rect = self.image.get_rect()

    def change_location(self, pos: tuple):
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def change_color(self, new_color):
        self.image = self.font.render(self.text, False, new_color).convert_alpha()
        self.rect = self.image.get_rect()


@staticmethod
def get_font_by_name(font_name: str, font_size: int) -> Font:
    match font_name:
        case "thaleah":
            return Font("./font/ThaleahFat.ttf", font_size)
        case "smart_basic":
            return Font("./font/smart_basic_9h.ttf", font_size)
        case "monogram":
            return Font("./font/monogram.ttf", font_size)
        case _:
            raise Exception("Please add a valid font name.")
