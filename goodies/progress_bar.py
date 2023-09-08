
import pygame
from typing import Callable
from goodies.mathy import clamp

class ProgressBar:

    def __init__(self, surface, color, max_val, pos:tuple, callback: Callable) -> None:
        self.surface = surface
        self.color = color
        self.under_color = pygame.Color('gray')
        self.pos = pos
        if callback is not None:
            self.callback = callback
        else:
            self.callback = self.no_callback
        self.max_val = max_val
        self.current_val = max_val
        self.bar_length = 100
        self.bar_ratio = self.max_val / self.bar_length
        self.rect = pygame.Rect(pos[0], pos[1], self.bar_length, 30)
        self.rect_under = pygame.Rect(pos[0], pos[1], self.bar_length, 30)
    
    def update(self, dt):
        
        self.bar_length = clamp((self.bar_length - 20 * dt), 0, self.max_val)
        self.rect.width = self.bar_length
        if self.bar_length == 0:
            pass
            #self.callback()
        # print(int(self.bar_length))
    
    def draw(self):
        pygame.draw.rect(self.surface, self.under_color, self.rect_under)
        pygame.draw.rect(self.surface, self.color, self.rect)

    def reset(self):
        self.bar_length = self.max_val
    
    def no_callback(self):
        print('progress bar is empty')