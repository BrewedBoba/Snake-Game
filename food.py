import random

import pygame

from constants import CELL_SIZE

class Food:
    def __init__(self, snake) -> None:
        self.get_snake_body_position(snake)

    def get_snake_body_position(self, snake):
        self.position = pygame.Vector2(random.randrange(0, 30), random.randrange(0, 30))
        while self.position in snake:
            self.position = pygame.Vector2(random.randrange(0, 30), random.randrange(0, 30))
        return self.position

    def draw(self, screen):
        position = self.position
        position = pygame.Rect(position.x * CELL_SIZE, position.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, "red", position, 0, 10)

    def eaten(self, snake_head, snake):
        if self.position == snake_head:
            self.get_snake_body_position(snake)
            return True
        return False
