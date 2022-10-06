from email.headerregistry import Group
import pygame
import os
from states.game_images import GAME_IMAGES
from states.settings import * 

HEALTH='health'
AMMO='ammo'
GRENADE='grenade'

class ItemBox(pygame.sprite.Sprite):
    def __init__(self, item_type, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.item_type = item_type
        item_boxes = {
            HEALTH   : GAME_IMAGES.get_health_box_image(),
            AMMO      : GAME_IMAGES.get_ammo_box_image(),
            GRENADE   : GAME_IMAGES.get_grenade_box_image()
        }
        self.image = item_boxes[self.item_type]
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y - (TILE_SIZE - self.image.get_height()))


    def update(self, target):
        # check if the player has picked up the box
        if pygame.sprite.collide_rect(self, target):
            # check the type of item
            if self.item_type == HEALTH:
                target.update_health(ITEM_BOX_HEALTH)
            elif self.item_type == AMMO: 
                target.update_ammo(ITEM_BOX_AMMO)
            elif self.item_type == GRENADE:
                target.update_grenade(ITEM_BOX_GRENADE)
            
            # remove item
            self.kill()
