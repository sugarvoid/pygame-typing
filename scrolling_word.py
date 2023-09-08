# scrolling_word.py

class Word:
    def __init__(self) -> None:
        self.y_pos: int
        self.y_pos: int
        self.value: str

    def update(self, dt):
        self.y_pos -= 30 * dt

    def draw(self) -> None:
        pass