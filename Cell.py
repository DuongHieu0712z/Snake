import pygame
from header import *


class Cell:
    def __init__(self, pos: tuple, color: tuple, size: int) -> None:
        self.rect = pygame.Rect(*pos, size, size)
        self.color = color

    def draw(self, surface: pygame.Surface, is_head: bool = False, direction = None) -> None:
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, (127, 127, 127), self.rect, 1)

        if is_head:
            if direction == UP:
                x1, x2, y1, y2 = 1, 3, 1, 1
            elif direction == DOWN:
                x1, x2, y1, y2 = 1, 3, 3, 3
            elif direction == LEFT:
                x1, x2, y1, y2 = 1, 1, 1, 3
            elif direction == RIGHT:
                x1, x2, y1, y2 = 3, 3, 1, 3

            r = 2
            x1 = self.rect.x + self.rect.w / 4 * x1
            x2 = self.rect.x + self.rect.w / 4 * x2
            y1 = self.rect.y + self.rect.h / 4 * y1
            y2 = self.rect.y + self.rect.h / 4 * y2
            pygame.draw.circle(surface, BLACK, (x1, y1), r)
            pygame.draw.circle(surface, BLACK, (x2, y2), r)
