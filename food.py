import random

import pygame

from constants import CELL_SIZE

class Food:
    def __init__(self) -> None:
        self.position = pygame.Vector2(random.randrange(0, 30), random.randrange(0, 30))

    def draw(self, screen):
        position = self.position
        position = pygame.Rect(position.x * CELL_SIZE, position.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, "red", position)

    def eaten(self, other):
        if self.position == other:
            self.position = pygame.Vector2(random.randrange(0, 30), random.randrange(0, 30))
