import pygame
from states.settings import * 

class Decoration(pygame.sprite.Sprite):
    def __init__(self, img, scale, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height()*scale))) 
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))

    def update(self, screen_scroll):
        self.rect.x += screen_scroll