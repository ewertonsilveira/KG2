from email.headerregistry import Group
import pygame
import os

from states.settings import * 

class Bullet(pygame.sprite.Sprite):
    def __init__(self, surface, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.surface = surface
        self.bullet_image = None
        self.speed = BULLET_SPEED
        self.direction = direction
        self.image = self.get_image()
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def update(self):
        # move bullet
        self.rect.x += self.direction * self.speed
        # check if bullet has gone off scree
        if self.rect.right < 0 or self.rect.left > self.surface.get_width():
            self.kill()


    def get_image(self):
        if self.bullet_image == None:        
            self.bullet_image = pygame.image.load("public/graphics/icons/bullet.png").convert_alpha();
        return self.bullet_image
