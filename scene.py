from typing import Protocol


class Scene(Protocol):
    def __init__(self):
        raise NotImplementedError()
    def on_enter(self):
        raise NotImplementedError()
    def on_exit(self):
        raise NotImplementedError()
    def input(self, sm, inputStream):
        raise NotImplementedError()
    def update(self, sm, inputStream):
        raise NotImplementedError()
    def draw(self, sm, screen):
        raise NotImplementedError()


