from email.headerregistry import Group
import pygame
import os

from states.settings import *
from states.shooting.explosion import Explosion 

class Grenade(pygame.sprite.Sprite):
    def __init__(self, surface, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.surface = surface
        self.bullet_image = None
        self.vel_y = -11
        self.speed = GRENADE_SPEED
        self.timer = GRENADE_TIMER
        self.direction = direction
        self.image = self.get_image()
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.grenade_explode_group = pygame.sprite.Group()

    def update(self):
        # gravity affecting the grenade
        self.vel_y += GRAVITY
        dx = self.direction * self.speed
        dy = self.vel_y

        # stop when touch the ground
        if self.rect.bottom + dy >= GROUND:
            dy = GROUND - self.rect.bottom
            self.speed = 0
        
        # check if bullet has gone off screen
        if self.rect.left + dx < 0 or self.rect.right + dx > self.surface.get_width():
            self.direction *= -1
            dx = self.direction * self.speed

        self.rect.y +=dy
        self.rect.x += dx

        self.timer -= 1
        if self.timer <= 0:
            explosion = Explosion(self.surface, self.rect.x, self.rect.y, GRENADE_EXPLOSION_SCALE)
            self.grenade_explode_group.add(explosion)
            self.kill()
    
        self.grenade_explode_group.update()
        self.grenade_explode_group.draw(self.surface)
    
    def get_image(self):
        if self.bullet_image == None:        
            self.bullet_image = pygame.image.load("public/graphics/icons/grenade.png").convert_alpha();
        return self.bullet_image
