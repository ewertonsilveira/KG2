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
        p, h, e = self.world.process_data(wd.world_data)

        self.player = p
        self.enemies = e
        self.health_bar = h

        self.item_box_group = pygame.sprite.Group()
        self.item_box_group.add(ItemBox(HEALTH, 20, GROUND))
        self.item_box_group.add(ItemBox(AMMO, 300, GROUND))
        self.item_box_group.add(ItemBox(GRENADE, 600, GROUND))

    def draw(self, surface):
        self.draw_bg(surface, COLORS.bgColor)
        pygame.draw.line(surface, COLORS.groundColor, (0, GROUND), (surface.get_width(), GROUND))

        for _, enemy in enumerate(self.enemies):
            enemy.ai(surface, self.player)
            enemy.draw(surface)            
            enemy.update(surface, [self.player])            
        
        self.player.draw(surface)
        self.player.update(surface, self.enemies)
        self.health_bar.draw(surface, self.player.health)

        self.item_box_group.update(self.player)
        self.item_box_group.draw(surface)

        # show ammo
        self.draw_text(surface, 'AMMO: ', FONTS.secondary_font, COLORS.WHITE, 10, 35)
        for x in range(self.player.ammo): surface.blit(GAME_IMAGES.get_bullet_image(), (80 + (x * 10), 40))

        # show grenades
        self.draw_text(surface, 'GRENADES:', FONTS.secondary_font, COLORS.WHITE, 10, 60)
        for x in range(self.player.grenade): surface.blit(GAME_IMAGES.get_grenade_image(), (125 + (x * 15), 60))

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
    
    def draw_text(self, surface, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        surface.blit(img, (x, y))
            
