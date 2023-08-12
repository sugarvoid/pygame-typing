import pygame
import time
from util import Text, ProgressBar
from settings import FPS, SCREEN_HEIGHT, SCREEN_WIDTH, GAME_SCREEN, TITLE, BG_COLOR
import settings


LETTERS: str = 'QWERTYUIOPASDFGHJKLZXCVBNM'
word_list: list = []
used_words: list = []


#TODO: Load txt list into a python list. So you don't need to load it each time?
def search_for_word(word:str) -> bool:
    has_word: bool 
    for w in word_list:
        if w == word:
            has_word = True
            break
        else:
            has_word = False
    return has_word


def load_words() -> None:
    myfile = open("word_list.txt", "r")
    while myfile:
        line  = myfile.readline()
        if line != "":
            word_list.append(line.strip('\n'))
        else:
            break
    myfile.close() 


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.dt: float = 0
        self.clock: pygame.Clock = pygame.time.Clock()
        self.is_running: bool = True
        self.state: int = 0 # 0=title, 1=play, 2=game_over
        self.canvas = pygame.Surface((GAME_SCREEN.x,GAME_SCREEN.y))
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)

        load_words()
        print(search_for_word('widget'))

        self.title_text = pygame.sprite.Group()
        self.game_text = pygame.sprite.Group()
        self.gameover_text = pygame.sprite.Group()

        self._add_text()



        self.current_word: str = ''
        self.round_timer = ProgressBar(self.canvas, pygame.Color('gold1'),60,[10,10])

    def _add_text(self) -> None:
        # Title
        print(SCREEN_WIDTH/2)
        self.title_text.add(Text("Game", "green", (100, 0)))
        self.title_text.add(Text("Title", "white", (0, 50)))

        # Gameplay
        self.game_text.add(Text('', "yellow", (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)))
        # Game Over


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
                case 0: # Title Screen
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.title_text.empty()
                            self.state = 1

                case 1:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            print(f'submitting {self.current_word}.')
                        elif event.key == pygame.K_BACKSPACE:
                            pass
                        else:
                            key_pressed = event.unicode.upper()
                            if key_pressed in LETTERS and key_pressed != "":
                                print(key_pressed)
                                self.current_word += key_pressed
                                print(f'Current word: {self.current_word}')

                case 2:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            # TODO: Restart game
                            print('Restart the game')


    def _check_for_quit(self, event) -> None:
        if event.type == pygame.QUIT:
                #exit()
                self.is_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                #exit()
                self.is_running = False

#region UPDATE_FUNTIONS 
    def update(self, dt):
        self._get_input()

        match self.state:
            case 0: #Title
                self.update_title()
            case 1: #Gameplay
                self.update_play(dt)
            case 2: #Gameover
                self.update_gameover(dt)
        pygame.display.flip()  # Refresh on-screen display
        self.clock.tick(FPS) # wait until next frame (at 60 FPS)

    
    def update_title(self) -> None:
        pass


    def update_play(self, dt) -> None:
        self.round_timer.update(dt)
        
    

    def update_gameover(self, dt) -> None:
        pass
#endregion 

#region DRAW_FUNCTIONS

    def draw(self):
        self.canvas.fill(BG_COLOR)
        match self.state:
            case 0:
                self.draw_title()
            case 1:
                self.round_timer.draw()
            case 2:
                self.draw_gameover()
 

        self.screen.blit(pygame.transform.scale(self.canvas,(SCREEN_WIDTH,SCREEN_HEIGHT)),(0,0))
        
            
    
    def draw_title(self) -> None:
        self.title_text.draw(self.canvas)

    def draw_play(self) -> None:
        pass
    

    def draw_gameover(self) -> None:
        all_text = pygame.sprite.Group()
        all_text.add(Text("Hello", "blue", (0, 0)))
        all_text.add(Text("World!", "white", (0, 50)))
        all_text.draw(self.canvas)
#endregion 