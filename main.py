import pygame

from constants import CELL_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH
from snake import Snake

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    snake = Snake()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        snake.update()

        screen.fill("lightgreen")
        snake.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
