import pygame


def show_score(color, size, score, screen):
    score_font = pygame.font.Font(None, size)
    score_surface = score_font.render("Score: " + str(score), True, color)
    screen.blit(score_surface, (5, 6))
