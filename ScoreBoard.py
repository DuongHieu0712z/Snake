import pygame
from header import *


class ScoreBoard:
    def __init__(self) -> None:
        self.pos = pygame.Vector2(SCORE_BOARD_POS)
        self.width = SCORE_BOARD_WIDTH
        self.height = SCORE_BOARD_HEIGHT
        self.surface = pygame.Surface((self.width, self.height))

        self.font = pygame.font.SysFont('consolas', 16)
        self.font.bold = True
        self.text = pygame.Surface((0, 0))

    def setText(self, text: str) -> None:
        self.text = self.font.render(text, True, WHITE)

    def draw(self, surface: pygame.Surface) -> None:
        self.surface.fill(BLACK)
        x = (self.width - self.text.get_width()) / 2
        y = (self.height - self.text.get_height()) / 2
        self.surface.blit(self.text, (x, y))
        surface.blit(self.surface, self.pos)
