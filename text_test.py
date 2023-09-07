import random

import pygame


WIDTH, HEIGHT = 640, 360
FPS = 60


class Text:
    font_families: dict[str, pygame.Font] = {}

    def __init__(self,
		screen: pygame.Surface,
        text: str,
        pos: tuple[int, int],
        font_path: str | None = None,
        size: int = 32,
        color: str | tuple[int, int, int] = "white",
    ) -> None:
        self.screen = screen
        self.pos = pos
        self.color = color

        font = type(self).font_families.get(font_path)
        if font is None:
            self.font = pygame.Font(font_path, size)
            type(self).font_families[font_path] = font
        else:
            self.font.point_size = size
        self.text = None  # force first image creation
        self.update_text(text)  # force first image creation

    # Method to allow changing the text in the field
    def update_text(self, new_text) -> None:
        if new_text == self.text:
            return  # Optimization - no need to create a new image

        self.text = new_text
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect(center=self.pos)

    def render(self) -> None:
        self.screen.blit(self.image, self.rect)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.Clock()

# Create one text object to show count of created text fields
counter_text = Text(screen, "Counter: 0", (70, 20), color='green')
n_text_fields = 0
texts = []

running = True
while running:
    dt = clock.tick(FPS) / 1000
    screen.fill("black")

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:  # who uses this constant, lol
                new_text = Text(
					screen,
                    random.choice(["Hello, World!", "Cats!!!!", "42", "Yum!"]),
                    event.pos,
                )
                texts.append(new_text)
                n_text_fields = n_text_fields + 1
                counter_text.update_text(f'Counter: {n_text_fields}')

    counter_text.render()
    for text_obj in texts:
        text_obj.render()  # removed screen argument

    pygame.display.flip()
pygame.quit()