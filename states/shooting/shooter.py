from email.headerregistry import Group
import pygame
import os
from states.colors import COLORS
from states.fonts import FONTS
from states.game_images import GAME_IMAGES
from states.shooting.enemy_soldier import EnemySoldier
from states.shooting.health_bar import HealthBar

from states.shooting.item_box import HEALTH,AMMO, GRENADE, ItemBox
from states.shooting.level_loader import LEVEL_LOADER
from states.shooting.word import World


from ..base import BaseState
from .soldier import Soldier

from states.settings import *

class Shooter(BaseState):
    def __init__(self):
        super(Shooter, self).__init__()
        self.next_state = "MENU"
        self.enemies = []

        # Game levels
        self.level = 1

        # player action variables
        self.moving_left = False
        self.moving_right = False
        self.shoot = False
        self.grenade = False

        # create World
        self.world = World()

        wd = LEVEL_LOADER.get_level(self.level)
        self.world.process_data(wd.world_data)


    def draw(self, surface):
        self.draw_bg(surface, COLORS.bgColor)
        pygame.draw.line(surface, COLORS.groundColor, (0, GROUND), (surface.get_width(), GROUND))

        for _, enemy in enumerate(self.world.enemies):
            enemy.ai(surface, self.world.player)
            enemy.draw(surface)            
            enemy.update(surface, [self.world.player])            
        
        self.world.player.draw(surface)
        self.world.player.update(surface, self.world.enemies)
        self.world.health_bar.draw(surface, self.world.player.health)

        self.world.item_box_group.update(self.world.player)
        self.world.item_box_group.draw(surface)

        # show ammo
        self.draw_text(surface, 'AMMO: ', FONTS.secondary_font, COLORS.WHITE, 10, 35)
        for x in range(self.world.player.ammo): surface.blit(GAME_IMAGES.get_bullet_image(), (80 + (x * 10), 40))

        # show grenades
        self.draw_text(surface, 'GRENADES:', FONTS.secondary_font, COLORS.WHITE, 10, 60)
        for x in range(self.world.player.grenade): surface.blit(GAME_IMAGES.get_grenade_image(), (125 + (x * 15), 60))

        # update player action
        if self.world.player.alive:
            # shoot bullets
            if self.shoot:
                self.world.player.shoot(surface)
            elif self.grenade:
                self.world.player.throw_grenade(surface)

            # other player actions
            if self.world.player.in_air:
                self.world.player.update_action(2) #1 run
            elif self.moving_left or self.moving_right:
                self.world.player.update_action(1) #1 run
            else:
                self.world.player.update_action(0) #1 idle

            self.world.player.move(self.moving_left, self.moving_right)
        

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.shoot = True
            if event.key == pygame.K_q:
                self.grenade = True
            if (event.key == pygame.K_w or event.key == pygame.K_UP) and self.world.player.alive:
                self.world.player.jump = True
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
    
    def draw_text(self, surface, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        surface.blit(img, (x, y))
            
