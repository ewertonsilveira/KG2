from email.headerregistry import Group
import pygame
import os
from states.gameImages import GAME_IMAGES
from states.settings import * 

class Bullet(pygame.sprite.Sprite):
    def __init__(self, surface, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.surface = surface
        self.bullet_image = None
        self.speed = BULLET_SPEED
        self.direction = direction
        self.image = GAME_IMAGES.get_bullet_image()
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def update(self, targets, group):
        # move bullet
        self.rect.x += self.direction * self.speed
        # check if bullet has gone off screen
        if self.rect.right < 0 or self.rect.left > self.surface.get_width():
            self.kill()

        # check collision with characters
        for t in targets:
            if pygame.sprite.spritecollide(t, group, False):
                if t.alive:
                    t.health -= ENEMY_BULLET_HEALTH_DAMAGE
                    print(t.char_type, t.health)
                    self.kill()