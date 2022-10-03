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

    def ai(self, target):
        if self.alive and target.alive:
            if self.idling == False and random.randint(1, 300) == 1:
                self.idling = True
                self.idling_counter = 50
                self.update_action(0) # idle

            if self.idling == False:
                ai_move_right = True if self.direction == 1 else False
                ai_move_left = not ai_move_right
                self.move(ai_move_left, ai_move_right)
                self.update_action(1) # run
                self.move_counter += 1

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