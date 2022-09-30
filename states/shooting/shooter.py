from email.headerregistry import Group
import pygame
import os


from ..base import BaseState
from .character import Soldier

from states.settings import *

class Shooter(BaseState):
    def __init__(self):
        super(Shooter, self).__init__()
        self.next_state = "MENU"
        self.bgColor = (144,201,120)
        self.groundColor = (255, 0, 0)

        # player action variables
        self.moving_left = False
        self.moving_right = False
        self.shoot = False

        self.bullet_group = pygame.sprite.Group()

        self.player = Soldier("player", 200, GROUND, 100, 3, 5, 20 * 100)
        self.enemies = [Soldier("enemy", 300, GROUND, 20, 3, 5, 200 * 100)]


    def draw(self, surface):
        self.draw_bg(surface, self.bgColor)
        pygame.draw.line(surface, self.groundColor, (0, GROUND), (surface.get_width(), GROUND))

        for _, enemy in enumerate(self.enemies):
            enemy.draw(surface)
            enemy.update(surface, [self.player])
        
        self.player.draw(surface)
        self.player.update(surface, self.enemies)

        

        # update player action
        if self.player.alive:
            if self.shoot:
                self.player.shoot(surface)
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
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self.moving_left = True
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.moving_right = True


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self.moving_left = False
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.moving_right = False
            elif (event.key == pygame.K_w or event.key == pygame.K_UP) and self.player.alive:
                self.player.jump = True
            elif event.key == pygame.K_SPACE:
                self.shoot = False
            elif event.key == pygame.K_ESCAPE:
                self.done = True