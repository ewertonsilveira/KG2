from email.headerregistry import Group
import pygame
import os

from states.settings import * 

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = BULLET_SPEED
        self.direction = direction
        self.image = self.get_image()
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.bullet_image = None

    bullet_image = None

    def get_image(self):
        if self.bullet_image == None:        
            self.bullet_image = pygame.image.load("public/graphics/icons/bullet.png").convert_alpha();
        return self.bullet_image
