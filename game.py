from os import path, remove
from random import randint
from string import ascii_lowercase

from settings import FPS, GAME_SCREEN, TITLE, BG_COLOR, TEXT_COLOR, MENU_TEXT_COLOR

import pygame.time
import pygame.event
import pygame.display

from pygame import init
from pygame import Clock, Surface, Color
from pygame import KEYDOWN, K_ESCAPE, K_RETURN, K_BACKSPACE, K_r, QUIT, K_SPACE

from pygame.display import set_mode, set_caption
from pygame.sprite import Group

from goodies.progress_bar import ProgressBar
from goodies.text import Text




LETTERS: str = 'QWERTYUIOPASDFGHJKLZXCVBNM'
DEBUG: bool = False
USED_WORDS_FILE: str = 'word_history.txt'
CENTER_TEXT_POS = (GAME_SCREEN.x/2, GAME_SCREEN.y/2)
LETTERS_TO_AVOID: list = ['x', 'q', 'u', 'z', 'w', 'y', 'i', 'v'] # For starting letter 
DEFAULT_FONT = 'monogram'


class Game:
    def __init__(self) -> None:

        init()
        self.MAX_WORD_LENGTH: int = 13
        self.word_list: list = []
        self.used_words: list = []
        self.used_words_txt = open(USED_WORDS_FILE, 'a+')
        self.valid_words: list = self.load_words('word_list.txt')
        
        if DEBUG:
            print('debug on')
            if path.exists(USED_WORDS_FILE):
                remove(USED_WORDS_FILE)
            else:
                print("The file does not exist") 

        self.dt: float = 0
        self.clock: Clock = pygame.time.Clock()
        self.is_running: bool = True
        self.state: int = 0 # 0=title, 1=play, 2=game_over
        self.canvas = Surface((GAME_SCREEN.x,GAME_SCREEN.y))
        self.screen = set_mode((GAME_SCREEN.x, GAME_SCREEN.y))
        set_caption(TITLE)
        self.load_words('word_list.txt')
        self.create_text_groups()
        self._add_text()
        self.current_word: str = ''
        self.pgb_round_timer = ProgressBar(self.canvas, 
                                       250, 
                                       Color('#f2d3ab'), 
                                       Color('#494d7e'), 
                                       250,
                                       [CENTER_TEXT_POS[0] - 120, 
                                        CENTER_TEXT_POS[1] + 90], 
                                        None)
        
    def setup(self) -> None:
        self.current_word = self.get_starting_letter()
        self.lbl_current_word.change_text(self.current_word)
        self.lbl_current_word.rect.center = CENTER_TEXT_POS

    def create_text_groups(self):
        self.title_text = Group()
        self.game_text = Group()
        self.gameover_text = Group()

    def _add_text(self) -> None:
        # Title
        self.title_text.add(Text(DEFAULT_FONT, 80, 'Typing', Color(MENU_TEXT_COLOR), (100, 100)))
        self.title_text.add(Text(DEFAULT_FONT, 80,"Game", Color(MENU_TEXT_COLOR), (100, 150)))
        self.title_text.add(Text(DEFAULT_FONT, 60, "Press Space", Color(MENU_TEXT_COLOR), (280, 400)))

        self.lbl_current_word: Text = Text("monogram", 150, '', TEXT_COLOR, (80, 350))
        self.lbl_current_word.change_location((100,30))
        self.game_text.add(self.lbl_current_word)

    #TODO: Load txt list into a python list. So you don't need to load it each time?
    def search_for_word(self, word:str) -> bool:
        has_word: bool 
        for w in self.word_list:
            if w == word:
                has_word = True
                break
            else:
                has_word = False
        return has_word
    
    def get_starting_letter(self) -> chr:
        usable_letter: bool = False

        while not usable_letter:
            index = randint(0, 25)
            letter = ascii_lowercase[index]
            if letter not in LETTERS_TO_AVOID:
                usable_letter = True

        return letter.upper()

    def load_words(self, file_name) -> list:
        word_list = []
        myfile = open(file_name, "r")
        while myfile:
            line  = myfile.readline()
            if line != "":
                word_list.append(line.strip('\n'))
            else:
                break
        myfile.close() 
        return word_list

    def is_new_word(self, word: str) -> bool:
        used_words = self.load_words(USED_WORDS_FILE)
        if used_words.count(word) == 0:
            return True
        else:
            return False

    def is_valid_word(self, word:str) -> bool:
        word = word.strip().lower()
        has_word: bool = False
        for w in self.valid_words:
            if w == word:
                has_word = True
                break
            else:
                has_word = False
        return has_word

    def run_game(self) -> None:
        while self.is_running:
            dt = self.clock.tick(60)/1000.0
            self.update(dt)
            self.draw()
    
    def _get_input(self) -> None:
        for event in pygame.event.get():
            self._check_for_quit(event)
            match self.state:
                case 0: # Title Screen
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            self.state = 1

                case 1:
                    if event.type == KEYDOWN:
                        if event.key == K_RETURN:
                            print(f'submitting {self.current_word}.')
                            # TODO: Submit word()
                            if self.is_valid_word(self.current_word):
                                print('ding')
                                self.pgb_round_timer.reset()
                            else:
                                print('wrong')
                            self.current_word = self.current_word[-1]
                        elif event.key == K_BACKSPACE:
                            if len(self.current_word) > 1:
                                self.current_word = self.current_word[:-1]
                        else:
                            key_pressed = event.unicode.upper()
                            if key_pressed in LETTERS and \
                                  key_pressed != "" and \
                                    len(self.current_word) <= self.MAX_WORD_LENGTH:
                                self.current_word += key_pressed
                        self.lbl_current_word.change_text(self.current_word)
                        self.lbl_current_word.rect.center = CENTER_TEXT_POS

                case 2:
                    if event.type == KEYDOWN:
                        if event.key == K_r:
                            # TODO: Restart game
                            print('Restart the game')

    def _check_for_quit(self, event) -> None:
        if event.type == QUIT:
                #exit()
                self.is_running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                #exit()
                self.is_running = False

    def update(self, dt):
        self._get_input()

        match self.state:
            case 0: # Title
                self.update_title()
            case 1: # Gameplay
                self.update_play(dt)
            case 2: # Gameover
                self.update_gameover(dt)
        pygame.display.flip()  # Refresh on-screen display
        self.clock.tick(FPS) # wait until next frame

    def update_title(self) -> None:
        pass

    def update_play(self, dt) -> None:
        self.pgb_round_timer.update(dt)

    def update_gameover(self, dt) -> None:
        pass

    def draw(self):
        self.canvas.fill(BG_COLOR)
        match self.state:
            case 0:
                self.draw_title()
            case 1:
                self.game_text.draw(self.canvas)
                self.pgb_round_timer.draw()
            case 2:
                self.draw_gameover()
 
        self.screen.blit(self.canvas,(0,0))
        
    def draw_title(self) -> None:
        self.title_text.draw(self.canvas)

    def draw_play(self) -> None:
        pass

    def draw_gameover(self) -> None:
        # TODO: Finish
        all_text = Group()
        all_text.add(Text("Hello", "blue", (0, 0)))
        all_text.add(Text("World!", Color(MENU_TEXT_COLOR), (0, 50)))
        all_text.draw(self.canvas)
