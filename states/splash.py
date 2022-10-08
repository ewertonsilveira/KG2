import pygame

from states.fonts import FONTS
from .base import BaseState

tenSeconds = 15000 * 1000
initialRotation = 60
class Splash(BaseState):
    def __init__(self):
        super(Splash, self).__init__()
        x,y = self.screen_rect.center
        self.title = FONTS.primary_font.render("KYLIE GAMES", True, pygame.Color("black"))
        self.title_rect = self.title.get_rect(center=(x+15,y+20))

        logo = pygame.image.load('assets/graphics/logo.png').convert_alpha()
        self.logo_sf = pygame.transform.scale(logo, (100,115))
 
        bg = pygame.image.load('assets/graphics/bg2.png').convert_alpha()
        self.bg_sf = pygame.transform.scale(bg, self.screen_rect.size)

        self.next_state = "MENU"
        self.time_active = 0
        self.rotation = initialRotation
        self.incrementalValue = 0

    def update(self, dt):
        self.time_active += dt
        if self.time_active >= tenSeconds:
            self.done = True

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                self.done = True
            elif event.key == pygame.K_SPACE:
                self.done = True
            elif event.key == pygame.K_ESCAPE:
                self.quit = True

    def draw(self, surface):
        
        surface.fill(pygame.Color("lightblue"))
        surface.blit(self.bg_sf, (0,0))
            
        if self.rotation >= initialRotation:
            self.incrementalValue = -1
        
        if self.rotation < -initialRotation:
            self.incrementalValue = 1

        self.rotation += self.incrementalValue

        logo = pygame.transform.rotate(self.logo_sf, self.rotation)
        
        x,y = self.screen_rect.center
        logo_rect = logo.get_rect(center=(x,y-60))
        surface.blit(logo, logo_rect)
        surface.blit(self.title, self.title_rect)
