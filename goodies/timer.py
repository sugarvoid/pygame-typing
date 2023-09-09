# timer.py 0.1.0

from typing import Callable

# test_timer: Timer = Timer(5)

class Timer:
    def __init__(self, finished_time: int=1, callback: Callable=None) -> None:
        self.time = 0
        self.is_paused: bool = True
        self.finished_time = finished_time
        self.is_finished: bool = False
        self.is_running: bool = False
        self.on_done_func = callback
        if self.on_done_func is None:
            self.on_done_func = self.print_done
    
    def update(self, dt) -> None:
        if not self.is_finished and not self.is_paused:
            self.time += dt
            if self.time > self.finished_time:
                self.is_finished = True
                self.is_running = False
                self.on_done_func()
    
    def start(self):
        self.is_running = True
        self.is_paused = False

    def pause(self):
        self.is_paused = not self.is_paused
    
    def print_done(self) -> None:
        print('I\'m done')