
import pygame
import time
from util import Text
import settings

class Word:
    def __init__(self) -> None:
        self.X_POS: int
        self.y_pos: int
        self.value: str


    def update(self, dt):
        self.y_pos -= 30 * dt


    def draw(self) -> None:
        pass


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.dt: float = 0
        self.clock: pygame.Clock = pygame.time.Clock()
        self.is_running: bool = True
        self.state: int = 0 # 0=title, 1=play, 2=game_over
        self.canvas = pygame.Surface((settings.game_screen.x,settings.game_screen.y))
        self.screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
        pygame.display.set_caption(settings.title)


        self.current_word: str = ''


    def run_game(self) -> None:
        previous_time = time.time()
        while self.is_running:
            now = time.time()
            dt = now - previous_time
            previous_time = now
            ##dt *= 60
            self.update(dt)
            self.draw()
    
    def _get_input(self) -> None:
        for event in pygame.event.get():
            self._check_for_quit(event)
            match self.state:
                case 0:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.state = 1
                case 1:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            pass
                        else:
                            key_pressed = event.unicode.upper()
                            if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                                print(key_pressed)
                                self.current_word += key_pressed
                                print(f'Current word: {self.current_word}')
                case 2:
                    pass


    def _check_for_quit(self, event) -> None:
        if event.type == pygame.QUIT:
                #exit()
                self.is_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                #exit()
                self.is_running = False
# Draw Functions

    def update(self, dt):
        self._get_input()

        match self.state:
            case 0:
                self.update_title()
            case 1:
                self.update_play()
            case 2:
                self.update_gameover(dt)
        pygame.display.flip()  # Refresh on-screen display
        self.clock.tick(settings.FPS) # wait until next frame (at 60 FPS)

    
    def update_title(self) -> None:
        pass


    def update_play(self) -> None:
        pass
    

    def update_gameover(self, dt) -> None:
        pass
    
    def draw(self):
        self.canvas.fill(settings.bg_color)
        match self.state:
            case 0:
                self.draw_title()
            case 1:
                pass
            case 2:
                self.draw_gameover()
 

        self.screen.blit(
            pygame.transform.scale(
                self.canvas,
               (settings.screen_width,settings.screen_height)), (0,0))
        
            
    
    def draw_title(self) -> None:

        all_text = pygame.sprite.Group()
        all_text.add(Text("Hello", "blue", (0, 0)))
        all_text.add(Text("World!", "white", (0, 50)))
        all_text.draw(self.canvas)

    def draw_play(self) -> None:
        pass
    

    def draw_gameover(self) -> None:
        all_text = pygame.sprite.Group()
        all_text.add(Text("Hello", "blue", (0, 0)))
        all_text.add(Text("World!", "white", (0, 50)))
        all_text.draw(self.canvas)


if __name__ == '__main__':
    my_game = Game()
    my_game.run_game()