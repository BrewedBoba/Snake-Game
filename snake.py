import pygame

from constants import CELL_SIZE

class Snake:
    def __init__(self) -> None:
        self.snake_body = [pygame.Vector2(14, 14), pygame.Vector2(14, 15), pygame.Vector2(14, 16)]
        self.direction = pygame.Vector2(0, 1)

    def draw(self, screen) -> None:
        for square in self.snake_body:
            squares = pygame.Rect(square.x * CELL_SIZE, square.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, "darkgreen", squares)

    def move(self) -> None:
        new_head = self.snake_body[-1] + self.direction
        self.snake_body.append(new_head)
        self.snake_body.pop(0)

    def update() -> None:
