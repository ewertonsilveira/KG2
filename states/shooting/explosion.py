from email.headerregistry import Group
import pygame
import os

from states.settings import * 

class Explosion(pygame.sprite.Sprite):
    def __init__(self, surface, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.surface = surface
        self.images = []
        for num in range(1, 6):
            img = pygame.image.load(f'public/graphics/explosion/exp{num}.png').convert_alpha()
            img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0