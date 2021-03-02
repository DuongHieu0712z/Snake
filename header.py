import pygame

ROW = 20
COL = 20

CELL_SIZE = 20

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 440
SCREEN = (SCREEN_WIDTH, SCREEN_HEIGHT)

FPS = 5

# Color
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Direction
UP = pygame.Vector2(0, -1)
DOWN = pygame.Vector2(0, 1)
LEFT = pygame.Vector2(-1, 0)
RIGHT = pygame.Vector2(1, 0)
