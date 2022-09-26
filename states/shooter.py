import pygame
from .base import BaseState


class Shooter(BaseState):
    def __init__(self):
        super(Shooter, self).__init__()
        self.rect = pygame.Rect((0, 0), (80, 80))
        self.rect.center = self.screen_rect.center
        self.next_state = "MENU"

        self.snail_x_pos = self.screen_rect.width
        self.sky_sf = pygame.image.load('public/graphics/sky.png').convert()
        self.ground_sf = pygame.image.load('public/graphics/ground.png').convert()
        self.snail_sf = pygame.image.load('public/graphics/snail/snail1.png').convert_alpha()
        self.snail_rect = self.snail_sf.get_rect(midbottom = (self.snail_x_pos, self.sky_sf.get_height()))

        self.player_sf = pygame.image.load('public/graphics/player/player_walk_1.png').convert_alpha()
        self.player_rect = self.player_sf.get_rect(midbottom = ((50, self.sky_sf.get_height())))

        self.text_sf = self.font.render('Shooter', False, 'Black')


    def draw(self, surface):
        surface.fill(pygame.Color("black"))
                
        if self.snail_rect.right < 0: self.snail_rect.left = self.screen_rect.width
        self.snail_rect.x -= 4

        surface.blit(self.sky_sf,(0, 0))
        surface.blit(self.ground_sf,(0, self.sky_sf.get_height()))
        surface.blit(self.text_sf, (self.screen_rect.width / 2 - self.text_sf.get_width() / 2, 50))
        surface.blit(self.snail_sf, self.snail_rect)
        surface.blit(self.player_sf, self.player_rect)

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self.done = True