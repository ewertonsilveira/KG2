from email.headerregistry import Group
import pygame
import os
import random

from states.shooting.bullet import Bullet

from states.settings import *
from states.shooting.soldier import Soldier 

class EnemySoldier(Soldier):
    def __init__(self, chart_type, x, y, health, scale, speed, direction, ammo, grenade):
        super(EnemySoldier, self).__init__(chart_type, x, y, health, scale, speed, direction, ammo, grenade)
        #ai specific variables
        self.move_counter = 0
        self.idling = False
        self.idling_counter = 0
        self.vision = pygame.Rect(0, 0, ENEMY_VISION_RANGE, 10)

    def ai(self, surface, obstacle_list, target):
        if not self.alive or not target.alive:
            # self.update_action(0) # idle
            return
        
        if self.idling == False and random.randint(1, 300) == 1:
            self.idling = True  
            self.idling_counter = 50
            self.update_action(0) # idle

        # shoot if player is in the range
        if self.vision.colliderect(target.rect):
            self.update_action(0) # idle
            self.shoot(surface)
        else:
            if self.idling == False:
                ai_move_right = True if self.direction == 1 else False
                ai_move_left = not ai_move_right
                self.move(obstacle_list, ai_move_left, ai_move_right)
                self.update_action(1) # run
                self.move_counter += 1

                #update ai vision as the enemy moves
                self.vision.center = (self.rect.centerx + 75 * self.direction, self.rect.centery)

                # move direction
                if self.move_counter > TILE_SIZE:
                    self.direction *= -1
                    self.move_counter *= -1
            else:                
                self.idling_counter -= 1
                if self.idling_counter <= 0:
                    self.idling = False


    def throw_grenade(self, surface):
        pass

    def update_ammo(self, value):
        pass
            
    def update_grenade(self, value): 
        pass