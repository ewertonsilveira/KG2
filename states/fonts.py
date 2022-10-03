import pygame

class GameFonts(pygame.font.Font):
    def __init__(self):
        self.primary_font = None

    def init(self):
        self.primary_font = pygame.font.Font('public/font/Pixeltype.ttf', 50)


FONTS = GameFonts()