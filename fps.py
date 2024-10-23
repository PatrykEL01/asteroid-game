import pygame


font = pygame.font.Font(None, 30)

def display_fps(screen, clock):
    fps = str(int(clock.get_fps()))
    fps_text = font.render(fps, True, pygame.Color('white'))
    screen.blit(fps_text, (10, 10))