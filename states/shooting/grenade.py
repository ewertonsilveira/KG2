import pygame
import os
from states.content_loader import LOADER

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
        img = LOADER.get_grenade_image()
        img = pygame.transform.scale(img, (int(img.get_width()*GRENADE_SCALE), int(img.get_height()*GRENADE_SCALE))) 
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.images = LOADER.get_grenade_explosion_images()
        self.counter = (len(self.images)-1 ) * 10
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self, screen_scroll, obstacle_list, player, enemies):
        # gravity affecting the grenade
        self.vel_y += GRAVITY
        dx = self.direction * self.speed + screen_scroll
        dy = self.vel_y

         #check for collision with level
        if self.timer >= 0:
            for tile in obstacle_list:
                #check collision with walls
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    self.direction *= -1
                    dx = self.direction * self.speed
                #check for collision in the y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    self.speed = 0
                    #check if below the ground, i.e. thrown up
                    if self.vel_y < 0:
                        self.vel_y = 0
                        dy = tile[1].bottom - self.rect.top
                    #check if above the ground, i.e. falling
                    elif self.vel_y >= 0:
                        self.vel_y = 0
                        dy = tile[1].top - self.rect.bottom 

            # update grenade
            self.rect.x += dx
            self.rect.y +=dy

        self.timer -= 1
        if self.timer <= 0:
            img = self.images[int(self.counter/10)]
            newRect = img.get_rect()            
            newRect.center = self.rect.center
            self.image = img
            self.rect = newRect
            self.rect.x += dx
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

    

