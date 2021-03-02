import pygame


class Time:
    def __init__(self) -> None:
        self.start_tick = 0
        self.pause_tick = 0
        self.is_started = False
        self.is_paused = False

    def start(self) -> None:
        self.is_started = True
        self.is_paused = False
        self.start_tick = pygame.time.get_ticks()

    def stop(self) -> None:
        self.is_started = False
        self.is_paused = False

    def pause(self) -> None:
        if self.is_started and not self.is_paused:
            self.is_paused = True
            self.pause_tick = pygame.time.get_ticks() - self.is_started

    def unpause(self) -> None:
        if self.is_paused:
            self.is_paused = False
            self.start_tick = pygame.time.get_ticks() - self.pause_tick
            self.pause_tick = 0

    def getTicks(self) -> int:
        if self.is_started:
            if self.is_paused:
                return self.pause_tick
            return self.start_tick
        return 0
