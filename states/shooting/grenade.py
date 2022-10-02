from email.headerregistry import Group
import pygame
import os
from states.gameImages import GAME_IMAGES

from states.settings import *

class Grenade(pygame.sprite.Sprite):
    def __init__(self, surface, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.surface = surface
        self.bullet_image = None
        self.vel_y = -11
        self.speed = GRENADE_SPEED
        self.timer = GRENADE_TIMER
        self.direction = direction
        self.image = GAME_IMAGES.get_grenade_image()
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.images = GAME_IMAGES.get_grenade_explosion_images()
        self.counter = (len(self.images)-1 ) * 10

    def update(self, group):
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
            img = self.images[int(self.counter/10)]
            self.image = img
            newRect = self.image.get_rect()
            newRect.center = self.rect.center
            self.rect = newRect
            self.counter -= 1

        if self.counter < 0:
            self.kill()
            # do damage to anyone close
            for e in group:
                if abs(self.rect.centerx - e.rect.centerx) < TILE_SIZE * 2 and \
                    abs(self.rect.centery - e.rect.centery) < TILE_SIZE * 2 :
                    if e.alive:
                        e.health -= GRENADE_HEALTH_DAMAGE


    

