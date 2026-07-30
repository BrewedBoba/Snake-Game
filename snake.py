import pygame

from constants import CELL_SIZE, NUMBER_OF_CELL, SNAKE_SPEED

class Snake:
    def __init__(self) -> None:
        self.snake_body = [pygame.Vector2(14, 14), pygame.Vector2(14, 15), pygame.Vector2(14, 16)]
        self.direction = pygame.Vector2(0, 1)
        self.time_since_last_move = 0
        self.has_move = False

    def draw(self, screen) -> None:
        for square in self.snake_body:
            squares = pygame.Rect(square.x * CELL_SIZE, square.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, "darkgreen", squares)


    def move(self) -> None:
        if self.has_move == True:
            new_head = self.snake_body[-1] + self.direction
            self.snake_body.append(new_head)
            self.snake_body.pop(0)

    def update(self, dt) -> None:
        # Adding deltaTime
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.has_move = True
        self.time_since_last_move += dt
        # Once time_since_last_move is bigger than the threshold, then the snake moves.
        if self.time_since_last_move > (CELL_SIZE / SNAKE_SPEED):
            self.move()
            self.time_since_last_move -= (CELL_SIZE / SNAKE_SPEED)
        # controls for the snake movement
        if keys[pygame.K_s] and self.direction != pygame.Vector2(0, -1):
            self.direction = pygame.Vector2(0, 1)
        if keys[pygame.K_w] and self.direction != pygame.Vector2(0, 1):
            self.direction = pygame.Vector2(0, -1)
        if keys[pygame.K_a] and self.direction != pygame.Vector2(1, 0):
            self.direction = pygame.Vector2(-1, 0)
        if keys[pygame.K_d] and self.direction != pygame.Vector2(-1, 0):
            self.direction = pygame.Vector2(1, 0)


    def collide_with_itself(self) -> bool:
        head = self.snake_body[-1]
        return head in self.snake_body[:-1]

    def teleport(self) -> None:
        for body in self.snake_body:
            if body.x > NUMBER_OF_CELL - 1:
                body.x = 0
            elif body.x < 0:
                body.x = NUMBER_OF_CELL - 1
            if body.y > NUMBER_OF_CELL - 1:
                body.y = 0
            elif body.y < 0:
                body.y = NUMBER_OF_CELL - 1
