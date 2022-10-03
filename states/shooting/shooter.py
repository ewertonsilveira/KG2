from email.headerregistry import Group
import pygame
import os

from states.shooting.itemBox import HEALTH,AMMO, GRENADE, ItemBox


from ..base import BaseState
from .soldier import Soldier

from states.settings import *

class Shooter(BaseState):
    def __init__(self):
        super(Shooter, self).__init__()
        self.next_state = "MENU"
        self.bgColor = (144,201,120)
        self.groundColor = (255, 0, 0)
        self.enemies = []

        # player action variables
        self.moving_left = False
        self.moving_right = False
        self.shoot = False
        self.grenade = False

        self.item_box_group = pygame.sprite.Group()

        self.create_player()
        self.create_enemies()

        self.item_box_group.add(ItemBox(HEALTH, 100, GROUND))
        self.item_box_group.add(ItemBox(AMMO, 300, GROUND))
        self.item_box_group.add(ItemBox(GRENADE, 600, GROUND))

    def draw(self, surface):
        self.draw_bg(surface, self.bgColor)
        pygame.draw.line(surface, self.groundColor, (0, GROUND), (surface.get_width(), GROUND))

        for _, enemy in enumerate(self.enemies):
            enemy.draw(surface)
            enemy.update(surface, [self.player])            
        
        self.player.draw(surface)
        self.player.update(surface, self.enemies)

        self.item_box_group.update(self.player)
        self.item_box_group.draw(surface)

        # update player action
        if self.player.alive:
            # shoot bullets
            if self.shoot:
                self.player.shoot(surface)
            elif self.grenade:
                self.player.throw_grenade(surface)

            # other player actions
            if self.player.in_air:
                self.player.update_action(2) #1 run
            elif self.moving_left or self.moving_right:
                self.player.update_action(1) #1 run
            else:
                self.player.update_action(0) #1 idle

            self.player.move(self.moving_left, self.moving_right)
        

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.shoot = True
            if event.key == pygame.K_q:
                self.grenade = True
            if (event.key == pygame.K_w or event.key == pygame.K_UP) and self.player.alive:
                self.player.jump = True
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self.moving_left = True
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.moving_right = True


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.shoot = False
            if event.key == pygame.K_q:
                self.grenade = False
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self.moving_left = False
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.moving_right = False
            if event.key == pygame.K_ESCAPE:
                self.done = True
            
    def create_enemies(self):
        self.enemies.append(Soldier("enemy", self.screen_rect.right * 0.4, GROUND * 1.1, ENEMY_BASE_HEALTH, 3, 5, -1, ENEMY_INITIAL_BULLETS, ENEMY_INITIAL_GRENADES))
        self.enemies.append(Soldier("enemy", self.screen_rect.right * 0.8, GROUND -50, ENEMY_BASE_HEALTH, 3, 5, -1, ENEMY_INITIAL_BULLETS, ENEMY_INITIAL_GRENADES))

    def create_player(self):
        self.player = Soldier("player", 200, GROUND, SOLDIER_BASE_HEALTH, 3, 5, 1, SOLDIER_INITIAL_BULLETS, SOLDIER_INITIAL_GRENADES)
