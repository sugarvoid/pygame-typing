import pygame
import sys

from copy import deepcopy

class Tween:
    def __init__(self, start_values, final_values, duration, finished_callback=None):
        self.start_values = start_values
        self.final_values = final_values
        self.duration = duration
        self.finished = False
        self.frame_count = int(FPS * duration)
        self.current_frame = 0
        self.current_values = deepcopy(start_values)  # Initialize current values
        self.finished_callback = finished_callback

    def start(self):
        print('i started!!!!!!!!!!!!!!!!!!!!!')
        self.current_frame = 0
        self.current_values = deepcopy(self.start_values)

    def update(self):
        if not self.finished: 
            
            t = self.current_frame / self.frame_count
            self.current_values = [
                start + t * (final - start)
                for start, final in zip(self.start_values, self.final_values)
            ]
            self.current_frame += 1

            # Check if the animation is complete
            if self.current_frame > self.frame_count and self.finished_callback:
                self.finished_callback()
                self.current_values = self.final_values
                self.finished = True

        return self.current_values

# Pygame initialization
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)

# Initialize Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Square properties
square_size = 50
start_pos = (50, 50)
end_pos = (200,200)

# Define a callback function to be called when the tween is finished
def on_tween_finished():
    print("Tween finished!")

# Create a Tween with a finished callback
tween = Tween(start_pos, end_pos, 2.0, finished_callback=on_tween_finished)

running = True
tween_started = False  # Track whether the tween has started

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            tween.start()  # Start the tween when space key is pressed
            tween_started = True

    
    # Update Tween
    current_pos = [int(value) for value in tween.update()]

    # Draw background
    screen.fill(WHITE)

    # Draw the square at the current position
    pygame.draw.rect(screen, (0, 128, 255), (current_pos[0], current_pos[1], square_size, square_size))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
