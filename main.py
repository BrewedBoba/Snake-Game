import pygame

from constants import CELL_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH
from snake import Snake

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    snake = Snake()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("lightgreen")
        snake.draw(screen)
        pygame.display.flip()
        clock.tick(10)

if __name__ == "__main__":
    main()
