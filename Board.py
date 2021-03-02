import pygame
from header import *


class Board:
    def __init__(self, pos: tuple, row: int, col: int, size: int = CELL_SIZE) -> None:
        self.row = row
        self.col = col
        self.size = size
        self.rect = pygame.Rect(0, 0, size, size)

        self.pos = pygame.Vector2(pos)
        self.width = col * size
        self.height = row * size
        self.surface = pygame.Surface((self.width, self.height))

    def draw(self, surface: pygame.Surface, snake, food) -> None:
        for row in range(self.row):
            for col in range(self.col):
                self.rect.x = col * self.size
                self.rect.y = row * self.size
                if (row + col) % 2:
                    color = (2, 125, 190)
                else:
                    color = (1, 105, 137)
                pygame.draw.rect(self.surface, color, self.rect)
        snake.draw(self.surface)
        food.draw(self.surface)
        surface.blit(self.surface, self.pos)
