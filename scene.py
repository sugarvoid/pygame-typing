from typing import Protocol
from pygame.display import flip


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


class SceneManager:
    def __init__(self):
        self.scenes = []
    def isEmpty(self):
        return len(self.scenes) == 0
    def enterScene(self):
        if len(self.scenes) > 0:
            self.scenes[-1].onEnter()
    def exitScene(self):
        if len(self.scenes) > 0:
            self.scenes[-1].onExit()
    def input(self, inputStream):
        if len(self.scenes) > 0:
            self.scenes[-1].input(self, inputStream)
    def update(self, inputStream):
        if len(self.scenes) > 0:
            self.scenes[-1].update(self, inputStream)
    def draw(self, screen):
        if len(self.scenes) > 0:
            self.scenes[-1].draw(self, screen)
        # present screen
        flip()
    def push(self, scene):
        self.exitScene()
        self.scenes.append(scene)
        self.enterScene()
    def pop(self):
        self.exitScene()
        self.scenes.pop()
        self.enterScene()
    def set(self, scenes):
        # pop all scenes
        while len(self.scenes) > 0:
            self.pop()
        # add new scenes
        for s in scenes:
            self.push(s)
