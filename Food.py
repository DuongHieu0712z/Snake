import pygame
import random
from header import *
from Cell import Cell


class Food(Cell):
    def __init__(self, color: tuple, size: int = CELL_SIZE) -> None:
        super().__init__((0, 0), color, size)

    def randomizePosition(self, snake) -> None:
        while True:
            row = random.randrange(ROW)
            col = random.randrange(COL)
            self.rect.x = col * CELL_SIZE
            self.rect.y = row * CELL_SIZE
            if self.rect not in map(lambda cell: cell.rect, snake.body):
                break
