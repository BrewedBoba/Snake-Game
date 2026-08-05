import pygame
import sys
from constants import CELL_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH
from food import Food
from snake import Snake
from ui import show_score

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #Set the Window
    pygame.display.set_caption("Snake Game") #set the display caption
    clock = pygame.time.Clock()
    dt = 0.0
    snake = Snake()
    score = 0
    food = Food(snake.snake_body)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        snake.update(dt)
        snake.teleport()

        if food.eaten(snake.snake_body[-1], snake.snake_body) == True:
            snake.grow()
            score += 1

        if snake.collide_with_itself() == True:
            sys.exit()

        screen.fill("lightgreen")
        snake.draw(screen)
        food.draw(screen)
        show_score("black", 36, score, screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
