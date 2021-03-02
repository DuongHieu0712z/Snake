import pygame
from header import *


class Board:
    def __init__(self) -> None:
        self.pos = pygame.Vector2(BOARD_POS)
        self.width = BOARD_WIDTH
        self.height = BOARD_HEIGHT
        self.row = ROW
        self.col = COL
        self.size = CELL_SIZE
        self.rect = pygame.Rect(0, 0, self.size, self.size)
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
