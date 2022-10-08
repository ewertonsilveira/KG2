import pygame

from states.fonts import FONTS

class BaseState(object):
    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pygame.display.get_surface().get_rect()
        self.persist = {}

    def startup(self, persistent):
        self.persist = persistent

    def get_event(self, event):
        pass

    def update(self, dt):
        pass

    def draw(self, surface):
        pass
    
    def draw_text(self, text, font, text_color, x, y):
        img = FONTS.primary_font.render(text, True, text_color)
        self.screen_rect.blit(img, (x,y))
    
    def draw_bg(self, surface, color):
        surface.fill(color)