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
        pygame.mixer.init()

        self.screen = pygame.display.set_mode(SCREEN)
        pygame.display.set_caption('Snake')

        icon = pygame.image.load('images.png')
        pygame.display.set_icon(icon)

        self.score_board = ScoreBoard()
        self.board = Board()
        self.snake = Snake(SNAKE_POS, RED)
        self.food = Food(GREEN)
        self.food.randomizePosition(self.snake)

        self.score = 0
        self.is_running = True

    def handleEvent(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.KEYDOWN:
                self.snake.handleInput()

    def update(self) -> None:
        self.snake.move(self.board)

        if self.snake.isCollisionFood(self.food):
            self.snake.eatFood()
            self.food.randomizePosition(self.snake)
            self.score += 1

        if self.snake.isCollisionBody():
            self.is_running = False

        text = f'Score:{self.score}'
        self.score_board.setText(text)

    def render(self) -> None:
        self.screen.fill(BLACK)
        self.score_board.draw(self.screen)
        self.board.draw(self.screen, self.snake, self.food)
        pygame.display.update()

    def run(self) -> None:
        time = Time()
        ms_per_frame = 1000 / FPS
        time.start()
        before_time = time.getTicks()
        lag = 0

        while self.is_running:
            time.start()
            current_time = time.getTicks()
            time_past = current_time - before_time
            before_time = current_time
            lag += time_past

            self.handleEvent()
            while lag > ms_per_frame:
                self.update()
                lag -= ms_per_frame
            self.render()

        pygame.quit()
        pygame.mixer.quit()
