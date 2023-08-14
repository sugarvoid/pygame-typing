import pygame
from pygame import Rect, font
from pygame.font import SysFont



pygame.init()
def get_font(size):
    _font = SysFont("Arial", size)
    return _font

font_default = get_font(20)


labels = []
class Label:
    
    def __init__(self, screen, text, x, y, size, color="white", group=pygame.sprite.Group):
        
        self.font = get_font(size)
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


def show_labels():
    for _ in labels:
        _.draw()


'''     when you import this module
text1 = Text(win, "Ciao a tutti", 100, 100) # out of loop
text.draw() # into the loop
'''

if __name__ == '__main__':
    # TEXT TO SHOW ON THE SCREEN AT POS 100 100
    win = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()


    Label(win, "Hello World", 100, 100, 36)
    second = Label(win, "GiovanniPython", 0, 0, 32, color="yellow")
    second.change_text('new test')
    # LOOP TO MAKE THINGS ON THE SCRREEN
    loop = 1
    while loop:
        win.fill(0) # CLEAN THE SCREEN EVERY FRAME
        # CODE TO CLOSE THE WINDOW
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = 0
        # CODE TO SHOW TEXT EVERY FRAME
        show_labels()
        second.draw()
        pygame.display.update()
        clock.tick(60)

    pygame.quit()