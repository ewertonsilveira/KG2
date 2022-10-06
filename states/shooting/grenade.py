from email.headerregistry import Group
import pygame
import os
from states.game_images import GAME_IMAGES

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
        img = GAME_IMAGES.get_grenade_image()
        img = pygame.transform.scale(img, (int(img.get_width()*GRENADE_SCALE), int(img.get_height()*GRENADE_SCALE))) 
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.images = GAME_IMAGES.get_grenade_explosion_images()
        self.counter = (len(self.images)-1 ) * 10

    def update(self, player, enemies):
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
            for e in enemies:
                self.apply_damage(e)

            self.apply_damage(player)
            
    def apply_damage(self, target):
        if abs(self.rect.centerx - target.rect.centerx) < TILE_SIZE * 2 and \
            abs(self.rect.centery - target.rect.centery) < TILE_SIZE * 2 :
            if target.alive:
                print(target.char_type, target.health)
                target.health -= GRENADE_HEALTH_DAMAGE

    

