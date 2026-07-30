import pygame

from constants import CELL_SIZE, SNAKE_SPEED

class Snake:
    def __init__(self) -> None:
        self.snake_body = [pygame.Vector2(14, 14), pygame.Vector2(14, 15), pygame.Vector2(14, 16)]
        self.direction = pygame.Vector2(0, 0)
        self.time_since_last_move = 0

    def draw(self, screen) -> None:
        for square in self.snake_body:
            squares = pygame.Rect(square.x * CELL_SIZE, square.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, "darkgreen", squares)

    def move(self) -> None:
        new_head = self.snake_body[-1] + self.direction
        self.snake_body.append(new_head)
        self.snake_body.pop(0)

    def update(self, dt) -> None:
        self.time_since_last_move += dt
        keys = pygame.key.get_pressed()
        if self.time_since_last_move > (CELL_SIZE / SNAKE_SPEED):
            self.move()
            self.time_since_last_move -= (CELL_SIZE / SNAKE_SPEED)
        if keys[pygame.K_s] and self.direction != pygame.Vector2(0, -1):
            self.direction = pygame.Vector2(0, 1)
        if keys[pygame.K_w] and self.direction != pygame.Vector2(0, 1):
            self.direction = pygame.Vector2(0, -1)
        if keys[pygame.K_a] and self.direction != pygame.Vector2(1, 0):
            self.direction = pygame.Vector2(-1, 0)
        if keys[pygame.K_d] and self.direction != pygame.Vector2(-1, 0):
            self.direction = pygame.Vector2(1, 0)
