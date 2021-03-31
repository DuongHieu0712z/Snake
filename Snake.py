import pygame
import random
from copy import deepcopy
from header import *
from Cell import Cell


class Snake:
    def __init__(self, pos: tuple, color: tuple, size: int = CELL_SIZE) -> None:
        self.direction = random.choice((UP, DOWN, LEFT, RIGHT))
        self.body = []
        pos = list(pos)
        length = 3
        for _ in range(length):
            cell = Cell(pos, color, size)
            self.body.append(cell)
            pos[0] -= size * self.direction.x
            pos[1] -= size * self.direction.y
        self.head = self.body[0]
        self.tail = self.body[-1]
        self.size = size

    def handleInput(self, key) -> None:
        if key == pygame.K_UP or key == pygame.K_w:
            if self.direction != DOWN:
                self.direction = UP
        elif key == pygame.K_DOWN or key == pygame.K_s:
            if self.direction != UP:
                self.direction = DOWN
        elif key == pygame.K_LEFT or key == pygame.K_a:
            if self.direction != RIGHT:
                self.direction = LEFT
        elif key == pygame.K_RIGHT or key == pygame.K_d:
            if self.direction != LEFT:
                self.direction = RIGHT

    def isCollisionFood(self, food) -> bool:
        return self.head.rect == food.rect

    def eatFood(self) -> None:
        self.body.append(self.tail)
        pygame.mixer.Sound('sound.wav').play()
    
    def isCollisionBody(self) -> bool:
        return self.head.rect in map(lambda cell: cell.rect, self.body[1:])

    def handleCollisionBorder(self, board) -> None:
        if self.head.rect.x < 0:
            self.head.rect.x = board.width - self.size
        elif self.head.rect.x >= board.width:
            self.head.rect.x = 0

        if self.head.rect.y < 0:
            self.head.rect.y = board.height - self.size
        elif self.head.rect.y >= board.height:
            self.head.rect.y = 0

    def move(self, board) -> None:
        self.tail = self.body[-1]
        self.body[1:] = deepcopy(self.body[:-1])
        self.head.rect.x += self.size * self.direction.x
        self.head.rect.y += self.size * self.direction.y
        self.body[0] = self.head
        self.handleCollisionBorder(board)

    def draw(self, surface: pygame.Surface) -> None:
        for cell in self.body:
            cell.draw(surface)
