import pygame
from header import *


class Cell:
    def __init__(self, pos: tuple, color: tuple, size: int) -> None:
        self.rect = pygame.Rect(*pos, size, size)
        self.color = color

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, (127, 127, 127), self.rect, 1)
