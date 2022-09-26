import pygame
from .base import BaseState

class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('public/graphics/player/idle/0.png').convert_alpha()
        self.image = pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height()*scale)))
        self.rect = img.get_rect(center = (x, y))
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Shooter(BaseState):
    def __init__(self):
        super(Shooter, self).__init__()
        self.next_state = "MENU"
        x = 200
        y = 200
        scale = 3

        self.players = [Soldier(x, y, scale), Soldier(x+50, y, scale)]

        # self.ground_sf = pygame.image.load('public/graphics/ground.png').convert()
        # self.snail_sf = pygame.image.load('public/graphics/snail/snail1.png').convert_alpha()
        # self.snail_rect = self.snail_sf.get_rect(midbottom = (self.snail_x_pos, self.sky_sf.get_height()))

        # self.player_sf = pygame.image.load('public/graphics/player/player_walk_1.png').convert_alpha()
        # self.player_rect = self.player_sf.get_rect(midbottom = ((50, self.sky_sf.get_height())))

        # self.text_sf = self.font.render('Shooter', False, 'Black')

    def draw(self, surface):
        surface.fill(pygame.Color("black"))
        for index, player in enumerate(self.players):
            player.draw(surface)

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self.done = True