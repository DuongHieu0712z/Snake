import pygame
from header import *
from Time import Time
from ScoreBoard import ScoreBoard
from Board import Board
from Snake import Snake
from Food import Food


class Game:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode(SCREEN)
        pygame.display.set_caption('Snake')

        # icon = pygame.image.load('images.png')
        # pygame.display.set_icon(icon)

        self.score_board = ScoreBoard()
        self.board = Board()
        self.snake = Snake(SNAKE_POS, RED)
        self.food = Food(GREEN)
        self.food.randomizePosition(self.snake)

        self.score = 0
        self.is_running = True

        self.time = Time()
        self.before_time = 0
        self.current_time = 0
        self.lag = 0

    def handleEvent(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.KEYDOWN:
                self.snake.handleInput(event.key)

    def update(self) -> None:
        self.snake.move(self.board)

        if self.snake.isCollisionFood(self.food):
            self.snake.eatFood()
            self.food.randomizePosition(self.snake)
            self.score += 1

        if self.snake.isCollisionBody():
            self.is_running = False
            
        self.score_board.setScore(self.score)

    def render(self) -> None:
        self.screen.fill(BLACK)
        self.score_board.draw(self.screen)
        self.board.draw(self.screen, self.snake, self.food)
        pygame.display.update()

    def getTime(self) -> None:
        self.time.start()
        self.current_time = self.time.getTicks()
        time_past = self.current_time - self.before_time
        self.before_time = self.current_time
        self.lag += time_past

    def run(self) -> None:
        ms_per_frame = 1000 / FPS
        while self.is_running:
            self.getTime()
            self.handleEvent()
            while self.lag >= ms_per_frame:
                self.update()
                self.lag -= ms_per_frame
            self.render()
        pygame.quit()
