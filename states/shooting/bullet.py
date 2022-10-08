from email.headerregistry import Group
import pygame
import os
from states.content_loader import LOADER
from states.settings import * 

class Bullet(pygame.sprite.Sprite):
    def __init__(self, surface, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.surface = surface
        self.bullet_image = None
        self.speed = BULLET_SPEED
        self.direction = direction
        img = LOADER.get_bullet_image()
        img = pygame.transform.scale(img, (int(img.get_width()*BULLETS_SCALE), int(img.get_height()*BULLETS_SCALE))) 
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
 
    def update(self, screen_scroll, obstacle_list, targets, group):
        # move bullet
        self.rect.x += self.direction * self.speed + screen_scroll
        # check if bullet has gone off screen
        if self.rect.right < 0 or self.rect.left > self.surface.get_width():
            self.kill()

        # check for collision with level
        for tile in obstacle_list:
            if tile[1].colliderect(self.rect):
                self.kill()
        
        # check collision with characters
        for t in targets:
            if pygame.sprite.spritecollide(t, group, False):
                if t.alive:
                    t.health -= ENEMY_BULLET_HEALTH_DAMAGE
                    print(t.char_type, t.health)
                    self.kill()