import pygame
import sys

# Initialize Pygame
pygame.init()

# Define constants for the window dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Define colors
DEFAULT_COLOR = (0, 0, 255)  # Blue
HOVER_COLOR = (255, 0, 0)  # Red

# define the RGB value for white,
#  green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)


class Square:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.letter: str = "A"
        self.size = size
        self.is_hovering = False
        self.font = pygame.font.Font("NicoBold.ttf", 32)
        self.text = self.font.render(self.letter, True, white)
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.x + 28, self.y + 30)

    def check_mouse_hover(self, x, y):
        if self.x < x < self.x + self.size and self.y < y < self.y + self.size:
            self.is_hovering = True
        else:
            self.is_hovering = False

    def draw(self, screen):
        if self.is_hovering:
            pygame.draw.rect(
                screen,
                pygame.Color(2, 12, 30),
                (self.x - 3, self.y - 3, self.size + 6, self.size + 6),
            )
            pygame.draw.rect(
                screen, HOVER_COLOR, (self.x, self.y, self.size, self.size)
            )
        else:
            pygame.draw.rect(
                screen, DEFAULT_COLOR, (self.x, self.y, self.size, self.size)
            )
        screen.blit(self.text, self.textRect)


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Mouse Hover Example")
        self.clock = pygame.time.Clock()

        self.grid_squares: pygame.sprite.Group = pygame.sprite.Group()

        self.square1 = Square(400, 300, 50)
        self.square2 = Square(200, 300, 50)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    x, y = event.pos
                    self.square1.check_mouse_hover(x, y)
                    self.square2.check_mouse_hover(x, y)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print(f"left click on {event.pos}")

            # Clear the screen
            self.screen.fill((255, 255, 255))  # Fill with white background

            # Draw the square
            self.grid_squares.draw(self.screen)
            self.square1.draw(self.screen)
            self.square2.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Game()
    game.run()
