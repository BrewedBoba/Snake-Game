import pygame

from constants import NUMBER_OF_CELL, SCREEN_HEIGHT, SCREEN_WIDTH


def show_score(color, size, score, screen):
    score_font = pygame.font.Font(None, size)
    score_surface = score_font.render("Score: " + str(score), True, color)
    screen.blit(score_surface, (5, 6))

def game_over_screen(color, size, screen):
    game_over_font = pygame.font.Font(None, size)
    game_over_surface = game_over_font.render("GAME OVER", True, color)
    screen.blit(game_over_surface, (SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3))
