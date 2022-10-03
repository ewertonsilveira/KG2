import pygame

class GameFonts(pygame.font.Font):
    def __init__(self):
        self.primary_font = None
        self.secondary_font = None

    def init(self):
        self.primary_font = pygame.font.Font('public/font/Pixeltype.ttf', 50)
        self.secondary_font = pygame.font.SysFont('Futura', 20)


FONTS = GameFonts()