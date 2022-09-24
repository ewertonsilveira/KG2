import pygame
from .base import BaseState

tenSeconds = 15000 * 1000
initialRotation = 35
class Splash(BaseState):
    def __init__(self):
        super(Splash, self).__init__()
        self.title = self.font.render("Welcome to Kylie's Game", True, pygame.Color("blue"))
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        self.logo_sf = pygame.image.load('public/graphics/logo.png').convert_alpha()
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
        surface.fill(pygame.Color("black"))
            
        if self.rotation >= initialRotation:
            self.incrementalValue = -1
        
        if self.rotation < -initialRotation:
            self.incrementalValue = 1

        self.rotation += self.incrementalValue

        logo = pygame.transform.scale(self.logo_sf, (90,105))
        logo = pygame.transform.rotate(logo, self.rotation)
        logo_rect = self.logo_sf.get_rect(center=self.screen_rect.center)

        surface.blit(logo, logo_rect)
        surface.blit(self.title, self.title_rect)
