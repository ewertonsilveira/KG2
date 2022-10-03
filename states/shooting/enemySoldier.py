from email.headerregistry import Group
import pygame
import os

from states.shooting.bullet import Bullet

from states.settings import *
from states.shooting.soldier import Soldier 

class EnemySoldier(Soldier):
    def __init__(self, chart_type, x, y, health, scale, speed, direction, ammo, grenade):
        super(EnemySoldier, self).__init__(chart_type, x, y, health, scale, speed, direction, ammo, grenade)
        #ai specific variables
        self.move_counter = 0

    def ai(self, target):
        if self.alive and target.alive:            
            ai_move_right = True if self.direction == 1 else False
            ai_move_left = not ai_move_right
            self.move(ai_move_left, ai_move_right)
            self.update_action(1)
            self.move_counter += 1

            if self.move_counter > TILE_SIZE:
                self.direction *= -1
                self.move_counter *= -1


    def throw_grenade(self, surface):
        pass

    def update_ammo(self, value):
        pass
            
    def update_grenade(self, value): 
        pass